import GodelQ.ZFC.ShCraigElimNegLaw

/-!
# 负控制：`iT`/`neg` 相容律的层数写错时被内核拒绝

`iT_neg` 的 `all`/`exs` 支依赖 `iT_all`/`iT_exs` 把层数**提升一**（`n ↦ n+1`），
所以归纳假设只在层数 `n+1` 上可用。本文件故意给出层数不动的归纳假设
（`iT n` 对 `iT (n+1)`），内核应当拒绝：目标里出现的是 `iT (n+1) (neg p)`，
最后一步的 `← ih` 找不到可改写的出现位置。

本文件**不是**任何运行的编译源；它的用途只是证明相容律的量词支不是空转。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.ShCraigElimNegLaw

open GodelQ.Translate GodelQ.ZFCArith GodelQ.SeqTranslate GodelQ.ShCraigElimNegFilled

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- 错误的层数（归纳假设应为 `iT (n+1) (neg p) = neg (iT (n+1) p)`）：内核必须拒绝。 -/
example {n p : V} (hp : IsSemiformula ℒₒᵣ (n + 1) p)
    (ih : iT n (neg ℒₒᵣ p) = neg ℒₛₑₜ (iT n p)) :
    iT n (neg ℒₒᵣ (^∀ p)) = neg ℒₛₑₜ (iT n (^∀ p)) := by
  rw [neg_all (L := ℒₒᵣ) hp.isUFormula, iT_exs (IsUFormula.neg hp.isUFormula),
    iT_all hp.isUFormula]
  rw [neg_all (L := ℒₛₑₜ) (IsUFormula.imp.mpr
    ⟨(isSemiformula_domZero (n := n)).isUFormula, (isSemiformula_iT p hp).isUFormula⟩)]
  have hneg : neg ℒₛₑₜ (imp ℒₛₑₜ domZero (iT (n+1) p)) =
      (neg ℒₛₑₜ (neg ℒₛₑₜ domZero) ^⋏ neg ℒₛₑₜ (iT (n+1) p) : V) :=
    neg_or (L := ℒₛₑₜ) (isSemiformula_domZero (n := n)).isUFormula.neg
      (isSemiformula_iT p hp).isUFormula
  rw [hneg, IsUFormula.neg_neg (isSemiformula_domZero (n := n)).isUFormula, ← ih]

end GodelQ.ShCraigElimNegLaw
