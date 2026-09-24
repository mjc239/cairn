#!/usr/bin/env bash
# Reproduce docs/phase0-pfr.md: clone PFR at the pinned commit and run the Phase 0 analysis.
set -euo pipefail
PFR_COMMIT=ddd44f6ce82ef48624e468662e0fbeb5e37e4026
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="$ROOT/data/raw/pfr"
if [ ! -d "$DEST/.git" ]; then
  git clone --filter=blob:none https://github.com/teorth/pfr.git "$DEST"
fi
git -C "$DEST" fetch --quiet origin "$PFR_COMMIT" 2>/dev/null || true
git -C "$DEST" checkout --quiet "$PFR_COMMIT"
cd "$ROOT"
uv run cairn phase0 "$DEST/blueprint/src" --project PFR \
  --provenance "teorth/pfr @ ${PFR_COMMIT:0:12} (2026-09-20), blueprint/src" \
  -o results/phase0/pfr "$@"
