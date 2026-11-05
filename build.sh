#!/usr/bin/env bash
# Build the FrequencyGrids formalization with the pre-built Mathlib on LEAN_PATH.
# Usage:  ./scripts/build.sh          (from the project root)
set -euo pipefail
cd "$(dirname "$0")/.."
export LEAN_PATH="$PWD:${LEAN_PATH}"
MODULES=(FrequencyGrids.Basic FrequencyGrids.Lattice FrequencyGrids.Uniqueness FrequencyGrids.Enclosure FrequencyGrids.Counting FrequencyGrids.Neighbour FrequencyGrids.Parametric
         FrequencyGrids.Structure FrequencyGrids.Resonance FrequencyGrids.Eigen FrequencyGrids.GeneralGram FrequencyGrids.Estimate FrequencyGrids.Congruence FrequencyGrids.Conjectures FrequencyGrids.Necessary
         FrequencyGrids)
for m in "${MODULES[@]}"; do
  f="${m//.//}.lean"
  if [ -f "$f" ]; then
    echo "== building $m"
    lean -o "${m//.//}.olean" -i "${m//.//}.ilean" "$f"
  fi
done
echo "done"
