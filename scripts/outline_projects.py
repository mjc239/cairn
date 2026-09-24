#!/usr/bin/env python3
"""Blueprint-free outlines of the 9 training projects, scored against their blueprints.

For each project, the key-declaration model is trained on the *other* training projects (leave one project out), so
the project's own blueprint is never seen; the baseline model is trained on PFR and Carleson only (minus the project).
Each outline uses the exposition style fitted to the project's blueprint (closest whole-document profile).

    uv run python scripts/cross_project.py      # once: unpacks the dumps, writes key_model_all.json
    uv run python scripts/outline_projects.py

Writes results/outline/projects/<project>.md (outline at the blueprint's own level of detail) and
results/outline/projects/eval.{json,md}.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "python"))
sys.path.insert(0, str(ROOT / "scripts"))

from cross_project import TRAIN, dump, harvested  # noqa: E402

from cairn.blueprint import parse_blueprint  # noqa: E402
from cairn.formal import join_blueprint, load_decls  # noqa: E402
from cairn.outline import KeyModel, build, evaluate, render  # noqa: E402
from cairn.style import Style  # noqa: E402

OUT = ROOT / "results" / "outline" / "projects"
GRID = (0.05, 0.1, 0.15, 0.2, 0.3)


def fitted_style(name: str) -> Style:
    path = {"PFR": ROOT / "results/style/pfr/style.json", "Carleson": ROOT / "results/style/carleson/style.json"}.get(
        name, ROOT / "results/harvest" / name / "style/style.json")
    return Style(**json.loads(path.read_text())["document"]["fit"]["closest_profile"]["style"])


def main() -> None:
    projects = {
        "PFR": (parse_blueprint(ROOT / "data/raw/pfr/blueprint/src", "chapter/main.tex"),
                load_decls(dump("pfr", "results/phase1/pfr/pfr_decls.jsonl.gz"))),
        "Carleson": (parse_blueprint(ROOT / "data/raw/carleson/blueprint/src", "content.tex", "section"),
                     load_decls(dump("carleson", "results/phase1/carleson/carleson_decls.jsonl.gz"))),
    }
    projects.update({n: harvested(n) for n in TRAIN})
    OUT.mkdir(parents=True, exist_ok=True)
    results = {}
    for name, (bp, decls) in projects.items():
        others = {n: p for n, p in projects.items() if n != name}
        base = {n: p for n, p in others.items() if n in ("PFR", "Carleson")}
        model, baseline = KeyModel.fit(others), KeyModel.fit(base)
        style = fitted_style(name)
        named = {d for ds in join_blueprint(bp, decls).node_decls.values() for d in ds}
        own = round(len(named) / len(decls), 3)  # the blueprint's own level of detail
        scores = model.score(decls)
        rows = evaluate(bp, decls, scores, style, details=(own, *GRID))
        base_rows = evaluate(bp, decls, baseline.score(decls), style, details=(own, *GRID))
        results[name] = {"style": style.label(), "own_detail": own, "trained_on": sorted(others),
                         "rows": rows, "baseline_rows": base_rows}
        o = build(decls, scores, style, own)
        note = (f"{len(o.named)} results in {len(o.chapter_order)} chapters, selected from {len(decls)} declarations "
                f"(detail {own}, the share its blueprint names). Key-declaration model trained on the other 8 "
                f"projects, never on this one; style fitted to this project's blueprint ({style.label()}).")
        (OUT / f"{name.lower()}.md").write_text(render(o, decls, f"{name}: blueprint-free outline", style, note))
        r, b = rows[0], base_rows[0]
        print(f"{name:22s} detail {own:.3f} style {style.label():32s} theorem precision {r['theorem_precision']:.0%} "
              f"(baseline {b['theorem_precision']:.0%}), recall {r['recall']:.0%} ({b['recall']:.0%}), "
              f"nodes covered {r['node_coverage']:.0%} ({b['node_coverage']:.0%}), NMI {r['chapter_nmi']:.2f}, "
              f"tau within chapters {r['tau_within_chapters']:+.2f}", flush=True)
    (OUT / "eval.json").write_text(json.dumps(results, indent=1) + "\n")

    lines = ["# Blueprint-free outlines of the 9 training projects", "",
             "Each project is outlined with a key-declaration model trained on the *other* 8 projects, at the "
             "blueprint's own level of detail (the share of declarations it names), in the style fitted to its "
             "blueprint. *Baseline*: model trained on PFR and Carleson only (minus the project). Precision is over "
             "named theorems, recall over the declarations the blueprint names.", "",
             "| Project | Detail | Style | Named (theorems) | Theorem precision | Recall | Nodes covered | "
             "Chapter NMI | τ within chapters | Baseline precision | Baseline recall |",
             "|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for name, res in results.items():
        r, b = res["rows"][0], res["baseline_rows"][0]
        lines.append(f"| [{name}]({name.lower()}.md) | {res['own_detail']:.3f} | {res['style']} | {r['named']} "
                     f"({r['named_theorems']}) | {r['theorem_precision']:.0%} | {r['recall']:.0%} | "
                     f"{r['node_coverage']:.0%} | {r['chapter_nmi']:.2f} | {r['tau_within_chapters']:+.2f} | "
                     f"{b['theorem_precision']:.0%} | {b['recall']:.0%} |")
    (OUT / "eval.md").write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
