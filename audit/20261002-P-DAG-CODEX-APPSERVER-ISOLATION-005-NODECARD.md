# P-DAG-CODEX-APPSERVER-ISOLATION-005：去除 ephemeral `thread/read` 的零理论健康 NodeCard

> **身份：** `PRELAUNCH_NODECARD / CODEX_APP_SERVER_FACADE / CONTROLLED_AUTH_BORROWING / ZERO_THEORY_ONLY`。

## Parent correction

`ISOLATION-004` passed the model-visible-input gate and reached the App Server, but its final inspection requested
`thread/read(includeTurns=true)` for an `ephemeral` thread. The current App Server rejected that request with
`-32600: ephemeral threads do not support includeTurns`. The health contract already obtains the agent text from the
raw message delta and the terminal event, so this extra post-turn read was neither required for the stated oracle nor
compatible with the chosen ephemeral lifecycle. The wrapper now retains only `thread/start`, `turn/start`, raw wire,
and terminal evidence.

## Frozen contract

```text
node_id: P-DAG-CODEX-APPSERVER-ISOLATION-005
parent: ISOLATION-004 API compatibility correction
runner wrapper SHA-256: d01af316bef82e946a5d35dddb525f69aedd33bf1239aa9ea0ee0b52dd448627
method repo: /Users/aurolafly/codex-worktrees/breadth-terms-3.12.1 (clean at launch)
private root: /Users/aurolafly/.codex-experiments/p-dag-appserver-isolation-20261002
run_id: p-dag-appserver-health-005
host: codex app-server --listen stdio:// (Codex app-server façade, not native ACP)
thread start: separate text-only cwd; gpt-5.6-terra; fallback=false;
              governance-regression-fresh permissions; approvalPolicy=never; ephemeral=true
turn start: gpt-5.6-terra / max / default
auth: existing R-035 controlled borrowing primitive, pre/post sandbox gates, no content/hash/size receipt,
      exact temporary target removed on completion or failure
model input: only P_DAG_APPSERVER_ISOLATION_HEALTH_PASS marker
timeout: 90 seconds + exact turn/interrupt fallback
```

## Acceptance

The preflight must show no HoTT project root, `QuestioningDelay`, `ZFC_Q_LOCATED`, `Power Set`, or P-pattern Skill
name in model-visible input, while allowing system metadata that merely declares a path inaccessible. The App Server
response must echo Terra, max, the isolated cwd, `governance-regression-fresh`, and `never`; the completed turn must
return exactly the marker without command, file-change, or permission-request events. This node cannot establish the
validity of any theory-level inference; it only qualifies one isolated runner lane.

All raw wire/stderr/receipt material remains in the private experiment root. A failure remains a runner boundary
result only.
