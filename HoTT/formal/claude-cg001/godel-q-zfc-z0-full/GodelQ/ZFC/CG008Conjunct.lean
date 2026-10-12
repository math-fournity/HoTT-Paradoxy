import GodelQ.ZFC.CG008VeLevel
import GodelQ.ZFC.CG008ITTR

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open GodelQ.ZFCArith GodelQ.Translate
open GodelQ.CG008VeParts GodelQ.CG008VeLevel GodelQ.CG008ITTR
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
namespace GodelQ.CG008Conjunct
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

set_option maxHeartbeats 800000 in
/-- **`cDomN` 是层 1 的公式**（`conjunct` 第一块要的）。 -/
lemma cDomN_isSemiformula :
    Bootstrapping.IsSemiformula ℒₛₑₜ 1 ((Translate.cDomN : ℕ) : V) := by
  rw [Translate.cDomN]
  rw [FFL.FirstOrder.Sentence.coe_quote_eq_quote (V := V) (L := ℒₛₑₜ) (n := 1)]
  simpa [Nat.cast_one] using
    FFL.FirstOrder.Sentence.quote_isSemiformula (V := V) (L := ℒₛₑₜ) (n := 1) _

set_option maxHeartbeats 800000 in
lemma conjunct_isUFormula (b n i y : V) (hy : Bootstrapping.IsUFormula ℒₛₑₜ y) :
    Bootstrapping.IsUFormula ℒₛₑₜ (Translate.conjunct b n i y) := by
  rw [Translate.conjunct]
  refine Bootstrapping.IsUFormula.and.mpr ⟨?_, ?_⟩
  · exact GodelQ.CG008VeParts.subst_singleton_isUFormula i cDomN_isSemiformula
  · sorry

end GodelQ.CG008Conjunct