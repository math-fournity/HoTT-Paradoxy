# M4-lite L3 three-task evaluation

- Status: `DESCRIPTIVE_M4_LITE_COMPLETE / SNAPSHOT_REPLAY_V2_VALID / NOT_A_GENERAL_EFFECTIVENESS_RESULT`
- Evaluation: `M4-LITE-L3-001`
- Run: `20260913-M4-LITE-L3-001`
- Frozen search source: `machine-overview/machine_overview/search.py` from
  `025938a07ef6ca9b74ca4874366ec1f97f06592e`, SHA-256
  `b1aec11190571a6c58adf1404ec882ab23024178328209436b4f565c29d47e20`
- Deterministic result SHA-256:
  `199793e000ba3de879d0f85c225b20b876775ccfa34f5abac9829004c8a90028`

## What was fixed before task materialization

`PROTOCOL.json` fixed three roles, their native ACCEPT/ACCEPT/REJECT outcomes,
the three comparison modes, one shared budget, metrics, the two-coordinate
treatment of time, and the same-designer limitation.  `DESIGN-FREEZE.json`
then checked that all TaskSpec, grammar and SPEC paths were absent, that the
live symbolic search source was byte-identical to the 0.2.0 implementation
commit, and that 46 tests passed.

The native renderers and shared `L3M4Support.agda` were qualified before this
freeze.  A pre-freeze probe found and repaired one missing product import in
the event renderer.  No frozen adapter or search source changed after the
freeze.

## Canonical task runs

| task role | full grammar | first witness | native result |
|---|---:|---|---|
| Path coherence positive | 76 checks / 7 terms | `λ i → f i` | verify 0 / controls 0 / negative 42 / replay 0, exact |
| explicit event boundary positive | 59 checks / 1 term | `(phase-start , (phase-finish , phase-apart))` | verify 0 / controls 0 / negative 42 / replay 0, exact |
| finite-to-exact negative | 59 checks / 4 terms | `finiteToExactCandidate finite` | verify 42 / controls 0 / negative 42 / failed-proof replay 42, exact |

Every full-grammar result was complete through depth 4, order-permutation
set-equal, and lost every goal term when its declared mechanism rule was
removed.  The evaluator independently recomputed the full-grammar first AST
and matched it to each canonical coordinator search receipt.

The negative task deliberately distinguishes two type systems.  Its proof AST
is well typed in the grammar's declared proposition graph.  Native Cubical
Agda then rejects `finiteToExactCandidate` because the pinned profile supplies
no such operation.  The coordinator records `NATIVE_CHECK_FAILED`; neither the
report nor the evaluator promotes it to a proof.

## Same-budget mode comparison

The accounting unit is canonical rule-application checks.  Each mode received
`max_checks=5000`, `max_witnesses=500`, and proof depth 4.  If hybrid feedback
reran after a native rejection, its first-stage checks were deducted from the
remaining check budget.

| mode | tasks with expected final decision | total checks | false promotions | feedback applications |
|---|---:|---:|---:|---:|
| full typed enumeration | 3/3 | 194 | 0 | 0 |
| same-designer LLM rule proposal + native check | 3/3 | 41 | 0 | 0 |
| same proposal + native-rejection feedback | 3/3 | 46 | 0 | 1 |

Per task:

| task | full | LLM subset | hybrid final |
|---|---:|---:|---:|
| Path positive | 76 checks / 7 terms | 5 / 1 accepted | 5 / 1 accepted |
| event positive | 59 / 1 | 24 / 1 accepted | 24 / 1 accepted |
| finite-to-exact negative | 59 / 4 rejected | 12 / 1 rejected | 17 total / 0 terms after removing the rejected rule |

Descriptive nanosecond timings are preserved in the run but are not treated as
performance evidence: each cell was executed once, all searches are tiny, and
the same process designed the rule subsets.  Timing is excluded from the
deterministic replay digest.

## What this evaluation establishes

Within these three fixed tasks, the coordinator can:

1. preserve a positive use where Path coherence is the requested result;
2. preserve exact completion when a separate event carrier is declared;
3. distinguish symbolic grammar typing from native Cubical inhabitation;
4. retain a rejected candidate and its exact failure receipt;
5. feed that rejection back into the declared rule set and make the unsupported
   goal disappear within the remaining budget; and
6. deterministically replay the comparison from pinned inputs.

This is stronger evidence about the control loop than the earlier single L3
obstruction and one-rule ablation.  It shows that the machine path can generate,
accept, reject and revise candidates without merging those states.

After this run, M3 breadth required new live native renderers. The original v1
freeze deliberately rejects that evolution because it pins live adapter paths.
Before editing those paths, all 10 frozen adapter/search sources were copied to
`REPLAY-CLOSURE-v2/snapshot/`; replay run
`20260913-M4-LITE-L3-REPLAY-V2` recomputes the same semantic digest from the
same task/run pins. It remains valid after the 0.4.0 renderer expansion. Exact
v1 failure and v2 success are recorded in
`REPLAY-CLOSURE-v2/POST-EVOLUTION.json`.

## What it does not establish

The same AI knew the three task roles and native gold outcomes, wrote the native
adapters, then wrote the TaskSpecs, grammars and rule subsets.  The smaller 41
versus 194 check count therefore mainly measures successful relevance slicing
on self-authored grammars.  It does not show a blind LLM advantage, novelty,
training-data independence, robustness to independently authored tasks, or
general effectiveness on HoTT research.

The next effectiveness upgrade requires tasks or rule proposals whose exact
solutions were not visible to their selector, a larger denominator, repeated
timings if latency matters, and at least one natural-source-derived task.  Gold
labels must remain fixed even when every mode fails.

## Evidence

- protocol: `machine-overview/evaluations/M4-LITE-L3-001/PROTOCOL.json`
- design freeze: `machine-overview/evaluations/M4-LITE-L3-001/DESIGN-FREEZE.json`
- exact evaluation spec: `machine-overview/evaluations/M4-LITE-L3-001/SPEC.json`
- replayable result:
  `machine-overview/evaluations/M4-LITE-L3-001/runs/20260913-M4-LITE-L3-001/RUN.json`
- evolution-safe replay result:
  `machine-overview/evaluations/M4-LITE-L3-001/runs/20260913-M4-LITE-L3-REPLAY-V2/RUN.json`
- task/case/search/native/review/report assets under their standard
  `machine-overview/` directories

These are machine-overview evaluation artifacts.  They do not create a formal
mathematical claim and do not enter `HoTT/CLAIM_EVIDENCE_MATRIX.md`.
