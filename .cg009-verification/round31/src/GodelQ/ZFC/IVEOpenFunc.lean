-- CG-009: the `func` branch of the `iVE` opening law.
--
-- ## The vector identity that drives it
--
-- For `mm : V` and `i ∈ {0,1}` both
--     termSubstVec (mm+2) (^#i ∷ shiftVec 3 (mm+1)) (QvecV (mm+1))
--     termSubstVec (mm+2) (QvecV (mm+3)) (^#i ∷ shiftVec 3 (mm+1))
-- equal the same explicit vector `OV mm i = [^#i, ^#3, …, ^#(mm+2), ^&0]` (length mm+2).
--
-- Left  side: `QvecV (mm+1)`'s entries are `^#j` (j < mm+1) and `^&0` (j = mm+1);
--   applying `V = ^#i ∷ shiftVec 3 (mm+1)` sends `^#0 ↦ ^#i` and `^#j ↦ ^#(j+2)`.
-- Right side: `V`'s entries are `^#i` and `^#(j+2)`; applying `W' = QvecV (mm+3)`
--   is the identity on indices `< mm+3` and sends index `mm+3` to `^&0`.
-- The two agree because the only index reaching `mm+3` on the right is the one that
-- reads `QvecV (mm+1)`'s last entry `^&0` on the left.
import GodelQ.ZFC.IVESubstOpen3

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.IVEOpenFunc
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat

/-- `shiftVec 3 (mm+1)` is a `ℒₛₑₜ`-term vector of length `mm+1` at layer `mm+4`. -/
lemma isSemitermVec_shiftVec3 (mm : V) :
    IsSemitermVec ℒₛₑₜ (mm + 1) (mm + 4) (shiftVec 3 (mm + 1)) := by
  have h := isSemitermVec_shiftVec_V 3 (mm + 1)
  rwa [show (3 : V) + (mm + 1) = mm + 4 by ring] at h

/-- `^#i ∷ shiftVec 3 (mm+1)` is a term vector of length `mm+2` at layer `mm+4`. -/
lemma isSemitermVec_cons_shiftVec3 (mm i : V) (hi : i < mm + 4) :
    IsSemitermVec ℒₛₑₜ (mm + 2) (mm + 4) ((^#i : V) ∷ shiftVec 3 (mm + 1)) := by
  rw [show (mm + 2 : V) = (mm + 1) + 1 by ring, IsSemitermVec.cons_iff]
  exact ⟨IsSemiterm.bvar.mpr hi, isSemitermVec_shiftVec3 mm⟩

/-- Entry `j` of `QvecV m`: `^#j` for `j < m`, `^&0` for `j = m`. -/
lemma nth_QvecV (m j : V) (hj : j ≤ m) :
    (QvecV (V := V) m).[j] = if j = m then (^&0 : V) else ^#j := by
  rcases eq_or_lt_of_le hj with rfl | hlt
  · rw [if_pos rfl, nth_QvecV_last]
  · rw [if_neg (ne_of_lt hlt), nth_QvecV_lt m j hlt]

end GodelQ.IVEOpenFunc

#print axioms GodelQ.IVEOpenFunc.nth_QvecV
#print axioms GodelQ.IVEOpenFunc.isSemitermVec_cons_shiftVec3
