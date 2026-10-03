# MP-ZFC-OBSERVATION-BOUNDARY-001

## Exact formal claims

Source: [ObservationBoundary.lean](ObservationBoundary.lean).

1. `no_done_classifier_of_observation_collision`:

   For arbitrary `observe : State → Observation` and `done : State → Prop`, if
   `observe` identifies a `done` state and a non-`done` state, no predicate on
   `Observation` alone decides `done` for every `State`.

2. `no_formal_completion_only_classifier`:

   In the explicit two-trace fixture, both `continuousEndpoint` and
   `sequentialNoLastAction` have `formalCompletion = 1`, while `strongDone`
   distinguishes them.  No predicate of `formalCompletion` alone decides
   `strongDone` for both traces.

3. `enriched_observation_decides_strong_done`:

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
