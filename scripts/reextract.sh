#!/usr/bin/env bash
# Re-extract the dependency dumps behind the three prose outlines (PFR, Carleson, APAP) at their pinned commits,
# after a change to lean/extract_deps.lean. Builds each project with the Mathlib cache, extracts, installs the dump
# (and its committed gzip), then deletes the build to keep disk use bounded. Needs elan and network access.
#   ./scripts/reextract.sh [pfr] [carleson] [apap]      (default: all three)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
export PATH="$HOME/.elan/bin:$PATH"
EXTRACT="$ROOT/lean/extract_deps.lean"

build_extract() {  # dir roots prefixes... ; writes $OUT
  local dir=$1 roots=$2; shift 2
  (cd "$dir" && lake exe cache get && lake build ${roots//,/ } && lake env lean --run "$EXTRACT" "$roots" "$@" > "$OUT.new")
  mv "$OUT.new" "$OUT"
  rm -rf "$dir/.lake" "$HOME/.cache/mathlib"
}

for p in "${@:-pfr carleson apap}"; do
  for q in $p; do
    case $q in
      pfr)
        OUT="$ROOT/data/raw/pfr_decls.jsonl"
        git -C "$ROOT/data/raw/pfr" checkout --quiet ddd44f6ce82e
        build_extract "$ROOT/data/raw/pfr" PFR PFR AddCombi
        gzip -9 -n -c "$OUT" > "$ROOT/results/phase1/pfr/pfr_decls.jsonl.gz" ;;
      carleson)
        OUT="$ROOT/data/raw/carleson_decls.jsonl"
        git -C "$ROOT/data/raw/carleson" checkout --quiet d966776f60fe32950878e75f158cd8fc911c4988
        build_extract "$ROOT/data/raw/carleson" Carleson Carleson
        gzip -9 -n -c "$OUT" > "$ROOT/results/phase1/carleson/carleson_decls.jsonl.gz" ;;
      apap)
        OUT="$ROOT/data/raw/harvest/apap/decls.jsonl"
        SRC="$ROOT/data/raw/harvest/apap.clone"
        rm -rf "$SRC"
        git clone --quiet --filter=blob:none https://github.com/YaelDillies/LeanAPAP.git "$SRC"
        git -C "$SRC" checkout --quiet 3b79412fbe529449c472f0a5f866ee2e3be88b87
        CAIRN_EXTRA="$ROOT/data/raw/harvest/apap/lean_names.txt" build_extract "$SRC" APAP APAP
        rm -rf "$SRC"
        gzip -9 -n -c "$OUT" > "$ROOT/results/harvest/apap/decls.jsonl.gz" ;;
    esac
    rm -rf "$HOME/.elan/toolchains/"*
    echo "re-extracted $q"
  done
done
