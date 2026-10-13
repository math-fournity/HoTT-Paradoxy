-- CG-009: the func branch's vector identity — entry-wise description.
import GodelQ.ZFC.IVEOpenFunc

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.IVEOpenFunc2
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat GodelQ.IVEOpenFunc

/-- Entry `j` of `V := ^#i ∷ shiftVec 3 (mm+1)`: `^#i` at 0, `^#(j+2)` otherwise. -/
lemma nth_V (mm i j : V) (hj : j < (mm + 1) + 1) :
    ((^#i : V) ∷ shiftVec 3 (mm + 1)).[j] =
      if j = 0 then (^#i : V) else ^#(j + 2) := by
  rcases zero_or_succ j with rfl | ⟨j', rfl⟩
  · simp
  · rw [nth_adjoin_succ]
    have hj' : j' < mm + 1 := by
      have h2 : j' + 1 < mm + 1 + 1 := by simpa using hj
      exact add_lt_add_iff_right (1 : V) |>.mp h2
    rw [nth_shiftVec 3 (mm + 1) j' hj',
      if_neg (by simp : ¬(j' + 1 = 0 : Prop))]
    congr 1
    ring

end GodelQ.IVEOpenFunc2

#print axioms GodelQ.IVEOpenFunc2.nth_V
