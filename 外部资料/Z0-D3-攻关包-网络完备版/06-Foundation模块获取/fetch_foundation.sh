#!/usr/bin/env bash
# 拉取本包依赖的 167 个 Foundation 模块到 ./foundation-src（相对本脚本所在目录的父级缓存）。
# 每个 URL 来自 Foundation commit 1fb01b72，已实测可达。
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
URL_FILE="$SCRIPT_DIR/Foundation_modules_urls.txt"
OUT_ROOT="${1:-$SCRIPT_DIR/../foundation-src}"
mkdir -p "$OUT_ROOT"
while IFS= read -r url; do
  [ -z "$url" ] && continue
  # 取 URL 中 Foundation/ 之后的相对路径
  rel="${url#*Foundation/}"
  dest="$OUT_ROOT/$rel"
  mkdir -p "$(dirname "$dest")"
  echo "GET $rel"
  curl -fsSL "$url" -o "$dest"
done < "$URL_FILE"
echo "DONE: 167 modules under $OUT_ROOT"
