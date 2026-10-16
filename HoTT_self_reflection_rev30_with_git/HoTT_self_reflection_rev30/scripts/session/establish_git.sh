#!/bin/sh
# Explicitly authorized local history; no remote, push, reset, or existing history replacement.
set -eu
cd "$(dirname "$0")/../.."
if [ -e .git ]; then echo 'Existing .git: inspect instead of reinitializing' >&2; exit 2; fi
git init -b main
git config --local user.name 'HoTT Research Session'
git config --local user.email 'hott-session@local.invalid'
git config --local core.quotePath false
git config --local core.logAllRefUpdates true
git add --all
git commit -m 'Import supplied revision 15 checkpoint without altering historical evidence'
git tag -a checkpoint-rev15-import -m 'Local import baseline; not historical host Git ancestry'
git status --porcelain=v1
