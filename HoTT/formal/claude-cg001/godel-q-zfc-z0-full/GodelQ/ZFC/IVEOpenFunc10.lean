-- CG-009: the func branch's cFunc piece — the identity part (proven).
--
-- ## Which layer of `QvecV` acts here
--
-- `subst` descends a binder by replacing the vector `W` with `qVec W`.  In `ve2`
-- the body substitution sits under `qqAlls … 2` (two binders), so when `subst`
-- reaches the body the opening vector has become
--     qVec²(QvecV (mm+1)) = QvecV (mm+3)   (by `QvecV_succ` twice)
-- of length `mm+4`.  The body vector `[^#2, ^#0, ^#1]` reads only indices `0,1,2`,
-- and `2 < mm+3` always, so `QvecV (mm+3)` is the identity on all three.
import GodelQ.ZFC.IVEOpenFunc8
import GodelQ.ZFC.IVEOpenFunc9

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.IVEOpenFunc10
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc2 GodelQ.IVEOpenFunc3 GodelQ.IVEOpenFunc4
open GodelQ.IVEOpenFunc5 GodelQ.IVEOpenFunc6 GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFunc9

/-- `2 < mm + 3` always. -/
lemma two_lt_add_three (mm : V) : (2 : V) < mm + 3 := by
  have h := lt_add_self_add_one 2 mm
  have e : (mm + 2 : V) + 1 = mm + 3 := by ring
  rwa [e] at h

/-- `i < mm + 3` for any `i ≤ 2`. -/
lemma lt_add_three {i mm : V} (hi : i ≤ 2) : i < mm + 3 :=
  lt_of_le_of_lt hi (two_lt_add_three mm)

/-- **The three-index identity**: `QvecV (mm+3)` fixes `[^#2, ^#0, ^#1]`. -/
lemma termSubstVec_three_QvecV_three {mm : V} :
    termSubstVec ℒₛₑₜ 3 (QvecV (V := V) (mm + 3))
        ((^#2 : V) ∷ (^#0 : V) ∷ (^#1 : V) ∷ (0 : V)) =
      (^#2 : V) ∷ (^#0 : V) ∷ (^#1 : V) ∷ (0 : V) := by
  apply nth_ext' 3
  · rw [len_termSubstVec isUTermVec_three_bvars, isUTermVec_three_bvars.lh]
  · rw [isUTermVec_three_bvars.lh]
  · intro j hj
    have hle : j ≤ 2 := lt_succ_iff_le.mp (by
      simpa [show (3 : V) = 2 + 1 by norm_num] using hj)
    rcases le_two_iff_eq_zero_or_one_or_two.mp hle with rfl | rfl | rfl
    · rw [nth_termSubstVec isUTermVec_three_bvars (by norm_num : (0 : V) < 3),
        nth_adjoin_zero, termSubst_bvar, nth_QvecV_lt (mm + 3) 2 (two_lt_add_three mm)]
    · rw [nth_termSubstVec isUTermVec_three_bvars (by norm_num : (1 : V) < 3)]
      rw [show ((^#2 : V) ∷ (^#0 : V) ∷ (^#1 : V) ∷ (0 : V)).[1] = ^#0 from by
        rw [show (1 : V) = 0 + 1 by norm_num, nth_adjoin_succ, nth_adjoin_zero]]
      rw [termSubst_bvar, nth_QvecV_lt (mm + 3) 0 (lt_add_three (by norm_num : (0 : V) ≤ 2))]
    · rw [nth_termSubstVec isUTermVec_three_bvars (by norm_num : (2 : V) < 3)]
      rw [show ((^#2 : V) ∷ (^#0 : V) ∷ (^#1 : V) ∷ (0 : V)).[2] = ^#1 from by
        rw [show (2 : V) = 1 + 1 by norm_num, nth_adjoin_succ,
          show (1 : V) = 0 + 1 by norm_num, nth_adjoin_succ, nth_adjoin_zero]]
      rw [termSubst_bvar, nth_QvecV_lt (mm + 3) 1 (lt_add_three (by norm_num : (1 : V) ≤ 2))]

end GodelQ.IVEOpenFunc10

#print axioms GodelQ.IVEOpenFunc10.termSubstVec_three_QvecV_three
