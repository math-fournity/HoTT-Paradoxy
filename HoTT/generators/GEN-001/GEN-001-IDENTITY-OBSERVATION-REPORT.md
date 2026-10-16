# Machine-overview calibration report: MS-TASK-GEN001-IDENTITY-OBSERVATION-001

- generated_at_utc: 2026-09-16T21:55:00+00:00 (AI-authored from validated receipts)
- case: `/Volumes/D/HoTT-machine-overview/machine-overview/cases/MS-TASK-GEN001-IDENTITY-OBSERVATION-001/case-revision-1.json` (revision 1, case identity sha256 `f7fd34d3bd050797090296896a768358505ef034feee2fd314313ef4b62e46aa`)
- search run: `/Volumes/D/HoTT-machine-overview/machine-overview/runs/20260916-SEARCH-GEN001-IDENTITY-OBSERVATION-001/RUN.json` (run `20260916-SEARCH-GEN001-IDENTITY-OBSERVATION-001`, COMPLETED_WITHIN_BUDGET)
- coordinator: `0.5.0` / registry `HOTT-MACHINE-OVERVIEW-M1`
- profile: `L1-IDENTITY-OBSERVATION-v1` (PROFILE_QUALIFIED)
- premise: `PREMISE-B-01` (definitional equality decidable, semantic identity pushed outside the boundary), AI-adjudicated pending external audit; supply `SUPPLY-003` (AI-frozen, not user supply)

## What was searched

- declared grammar: `machine-overview/grammars/l1-identity-observation-v1.json` (family `TASK-FAMILY-IDENTITY-OBSERVATION-LAYER`)
- delay atoms: 7; contexts planned: 440; contexts examined: 440
- pair-context checks: 5280 executed of 5280 planned; separations seen: 956
- reduced distinct witnesses: 70; complete-within-declared-grammar: `True`; truncated: `False`
- search answer-independence: order permutation set-equal = `True`, statistics match = `True`; grammar mutation (deadline kind removed) changes statistics = `True` (sensitivity confirmed)
- known calibration benchmark present in the discovered set: `NOT_DECLARED` (None)

## B-01 modelling statement (what this family accepts, not a mathematical claim)

The pinned delay fragment's own identity criterion is delay equivalence `_≈_`: two `ret`-valued
delays are identified whenever they carry the same Bool value, and the arrival round is forgotten.
This is the bounded correspondent of the B-01 premise's theory step: the theory treats two
result-equivalent processes as the same already-completed value sequence, and any judgement whose
correctness depends on "are these two the same" is decided by information the identity criterion
erased. In this family:

- the **pair** of every separating witness is delay-equivalent (the theory's own verdict: "same");
- the **context** is a declared observation layer — a race against a reference delay, or a bounded
  deadline — that reads the erased round;
- a **verdict consumer** (new declared bind continuation) then renders the layer's same/different
  conclusion;
- under the definitional layer (a bare deadline at or above both arrival rounds) the same pair is
  NOT separated — the identity verdict depends on the observation layer, which is exactly the
  condition B-01 claims the theory omitted.

This is a bounded acceptance unit over the pinned fragment. It is **not** a claim that Delay Bool is
HoTT's identity type, and it is **not** a claim that B-01 is non-real (that verdict is
pending external audit).

## New declared constructs (out-of-envelope essence)

| continuation | map | role |
|---|---|---|
| `identity_verdict_definitional` | true↦ret 0 true; false↦ret 1 false | definitional-layer verdict: congruent, value-only |
| `identity_verdict_purpose` | true↦ret 1 true; false↦ret 2 false | purpose-layer verdict: adds its own processing rounds |
| `identity_verdict_never_on_true` | true↦ω; false↦ret 0 true | availability-layer verdict: never renders on one branch |

All three maps are mechanically unique against the continuation maps of all pre-existing grammars
(checked programmatically before the family was frozen). Bounds are deliberately aligned with the
existing L1 index horizons (delay_index_max 2, partner 2, horizons {0,1,2}) so that an
out-of-envelope witness fails the pre-existing grammars on exactly one dimension.

## Out-of-envelope mechanical proof

- reduced witnesses: 70; out-of-envelope (outside all 17 pre-existing grammars): **44**
- rejection reason tally across the 5 delay-fragment pre-existing grammars (l1-v0/v1/v2,
  l1-witness-recovery-v1, l1-completion-process-v1): **220 / 220 = BIND_CONTINUATION**, i.e.
  the rejection reason is unique for every out-of-envelope witness; the remaining 12 symbolic-horn
  grammars return `BACKEND_MISMATCH` by construction
- continuation usage among the 44 out-of-envelope witnesses:
  `identity_verdict_definitional` 18 / `identity_verdict_never_on_true` 14 /
  `identity_verdict_purpose` 12
- separation kinds among the 44: value_mismatch 28 / deadline_observation 8 / completion_divergence 8
- full per-witness membership table: `GEN-001-IDENTITY-OBSERVATION-OUT-OF-ENVELOPE.json`

## Controls

- positive control (`bind_preserves_result_equivalence`, claim ref C-71): preserved = `True`
- negative control (`declared_deadline_does_not_separate_this_pair`, pair (ret 0 false, ret 1 false),
  bare deadline k=1): separated = `False`, expectation met = `True` — the definitional layer judges
  the identified pair "same"

## Native kernel verification (accepted runs)

Four witnesses were selected to cover 3 new constructors × 3 separation mechanisms. Each run
executed the four-way kernel check on Cubical Agda 2.8.0 + cubical v0.9: `verify` and `controls`
must be accepted, the `negative-control` must be rejected (exit 42, EXPECTED_TYPE_REJECTION), and
`verify-replay` must match exactly. All four were additionally independently reproduced from a
main-repo copy of the generated sources (exit 0).

### `20260916-VERIFY-GEN001-IDENTITY-OBSERVATION-0014` (witness WV-0014)

- constructor × mechanism: `identity_verdict_never_on_true` × completion_divergence
- statement: pair (ret 0 false, ret 1 false) — delay-equivalent — under
  race(□, ret 0 true) → bind(□, λ{true↦ω; false↦ret 0 true})
- observations: ret 1 true ≠ ω
- status: `NATIVE_CHECKED_EXPLORATION_CANDIDATE`; replay: `EXACT_EXIT_STDOUT_STDERR_MATCH`
- kernel verify exit 0 ACCEPTED; controls exit 0 ACCEPTED; negative-control exit 42
  REJECTED_AS_EXPECTED; verify-replay exit 0 ACCEPTED; main-repo independent replay exit 0
- registers new claim: **false**

### `20260916-VERIFY-GEN001-IDENTITY-OBSERVATION-0023` (witness WV-0023)

- constructor × mechanism: `identity_verdict_definitional` × value_mismatch
- statement: pair (ret 0 false, ret 1 false) — delay-equivalent — under
  race(□, ret 0 true) → bind(□, λ{true↦ret 0 true; false↦ret 1 false})
- observations: ret 2 false ≠ ret 1 true
- status: `NATIVE_CHECKED_EXPLORATION_CANDIDATE`; replay: `EXACT_EXIT_STDOUT_STDERR_MATCH`
- kernel verify exit 0 ACCEPTED; controls exit 0 ACCEPTED; negative-control exit 42
  REJECTED_AS_EXPECTED; verify-replay exit 0 ACCEPTED; main-repo independent replay exit 0
- registers new claim: **false**

### `20260916-VERIFY-GEN001-IDENTITY-OBSERVATION-0044` (witness WV-0044)

- constructor × mechanism: `identity_verdict_definitional` × deadline_observation
- statement: pair (ret 0 true, ret 1 true) — delay-equivalent — under
  bind(□, λ{true↦ret 0 true; false↦ret 1 false}) → deadline k=1
- observations: some true ≠ none
- status: `NATIVE_CHECKED_EXPLORATION_CANDIDATE`; replay: `EXACT_EXIT_STDOUT_STDERR_MATCH`
- kernel verify exit 0 ACCEPTED; controls exit 0 ACCEPTED; negative-control exit 42
  REJECTED_AS_EXPECTED; verify-replay exit 0 ACCEPTED; main-repo independent replay exit 0
- registers new claim: **false**

### `20260916-VERIFY-GEN001-IDENTITY-OBSERVATION-0067` (witness WV-0067)

- constructor × mechanism: `identity_verdict_purpose` × deadline_observation
- statement: pair (ret 0 true, ret 1 true) — delay-equivalent — under
  bind(□, λ{true↦ret 1 true; false↦ret 2 false}) → deadline k=2
- observations: some true ≠ none
- status: `NATIVE_CHECKED_EXPLORATION_CANDIDATE`; replay: `EXACT_EXIT_STDOUT_STDERR_MATCH`
- kernel verify exit 0 ACCEPTED; controls exit 0 ACCEPTED; negative-control exit 42
  REJECTED_AS_EXPECTED; verify-replay exit 0 ACCEPTED; main-repo independent replay exit 0
- registers new claim: **false**

## Verdict

`GENERATOR_LINK_DEMONSTRATED_WITH_SCOPE` — a third AI-frozen task family over the pinned delay
model runs the complete chain (supply registration → grammar/task/profile freeze → profile
qualification → case freeze → complete enumeration with remainder 0 → grammar-preserving
reduction → unique-reason out-of-envelope proof → native-kernel four-way verification with
independent replay), with the role discipline intact: the family is AI supply, the engine only
enumerates and reduces, and only the native kernel issues verdicts.

## Phenomenon novelty disclosure (per revision shard 012)

1. **Is this family's phenomenon (identity verdict depends on observation layer) already
   partially expressible in the pre-existing grammars?** Yes, partially, and this is
   mechanically recomputable from the search receipts: a bare deadline separates the
   delay-equivalent pair (ret 1 true, ret 2 true) at horizon k=1 but not at k=2. The choice of
   horizon is itself the choice of an observation layer, and the identity verdict flips with it.
   This half of the phenomenon needs no new construct at all.
2. **What do the new continuations carry?** They objectify the layer's conclusion into an
   explicit same/different value that a downstream consumer can consume: the verdict renderer.
   The race/deadline operations that expose the erased round are pre-existing. So the family's
   substantive novelty is the explicit verdict object, not the layer-exposure mechanism.
   Novelty rating: `PARTIAL` (grammar novelty is full and unique-reason; phenomenon novelty is
   partial because layer-exposure pre-exists). This is submitted to external audit, not
   self-adjudicated.
3. **Cross-family mechanism overlap:** the race-truncation mechanism (race converts an
   arrival-round difference into a value difference; bind/deadline converts it into a
   completion or verdict difference) is shared with GEN-001-1 (E-02) and GEN-001-2 (A-03).
   Registered as out-of-envelope ingress; cross-family independence is not proved.

## Prohibited extrapolation

- This unit registers **no** mathematical claim and does **not** enter `HoTT/CLAIM_EVIDENCE_MATRIX.md`
  (revision 003 §4 / 010 §2 / F-011). The B-01 non-reality verdict remains
  `AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT`.
- The family shares the race-truncation separation mechanism with the E-02 first chain and the
  A-03 completion-process family (the race converts an arrival-round difference into a value
  difference, and a bind/deadline converts that into a completion or verdict difference).
  Cross-family independence is **not proved** and is registered as out-of-envelope ingress, not as
  a conclusion.
- The Delay Bool fragment is a bounded correspondent of B-01, not HoTT's identity type or
  univalence. A propositional-equality / univalence family remains a V2 candidate.
- This unit does not claim the open candidate space is exhausted, nor that the engine discovers
  task families autonomously.
