/-
  Expected-rejection control for C-366.

  The frozen sequence interface gives exactly one graph value at an in-domain
  ordinal stage.  This file deliberately tries to manufacture two distinct
  values at that same stage.  The last `rfl` cannot inhabit `value ≠ value`.
-/
import Foundation.FirstOrder.SetTheory.Recursion.Seq

namespace WrongZFCH0ProcessRepresentation

open FFL FirstOrder SetTheory

namespace FFL.FirstOrder.SetTheory

variable {V : Type*} [SetStructure V] [Nonempty V] [V↓[ℒₛₑₜ] ⊧* 𝗭]

theorem wrong_trace_stage_has_two_distinct_values {trace stage : V}
    (htrace : Seq trace) (hstage : stage ∈ lh trace) :
    ∃ value₁ value₂ : V,
      ⟨stage, value₁⟩ₖ ∈ trace ∧
      ⟨stage, value₂⟩ₖ ∈ trace ∧
      value₁ ≠ value₂ := by
  obtain ⟨value, hvalue⟩ := htrace.exists hstage
  exact ⟨value, value, hvalue, hvalue, by rfl⟩

end FFL.FirstOrder.SetTheory

end WrongZFCH0ProcessRepresentation
