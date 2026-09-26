#!/usr/bin/env bash
# Blueprint-free outlines of OpenAI's Navier–Stokes / Euler blowup formalisation (no LLM involved).
# Builds the project at a pinned commit (~2.5 h with the Mathlib cache), extracts it (the dump is ~360 MB, not
# committed), and outlines the dependency cone of each main theorem with the 9-project key-declaration model.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
export PATH="$HOME/.elan/bin:$PATH"
SRC="$ROOT/data/raw/harvest/nse"; DUMP="$ROOT/data/raw/harvest/nse_decls.jsonl"
if [ ! -f "$DUMP" ]; then
  [ -d "$SRC/.git" ] || git clone --quiet https://github.com/openai/NavierStokesAndEuler "$SRC"
  git -C "$SRC" checkout --quiet f9e8bc5b38b6e212696e8a30e3e91517af887bbd
  # Euler.Solution (the Euler main theorem) is not imported by the Euler root module, so it is listed explicitly.
  (cd "$SRC" && lake exe cache get && lake build NavierStokes Euler Euler.Solution &&
     lake env lean --run "$ROOT/lean/extract_deps.lean" NavierStokes,Euler,Euler.Solution NavierStokes Euler > "$DUMP")
fi
O=results/outline/navier_stokes_euler
M=results/outline/key_model_all.json
cd "$ROOT"
uv run cairn outline "$DUMP" --model $M --root NavierStokes.Comparator.navier_stokes_breakdown_R3 --count 150 \
  --no-define-used --title "Navier–Stokes breakdown on ℝ³: outline of the formalisation" -o $O/ns_R3.md
uv run cairn outline "$DUMP" --model $M --root NavierStokes.Comparator.navier_stokes_breakdown_periodic --count 150 \
  --no-define-used --title "Navier–Stokes breakdown on the torus: outline of the formalisation" -o $O/ns_periodic.md
uv run cairn outline "$DUMP" --model $M --root Euler.euler_breakdown_R3 --count 150 \
  --no-define-used --title "Euler breakdown on ℝ³: outline of the formalisation" -o $O/euler_R3.md
