#!/usr/bin/env bash
set +e
OUT="$(cd "$(dirname "$0")" && pwd)/build/preflight.log"
mkdir -p "$(dirname "$OUT")"
: > "$OUT"
for x in agda ghc cabal lean lake coqc rocq rzk git python3; do
  printf '%-10s ' "$x" | tee -a "$OUT"
  command -v "$x" 2>&1 | tee -a "$OUT"
done
printf 'timestamp_utc=' | tee -a "$OUT"; date -u +%Y-%m-%dT%H:%M:%SZ | tee -a "$OUT"
exit 0
