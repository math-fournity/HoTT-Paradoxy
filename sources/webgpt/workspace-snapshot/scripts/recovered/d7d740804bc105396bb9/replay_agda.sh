#!/usr/bin/env bash
set -u
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LOG="$ROOT/formal/build.log"
: > "$LOG"
exec > >(tee -a "$LOG") 2>&1
printf 'timestamp_utc=%s\n' "$(date -u +%FT%TZ)"
printf 'cwd=%s\n' "$PWD"
printf 'argv='; printf '%q ' "$0" "$@"; printf '\n'
if ! command -v agda >/dev/null 2>&1; then
  echo 'status=BLOCKED'
  echo 'reason=agda executable not found'
  echo 'exit_code=77'
  exit 77
fi
if [[ -z "${AGDA_UNIMATH_ROOT:-}" || ! -d "${AGDA_UNIMATH_ROOT}/src" ]]; then
  echo 'status=BLOCKED'
  echo 'reason=AGDA_UNIMATH_ROOT is unset or does not contain src/'
  echo 'exit_code=78'
  exit 78
fi
status=0
for file in "$ROOT"/formal/agda/*.agda; do
  echo "--- checking $file"
  agda -i "$AGDA_UNIMATH_ROOT/src" -i "$ROOT/formal/agda" "$file" || status=$?
done
printf 'exit_code=%s\n' "$status"
if [[ "$status" -eq 0 ]]; then echo 'status=PASS'; else echo 'status=FAIL'; fi
exit "$status"
