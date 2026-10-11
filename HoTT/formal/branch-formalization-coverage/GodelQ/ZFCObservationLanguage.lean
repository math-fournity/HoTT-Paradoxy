/-!
`MP-ZFC-OBSERVATION-LANGUAGE-BOUNDARY-001` formalizes one deliberately
limited reading of the proposed missing observation power Q.

It does *not* encode the ZFC axiom scheme, construct a ZFC model, or prove
that ZFC cannot represent time, sequences, computation, or a chosen completion
predicate.  Instead it proves a semantic boundary that applies to any base
theory whose models expose only membership information: an extra predicate
`originDone` is not fixed until a completion bridge specifies it.

This is the exact distinction needed for the Zeno/circle line.  A base theory
may later define an appropriate process predicate from membership data; when
it does, the explicit bridge is a positive control.  Without that bridge, the
base theory alone cannot decide which external process-completion reading is
intended.
-/

namespace ZFCObservationLanguage

universe u

/-- A minimal semantic carrier for a membership-language theory.  The carrier
    type and membership relation may satisfy arbitrarily rich axioms, including
    a future formalization of ZFC.  Crucially, no process-completion predicate
    occurs in this interface. -/
structure MembershipModel (α : Type u) where
  member : α → α → Prop

/-- A base theory can inspect only membership-model data.  This represents the
    language boundary, not a claim that a particular set theory has no models. -/
abbrev MembershipTheory (α : Type u) : Type u :=
  MembershipModel α → Prop

/-- An external process-completion predicate is added only in an expansion.
    It is not silently present in the membership-only base interface. -/
structure CompletionExpansion (α : Type u) extends MembershipModel α where
  originDone : α → Prop

def expand
    (base : MembershipModel α)
    (done : α → Prop) : CompletionExpansion α where
  member := base.member
  originDone := done

/-- Satisfaction of a membership-only theory deliberately forgets the added
    completion predicate. -/
def Models
    (theory : MembershipTheory α)
    (expansion : CompletionExpansion α) : Prop :=
  theory expansion.toMembershipModel

/-- Changing an unspecified completion predicate leaves every
    membership-only theory judgment unchanged. -/
theorem expansion_preserves_base_theory
    (theory : MembershipTheory α)
    (base : MembershipModel α)
    (done : α → Prop) :
    Models theory (expand base done) ↔ theory base := by
  cases base
  rfl

/-- Hence two expansions with identical membership data satisfy exactly the
    same membership-only theory, even when their completion predicates differ. -/
theorem completion_change_is_invisible_to_base_theory
    (theory : MembershipTheory α)
    (base : MembershipModel α)
    (leftDone rightDone : α → Prop) :
    Models theory (expand base leftDone) ↔
      Models theory (expand base rightDone) := by
  cases base
  rfl

/-- If a membership-only theory has a model and the carrier has an element,
    it has two compatible expansions that disagree about that element's
    external process completion.  This is conditional on a base model; it does
    not assert a model or consistency theorem for ZFC. -/
theorem base_model_admits_opposite_originDone_expansions
    (theory : MembershipTheory α)
    (base : MembershipModel α)
    (baseModel : theory base)
    (state : α) :
    ∃ positive negative : CompletionExpansion α,
      Models theory positive ∧
      Models theory negative ∧
      (∀ x y, positive.member x y ↔ negative.member x y) ∧
      positive.originDone state ∧
      ¬ negative.originDone state := by
  refine ⟨expand base (fun _ => True), expand base (fun _ => False), ?_, ?_, ?_, ?_, ?_⟩
  · exact (expansion_preserves_base_theory theory base (fun _ => True)).mpr baseModel
  · exact (expansion_preserves_base_theory theory base (fun _ => False)).mpr baseModel
  · intro x y
    rfl
  · exact True.intro
  · intro h
    exact h

/-- A completion specification may use the full membership model, so it can
    stand for a set-theoretically definable process predicate once such a
    definition is actually supplied. -/
abbrev CompletionSpecification (α : Type u) : Type u :=
  MembershipModel α → α → Prop

/-- A bridge pays the missing obligation: it says exactly when the expanded
    predicate agrees with a fixed specification from the base model. -/
def CompletionBridge
    (specification : CompletionSpecification α)
    (expansion : CompletionExpansion α) : Prop :=
  ∀ state,
    expansion.originDone state ↔
      specification expansion.toMembershipModel state

/-- Once the same bridge specification is supplied, two expansions of the
    same membership model cannot disagree about completion.  This is the
    positive control corresponding to a paid Q-observation bridge. -/
theorem shared_completion_bridge_determines_originDone
    (base : MembershipModel α)
    (specification : CompletionSpecification α)
    (leftDone rightDone : α → Prop)
    (leftBridge : CompletionBridge specification (expand base leftDone))
    (rightBridge : CompletionBridge specification (expand base rightDone))
    (state : α) :
    leftDone state ↔ rightDone state := by
  cases base
  simpa [CompletionBridge, expand] using
    (Iff.trans (leftBridge state) (rightBridge state).symm)

/-- A supplied specification has a canonical expansion that pays its bridge.
    The result is a positive control: the theorem does not portray every
    membership-based formalization as incomplete. -/
theorem specified_completion_has_a_paid_bridge
    (base : MembershipModel α)
    (specification : CompletionSpecification α) :
    CompletionBridge specification
      (expand base (fun state => specification base state)) := by
  intro state
  rfl

/-- The two opposite expansions cannot both satisfy one fixed completion
    bridge.  This is the machine form of the distinction between an unlicensed
    completion reading and a source- or theory-supplied bridge. -/
theorem shared_bridge_rejects_opposite_completion_readings
    (base : MembershipModel α)
    (specification : CompletionSpecification α)
    (state : α)
    (positiveBridge : CompletionBridge specification (expand base (fun _ => True)))
    (negativeBridge : CompletionBridge specification (expand base (fun _ => False))) :
    False := by
  have specified : specification base state := by
    cases base
    exact (positiveBridge state).mp True.intro
  have impossible : False := by
    cases base
    exact (negativeBridge state).mpr specified
  exact impossible

#print axioms expansion_preserves_base_theory
#print axioms completion_change_is_invisible_to_base_theory
#print axioms base_model_admits_opposite_originDone_expansions
#print axioms shared_completion_bridge_determines_originDone
#print axioms specified_completion_has_a_paid_bridge
#print axioms shared_bridge_rejects_opposite_completion_readings

end ZFCObservationLanguage
