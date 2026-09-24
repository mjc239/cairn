"""Command-line entry point: ``cairn parse`` and ``cairn phase0``."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from dataclasses import asdict
from pathlib import Path

from .blueprint import GROUP_BY, parse_blueprint


def main(argv: list[str] | None = None) -> None:
    ap = argparse.ArgumentParser(prog="cairn")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("parse", help="parse a blueprint and dump nodes/edges as JSON")
    p.add_argument("src", type=Path, help="blueprint source dir, e.g. <project>/blueprint/src")
    p.add_argument("--entry", default="content.tex")
    p.add_argument("--group-by", choices=GROUP_BY, default="file", help="what counts as a chapter")
    p.add_argument("-o", "--out", type=Path)

    p0 = sub.add_parser("phase0", help="compare the human order with random and heuristic orders")
    p0.add_argument("src", type=Path)
    p0.add_argument("--entry", default="content.tex")
    p0.add_argument("--group-by", choices=GROUP_BY, default="file", help="what counts as a chapter")
    p0.add_argument("--project", required=True, help="name used in report titles")
    p0.add_argument("--provenance", default="", help="e.g. repo URL and commit, recorded in the report")
    p0.add_argument("-o", "--out", type=Path, required=True, help="output directory")
    p0.add_argument("--samples", type=int, default=1000)
    p0.add_argument("--restarts", type=int, default=20)
    p0.add_argument("--seed", type=int, default=0)

    p1 = sub.add_parser("phase1", help="compare \\uses with Lean dependencies; rerun ordering analysis on Lean edges")
    p1.add_argument("src", type=Path)
    p1.add_argument("decls", type=Path, help="JSONL from lean/extract_deps.lean")
    p1.add_argument("--entry", default="content.tex")
    p1.add_argument("--group-by", choices=GROUP_BY, default="file", help="what counts as a chapter")
    p1.add_argument("--project", required=True)
    p1.add_argument("--provenance", default="")
    p1.add_argument("-o", "--out", type=Path, required=True)
    p1.add_argument("--samples", type=int, default=1000)
    p1.add_argument("--seed", type=int, default=0)

    p2 = sub.add_parser("phase2", help="key-declaration, chapter-clustering and ordering baselines")
    p2.add_argument("src", type=Path)
    p2.add_argument("decls", type=Path, help="JSONL from lean/extract_deps.lean")
    p2.add_argument("--entry", default="content.tex")
    p2.add_argument("--group-by", choices=GROUP_BY, default="file", help="what counts as a chapter")
    p2.add_argument("--project", required=True)
    p2.add_argument("--provenance", default="")
    p2.add_argument("-o", "--out", type=Path, required=True)
    p2.add_argument("--llm-dir", type=Path, help="directory of <chapter>.response.json files (see llm-prompts)")
    p2.add_argument("--seed", type=int, default=0)

    pl = sub.add_parser("llm-prompts", help="write per-chapter ordering prompts for the LLM baseline")
    pl.add_argument("src", type=Path)
    pl.add_argument("decls", type=Path)
    pl.add_argument("--entry", default="content.tex")
    pl.add_argument("--group-by", choices=GROUP_BY, default="file", help="what counts as a chapter")
    pl.add_argument("-o", "--out", type=Path, required=True)
    pl.add_argument("--seed", type=int, default=0)
    pl.add_argument("--anonymise", action="store_true", help="replace blueprint labels by random ids")
    pl.add_argument("--no-titles", action="store_true", help="omit result titles")

    pe = sub.add_parser("llm-eval", help="score repeated LLM ordering runs per prompt variant")
    pe.add_argument("src", type=Path)
    pe.add_argument("decls", type=Path)
    pe.add_argument("--entry", default="content.tex")
    pe.add_argument("--group-by", choices=GROUP_BY, default="file", help="what counts as a chapter")
    pe.add_argument("--run", action="append", required=True, metavar="VARIANT=DIR",
                    help="a directory of responses; repeat, same VARIANT for repeated runs")
    pe.add_argument("--project", required=True)
    pe.add_argument("-o", "--out", type=Path, required=True, help="markdown report path")

    pv = sub.add_parser("events", help="statement/proof event analysis (deferred proofs are not forward refs)")
    pv.add_argument("src", type=Path)
    pv.add_argument("decls", type=Path)
    pv.add_argument("--entry", default="content.tex")
    pv.add_argument("--group-by", choices=GROUP_BY, default="file", help="what counts as a chapter")
    pv.add_argument("--project", required=True)
    pv.add_argument("--provenance", default="")
    pv.add_argument("-o", "--out", type=Path, required=True)
    pv.add_argument("--samples", type=int, default=1000)

    pq = sub.add_parser("event-prompts", help="LLM prompts over statement/proof events (proofs may be deferred)")
    pq.add_argument("src", type=Path)
    pq.add_argument("decls", type=Path)
    pq.add_argument("--entry", default="content.tex")
    pq.add_argument("--group-by", choices=GROUP_BY, default="file", help="what counts as a chapter")
    pq.add_argument("-o", "--out", type=Path, required=True)
    pq.add_argument("--seed", type=int, default=0)
    pq.add_argument("--anonymise", action="store_true")
    pq.add_argument("--no-titles", action="store_true")

    pr = sub.add_parser("event-llm-eval", help="score event-level (and node-level) LLM runs on events")
    pr.add_argument("src", type=Path)
    pr.add_argument("decls", type=Path)
    pr.add_argument("--entry", default="content.tex")
    pr.add_argument("--group-by", choices=GROUP_BY, default="file", help="what counts as a chapter")
    pr.add_argument("--run", action="append", default=[], metavar="VARIANT=DIR", help="event-level responses")
    pr.add_argument("--node-run", action="append", default=[], metavar="VARIANT=DIR",
                    help="node-level responses (from llm-prompts), recast as events")
    pr.add_argument("--project", required=True)
    pr.add_argument("-o", "--out", type=Path, required=True, help="markdown report path")

    pt = sub.add_parser("transfer", help="train the key-declaration model on one project, test on others")
    pt.add_argument("--project", action="append", required=True, metavar="NAME=SRC:DECLS[:GROUP_BY[:ENTRY]]")
    pt.add_argument("-o", "--out", type=Path, required=True, help="JSON output path")

    args = ap.parse_args(argv)
    if args.cmd == "transfer":
        from .formal import load_decls
        from .phase2 import transfer_key_nodes

        projects = {}
        for spec in args.project:
            name, _, rest = spec.partition("=")
            src, decls, *more = rest.split(":")
            group_by = more[0] if more else "file"
            entry = more[1] if len(more) > 1 else "content.tex"
            projects[name] = (parse_blueprint(Path(src), entry, group_by), load_decls(Path(decls)))
        res = transfer_key_nodes(projects)
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(res, indent=2))
        for k, v in res.items():
            print(f"{k}: AUROC {v['auroc']:.2f}, P@k {v['p_at_k']:.0%} (base rate {v['base_rate']:.0%})")
        return
    bp = parse_blueprint(args.src, args.entry, args.group_by)

    if args.cmd == "parse":
        data = {
            "nodes": [asdict(n) for n in bp.nodes],
            "edges": [{"source": u, "target": v, "kind": k} for u, v, k in bp.edges()],
            "unresolved": bp.unresolved,
            "orphan_proofs": bp.orphan_proofs,
        }
        text = json.dumps(data, indent=2)
        if args.out:
            args.out.write_text(text)
        else:
            print(text)
        return

    if args.cmd in ("event-prompts", "event-llm-eval"):
        from .event_llm import evaluate, write_event_prompts
        from .event_llm import write_report as write_event_llm
        from .formal import load_decls

        decls = load_decls(args.decls)
        if args.cmd == "event-prompts":
            paths = write_event_prompts(bp, decls, args.out, args.seed, anonymise=args.anonymise,
                                        titles=not args.no_titles)
            print(f"wrote {len(paths)} prompts to {args.out}")
            return

        def runs_of(specs):
            out: dict[str, list[Path]] = {}
            for spec in specs:
                variant, _, d = spec.partition("=")
                out.setdefault(variant, []).append(Path(d))
            return out

        res = evaluate(bp, decls, runs_of(args.run), runs_of(args.node_run))
        write_event_llm(res, args.out, args.project)
        print(f"wrote {args.out}")
        return

    if args.cmd == "events":
        from .events import analyse as analyse_events
        from .events import write_report as write_events
        from .formal import load_decls

        res = analyse_events(bp, load_decls(args.decls), samples=args.samples)
        write_events(res, args.out, args.project, args.provenance)
        print(f"wrote {args.out}/events.md")
        return

    if args.cmd == "llm-eval":
        from .formal import load_decls
        from .phase2 import evaluate_llm_runs, write_llm_runs_report

        runs: dict[str, list[Path]] = {}
        for spec in args.run:
            variant, _, d = spec.partition("=")
            runs.setdefault(variant, []).append(Path(d))
        res = evaluate_llm_runs(bp, load_decls(args.decls), runs)
        write_llm_runs_report(res, args.out, args.project)
        print(f"wrote {args.out}")
        return

    if args.cmd in ("phase2", "llm-prompts"):
        from .formal import formal_graph, join_blueprint, load_decls, projected_graph
        from .phase2 import analyse as analyse2
        from .phase2 import write_llm_prompts
        from .phase2 import write_report as write_phase2

        decls = load_decls(args.decls)
        if args.cmd == "llm-prompts":
            join = join_blueprint(bp, decls)
            nodes = [n.id for n in bp.nodes if n.id in join.node_decls]
            lean_g = projected_graph(bp, formal_graph(decls), join).subgraph(nodes).copy()
            paths = write_llm_prompts(bp, lean_g, args.out, args.seed, anonymise=args.anonymise,
                                      titles=not args.no_titles)
            print(f"wrote {len(paths)} prompts to {args.out}")
            return
        res = analyse2(bp, decls, args.llm_dir, args.seed)
        write_phase2(res, args.out, args.project, args.provenance)
        print(f"wrote {args.out}/phase2.md")
        return

    if args.cmd == "phase1":
        from .formal import load_decls
        from .phase1 import analyse
        from .phase1 import write_report as write_phase1

        decls = load_decls(args.decls)
        stats, results, _ = analyse(bp, decls, samples=args.samples, seed=args.seed)
        write_phase1(stats, results, args.out, args.project, args.provenance)
        print(f"{stats['project_decls']} project decls, coverage {stats['coverage']:.0%}; wrote {args.out}/phase1.md")
        return

    from .phase0 import analyse_blueprint, write_report

    print(f"{len(bp.nodes)} nodes {dict(Counter(n.kind for n in bp.nodes))}, {len(bp.edges())} edges, "
          f"{len(bp.unresolved)} unresolved refs")
    results = analyse_blueprint(bp, samples=args.samples, restarts=args.restarts, seed=args.seed)
    write_report(results, args.out, args.project, args.provenance)
    print(f"wrote {args.out}/phase0.md")


if __name__ == "__main__":
    main()
