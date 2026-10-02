# P-DAG-RUNNER-HEALTH-001：独立 HoTT 重放前的 Terra/Max 运行健康检查

> **身份：** `PRELAUNCH_NODECARD / INFRASTRUCTURE_HEALTH_CHECK / NOT_A_THEORY_OR_SOURCE_RESULT`。
>
> **目的：** 在任何新的 HoTT replay 或 ZFC source node 前，检查 fresh Codex CLI 是否能实际启动并交付一个最小终态。此卡不携带理论、来源、项目答案或数学任务。

```text
node_id: P-DAG-RUNNER-HEALTH-001
runner: fresh Codex CLI --ephemeral --no-daemon
model/effort request: gpt-5.6-terra / max
sandbox/approval: read-only / never
access: no network, no local project, no Git, no files, no delegation
prompt: return exactly RUNNER_HEALTH_PASS and one public sentence stating no theory was analyzed
acceptance: terminal output includes exact marker; CLI banner returns requested profile
deadline: 45 seconds
failure: RUNNER_CONNECTION_FAILURE / NO_AGENT_OUTPUT or TIMEOUT_NO_TERMINAL_OUTPUT
successor: only PASS permits a pre-registered no-answer-leak HoTT replay NodeCard
```

No health result implies anything about P1/P2/P3, HoTT, ZFC, or a source. It only qualifies the execution surface for the next bounded node.
