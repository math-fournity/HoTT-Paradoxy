# /checkpoint-dry

Prepare and inspect a governance checkpoint **without applying it**. This command is intentionally a dry-run
wrapper around the repository's one runtime; it does not edit STATE, HEAD, session evidence, or checkpoint files.

1. Confirm the task is authorized for checkpoint work and that its tier is `T3-mutation`.
2. Obtain a fresh governance-plan snapshot and prepare a complete `cognition-checkpoint/v1` payload using the
   repository's documented session bundle and expected file hashes.
3. Run the canonical command without `--apply`:

   ```bash
   python3 -B .codex/tools/cognition_runtime.py checkpoint \
     --snapshot <plan-snapshot> --payload <checkpoint-payload.json>
   ```

4. Treat `DRY_RUN` as a payload validation result only. An actual state transition requires explicit user-authorized
   `--apply`, an atomic runtime receipt, and `result.json.status=CHECKPOINT_COMMITTED`.

Do not replace the canonical runtime with shell edits, hand-written HEAD hashes, or a second checkpoint format.
