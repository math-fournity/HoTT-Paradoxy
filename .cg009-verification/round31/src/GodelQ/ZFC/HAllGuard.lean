-- CG-009: hAll route — prove 9276's guard step ③ (pure Derivable manipulation), and probe ②.
import GodelQ.ZFC.TShiftBranches

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.HAllGuard
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- ③ Guard step: `Derivable (insert A S) → Derivable (insert (B → A) S)`
    (via or_m + wk). This is what lets hAll trade the free-form for a guarded form. -/
theorem guard_step {A B S : V} (hA : IsFormula ℒₛₑₜ A) (hB : IsFormula ℒₛₑₜ B)
    (hS : IsFormulaSet (L := ℒₛₑₜ) S)
    (hd : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert A S)) :
    Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert (imp ℒₛₑₜ B A) S) := by
  have hfs : IsFormulaSet (L := ℒₛₑₜ) (neg ℒₛₑₜ B ⫽ A ⫽ imp ℒₛₑₜ B A ⫽ S) := by
    intro p hp
    simp only [mem_bitInsert_iff] at hp
    rcases hp with rfl | rfl | rfl | hp
    · exact hB.neg
    · exact hA
    · exact IsSemiformula.or.mpr ⟨hB.neg, hA⟩
    · exact hS p hp
  refine Derivable.or_m (s := insert (imp ℒₛₑₜ B A) S)
    (p := neg ℒₛₑₜ B) (q := A) (by simp [imp]) ?_
  refine Derivable.wk hfs ?_ hd
  intro x hx
  simp only [mem_bitInsert_iff] at hx ⊢
  tauto

end GodelQ.HAllGuard

#print axioms GodelQ.HAllGuard.guard_step
