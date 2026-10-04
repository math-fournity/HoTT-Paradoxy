/-
  M3 positive control for ZFC-H0-FINAL-PROOF-CLOSURE-SOP.

  This file is compiled against the frozen Foundation Lean formalization of
  Zermelo set theory.  It does not claim that a bare ZFC axiom alone decides
  when an external process has finished.  Its deliberately narrower role is
  to rule out an overstrong candidate reading of Q: a set-theoretic model can
  represent an ordinal-indexed sequence, its domain/length, and a unique value
  at every in-domain index.

  Thus a later claim about inadequate Q-observation has to concern which
  represented data an acceptance interface consumes, or which completion
  bridge it requires.  It cannot rest only on the absence of a primitive
  temporal symbol in the language of set theory.
-/
import Foundation.FirstOrder.SetTheory.Recursion.Seq

namespace ZFCH0ProcessRepresentation

open FFL FirstOrder SetTheory

namespace FFL.FirstOrder.SetTheory

variable {V : Type*} [SetStructure V] [Nonempty V] [V↓[ℒₛₑₜ] ⊧* 𝗭]

/-- An ordinal-indexed trace has an ordinal domain in the frozen Zermelo model. -/
theorem trace_domain_is_ordinal {trace : V} (htrace : Seq trace) :
    IsOrdinal (domain trace) :=
  isOrdinal_domain htrace

/-- Every in-range ordinal stage of a represented trace has exactly one value. -/
theorem trace_stage_has_unique_value {trace stage : V} (htrace : Seq trace)
    (hstage : stage ∈ lh trace) :
    ∃! value : V, ⟨stage, value⟩ₖ ∈ trace :=
  htrace.nth_exists_uniq hstage

/-- The selected sequence value is a member of the trace graph. -/
theorem trace_nth_is_graph_member {trace stage : V} (htrace : Seq trace)
    (hstage : stage ∈ lh trace) :
    ⟨stage, htrace.nth hstage⟩ₖ ∈ trace :=
  htrace.nth_mem hstage

/-- Sequencehood is a first-order set-theoretically definable predicate. -/
theorem trace_predicate_is_set_definable :
    ℒₛₑₜ-predicate (Seq : V → Prop) :=
  seq.definable

/-- The sequence length function is first-order set-theoretically definable. -/
theorem trace_length_is_set_definable :
    ℒₛₑₜ-function₁ (lh : V → V) :=
  lh.definable

#print axioms trace_domain_is_ordinal
#print axioms trace_stage_has_unique_value
#print axioms trace_nth_is_graph_member
#print axioms trace_predicate_is_set_definable
#print axioms trace_length_is_set_definable

end FFL.FirstOrder.SetTheory

end ZFCH0ProcessRepresentation
