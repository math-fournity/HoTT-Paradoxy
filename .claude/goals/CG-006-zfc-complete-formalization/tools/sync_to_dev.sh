#!/bin/bash
# CG-006: copy this goal package from the main checkout into the dev worktree and commit it there
# (exact path only). The main checkout may be on another branch; goal-x reads the package from it.
# usage: tools/sync_to_dev.sh "commit subject" [extra path relative to repo root, already present in the worktree ...]
set -euo pipefail
MAIN=/Volumes/D/HoTT_AI_HANDOFF_20260911
WT=$MAIN/.claude/worktrees/cg006-dev
PKG=.claude/goals/CG-006-zfc-complete-formalization
MSG="${1:?commit subject}"; shift || true
[ -d "$WT" ] || git -C "$MAIN" worktree add "$WT" dev
cd "$WT"
[ "$(git rev-parse --abbrev-ref HEAD)" = dev ] || { echo "worktree not on dev"; exit 1; }
[ -z "$(git diff --cached --name-only)" ] || { echo "index not empty; abort"; exit 1; }
rsync -a --delete "$MAIN/$PKG/" "$WT/$PKG/"
git add -- "$PKG" "$@"
git diff --cached --stat | tail -4
git commit -q -m "$MSG" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
git log --oneline -1
