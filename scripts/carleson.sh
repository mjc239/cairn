#!/usr/bin/env bash
# Phases 0-2 on the Carleson project (fpvandoorn/carleson). Its blueprint is a single file, so
# chapters are its \section's (--group-by section).
#   ./scripts/carleson.sh           # full run: clone, Mathlib cache, build (~40 min), extract, analyse
#   ./scripts/carleson.sh --no-lean # analyses only, from the committed dependency dump
# LLM baseline: prompts are written to results/phase2/carleson/llm/; answer each into
# <chapter>.response.json and rerun with --no-lean.
set -euo pipefail
COMMIT=d966776f60fe32950878e75f158cd8fc911c4988
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="$ROOT/data/raw/carleson"
DUMP="$ROOT/results/phase1/carleson/carleson_decls.jsonl.gz"
DECLS="$ROOT/data/raw/carleson_decls.jsonl"
PROV="fpvandoorn/carleson @ ${COMMIT:0:12} (2026-09-23), chapters = \\section"
[ -d "$DEST/.git" ] || git clone --filter=blob:none https://github.com/fpvandoorn/carleson.git "$DEST"
git -C "$DEST" fetch --quiet origin "$COMMIT" 2>/dev/null || true
git -C "$DEST" checkout --quiet "$COMMIT"
if [ "${1:-}" != "--no-lean" ]; then
  export PATH="$HOME/.elan/bin:$PATH"
  (cd "$DEST" && lake exe cache get && lake build Carleson &&
   lake env lean --run "$ROOT/lean/extract_deps.lean" Carleson Carleson > "$DECLS")
  mkdir -p "$(dirname "$DUMP")"
  gzip -9 -n -c "$DECLS" > "$DUMP"
fi
[ -f "$DECLS" ] || gunzip -c "$DUMP" > "$DECLS"
cd "$ROOT"
SRC="$DEST/blueprint/src"
COMMON=(--group-by section --project Carleson --provenance "$PROV")
uv run cairn phase0 "$SRC" "${COMMON[@]}" -o results/phase0/carleson
uv run cairn phase1 "$SRC" "$DECLS" "${COMMON[@]}" -o results/phase1/carleson
uv run cairn llm-prompts "$SRC" "$DECLS" --group-by section -o results/phase2/carleson/llm
uv run cairn phase2 "$SRC" "$DECLS" "${COMMON[@]}" --llm-dir results/phase2/carleson/llm -o results/phase2/carleson
R=results/phase2/carleson/llm_runs
uv run cairn llm-eval "$SRC" "$DECLS" --group-by section --project Carleson -o results/phase2/carleson/llm_runs.md \
  --run named=results/phase2/carleson/llm --run named=$R/named-s1 --run blind=$R/blind-s0 --run blind=$R/blind-s1
# Cross-project: train the key-declaration model on one project, test on the other (needs the PFR dump too).
PFR_DECLS="$ROOT/data/raw/pfr_decls.jsonl"
[ -f "$PFR_DECLS" ] || gunzip -c results/phase1/pfr/pfr_decls.jsonl.gz > "$PFR_DECLS"
[ -d "$ROOT/data/raw/pfr/.git" ] || "$ROOT/scripts/phase0_pfr.sh" >/dev/null
uv run cairn transfer -o results/cross_project/key_node_transfer.json \
  --project "PFR=$ROOT/data/raw/pfr/blueprint/src:$PFR_DECLS" \
  --project "Carleson=$SRC:$DECLS:section"
# Statement/proof events (deferred proofs, motivation vs load) for both projects, and the frontier figure.
uv run cairn events "$SRC" "$DECLS" "${COMMON[@]}" -o results/events/carleson --samples 300
uv run cairn events "$ROOT/data/raw/pfr/blueprint/src" "$PFR_DECLS" --project PFR -o results/events/pfr --samples 300 \
  --provenance "teorth/pfr @ ddd44f6ce82e"
uv run python -c "
import json; from pathlib import Path; from cairn.plots import plot_motivation_frontier
p = {n: json.load(open(f'results/events/{k}/events.json')) for n, k in
     [('PFR (bottom-up blueprint)', 'pfr'), ('Carleson (paper-style blueprint)', 'carleson')]}
plot_motivation_frontier(p, Path('results/cross_project/motivation_frontier.png'))"
# Event-level LLM baseline (proofs may be deferred). Prompts: cairn event-prompts ... [--anonymise --no-titles] --seed N;
# responses were produced by the current Claude model. Scored against the node-level runs on chapter cores.
E=results/events
uv run cairn event-llm-eval "$SRC" "$DECLS" --group-by section --project Carleson -o $E/carleson/llm_eval.md \
  --run labelled=$E/carleson/llm/named-s0 --run labelled=$E/carleson/llm/named-s1 \
  --run anonymised=$E/carleson/llm/blind-s0 --run anonymised=$E/carleson/llm/blind-s1 \
  --node-run labelled=results/phase2/carleson/llm --node-run labelled=$R/named-s1 \
  --node-run anonymised=$R/blind-s0 --node-run anonymised=$R/blind-s1
P2=results/phase2/pfr
uv run cairn event-llm-eval "$ROOT/data/raw/pfr/blueprint/src" "$PFR_DECLS" --project PFR -o $E/pfr/llm_eval.md \
  --run labelled=$E/pfr/llm/named-s0 --run labelled=$E/pfr/llm/named-s1 \
  --run anonymised=$E/pfr/llm/blind-s0 --run anonymised=$E/pfr/llm/blind-s1 \
  --node-run labelled=$P2/llm --node-run labelled=$P2/llm_runs/named-s1 --node-run labelled=$P2/llm_runs/named-s2 \
  --node-run anonymised=$P2/llm_runs/blind-s0 --node-run anonymised=$P2/llm_runs/blind-s1 --node-run anonymised=$P2/llm_runs/blind-s2
# Parameterised styles: sweep and fit for both projects, and the whole-document frontier figure.
uv run cairn style "$SRC" "$DECLS" "${COMMON[@]}" -o results/style/carleson
uv run cairn style "$ROOT/data/raw/pfr/blueprint/src" "$PFR_DECLS" --project PFR -o results/style/pfr \
  --provenance "teorth/pfr @ ddd44f6ce82e"
uv run python -c "
import json; from pathlib import Path; from cairn.plots import plot_style_frontier
p = {n: json.load(open(f'results/style/{k}/style.json')) for n, k in [('PFR', 'pfr'), ('Carleson', 'carleson')]}
plot_style_frontier(p, Path('results/cross_project/style_frontier.png'))"
