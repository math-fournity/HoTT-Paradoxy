-- CG-009: the func vector identity — assembling nth_left and nth_right.
import GodelQ.ZFC.IVEOpenFunc5

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.IVEOpenFunc6
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc2 GodelQ.IVEOpenFunc3 GodelQ.IVEOpenFunc4
open GodelQ.IVEOpenFunc5

/-- **The func vector identity**: the two ways of "opening" agree.
    `nth_left` and `nth_right` give the same entry-wise description. -/
lemma substVec_func_eq (mm i : V) (hi : i < mm + 4) (hi2 : i ≠ mm + 3) :
    termSubstVec ℒₛₑₜ ((mm + 1) + 1) ((^#i : V) ∷ shiftVec 3 (mm + 1))
        (QvecV (V := V) (mm + 1)) =
      termSubstVec ℒₛₑₜ ((mm + 1) + 1) (QvecV (V := V) (mm + 3))
        ((^#i : V) ∷ shiftVec 3 (mm + 1)) := by
  apply nth_ext' ((mm + 1) + 1)
  · rw [len_termSubstVec (isSemitermVec_QvecV (mm + 1)).isUTerm]
  · rw [show ((mm + 1) + 1 : V) = mm + 2 by ring]
    rw [len_termSubstVec (isSemitermVec_cons_shiftVec3 mm i hi).isUTerm]
  · intro j hj
    rw [nth_left mm i j hj]
    rw [show (termSubstVec ℒₛₑₜ ((mm + 1) + 1) (QvecV (V := V) (mm + 3))
          ((^#i : V) ∷ shiftVec 3 (mm + 1))).[j]
        = (termSubstVec ℒₛₑₜ (mm + 2) (QvecV (V := V) (mm + 3))
          ((^#i : V) ∷ shiftVec 3 (mm + 1))).[j] from by
      rw [show ((mm + 1) + 1 : V) = mm + 2 by ring]]
    rw [nth_right mm i j hi hi2 (by
      have e : (mm + 2 : V) = (mm + 1) + 1 := by ring
      rwa [← e] at hj)]

end GodelQ.IVEOpenFunc6

#print axioms GodelQ.IVEOpenFunc6.substVec_func_eq
