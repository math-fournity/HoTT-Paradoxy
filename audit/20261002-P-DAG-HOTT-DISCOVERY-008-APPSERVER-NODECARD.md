# P-DAG-HOTT-DISCOVERY-008：隔离 App Server 上的 D-L6b HoTT 盲态重放 NodeCard

> **身份：** `PRELAUNCH_NODECARD / BLIND_SCHEMA_REPLAY / D_L6B_REGRESSION / NOT_A_HOTT_RESULT`。

## Parent correction

`HOTT-DISCOVERY-007` 不是 D-L6b 的结果：其 fresh CLI 在输出前已经出现 global instruction injection 和
workspace/tool discovery，因此被终止并标为 `ACCESS_LEAK_SUSPECTED`。其后 empty-home node 在模型采样前
`401`，没有测试到隔离行为。`P-DAG-CODEX-APPSERVER-ISOLATION-005` 已在新的 run-scoped App Server 环境中通过
zero-material health：model/effort/cwd/approval/permission echo、prompt-input、pre/post auth gates 都合格，且
无 command/file/approval event。本节点首次把**原 H-007 的冻结 D-L6b Prompt**放入该已资格化的运行链。

## Frozen contract

```text
node_id: P-DAG-HOTT-DISCOVERY-008
parent: HOTT-DISCOVERY-007 access-leak failure + APPSERVER-ISOLATION-005 health pass
runner wrapper: scripts/pattern_p_appserver_blind_discovery.py
wrapper SHA-256: a09194bd03b7c177d134e013a14db0458c597d46047622b76f31abacf5eecd7e
governance control: governance-v3.26.0 BLIND_EXTERNAL_CODEX_WORKER_ISOLATION_V1
method repo: /Users/aurolafly/codex-worktrees/breadth-terms-3.12.1 (must be clean at launch)
private root: /Users/aurolafly/.codex-experiments/p-dag-appserver-isolation-20261002
run_id: p-dag-hott-discovery-008
host: codex app-server --listen stdio:// (app-server façade, not native ACP)
worker home/state: run-scoped HOME / CODEX_HOME / CODEX_SQLITE_HOME and text-only cwd
model/effort: gpt-5.6-terra / max; fallback=false
permission/approval: governance-regression-fresh / never; network default-deny
prompt source: audit/20261002-P-DAG-HOTT-DISCOVERY-007-DL6B-PROMPT.md
prompt SHA-256: a2f6b018d0f547d88b8f886c0b6010109c33598b20cce2017dc169444dc2c918
prompt bytes: 2592
authentication: R-035 controlled temporary local borrowing; pre/post deny gates; independent 0600 copy;
                no content/hash/size public receipt; finally remove
time limit: 180 seconds + one exact interrupt and 20-second terminal grace
```

## Blindness and output contract

The prompt is transmitted only as the App Server turn text; it is not stored in the worker workspace. Before model
sampling, `debug prompt-input` must contain the isolated worker contract and the frozen task profile while excluding
the HoTT project root, `QuestioningDelay`, `ZFC_Q_LOCATED`, `Power Set`, the Pattern-P Skill name and the known
`ua : (A ≃ B)` answer string. The worker may not use files, web, commands, Git, configuration inspection, delegation
or artifact creation.

Its only public result is the D0–D5 `DiscoveryTrace`, at most 350 English words, containing exactly one
`MODEL_RECALL_SITE_CANDIDATE` or `NO_MODEL_RECALL_CANDIDATE / DIRECT_PAYMENT_ONLY`. Full prompt-input, wire,
stderr, final text and home receipt remain private. The public Master audit can quote the final D0–D5 trace because
the prompt requests it as public evidence, while keeping private environment data excluded.

## Stop and interpretation rule

Any input leak, command/file-change/approval event, missing exact echo, auth-gate failure, timeout without terminal
output, or output contract failure is `RUNNER_ISOLATION_NOT_QUALIFIED` or `TIMEOUT_NO_TERMINAL_OUTPUT`; the text
will not be used as a discovery result. A clean terminal trace remains only a `MODEL_RECALL_SITE_CANDIDATE` or
negative discovery observation. It creates no source fact, P2/P3 mapping, natural consumer, theorem, HoTT replay
pass, ZFC result or mathematical conclusion. A later source-validation NodeCard is required before any P1 candidate
is promoted.
