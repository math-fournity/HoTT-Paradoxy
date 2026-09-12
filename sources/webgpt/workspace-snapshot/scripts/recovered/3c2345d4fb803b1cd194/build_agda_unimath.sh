#!/usr/bin/env bash
set -uo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
PREFIX="${PREFIX:-$ROOT/.toolchain}"
AGDA="${AGDA:-$PREFIX/bin/agda}"
LIB="${AGDA_UNIMATH_ROOT:-$PREFIX/src/agda-unimath}"
OUT="$ROOT/build"
mkdir -p "$OUT"
LOG="$OUT/build.log"
: > "$LOG"
STATUS=0
if [[ ! -x "$AGDA" ]]; then
  echo "BLOCKED: Agda executable not found at $AGDA" | tee -a "$LOG"
  exit 77
fi
if [[ ! -d "$LIB/src" ]]; then
  echo "BLOCKED: agda-unimath source not found at $LIB" | tee -a "$LOG"
  exit 77
fi
"$AGDA" --version | tee -a "$LOG"
git -C "$LIB" rev-parse HEAD 2>&1 | tee -a "$LOG"
FLAGS=(--without-K --exact-split --no-import-sorts --auto-inline --no-require-unique-meta-solutions -WnoWithoutKFlagPrimEraseEquality --no-postfix-projections)
FILES=(
  "$ROOT/specs/FixedPointFreeMonodromy.agda"
  "$ROOT/specs/FiberTruthInvariant.agda"
  "$ROOT/specs/NoFreeEnrichment.agda"
  "$ROOT/specs/GuardErasure.agda"
  "$ROOT/specs/SnapshotProvenance.agda"
  "$ROOT/specs/IntentRole.agda"
  "$ROOT/specs/ContextFormalizer.agda"
  "$ROOT/specs/ExtensionalCost.agda"
  "$ROOT/specs/WalkingArrowCore.agda"
  "$ROOT/agda-unimath/hott-z/no-canonical-earlier-event.agda"
  "$ROOT/agda-unimath/hott-z/no-canonical-temporal-order.agda"
  "$ROOT/agda-unimath/hott-z/no-uniform-witness-extractor.agda"
)
for f in "${FILES[@]}"; do
  echo "=== $f ===" | tee -a "$LOG"
  "$AGDA" "${FLAGS[@]}" -i "$LIB/src" -i "$ROOT/agda-unimath" -i "$ROOT/specs" "$f" 2>&1 | tee -a "$LOG"
  rc=${PIPESTATUS[0]}
  echo "exit_code=$rc" | tee -a "$LOG"
  if [[ $rc -ne 0 ]]; then STATUS=$rc; fi
done
exit "$STATUS"
