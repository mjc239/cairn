#!/usr/bin/env bash
# Reproduce results/phase1/pfr: build PFR at the pinned commit (Mathlib from cache), extract
# declaration-level dependencies with lean/extract_deps.lean, and run the Phase 1 analysis.
# Needs elan and network access to release.lean-lang.org, github.com and cache.mathlib.org.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="$ROOT/data/raw/pfr"
"$ROOT/scripts/phase0_pfr.sh" >/dev/null   # clones and pins PFR
export PATH="$HOME/.elan/bin:$PATH"
cd "$DEST"
lake exe cache get
lake build PFR
lake env lean --run "$ROOT/lean/extract_deps.lean" PFR PFR AddCombi > "$ROOT/data/raw/pfr_decls.jsonl"
cd "$ROOT"
mkdir -p results/phase1/pfr
gzip -9 -n -c data/raw/pfr_decls.jsonl > results/phase1/pfr/pfr_decls.jsonl.gz
uv run cairn phase1 "$DEST/blueprint/src" data/raw/pfr_decls.jsonl --project PFR \
  --entry chapter/main.tex --provenance "teorth/pfr @ $(git -C "$DEST" rev-parse --short=12 HEAD), Lean $(cat "$DEST/lean-toolchain")" \
  -o results/phase1/pfr "$@"
