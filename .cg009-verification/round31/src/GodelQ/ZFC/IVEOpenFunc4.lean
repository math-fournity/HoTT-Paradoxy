-- CG-009: func branch, right side — entry-wise expansion.
import GodelQ.ZFC.IVEOpenFunc3

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.IVEOpenFunc4
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc2 GodelQ.IVEOpenFunc3

/-- Entry `j` of `QvecV (mm+3)`: `^#j` for `j < mm+3`, `^&0` at `j = mm+3`. -/
lemma nth_QvecV_three (mm j : V) (hj : j ≤ mm + 3) :
    (QvecV (V := V) (mm + 3)).[j] = if j = mm + 3 then (^&0 : V) else ^#j := by
  rcases eq_or_lt_of_le hj with h | h
  · rw [if_pos h, h, nth_QvecV_last]
  · rw [if_neg (ne_of_lt h), nth_QvecV_lt (mm + 3) j h]

end GodelQ.IVEOpenFunc4

#print axioms GodelQ.IVEOpenFunc4.nth_QvecV_three
