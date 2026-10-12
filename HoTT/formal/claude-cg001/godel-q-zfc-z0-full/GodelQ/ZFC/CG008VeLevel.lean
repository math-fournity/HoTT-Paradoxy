import GodelQ.ZFC.CG008VeParts

/-!
# CG-008 · `ve0` 的最后一跳：`cFunc` 的层数分派
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008VeLevel
open GodelQ.ZFCArith GodelQ.Translate GodelQ.CG008VeParts
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- **关键观察**：`subst L w q` 要 `IsSemitermVec L n m w` 且 `len w = n`。
-- `?[^#0]` 的 `len` 是 1，所以公式的层数必须是 **1**。
-- 而 `cFunc k f` 在 `k = 0` 时是 1 元公式（`“z. isEmpty z”` 等），层数 1；
-- `k ≠ 0` 时是 3 元公式（add/mul），层数 3。
-- **`ve0` 只在 `k = 0` 时被 `iVE.construction` 调用**（`if k = 0 then ve0 k f else ve2 …`），
-- 所以只需 `k = 0` 的情形。
lemma cFunc_isSemiformula_one {k f : V} (hk : k = 0) :
    Bootstrapping.IsSemiformula ℒₛₑₜ 1 (Translate.cFunc k f) := by
  subst hk
  rw [Translate.cFunc]
  by_cases hf : f = 0 <;> simp only [hf, ↓reduceIte, Translate.cFuncN, ite_true, ite_false]
  all_goals try (norm_num)
  · rw [FFL.FirstOrder.Sentence.coe_quote_eq_quote (V := V) (L := ℒₛₑₜ) (n := 1)
      (arithTrln.func Language.ORing.Func.zero)]
    simpa [Nat.cast_one] using
      FFL.FirstOrder.Sentence.quote_isSemiformula (V := V) (L := ℒₛₑₜ) (n := 1) _
  · rw [FFL.FirstOrder.Sentence.coe_quote_eq_quote (V := V) (L := ℒₛₑₜ) (n := 1)
      (arithTrln.func Language.ORing.Func.one)]
    simpa [Nat.cast_one] using
      FFL.FirstOrder.Sentence.quote_isSemiformula (V := V) (L := ℒₛₑₜ) (n := 1) _

/-- **`ve0 k f` 是公式**（`k = 0` 的情形，即 `iVE.construction` 实际调用的那支）。 -/
lemma ve0_isUFormula {k f : V} (hk : k = 0) :
    Bootstrapping.IsUFormula ℒₛₑₜ (Translate.ve0 k f) := by
  rw [Translate.ve0]
  refine Bootstrapping.IsUFormula.imp.mpr ⟨Bootstrapping.IsUFormula.verum, ?_⟩
  exact GodelQ.CG008VeParts.subst_singleton_isUFormula (V := V) 0 (cFunc_isSemiformula_one hk)

end GodelQ.CG008VeLevel

#print axioms GodelQ.CG008VeLevel.cFunc_isSemiformula_one
#print axioms GodelQ.CG008VeLevel.ve0_isUFormula
