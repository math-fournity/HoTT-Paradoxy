/-!
`MP-ZFC-UNPAID-COMPLETION-PROMOTION-001` is the semantic countermodel half
of the user's Q/P proposal.

The base/subtheory interface deliberately contains all data that a standard
mathematical completion argument normally exposes here: membership data,
initial state, transition, observation, and `formalDone`.  It deliberately
does not contain `originDone`.  The kernel proves that, if a formal-completion
witness exists, this interface has an expansion satisfying exactly the same
base theory and formal data in which the original completion is false.  Hence
no promotion from formal completion to original completion is semantically
entailed until a bridge is supplied.

This does not encode the ZFC axiom scheme, construct a model of ZFC, decide a
physical completion question, or assert that a real source accepts the bad
promotion.  It formalizes the exact extra premise that must be added to turn a
ZFC-supported formal result into an original-process completion claim.
-/

namespace ZFCUnpaidCompletionPromotion

universe u

/-- Everything a base theory plus a subtheory exposes before it speaks about
    the original process-completion predicate.  `observe` is an explicit
    natural-number observation channel; it can represent stages, reported
    outcomes, or a finite observation code without claiming to model all time. -/
structure BaseSubtheoryModel (α : Type u) where
  member : α → α → Prop
  input : α
  step : α → α
  observe : α → Nat
  formalDone : α → Prop

/-- A ZFC-style base/subtheory theory may inspect every field above, but it is
    type-wise unable to inspect an external `originDone` predicate. -/
abbrev BaseSubtheory (α : Type u) : Type u :=
  BaseSubtheoryModel α → Prop

/-- A process expansion carries the missing original completion predicate in
    addition to the full base/subtheory observation package. -/
structure ProcessExpansion (α : Type u) extends BaseSubtheoryModel α where
  originDone : α → Prop

def expand
    (base : BaseSubtheoryModel α)
    (originDone : α → Prop) : ProcessExpansion α where
  member := base.member
  input := base.input
  step := base.step
  observe := base.observe
  formalDone := base.formalDone
  originDone := originDone

def Models
    (theory : BaseSubtheory α)
    (expansion : ProcessExpansion α) : Prop :=
  theory expansion.toBaseSubtheoryModel

/-- `P` in its strict formal form: a completion promotion asserts that each
    state the subtheory calls formally complete is originally complete too. -/
def CompletionPromotion (expansion : ProcessExpansion α) : Prop :=
  ∀ state, expansion.formalDone state → expansion.originDone state

/-- The user's `ZFC-1 = ZFC + P` is modeled here only as an extra use-level
    requirement on an expansion.  It is not an object-language extension of
    the ZFC axiom scheme. -/
def CompletionPromotionExtension
    (theory : BaseSubtheory α)
    (expansion : ProcessExpansion α) : Prop :=
  Models theory expansion ∧ CompletionPromotion expansion

/-- Adding or changing only the original completion predicate cannot change a
    membership/subtheory theory judgment. -/
theorem expansion_preserves_base_subtheory
    (theory : BaseSubtheory α)
    (base : BaseSubtheoryModel α)
    (originDone : α → Prop) :
    Models theory (expand base originDone) ↔ theory base := by
  cases base
  rfl

/-- The decisive countermodel.  Given a base/subtheory model with a witness
    of formal completion, retain every base field and set origin completion to
    false.  The resulting expansion refutes the unlicensed promotion P. -/
theorem unpaid_formal_completion_has_countermodel
    (theory : BaseSubtheory α)
    (base : BaseSubtheoryModel α)
    (baseModel : theory base)
    (state : α)
    (formalWitness : base.formalDone state) :
    ∃ expansion : ProcessExpansion α,
      Models theory expansion ∧
      expansion.formalDone state ∧
      ¬ expansion.originDone state ∧
      ¬ CompletionPromotion expansion := by
  refine ⟨expand base (fun _ => False), ?_, ?_, ?_, ?_⟩
  · exact (expansion_preserves_base_subtheory theory base (fun _ => False)).mpr baseModel
  · exact formalWitness
  · intro h
    exact h
  · intro promotion
    exact promotion state formalWitness

/-- Equivalently, a theory whose interface excludes origin completion cannot
    semantically entail the promotion merely because it has a formal-done
    witness.  This is the machine statement of the Q boundary. -/
theorem base_subtheory_does_not_semantically_entail_unpaid_promotion
    (theory : BaseSubtheory α)
    (base : BaseSubtheoryModel α)
    (baseModel : theory base)
    (state : α)
    (formalWitness : base.formalDone state) :
    ¬ (∀ expansion : ProcessExpansion α,
      Models theory expansion → CompletionPromotion expansion) := by
  intro entailsPromotion
  rcases unpaid_formal_completion_has_countermodel theory base baseModel state formalWitness with
    ⟨expansion, models, _, _, notPromotion⟩
  exact notPromotion (entailsPromotion expansion models)

/-- A specification may depend on the full base/subtheory model.  It is the
    place where a source can state the original process contract explicitly. -/
abbrev OriginCompletionSpecification (α : Type u) : Type u :=
  BaseSubtheoryModel α → α → Prop

/-- A bridge says that an expansion's original completion predicate matches
    the explicit specification. -/
def CompletionBridge
    (specification : OriginCompletionSpecification α)
    (expansion : ProcessExpansion α) : Prop :=
  ∀ state,
    expansion.originDone state ↔
      specification expansion.toBaseSubtheoryModel state

/-- The source/theory must additionally connect formal completion to the
    specified original contract.  Bridge equality alone is not enough. -/
def FormalCompletionAdequacy
    (specification : OriginCompletionSpecification α)
    (expansion : ProcessExpansion α) : Prop :=
  ∀ state,
    expansion.formalDone state →
      specification expansion.toBaseSubtheoryModel state

/-- This is the positive control: a paid bridge plus a formal adequacy proof
    yields the completion promotion P. -/
theorem paid_bridge_justifies_completion_promotion
    (specification : OriginCompletionSpecification α)
    (expansion : ProcessExpansion α)
    (bridge : CompletionBridge specification expansion)
    (adequacy : FormalCompletionAdequacy specification expansion) :
    CompletionPromotion expansion := by
  intro state formal
  exact (bridge state).mpr (adequacy state formal)

/-- A canonical expansion pays the bridge when the specification itself is
    chosen as origin completion.  It is a positive control against claiming
    that every formalization is necessarily missing Q. -/
theorem specified_origin_completion_has_paid_bridge
    (base : BaseSubtheoryModel α)
    (specification : OriginCompletionSpecification α) :
    CompletionBridge specification
      (expand base (fun state => specification base state)) := by
  intro state
  rfl

/-- If a base/subtheory model has a formal completion witness, its all-false
    origin expansion satisfies the base theory but not the use-level extension
    carrying P.  This displays `ZFC-1` as an additional assumption in the
    present semantic model rather than a consequence of the base theory. -/
theorem base_model_can_fail_completion_promotion_extension
    (theory : BaseSubtheory α)
    (base : BaseSubtheoryModel α)
    (baseModel : theory base)
    (state : α)
    (formalWitness : base.formalDone state) :
    ∃ expansion : ProcessExpansion α,
      Models theory expansion ∧
      ¬ CompletionPromotionExtension theory expansion := by
  refine ⟨expand base (fun _ => False), ?_, ?_⟩
  · exact (expansion_preserves_base_subtheory theory base (fun _ => False)).mpr baseModel
  · intro extension
    exact extension.2 state formalWitness

#print axioms expansion_preserves_base_subtheory
#print axioms unpaid_formal_completion_has_countermodel
#print axioms base_subtheory_does_not_semantically_entail_unpaid_promotion
#print axioms paid_bridge_justifies_completion_promotion
#print axioms specified_origin_completion_has_paid_bridge
#print axioms base_model_can_fail_completion_promotion_extension

end ZFCUnpaidCompletionPromotion
