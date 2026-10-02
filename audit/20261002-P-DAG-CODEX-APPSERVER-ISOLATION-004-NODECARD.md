# P-DAG-CODEX-APPSERVER-ISOLATION-004：修正 prompt-input 判据后的零理论健康 NodeCard

> **身份：** `PRELAUNCH_NODECARD / CODEX_APP_SERVER_FACADE / CONTROLLED_AUTH_BORROWING / ZERO_THEORY_ONLY`。

## Parent correction

`ISOLATION-003` stopped before auth borrowing because its prompt-input gate treated every visible `~/.codex` string and the local word `P-DAG` as an answer leak. Direct inspection showed those occurrences were a denied-path/Skill-root list and this NodeCard's own local contract; the actual HoTT project path and known answer markers were absent. The gate now rejects project-specific material rather than harmless system denial metadata.

## Frozen contract

```text
node_id: P-DAG-CODEX-APPSERVER-ISOLATION-004
parent: ISOLATION-003 pre-auth false-positive repair
runner wrapper SHA-256: d61c1672bc361388b1e8b78716bc2c1d89bbe768df00223a31a4b4d15ae68885
method repo: /Users/aurolafly/codex-worktrees/breadth-terms-3.12.1 (clean at launch)
private root: /Users/aurolafly/.codex-experiments/p-dag-appserver-isolation-20261002
run_id: p-dag-appserver-health-004
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

The preflight must show no HoTT project root, `QuestioningDelay`, `ZFC_Q_LOCATED`, `Power Set`, or P-pattern Skill name in model-visible input, while allowing system metadata that merely declares a path inaccessible. The App Server response must echo Terra, max, the isolated cwd, `governance-regression-fresh`, and `never`; the completed turn must return exactly the marker without command, file-change, or permission-request events.

All raw wire/stderr/receipt material remains in the private experiment root. A failure remains a runner boundary result only.
