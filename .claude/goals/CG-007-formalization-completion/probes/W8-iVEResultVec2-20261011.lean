import GodelQ.ZFC.TranslateShiftCompat

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

namespace GodelQ.ProbeB

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- `iVE` 对二元项向量：`resultVec` 的两个分量都是 `iVE`。 -/
lemma iVE_resultVec_two {n k f v : V} (hv : IsUTermVec ℒₒᵣ k v) (hk : k = 2) :
    iVE.construction.resultVec ℒₒᵣ ![n] k v =
      ?[iVE n v.[0], iVE n v.[1]] := by
  subst hk
  apply nth_ext' 2
  · rw [iVE.construction.resultVec_lh ℒₒᵣ ![n] hv]
  · simp [show (2 : V) = 1 + 1 by norm_num]
  · intro i hi
    rw [iVE.construction.nth_resultVec ℒₒᵣ ![n] hv hi]
    rcases le_one_iff_eq_zero_or_one.mp (lt_two_iff_le_one.mp hi) with rfl | rfl <;> simp [iVE]

end GodelQ.ProbeB
