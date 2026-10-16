# 接手包 · Z0-D3 / ShCraigElim 攻关（Codex 接管版，最小完备）

本包给下一个 AI（或下一个 Session）用来攻下主线“形式化与机器证明”最后唯一未闭合的命题：
`ShCraigElim`（即 Hilbert–Bernays 可导性条件 D3 的唯一实质内容）。

## 0. 你先要纠正的三个误传

接力材料里有三段互相冲突、且与本机事实不符的说法。本包以本机 Lean 4.34.0 实编译为唯一判据。

1. “neg 律（ShCraigElimNegLaw.lean）0 sorry 已证、编译通过” —— 假的。
   本机用 devbuild_ns.py 编译它报错：iT_and / iT_or 的 rewrite 模式匹配不上
   （目标里是 iT (neg (p⋏q))，而引理改写的是 iT (p⋏q)），且文件含 sorry（sorryAx）。
2. “Foundation 缺 140 个模块（第三位 AI 称沙箱里没有 Lean/Mathlib/Foundation）” —— 假的。
   本机 Foundation 源 1fb01b72 共 308 个 .lean 已存在且已构建；“缺模块”是其无网络沙箱的假象。
   本包 06-Foundation闭包/ 已复制全部 308 个模块，离线可用；Foundation地址.md 给网络 URL。
3. “八个工作方向”还开着 —— 假的。八个 git worktree 方向的逐条覆盖已在 2026-10-10 用本机
   Foundation 构建树重放闭合（CG001-C-123..C-127、CG001-C-387）。当前唯一开放方向是 Z0 的 ShCraigElim。

## 1. 最小目标

把 ShCraigElim 证成无 sorry 的定理，使 Z0Blocked.lean 的 sorry 改为引用它，
从而 Z0 完整形式 ZFC ⊬ (ZFC.consistent)^t 在本机工具链下完整成立。

归约链（全部已证）：ShCraigElim ⇐ bwd_of_shcraig_elim（C-390）=> keyE =>
zfcTr_D3_internalize（Z0Blocked.lean）=> zfc_z0_full_of_D3_internalize（C-122）=
ZFC ⊬ arithTrln.translate (ZFC.consistent)。

## 2. 阅读顺序

1. START.md（本文件）
2. 01-目标与缺口/GOAL.md —— 目标命题逐字、归约链、已证零件
3. 01-目标与缺口/STATUS.md —— 逐文件真实编译状态（本机实测）
4. 03-九支归纳任务拆解/ROUTES.md —— 10 个归纳支需要什么、neg 律怎么修
5. 02-API与源码地址/API.md + Foundation地址.md —— 关键 Foundation 引理与源码位置
6. 04-编译与收据/BUILD.md —— 如何编译、如何抓 F-011 收据
7. 07-修订说明/REVISION.md —— 对原计划 zfcTr-D3-plan.md 的独立评审

## 3. 环境（本机已实测可用）

- Lean 4.34.0：/Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0
- Foundation 源 1fb01b72：本包 06-Foundation闭包/Foundation/（离线）；网络版见 Foundation地址.md
- 增量编译脚本：.claude/goals/CG-007-formalization-completion/tools/devbuild_ns.py
- 不得修改 Foundation/Mathlib 源码；新引理只能写成包内新文件
