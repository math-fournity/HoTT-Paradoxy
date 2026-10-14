import GodelQ.ZFC.SeqTranslateFormula

/-!
# CG-007 · W8 第二层（十）：码层面 `neg` 的对合律

`iT`/`neg` 相容律的 `nrel` 支需要码层面的对合律 `neg (neg x) = x`。

## 结论：不需要新证，Foundation 已有

前几轮（`ShCraigElimNegFilled.lean` 的文档、`ShCraigElimNegGen.lean` 的「真实子障碍」节）
记载「Foundation 只有元层的 `Semiformula.neg_neg`，码层面的没有现成引理」。
**这条记载不成立。** Foundation 在 `Syntax/Formula/Functions.lean:127` 就有

```lean
@[simp] lemma IsUFormula.neg_neg {p : V} :
    IsUFormula L p → Bootstrapping.neg L (Bootstrapping.neg L p) = p
```

而 `Bootstrapping.neg L p := Negation.construction.result L 0 p` 正是码层面的 `neg`。
所以本文件只是把 `IsSemiformula` 的公式性取出 `IsUFormula`，交给该引理即可——
不需要沿 `semiformula_result_induction` 重做一遍归纳。

（本机实测：`IsUFormula.neg_neg hp.isUFormula` 直接编译通过，exit 0。）
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

namespace GodelQ.NegInvolution

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- `neg` 保持公式性（码层面）：由 `IsSemiformula.neg` 给出。 -/
lemma isSemiformula_neg {n p : V} (hp : IsSemiformula ℒₒᵣ n p) :
    IsSemiformula ℒₒᵣ n (neg ℒₒᵣ p) :=
  IsSemiformula.neg hp

/-- `IsUFormula` 版的推论（`n` 任取 0 即可，公式性只要求某个层数）。 -/
lemma isUFormula_neg {p : V} (hp : IsUFormula ℒₒᵣ p) : IsUFormula ℒₒᵣ (neg ℒₒᵣ p) :=
  hp.neg

/-- **码层面的 `neg` 对合律**：`neg (neg p) = p`，对 V 内任意公式码成立。

直接取自 Foundation 的 `IsUFormula.neg_neg`（`Bootstrapping.neg` 就是码层面的 `neg`）。 -/
theorem neg_neg_code : ∀ {n p : V}, IsSemiformula ℒₒᵣ n p → neg ℒₒᵣ (neg ℒₒᵣ p) = p :=
  fun hp ↦ IsUFormula.neg_neg hp.isUFormula

end GodelQ.NegInvolution

#print axioms GodelQ.NegInvolution.neg_neg_code
