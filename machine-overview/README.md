# Machine-overview coordinator (plan stages M0/M1)

Status: `IMPLEMENTED_AND_EXERCISED_IN_ISOLATED_WORKTREE / NOT_INTEGRATED_INTO_MAIN_LINE`.

This directory implements the first two stages of the plan
`/Volumes/D/HoTT独立答复/HoTT非现实性悖论机器统观完整方案.md`
(index + 9 shards — read the plan itself; this README is not a substitute):

- **M0 规则与任务资格化** — a pinned profile (toolchain + source hashes + declared
  symbol map), a frozen TaskSpec, and positive/negative controls;
- **M1 最小完整搜索链** — automatic typed enumeration → finding differences →
  reduction → exact native Cubical Agda check → correspondence review → report →
  save/restore, exercised end-to-end on the L1 calibration (delay / race /
  deadline fragment of the already machine-proved `MP-RACE-TIMEOUT-001`).

It is a research instrument, not a claim database. Exploration receipts live
under `machine-overview/runs/`; they do **not** enter
`HoTT/CLAIM_EVIDENCE_MATRIX.md`.

## Layout

```text
machine-overview/
  mo.py                     launcher: python3 machine-overview/mo.py <command>
  machine_overview/         coordinator package (stdlib only)
  profiles/                 pinned theory profiles (toolchain + sources + symbols)
  tasks/                    TaskSpec revisions (input, observation, completion, correspondence)
  grammars/                 declared search grammars (bounded, typed, revisioned)
  cases/<case-id>/          immutable case revisions (profile/task/grammar hashes)
  runs/<run-id>/            search and verify receipts + generated Agda sources
  formal/MVSupport.agda     pinned support lemmas (trusted base, not generated)
  reviews/                  correspondence checklist reviews
  reports/                  human-readable calibration reports
  generated-index/          rebuildable query projection (derived data)
  tests/                    unit tests + rejected-candidate fixtures
```

## Quick start (from the worktree root)

```bash
python3 machine-overview/mo.py inspect-profile --profile machine-overview/profiles/l1-partiality-v0.json
python3 machine-overview/mo.py create-case --profile machine-overview/profiles/l1-partiality-v0.json \
    --task machine-overview/tasks/MS-TASK-L1-RACE-COMPLETION-001.json \
    --grammar machine-overview/grammars/l1-v1.json --revision 2
python3 machine-overview/mo.py search --case machine-overview/cases/MS-TASK-L1-RACE-COMPLETION-001 \
    --run-id <search-run-id>
python3 machine-overview/mo.py verify --case machine-overview/cases/MS-TASK-L1-RACE-COMPLETION-001 \
    --search-run <search-run-id> --witness WV-0013 --run-id <verify-run-id>
python3 machine-overview/mo.py review-correspondence --case ... --search-run ... --witness WV-0013
python3 machine-overview/mo.py explain --case ...
python3 machine-overview/mo.py list
python3 machine-overview/mo.py validate
python3 machine-overview/mo.py selftest
```

## What the first calibration actually did (2026-09-13)

- Profile `L1-PARTIALITY-RACE-DEADLINE-v0` qualified: Agda `2.8.0-3d04bac`
  (binary SHA-256 pinned), Cubical `v0.9` (library-file and 1,111-file source-tree
  hashes pinned), model source SHA-256 pinned, 20 declared symbols checked at
  their pinned line ranges.
- Search run `20260913-SEARCH-L1-002` (grammar `l1-v1`): **complete enumeration of
  the declared grammar** — 7 delay atoms, 399 well-typed contexts, 4,788
  pair-context checks, 916 separations, reduced to 50 distinct witnesses in three
  families: `deadline_observation` 14, `value_mismatch` 28,
  `completion_divergence` 8.
- Answer independence: the same witness set appears under a shuffled enumeration
  order (`order_independent_set_equal: true`); removing the `deadline` operation
  from the grammar removes the deadline family
  (`mutated_contains_deadline_kind: false`); the known R041 benchmark is found by
  the search (`calibration_match: PRESENT`, related claims `C-73`, `C-74`).
- Native Cubical Agda checks (one minimal witness per family), each with
  `verify` (exit 0), `controls` (exit 0), a negative control that must fail
  (exit 42, expectation met) and a replay with byte-identical stdout/stderr:
  `20260913-VERIFY-L1-DEADLINE-001` (WV-0001),
  `20260913-VERIFY-L1-VALUE-002` (WV-0002),
  `20260913-VERIFY-L1-COMPLETION-002` (WV-0013).
- Two earlier attempts (`...-VALUE-001`, `...-COMPLETION-001`) failed in the kernel
  because of real defects in the generated proof templates (inverted refutation
  lemma; a missing name re-export). Both failure receipts are kept unchanged and
  are part of the evidence.
- Candidate-hygiene negative control: a proof that buys the target with
  `postulate` is rejected before any side effect
  (`CANDIDATE_FORBIDDEN_DECLARATION:external_file:postulate`, exit 2, no run
  directory created). A tampered frozen target hash raises `TARGET_CHANGED`
  (unit test).
- `selftest`: 12/12 unit and negative-control tests pass; `validate`: workspace
  VALID (2 case revisions, 7 runs).

The calibration report is
`machine-overview/reports/MS-TASK-L1-RACE-COMPLETION-001-report.md`.

## Guarantees and boundaries of the implementation

Held:

- the declared grammar is enumerated completely within the budget, and the
  receipt says so explicitly (`complete_within_declared_grammar`);
- reduction is guarded so it cannot silently change the task the candidate
  answers (`reduction_guard` keeps the declared consumers; only parameters
  shrink) — this guard was added as grammar `l1-v1` after run `-001` showed the
  collapse it prevents;
- candidate proofs are rejected by a hygiene scan (`postulate`, `primitive`,
  termination/universe bypasses, incomplete matches) **before** a run id is
  consumed;
- the Target module is generated first, hashed, and re-checked; a verify run
  records its exact target hash, toolchain identity, command, environment,
  stdout/stderr hashes and the replay comparison;
- every verified statement is a ground instance of the declared grammar. No
  universal, implementation-level or physical claim is made.

Not held / not done:

- this is a **calibration instance** of mechanisms already machine-proved as
  `C-73`–`C-76`; it is not a new mathematical claim and is not in the claim
  matrix;
- research lines M2 (symbolic / higher path search), M3 (six-line coverage),
  M4 (search-effectiveness evaluation with held-out tasks) and M5 (project
  integration and maintenance) are not implemented;
- `cvc5`, Alloy and egg are not installed on this host; the plan's SyGuS/SMT
  adapter is a declared future backend;
- L3 (continuity / density / motion structure) and B-direction tasks are absent
  from this profile by declaration, not by success;
- the reality bridge stays `UNRESOLVED`; correspondence reviews are rule-based
  checklists over declared inputs, not philosophical judgments;
- OS-level isolation of arbitrary candidate code is not implemented. M1 follows
  the plan's fallback: candidates are declarative ASTs interpreted by the
  trusted coordinator, and externally supplied proofs are generated/checked
  without executing candidate code.

## Integration gap for stage M5

`scripts/audit/capture_agda_proof_run.py` requires `(project_root / ".git").is_dir()`
and therefore rejects a linked worktree, where `.git` is a file
(`PROJECT_GIT_ROOT_REQUIRED`). The canonical F-011 capture path, the
`HoTT/formal` + `HoTT/verification/runs` + `CLAIM_EVIDENCE_MATRIX.md` delivery,
and the main-line checkpoint are integration work for M5; they were deliberately
**not** executed from this worktree branch. This coordinator therefore writes its
own `machine-overview-*/v1` receipts, which are explicitly labelled as
exploration/calibration evidence.

## Source and plan anchors

- Plan: `/Volumes/D/HoTT独立答复/HoTT非现实性悖论机器统观完整方案.md` (index + 9 shards,
  `HOTT-MACHINE-OVERVIEW-PLAN`).
- Pinned model: `HoTT/formal/partiality-race-timeout/PartialityRaceTimeout.agda`
  (`C-71`–`C-76`), toolchain `TOOLCHAIN.json` + `AGDA_LIBRARIES`.
- Related project method: `理解章节/C11-HoTT理论经济账本与悖论位置判别-20260913.md`.
