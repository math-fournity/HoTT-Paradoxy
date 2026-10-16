# P-DAG-HOTT-DISCOVERY-009：模型采样前的 Prompt 包装失败收据

> **身份：** `PREAUTH_PREFLIGHT_FAILURE / NO_AGENT_OUTPUT / NO_THEORY_VERDICT`。

The H-009 runner reached `debug prompt-input` before authentication borrowing or App Server startup. Its input gate
failed with return code 0 because the Markdown audit header itself named the forbidden source/result identifiers
`QuestioningDelay`, `PedometerSemantics`, `universeHasNoLevel`, and `QIsNever`. These words were not leaked from the
project into an otherwise clean worker environment; they were accidentally transmitted because the runner sent the
entire Markdown file rather than just its fenced `text` payload.

```text
prompt-input gate: FAIL
auth copied: no
model sampled: no
App Server started: no
agent output: none
theory / P verdict: none
```

Repair: the wrapper now extracts exactly one fenced `text` payload before prompt compilation. The fixed payload is
2425 bytes, SHA-256 `9eaf50c72bb9d42b4b9a57c07f50ed36c15fcd29776814ffdbb346d190dfcdec`, and excludes all four markers.
H-010 is a new run identity using that repaired packaging; H-009 is retained as an input-boundary control, not retried
under the same run ID.
