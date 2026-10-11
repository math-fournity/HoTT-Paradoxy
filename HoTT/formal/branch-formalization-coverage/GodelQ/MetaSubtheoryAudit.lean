/-!
`MP-ZFC-META-SUBTHEORY-AUDIT-001` gives a small formal contract for the
research initiator's Meta Theory / Sub Theory proposal.

It does not claim that bare ZFC literally contains this interface.  It proves
what must be supplied for a meta-level acceptance of a subtheory's formal
completion to count as an origin-process completion: an acceptance path and a
bridge.  A coarse meta observation with an origin-done collision cannot audit
the origin predicate; an enriched, bridge-aware positive control can.
-/

namespace ZfcMetaSubtheoryAudit

universe u v

/-- The process contract whose boundary a subtheory may or may not preserve. -/
structure ProcessTask (State : Type u) where
  input : State
  step : State → State
  formalDone : State → Prop
  originDone : State → Prop

/-- A subtheory reports a formal completion predicate for one process contract. -/
structure Subtheory (State : Type u) where
  task : ProcessTask State

/-- A meta theory sees a chosen observation and decides which observed outputs
    it accepts.  The structure says nothing yet about whether acceptance pays
    the originating process contract. -/
structure MetaTheory (State : Type u) (Observation : Type v) where
  observe : State → Observation
  accepts : Observation → Prop

/-- The meta theory accepts every state that the subtheory calls formally
    complete.  This models the delivery of a subtheory result into a meta-level
    verdict, while keeping the origin completion predicate separate. -/
def MetaAcceptsFormalCompletion
    {State : Type u} {Observation : Type v}
    (framework : MetaTheory State Observation) (sub : Subtheory State) : Prop :=
  ∀ state, sub.task.formalDone state → framework.accepts (framework.observe state)

/-- The meta theory has enough observational precision for this origin Done
    exactly when a predicate of what it observes classifies origin completion. -/
def MetaCanAuditOriginDone
    {State : Type u} {Observation : Type v}
    (framework : MetaTheory State Observation) (sub : Subtheory State) : Prop :=
  ∃ classify : Observation → Prop,
    ∀ state, classify (framework.observe state) ↔ sub.task.originDone state

/-- A strong meta-level promotion says that any state the meta theory accepts
    as a result is originally complete.  This is the policy that needs a
    bridge; it is not granted by being a meta language. -/
def MetaPromotesAcceptedAsOrigin
    {State : Type u} {Observation : Type v}
    (framework : MetaTheory State Observation) (sub : Subtheory State) : Prop :=
  ∀ state, framework.accepts (framework.observe state) → sub.task.originDone state

/-- If a meta theory accepts the subtheory's formal completions and promotes
    accepted results to origin completion, it has supplied the statewise bridge
    from formal Done to origin Done. -/
theorem meta_promotion_pays_subtheory_bridge
    {State : Type u} {Observation : Type v}
    (framework : MetaTheory State Observation) (sub : Subtheory State)
    (acceptsFormal : MetaAcceptsFormalCompletion framework sub)
    (promotes : MetaPromotesAcceptedAsOrigin framework sub) :
    ∀ state, sub.task.formalDone state → sub.task.originDone state := by
  intro state formal
  exact promotes state (acceptsFormal state formal)

/-- One formally complete but originally incomplete state refutes any claimed
    meta promotion, provided the meta theory accepts formal completion. -/
theorem unpaid_subtheory_completion_blocks_meta_promotion
    {State : Type u} {Observation : Type v}
    (framework : MetaTheory State Observation) (sub : Subtheory State)
    (acceptsFormal : MetaAcceptsFormalCompletion framework sub)
    (state : State)
    (formal : sub.task.formalDone state)
    (notOrigin : ¬ sub.task.originDone state) :
    ¬ MetaPromotesAcceptedAsOrigin framework sub := by
  intro promotes
  exact notOrigin (promotes state (acceptsFormal state formal))

/-- A collision at the meta observation boundary between one origin-complete
    and one origin-incomplete state proves that this meta interface cannot
    audit origin Done. -/
theorem meta_observation_collision_blocks_origin_audit
    {State : Type u} {Observation : Type v}
    (framework : MetaTheory State Observation) (sub : Subtheory State)
    (completed uncompleted : State)
    (sameObservation : framework.observe completed = framework.observe uncompleted)
    (completedOrigin : sub.task.originDone completed)
    (uncompletedNotOrigin : ¬ sub.task.originDone uncompleted) :
    ¬ MetaCanAuditOriginDone framework sub := by
  intro audit
  rcases audit with ⟨classify, classifies⟩
  have atCompleted : classify (framework.observe completed) :=
    (classifies completed).mpr completedOrigin
  have atUncompleted : classify (framework.observe uncompleted) := by
    simpa [sameObservation] using atCompleted
  exact uncompletedNotOrigin ((classifies uncompleted).mp atUncompleted)

/-- A two-state controlled process.  The subtheory's coarse formal result is
    intentionally true of both states, but only one state is origin complete. -/
inductive TwoState where
  | origin
  | unresolved
deriving DecidableEq

def coarseSubtheory : Subtheory TwoState where
  task := {
    input := .unresolved
    step := id
    formalDone := fun _ => True
    originDone := fun
      | .origin => True
      | .unresolved => False }

/-- The coarse meta interface erases the distinction altogether. -/
def coarseMeta : MetaTheory TwoState Unit where
  observe := fun _ => ()
  accepts := fun _ => True

theorem coarse_meta_accepts_all_formal_results :
    MetaAcceptsFormalCompletion coarseMeta coarseSubtheory := by
  intro _ _
  trivial

theorem coarse_meta_lacks_origin_audit :
    ¬ MetaCanAuditOriginDone coarseMeta coarseSubtheory := by
  apply meta_observation_collision_blocks_origin_audit coarseMeta coarseSubtheory
    .origin .unresolved
  · rfl
  · trivial
  · intro h
    exact h

theorem coarse_meta_cannot_promote_formal_to_origin :
    ¬ MetaPromotesAcceptedAsOrigin coarseMeta coarseSubtheory := by
  apply unpaid_subtheory_completion_blocks_meta_promotion coarseMeta coarseSubtheory
    coarse_meta_accepts_all_formal_results .unresolved
  · trivial
  · intro h
    exact h

/-- Positive control: a subtheory whose formal completion is exactly the
    origin-complete state, together with a meta observation that preserves that
    distinction. -/
def paidSubtheory : Subtheory TwoState where
  task := {
    input := .unresolved
    step := id
    formalDone := fun
      | .origin => True
      | .unresolved => False
    originDone := fun
      | .origin => True
      | .unresolved => False }

def bridgeAwareMeta : MetaTheory TwoState TwoState where
  observe := id
  accepts := fun state => state = .origin

theorem bridge_aware_meta_accepts_paid_formal_completion :
    MetaAcceptsFormalCompletion bridgeAwareMeta paidSubtheory := by
  intro state formal
  cases state with
  | origin => rfl
  | unresolved => exact False.elim formal

theorem bridge_aware_meta_promotes_paid_completion :
    MetaPromotesAcceptedAsOrigin bridgeAwareMeta paidSubtheory := by
  intro state accepted
  cases state with
  | origin => trivial
  | unresolved => cases accepted

theorem bridge_aware_meta_has_origin_audit :
    MetaCanAuditOriginDone bridgeAwareMeta paidSubtheory := by
  refine ⟨fun state => state = .origin, ?_⟩
  intro state
  cases state with
  | origin => constructor <;> intro _ <;> trivial
  | unresolved =>
      constructor
      · intro h
        cases h
      · intro h
        cases h

theorem bridge_aware_meta_pays_subtheory_bridge :
    ∀ state, paidSubtheory.task.formalDone state → paidSubtheory.task.originDone state :=
  meta_promotion_pays_subtheory_bridge bridgeAwareMeta paidSubtheory
    bridge_aware_meta_accepts_paid_formal_completion
    bridge_aware_meta_promotes_paid_completion

#print axioms meta_promotion_pays_subtheory_bridge
#print axioms unpaid_subtheory_completion_blocks_meta_promotion
#print axioms meta_observation_collision_blocks_origin_audit
#print axioms coarse_meta_accepts_all_formal_results
#print axioms coarse_meta_lacks_origin_audit
#print axioms coarse_meta_cannot_promote_formal_to_origin
#print axioms bridge_aware_meta_accepts_paid_formal_completion
#print axioms bridge_aware_meta_promotes_paid_completion
#print axioms bridge_aware_meta_has_origin_audit
#print axioms bridge_aware_meta_pays_subtheory_bridge

end ZfcMetaSubtheoryAudit
