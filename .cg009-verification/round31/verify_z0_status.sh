#!/bin/bash
# CG-009: 一次性核验"Z0 战线已证/未证边界"。
#
# 每个文件都编译到私有输出目录 /tmp/cg009mine（不用共享 build/，避免他人的并发改写
# 造成假性 object-file-missing）。判据只有两条：退出码 0，且 sorryAx 行数 0。
#
# 用法： bash verify_z0_status.sh
#
# 背景（2026-10-13）：共享核验树 round31 曾被他人在核验后"清理"删除未入 git 的文件，
# 因此本脚本只读源文件、只写自己的 /tmp 输出，对 round31 不做任何增删。

set -u
ROOT=/Volumes/D/HoTT_AI_HANDOFF_20260911/.claude/worktrees/elegant-mclaren-767fb0/.cg009-verification/round31
MINE=/tmp/cg009mine
LEAN=/Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0/bin/lean

mkdir -p "$MINE"
cd "$ROOT" || exit 2
export LEAN_PATH="$MINE:$(cat lean_path.txt)"

# $1 = 相对 src 的路径
one() {
  f="$1"; base=$(basename "$f" .lean)
  if "$LEAN" --o="$MINE/${base}.olean" -R src "$f" > "/tmp/z0st_${base}.out" 2>&1; then
    sad=$(grep -c "sorryAx" "/tmp/z0st_${base}.out" || true)
    if [ "$sad" = "0" ]; then
      printf '[已证] %-28s rc=0 sorryAx=0\n' "$base"
    else
      printf '[有 sorry] %-26s rc=0 sorryAx=%s  ← 不可作为收据\n' "$base" "$sad"
    fi
  else
    printf '[编译失败] %-26s\n' "$base"
    grep -m3 "error" "/tmp/z0st_${base}.out" | sed 's/^/         /'
  fi
}

echo "=============================================================="
echo " CG-009 / Z0 战线 · 已证边界核验  (2026-10-13)"
echo " 判据：rc=0 且 sorryAx=0。只读源，不碰 round31。"
echo "=============================================================="
echo
echo "--- A 组：iVE_open 全证（c50e1d0b 移植的四个文件）---"
for f in ShiftTools ShiftConjunct IVeShift TranslateShiftCompat ITShift \
         IVEOpenFunc15 IVEOpenFunc16 IVEOpenFunc17 IVEOpenFull; do
  one "src/GodelQ/ZFC/${f}.lean"
done

echo
echo "--- B 组：影子级无条件 Z0（本次新确认，TranslateRE.lean）---"
for f in ShRE TranslateRE; do
  one "src/GodelQ/ZFC/${f}.lean"
done
echo
echo "    B 组关键结论（若上面两行均为 [已证]）："
echo "      zfc_z0 : 𝙕𝙁𝘾 ⊬ arithTrln.translate (Sh.craig.consistent.val)"
echo "      translate_computable : Computable (fun σ ↦ arithTrln.translate σ)"
echo "    二者 machine-verified，公理仅 [propext, Classical.choice, Quot.sound]"

echo
echo "--- C 组：完整 Z0 的骨架（依赖 zfcTr.HBL3）---"
one "src/GodelQ/ZFC/Z0Full.lean"
echo
echo "    C 组说明：zfc_z0_full 以 [zfcTr.HBL3] 为前提；"
echo "    zfc_z0_full_of_D3_internalize 把缺口约成一条可搬移性断言；"
echo "    zfcTr_D3_standard 证明该断言在标准模型 ℕ 中为真。"

echo
echo "--- D 组：尚未证成（对照，说明缺口在哪）---"
for f in HRoot ITSubsts1; do
  one "src/GodelQ/ZFC/${f}.lean"
done
echo
echo "    D 组说明：HRoot.hRoot_uncond = axmBridge 本身（带 sorry）；"
echo "    ITSubsts1.iT_substs1 = hAB 所需桥（带 sorry，且有第三方会话在编辑)。"

echo
echo "=============================================================="
echo " 汇总：A+B+C 全 [已证] ⇒ 影子级无条件 Z0 成立，"
echo "       完整形式的唯一缺口 = HBL3（D3 内部化，ℕ → 任意 V）。"
echo "       D 组是 axmBridge/hAB 两条独立缺口，不遮蔽 A+B+C。"
echo "=============================================================="
