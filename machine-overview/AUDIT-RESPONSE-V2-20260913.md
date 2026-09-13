# Strict-v2 response to the M1 repair re-audit and first L3 extension

- Status: `SECOND-AUDIT P1/P2 FIXED / STRICT V2 RE-RUN / FIRST SYMBOLIC L3 CASE / LOCAL BRANCH VERSION-CLOSED`
- Date: 2026-09-13
- Worktree: `/Volumes/D/HoTT-machine-overview`
- Branch: `feat/machine-overview-m1`
- Starting HEAD: `2705847db5893bbbdfae21abb58c5a01beff6e27`

This response addresses the re-audit
`/Volumes/D/HoTT独立答复/20260913-M1自动化统观修复复审.md`.
That audit confirmed that the original F1–F7 triggers were repaired, then found
five P1 and three P2 trust-boundary gaps. The implementation below was made
only in the isolated worktree. The main branch was not modified, merged,
tagged or pushed.

## P1 findings

### P1.1 Toolchain, registry and runner identity were incomplete

Strict profiles now require byte hashes for both `TOOLCHAIN.json` and
`AGDA_LIBRARIES`; qualification also checks that the registry resolves the
exact Cubical library file pinned by the toolchain. The Agda executable,
Cubical library file and 1,111-file source tree remain independently checked.

Every strict search/verify run now stores:

- `runner-manifest.json` with Python version/executable/hash and Git identity;
- a byte-for-byte snapshot of `mo.py`, `registry.json` and every coordinator
  package module under `runner-snapshot/`;
- exact source roster, byte counts and hashes;
- run fields checked against the registry inside that saved snapshot.

Validation uses the snapshot without requiring future live coordinator bytes to
remain unchanged. During a run, live bytes must remain equal to the captured
snapshot or the run aborts.

Regression coverage includes toolchain-file drift, library-registry drift and
runner-snapshot tampering.

### P1.2 Artifact roster and hashes were incomplete

Strict verify validation now requires the exact five generated Agda sources,
re-renders Target/Proof/Verify/Controls/Falsify from the frozen inputs, checks
source bytes and hashes, and verifies proof hygiene.

For every kernel step it checks:

- exact label order: verify, controls, negative-control, verify-replay;
- exact artifact files: command, environment, stdout and stderr;
- artifact path, bytes and SHA-256;
- command JSON against the run receipt;
- independently reconstructed Agda argv, cwd, entry, success expectation and
  timeout;
- environment artifact bytes;
- stdout/stderr-derived diagnostic, status and expectation result;
- replay derived again from the two verify outputs;
- exact source/import closure, profile and toolchain identity;
- target-freeze ledger entry and receipt classification.

Agda `.agdai` files remain explicitly treated as disposable caches rather than
evidence sources.

### P1.3 Semantic/status validation and legacy handling were fail-open

Search generation and validation share the same deterministic semantic
functions. Validation recomputes budgets, enumeration statistics, order
independence, grammar sensitivity, controls, calibration comparison, witness
set, observations, separation kinds, AST hashes and exit reason from the frozen
grammar and seed.

Verify status is recomputed from raw kernel outputs and replay. Changing a
stored separation label, kernel status or final status is rejected.

All pre-v2 cases, runs, interrupted attempts and reviews are now accepted only
at exact hashes in `legacy/legacy-evidence-v1.json`. A marker file has no power
to classify a new or changed artifact as legacy. The manifest lists the known
schema gaps so a `VALID` workspace does not imply that old evidence acquired
fields it never had.

### P1.4 Correspondence and report selection could bind the wrong evidence

Strict correspondence reviews are now fully recomputable from the exact case,
qualified profile, task, grammar, search receipt and witness. They rederive the
mechanism, consumer requirements, observation class, compensation class,
checklist and conclusion. Profile failure or witness/status tampering produces
`REVIEW_REQUIRED` or validation failure.

Reports select verify runs and reviews only when `source_search_run.run_id` and
its exact SHA-256 both match the chosen search receipt. Evidence from a
different search of the same case revision is excluded.

### P1.5 Search run IDs could escape the run root

Case, run, search-run and witness identifiers use one strict identifier
validator before path construction. Values such as `../outside` fail with
`UNSAFE_IDENTIFIER` before any directory is created. User-supplied file paths
are resolved inside the repository and fail with `PATH_OUTSIDE_REPO` otherwise.

## P2 findings

### P2.1 RUN and ATTEMPT could disagree

Every strict run requires `machine-overview-attempt/v2`, final status
`COMPLETED`, an end timestamp, identical run/case/revision identity, identical
witness and AST identity for verify runs, the same attempt number and the exact
planned step list. Mismatches are validation errors.

### P2.2 A sparse grammar could produce an out-of-grammar negative control

Search chooses the least declared deadline horizon at or above both input
indices. If no such horizon exists it records
`CONTROL_NOT_AVAILABLE_IN_GRAMMAR`; strict native verification refuses to
invent an undeclared horizon. Regression tests cover both a declared sparse
case and the unavailable-control failure.

### P2.3 Documentation and version state had drifted

The coordinator is version `0.2.0`. `registry.json`, `README.md`, this response
and `HANDOFF-20260913.md` now describe the same strict-v2 behavior, exact
evidence counts and partial M2/M3 status. The earlier F1–F7 response remains as
a labeled historical audit response instead of being rewritten as if its old
29-test/11-run snapshot were current.

## Strict L1 acceptance chain

| Item | Current result |
|---|---|
| Case | `MS-TASK-L1-RACE-COMPLETION-001` revision 4 |
| Profile | `L1-PARTIALITY-RACE-DEADLINE-v2`, fully qualified |
| Search | `20260913-SEARCH-L1-V2-001`: 4,788/4,788 checks, 50 witnesses, complete, benchmark PRESENT |
| Deadline | `20260913-VERIFY-L1-V2-DEADLINE-001`: 0/0/42(expected)/0, exact replay |
| Value | `20260913-VERIFY-L1-V2-VALUE-001`: 0/0/42(expected)/0, exact replay |
| Completion | `20260913-VERIFY-L1-V2-COMPLETION-001`: 0/0/42(expected)/0, exact replay |
| Correspondence | three exact-search-bound reviews, all model-level preservation checks PASS |
| Report | `reports/MS-TASK-L1-RACE-COMPLETION-001-r4-v2-report.md` |

The L1 result remains a calibration of existing C-73–C-76 mechanisms. It adds
evidence integrity, not a new mathematical claim.

## First M2/L3 slice

After the strict M1 repair, a small generic typed symbolic proof search was
added and exercised on a time/motion-structure TaskSpec. The configuration asks
what happens when an exact Pending→Done completion observation is represented
as one Cubical-dimension-indexed term.

| Item | Result |
|---|---|
| Case | `MS-TASK-L3-INTERVAL-COMPLETION-001` revision 1 |
| Profile | `L3-CUBICAL-INTERVAL-MOTION-v1`, fully qualified |
| Search | `20260913-SEARCH-L3-SYMBOLIC-001`: 39 rule checks, two proof trees, depth-4 grammar complete |
| Minimal proof | `apart_elim(interval_eta)` / `apart ((λ i → f i))` |
| Ablation | remove `interval_eta` → zero goal proofs |
| Native run | `20260913-VERIFY-L3-SYMBOLIC-001`: 0/0/42(expected)/0, exact replay |
| Status | `NATIVE_CHECKED_EXPLORATION_CANDIDATE` |
| Correspondence | `PRESERVED_ACROSS_DECLARED_ENDPOINT_OBSERVATION`; reality `UNRESOLVED` |
| Report | `reports/MS-TASK-L3-INTERVAL-COMPLETION-001-r1-report.md` |
| Academic assessment | `evaluations/L3-ACADEMIC-BRIDGE-001.md` |

The native development probe also caught an important modeling error: `I` has
the special sort `IUniv` and is not an ordinary Type. The final control therefore
uses a genuine `Segment : Type` with a path constructor. This is consistent
with the official Cubical Agda documentation and prevents the report from
calling `I` a physical-time type.

The L3 result is a concrete model-relative obstruction generated by the
declared theoryization. No checked primary source requires all exact completion
predicates to be I-indexed, so this is not classified as a HoTT BUG. It is the
first successful machine-overview result outside the L1 finite delay model and
shows that the system can both find a relation and stop it at the correct
interpretation boundary.

## Verification snapshot

- `python3 machine-overview/mo.py selftest`: 41/41 PASS before the final
  documentation-only update; final rerun is required before handoff.
- `python3 machine-overview/mo.py validate`: `VALID`, 0 errors after the L3
  native run; final rerun is required before handoff.
- Current evidence inventory before final rerun: 5 cases, 17 runs, 7 reviews,
  one registered interrupted legacy attempt.

## Remaining limits

- The current symbolic backend is one Horn-style proof grammar. It is not a
  general dependent-term, HIT, higher-coherence or universe solver; M2 is
  partial.
- Only L1 and one L3 chain exist; M3 six-line coverage is partial.
- The engine/task ordering is a search-configuration holdout with a documented
  designer-visibility limitation. It is not a blind LLM, novelty or full M4
  effectiveness evaluation.
- The L3 standard-use and physical-reality bridges remain open.
- Main-line STATE/projections, canonical formal proof capture and claim matrix
  were not changed. M5 remains unimplemented and requires an explicit,
  reviewable integration decision.
- This report is carried by the authorized local branch commit. Its exact OID
  is read from Git after commit rather than self-embedded here. No tag, push,
  merge or main-line checkpoint is claimed by this document.
