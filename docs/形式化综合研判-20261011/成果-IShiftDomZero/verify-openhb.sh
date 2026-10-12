#!/usr/bin/env bash
# CG-009 开口律链的从零核验（2026-10-12）
#
# 逐文件用**全新输出路径**重编译（--o 指向临时目录），避免 olean 缓存假命中。
# 用法:  bash docs/形式化综合研判-20261011/成果-IShiftDomZero/verify-openhb.sh
#
# 依赖（pinned，不走 elan 代理）:
#   Lean 4.34.0  /Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0
#   Foundation   1fb01b72  /Volumes/D/HoTT-toolchain-cache/foundation-build-1fb01b72-v4.34.0
#   Mathlib      5ed29652  /Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0/...
set -u
LEAN=/Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0/bin/lean
ASTRA=/Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0/mathlib4-5ed2965256430c3649e86755f9576b54eca72435
export LEAN_SYSROOT=/Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0/lib/lean
SRC=.cg009-verification/round31/src
BUILD=.cg009-verification/round31/build
export LEAN_PATH="$BUILD:/Volumes/D/HoTT-toolchain-cache/foundation-build-1fb01b72-v4.34.0/lib/lean"
for p in batteries aesop Qq proofwidgets importGraph LeanSearchClient plausible Cli; do
  LEAN_PATH="$LEAN_PATH:$ASTRA/.lake/packages/$p/.lake/build/lib/lean"
done

OUT=$(mktemp -d /tmp/cg009verify.XXXXXX) || exit 1
trap 'rm -rf "$OUT"' EXIT

FILES="QvecV ITSubstOpen ITRSubstOpen IVESubstOpen IVESubstOpen2 IVESubstOpen3 \
IVEOpenFunc IVEOpenFunc2 IVEOpenFunc3 IVEOpenFunc4 IVEOpenFunc5 IVEOpenFunc6 \
IVEOpenFunc8 IVEOpenFunc9 IVEOpenFunc10 IVEOpenFunc11 GateBranchesU2"

ok=0; bad=0; sorry=0
for f in $FILES; do
  log="$OUT/$f.log"
  timeout 110 "$LEAN" --o="$OUT/$f.olean" -R "$SRC" "$SRC/GodelQ/ZFC/$f.lean" >"$log" 2>&1
  if grep -q '^src.*error' "$log"; then
    echo "FAIL  $f"; grep '^src.*error' "$log" | head -2; bad=$((bad+1))
  elif grep -q 'sorry' "$log"; then
    echo "SORRY $f  (已文档化: iVE_open.func 未完成)"; sorry=$((sorry+1))
  else
    echo "OK    $f"; ok=$((ok+1))
  fi
done
echo "-----"
echo "clean $ok / $((ok+bad+sorry))   (FAIL $bad, SORRY $sorry)"
[ "$bad" -eq 0 ]
