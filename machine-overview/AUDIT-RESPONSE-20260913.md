# Response to the external M1 audit (2026-09-13)

> Historical scope: this document answers the first F1–F7 audit and preserves
> that acceptance run. The current strict-v2 response to the later repair
> re-audit is `AUDIT-RESPONSE-V2-20260913.md`; current counts and commands are in
> `README.md`.

Status: `F1-F7 FIXED / POST-FIX ACCEPTANCE RE-RUN / WORKTREE-LOCAL`.

The audit object was worktree `/Volumes/D/HoTT-machine-overview` at
`e4ab45bcb6931861fa57cfa9f8ac8de2af12acce`; the audit verdict was
`REQUEST_CHANGES` with seven findings (F1–F7). This document records, for each
finding: the independently reproduced failure, the fix in this worktree, the
regression test, and the evidence.

## Independent reproduction before the fix

Every finding was reproduced in this worktree by the current main agent before
any change; the numbers matched the audit.

| Finding | Reproduction result (pre-fix) |
|---|---|
| F1 | `inspect-profile` returned `PROFILE_QUALIFIED` with `sources[0].status = FAIL` and `failures = []` after appending one comment to the model source |
| F2 | (a) after changing the frozen grammar, `search` recorded grammar sha `77b04fc6…` while reading bytes with sha `2b9d1b0e…` (252 checks); (b) a rev-2 deadline witness was accepted under a rev-3 case with the kernel call stubbed — status `NATIVE_CHECKED_CALIBRATION_INSTANCE` |
| F3 | deleting `kernel/verify/stdout.txt` from an accepted verify run still produced `validate = VALID` with 7 runs |
| F4 | committed review `RV-…-WV-0002.json` described a race-only value mismatch as "business continuation → divergence" and fixed `task_preservation = PRESERVED_AT_MODEL_LEVEL` |
| F5 | with `deadline_horizons = [2]`, reduction produced 6 witnesses using `deadline 0` |
| F6 | `--max-checks 1` produced `exit_reason = BUDGET_REACHED`, `truncated = true` and `complete_within_declared_grammar = true` |
| F7 | a blocked cache path raised `FileExistsError`, left `generated/` without `RUN.json`, `validate` stayed `VALID`, and the same run id could not be retried |

## Fixes

### F1 — source pins are qualification failures

- `profile.py`: `qualification_verdict()` aggregates every FAIL, including
  per-source hash mismatches; missing `sha256` pins are now an explicit failure
  (`SHA256_PIN_REQUIRED`); the profile also checks that `library_registry`
  matches the toolchain declaration.
- The trusted support module `machine-overview/formal/MVSupport.agda` is pinned
  in the new `profiles/l1-partiality-v1.json` (`support_sources`).
- Regression: `test_source_hash_mismatch_fails_qualification`,
  `test_verdict_includes_source_failures`.

### F2 — every consumer re-verifies the frozen inputs and evidence identity

- `case.load_case_inputs()` re-hashes profile/task/grammar against the case
  revision and fails closed (`CASE_INPUT_HASH_MISMATCH:<key>`); `search` uses the
  verified grammar bytes and records the actual content hash.
- `verify.assert_witness_binding()` refuses witnesses whose search run belongs to
  another case revision (`WITNESS_FROM_DIFFERENT_CASE_REVISION`), another
  grammar/task (`SEARCH_RUN_INPUT_MISMATCH`) or outside the declared grammar
  (`WITNESS_OUTSIDE_DECLARED_GRAMMAR`). Verify receipts now record
  `source_search_run` (run id + sha256), `candidate_ast_sha256`,
  `case_sha256`, `case_identity_sha256`; witnesses carry `ast_sha256`.
- A persistent target freeze ledger
  (`cases/<case-id>/target-freeze-<revision>.json`) binds
  `(witness AST) → target_text_hash`; a mismatch raises `TARGET_CHANGED`.
- Regression: `test_case_input_hash_mismatch_is_rejected`,
  `test_cross_revision_witness_is_rejected`,
  `test_witness_outside_grammar_is_rejected`; CLI demo: cross-revision verify →
  exit 2 `WITNESS_FROM_DIFFERENT_CASE_REVISION`, no run directory created;
  stale-grammar search → exit 2 `CASE_INPUT_HASH_MISMATCH:grammar`.

### F3 — validate re-derives validity from kernel evidence

- `case.validate_workspace()` now checks: case reference hashes; profile source
  pins; search input hashes and witness membership/AST hashes; verify bindings
  (search run hash, case identity, candidate AST); generated-source hashes;
  `Target.agda` vs `target_text_hash`; target-freeze ledger agreement; every
  kernel artifact (`stdout.txt`, `stderr.txt`, `command.json`,
  `environment.txt`) with recorded byte counts and SHA-256; kernel
  status/expectation consistency; and the overall run-status consistency.
- Pre-audit receipts are kept byte-identical but must carry an explicit
  `LEGACY.json` attestation; they are then validated as far as their schema
  allows and listed under `legacy_runs`.
- Regression: `test_missing_kernel_output_is_invalid`; CLI demo on a temp copy →
  exit 1 with `KERNEL_ARTIFACT_MISSING`.

### F4 — correspondence is derived from the witness structure

- `correspondence.mechanism_facts()` distinguishes
  `deadline_observation`, `value_mismatch`, `completion_divergence` with/without
  the declared business continuation and produces the mechanism text and
  compensation class from the actual ops.
- `task_preservation` is now computed from five explicit checks (grammar
  membership, case↔search binding, declared observation kind, declared consumer
  present, compensation classified) instead of being asserted.
- The deadline compensation class is `READS_DECLARED_REPRESENTATION` with an
  explicit statement that the round index is part of the constructor and that no
  quotient-level recovery is claimed.
- Review ids now include case revision, search run and witness AST prefix; the
  three pre-audit reviews were moved to `reviews/.superseded/` (byte-identical)
  with a README explaining the F4 error.
- Regression: `test_value_mismatch_mechanism_has_no_business_continuation`,
  `test_completion_mechanism_mentions_declared_continuation`.

### F5 — reduction stays inside the declared grammar

- `search.within_grammar_witness()` checks index bounds, declared continuation
  maps, declared deadline parameters and context depth; every shrink in
  `reduce_witness()` must pass it, as must every emitted witness
  (`grammar_membership` field). A witness set that leaves the grammar raises
  `REDUCTION_LEFT_DECLARED_GRAMMAR`.
- Regression: `test_sparse_deadline_parameters_are_respected` (declared `[2]` →
  zero escaped witnesses).

### F6 — completeness, budgets and capture limits are separate facts

- Statistics now distinguish `contexts_examined`/`contexts`,
  `pair_context_checks`/`checks_planned`,
  `checks_budget_exhausted`, `context_budget_exhausted`,
  `witness_capture_truncated` and `truncated`. `complete_within_declared_grammar`
  requires full traversal, no budget stop and no capture truncation; the budget
  counter no longer counts the check that exceeded the budget.
- Regression: `test_budget_reached_never_claims_completeness`.

### F7 — attempts, timeouts, cancellation and recovery

- Every run (search and verify) writes `ATTEMPT.json` with status
  `RUNNING` before work and upgrades it to `COMPLETED` or `INTERRUPTED`
  (with the exception text). `prepare_run_dir()` rolls a recorded interrupted
  attempt over to `<run-id>.attempt-<k>-interrupted` and starts a fresh attempt,
  so the same run id can be retried without deleting the failure.
- `run_kernel()` runs the kernel in its own process group with an internal
  timeout (default 900 s, `--timeout-seconds`), terminates the group with
  SIGTERM then SIGKILL, records `KERNEL_TIMEOUT` plus the partial output.
- The negative control must show a type-error diagnostic in the `Falsify`
  module (`EXPECTED_TYPE_REJECTION`); infrastructure markers and exit 154 are
  classified as `KERNEL_INFRASTRUCTURE_ERROR`, other non-zero exits as
  `KERNEL_REJECTED_WITH_UNEXPECTED_DIAGNOSTIC`.
- Replay classification distinguishes
  `EXACT_EXIT_STDOUT_STDERR_MATCH`,
  `EXIT_STDERR_MATCH_WITH_CACHE_LOG_DIFFERENCE` (only Agda
  `Checking <Module> (<path>).` lines differ, e.g. cold vs warm interface cache)
  and hard mismatches; a cache-log difference no longer turns an accepted kernel
  result into `NATIVE_CHECK_FAILED`.
- `validate` reports `interrupted_attempts`; a run directory without any receipt
  is `INVALID` (`RUN_DIRECTORY_WITHOUT_RECEIPT`).
- Regression: `test_interrupted_attempt_is_rolled_over`,
  `test_recorded_interruption_is_visible_and_valid`,
  `test_unrecorded_partial_directory_is_invalid`,
  `test_kernel_timeout_is_recorded_and_killed`,
  `test_replay_classification_distinguishes_cache_logs`,
  `test_negative_control_diagnostic_classification`.

## Post-fix acceptance re-run

| Item | Result |
|---|---|
| `selftest` | 29/29 PASS |
| Case | revision 3 (profile `L1-PARTIALITY-RACE-DEADLINE-v1`, grammar `l1-v1`) |
| Search `20260913-SEARCH-L1-003` | 7 atoms, 399 contexts, 4,788/4,788 checks, 916 separations, 50 witnesses (deadline 14 / value 28 / completion 8), `complete_within_declared_grammar = true`, benchmark `PRESENT` |
| Verify deadline `20260913-VERIFY-L1-POSTFIX-DEADLINE-001` (WV-0001) | `NATIVE_CHECKED_CALIBRATION_INSTANCE`; kernels 0/0/42(-expected)/0; replay `EXACT_EXIT_STDOUT_STDERR_MATCH` |
| Verify value `20260913-VERIFY-L1-POSTFIX-VALUE-001` (WV-0002) | same shape; negative control `EXPECTED_TYPE_REJECTION` |
| Verify completion `20260913-VERIFY-L1-POSTFIX-COMPLETION-001` (WV-0013) | same shape |
| Cross-revision verify (rev 2 case, rev 3 witness) | rejected: `WITNESS_FROM_DIFFERENT_CASE_REVISION`, no run directory |
| Stale grammar (temp fixture) | rejected: `CASE_INPUT_HASH_MISMATCH:grammar` |
| Missing kernel output (temp fixture) | `validate` exit 1 with `KERNEL_ARTIFACT_MISSING` |
| Postulate proof | rejected: `CANDIDATE_FORBIDDEN_DECLARATION`, no run directory |
| `validate` (real workspace) | `VALID`, 0 errors, 11 runs, 7 legacy-attested runs, 1 recorded interrupted attempt |

The first attempt at search run `-003` failed because of a same-id directory
bug (`run_search` tried to recreate the directory owned by `begin_attempt`);
the attempt is preserved as `runs/20260913-SEARCH-L1-003.attempt-1-interrupted`
and the fix was to let the caller own directory exclusivity.

## Remaining scope (not part of this fix)

- M2 (symbolic / higher-path search), M3 (six-line coverage), M4 (held-out
  evaluation) and M5 (main-line integration) are still not implemented.
- The `capture_agda_proof_run.py` `.git`-directory requirement and the two
  verifiers that need gitignored nested assets remain worktree-portability gaps
  for M5.
- The cold/warm cache replay difference is now classified and recorded, but the
  cache state itself is not yet declared in the profile (future improvement).
