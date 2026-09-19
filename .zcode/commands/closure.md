# /closure

Use the repository's single governance tree; this command does not create a second policy or state store.

1. State the task tier (`T0-lite`, `T1-standard`, `T2-research`, or `T3-mutation`) and why it applies.
2. Read the tier route in root `AGENTS.md`, then the corresponding `LOAD_SET.json` and `PROTOCOL.md` contract.
3. Run the canonical read-only plan from the repository root:

   ```bash
   python3 -B .codex/tools/cognition_runtime.py plan --profile governance
   ```

4. Record the returned snapshot, relevant file hashes, host, model, and tier in the session evidence required by
   the selected tier. If the requested tier requires research hydration, use the documented profile and stable
   record route instead of guessing from historical notes.
5. If the plan fails, a required document is incomplete, or the tier must increase, stop before mutation and
   follow the root `AGENTS.md` / `PROTOCOL.md` failure route.

The plan certifies file selection and byte identity only. It does not certify model understanding, a mathematical
claim, or a checkpoint.
