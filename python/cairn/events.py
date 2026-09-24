"""Statement/proof event model of an exposition.

A blueprint node is two events: its statement ``S:v`` and (if it has one) its proof ``P:v``. Reading
constraints:

- ``S:v`` before ``P:v``;
- if ``v``'s *statement* mentions ``u``, then ``S:u`` before ``S:v``;
- if only ``v``'s *proof* uses ``u``, then ``S:u`` before ``P:v``. The proof of ``u`` may come later: a
  *deferred proof*, as in "state the goal, prove the lemmas it needs, then prove the goal".

Statement vs proof use comes from Lean (a dependency in the declaration's type vs only in its value),
because blueprints put ``\\uses`` inconsistently (Carleson puts proof dependencies in statements).

Under this model the metrics of :mod:`cairn.graph` apply unchanged to event sequences. A deferred proof
is charged as an open item from ``S:v`` to ``P:v`` through the ``S:v -> P:v`` edge, and a forward reference
means a genuine use-before-statement.
"""

from __future__ import annotations

import random

import networkx as nx

from .blueprint import Blueprint
from .formal import FormalDecl, formal_graph, join_blueprint, projected_graph


def S(v: str) -> str:  # noqa: N802 - mathematical notation
    return f"S:{v}"


def P(v: str) -> str:  # noqa: N802
    return f"P:{v}"


def node_of(event: str) -> str:
    return event[2:]


def event_graph(bp: Blueprint, decls: dict[str, FormalDecl]) -> tuple[nx.DiGraph, list[str]]:
    """Event graph over formalised blueprint nodes, and the human event order."""
    join = join_blueprint(bp, decls)
    nodes = [n.id for n in bp.nodes if n.id in join.node_decls]
    by_id = bp.by_id()
    statement = projected_graph(bp, formal_graph(decls, include_value=False), join).subgraph(nodes)
    full = projected_graph(bp, formal_graph(decls), join).subgraph(nodes)
    g = nx.DiGraph()
    for v in nodes:
        n = by_id[v]
        g.add_node(S(v), chapter=n.chapter, kind="statement", result=n.kind)
        if n.has_proof:
            g.add_node(P(v), chapter=n.proof_chapter or n.chapter, kind="proof")
            g.add_edge(S(v), P(v))
    for u, v in full.edges:
        if statement.has_edge(u, v) or not by_id[v].has_proof:
            g.add_edge(S(u), S(v))
        else:
            g.add_edge(S(u), P(v))
    events = [(by_id[v].statement_event, S(v)) for v in nodes]
    events += [(by_id[v].proof_event, P(v)) for v in nodes if by_id[v].has_proof]
    human = [e for _, e in sorted(events)]
    return g, human


def classify_edges(g: nx.DiGraph, order: list[str]) -> dict[str, int]:
    """Count edges by how the order treats them."""
    pos = {e: i for i, e in enumerate(order)}
    out = {"backward": 0, "deferred proofs (S before a later P)": 0, "genuine forward references": 0}
    for u, v in g.edges:
        if pos[u] > pos[v]:
            out["genuine forward references"] += 1
        elif u[:2] == "S:" and v == P(node_of(u)) and pos[v] - pos[u] > 1:
            out["deferred proofs (S before a later P)"] += 1
        else:
            out["backward"] += 1
    return out


def deferred_goal_first_order(g: nx.DiGraph, rng: random.Random) -> list[str]:
    """Top-down with deferred proofs: state a goal, then (depth-first) state and prove what its proof
    needs, then prove the goal. Statement prerequisites are handled before a statement is made. Always a
    valid event order."""
    out: list[str] = []
    done: set[str] = set()
    active: set[str] = set()  # guards against the few cycles in projected graphs

    def emit(e: str) -> None:
        if e in done or e in active:
            return
        active.add(e)
        # everything this event needs first (statements only reach statements; P needs S and proof deps)
        for pre in _shuffled([p for p in g.predecessors(e) if p not in done and p not in active], rng):
            if pre.startswith("S:"):
                state_and_prove(node_of(pre))
            else:
                emit(pre)
        active.discard(e)
        if e not in done:
            done.add(e)
            out.append(e)

    def state_and_prove(v: str) -> None:
        emit(S(v))
        if P(v) in g and P(v) not in done:
            emit(P(v))

    finals = [node_of(e) for e in g if e.startswith("S:")
              and not any(node_of(w) != node_of(e) for w in g.successors(e))]
    for v in _shuffled(finals, rng):
        state_and_prove(v)
    for e in _shuffled([e for e in g if e not in done], rng):  # anything unreachable from a final result
        emit(e)
    return out


def bottom_up_order(g: nx.DiGraph, rng: random.Random) -> list[str]:
    """Just-in-time bottom-up: before a goal is stated, state *and prove* everything its statement and
    proof need; each proof immediately follows its statement."""
    out: list[str] = []
    done: set[str] = set()
    active: set[str] = set()

    def complete(v: str) -> None:
        if v in active:
            return
        active.add(v)
        own = [e for e in (S(v), P(v)) if e in g and e not in done]
        needed = {node_of(p) for e in own for p in g.predecessors(e) if node_of(p) != v and p not in done}
        for u in _shuffled(needed, rng):  # finish everything v's statement *and* proof need first
            complete(u)
        for e in own:
            done.add(e)
            out.append(e)
        active.discard(v)

    finals = [node_of(e) for e in g if e.startswith("S:")
              and not any(node_of(w) != node_of(e) for w in g.successors(e))]
    for v in _shuffled(finals, rng):
        complete(v)
    for e in _shuffled([e for e in g if e not in done], rng):
        complete(node_of(e))
    return out


def hybrid_order(g: nx.DiGraph, goals: set[str], rng: random.Random) -> list[str]:
    """State goals first and defer their proofs; build everything else bottom-up.

    For a goal ``v``: place what its *statement* needs, state it, place what its *proof* needs (nested goals
    are again stated first), then prove it. For any other result: place everything its statement and proof
    need, then state and immediately prove it. ``goals = all`` gives a fully top-down exposition,
    ``goals = {}`` the bottom-up one. Always a valid event order (up to cycles in the input).
    """
    out: list[str] = []
    done: set[str] = set()
    active: set[str] = set()

    def emit(e: str) -> None:
        if e in g and e not in done:
            done.add(e)
            out.append(e)

    def needs(e: str, v: str) -> list[str]:
        if e not in g:
            return []
        return _shuffled({node_of(p) for p in g.predecessors(e) if node_of(p) != v and p not in done}, rng)

    def place(v: str) -> None:
        if v in active or (S(v) in done and (P(v) not in g or P(v) in done)):
            return
        active.add(v)
        if v in goals:
            for u in needs(S(v), v):
                place(u)
            emit(S(v))
            for u in needs(P(v), v):
                place(u)
        else:
            for u in sorted(set(needs(S(v), v)) | set(needs(P(v), v))):
                place(u)
            emit(S(v))
        emit(P(v))
        active.discard(v)

    finals = [node_of(e) for e in g if e.startswith("S:")
              and not any(node_of(w) != node_of(e) for w in g.successors(e))]
    for v in _shuffled(finals, rng):
        place(v)
    for e in _shuffled([e for e in g if e not in done], rng):
        place(node_of(e))
    return out


def goals_by_fan_in(g: nx.DiGraph, m: int) -> set[str]:
    """Label-free goal rule: results whose proof needs at least ``m`` other results."""
    return {node_of(e) for e in g if e.startswith("P:")
            and len({node_of(p) for p in g.predecessors(e)} - {node_of(e)}) >= m}


def _shuffled(items, rng: random.Random) -> list:
    items = sorted(items)
    rng.shuffle(items)
    return items


# --- analysis ------------------------------------------------------------------


def motivated_share(g: nx.DiGraph, order: list[str], prior: set[str] | frozenset = frozenset()) -> float:
    """Share of supporting results stated *after* the statement of some result that uses them, i.e. the
    reader has already seen a goal the lemma serves ("no node before the goal it serves").

    ``g`` may be the whole event graph and ``order`` one chapter; statements in ``prior`` (earlier chapters)
    count as already made, so a goal announced in an overview section motivates the lemmas proving it.
    """
    pos = {e: i for i, e in enumerate(order)}
    supporting = motivated = 0
    for e in order:
        if not e.startswith("S:"):
            continue
        v = node_of(e)
        users = {node_of(w) for w in g.successors(e) if node_of(w) != v}
        users = {w for w in users if S(w) in pos or S(w) in prior}
        if not users:
            continue
        supporting += 1
        motivated += any(S(w) in prior or pos[S(w)] < pos[e] for w in users)
    return motivated / supporting if supporting else 0.0


def prior_statements(human: list[str], scope: list[str]) -> set[str]:
    """Statements made (in the human document) before the scope's first event and outside it."""
    first = min(human.index(e) for e in scope)
    inside = set(scope)
    return {e for e in human[:first] if e.startswith("S:") and e not in inside}



def analyse(bp: Blueprint, decls: dict[str, FormalDecl], samples: int = 1000, seed: int = 0,
            min_chapter_nodes: int = 8) -> dict:
    """Human event order vs random valid event orders and two constructive styles, per scope."""
    import statistics

    from .graph import kendall_tau, make_dag, order_metrics, random_topological_order
    from .phase0 import _quantile, analyse_scope

    g, human = event_graph(bp, decls)
    scopes = {"(whole blueprint)": human}
    chapter = nx.get_node_attributes(g, "chapter")
    for ch in dict.fromkeys(chapter[e] for e in human):
        members = [e for e in human if chapter[e] == ch]
        if len({node_of(e) for e in members}) >= min_chapter_nodes:
            scopes[ch] = members
    out = {"edges": classify_edges(g, human), "scopes": {}}
    for name, h in scopes.items():
        sub = g.subgraph(h).copy()
        prior = prior_statements(human, h)
        base = analyse_scope(name, sub, h, samples=samples, seed=seed, uniform_samples=100)
        dag, _ = make_dag(sub, h)
        rng = random.Random(seed)
        styles = {"top-down, deferred proofs": [deferred_goal_first_order(dag, rng) for _ in range(20)],
                  "bottom-up, proofs immediately": [bottom_up_order(dag, rng) for _ in range(20)]}
        row = {
            "events": len(h),
            "edges": classify_edges(sub, h),
            "human_mean_open": base.orders["human"].mean_open,
            "optimised_mean_open": base.orders["optimised"].mean_open,
            "uniform_median_mean_open": _quantile(base.uniform["mean_open"], 0.5),
            "share_uniform_better": base.percentile("human", "mean_open", "uniform"),
            "tau_random": statistics.fmean(base.random_tau_vs_human),
            "tau_optimised": base.tau_vs_human["optimised"],
            "human_motivated": motivated_share(g, h, prior),
            "random_motivated": statistics.fmean(
                motivated_share(g, random_topological_order(dag, rng), prior) for _ in range(100)),
        }
        for m in (1, 2, 3, 4, 6):
            goals = goals_by_fan_in(dag, m)
            styles[f"hybrid, goals = proofs using >= {m} results"] = [hybrid_order(dag, goals, rng) for _ in range(20)]
        for style, runs in styles.items():
            row[style] = {
                "tau": statistics.fmean(kendall_tau(h, o) for o in runs),
                "mean_open": statistics.fmean(order_metrics(sub, o).mean_open for o in runs),
                "motivated": statistics.fmean(motivated_share(g, o, prior) for o in runs),
            }
        out["scopes"][name] = row
    return out


def write_report(res: dict, out_dir, project: str, provenance: str) -> None:
    import json
    from pathlib import Path

    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "events.json").write_text(json.dumps({"project": project, "provenance": provenance, **res},
                                                    indent=2))
    e = res["edges"]
    td, bu = "top-down, deferred proofs", "bottom-up, proofs immediately"
    lines = [
        f"# Statement/proof events: {project}",
        "",
        f"*{provenance}*",
        "",
        "Each blueprint node is a statement event and a proof event; a proof may use any result already "
        "*stated*, so stating a goal and proving it after its lemmas is not a forward reference. Edge kinds "
        "(statement vs proof use) come from Lean.",
        "",
        f"Whole blueprint: {e['backward']} backward edges, {e['deferred proofs (S before a later P)']} deferred "
        f"proofs, {e['genuine forward references']} genuine forward references.",
        "",
        "**Motivated** = share of supporting results stated after the statement of a result that uses them "
        "(the reader has seen the goal a lemma serves). **Mean open** = the Phase 0 working-memory proxy on the "
        "event sequence (lower is better).",
        "",
        "| Scope | motivated: human | random | top-down (deferred) | bottom-up | mean open: human | random "
        "(uniform median) | top-down (deferred) | bottom-up |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for name, r in res["scopes"].items():
        lines.append(
            f"| {name} | {r['human_motivated']:.0%} | {r['random_motivated']:.0%} | {r[td]['motivated']:.0%} | "
            f"{r[bu]['motivated']:.0%} | {r['human_mean_open']:.1f} | {r['uniform_median_mean_open']:.1f} | "
            f"{r[td]['mean_open']:.1f} | {r[bu]['mean_open']:.1f} |"
        )
    lines += [
        "",
        "## Hybrid styles: state a goal first (deferring its proof) iff its proof uses at least m results",
        "",
        "| Scope | style | τ with human | motivated | mean open |",
        "|---|---|---:|---:|---:|",
    ]
    for name, r in res["scopes"].items():
        lines.append(f"| {name} | human | +1.00 | {r['human_motivated']:.0%} | {r['human_mean_open']:.1f} |")
        for style in [k for k in r if k.startswith(("top-down", "bottom-up", "hybrid"))]:
            x = r[style]
            lines.append(f"| | {style} | {x['tau']:+.2f} | {x['motivated']:.0%} | {x['mean_open']:.1f} |")
    lines += [
        "",
        "## Detail",
        "",
        "Mean open = the Phase 0 working-memory proxy on the event sequence; a deferred proof counts as open "
        "from its statement to its proof. τ = Kendall correlation with the human event order.",
        "",
        "| Scope | events | deferred proofs | genuine fwd refs | human mean open | uniform median | uniform orders "
        "better | optimum | τ random | τ top-down (deferred) | τ bottom-up |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for name, r in res["scopes"].items():
        lines.append(
            f"| {name} | {r['events']} | {r['edges']['deferred proofs (S before a later P)']} | "
            f"{r['edges']['genuine forward references']} | {r['human_mean_open']:.1f} | "
            f"{r['uniform_median_mean_open']:.1f} | {r['share_uniform_better']:.0%} | {r['optimised_mean_open']:.1f} | "
            f"{r['tau_random']:+.2f} | {r[td]['tau']:+.2f} | {r[bu]['tau']:+.2f} |"
        )
    lines.append("")
    (out_dir / "events.md").write_text("\n".join(lines))
