# Archived interrupted GEN-001 verify run (20260916-VERIFY-GEN001-WITNESS-RECOVERY-041)

## Why archived
The first process executing run `20260916-VERIFY-GEN001-WITNESS-RECOVERY-041` (witness WV-0041)
was externally terminated during the kernel phase. The engine rolled the interrupted attempt over
and a second attempt of the same run id completed successfully with four kernel receipts.

The completed receipt honestly records `target_freeze.status = "REUSED"` because the target-freeze
ledger entry for this candidate hash was created by the killed first attempt (with
`first_verify_run` = this run id). The workspace validator expects `"FROZEN"` whenever
`first_verify_run == run_id`, which does not account for the same run id re-freezing after a
roll-over. The mismatch is a validator seam, not receipt tampering.

## Resolution
Witness WV-0041 (identical candidate AST, hash 36be2871...) was re-verified under the fresh run id
`20260916-VERIFY-GEN001-WITNESS-RECOVERY-041B`, which produces a fully consistent receipt
(`REUSED`, matching the ledger). 041B is the receipt of record for that witness.

## What is preserved here
- `20260916-VERIFY-GEN001-WITNESS-RECOVERY-041/` — the completed-but-seamed receipt
- `20260916-VERIFY-GEN001-WITNESS-RECOVERY-041.attempt-1-interrupted/` — the externally killed attempt

Both are unmodified. They are moved out of the validated `runs/` tree so that workspace validation
is clean; they remain readable for audit.
