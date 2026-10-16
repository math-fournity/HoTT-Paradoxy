# P-DAG-HOTT-REPLAY-002：修复终态收据后的无泄漏 HoTT 重放 NodeCard

> **身份：** `RETRY_AFTER_OUTPUT_CAPTURE_FAILURE / PRELAUNCH_NODECARD / NOT_A_THEORY_RESULT`。
>
> **parent:** `P-DAG-HOTT-REPLAY-001` only. This retry is authorized because it changes output capture and deadline; it is not a repeated vote on the same theory question.

## Inherited frozen content

The source pack, no-leak exclusions, task scope and agent prompt are byte-for-byte the same as [H-001](20261002-P-DAG-HOTT-REPLAY-001-NODECARD.md). The worker still receives only the neutral universe/univalence/h-level excerpts and cannot access the repository, web, prior answers, `QuestioningDelay`, formal proof assets or other agents.

## Changed execution contract

```text
runner: fresh Codex CLI --no-daemon --ephemeral
model/effort request: gpt-5.6-terra / max
sandbox/approval: read-only / never
output capture: --output-last-message /tmp/hott-p-dag-hott-replay-002-final.md
Master polling: exact output file only; console/planning text remains non-evidence
deadline: 90 seconds wall-clock
failure: TIMEOUT_NO_TERMINAL_OUTPUT if final path is absent; no source/theory verdict
success: final path has a public E0–E7 MatchTrace and exact marker of scope
```

The file name is new and did not exist at launch. This NodeCard does not authorize a third identical retry: a further attempt needs a different runner or external state change.
