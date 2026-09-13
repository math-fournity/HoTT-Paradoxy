# Machine-overview coordinator

Status: `M0/M1 STRICT-V2 COMPLETE / M2 FIRST SYMBOLIC SLICE / L3 FIRST CASE / WORKTREE-LOCAL / NOT INTEGRATED INTO MAIN`.

This directory implements the first executable machine-overview chain from
`/Volumes/D/HoTT独立答复/HoTT非现实性悖论机器统观完整方案.md`.
It runs in the isolated worktree `/Volumes/D/HoTT-machine-overview`, branch
`feat/machine-overview-m1`. It has not modified, merged into, tagged or pushed
the main branch.

The coordinator is a research instrument. Its receipts remain under
`machine-overview/`; they do not enter `HoTT/CLAIM_EVIDENCE_MATRIX.md` and do
not by themselves become project mathematical claims.

## What now works

### M0/M1 strict evidence chain

The strict v2 path performs:

```text
qualified profile
  → immutable case revision
  → typed complete search inside a declared grammar
  → structure-derived correspondence review
  → frozen native Cubical Agda target
  → proof + positive controls + expected negative control + replay
  → full evidence revalidation
  → search-hash-bound report
```

New v2 cases and runs bind the exact profile, TaskSpec, grammar, toolchain
configuration, Agda library registry, declared sources, case identity,
candidate AST, frozen target, generated sources, kernel command and output
artifacts, ATTEMPT identity, Python identity and a byte-for-byte coordinator
source snapshot. `validate` recomputes search semantics, witness fields,
correspondence fields, generated source text, kernel classifications, replay and
final status. It does not trust a stored `PASS` string.

Pre-v2 evidence remains byte-identical and readable only when its exact hash is
listed in `legacy/legacy-evidence-v1.json`. Adding an arbitrary `LEGACY.json`
marker cannot bless a new or altered v1 receipt.

### L1 strict-v2 calibration

Case `MS-TASK-L1-RACE-COMPLETION-001` revision 4 uses profile
`L1-PARTIALITY-RACE-DEADLINE-v2`, TaskSpec revision 2 and grammar `l1-v2`.

- Search `20260913-SEARCH-L1-V2-001` exhaustively checks 4,788 pair/context
  combinations and produces 50 reduced witnesses across deadline, value and
  completion-divergence families. Enumeration-order permutation yields the
  same witness set; removing deadline removes that family; the external known
  calibration is found after enumeration.
- Native runs
  `20260913-VERIFY-L1-V2-DEADLINE-001`,
  `20260913-VERIFY-L1-V2-VALUE-001` and
  `20260913-VERIFY-L1-V2-COMPLETION-001` each produce kernel exits
  `0 / 0 / 42(expected) / 0` and
  `EXACT_EXIT_STDOUT_STDERR_MATCH` replay.
- All three correspondence reviews recompute to
  `PRESERVED_AT_MODEL_LEVEL`; reality correspondence stays `UNRESOLVED`.
- Report: `reports/MS-TASK-L1-RACE-COMPLETION-001-r4-v2-report.md`.

This remains a calibration of already known `C-73`–`C-76` mechanisms and is
not a new claim.

### M2 first symbolic slice and L3 first case

The first symbolic backend, `symbolic-horn-v1`, enumerates typed proof trees
through a declared depth, renders the discovered AST into native Cubical Agda,
and keeps rule-order and rule-ablation controls. Its first case is
`MS-TASK-L3-INTERVAL-COMPLETION-001` revision 1.

The task distinguishes temporal order from time/motion structure:

- operational control: `Stage` has `start` and `finish`; its exact Bool phase
  changes from Pending to Done;
- theoryization under test: represent the whole activity by an internal
  dimension-indexed observable `f : I → A`;
- searched obligation: dimension abstraction supplies an endpoint Path, while
  the task requires those endpoint observations to remain distinguishable.

Search `20260913-SEARCH-L3-SYMBOLIC-001` performs 39 rule-application checks,
completely enumerates the four-rule grammar through depth 4, and finds two
proof trees. The smallest has two nodes:

```text
apart_elim(interval_eta)
proof term: apart ((λ i → f i))
```

After removing `interval_eta`, the goal is unreachable. No calibration
benchmark or expected proof AST appears in the grammar.

Native run `20260913-VERIFY-L3-SYMBOLIC-001` checks the symbolic Type₀ target,
the Stage and Segment controls, the expected rejection of applying dimension
abstraction to an ordinary Stage index, and an exact replay. Kernel exits are
again `0 / 0 / 42(expected) / 0`. Its status is deliberately
`NATIVE_CHECKED_EXPLORATION_CANDIDATE`.

The result is a concrete model-relative L3 candidate: the explicit
theoryization adds Path coherence and thereby adds a completion obstacle. It
does not establish that standard HoTT equates Path with physical time or
requires arbitrary discrete completion predicates to be I-indexed. The
academic and interpretation assessment is
`evaluations/L3-ACADEMIC-BRIDGE-001.md`; reality correspondence and originality
remain unresolved/limited exactly as recorded there.

The engine freeze is a configuration holdout, not a blind-model evaluation.
The TaskSpec and grammar were absent at freeze time, while the designing AI
already knew the conceptual experiment. A pre-side-effect hygiene failure led
to one qualified-name correction in the native proof renderer; the post-freeze
assessment records this instead of calling the entire coordinator frozen.

## Current verification snapshot

At the final verification snapshot carried by the branch-local version-closure
commit:

- `selftest`: 41/41 PASS;
- `validate`: `VALID`, 0 errors;
- cases: 5 (three exact-hash legacy v1, L1 strict v2, L3 strict v2);
- runs: 17 (11 legacy v1, six strict v2) plus one registered interrupted legacy
  attempt;
- correspondence reviews: 7 (three legacy, four strict v2);
- all four accepted strict native verification runs have exact byte replay.

The implementation and evidence paths are version-closed on the isolated
feature branch. The exact commit OID is repository metadata and is intentionally
read from Git after commit instead of being self-embedded here. All untracked
`dev-notes/` files are outside the implementation change set and were excluded
from staging.

## Layout

```text
machine-overview/
  mo.py                       CLI launcher
  registry.json               coordinator registry and stage coverage
  machine_overview/           standard-library coordinator package
  profiles/                   pinned theory/toolchain profiles
  tasks/                      independently frozen TaskSpecs
  grammars/                   bounded typed search grammars
  cases/<case-id>/            immutable revisions and target-freeze ledgers
  runs/<run-id>/              ATTEMPT, RUN, runner snapshot, generated sources,
                              kernel commands/environment/stdout/stderr
  reviews/                    recomputable correspondence reviews
  reports/                    exact-search-bound human-readable reports
  evaluations/                engine freeze and L3 interpretation assessment
  formal/                     pinned support/control modules
  legacy/                     exact-hash allowlist for pre-v2 evidence
  generated-index/            rebuildable query projection
  tests/                      unit, regression and fault-injection tests
```

## Commands

Run from `/Volumes/D/HoTT-machine-overview`:

```bash
python3 machine-overview/mo.py selftest
python3 machine-overview/mo.py validate

python3 machine-overview/mo.py inspect-profile \
  --profile machine-overview/profiles/l1-partiality-v2.json
python3 machine-overview/mo.py explain \
  --case machine-overview/cases/MS-TASK-L1-RACE-COMPLETION-001 \
  --revision 4 --search-run 20260913-SEARCH-L1-V2-001

python3 machine-overview/mo.py inspect-profile \
  --profile machine-overview/profiles/l3-interval-motion-v1.json
python3 machine-overview/mo.py explain \
  --case machine-overview/cases/MS-TASK-L3-INTERVAL-COMPLETION-001 \
  --revision 1 --search-run 20260913-SEARCH-L3-SYMBOLIC-001

python3 machine-overview/mo.py list
python3 machine-overview/mo.py query L3
```

Create new run IDs for every new experiment. Do not overwrite immutable case,
run, review or target-freeze records.

## What remains

- **M2 is partial.** The current symbolic backend is a small typed Horn proof
  grammar plus one native Type₀ Path target. It does not yet synthesize general
  dependent terms, universe constraints, arbitrary HIT eliminators or higher
  coherences.
- **M3 is partial.** L1 and one L3 chain are executable. L2, L4, L5 and L6 do
  not yet have machine-overview cases.
- **M4 is not complete.** The L3 configuration was added after a search-engine
  freeze and has an ablation, but there is no same-budget baseline/LLM/mixed
  comparison, sample distribution or defensible performance estimate.
- **M5 is not implemented.** The worktree has not updated main-line STATE,
  direction/panorama projections or the formal claim matrix. The existing
  canonical proof-capture script still assumes `.git` is a directory and needs
  an explicit worktree-compatibility change before main-line integration.
- A standard or natural HoTT consumer that makes the L3 activity-time
  interpretation has not been found. Without that bridge, the L3 result remains
  an interpretation/representation candidate rather than a HoTT defect.
- `cvc5`, Alloy and egg remain uninstalled; no current bottleneck requires them.

## Audit trail

- First audit and F1–F7 response:
  `/Volumes/D/HoTT独立答复/20260913-M1自动化统观实现审计.md` and
  `AUDIT-RESPONSE-20260913.md`.
- Second audit:
  `/Volumes/D/HoTT独立答复/20260913-M1自动化统观修复复审.md`.
- Strict-v2 response and L3 result: `AUDIT-RESPONSE-V2-20260913.md`.
- Current handoff: `HANDOFF-20260913.md`.
