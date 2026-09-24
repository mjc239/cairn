#!/usr/bin/env bash
# Reproduce results/phase2/pfr from the committed Lean dependency dump (no Lean build needed).
# LLM baseline: `cairn llm-prompts` writes one prompt per chapter to results/phase2/pfr/llm/; answer each
# with any model into <chapter>.response.json (a JSON array of ids), then rerun this script.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
"$ROOT/scripts/phase0_pfr.sh" >/dev/null   # clones and pins PFR (blueprint source)
DECLS="$ROOT/data/raw/pfr_decls.jsonl"
[ -f "$DECLS" ] || gunzip -c results/phase1/pfr/pfr_decls.jsonl.gz > "$DECLS"
SRC="$ROOT/data/raw/pfr/blueprint/src"
uv run cairn llm-prompts "$SRC" "$DECLS" -o results/phase2/pfr/llm
uv run cairn phase2 "$SRC" "$DECLS" --project PFR --llm-dir results/phase2/pfr/llm \
  --provenance "teorth/pfr @ ddd44f6ce82e, Lean v4.35.0-rc2" -o results/phase2/pfr "$@"
