# MP-ZFC-OBSERVATION-BOUNDARY-001

## Exact formal claims

Source: [ObservationBoundary.lean](ObservationBoundary.lean).

1. `no_done_classifier_of_observation_collision`:

   For arbitrary `observe : State → Observation` and `done : State → Prop`, if
   `observe` identifies a `done` state and a non-`done` state, no predicate on
   `Observation` alone decides `done` for every `State`.

2. `CompletionObservable`, `CompletionObservationIncomplete`, and
   `observation_collision_implies_completion_observation_incomplete`:

   `CompletionObservable observe done` means that a predicate on the observed
   output decides the chosen completion predicate on all source states.
   Under an observation collision between a done and non-done state, the named
   relative incompleteness predicate follows.  This gives a formal meaning to
   “observation is incomplete for this completion question” without assigning
   that status to ZFC or any other theory by name.

3. `CompletionBridge` and `completion_bridge_delivers_origin_done`:

   A bridge is an explicit statewise implication from a named formal completion
   predicate to a named origin/process completion predicate.  The theorem
   checks the positive control: only once that bridge is supplied can formal
   completion be transported to origin completion for the same state.  A shared
   natural-language label does not supply this premise.

4. `CompletionEquivalent` and `completion_equivalence_supplies_bridge`:

   The stronger same-task condition is a pointwise equivalence of two named
   completion predicates over one state domain.  Lean checks that such an
   equivalence supplies the forward bridge.  This is the exact formal shape of
   the evidence requested by the H093 cross-source adjudication; no actual
   source equivalence is asserted here.

5. `no_formal_completion_only_classifier`:

   In the explicit two-trace fixture, both `continuousEndpoint` and
   `sequentialNoLastAction` have `formalCompletion = 1`, while `strongDone`
   distinguishes them.  No predicate of `formalCompletion` alone decides
   `strongDone` for both traces.

6. `enriched_observation_decides_strong_done`:

   If the fixture observation retains a terminal-event `Bool`, a classifier can
   decide this fixture's `strongDone` predicate.

## Research interpretation

This is the machine-checkable logical kernel of the Q0 phrase “O2 does not
settle O3.” It proves an information/observation boundary under an explicit
collision hypothesis. It provides **no proof** that ZFC actually identifies
such process states, that a real limit has this exact semantics, that any
actual source makes an unpaid LiftClaim, or that ZFC is incomplete or
inconsistent. Those obligations remain in `ZFC-CIRCLE-Q0/Q1` source cards.

## Proof scope

- Assistant: Lean 4.34.1 core kernel.
- Dependencies: Lean prelude only; no imports, axioms, `sorry`, or classical
  choice are used by the three printed theorems. The run receipt preserves
  Lean's actual `#print axioms` output as the authoritative check.
- Claim identity: `CONTRIBUTOR_CANDIDATE_NOT_CURRENT` until a canonical
  integrator reviews the exact source, run receipt and claim-index placement.
