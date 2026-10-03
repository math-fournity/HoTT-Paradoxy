# MP-ZFC-GEOMETRIC-COMPLETION-001

## Exact formal claims

Source: [GeometricCompletion.lean](GeometricCompletion.lean).

1. `zenoPartialSum_strictly_below_one`:

   For every natural-number stage `n`, the explicitly defined geometric partial
   sum `1 - (1 / 2)^n` is strictly below `1`.

2. `zenoPartialSum_never_reaches_one`:

   No individual natural-number stage of that sequence equals `1`.

3. `zenoPartialSum_tendsto_one` and `zeno_has_limit_outcome`:

   The same sequence tends to `1` in the usual topology on the real numbers.

4. `zeno_has_no_finite_stage_endpoint`:

   The formal predicate `hasFiniteStageEndpoint := ∃ n, zenoPartialSum n = 1`
   is false.

5. `zeno_limit_outcome_without_finite_stage_endpoint`:

   The formal predicates `hasLimitOutcome` and `¬ hasFiniteStageEndpoint` hold
   together.  The source deliberately keeps these predicates separately named.

6. `zeno_limit_outcome_does_not_imply_finite_stage_endpoint`:

   For this concrete sequence, the proposition `hasLimitOutcome →
   hasFiniteStageEndpoint` is false.  This is the direct formal non-implication
   between the named analysis result and finite-stage endpoint arrival.

7. `zeno_limit_outcome_done_not_equiv_final_stage_done`:

   With the source-aligned aliases `limitOutcomeDone` and `finalStageDone`, the
   two predicates are not equivalent for this geometric sequence.  This is a
   precise task-switch control: if a source replaces the second predicate by
   the first, equivalence requires a separate bridge rather than a change of
   label alone.

8. `closed_continuous_time_has_endpoint_arrival` and
   `closed_continuous_time_has_terminal_witness`:

   In a deliberately separate positive-control model whose time domain is the
   closed interval `[0, 1]`, a trajectory has an actual terminal parameter at
   which it is at its goal.  This proves that the finite-stage result above
   does not rule out a continuous-time endpoint model; a separate bridge is
   still required to call such model arrival an original process completion.

## Research interpretation

This is a direct real-analysis control for the inquiry.  It checks the exact
coexistence of two statements that ordinary prose often compresses: a sequence
has a real topological limit at its endpoint, while no finite indexed stage is
that endpoint.  It is therefore evidence that a limit theorem alone does not
mathematically entail a finite-stage-arrival theorem.

It does **not** decide whether a specified physical or philosophical process is
completed at a time endpoint, whether the standard resolution of Zeno uses a
stronger notion of completion, whether ZFC lacks a required metatheoretic
judgment, or whether ZFC is inconsistent.  Those are separate source and
same-task obligations.

## Proof scope

- Assistant: Lean 4.34.1 using the pinned local Mathlib build recorded in the
  run receipt.
- Lean reports the expected Mathlib/classical dependencies
  `propext`, `Classical.choice`, and `Quot.sound`; this is not a no-axiom core
  proof.
- Claim identity: `CONTRIBUTOR_CANDIDATE_NOT_CURRENT` until canonical review
  places the source and receipt in the claim-evidence matrix.
