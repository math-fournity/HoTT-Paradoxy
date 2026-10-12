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
lemma nth_right_ne_zero {mm j : V} (h0 : ¬(j = 0)) (hj : j < mm + 2) :
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

namespace GodelQ.IVEOpenFunc5
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc2 GodelQ.IVEOpenFunc3 GodelQ.IVEOpenFunc4

/-- **Right side, entry-wise**: substituting `QvecV (mm+3)` into `V`.

`hi2 : i ≠ mm + 3` is needed: the source entry `^#i` reads `QvecV (mm+3)`'s *last*
slot exactly when `i = mm + 3`, where it would become `^&0` instead of `^#i`.
In the actual `ve2` use `i = 2` and `mm + 3 ≥ 3`, so the hypothesis is free. -/
lemma nth_right (mm i j : V) (hi : i < mm + 4) (hi2 : i ≠ mm + 3)
    (hj : j < (mm + 1) + 1) :
    (termSubstVec ℒₛₑₜ ((mm + 1) + 1) (QvecV (V := V) (mm + 3))
      ((^#i : V) ∷ shiftVec 3 (mm + 1))).[j] =
      if j = 0 then (^#i : V) else if j = mm + 1 then ^&0 else ^#(j + 2) := by
  have hj2 : j < mm + 2 := by
    have e : (mm + 1) + 1 = mm + 2 := by ring
    rwa [e] at hj
  rw [show ((mm + 1) + 1 : V) = mm + 2 by ring]
  rw [nth_termSubstVec (isSemitermVec_cons_shiftVec3 mm i hi).isUTerm hj2]
  rw [show termSubst ℒₛₑₜ (QvecV (V := V) (mm + 3))
        (((^#i : V) ∷ shiftVec 3 (mm + 1)).[j])
      = termSubst ℒₛₑₜ (QvecV (V := V) (mm + 3))
        (if j = 0 then (^#i : V) else ^#(j + 2)) from by
    rw [nth_V mm i j hj]]
  by_cases h0 : j = 0
  · -- j = 0 : source is ^#i, an identity slot since i ≤ mm+3
    rw [if_pos h0, if_pos h0, termSubst_bvar,
      nth_QvecV_three mm i (lt_succ_iff_le.mp (by
        have e : (mm + 3) + 1 = mm + 4 := by ring
        rwa [e])),
      if_neg hi2]
  · -- j ≠ 0 : the source entry is ^#(j+2)
    rw [if_neg h0, if_neg h0]
    exact nth_right_ne_zero h0 hj2

end GodelQ.IVEOpenFunc5

#print axioms GodelQ.IVEOpenFunc5.nth_right
