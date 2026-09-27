#!/usr/bin/env bash
# Byte-exact re-verification of the 16 Zeno-line Linux replays (Cloud-Opus, 2026-09-27).
# Writes one JSON object per run (tools/verify_copus_run.py output) to the file given as $1.
set -u
cd "$(dirname "$0")/../.."
OUT="${1:?output file}"
: > "$OUT"
for n in SST-FINITE-LEVELS WILD-SST WILD-SST2 WILD-SST-P4 WINDING-COCYCLE WILD-SST-LEVELS SELF-INTERPRETATION WILD-SST-LEAN; do
  for s in 01 NEG-01; do
    r="20260927-COPUS-REPLAY-CG001-$n-$s"
    extra=""; [ "$s" = "NEG-01" ] && extra="--expect-rejected"
    python3 -B Cloud-Opus审计并补完GLM/tools/verify_copus_run.py --run-dir "HoTT/verification/runs/$r" --rerun $extra \
      | python3 -c "import json,sys; d=json.load(sys.stdin); print(json.dumps({k: d.get(k) for k in ('run_id','status','replay','index','exit_code','rejection_stage','agda_error_tag')}, ensure_ascii=False))" >> "$OUT" \
      || echo "{\"run_id\": \"$r\", \"status\": \"VERIFY_FAILED\"}" >> "$OUT"
  done
done
