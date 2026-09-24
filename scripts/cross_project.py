#!/usr/bin/env python3
"""Cross-project key-declaration model on the harvested blueprint projects.

Training projects are those whose blueprints are mostly linked to Lean (at least half the nodes) and name at least
30 project declarations: PFR, Carleson and the harvested projects in TRAIN. Other harvested projects with some
links are scored as held-out test projects only (their unlinked nodes make the negatives unreliable for training).

    uv run python scripts/cross_project.py

Writes results/cross_project/key_node_loo.{json,md} (leave-one-project-out, against the old PFR + Carleson model)
and results/outline/key_model_all.json (trained on every training project).
"""

from __future__ import annotations

import gzip
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "python"))

from cairn.blueprint import parse_blueprint  # noqa: E402
from cairn.formal import load_decls  # noqa: E402
from cairn.outline import KeyModel  # noqa: E402
from cairn.phase2 import leave_one_out_key_nodes  # noqa: E402

TRAIN = ["brownian_motion", "testing_lower_bounds", "sphere_packing", "flt3", "sphere_eversion",
         "abc_exceptions", "apap"]
TEST_ONLY = ["formal_book", "semicircle", "con_nf", "toric", "chandra_furst_lipton", "flt_regular", "iwasawa",
             "bonn_analysis", "clt"]
RESULTS = ROOT / "results" / "harvest"


def harvested(name: str):
    r = json.loads((RESULTS / name / "triage.json").read_text())
    decls = ROOT / "data" / "raw" / "harvest" / name / "decls.jsonl"
    if not decls.exists():
        with gzip.open(RESULTS / name / "decls.jsonl.gz", "rb") as f, decls.open("wb") as g:
            shutil.copyfileobj(f, g)
    bp = parse_blueprint(ROOT / "data" / "raw" / "harvest" / name / r["blueprint_dir"], r["entry"], r["group_by"])
    return bp, load_decls(decls)


def dump(name: str, gz: str) -> Path:
    path = ROOT / "data" / "raw" / f"{name}_decls.jsonl"
    if not path.exists():
        with gzip.open(ROOT / gz, "rb") as f, path.open("wb") as g:
            shutil.copyfileobj(f, g)
    return path


def main() -> None:
    train = {
        "PFR": (parse_blueprint(ROOT / "data/raw/pfr/blueprint/src", "chapter/main.tex"),
                load_decls(dump("pfr", "results/phase1/pfr/pfr_decls.jsonl.gz"))),
        "Carleson": (parse_blueprint(ROOT / "data/raw/carleson/blueprint/src", "content.tex", "section"),
                     load_decls(dump("carleson", "results/phase1/carleson/carleson_decls.jsonl.gz"))),
    }
    train.update({n: harvested(n) for n in TRAIN})
    test = {n: harvested(n) for n in TEST_ONLY}
    res = leave_one_out_key_nodes(train, test, baseline=("PFR", "Carleson"))
    out = ROOT / "results" / "cross_project"
    out.mkdir(parents=True, exist_ok=True)
    (out / "key_node_loo.json").write_text(json.dumps(res, indent=1) + "\n")

    lines = ["# Key-declaration model: leave one project out", "",
             "Each training project is scored by a model trained on the other training projects; held-out projects "
             "by a model trained on all of them. *Baseline*: trained on PFR and Carleson only (minus the project "
             "itself). P@k: precision among the top k, k = the number of blueprint-named declarations.", "",
             "| Project | Role | Decls | Named | Base rate | AUROC | P@k | Baseline AUROC | Baseline P@k |",
             "|---|---|---:|---:|---:|---:|---:|---:|---:|"]
    for name, r in res.items():
        b = r.get("baseline", {})
        lines.append(f"| {name} | {'held out' if r['heldout'] else 'train'} | {r['decls']} | {r['positives']} | "
                     f"{r['base_rate']:.1%} | {r['auroc']:.2f} | {r['p_at_k']:.0%} | "
                     f"{b.get('auroc', float('nan')):.2f} | {b.get('p_at_k', float('nan')):.0%} |")
    (out / "key_node_loo.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))

    model = KeyModel.fit(train)
    model.save(ROOT / "results" / "outline" / "key_model_all.json")
    print(f"wrote results/outline/key_model_all.json (trained on {', '.join(model.trained_on)})")


if __name__ == "__main__":
    main()
