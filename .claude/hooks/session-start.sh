#!/bin/bash
# SessionStart hook for Claude Code on the web: Python deps (uv) and the Lean toolchain (elan)
# needed by scripts/phase1_pfr.sh. The heavy PFR build and Mathlib cache stay in that script.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "${CLAUDE_PROJECT_DIR:-$(dirname "$0")/../..}"

# Python: the cairn package, matplotlib/networkx, pytest, ruff.
if ! command -v uv >/dev/null 2>&1; then
  pip install --quiet uv
fi
uv sync --quiet

# Lean: elan plus the toolchain pinned by the PFR commit used in scripts/phase1_pfr.sh.
LEAN_TOOLCHAIN="leanprover/lean4:v4.35.0-rc2"
export PATH="$HOME/.elan/bin:$PATH"
if ! command -v elan >/dev/null 2>&1; then
  curl -sSfL https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh \
    | sh -s -- -y --no-modify-path --default-toolchain none >/dev/null
fi
if ! elan toolchain list | grep -qF "$LEAN_TOOLCHAIN"; then
  elan toolchain install "$LEAN_TOOLCHAIN" >/dev/null
fi
elan default "$LEAN_TOOLCHAIN" >/dev/null 2>&1

if [ -n "${CLAUDE_ENV_FILE:-}" ]; then
  echo 'export PATH="$HOME/.elan/bin:$PATH"' >> "$CLAUDE_ENV_FILE"
fi
