/-!
`MP-ZFC-OBSERVATION-BOUNDARY-001` is a minimal logical model of the
observation gap discussed by `ZFC-CIRCLE-Q0/Q1`.

It does NOT formalize ZFC, real analysis, the physical Zeno process, or a
claim that ZFC is inconsistent.  It proves only this exact fact:

If an observation map identifies two states whose strong completion predicates
have opposite truth values, then no predicate of that observation alone can
decide strong completion for every state.  A second theorem gives the positive
control: retaining a terminal-event bit makes the toy strong-completion
predicate decidable.
-/

namespace ZfcObservationBoundary

universe u v

/-- A process-level predicate cannot factor through an observation that
    identifies one completed and one non-completed state. -/
theorem no_done_classifier_of_observation_collision
    {State : Type u} {Observation : Type v}
    (observe : State → Observation) (done : State → Prop)
    (completed uncompleted : State)
    (sameObservation : observe completed = observe uncompleted)
    (completedDone : done completed)
    (uncompletedNotDone : ¬ done uncompleted) :
    ¬ ∃ classify : Observation → Prop,
      ∀ state, classify (observe state) ↔ done state := by
  intro h
  rcases h with ⟨classify, hclassify⟩
  have atCompleted : classify (observe completed) :=
    (hclassify completed).mpr completedDone
  have atUncompleted : classify (observe uncompleted) := by
    simpa [sameObservation] using atCompleted
  exact uncompletedNotDone ((hclassify uncompleted).mp atUncompleted)

/-- An observation is completion-adequate precisely when a predicate on the
    observed data can decide the specified completion predicate for every
    state.  This definition is relative to both `observe` and `done`; it makes
    no claim about a theory until those two interfaces have been supplied. -/
def CompletionObservable
    {State : Type u} {Observation : Type v}
    (observe : State → Observation) (done : State → Prop) : Prop :=
  ∃ classify : Observation → Prop,
    ∀ state, classify (observe state) ↔ done state

/-- A name for the precise, relative notion of observation incompleteness used
    by the research bridge. -/
def CompletionObservationIncomplete
    {State : Type u} {Observation : Type v}
    (observe : State → Observation) (done : State → Prop) : Prop :=
  ¬ CompletionObservable observe done

/-- A collision between oppositely classified process states proves the
    corresponding observation is not completion-adequate. -/
theorem observation_collision_implies_completion_observation_incomplete
    {State : Type u} {Observation : Type v}
    (observe : State → Observation) (done : State → Prop)
    (completed uncompleted : State)
    (sameObservation : observe completed = observe uncompleted)
    (completedDone : done completed)
    (uncompletedNotDone : ¬ done uncompleted) :
    CompletionObservationIncomplete observe done := by
  exact no_done_classifier_of_observation_collision observe done completed
    uncompleted sameObservation completedDone uncompletedNotDone

/-- Two deliberately distinct process contracts.  `continuousEndpoint` has a
    registered terminal event; `sequentialNoLastAction` has no final action.
    The type is a semantic fixture, not a model of all continuous or discrete
    motion. -/
inductive CompletionTrace where
  | continuousEndpoint
  | sequentialNoLastAction
deriving DecidableEq

/-- The intentionally coarse formal observation: both traces are assigned the
    same completed mathematical value. -/
def formalCompletion : CompletionTrace → Nat
  | .continuousEndpoint => 1
  | .sequentialNoLastAction => 1

/-- Strong Done keeps the terminal-event requirement that the coarse result
    forgets. -/
def strongDone : CompletionTrace → Prop
  | .continuousEndpoint => True
  | .sequentialNoLastAction => False

theorem continuous_endpoint_is_strong_done :
    strongDone .continuousEndpoint := by
  trivial

theorem no_last_action_is_not_strong_done :
    ¬ strongDone .sequentialNoLastAction := by
  intro h
  exact h

/-- Concrete O2-to-O3 boundary: a shared formal completion value cannot decide
    the stronger process predicate. -/
theorem no_formal_completion_only_classifier :
    ¬ ∃ classify : Nat → Prop,
      ∀ trace, classify (formalCompletion trace) ↔ strongDone trace := by
  apply no_done_classifier_of_observation_collision
    formalCompletion strongDone .continuousEndpoint .sequentialNoLastAction
  · rfl
  · exact continuous_endpoint_is_strong_done
  · exact no_last_action_is_not_strong_done

/-- An enriched observation retains the terminal-event bit that the coarse
    formal completion erases. -/
def enrichedObservation : CompletionTrace → Nat × Bool
  | .continuousEndpoint => (1, true)
  | .sequentialNoLastAction => (1, false)

def enrichedClassifier : Nat × Bool → Prop
  | (_, true) => True
  | (_, false) => False

/-- Positive control: once the terminal-event observation is retained, this
    particular strong Done predicate factors through the enriched observation. -/
theorem enriched_observation_decides_strong_done :
    ∀ trace, enrichedClassifier (enrichedObservation trace) ↔ strongDone trace := by
  intro trace
  cases trace with
  | continuousEndpoint =>
      constructor <;> intro _ <;> trivial
  | sequentialNoLastAction =>
      constructor <;> intro h <;> exact h

#print axioms no_done_classifier_of_observation_collision
#print axioms observation_collision_implies_completion_observation_incomplete
#print axioms no_formal_completion_only_classifier
#print axioms enriched_observation_decides_strong_done

end ZfcObservationBoundary
