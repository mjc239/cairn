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

    from .phase0 import analyse_blueprint, write_report

    print(f"{len(bp.nodes)} nodes {dict(Counter(n.kind for n in bp.nodes))}, {len(bp.edges())} edges, "
          f"{len(bp.unresolved)} unresolved refs")
    results = analyse_blueprint(bp, samples=args.samples, restarts=args.restarts, seed=args.seed)
    write_report(results, args.out, args.project, args.provenance)
    print(f"wrote {args.out}/phase0.md")


if __name__ == "__main__":
    main()
