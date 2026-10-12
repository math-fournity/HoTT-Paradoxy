-- CG-009: entry-wise expansions of the two sides of the func vector identity.
import GodelQ.ZFC.IVEOpenFunc2

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.IVEOpenFunc3
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc2

/-- Entry `j` of `QvecV (mm+1)`: `^#j` for `j < mm+1`, `^&0` at `j = mm+1`. -/
lemma nth_QvecV_succ (mm j : V) (hj : j < (mm + 1) + 1) :
    (QvecV (V := V) (mm + 1)).[j] = if j = mm + 1 then (^&0 : V) else ^#j := by
  rcases eq_or_lt_of_le (lt_succ_iff_le.mp hj) with h | h
  · rw [if_pos h, h, nth_QvecV_last]
  · rw [if_neg (ne_of_lt h), nth_QvecV_lt (mm + 1) j h]

/-- **Left side, entry-wise**: substituting `V` into `QvecV (mm+1)`. -/
lemma nth_left (mm i j : V) (hj : j < (mm + 1) + 1) :
    (termSubstVec ℒₛₑₜ ((mm + 1) + 1) ((^#i : V) ∷ shiftVec 3 (mm + 1))
      (QvecV (V := V) (mm + 1))).[j] =
      if j = 0 then (^#i : V) else if j = mm + 1 then ^&0 else ^#(j + 2) := by
  rw [nth_termSubstVec (isSemitermVec_QvecV (mm + 1)).isUTerm hj, nth_QvecV_succ mm j hj]
  by_cases heq : j = mm + 1
  · -- j = mm + 1 : the source entry is the *fvar* ^&0, which termSubst leaves alone.
    rw [if_pos heq, termSubst_fvar]
    have hne : ¬(j = 0) := by
      intro h0
      exact (zero_ne_add_one mm) (h0 ▸ heq : (0 : V) = mm + 1)
    rw [if_neg hne, if_pos heq]
  · -- j ≠ mm+1 : source entry is ^#j, so termSubst reads V.[j]
    rw [if_neg heq, termSubst_bvar, nth_V mm i j hj]
    by_cases h0 : j = 0
    · rw [if_pos h0, if_pos h0]
    · rw [if_neg h0, if_neg h0, if_neg heq]

end GodelQ.IVEOpenFunc3

#print axioms GodelQ.IVEOpenFunc3.nth_QvecV_succ
#print axioms GodelQ.IVEOpenFunc3.nth_left

namespace GodelQ.IVEOpenFunc3
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc2

end GodelQ.IVEOpenFunc3
