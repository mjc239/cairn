"""LLM ordering baseline over statement/proof events.

Unlike the node-level baseline in :mod:`cairn.phase2`, the model orders ``S:<id>`` (state) and ``P:<id>``
(prove) separately, so it can state a goal, develop lemmas, and prove the goal later. Prompts and
responses are files, so any model or API can fill them in. Scoring compares against the human event order
and against the node-level LLM runs (recast as events with each proof straight after its statement).
"""

from __future__ import annotations

import json
import random
import statistics
from pathlib import Path

import networkx as nx

from .blueprint import Blueprint
from .events import P, S, event_graph, goals_by_fan_in, hybrid_order, motivated_share, node_of, prior_statements
from .formal import FormalDecl
from .graph import kendall_tau, make_dag, nearest_topological_order, order_metrics
from .phase2 import _REF_RE

EVENT_INSTRUCTIONS = """You are organising one chapter of a mathematical exposition. Below are its results
(definitions, lemmas, propositions, theorems), in an arbitrary order, each with an id and its statement.

You decide the order of two kinds of step:
- `S:<id>` means *state* the result;
- `P:<id>` means *prove* it.
Each result says which of its steps belong to this chapter; include exactly those.

You may prove a result immediately after stating it, or state it early (for instance, announce the goal of
the chapter first) and prove it later, once the lemmas its proof needs have been developed. Whichever you
choose, respect every constraint below. A proof may use any result that has already been *stated*, even if
that result's own proof comes later.

Choose the order that makes the chapter clearest for a mathematician reading it for the first time.

Reply with only a JSON array containing every step exactly once, in your chosen order,
e.g. ["S:a", "S:b", "P:b", "P:a"]."""


def chapters_of(bp: Blueprint, g: nx.DiGraph, human: list[str], min_size: int = 8) -> dict[str, list[str]]:
    chapter = nx.get_node_attributes(g, "chapter")
    out = {}
    for ch in dict.fromkeys(chapter[e] for e in human):
        members = [e for e in human if chapter[e] == ch]
        if len({node_of(e) for e in members}) >= min_size:
            out[ch] = members
    return out


def core_events(g: nx.DiGraph, events: list[str]) -> list[str]:
    """Events of results whose statement and proof (if any) both belong to this chapter."""
    here = set(events)
    return [e for e in events if S(node_of(e)) in here and (P(node_of(e)) not in g or P(node_of(e)) in here)]


def write_event_prompts(bp: Blueprint, decls: dict[str, FormalDecl], out_dir: Path, seed: int = 0,
                        anonymise: bool = False, titles: bool = True, min_size: int = 8) -> list[Path]:
    g, human = event_graph(bp, decls)
    dag, _ = make_dag(g, human)
    by_id = bp.by_id()
    rng = random.Random(seed)
    out_dir.mkdir(parents=True, exist_ok=True)
    paths = []
    for ch, events in chapters_of(bp, g, human, min_size).items():
        nodes = list(dict.fromkeys(node_of(e) for e in events))
        rng.shuffle(nodes)
        if anonymise:
            alias = {v: f"r{c}" for v, c in zip(nodes, rng.sample(range(100, 1000), len(nodes)), strict=True)}
            labels = {lab: alias[v] for v in nodes for lab in by_id[v].labels}
            (out_dir / f"{ch}.ids.json").write_text(json.dumps({a: v for v, a in alias.items()}, indent=1))
        else:
            alias, labels = {v: v for v in nodes}, None

        def text_of(n, labels=labels):
            if labels is None:
                return n.text
            return _REF_RE.sub(lambda m: ", ".join(
                f"`{labels[x.strip()]}`" if x.strip() in labels else "[another result]"
                for x in m.group(1).split(",")), n.text)

        lines = [EVENT_INSTRUCTIONS, "", "## Results", ""]
        for v in nodes:
            n = by_id[v]
            title = f" ({n.title})" if n.title and titles else ""
            here = set(events)
            if S(v) in here and P(v) in here:
                steps = "steps here: state and prove"
            elif S(v) in here and P(v) in g:
                steps = "steps here: state only (it is proved in a later section)"
            elif S(v) in here:
                steps = "steps here: state only (no proof needed)"
            else:
                steps = "steps here: prove only (it was stated in an earlier section)"
            lines.append(f"- id `{alias[v]}`: {n.kind}{title}; {steps}. {text_of(n)}")
        sub = dag.subgraph(events)
        cons = sorted({(f"{u[:2]}{alias[node_of(u)]}", f"{w[:2]}{alias[node_of(w)]}")
                       for u, w in sub.edges if node_of(u) != node_of(w)})
        lines += ["", "## Constraints", "", "When both are here, `S:x` must come before `P:x`. In addition:", ""]
        lines += [f"- `{a}` before `{b}`" for a, b in cons] or ["None."]
        path = out_dir / f"{ch}.prompt.md"
        path.write_text("\n".join(lines) + "\n")
        paths.append(path)
    return paths


def _read_response(d: Path, ch: str) -> list[str] | None:
    resp = d / f"{ch}.response.json"
    if not resp.exists():
        return None
    try:
        got = json.loads(resp.read_text())
    except json.JSONDecodeError:
        return None
    ids = d / f"{ch}.ids.json"
    mapping = json.loads(ids.read_text()) if ids.exists() else {}

    def unalias(x: str) -> str:
        if x[:2] in ("S:", "P:"):
            return x[:2] + mapping.get(x[2:], x[2:])
        return mapping.get(x, x)

    return [unalias(x) for x in got]


def load_event_run(d: Path, g: nx.DiGraph, chapters: dict[str, list[str]], node_level: bool = False) -> dict:
    """Per-chapter event orders from a run directory. ``node_level`` reads the node-level baseline's
    responses and puts each proof straight after its statement. Invalid chapters are skipped and reported;
    constraint violations are repaired to the nearest valid order and counted."""
    orders, invalid, violations = {}, [], {}
    for ch, human in chapters.items():
        got = _read_response(d, ch)
        if got is None:
            continue
        if node_level:
            core = set(core_events(g, human))
            got = [e for v in got for e in (S(v), P(v)) if e in core]
            human = [e for e in human if e in core]
        if sorted(got) != sorted(human):
            invalid.append(ch)
            continue
        dag, _ = make_dag(g.subgraph(human).copy(), human)
        pos = {e: i for i, e in enumerate(got)}
        bad = sum(1 for u, w in dag.edges if pos[u] > pos[w])
        if bad:
            got = nearest_topological_order(dag, got)
        violations[ch] = bad
        orders[ch] = got
    return {"orders": orders, "invalid": invalid, "violations_repaired": violations}


def _score(g: nx.DiGraph, human_all: list[str], human: list[str], order: list[str]) -> dict:
    sub = g.subgraph(human)
    pos = {e: i for i, e in enumerate(order)}
    deferred = sum(1 for e in order if e.startswith("P:") and S(node_of(e)) in pos
                   and pos[e] - pos[S(node_of(e))] > 1)
    return {"tau": kendall_tau(human, order),
            "motivated": motivated_share(g, order, prior_statements(human_all, human)),
            "mean_open": order_metrics(sub, order).mean_open, "deferred_proofs": deferred}


def evaluate(bp: Blueprint, decls: dict[str, FormalDecl], runs: dict[str, list[Path]],
             node_runs: dict[str, list[Path]] | None = None, seed: int = 0) -> dict:
    g, human_all = event_graph(bp, decls)
    chapters = chapters_of(bp, g, human_all)
    rng = random.Random(seed)
    per_variant: dict[str, dict] = {}

    core = {ch: core_events(g, h) for ch, h in chapters.items()}

    def add(variant: str, run_label: str, orders: dict[str, list[str]]) -> None:
        # Score on each chapter's core (results stated *and* proved there), the part every method orders.
        v = per_variant.setdefault(variant, {"runs": []})
        scores = {}
        for ch, o in orders.items():
            c = set(core[ch])
            scores[ch] = _score(g, human_all, core[ch], [e for e in o if e in c])
        v["runs"].append({"run": run_label, "chapters": scores})

    add("human", "blueprint", chapters)
    for m, label in ((10**9, "bottom-up (m = ∞)"), (3, "hybrid m = 3"), (1, "top-down (m = 1)")):
        for r in range(5):
            orders = {}
            for ch, h in chapters.items():
                dag, _ = make_dag(g.subgraph(h).copy(), h)
                orders[ch] = hybrid_order(dag, goals_by_fan_in(dag, m), rng)
            add(label, f"seed {r}", orders)
    meta = {}
    for kind, spec, node_level in (("node-level LLM", node_runs or {}, True), ("event-level LLM", runs, False)):
        for variant, dirs in spec.items():
            for d in dirs:
                res = load_event_run(d, g, chapters, node_level=node_level)
                if res["orders"]:
                    add(f"{kind}, {variant}", str(d), res["orders"])
                    meta[str(d)] = {"invalid": res["invalid"], "violations_repaired": res["violations_repaired"]}
    # Compare every order on the same chapters: those answered by every run of every variant.
    common = [ch for ch in chapters if all(ch in r["chapters"] for v in per_variant.values() for r in v["runs"])]
    summary = {}
    for variant, v in per_variant.items():
        rows = [r["chapters"][ch] for r in v["runs"] for ch in common]
        run_taus = [statistics.fmean(r["chapters"][ch]["tau"] for ch in common) for r in v["runs"]]
        summary[variant] = {
            "runs": len(v["runs"]),
            "tau_mean": statistics.fmean(run_taus),
            "tau_sd": statistics.stdev(run_taus) if len(run_taus) > 1 else 0.0,
            "motivated": statistics.fmean(c["motivated"] for c in rows),
            "mean_open": statistics.fmean(c["mean_open"] for c in rows),
            "deferred_per_chapter": statistics.fmean(c["deferred_proofs"] for c in rows),
            "per_chapter_tau": {ch: statistics.fmean(r["chapters"][ch]["tau"] for r in v["runs"]) for ch in common},
        }
    return {"chapters": common, "excluded_chapters": [c for c in chapters if c not in common],
            "summary": summary, "runs": per_variant, "meta": meta}


def write_report(res: dict, path: Path, project: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.with_suffix(".json").write_text(json.dumps(res, indent=2))
    s = res["summary"]
    lines = [
        f"# Event-level LLM ordering: {project}",
        "",
        "The model orders statements (`S:x`) and proofs (`P:x`) separately and may defer proofs. Everything is "
        "scored on statement/proof events, averaged over chapters with at least 8 results. τ = Kendall "
        "correlation with the human event order; motivated = share of lemmas stated after a goal they serve; "
        "mean open = working-memory proxy (lower is better). Node-level LLM runs are recast with each proof "
        "straight after its statement. All orders are compared on each chapter's *core*: results whose "
        "statement and proof both sit in that chapter (proofs deferred to another section, and their "
        "statements, are left out, since node-level prompts never placed them).",
        "",
        f"Chapters compared: {len(res['chapters'])}. Excluded (not answerable by every method, e.g. node-level "
        f"prompts cannot place a proof whose statement is in another section): "
        f"{', '.join(res['excluded_chapters']) or 'none'}.",
        "",
        "| Order | runs | τ with human (mean ± sd over runs) | motivated | mean open | deferred proofs / chapter |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for name, r in s.items():
        lines.append(f"| {name} | {r['runs']} | {r['tau_mean']:+.2f} ± {r['tau_sd']:.2f} | {r['motivated']:.0%} | "
                     f"{r['mean_open']:.1f} | {r['deferred_per_chapter']:.1f} |")
    lines += ["", "Per-chapter τ with the human order (mean over runs):", "",
              "| Order | " + " | ".join(res["chapters"]) + " |", "|---|" + "---:|" * len(res["chapters"])]
    for name, r in s.items():
        if name == "human":
            continue
        lines.append(f"| {name} | " + " | ".join(f"{r['per_chapter_tau'][c]:+.2f}" for c in res["chapters"]) + " |")
    bad = {k: v for k, v in res["meta"].items() if v["invalid"] or any(v["violations_repaired"].values())}
    lines += ["", "Invalid responses or repaired constraint violations: "
              + (", ".join(f"{k}: {v}" for k, v in bad.items()) if bad else "none") + "."]
    path.write_text("\n".join(lines) + "\n")
