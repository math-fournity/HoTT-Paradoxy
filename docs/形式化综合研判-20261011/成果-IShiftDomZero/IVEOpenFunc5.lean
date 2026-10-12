-- CG-009: func branch, right side — a cleaner route through `nth_V` + case analysis.
import GodelQ.ZFC.IVEOpenFunc4

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.IVEOpenFunc5
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc2 GodelQ.IVEOpenFunc3 GodelQ.IVEOpenFunc4

/-- Entry `j` of the **right** side, in the `j ≠ 0` case where the source entry is `^#(j+2)`. -/
lemma nth_right_ne_zero {mm i j : V} (h0 : ¬(j = 0)) (hj : j < mm + 2) :
    termSubst ℒₛₑₜ (QvecV (V := V) (mm + 3)) (^#(j + 2) : V) =
      if j = mm + 1 then (^&0 : V) else ^#(j + 2) := by
  rw [termSubst_bvar]
  by_cases heq : j = mm + 1
  · rw [if_pos heq, heq]
    have : mm + 1 + 2 = mm + 3 := by ring
    rw [this, nth_QvecV_last]
  · rw [if_neg heq]
    apply nth_QvecV_lt (mm + 3) (j + 2)
    have hj' : j < (mm + 1) + 1 := by
      have e : mm + 2 = (mm + 1) + 1 := by ring
      rwa [e] at hj
    have h1 : j ≤ mm + 1 := lt_succ_iff_le.mp hj'
    by_contra hcon
    have h2 : mm + 3 ≤ j + 2 := le_of_not_gt hcon
    have h3 : j + 2 ≤ mm + 3 := by
      have hh := add_le_add_right h1 2
      rw [show (2 : V) + j = j + 2 by ring, show (2 : V) + (mm + 1) = mm + 3 by ring] at hh
      exact hh
    have h4 : j + 2 = mm + 3 := le_antisymm h3 h2
    exact heq (by
      have h5 : j + 2 = mm + 1 + 2 := by rw [h4]; ring
      exact add_right_cancel h5)

end GodelQ.IVEOpenFunc5

#print axioms GodelQ.IVEOpenFunc5.nth_right_ne_zero
