-- CG-009: extracted from 9276's ShCraigElimSetupQ for independent verification.
import GodelQ.ZFC.TShiftBranches

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.ProvableSeq
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

lemma provable_into_sequent {A B : V} (hB : IsFormulaSet (L := ℒₛₑₜ) B)
    (hd : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert A ∅)) :
    Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert A B) := by
  have hA : IsFormula ℒₛₑₜ A := hd.isFormulaSet A (by simp)
  have hf : IsFormulaSet (L := ℒₛₑₜ) (insert A B) := by
    intro z hz
    rcases mem_bitInsert_iff.mp hz with rfl | hz
    · exact hA
    · exact hB z (by simpa using hz)
  refine Derivable.wk hf ?_ hd
  intro z hz
  rcases mem_bitInsert_iff.mp hz with rfl | hz
  · exact mem_bitInsert_iff.mpr (Or.inl rfl)
  · exact mem_bitInsert_iff.mpr (Or.inr (by simpa using hz))


end GodelQ.ProvableSeq
