# 逐文件真实编译状态（本机 Lean 4.34.0 实编译，2026-10-11）

判据：用 .claude/goals/CG-007-formalization-completion/tools/devbuild_ns.py 编译每个文件，看 exit code 与是否含 sorryAx。

## 已编译通过、无 sorry（可直接复用）

- Z0Full.lean、Z0Bridge.lean、Z0UniBridge.lean、Z0Shadow.lean、Z0PA.lean、Z0Probe.lean —— 主链与归约，均通过。
- SeqTranslate.lean、SeqTranslateFormula.lean —— translateSeq 与 isSemiformula_iT 等，通过。
- InternalTranslate.lean —— iT 与 iT_rel/iT_nrel/iT_verum/iT_falsum/iT_and/iT_or/iT_all/iT_exs/iT_quote（仅引号化版本）均通过。
- NegInvolution.lean / NegInvolutionBranches.lean —— 含 sorryAx，不在主链上，与本任务无关，忽略。
- ShCraigElimSetup.lean / ShCraigElimPredicate.lean —— 归纳不变量 P/Q 是 Σ1 谓词，induction_setup 的 10 个支全是 sorry 骨架（编译通过，但无实质证明）。
- ShCraigElimBranches.lean —— 只填了 hWk/hVerumIntro（通过），其余支未填。

## 未编译通过（必须修）

- ShCraigElimNegLaw.lean —— 报错。错误点：
  - and 支：`rw [iT_and hp.isUFormula hq.isUFormula, iT.construction.and, neg_and ..]` 之后目标里是
    `iT param (neg ℒₒᵣ (p ^⋏ q))`，而 iT_and 改写的是 `iT param (p ^⋏ q)`，模式不匹配。
  - or 支：`rw [iT_or ..]` 同样 "Did not find an occurrence of `iT ?m (p ^⋎ q)`"。
  - all/exs 支：`rw [neg_all .., iT_exs .., imp]` 之后 "Failed to rewrite using equation theorems for 'imp'"；
    以及 IsUFormula.imp 被当作函数应用（应为 iff）。
  - 文件末尾 #print axioms 显示 sorryAx，证实含未证。
  修复思路见 03-九支归纳任务拆解/ROUTES.md 的 neg 律一节。

## 包外依赖（第三方 AI 误报“缺失”的，本机齐全）

Foundation 1fb01b72 的 308 个 .lean 全在 06-Foundation闭包/Foundation/；关键模块
DerivabilityCondition/D3.lean、Syntax/CraigTrick.lean、Syntax/Proof/Basic.lean、
Syntax/Proof/Typed.lean、Syntax/Formula/Hierarchy.lean 均在。
（唯一的 FirstOrder/SetTheory/R0/Basic.lean 不在闭包内——因为本包根本不用 R0，无关。）
