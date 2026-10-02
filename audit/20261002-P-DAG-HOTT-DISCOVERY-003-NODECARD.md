# P-DAG-HOTT-DISCOVERY-003：无泄漏 HoTT 一遍发现 NodeCard

> **身份：** `P_DISCOVERY / BLIND_MODEL_RECALL_CANDIDATE / NOT_A_VALIDATION_OR_THEORY_RESULT`。
>
> **parent:** HOTT-REPLAY-002. This run exercises only the newly separated discovery stage.

## Inherited source and isolation

The exact neutral HoTT Book source pack, source hashes, no-leak exclusions and theory variant are inherited from [HOTT-REPLAY-001](20261002-P-DAG-HOTT-REPLAY-001-NODECARD.md). The worker has no access to the repository, Book §8.8 examples, `QuestioningDelay`, past outputs, web, Git, local files or any named previous HoTT result.

## Discovery contract

```text
role: P-DISCOVERY mapper
runner: fresh Codex CLI --no-daemon --ephemeral
model/effort request: gpt-5.6-terra / max
sandbox/approval: read-only / never
output capture: --output-last-message /tmp/hott-p-dag-hott-discovery-003-final.md
deadline: 90 seconds
allowed output: D0–D5 public DiscoveryTrace only
allowed verdicts: MODEL_RECALL_SITE_CANDIDATE / NO_MODEL_RECALL_CANDIDATE / DISCOVERY_TASK_TOO_THIN
mandatory unknowns: C/I/O/Done, source validation, P2/P3 and any theorem/UR status unless the frozen pack itself supplies them
```

The discovery card must name one candidate `u/F/Q?`, one neighboring alternative, why its candidate is a theory-level line rather than a conclusion, what exact source evidence must next be sought, and what source/control would falsify it. It may not output `SITE_SELECTED`, `ZFC_Q_LOCATED`, `HOTT_REPLAY_PASS`, an internal inconsistency, or a mathematical theorem.

## Master evaluation

This is a necessary but insufficient part of the HoTT replay release. Master will compare its line with the known target only after terminal output is sealed; a plausible mention of universes, h-levels or univalence without a concrete candidate/Q? and expected validation gap does not count as a discovery pass.

## H-003-A execution outcome

Fresh CLI session `01a0fd8d-9031-7762-a403-266cee07f515` returned the requested Terra/Max/read-only/never banner and began planning a discovery trace. At the 90-second deadline, `/tmp/hott-p-dag-hott-discovery-003-final.md` was absent; Master sent `SIGINT` and confirmed the process ended.

```text
TIMEOUT_NO_TERMINAL_OUTPUT
NO_DISCOVERY_TRACE
NO_P_DISCOVERY_VERDICT
```

This does not falsify P-DISCOVERY. It only establishes that this max-effort structured request did not finish within 90 seconds. One successor with the same no-leak content but a short output contract and a 180-second deadline is allowed; further identical retries require an external runner change.
