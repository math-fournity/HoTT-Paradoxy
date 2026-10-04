# MP-ZFC-META-SUBTHEORY-AUDIT-001

## Exact formal scope

Source: [MetaSubtheoryAudit.lean](MetaSubtheoryAudit.lean).

This package is a Lean 4 core model of the research initiator's claim that a
foundation used as a meta framework should be able to audit when a subtheory's
formal completion is being promoted to origin-process completion. It does not
formalize bare ZFC, any actual limit theory, physical motion, a mathematical
community, or an actual HoTT interpretation.

| User-side role | Lean object | Exact machine-checked content |
|---|---|---|
| Sub Theory | `Subtheory` / `ProcessTask` | A task has an input, transition, `formalDone`, and `originDone`. |
| Meta Theory | `MetaTheory` | The meta interface observes states and accepts selected observations. |
| Meta accepts sub result | `MetaAcceptsFormalCompletion` | Every formal completion receives a meta-level acceptance. |
| Q: completion observation capacity | `MetaCanAuditOriginDone` | An observation predicate classifies origin Done for every task state. |
| Strong promotion P | `MetaPromotesAcceptedAsOrigin` | Every meta-accepted observation is claimed to be origin complete. |

## Machine-checked theorems

1. `meta_promotion_pays_subtheory_bridge`

   If a meta theory accepts every formal subtheory completion and promotes every
   accepted result to origin completion, then it has supplied the statewise
   bridge `formalDone → originDone`.

2. `unpaid_subtheory_completion_blocks_meta_promotion`

   If one formally completed state is not origin complete, a meta theory that
   accepts formal completion cannot soundly promote every accepted observation
   to origin completion.

3. `meta_observation_collision_blocks_origin_audit`

   If the meta observation identifies an origin-complete state with an
   origin-incomplete state, no predicate of that observation alone audits
   origin Done for the entire task.

4. `coarse_meta_lacks_origin_audit` and
   `coarse_meta_cannot_promote_formal_to_origin`

   A two-state controlled subtheory makes both states formally complete; a
   coarse meta observation erases their difference. Lean proves both the
   relative observation gap and the failure of the resulting strong promotion.

5. `bridge_aware_meta_has_origin_audit` and
   `bridge_aware_meta_pays_subtheory_bridge`

   The paired positive control keeps the distinguishing state observation and
   lets the subtheory's formal completion agree with origin completion. It
   proves that the package is not claiming every meta theory is incomplete.

## Negative control

[WrongMetaSubtheoryAudit.lean](WrongMetaSubtheoryAudit.lean) tries to prove
that `coarseMeta` promotes all formally accepted states to origin completion.
Lean must reject it at the unresolved state. The capture script compiles the
positive source to an external temporary `.olean`, then uses `LEAN_PATH` for
the negative source; the rejected run therefore tests the intended theorem,
not a missing import path.

Initial negative run `...NEG-001-01` reached the expected Lean rejection, but
its capture helper inspected only stderr while this Lean invocation emitted the
diagnostic on stdout. It is retained as `RUNNER_OR_EVIDENCE_FAILURE`; the
helper now inspects both streams, and `...NEG-001-02` is the current negative
receipt.

## Non-goals

- No theorem that actual ZFC is formally inconsistent or literally lacks all
  temporal / computational representation.
- No theorem that ZFC must audit every informal physical process merely because
  a user calls it a meta theory.
- No theorem that standard real analysis incorrectly resolves Zeno.
- No theorem that a real HoTT result is the same `ProcessTask` as a Zeno task.
- No claim that an actual source has adopted `MetaPromotesAcceptedAsOrigin`
  without a task-specific bridge.
