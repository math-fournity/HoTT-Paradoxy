-- CG-009: tshift — translateSeq commutes with setShift, unconditional (uses iT_shift).
import GodelQ.ZFC.ITShiftFull

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate
open GodelQ.GateBranches

namespace GodelQ.TShiftFull
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`tshift`, unconditional**: `translateSeq (setShift s) = setShift (translateSeq s)`.
    Reduces (via `GateBranches.tshift_of_ishift`) to the element law, now available
    unconditionally for *formula* elements via `iT_shift`. -/
theorem tshift (s : V) (hs : IsFormulaSet (L := ℒₒᵣ) s) :
    translateSeq (V := V) (setShift (L := ℒₒᵣ) s) =
      setShift (L := ℒₛₑₜ) (translateSeq (V := V) s) := by
  apply Arithmetic.mem_ext; intro y
  rw [mem_translateSeq_iff, mem_setShift_iff]
  constructor
  · rintro ⟨x, hx, rfl⟩
    rw [mem_setShift_iff] at hx
    rcases hx with ⟨x', hx', rfl⟩
    refine ⟨iT (0 : V) x', mem_translateSeq_iff.mpr ⟨x', hx', rfl⟩, ?_⟩
    exact GodelQ.ITShiftFull.iT_shift x' (hs x' hx')
  · rintro ⟨y', hy', rfl⟩
    rw [mem_translateSeq_iff] at hy'
    rcases hy' with ⟨x', hx', rfl⟩
    refine ⟨shift (L := ℒₒᵣ) x', mem_setShift_iff.mpr ⟨x', hx', rfl⟩, ?_⟩
    exact (GodelQ.ITShiftFull.iT_shift x' (hs x' hx')).symm

end GodelQ.TShiftFull

#print axioms GodelQ.TShiftFull.tshift
