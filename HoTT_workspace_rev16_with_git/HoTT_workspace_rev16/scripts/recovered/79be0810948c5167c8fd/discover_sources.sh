#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "$0")/../.." && pwd -P)"
baseline_commit="dc1e369a6a74"
source_dir="$repo_root/HoTT/sources/aistudio-docs"
archive_dir="$repo_root/aistudio-docs"

echo "baseline_commit=$baseline_commit"
echo "filename_hits_at_baseline"
git -C "$repo_root" ls-tree -r --name-only "$baseline_commit" -- aistudio-docs \
  | rg -i '(^|/)?.*hott.*\.md$' \
  | sort

echo "filename_hit_count_at_baseline=$(git -C "$repo_root" ls-tree -r --name-only "$baseline_commit" -- aistudio-docs | rg -i '(^|/)?.*hott.*\.md$' | wc -l | tr -d ' ')"
echo "relocated_source_count=$(find "$source_dir" -maxdepth 1 -type f -name '*.md' | wc -l | tr -d ' ')"
echo "remaining_filename_hit_count=$(find "$archive_dir" -type f -name '*.md' -print | rg -i '(^|/)?.*hott.*\.md$' | wc -l | tr -d ' ')"

broad_pattern='HoTT|homotopy[ -]type[ -]theory|同伦类型论'
issue_pattern='HoTT.{0,80}(paradox|悖论|bug|time|时间|incomplete|不完备)|((paradox|悖论|bug|time|时间|incomplete|不完备).{0,80}HoTT)'

echo "remaining_broad_mention_files=$(rg -l -i -g '*.md' "$broad_pattern" "$archive_dir" | wc -l | tr -d ' ')"
echo "remaining_issue_context_files=$(rg -l -i -g '*.md' "$issue_pattern" "$archive_dir" | wc -l | tr -d ' ')"

echo "NOTE: broad/content counts are candidate mentions, not a permission to move every matching file."
echo "NOTE: the selection decision and its bounded negative conclusion are documented in HoTT/SOURCE_REGISTRY.md."
