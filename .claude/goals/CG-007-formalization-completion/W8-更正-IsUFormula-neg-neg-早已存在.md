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

### 层数障碍的精确形状（本机进一步实测）

`isSemiformula_iTR` 的签名是

```lean
lemma isSemiformula_iTR {n k R v : V} (hR : ℒₒᵣ.IsRel k R)
    (hv : IsSemitermVec ℒₒᵣ k n v) : IsSemiformula ℒₛₑₜ n (iTR n k R v)
```

**注意 `n` 出现了三次**：它既是项向量的层数、又是输出公式的层数、还是 `iTR` 自己的参数。
而 `iT_rel` 只给 `IsUTermVec ℒₒᵣ k v`（无层数），
`IsUTermVec.isSemitermVec` 产出的层数是 `listMax (termBVVec ℒₒᵣ k v)`——
即"项向量里出现的最大 bound variable 索引"。

**要把它提到 `param` 需要 `listMax (termBVVec ℒₒᵣ k v) ≤ param`，
而这个不等式在 `IsUTermVec` 下不成立**：项可以引用任意大的 bound var。
（`IsUTerm` 只要求是良构的项，不限制它引用哪些变量。）

**同时 `iTR` 真的依赖 `param`**：展开是
`qqAlls (imp (conjunct 2 param 0 (iVE param v.[0]) ^⋏ …) …) 2`，
`param` 出现在 `conjunct` 与 `iVE` 的参数位。所以也不能用
`iTR listMax = iTR param` 绕过去。

**结论**：`nrel` 支的完整证明需要
`IsUFormula ℒₛₑₜ (iTR param k R v)`，而它的两条来路（`isSemiformula_iTR` 与
`isSemiformula_iT` + `iT_rel`）都卡在同一个层数不等式上。
下一步要么证那个不等式（在 `iT` 的调用语境下 `param` 确实足够大——
因为 `induction1` 的支里 `param` 来自 `iT` 自己的层数记账），
要么改用别的途径拿 `IsUFormula (iTR param k R v)`（如逐构造子拼，
本机已验证 `iTR` 的展开式在 `IsUFormula` 层面结构正确）。

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
