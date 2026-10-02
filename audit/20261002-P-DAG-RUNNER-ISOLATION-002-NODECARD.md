# P-DAG-RUNNER-ISOLATION-002：空 CODEX_HOME 的 prompt-only 健康 NodeCard

> **身份：** `PRELAUNCH_NODECARD / ZERO_THEORY_RUNNER_HEALTH / NOT_A_THEORY_NODE`。

## Contract

```text
node_id: P-DAG-RUNNER-ISOLATION-002
parent: P-DAG-BLIND-RUNNER-ISOLATION-001
purpose: test whether an empty CODEX_HOME suppresses global AGENTS injection
runner: fresh Codex CLI --ephemeral
environment: CODEX_HOME=/tmp/hott-p-dag-codex-home-002 (created empty)
auth store: cli_auth_credentials_store="keyring" only; no credential file is copied or read into repo
model/effort request: gpt-5.6-terra / max
sandbox/approval: read-only / never
access profile: ZERO_THEORY_NO_TOOLS
working root: /tmp/hott-p-dag-runner-isolation-002-scratch
prompt: audit/20261002-P-DAG-RUNNER-ISOLATION-002-PROMPT.md
prompt SHA-256: 9f97f325a53001ee7da85e9bbd2e302a3f836b63683c31960aeadfdbe66a8ba3
prompt bytes: 545
output capture: /tmp/hott-p-dag-runner-isolation-002-final.md
deadline: 60 seconds
acceptance: exact final text RUNNER_ISOLATION_HEALTH_PASS; no observed global instruction,
            no tool call, and banner confirms requested model/effort/sandbox/approval
failure: any global instruction, tool call, incorrect marker, auth/config failure, or no final artifact
         means RUNNER_ISOLATION_NOT_QUALIFIED
partial-output policy: console is inspected only for injection/tool event; no theory/source conclusion
recursion: false
```

## Boundary

This test has no theory payload and cannot establish a HoTT or ZFC result. A pass only qualifies the next blind NodeCard's **runner context**. It does not revalidate H-005/H-006 retroactively, nor does it release the HoTT replay or ZFC gates.
