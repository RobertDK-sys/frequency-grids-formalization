#!/usr/bin/env bash
# Verification gate for the FrequencyGrids development.
#
#   1. build (lake if the project has a lakefile, otherwise scripts/build.sh, since this
#      development uses the prebuilt, read-only Mathlib on LEAN_PATH);
#   2. scan the sources for `sorry`, `admit`, `native_decide` and `axiom`;
#   3. `#print axioms` on every top-level theorem, failing on anything beyond
#      propext, Classical.choice, Quot.sound.
#
# Exit status 0 means all three gates passed.
set -uo pipefail
cd "$(dirname "$0")/.."

SRC=(FrequencyGrids/*.lean)
fail=0

echo "== 1/3 build"
if [ -f lakefile.lean ] || [ -f lakefile.toml ]; then
  lake build || { echo "FAIL: lake build"; exit 1; }
else
  echo "   (no lakefile: using scripts/build.sh over the prebuilt Mathlib)"
  ./scripts/build.sh || { echo "FAIL: build"; exit 1; }
fi

echo "== 2/3 forbidden constructs (sorry / admit / native_decide / axiom)"
hits=$(grep -nE '\b(sorry|admit|native_decide|axiom)\b' "${SRC[@]}" FrequencyGrids.lean || true)
if [ -n "$hits" ]; then
  echo "$hits"
  echo "FAIL: forbidden construct in the sources"
  fail=1
else
  echo "   clean"
fi

echo "== 3/3 axioms of every top-level theorem"
mkdir -p .scratch
{
  echo "import FrequencyGrids"
  echo "open FrequencyGrids"
  for f in "${SRC[@]}"; do
    grep -oE '^(theorem|lemma) +[A-Za-z0-9_'"'"']+' "$f" \
      | sed -E 's/^(theorem|lemma) +/#print axioms /' || true
  done
} > .scratch/Axioms.lean
n=$(grep -c '#print axioms' .scratch/Axioms.lean)
if ! LEAN_PATH="$PWD:${LEAN_PATH}" lean .scratch/Axioms.lean > .scratch/axioms.out 2>&1; then
  echo "FAIL: axiom check did not elaborate"
  tail -5 .scratch/axioms.out
  fail=1
fi
allowed='\[(propext|Classical\.choice|Quot\.sound)(, (propext|Classical\.choice|Quot\.sound))*\]'
bad=$(grep 'depends on axioms' .scratch/axioms.out | grep -vE "depends on axioms: $allowed" || true)
other=$(grep -vE 'depends on axioms|does not depend on any axioms' .scratch/axioms.out || true)
if [ -n "$bad" ] || [ -n "$other" ]; then
  [ -n "$bad" ] && { echo "$bad"; echo "FAIL: unexpected axiom"; }
  [ -n "$other" ] && { echo "$other"; echo "FAIL: unexpected output from #print axioms"; }
  fail=1
else
  echo "   $n theorems checked: only propext, Classical.choice, Quot.sound"
fi

if [ "$fail" -ne 0 ]; then echo "== CHECK FAILED"; exit 1; fi
echo "== ALL CHECKS PASSED"
