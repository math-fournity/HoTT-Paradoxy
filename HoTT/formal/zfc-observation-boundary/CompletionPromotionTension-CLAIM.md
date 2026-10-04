# MP-ZFC-COMPLETION-PROMOTION-TENSION-001

## Exact formal scope

Source: [CompletionPromotionTension.lean](CompletionPromotionTension.lean).

This Lean 4 core package is the semantic refinement of the project’s Q/P/A/B
policy discussion. It uses the already controlled two-state Meta/Sub Theory
fixture. It does **not** encode ZFC syntax or semantics, real analysis, the
actual HoTT `QuestioningDelay` task, a physical motion, or the beliefs of a
mathematical community.

The package gives the phrase **“数学幻觉 P”** a precise formal role:

> P is an adopted *inference rule* that derives an origin-process completion
> judgment from a formal completion judgment. P is not itself the semantic
> bridge that would make that inference sound.

| User-side role | Lean object | What is and is not proved |
|---|---|---|
| Q | `MetaCanAuditOriginDone` | A relative observation capacity for one fixed task. No claim about actual ZFC’s full temporal resources. |
| P | `PAdopted policy` / `Derives.promote` | A policy permits a formal completion judgment to be promoted. It is not evidence that the promotion is semantically valid. |
| A | `FormalResolutionA` | The policy can derive formal completion at a named state. |
| B | `OriginCountertraceB` | At that same state, origin completion is semantically false. |
| paid bridge | `CompletionBridge` | The statewise fact `formalDone → originDone` required for a sound promotion. |

## Machine-checked statements

1. **Promotion carries a traceable P and A premise.**
   `origin_derivation_exposes_p_and_A` shows that every origin-completion
   derivation in this calculus contains an adopted P rule and the formal A
   premise. This is a derivation-provenance theorem, not historical causation.

2. **A sound P policy pays the bridge.**
   `sound_adopted_P_pays_completion_bridge` proves that if a policy which
   admits promotion is semantically sound, it entails the whole statewise
   bridge `formalDone → originDone`. A source that merely says “the formal
   result is complete” has not yet supplied this theorem’s premise.

3. **The controlled Q/P/A/B conjunction is unsound.**
   In `coarseSubtheory`, `unresolved` is formally complete but not origin
   complete. `coarse_fixture_lacks_Q_observation_capacity`,
   `promoted_policy_adopts_P`, `coarse_unresolved_has_formal_resolution_A`,
   `coarse_unresolved_has_origin_countertrace_B`, and
   `P_A_B_fixture_breaks_policy_soundness` prove the exact controlled chain.
   `controlled_Q_P_A_B_tension` bundles it.

4. **Q-missing does not by itself entail P.**
   `Q_missing_alone_does_not_entail_P_adoption` uses the same coarse
   observation and `guardedPolicy`, which refuses the promotion. Thus the
   research claim `Q-missing → permission/adoption of P` remains a separate
   source-mapping obligation; it cannot be manufactured from an observation
   collision.

5. **A positive control is included.**
   `promoted_policy_is_sound_when_bridge_is_paid` and
   `paid_fixture_has_completion_bridge` prove that the exact same rule is
   sound when formal and origin completion agree. This avoids treating every
   use of a formal completion as an error.

6. **The countertrace blocks the bridge.**
   `coarse_fixture_has_no_completion_bridge` proves that the coarse fixture’s
   formal completion cannot be promoted to origin completion for all states.

## Negative control

[WrongCompletionPromotionTension.lean](WrongCompletionPromotionTension.lean)
tries to prove that the promoted policy is sound on the coarse fixture. Lean
must reject the unresolved case. The capture script compiles the positive
dependency chain to temporary `.olean` files, so the negative result is a
rejection of the intended theorem rather than a missing-import error.

## Non-goals and source obligations

- No theorem says actual ZFC adopts P, lacks Q, or is inconsistent.
- No theorem says standard limit theory fails a physical Zeno or circle task.
- No theorem identifies the current HoTT process with a Zeno process.
- No theorem supplies the needed actual P-to-B source provenance.
- To instantiate this package outside its fixture, a source must fix the same
  process state, `formalDone`, `originDone`, observation, policy rule and
  evidence for whether its bridge is paid.
