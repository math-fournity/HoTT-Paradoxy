# P-DAG-HOTT-DISCOVERY-010：修正 Prompt 包装后的脱敏 h-level 追问 NodeCard

> **身份：** `PRELAUNCH_NODECARD / BLIND_PROCESS_PROFILE / HOTT_REPLAY_CALIBRATION / NOT_A_HOTT_RESULT`。

## Parent correction

H-009 stopped before authentication, App Server startup or model sampling because its Markdown audit header became
part of the turn input. H-010 uses the same frozen fenced theory payload and D-L5/D-L6/D-L6b contract, while the
wrapper now extracts only that payload. This is a runner packaging repair, not another draw from the same model
prompt.

## Frozen contract

```text
node_id: P-DAG-HOTT-DISCOVERY-010
parent: HOTT-DISCOVERY-009 pre-auth prompt-wrapper failure
runner wrapper SHA-256: 95f720e50fd1ce05d68bff56e0a53e7fad5e23179fc6c560dc2cc4bc4d9b1b09
turn payload SHA-256: 9eaf50c72bb9d42b4b9a57c07f50ed36c15fcd29776814ffdbb346d190dfcdec
turn payload bytes: 2425
markdown prompt file SHA-256: a21ff7c4004485f51fe19ee25075f042af09e9db17ad0e108455d929fbd5d46b
method repo: /Users/aurolafly/codex-worktrees/breadth-terms-3.12.1 (clean at launch)
private root: /Users/aurolafly/.codex-experiments/p-dag-appserver-isolation-20261002
run_id: p-dag-hott-discovery-010
actor: gpt-5.6-terra / max; fallback=false
permission/approval: governance-regression-fresh / never; network default-deny
authorization: R-035 controlled temporary auth borrowing under user-authorized P-DAG scope
timeout: 180 seconds + exact interrupt and 20-second grace
trajectory policy: REQUIRED_AFTER_TERMINAL
expected native source view: private bidirectional {timestamp,direction,message} wire; persisted rollout may be absent
post-terminal reader: governance-v3.26.1 /Users/aurolafly/codex/tools/session_trajectory.py
receipt predicate: catalog + tree must resolve the returned thread/turn; filtered tool/result/approval scan, terminal,
                   private 0600 context extracts and separate L1-L5 status must be recorded before output interpretation
reasoning boundary: only Host-exported summary is usable; encrypted, redacted or absent reasoning is OPAQUE/UNAVAILABLE
```

## Blindness, output and stop rule

The worker sees only the fenced theory payload and its isolated text-only workspace. Prompt-input must exclude the
project root, `QuestioningDelay`, `PedometerSemantics`, `universeHasNoLevel`, `QIsNever`, `Power Set`,
`ZFC_Q_LOCATED`, the Pattern-P Skill name and the known univalence answer. It must emit exactly one bounded D0–D5
trace, with no tools or side effects. A clean terminal output is a P1 discovery observation only; source validation,
P2/P3/C/I/O/Done, UR, mathematical status and replay release stay open. Any gate, echo, tool, output-schema or
terminal failure is a runner failure and ends this node without a theory conclusion. If the run has a private wire but
no persisted rollout, its trajectory source stays `PARTIAL`, not absent. If the current reader cannot parse the actual
direct App Server envelope, classify `TRAJECTORY_PARSER_COVERAGE_GAP`, isolate the output's behavior interpretation,
and repair the reader through a redacted fixture before retrying any analysis.
