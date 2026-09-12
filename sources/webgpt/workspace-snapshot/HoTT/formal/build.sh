#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "$0")" && pwd -P)"
agda_bin="${AGDA:-$(command -v agda || true)}"
lean_bin="${LEAN:-$(command -v lean || true)}"
library_root="${AGDA_UNIMATH_ROOT:-}"

sha256_file() {
  if command -v sha256sum >/dev/null 2>&1; then
    sha256sum "$1" | awk '{print $1}'
  elif command -v shasum >/dev/null 2>&1; then
    shasum -a 256 "$1" | awk '{print $1}'
  else
    echo "BLOCKED: neither sha256sum nor shasum is available" >&2
    return 77
  fi
}

if [ -z "$agda_bin" ] || [ ! -x "$agda_bin" ]; then
  echo "BLOCKED: set AGDA to an Agda 2.8.0 executable" >&2
  exit 77
fi

if [ -z "$library_root" ] || [ ! -f "$library_root/agda-unimath.agda-lib" ]; then
  echo "BLOCKED: set AGDA_UNIMATH_ROOT to agda-unimath commit 88cfce0ce195ae3b64a9e73e8ec744ae64b4006b" >&2
  exit 77
fi

expected_two_element_sha="72f9ad29b6c24b84e1e06f10f701895783e7a56cfaedc1dc0d295dba3629c82e"
expected_library_file_sha="d42bd31babacf7fced8aab84f499d9004a1cac5c3219dc7b360c56c23e9b6221"
actual_two_element_sha="$(sha256_file "$library_root/src/univalent-combinatorics/2-element-types.lagda.md")"
actual_library_file_sha="$(sha256_file "$library_root/agda-unimath.agda-lib")"

if [ "$actual_two_element_sha" != "$expected_two_element_sha" ] ||
   [ "$actual_library_file_sha" != "$expected_library_file_sha" ]; then
  echo "FAIL: agda-unimath sources do not match the pinned evidence snapshot" >&2
  echo "2-element-types sha256=$actual_two_element_sha" >&2
  echo "agda-lib sha256=$actual_library_file_sha" >&2
  exit 65
fi

"$agda_bin" --version
"$agda_bin" -i "$root/self-contained" "$root/self-contained/ZCore.agda"
"$agda_bin" \
  -i "$library_root/src" \
  -i "$root/agda-unimath" \
  "$root/agda-unimath/hott-z/NoCanonicalPoint.agda"

if [ -n "$lean_bin" ] && [ -x "$lean_bin" ]; then
  "$lean_bin" --version
  "$lean_bin" "$root/lean/TwoEvent.lean"
else
  echo "NOTICE: Lean not found; Agda checks passed but independent Lean check was skipped" >&2
fi
