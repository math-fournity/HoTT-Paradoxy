# P-DAG-HOTT-DISCOVERY-004：长观察窗、短输出的无泄漏 HoTT 发现 NodeCard

> **身份：** `RETRY_AFTER_DISCOVERY_TIMEOUT / PRELAUNCH_NODECARD / NOT_A_HOTT_RESULT`。
>
> **parent:** HOTT-DISCOVERY-003. This retry changes two observable execution conditions: a 180-second deadline and a bounded short final response. It preserves the source pack, no-leak exclusions, model request and discovery-only semantics.

## Contract

```text
runner: fresh Codex CLI --no-daemon --ephemeral
model/effort request: gpt-5.6-terra / max
sandbox/approval: read-only / never
source pack: exactly HOTT-DISCOVERY-003 / HOTT-REPLAY-001
output capture: --output-last-message /tmp/hott-p-dag-hott-discovery-004-final.md
final response limit: ≤ 350 English words, D0–D5 in compact bullets
deadline: 180 seconds
failure: TIMEOUT_NO_TERMINAL_OUTPUT; no P discovery verdict
retry policy: no further same-source discovery retry without external runner change
```

The task remains to propose at most one `MODEL_RECALL_SITE_CANDIDATE`, one nearby alternative, a tentative `Q?`, required source validation, and one falsifier. It may not make C/I/O/Done, P2/P3, theorem, inconsistency, UR or HoTT replay-pass claims.
