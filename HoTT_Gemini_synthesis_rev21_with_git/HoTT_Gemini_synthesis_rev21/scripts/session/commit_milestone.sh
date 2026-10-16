#!/bin/sh
set -eu
cd "$(dirname "$0")/../.."
if [ "$#" -ne 1 ]; then echo 'One explicit commit message required' >&2; exit 2; fi
git diff --check
git add --all
git commit -m "$1"
git status --porcelain=v1
git log -1 --format='%H %s'
