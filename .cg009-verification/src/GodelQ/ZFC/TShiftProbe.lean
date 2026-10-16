-- CG-009: attacking obligation tshift
--   translateSeq (setShift s) = setShift (translateSeq s)
-- Both setShift and translateSeq are built via sigma₁_replacement; try a
-- membership-extensionality proof: y ∈ LHS ↔ y ∈ RHS.
import GodelQ.ZFC.GateBranches

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate

namespace GodelQ.TShiftProbe

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- Attempt: translateSeq (setShift s) = setShift (translateSeq s) needs
    iT 0 (shift x) = shift (iT 0 x) at the element level — the iT/shift
    compatibility. Probe whether it is needed as an explicit hypothesis. -/
example (s : V)
    (ishift : ∀ x : V, iT (0 : V) (shift (L := ℒₒᵣ) x) = shift (L := ℒₛₑₜ) (iT (0 : V) x)) :
    translateSeq (V := V) (setShift (L := ℒₒᵣ) s) = setShift (L := ℒₛₑₜ) (translateSeq (V := V) s) := by
  apply Arithmetic.mem_ext; intro y
  rw [mem_translateSeq_iff, mem_setShift_iff]
  constructor
  · rintro ⟨x, hx, rfl⟩
    rw [mem_setShift_iff] at hx
    rcases hx with ⟨x', hx', rfl⟩
    exact ⟨iT (0 : V) x', mem_translateSeq_iff.mpr ⟨x', hx', rfl⟩, by rw [ishift]⟩
  · rintro ⟨y', hy', rfl⟩
    rw [mem_translateSeq_iff] at hy'
    rcases hy' with ⟨x', hx', rfl⟩
    exact ⟨shift (L := ℒₒᵣ) x', mem_setShift_iff.mpr ⟨x', hx', rfl⟩, by rw [ishift]⟩

end GodelQ.TShiftProbe

