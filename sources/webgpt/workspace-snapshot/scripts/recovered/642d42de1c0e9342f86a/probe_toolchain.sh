#!/usr/bin/env bash
set -u
printf 'timestamp_utc=%s\n' "$(date -u +%FT%TZ)"
printf 'cwd=%s\n' "$PWD"
printf 'argv='; printf '%q ' "$0" "$@"; printf '\n'
printf 'uname=%s\n' "$(uname -a)"
printf 'python='; python --version 2>&1 || true
printf 'node='; node --version 2>&1 || true
for x in agda lean lake elan coqc rocq rzk ghc cabal stack nix; do
  if command -v "$x" >/dev/null 2>&1; then
    printf '%s_path=%s\n' "$x" "$(command -v "$x")"
    "$x" --version 2>&1 | head -n 3 | sed "s/^/${x}_version=/"
  else
    printf '%s_path=NOT_FOUND\n' "$x"
  fi
done
printf 'dns_github='; getent hosts github.com 2>&1 || true
