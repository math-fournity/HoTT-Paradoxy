-- CG-009: hShift, unconditional — inlines hShift's proof with tshift at fstIdx d.
import GodelQ.ZFC.TShiftFull

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate
open GodelQ.GateBranches

namespace GodelQ.TShiftBranches
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- General: if `setShift s' = s` and `s` is a formula set, so is `s'`. -/
lemma isFormulaSet_of_setShift_eq {s s' : V}
    (hs : IsFormulaSet (L := ℒₒᵣ) s) (h : s = setShift (L := ℒₒᵣ) s') :
    IsFormulaSet (L := ℒₒᵣ) s' := by
  intro p hp
  have hmem : shift (L := ℒₒᵣ) p ∈ s := by
    rw [h]; exact shift_mem_setShift hp
  exact (IsSemiformula.shift_iff.mp (hs (shift (L := ℒₒᵣ) p) hmem))

/-- **`hShift`, unconditional**: same proof as `GateBranches.hShift`, with `tshift` supplied
    at `fstIdx d` (the only call site) from the proven `TShiftFull.tshift`. -/
theorem hShift_uncond {s d : V}
    (hs : IsFormulaSet (L := ℒₒᵣ) s)
    (h : s = setShift (L := ℒₒᵣ) (fstIdx d)) (ih : Q d) : Q (shiftRule s d) := by
  have hts := GodelQ.TShiftFull.tshift (fstIdx d) (isFormulaSet_of_setShift_eq hs h)
  simp only [Q, fstIdx_shiftRule]
  rw [h, hts]
  exact Derivable.shift ih

end GodelQ.TShiftBranches

#print axioms GodelQ.TShiftBranches.hShift_uncond
