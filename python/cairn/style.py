"""Parameterised exposition styles.

A :class:`Style` says how to organise a chapter's statement/proof events (see :mod:`cairn.events`):

``top_down`` (0..1)
    Position on the bottom-up <-> top-down curve: the share of eligible results (those whose proof uses
    other results in the chapter) that are *goals*. A goal is stated before the material its proof needs
    and proved after it. Everything else is built bottom-up with its proof straight after its statement.
``roadmap`` ("none" | "chapter" | "document")
    Announce main results early and prove them later. "chapter": each chapter opens by stating its main
    results (those nothing else in the chapter uses) and proves them last. "document": an overview at the
    start of the document states every chapter's main results, which are then proved in their own
    chapters (Carleson's overview device).
``definitions`` ("just-in-time" | "upfront")
    Introduce each definition just before its first use ("definitions in the middle") or collect them
    at the start of the chapter.
``goal_rule`` ("fan-in" | "support" | "key")
    How goals are ranked for ``top_down``: by how many results their proof uses, by how much of the
    chapter they depend on (transitively), or by the Phase 2 key-declaration score.

:func:`arrange` produces a valid event order for any style; :func:`sweep` and :func:`fit` evaluate styles
against a human blueprint.
"""

from __future__ import annotations

import itertools
import random
import statistics
from dataclasses import asdict, dataclass

import networkx as nx

from .events import P, S, motivated_share, node_of, prior_statements
from .graph import kendall_tau, make_dag, order_metrics

GOAL_RULES = ("fan-in", "support", "key")
ROADMAPS = ("none", "chapter", "document")
DEFINITIONS = ("just-in-time", "upfront")


@dataclass(frozen=True)
class Style:
    top_down: float = 0.0
    roadmap: str = "none"
    definitions: str = "just-in-time"
    goal_rule: str = "fan-in"

    def label(self) -> str:
        parts = [f"top_down={self.top_down:g}"]
        if self.roadmap != "none":
            parts.append(f"{self.roadmap} roadmap")
        if self.definitions != "just-in-time":
            parts.append(f"definitions={self.definitions}")
        if self.goal_rule != "fan-in":
            parts.append(f"goals by {self.goal_rule}")
        return ", ".join(parts)


def _shuffled(items, rng: random.Random) -> list:
    items = sorted(items)
    rng.shuffle(items)
    return items


def rank_goal_candidates(g: nx.DiGraph, rule: str, key: dict[str, float] | None = None) -> list[str]:
    """Results whose proof uses at least one other result here, most goal-like first."""
    nodes = {node_of(e) for e in g}
    uses = {v: {node_of(p) for p in g.predecessors(P(v))} - {v} for v in nodes if P(v) in g}
    candidates = [v for v, u in uses.items() if u]
    if rule == "fan-in":
        score = {v: len(uses[v]) for v in candidates}
    elif rule == "support":
        score = {v: len({node_of(a) for a in nx.ancestors(g, P(v))} - {v}) for v in candidates}
    elif rule == "key":
        if key is None:
            raise ValueError("goal_rule='key' needs key scores")
        score = {v: key.get(v, 0.0) for v in candidates}
    else:
        raise ValueError(f"goal_rule must be one of {GOAL_RULES}")
    return sorted(candidates, key=lambda v: (-score[v], v))


def arrange(g: nx.DiGraph, style: Style, rng: random.Random, key: dict[str, float] | None = None) -> list[str]:
    """A valid order of the events of ``g`` (one chapter, acyclic) in the given style."""
    ranked = rank_goal_candidates(g, style.goal_rule, key)
    goals = set(ranked[: round(style.top_down * len(ranked))])
    finals = [node_of(e) for e in g if e.startswith("S:")
              and not any(node_of(w) != node_of(e) for w in g.successors(e))]
    if style.roadmap not in ROADMAPS:
        raise ValueError(f"roadmap must be one of {ROADMAPS}")
    if style.roadmap == "chapter":
        goals |= {v for v in finals if P(v) in g}

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

    def state(v: str) -> None:
        """Make ``S:v`` (and whatever its statement needs); for a non-goal also prove it."""
        if S(v) in done or v in active:
            return
        if v in goals:
            active.add(v)
            for u in needs(S(v), v):
                place(u)
            emit(S(v))
            active.discard(v)
        else:
            place(v)

    def place(v: str) -> None:
        if v in active or ((S(v) not in g or S(v) in done) and (P(v) not in g or P(v) in done)):
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

    if style.definitions == "upfront":
        defs = [node_of(e) for e in g if e.startswith("S:") and g.nodes[e].get("result") == "definition"]
        for v in nx.topological_sort(g.subgraph([S(d) for d in defs])):
            place(node_of(v))
    elif style.definitions != "just-in-time":
        raise ValueError(f"definitions must be one of {DEFINITIONS}")
    order_finals = _shuffled(finals, rng)
    if style.roadmap == "chapter":
        for v in order_finals:  # announce the chapter's main results
            state(v)
    for v in order_finals:
        place(v)
    for e in _shuffled([e for e in g if e not in done], rng):
        place(node_of(e))
    return out


# --- evaluation against a human blueprint ---------------------------------------------------


def chapter_scopes(g: nx.DiGraph, human: list[str], min_nodes: int = 8) -> dict[str, list[str]]:
    chapter = nx.get_node_attributes(g, "chapter")
    out = {}
    for ch in dict.fromkeys(chapter[e] for e in human):
        members = [e for e in human if chapter[e] == ch]
        if len({node_of(e) for e in members}) >= min_nodes:
            out[ch] = members
    return out


def evaluate_style(g: nx.DiGraph, human: list[str], style: Style, runs: int = 5, seed: int = 0,
                   key: dict[str, float] | None = None) -> dict:
    """Chapter-averaged τ with the human order, motivated share and mean open for one style."""
    rng = random.Random(seed)
    rows = []
    for h in chapter_scopes(g, human).values():
        dag, _ = make_dag(g.subgraph(h).copy(), h)
        prior = prior_statements(human, h)
        for _ in range(runs):
            o = arrange(dag, style, rng, key)
            rows.append((kendall_tau(h, o), motivated_share(g, o, prior), order_metrics(dag, o).mean_open))
    return {"tau": statistics.fmean(r[0] for r in rows), "motivated": statistics.fmean(r[1] for r in rows),
            "mean_open": statistics.fmean(r[2] for r in rows)}


def human_profile(g: nx.DiGraph, human: list[str]) -> dict:
    rows = []
    for h in chapter_scopes(g, human).values():
        dag, _ = make_dag(g.subgraph(h).copy(), h)
        rows.append((motivated_share(g, h, prior_statements(human, h)), order_metrics(dag, h).mean_open))
    return {"tau": 1.0, "motivated": statistics.fmean(r[0] for r in rows),
            "mean_open": statistics.fmean(r[1] for r in rows)}


def sweep(g: nx.DiGraph, human: list[str], key: dict[str, float] | None = None,
          top_down=(0, 0.2, 0.4, 0.6, 0.8, 1.0), runs: int = 5) -> list[dict]:
    rules = [r for r in GOAL_RULES if r != "key" or key is not None]
    out = []
    for td, roadmap, defs, rule in itertools.product(top_down, ("none", "chapter"), DEFINITIONS, rules):
        if td == 0 and rule != "fan-in":
            continue  # goal rule is irrelevant without goals
        st = Style(td, roadmap, defs, rule)
        out.append({"style": asdict(st), "label": st.label(), **evaluate_style(g, human, st, runs, key=key)})
    return out


def fit(results: list[dict], human: dict) -> dict:
    """Best style by τ, and closest style to the human (motivated, load) profile."""
    best_tau = max(results, key=lambda r: r["tau"])
    span_m = max(r["motivated"] for r in results) - min(r["motivated"] for r in results) or 1
    span_o = max(r["mean_open"] for r in results) - min(r["mean_open"] for r in results) or 1

    def dist(r):
        dm = (r["motivated"] - human["motivated"]) / span_m
        do = (r["mean_open"] - human["mean_open"]) / span_o
        return dm**2 + do**2

    return {"best_tau": best_tau, "closest_profile": min(results, key=dist)}


# --- whole documents -------------------------------------------------------------------------


def home_chapters(g: nx.DiGraph) -> dict[str, str]:
    """Each result's home chapter: where its proof sits (or its statement, if it has no proof)."""
    return {node_of(e): g.nodes[P(node_of(e))]["chapter"] if P(node_of(e)) in g else g.nodes[e]["chapter"]
            for e in g if e.startswith("S:")}


def arrange_document(g: nx.DiGraph, chapter_order: list[str], style: Style, rng: random.Random,
                     key: dict[str, float] | None = None) -> list[str]:
    """Arrange a whole document: chapters in ``chapter_order`` (by home chapter), each in ``style``.

    With ``roadmap="document"`` an overview first states every chapter's main results (and, as
    statements only, whatever their statements need); their proofs stay in their chapters.
    """
    home = home_chapters(g)
    members = {ch: [e for e in g if home[node_of(e)] == ch] for ch in chapter_order}
    out: list[str] = []
    done: set[str] = set()
    if style.roadmap == "document":
        def announce(v: str) -> None:
            if S(v) in done:
                return
            for p in sorted(g.predecessors(S(v))):
                announce(node_of(p))
            done.add(S(v))
            out.append(S(v))

        for ch in chapter_order:
            sub = g.subgraph(members[ch])
            for e in _shuffled([e for e in sub if e.startswith("S:")
                                and not any(node_of(w) != node_of(e) for w in sub.successors(e))], rng):
                announce(node_of(e))
    local = Style(style.top_down, "none" if style.roadmap == "document" else style.roadmap,
                  style.definitions, style.goal_rule)
    for ch in chapter_order:
        rest = [e for e in members[ch] if e not in done]
        if not rest:
            continue
        for e in arrange(g.subgraph(rest).copy(), local, rng, key):
            done.add(e)
            out.append(e)
    return out


def evaluate_document(g: nx.DiGraph, human: list[str], style: Style, runs: int = 5, seed: int = 0,
                      key: dict[str, float] | None = None) -> dict:
    """Whole-document τ, motivated share and mean open; chapters in the human order of home chapters."""
    home = home_chapters(g)
    chapter_order = list(dict.fromkeys(
        home[node_of(e)] for e in human if e.startswith("P:") or P(node_of(e)) not in g))
    chapter_order += [c for c in dict.fromkeys(home.values()) if c not in chapter_order]
    dag, _ = make_dag(g, human)
    rng = random.Random(seed)
    rows = []
    for _ in range(runs):
        o = arrange_document(dag, chapter_order, style, rng, key)
        rows.append((kendall_tau(human, o), motivated_share(dag, o), order_metrics(dag, o).mean_open))
    return {"tau": statistics.fmean(r[0] for r in rows), "motivated": statistics.fmean(r[1] for r in rows),
            "mean_open": statistics.fmean(r[2] for r in rows)}


def document_profile(g: nx.DiGraph, human: list[str]) -> dict:
    dag, _ = make_dag(g, human)
    return {"tau": 1.0, "motivated": motivated_share(dag, human), "mean_open": order_metrics(dag, human).mean_open}


def document_sweep(g: nx.DiGraph, human: list[str], top_down=(0, 0.2, 0.4, 0.6, 0.8, 1.0),
                   runs: int = 5) -> list[dict]:
    out = []
    for td, roadmap in itertools.product(top_down, ROADMAPS):
        st = Style(td, roadmap)
        out.append({"style": asdict(st), "label": st.label(), **evaluate_document(g, human, st, runs)})
    return out


def node_key_scores(bp, decls) -> dict[str, float]:
    """Key-declaration score of each blueprint node: the max over its Lean declarations (out-of-fold)."""
    from .formal import join_blueprint
    from .phase2 import key_scores

    ks = key_scores(bp, decls)
    join = join_blueprint(bp, decls)
    return {v: max(ks.get(d, 0.0) for d in ds) for v, ds in join.node_decls.items()}


def run(bp, decls, out_dir, project: str, provenance: str = "", runs: int = 5) -> dict:
    import json
    from pathlib import Path

    from .events import event_graph

    g, human = event_graph(bp, decls)
    key = node_key_scores(bp, decls)
    results = sweep(g, human, key, runs=runs)
    prof = human_profile(g, human)
    doc = document_sweep(g, human, runs=runs)
    doc_prof = document_profile(g, human)
    res = {"project": project, "provenance": provenance, "human": prof, "fit": fit(results, prof),
           "results": results, "document": {"human": doc_prof, "fit": fit(doc, doc_prof), "results": doc}}
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "style.json").write_text(json.dumps(res, indent=2))
    lines = [f"# Style sweep: {project}", "", f"*{provenance}*", "",
             "Chapter averages over chapters with at least 8 results; 5 arrangements per style. τ = Kendall "
             "correlation with the human event order; motivated = lemmas stated after a goal they serve; "
             "mean open = working-memory load (lower is better).", "",
             f"**Human:** motivated {prof['motivated']:.0%}, mean open {prof['mean_open']:.2f}.", "",
             f"**Best τ:** {res['fit']['best_tau']['label']} (τ {res['fit']['best_tau']['tau']:+.2f}).", "",
             f"**Closest (motivated, load) profile:** {res['fit']['closest_profile']['label']} "
             f"(motivated {res['fit']['closest_profile']['motivated']:.0%}, "
             f"mean open {res['fit']['closest_profile']['mean_open']:.2f}, "
             f"τ {res['fit']['closest_profile']['tau']:+.2f}).",
             "", "| Style | τ | motivated | mean open |", "|---|---:|---:|---:|"]
    for r in sorted(results, key=lambda r: -r["tau"]):
        lines.append(f"| {r['label']} | {r['tau']:+.2f} | {r['motivated']:.0%} | {r['mean_open']:.2f} |")
    d = res["document"]
    lines += ["", "## Whole document", "",
              "Chapters kept intact, in the human order of each result's home chapter (where it is proved). "
              "Every promise counts, including goals announced in one chapter and proved in another.", "",
              f"**Human:** motivated {d['human']['motivated']:.0%}, mean open {d['human']['mean_open']:.1f}. "
              f"**Closest profile:** {d['fit']['closest_profile']['label']} (motivated "
              f"{d['fit']['closest_profile']['motivated']:.0%}, "
              f"mean open {d['fit']['closest_profile']['mean_open']:.1f}).",
              "", "| Style | τ | motivated | mean open |", "|---|---:|---:|---:|"]
    for r in d["results"]:
        lines.append(f"| {r['label']} | {r['tau']:+.2f} | {r['motivated']:.0%} | {r['mean_open']:.1f} |")
    (out_dir / "style.md").write_text("\n".join(lines) + "\n")
    return res
