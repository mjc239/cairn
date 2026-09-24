#!/usr/bin/env bash
# Blueprint-free outlines and their evaluation. Each project is outlined with a key-declaration model
# trained only on the *other* project's blueprint; the blueprint is used only for evaluation.
# Needs the dependency dumps (committed gzipped under results/phase1/).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
for p in pfr carleson; do
  [ -f "data/raw/${p}_decls.jsonl" ] || gunzip -c "results/phase1/$p/${p}_decls.jsonl.gz" > "data/raw/${p}_decls.jsonl"
done
[ -d data/raw/pfr/.git ] || ./scripts/phase0_pfr.sh >/dev/null
[ -d data/raw/carleson/.git ] || ./scripts/carleson.sh --no-lean >/dev/null
PFR="data/raw/pfr/blueprint/src:data/raw/pfr_decls.jsonl"
CAR="data/raw/carleson/blueprint/src:data/raw/carleson_decls.jsonl:section"
O=results/outline
mkdir -p $O
uv run cairn key-model --project "PFR=$PFR" -o $O/key_model_pfr.json
uv run cairn key-model --project "Carleson=$CAR" -o $O/key_model_carleson.json
uv run cairn key-model --project "PFR=$PFR" --project "Carleson=$CAR" -o $O/key_model.json   # for new projects

# Evaluation against the blueprints (styles as fitted in docs/style.md)
for dd in "" "--no-define-used"; do
  tag=${dd:+-nodefs}
  uv run cairn outline-eval data/raw/pfr/blueprint/src data/raw/pfr_decls.jsonl --model $O/key_model_carleson.json \
    --project PFR --modules PFR $dd -o $O/pfr_eval$tag.json
  uv run cairn outline-eval data/raw/carleson/blueprint/src data/raw/carleson_decls.jsonl --group-by section \
    --model $O/key_model_pfr.json --project Carleson --top-down 0.2 --roadmap chapter $dd -o $O/carleson_eval$tag.json
done

# Example outlines
# Prose (chapter titles, English statements, proof sketches, faithfulness checks) lives in $O/prose/<outline>/.
# To regenerate it: add --write-prose-prompts, answer <chapter>.prompt.md with <chapter>.prose.json using any model,
# then rerun with --write-check-prompts and answer <chapter>.check.md with <chapter>.check.json using a second reader.
# Then --write-repair-prompts: answer <chapter>.repair[N].md with .repair[N].json, and check again until nothing is flagged.
uv run cairn outline data/raw/pfr_decls.jsonl --model $O/key_model_carleson.json --root PFR_conjecture --detail 0.25 \
  --title "PFR conjecture: outline of the proof" --prose $O/prose/pfr_conjecture -o $O/pfr_conjecture.md
uv run cairn outline data/raw/pfr_decls.jsonl --model $O/key_model_carleson.json --root PFR_conjecture --detail 0.25 \
  --top-down 0.6 --roadmap chapter --title "PFR conjecture: outline of the proof (goal-first style)" \
  -o $O/pfr_conjecture_topdown.md
uv run cairn outline data/raw/carleson_decls.jsonl --model $O/key_model_pfr.json --root classical_carleson \
  --detail 0.08 --no-define-used --top-down 0.2 --roadmap chapter \
  --title "Classical Carleson theorem: outline of the proof" --prose $O/prose/classical_carleson \
  -o $O/classical_carleson.md
uv run cairn outline data/raw/pfr_decls.jsonl --model $O/key_model_carleson.json --modules PFR --detail 0.1 \
  --title "PFR project: full outline" -o $O/pfr_full.md
