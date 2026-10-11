# CG-007 · W8 记录：`IsUFormula.neg_neg` 早已存在（更正上一轮的判断）

> 2026-10-11。本文件是一条**更正记录**，不是新定理。
> 它纠正 `NegInvolution.lean` 头部与上一轮汇报中的一处判断错误。

## 更正什么

上一轮我写下："码层面的 `neg` 对合律 `neg (neg x) = x` 在 Foundation 里**不存在**
（只有元层的 `Semiformula.neg_neg`），需要新的同步归纳。"并据此写了
`NegInvolution.lean`（走 `semiformula_result_induction`，八支 + `param` 无关性辅助引理，
至今仍有未证标记）。

**这个判断是错的。** Foundation 有码层面的对合律：

```lean
-- Foundation/FirstOrder/Arithmetic/Bootstrapping/Syntax/Formula/Functions.lean:127
@[simp] lemma IsUFormula.neg_neg {p : V} :
    IsUFormula L p → Bootstrapping.neg L (Bootstrapping.neg L p) = p
```

本机实测（`#check` + elaboration）确认可用。它的证明用
`IsUFormula.ISigma1.sigma1_succ_induction`（对 `IsUFormula` 的 Σ1 归纳），
比走 `semiformula_result_induction` 直接得多。

**区别只在前提**：它是 `IsUFormula L p`，不是 `IsSemiformula L n p`。
`IsUFormula` 不带层数，是 `Fixpoint ![]`。

## 这对缺口意味着什么

`iT`/`neg` 相容律的 `nrel` 支需要 `neg (neg (iTR param k R v)) = iTR param k R v`。
用 `IsUFormula.neg_neg` 只需 `IsUFormula ℒₛₑₜ (iTR param k R v)`。

**拿它的两条路**（本机都试过）：

1. 从 `isSemiformula_iTR` 取 `.isUFormula`——但它要求
   `IsSemitermVec ℒₒᵣ k n v`，而 `iT_rel` 里的 `hv` 是 `IsUTermVec ℒₒᵣ k v`；
   `IsUTermVec.isSemitermVec` 给的层数是 `listMax (termBVVec ℒₒᵣ k v)`，
   与 `iT` 的层数参数 `param` 不一致。要弥合需 `isSemiformula_mono` 加层数算术。
2. 从 `iT` 的公式性：`iT_rel` 把 `iTR param k R v` 换成 `iT param (^rel k R v)`，
   再用 `isSemiformula_iT` —— 但它同样要求 `IsSemiformula ℒₒᵣ param (^rel k R v)`，
   即 `IsSemitermVec ℒₒᵣ k param v`，同一个层数问题。

**所以真正剩下的是层数记账，不是对合律本身。** 这与 `NegInvolution.lean` 里
`Negation` 的 `allChanges` 默认值问题是同一类：都是"两个递归的层数参数不一致"。

## 应当怎么处置

* `NegInvolution.lean`（走 `semiformula_result_induction` 重建对合律）**不再是必要路线**——
  `IsUFormula.neg_neg` 已提供结论。它的八支核心步骤
  （`NegInvolutionBranches.lean`，CG001-C-397，有收据）仍有独立价值（记录了
  `neg` 的逐构造子行为），但组装完整对合律的工作可以停。
* `iT`/`neg` 相容律的 `nrel` 支应改为：
  `rw [neg_nrel, iT_rel, iT_nrel]` 后用 `IsUFormula.neg_neg`，
  前提义务是 `IsUFormula ℒₛₑₜ (iTR param k R v)` —— 需解决层数记账。

## 教训

Foundation 的 `Formula/Functions.lean` 里有一整段 `IsUFormula.*` 的引理
（`neg_neg`、`neg_iff`、`neg_not_uformula` 等），它们在 `IsUFormula`（无层数）层面工作。
下次遇到"码层面缺某条引理"时，应先在这个文件的 `IsUFormula` 段里找一遍，
而不是假定只有 `Semiformula`（元层）版本。
