# Machine-overview coordinator

Status: `M0/M1 STRICT-V2 COMPLETE / M2 SYMBOLIC SLICE / M3 SIX-LINE WALKING SKELETON COMPLETE / L5 FOUR-CAPABILITY + 5-SOURCE CONSUMER QUALIFICATION / HOTT QUOTATION-LATER BRIDGE WITH GUARDED FORCE-ERASURE DEFENSE / CCTT TICK-IRRELEVANCE OPERATIONAL GAP WITH REPRESENTATION DEFENSE / M4-LITE SNAPSHOT-REPLAYABLE / L3 NATURAL-CONSUMER 7-SOURCE BOUNDED NEGATIVE / M5 PARTIAL FORMAL-CAPTURE + R1 DIVERGENCE + GODEL NAT-PROOF INFRASTRUCTURE + AUTHOR COQ INCOMPLETENESS REPLAY + MACHINE-PROVED BOUNDED CANDIDATE COVERAGE / WORKTREE-LOCAL`.

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

### M4-lite three-task comparison

`evaluations/M4-LITE-L3-001/` freezes the unchanged `symbolic-horn-v1`
search source from implementation commit `025938a…`, the three task roles,
same-budget protocol and native adapters before any new TaskSpec or grammar
exists. The same AI designed the roles, adapters, later tasks and rule subsets,
so this is a descriptive pilot rather than a blind-model evaluation.

Three post-freeze tasks exercise different outcomes:

- `MS-TASK-L3-PATH-COHERENCE-POSITIVE-001`: Path coherence is the requested
  result; native verify accepts `λ i → f i`;
- `MS-TASK-L3-EXPLICIT-EVENT-BOUNDARY-001`: an ordinary Stage structure keeps
  exact start/finish/apartness facts; native verify accepts the three-fact
  product; and
- `MS-TASK-L3-FINITE-TO-EXACT-001`: symbolic search proposes
  `finiteToExactCandidate finite`, while native Cubical Agda rejects the
  undeclared exact-lift rule and preserves the failed run.

All three full grammars complete through depth 4, retain order-independent
witness sets and lose the goal under the declared key-rule ablation. Under the
same canonical-check budget, full enumeration uses 194 checks, the
same-designer LLM rule subsets use 41, and native-feedback mode uses 46. The
feedback mode removes the rejected finite-to-exact rule and reruns to zero goal
candidates. All modes make the expected final decision on 3/3 tasks with zero
false promotion. The result replays to deterministic digest
`199793e000ba3de879d0f85c225b20b876775ccfa34f5abac9829004c8a90028`.

Report: `evaluations/M4-LITE-L3-001/REPORT.md`. The lower check count mainly
measures relevance slicing on self-authored grammars; it does not establish
general LLM or machine-overview effectiveness.

### L3 natural-consumer bounded audit

`evaluations/L3-NATURAL-CONSUMER-AUDIT-001/` freezes seven primary-source
versions, exact E1–E6 hit criteria and a no-global-extrapolation rule. Remote
PDF bytes stay in an external cache; the repository pins their URLs, sizes,
hashes, page-marked extracted text identity and extraction runtime. A
deterministic inventory covers all seven sources and the complete 1,111-file
Cubical v0.9 tree.

The per-source assessment finds zero construction satisfying all E1–E6. The
three strongest counter-readings are preserved: the HoTT Book's
moment-in-time path intuition, GCTT's cubical constraint on fixed-point
unfolding, and Directed HoTT's execution paths. They do not close the bridge:
the book bounds the intuition to homotopical identity, guarded/clocked theories
use `later`, clocks or ticks for progression, and Directed HoTT adds a distinct
`hom` type for irreversible paths.

The result is therefore
`ZERO_E1_TO_E6_HITS_IN_FROZEN_SEVEN_SOURCE_SET / L3_CANDIDATE_NOT_UPGRADED`.
Within this set the evidence favors `REPRESENTATION_BOUNDARY / DEFENSE_WORKS`;
it does not prove global nonexistence. Full assessment:
`evaluations/L3-NATURAL-CONSUMER-AUDIT-001/ASSESSMENT.md`.

### M3 six-line walking skeleton

`evaluations/M3-BREADTH-001/` freezes four native adapters and the shared
`M3-CUBICAL-BREADTH-v1` profile before the L2/L4/L5/L6 TaskSpec/grammar pairs
exist. Together with the prior L1/L3 chains, every line now has at least one
real TaskSpec, complete declared-grammar search, native verify/control/rejection
and replay, correspondence review and report.

| line | new case | search | native |
|---|---|---:|---|
| L2 local existence/global completion | `MS-TASK-L2-TRUNCATED-LIMIT-001` | 62 checks / 2 terms | 0 / 0 / 42 / 0 exact |
| L4 identity/operational observation | `MS-TASK-L4-SIP-OBSERVATION-001` | 50 / 1 | 0 / 0 / 42 / 0 exact |
| L5 self-description/internal guarantee | `MS-TASK-L5-SELF-GUARANTEE-001` | 44 / 2 | 0 / 0 / 42 / 0 exact |
| L6 compensation composition | `MS-TASK-L6-COMPENSATION-COHERENCE-001` | 90 / 4 | 0 / 0 / 42 / 0 exact |

L2 reconstructs existing C-114–C-116; L4 reconstructs existing C-124–C-128;
L6 deliberately reuses the known Path/apartness mechanism. L5 is the only new
configuration: an exact section representing every `A → Bool` predicate is
instantiated at its diagonal predicate and yields a Boolean-negation fixed
point, while checking one already supplied proof remains a positive control.
It does not formalize Gödel incompleteness, a proof predicate, reflection or an
actual HoTT self-guarantee consumer; ERCF-3 remains gated.

M3 is complete only at walking-skeleton breadth. General dependent-term/HIT
search, natural consumers and deep results in the four lines remain open.
Report: `evaluations/M3-BREADTH-001/REPORT.md`.

### L5 consumer-qualified self-reference

`evaluations/L5-CONSUMER-QUALIFICATION-001/` deepens the M3/L5 placeholder
without changing the symbolic search engine. It freezes four distinct roles
before their TaskSpecs and grammars exist:

| capability | case | search | native |
|---|---|---:|---|
| supplied-proof checking | `MS-TASK-L5-GIVEN-PROOF-CHECK-001` | 20 checks / 1 term | 0 / 0 / 42 / 0 exact |
| one-fuel proof search | `MS-TASK-L5-BOUNDED-PROOF-SEARCH-001` | 26 / 1 | 0 / 0 / 42 / 0 exact |
| closed finite-fragment truth | `MS-TASK-L5-FINITE-TRUTH-DECISION-001` | 6 / 1 | 0 / 0 / 42 / 0 exact |
| Löb self-certification boundary | `MS-TASK-L5-LOB-SELF-CERTIFICATION-001` | 33 / 1 | 0 / 0 / 42 / 0 exact |

The first three cases are positive capability controls. The fourth composes
the exact conditional interface
`reflect A : Box A → A`,
`lob A : Box (Box A → A) → Box A`, and
`certify A : Box (Box A → A)` at bottom. It does not assert that a real HoTT
system supplies those operations.

The independent Q1–Q6 source matrix pins Agda reflection 2.8.0, MetaRocq 9.1
at `c8cd4605…`, 2LTT v5, NBE-in-type-theory v4 and the current local ERCF-3
modules. All 49 source anchors replay, and no one source passes all six
consumer criteria. MetaRocq is the strongest near-hit: raw quotation/cojoin
and self-erasure are real, while typed quotation remains in progress and the
safe checker relies on a strong-normalization postulate. 2LTT explicitly moves
HoTT metatheory to an outer theory; Agda reflection runs through its built-in
`TC` interface.

Verdict:
`NO_QUALIFIED_CONSUMER_IN_FROZEN_SET / GENERIC_LOB_BOUNDARY_ONLY /
ERCF3_STILL_GATED`. Full report:
`evaluations/L5-CONSUMER-QUALIFICATION-001/REPORT.md`.

### HoTT quotation/later bridge and guarded force erasure

`evaluations/HOTT-QUOTATION-BRIDGE-001/` follows the L5 result into a fixed
HoTT-adjacent time mechanism. It prevents three superficially similar carriers
from being identified:

- Agda `TC A` is a host type-checking computation;
- MetaRocq `□A` is syntax or typed-proof quotation; and
- GCTT/CCTT `▷κ A` means that data becomes available after a tick.

Six fixed source systems, twelve artifacts and 66 H1–H6 anchors feed ten actual
Agda probes. Every probe matches its declared result and exact replay. The
central accepted conditional target is:

```text
collapse : (▷ ⊥ → ⊥) → ⊥
collapse forceNow = fix forceNow
```

GCTT's guarded `fix : (▷A → A) → A` makes an unrestricted fixed-clock
`forceNow : ▷A → A` collapse at bottom. The real systems retain the time
qualification: Agda rejects `▷A` as `A`; GCTT has no unrestricted now
eliminator; CCTT's controlled force requires an all-clock input
`(∀κ. ▷κ Aκ) → ∀κ. Aκ`; and a second negative probe rejects using one local
clock value as that global family.

The complete forcing-ticks source tree has only nine `force*` matching lines in
two files. Its one downstream use constructs the full clock-indexed family
before calling `force`; no fixed-clock erasure consumer appears. The standard
pinned Agda 2.8.0 binary cannot compile the experimental forcing-ticks source
(`InvalidTypeSort`), which is recorded as a toolchain-version mismatch rather
than a mathematical failure.

Verdict:
`GUARDED_FORCE_ERASURE_CONDITIONAL_COLLAPSE_WITH_DEFENSE /
HOTT_BUG_NOT_ESTABLISHED`. This specializes the existing guard-erasure core to
actual GCTT/CCTT rules and compiler diagnostics; it is not claimed as an
original guarded-recursion theorem. Full report:
`evaluations/HOTT-QUOTATION-BRIDGE-001/REPORT.md`.

### CCTT tick irrelevance versus current reduction

`evaluations/TICK-IRRELEVANCE-OPERATIONAL-GAP-001/` closes the bridge's
toolchain gap by building and running the exact historical Agda
`forcing-ticks` checker at commit `5bec849…`. The checker operationally
distinguishes forcing tick `◇` from an ordinary tick: the former makes a
guarded fixed point judgementally unfold at the current checking step, while
the latter exposes the same endpoint only through `pfix'` or `force-delay`
Path equality.

The frozen evaluator combines three evidence forms:

- six source signatures across four pinned source trees locate both tick
  irrelevance/Path rules and the reducer's `ForcingTick` branch;
- a complete three-assumption equality search finds the unique minimal
  conditional path from `true` to `false`, and removal of any assumption makes
  the target unreachable; and
- nine native probes check the internal-observer collision, two independent
  negative controls, exact `Clocked.Primitives`, diamond computation,
  ordinary-tick Path computation and the corresponding failed `refl` claims.

All 9 probes meet their frozen expectation and reproduce exact
stdout/stderr/exit bytes on internal replay and an independent `--rerun`.
Actual consumers do not cross the boundary: ticks remain special syntax,
operation discrimination remains in the meta reducer, and `pfix`, `tirr` and
`force-delay` remain Path witnesses rather than judgemental equalities.

Verdict:
`EXTENSIONAL_TICK_IRRELEVANCE_WITH_METALEVEL_OPERATIONAL_SPLIT /
REPRESENTATION_BOUNDARY / NATURAL_USAGE_MISMATCH_NOT_FOUND_IN_FROZEN_SET /
HOTT_BUG_NOT_ESTABLISHED`. Full report:
`evaluations/TICK-IRRELEVANCE-OPERATIONAL-GAP-001/REPORT.md`.

### Nontermination and Gödel evidence extensions

The living route is `HOTT-NONTERMINATION-MACHINE-OVERVIEW-PLAN.md`. It keeps
proof checking, proof search, object-program execution, normalization,
productive infinitude, undecidability and Gödel incompleteness as distinct
phenomena. The user-supplied 1,115-line research plan is preserved byte for
byte under `literature/snapshots/`, with its source identity recorded in
`literature/README.md`.

Three executable extensions now connect the earlier search coordinator to
native source/run/index evidence:

- `REFLECTED-TICK-REDUCTION-OBSERVER-001` uses ten frozen Agda probes to
  separate host-syntax reflection from object-level Path-respecting
  observation and to calibrate manually termination-asserted recursion. It is
  an implementation-level completion boundary, not a Gödel instance. Revision
  5 freezes the 99-file project-formal-tree denominator as an exhaustive
  per-file snapshot and reproduces all ten probes exactly, without making later
  unrelated formal packages invalidate the operational replay. Revision 1
  reports stale by design, and two path/module qualification failures are preserved.
- `COQ-HOTT-REFLECTIVE-TYPECLASS-RECURSION-001` builds Coq-HoTT commit
  `cc618472…` under Rocq 9.0.1 and compares default, registered, bounded-depth,
  known-equivalence and generic recursive typeclass search. Eight probes replay
  exactly; the result is a community HoTT automation recursion boundary.
- `PF-CUBICAL-MACHINE-HALTING-001` defines a deterministic two-counter object
  machine and machine-proves one fixed halt, one fixed all-finite-step
  divergence and its non-halting consequence. This reaches R1 certified
  concrete divergence. It does not yet reach R2 universal undecidability.

The Gödel branch now has a five-package Cubical Agda chain:

```text
raw proof checker
  → postfix proof serialization
  → self-delimiting formula bits
  → self-delimiting proof bits
  → natural-number proof code and total checker
```

Across these packages, 20 exact claims have source manifests, kernel receipts,
frozen claim-matrix rows and independent byte-exact replay. The final package
proves proof-code roundtrip and injectivity, checker commutation, and both
directions between accepted natural-number proof codes and indexed
derivations. This is an externally effective proof relation for one small
Hilbert calculus. Object-level arithmetic representability, a fixed-point
sentence, Gödel/Rosser unprovability, exact HoTT-calculus instantiation and the
reality correspondence all remain open. Full assessment:
`evaluations/CUBICAL-GODEL-PROOF-CHECKER-001/REPORT.md`.

`PF-CUBICAL-SYNTHETIC-INCOMPLETENESS-001` adds the conditional theorem core.
Under an explicit universal step-indexed partial-function hypothesis, it
constructs the input on which every self-return separator diverges; a formal
system with an effective proof/refutation classifier and strong separation
therefore has an independent sentence, and every extension inherits one.
Its five claims replay exactly. Universality, classifier construction and
strong separation are parameters of this package, so by itself it is not yet
an incompleteness instance for the small Hilbert calculus or for HoTT. Report:
`evaluations/CUBICAL-SYNTHETIC-INCOMPLETENESS-001/REPORT.md`.

`PF-CUBICAL-GODEL-PROOF-SEARCH-CLASSIFIER-001` then connects the natural-code
checker to that theorem's effective-system interface. It proves Boolean
semantic consistency for the exact K/S/MP calculus, checks one proof code per
stage on the proof and refutation sides, proves cross-stage determinism, and
constructs `HilbertSystem : FormalSystem Fml negF`. This removes the classifier
parameter for the small calculus while leaving universality and strong
separation open.

The accompanying author source is now independently qualified rather than
used only as a textual guide. The pinned
`uds-psl/coq-synthetic-incompleteness@cd7d849…` source builds
`FOL/Incompleteness/fol_incompleteness.vo` from two clean worktrees under Coq
8.15.2. Both builds have byte-identical stdout/stderr, 1,284 byte-identical
stable `.vo/.vos/.vok/.glob` artifacts, and the same final target. A separate
module loads five core constants and replays exactly. The signatures show that
`Q_incomplete` still explicitly requires Peirce, CTQ, a theory extending
`Qeq`, enumerability and consistency; `epf_mu_ctq` still requires universality
of the chosen μ-recursive interpreter. Report:
`evaluations/COQ-SYNTHETIC-INCOMPLETENESS-REPLAY-001/REPORT.md`.

The completeness audit distinguishes a closed research protocol and exhaustive
search inside frozen grammars from coverage of all HoTT terms or all reality
interpretations. Current verdict: the protocol is structurally complete and
several declared finite slices are relatively complete; there is no
candidate-to-grammar coverage theorem, exact HoTT incompleteness instance or
reality bridge. A total global paradox decider is not the target once the
candidate language can express general partial computation. Report:
`evaluations/NONTERMINATION-OVERVIEW-COMPLETENESS-AUDIT-001/REPORT.md`.

`PF-CUBICAL-CANDIDATE-COVERAGE-001` supplies the first formal certificate for
one of those relative-completeness claims. For each bound `n`, `allRaw n`
covers the exact bounded `never/now/laterR` language. Normalization into the
existing canonical `Delay Bool` model preserves convergence and all deadline
observations; reduction preserves task horizon and expected observation; every
reduced candidate appears in the canonical generated space. The five claims
have an indexed canonical run and exact replay. The package remains a small
deadline-consumer slice and does not supply a reduction from all HoTT paradox
candidates. Assessment:
`evaluations/CUBICAL-CANDIDATE-COVERAGE-001/REPORT.md`; exact claim scope:
`HoTT/formal/cubical-candidate-coverage/CLAIM.md`.

The project-level completeness owner now lives in the actual Codex project
directory rather than this contributor worktree:
`/Volumes/D/HoTT_AI_HANDOFF_20260911/.codex/research/hott/HOTT-PARADOX-PROGRAMMATIC-EXPLORATION-COMPLETENESS.md`.
Its five shards define the eight-axis search tensor, fourteen HoTT construct
families, fourteen excitation operators, A/B/Gödel/time and counter-model
families, six generator families, seven unknown-ingress routes and the P0–P9
acceptance roadmap. This worktree's nontermination plan is the dynamic execution
owner and points to that project-level plan; it does not duplicate the plan.

## Current verification snapshot

At the current worktree snapshot, based on branch HEAD `1aa1a6e…` and
not yet version-closed by a new commit:

- `selftest`: 94/94 PASS;
- `validate`: `VALID`, 0 errors;
- case revisions: 16 (three exact-hash legacy L1 revisions, L1 strict v2, four
  L3 cases, one case in each of L2/L4/L5/L6 and four L5 capability cases);
- runs: 39 (11 legacy plus 28 strict-v2 search/verify runs) and one registered
  interrupted legacy attempt;
- correspondence reviews: 18 (three legacy, fifteen strict v2);
- fourteen accepted strict native verification runs have exact byte replay; the
  finite-to-exact main proof has a separate exact failed-proof replay;
- M4 evolution-safe replay: `M4_LITE_REPLAY_V2_VALID` for 3 tasks;
- natural-consumer inventory replay: `NATURAL_CONSUMER_INVENTORY_VALID` for 7
  sources; semantic table: 42/42 E1–E6 cells present, 0 hits;
- L5 consumer audit replay: `L5_CONSUMER_AUDIT_VALID`; 5 systems / 9 artifacts /
  49 source anchors / 30 Q-cells, 0 qualified same-layer self-reliability hits;
- quotation/later bridge replay: `HOTT_QUOTATION_BRIDGE_VALID`; 6 systems / 12
  artifacts / 66 anchors / 10 exact-replay probes, H6 hits 0;
- forcing-ticks source inventory: 9 `force*` matching lines in 2 files across
  the complete 6-file pinned tree;
- tick-operational-gap replay: 3 systems / 18 artifacts / 4 source trees / 54
  anchors / 9 exact-replay probes; the equality search has one minimal
  three-edge witness and all three single-assumption ablations have zero
  witnesses;
- reflected-tick/termination revision 5: frozen formal snapshot 99 files /
  384,804 bytes / SHA `925765a8…1ad4`; 26 anchors; 10/10 exact native rerun;
  current run SHA `69db8953…829b`; historical revision 1 stale signal and revision 2/3
  failed refresh receipts retained;
- canonical F-011 worktree capture accepts primary and linked Git worktrees,
  records repository-contained cross-package include directories, and passes
  4/4 regression tests;
- one object-machine package, seven Gödel/synthetic-incompleteness packages and
  one bounded candidate-coverage package are indexed in
  `HoTT/CLAIM_EVIDENCE_MATRIX.md`; all nine verify with their exact
  frozen rows, and the synthetic/classifier runs retain their recorded exact
  stdout/stderr/exit replay;
- the six-test Gödel integrity regression suite covers all seven related
  packages and passes 6/6;
- the pinned author Coq source passes two clean full builds, stable-artifact
  exact comparison, an independent theorem-signature qualification and 4/4
  verifier regressions;
- the completeness audit records six distinct completeness quantifiers and
  prohibits promoting bounded grammar coverage into global HoTT coverage;
- the candidate-coverage package has 5 machine-checked claims, exact replay and
  a 4/4 integrity suite; its retained indexed-match diagnostic and resulting
  computation boundary are explicit.

This M4-lite/M3/L5/natural-consumer/tick-gap increment is local and uncommitted. The prior
strict-v2/L3 increment remains version-closed at `025938a…` plus documentation
closure `1aa1a6e…`. All `dev-notes/` remain outside the implementation change
set. No merge, tag, push or main-line checkpoint has been performed.

## Layout

```text
machine-overview/
  mo.py                       CLI launcher
  m4_eval.py                  frozen-engine same-budget comparison and replay
  m4_replay_closure.py        evolution-safe M4 adapter snapshots and replay
  freeze_breadth.py           M3 adapter/configuration freeze manager
  freeze_l5.py                L5 adapter/source/role freeze manager
  l5_consumer_audit.py        Q1-Q6 fixed-source audit and replay
  hott_quotation_bridge.py    TC/quotation/later source and native bridge replay
  tick_irrelevance_gap.py     exact forcing-tick reduction/Path gap evaluator
  force_consumer_inventory.py fixed forcing-ticks force-use inventory
  natural_consumer_audit.py  pinned-source keyword inventory and replay
  coq_synthetic_incompleteness.py pinned source/build/qualification verifier
  HOTT-NONTERMINATION-MACHINE-OVERVIEW-PLAN.md living completion/Gödel plan
  literature/                 source index and byte-preserved research inputs
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
  evaluations/                engine freezes, M4 results and source/interpretation audits
  formal/                     pinned support/control modules
  legacy/                     exact-hash allowlist for pre-v2 evidence
  generated-index/            rebuildable query projection
  tests/                      unit, regression and fault-injection tests

HoTT/formal/ contains formal claim sources; HoTT/verification/runs/ contains
canonical kernel receipts; HoTT/CLAIM_EVIDENCE_MATRIX.md is their claim index.
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

python3 machine-overview/m4_replay_closure.py verify \
  --run machine-overview/evaluations/M4-LITE-L3-001/runs/20260913-M4-LITE-L3-REPLAY-V2/RUN.json
python3 machine-overview/natural_consumer_audit.py verify \
  --inventory machine-overview/evaluations/L3-NATURAL-CONSUMER-AUDIT-001/KEYWORD-INVENTORY.json
python3 machine-overview/l5_consumer_audit.py verify \
  --run machine-overview/evaluations/L5-CONSUMER-QUALIFICATION-001/runs/20260913-L5-CONSUMER-AUDIT-001/RUN.json
python3 machine-overview/hott_quotation_bridge.py verify \
  --run machine-overview/evaluations/HOTT-QUOTATION-BRIDGE-001/runs/20260913-HOTT-QUOTATION-BRIDGE-001/RUN.json \
  --rerun
python3 machine-overview/force_consumer_inventory.py verify \
  --inventory machine-overview/evaluations/HOTT-QUOTATION-BRIDGE-001/FORCE-CONSUMER-INVENTORY.json
python3 machine-overview/tick_irrelevance_gap.py verify \
  --run machine-overview/evaluations/TICK-IRRELEVANCE-OPERATIONAL-GAP-001/runs/20260913-TICK-IRRELEVANCE-OPERATIONAL-GAP-001/RUN.json \
  --rerun

python3 scripts/audit/verify_formal_proof_run.py \
  --run-dir HoTT/verification/runs/20260914-CUBICAL-GODEL-NAT-PROOF-CODE-001 \
  --rerun
python3 -m unittest machine-overview/tests/test_cubical_godel_infrastructure.py
```

Create new run IDs for every new experiment. Do not overwrite immutable case,
run, review or target-freeze records.

## What remains

- **M2 is partial.** The current symbolic backend is a small typed Horn proof
  grammar plus four controlled native L3 renderers. It does not yet synthesize general
  dependent terms, universe constraints, arbitrary HIT eliminators or higher
  coherences.
- **M3 breadth is complete; depth is partial.** L1–L6 each have an executable
  case chain. L2/L4 are existing-claim calibrations and L6 reuses a known
  mechanism. L5 now separates four capabilities and audits five real source
  systems, but its strongest Löb/self-certification result is still conditional
  because the frozen set contains no Q1–Q6-qualified HoTT consumer.
- **M4-lite is complete; M4 is not.** The three-task same-budget comparison is
  replayable and exercises native feedback, but task roles and LLM rule subsets
  were designed by the same AI. There is no independent holdout, sufficiently
  large denominator, repeated timing distribution or defensible general
  performance estimate.
- **M5 is partial.** Canonical Agda capture now qualifies linked worktrees and
  the object-machine/Gödel/synthetic/candidate-coverage packages are in the formal source/run/claim-matrix
  chain. Main-line STATE, direction/panorama projections, checkpoint receipts
  and Git version closure have not been applied from this isolated branch.
- **Completeness is relative to an explicit denominator.** Strict-v2 closes the
  evidence lifecycle and registered complete runs exhaust their frozen
  grammars. No theorem currently maps every relevant HoTT candidate to those
  grammars while preserving the task and reality correspondence; no global
  absence claim follows from a search miss.
- **The full exploration plan is project-level.** The project root AGENTS and
  two HoTT Skills load the canonical five-shard plan from
  `/Volumes/D/HoTT_AI_HANDOFF_20260911/.codex/research/hott/`; this contributor
  branch retains only implementation/evidence and its dynamic execution plan.
- A frozen seven-primary-source audit found no E1–E6 natural consumer. This
  closes that bounded set only; broader literature and later versions remain
  outside its denominator. The L3 result remains a checked model-relative
  obstruction and is not upgraded to a HoTT defect.
- The HoTT quotation/later bridge locates an exact time-erasure collapse, but
  every fixed source preserves the host/tick/clock qualification and H6 has no
  consumer. The exact historical forcing-ticks checker was built and run;
  replaying full `Clocked.Lift` against its matching historical Cubical
  dependency remains open.
- `cvc5`, Alloy and egg remain uninstalled; no current bottleneck requires them.

## Audit trail

- First audit and F1–F7 response:
  `/Volumes/D/HoTT独立答复/20260913-M1自动化统观实现审计.md` and
  `AUDIT-RESPONSE-20260913.md`.
- Second audit:
  `/Volumes/D/HoTT独立答复/20260913-M1自动化统观修复复审.md`.
- Strict-v2 response and L3 result: `AUDIT-RESPONSE-V2-20260913.md`.
- M4-lite report: `evaluations/M4-LITE-L3-001/REPORT.md`.
- Natural-consumer audit:
  `evaluations/L3-NATURAL-CONSUMER-AUDIT-001/ASSESSMENT.md`.
- M3 breadth report: `evaluations/M3-BREADTH-001/REPORT.md`.
- L5 consumer-qualification report:
  `evaluations/L5-CONSUMER-QUALIFICATION-001/REPORT.md`.
- HoTT quotation/later bridge:
  `evaluations/HOTT-QUOTATION-BRIDGE-001/REPORT.md`.
- Nontermination/Gödel route:
  `HOTT-NONTERMINATION-MACHINE-OVERVIEW-PLAN.md`.
- Object-machine R1 report:
  `evaluations/CUBICAL-MACHINE-HALTING-001/REPORT.md`.
- Natural-number proof-predicate infrastructure:
  `evaluations/CUBICAL-GODEL-PROOF-CHECKER-001/REPORT.md`.
- Current handoff: `HANDOFF-20260913.md`.
