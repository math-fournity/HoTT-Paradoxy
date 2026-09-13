# Machine-overview coordinator (plan stages M0/M1)

Status: `IMPLEMENTED / EXTERNAL AUDIT F1-F7 FIXED / POST-FIX ACCEPTANCE RE-RUN /
ISOLATED WORKTREE / NOT INTEGRATED INTO MAIN LINE`.

This directory implements the first two stages of the plan
`/Volumes/D/HoTT独立答复/HoTT非现实性悖论机器统观完整方案.md`
(index + 9 shards — read the plan itself; this README is not a substitute):

- **M0 规则与任务资格化** — a pinned profile (toolchain + source hashes +
  declared symbol map + pinned support module), a frozen TaskSpec, and
  positive/negative controls;
- **M1 最小完整搜索链** — automatic typed enumeration → finding differences →
  grammar-preserving reduction → exact native Cubical Agda check →
  correspondence review → report → save/restore, exercised end-to-end on the L1
  calibration (delay / race / deadline fragment of the already machine-proved
  `MP-RACE-TIMEOUT-001`).

It is a research instrument, not a claim database. Exploration receipts live
under `machine-overview/runs/`; they do **not** enter
`HoTT/CLAIM_EVIDENCE_MATRIX.md`.

The external audit of the first version (`REQUEST_CHANGES`, findings F1–F7) is
answered in `machine-overview/AUDIT-RESPONSE-20260913.md`; every finding is
fixed and covered by a regression test.

## Layout

```text
machine-overview/
  mo.py                     launcher: python3 machine-overview/mo.py <command>
  machine_overview/         coordinator package (stdlib only)
  profiles/                 pinned profiles (v0 legacy-era, v1 current)
  tasks/                    TaskSpec revisions
  grammars/                 declared search grammars (bounded, typed, revisioned)
  cases/<case-id>/          immutable case revisions + target-freeze ledgers
  runs/<run-id>/            search/verify receipts, ATTEMPT.json, generated Agda
  formal/MVSupport.agda     pinned support lemmas (trusted base, not generated)
  reviews/                  structure-derived correspondence reviews
  reports/                  human-readable calibration reports
  generated-index/          rebuildable query projection (derived data)
  tests/                    unit tests + audit regression tests + fixtures
  AUDIT-RESPONSE-20260913.md
```

Pre-audit receipts stay in place and carry a `LEGACY.json` attestation; the
three pre-audit correspondence reviews live in `reviews/.superseded/`.

## Quick start (from the worktree root)

```bash
python3 machine-overview/mo.py inspect-profile --profile machine-overview/profiles/l1-partiality-v1.json
python3 machine-overview/mo.py create-case --profile machine-overview/profiles/l1-partiality-v1.json \
    --task machine-overview/tasks/MS-TASK-L1-RACE-COMPLETION-001.json \
    --grammar machine-overview/grammars/l1-v1.json --revision 3
python3 machine-overview/mo.py search --case machine-overview/cases/MS-TASK-L1-RACE-COMPLETION-001 \
    --revision 3 --run-id <search-run-id>
python3 machine-overview/mo.py verify --case machine-overview/cases/MS-TASK-L1-RACE-COMPLETION-001 \
    --revision 3 --search-run <search-run-id> --witness WV-0013 --run-id <verify-run-id>
python3 machine-overview/mo.py review-correspondence --case ... --revision 3 \
    --search-run <search-run-id> --witness WV-0013
python3 machine-overview/mo.py explain --case ... --revision 3
python3 machine-overview/mo.py list          # read-only
python3 machine-overview/mo.py get WV-0013   # read-only, all matching revisions
python3 machine-overview/mo.py validate      # re-derives validity from evidence
python3 machine-overview/mo.py selftest
```

## Post-fix acceptance run (2026-09-13)

- Case revision 3 uses profile `L1-PARTIALITY-RACE-DEADLINE-v1` (model source,
  pinned support module, toolchain, Cubical tree).
- Search `20260913-SEARCH-L1-003`: **complete enumeration** of the declared
  grammar — 7 delay atoms, 399 well-typed contexts, 4,788/4,788 pair-context
  checks, 916 separations, 50 reduced witnesses in three families
  (`deadline_observation` 14, `value_mismatch` 28, `completion_divergence` 8);
  order-permutation set equality, grammar-sensitivity (removing `deadline`
  removes that family), benchmark `PRESENT` (`C-73`, `C-74`).
- Native kernel runs, each bound to (case revision, search run hash, witness AST
  hash, frozen target hash), with positive control, diagnostic-checked negative
  control and replay:
  `20260913-VERIFY-L1-POSTFIX-DEADLINE-001` (WV-0001),
  `20260913-VERIFY-L1-POSTFIX-VALUE-001` (WV-0002),
  `20260913-VERIFY-L1-POSTFIX-COMPLETION-001` (WV-0013) — all
  `NATIVE_CHECKED_CALIBRATION_INSTANCE`, kernels 0 / 0 / 42(expected) / 0,
  replay `EXACT_EXIT_STDOUT_STDERR_MATCH`.
- Audit regression scenarios (see the response document for details):
  cross-revision verify rejected; stale-grammar search rejected; missing kernel
  output makes `validate` INVALID; budget exhaustion never claims completeness;
  sparse deadline grammar produces no out-of-grammar witnesses; an interrupted
  attempt is recorded and rolled over; a `postulate` proof is rejected before
  any side effect; the value-mismatch review no longer claims a business
  continuation.
- `selftest`: 29/29; `validate`: `VALID` with 11 runs, 7 legacy-attested runs and
  1 recorded interrupted attempt.

The calibration report is
`machine-overview/reports/MS-TASK-L1-RACE-COMPLETION-001-r3-report.md`.

## Guarantees and boundaries of the implementation

Held:

- **frozen inputs**: every entry point re-hashes the profile/task/grammar pinned
  in the case revision and refuses to run on any mismatch;
- **evidence identity**: verify receipts bind case revision, case identity hash,
  search run + sha256, witness AST sha256 and the frozen `Target` hash; a
  persistent per-case target-freeze ledger detects target changes;
- **kernel evidence**: every kernel invocation is recorded with command, cwd,
  environment, stdout/stderr bytes and hashes; `validate` re-derives validity
  from those artifacts instead of trusting status strings;
- **grammar-preserving reduction**: every emitted witness is a member of the
  declared grammar (bounds, continuations, deadline parameters, depth);
- **budget honesty**: completeness, budget stops and capture limits are separate
  fields; a truncated search never reports completeness;
- **failure visibility and recovery**: runs write `ATTEMPT.json` before work;
  interruptions are recorded, same-id retries roll the interrupted attempt aside
  instead of deleting it, kernel runs have an internal timeout with
  process-group termination, and the negative control must show the expected
  type-error diagnostic;
- **correspondence derived from structure**: mechanism text and compensation
  class come from the actual ops/observations; task preservation is computed
  from explicit checks and falls back to `REVIEW_REQUIRED`.

Not held / not done:

- this is a **calibration instance** of mechanisms already machine-proved as
  `C-73`–`C-76`; it is not a new mathematical claim and is not in the claim
  matrix;
- research lines M2 (symbolic / higher-path search), M3 (six-line coverage),
  M4 (search-effectiveness evaluation with held-out tasks) and M5 (project
  integration) are not implemented;
- `cvc5`, Alloy and egg are not installed on this host;
- L3 (continuity / density / motion structure) and B-direction tasks are absent
  from this profile by declaration, not by success;
- the reality bridge stays `UNRESOLVED`; correspondence reviews are rule-based
  checklists over declared inputs, not philosophical judgments;
- OS-level isolation of arbitrary candidate code is not implemented: M1 uses
  declarative ASTs plus coordinator-templated or hygiene-checked proof sources.

## Integration gap for stage M5

`scripts/audit/capture_agda_proof_run.py` requires `(project_root / ".git").is_dir()`
and therefore rejects a linked worktree, where `.git` is a file
(`PROJECT_GIT_ROOT_REQUIRED`). The canonical F-011 capture path, the
`HoTT/formal` + `HoTT/verification/runs` + `CLAIM_EVIDENCE_MATRIX.md` delivery,
and the main-line checkpoint are integration work for M5; they were deliberately
**not** executed from this worktree branch.

Two of the six canonical verifiers also depend on gitignored nested assets and
fail in a fresh worktree (documented in the session record):
`verify_understanding_merge.py` needs `AI对话录/理解章节`;
`verify_fresh_three_way.py` needs
`sources/local-gpt/ALL-Markdown-root/HoTT_is_GONE_COMPLETE.md`. The other four
verifiers PASS in the worktree.

## Source and plan anchors

- Plan: `/Volumes/D/HoTT独立答复/HoTT非现实性悖论机器统观完整方案.md` (index + 9 shards).
- External audit: `/Volumes/D/HoTT独立答复/20260913-M1自动化统观实现审计.md`
  (index + 3 shards) and the reproduction package
  `…/20260913-M1实现审计-e4ab45b/`.
- Pinned model: `HoTT/formal/partiality-race-timeout/PartialityRaceTimeout.agda`
  (`C-71`–`C-76`), toolchain `TOOLCHAIN.json` + `AGDA_LIBRARIES`.
- Related project method: `理解章节/C11-HoTT理论经济账本与悖论位置判别-20260913.md`.
