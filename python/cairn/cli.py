"""Command-line entry point: ``cairn parse`` and ``cairn phase0``."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from dataclasses import asdict
from pathlib import Path

from .blueprint import parse_blueprint


def main(argv: list[str] | None = None) -> None:
    ap = argparse.ArgumentParser(prog="cairn")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("parse", help="parse a blueprint and dump nodes/edges as JSON")
    p.add_argument("src", type=Path, help="blueprint source dir, e.g. <project>/blueprint/src")
    p.add_argument("--entry", default="content.tex")
    p.add_argument("-o", "--out", type=Path)

    p0 = sub.add_parser("phase0", help="compare the human order with random and heuristic orders")
    p0.add_argument("src", type=Path)
    p0.add_argument("--entry", default="content.tex")
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
    p1.add_argument("--project", required=True)
    p1.add_argument("--provenance", default="")
    p1.add_argument("-o", "--out", type=Path, required=True)
    p1.add_argument("--samples", type=int, default=1000)
    p1.add_argument("--seed", type=int, default=0)

    p2 = sub.add_parser("phase2", help="key-declaration, chapter-clustering and ordering baselines")
    p2.add_argument("src", type=Path)
    p2.add_argument("decls", type=Path, help="JSONL from lean/extract_deps.lean")
    p2.add_argument("--entry", default="content.tex")
    p2.add_argument("--project", required=True)
    p2.add_argument("--provenance", default="")
    p2.add_argument("-o", "--out", type=Path, required=True)
    p2.add_argument("--llm-dir", type=Path, help="directory of <chapter>.response.json files (see llm-prompts)")
    p2.add_argument("--seed", type=int, default=0)

    pl = sub.add_parser("llm-prompts", help="write per-chapter ordering prompts for the LLM baseline")
    pl.add_argument("src", type=Path)
    pl.add_argument("decls", type=Path)
    pl.add_argument("--entry", default="content.tex")
    pl.add_argument("-o", "--out", type=Path, required=True)
    pl.add_argument("--seed", type=int, default=0)

    args = ap.parse_args(argv)
    bp = parse_blueprint(args.src, args.entry)

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
            paths = write_llm_prompts(bp, lean_g, args.out, args.seed)
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
