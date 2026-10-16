# P-DAG-CODEX-APPSERVER-ISOLATION-003：受控认证的零理论 App Server 健康 NodeCard

> **身份：** `PRELAUNCH_NODECARD / CODEX_APP_SERVER_FACADE / ZERO_THEORY_ISOLATION_HEALTH / NOT_A_THEORY_NODE`。

## User and method authority

The user directed the Master to use the separate-directory Codex App Server technique established in `/Users/aurolafly/shuxuedashi-analysis-system`. Inspection found that project uses the analogous OpenCode ACP pattern (`--cwd` + session cwd + model/effort echo + raw notification receipts), while the current shared Codex governance worktree provides the Codex-specific App Server implementation and R-035 controlled auth borrowing gate.

This node uses that existing method with the user's active P-DAG authorization. It does not disclose, print, hash, stage, commit, or retain credential contents.

## Frozen contract

```text
node_id: P-DAG-CODEX-APPSERVER-ISOLATION-003
parent: HOTT-DISCOVERY-007 access leak + RUNNER-ISOLATION-002 auth failure
host: Codex app-server façade, explicitly not native ACP
method repo: /Users/aurolafly/codex-worktrees/breadth-terms-3.12.1 (clean at launch)
shared primitives: tools/governance_regression.py + tools/agent_session_broker.py
private root: /Users/aurolafly/.codex-experiments/p-dag-appserver-isolation-20261002
run_id: p-dag-appserver-health-003
model/effort: gpt-5.6-terra / max
model fallback: false
thread permissions: governance-regression-fresh
approval policy: never; server requests deny
worker cwd: generated text-only probe workspace inside the isolated experiment root
CODEX_HOME / SQLite: run-scoped generated locations only
source payload: none; user turn is exact marker P_DAG_APPSERVER_ISOLATION_HEALTH_PASS
timeout: 90 seconds + exact turn/interrupt fallback
```

## Required gates, in order

1. clean method worktree and current runtime auth shape;
2. generated no-auth `CODEX_HOME` and dummy/current-auth denial probes;
3. pre-copy clean gate; model-visible `debug prompt-input` check that P-project paths and known answer markers are absent;
4. R-035 controlled temporary auth copy, login status and post-copy borrowed-auth denial probes;
5. App Server `initialize → initialized → thread/start → turn/start`, with exact model, reasoning effort, cwd, named permission profile and approval-policy echo;
6. exact marker output, zero command/file-change/permission-request count, private raw wire/stderr receipt;
7. remove borrowed auth before emitting any safe summary.

Any failed gate is a runner result only. It cannot support an HoTT, ZFC, Pattern-P, model-capability, or no-cheat conclusion.
