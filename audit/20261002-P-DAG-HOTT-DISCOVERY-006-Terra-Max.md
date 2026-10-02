# P-DAG-HOTT-DISCOVERY-006：宽基础理论画像的 D-L6 回归结果

> **身份：** `P_DISCOVERY_TERMINAL_OUTPUT / D_L5_PASS / D_L6_DIRECT_PAYMENT_PASS / ALTERNATE_SITE_CONTINUATION_REQUIRED / NOT_A_HOTT_REPLAY_PASS`。

## 1. Execution receipt

| Field | Value |
|---|---|
| Parent NodeCard | [`20261002-P-DAG-HOTT-DISCOVERY-006-BLIND-SCHEMA-NODECARD.md`](20261002-P-DAG-HOTT-DISCOVERY-006-BLIND-SCHEMA-NODECARD.md) |
| Exact prompt | [`20261002-P-DAG-HOTT-DISCOVERY-006-BLIND-SCHEMA-PROMPT.md`](20261002-P-DAG-HOTT-DISCOVERY-006-BLIND-SCHEMA-PROMPT.md) |
| Prompt SHA-256 / bytes | `c0f1d46d8abdc1ab906c109cab112e9fa8c2ce213dc9dfc73a8e6b729c70f447` / `2355` |
| Session | `01a0fda6-8964-7e82-8afd-75eb317e9599` |
| CLI banner | `gpt-5.6-terra / max / read-only / never` |
| Working root | isolated `/tmp/hott-p-dag-hott-discovery-006-scratch`; no project directory added |
| Final artifact | `/tmp/hott-p-dag-hott-discovery-006-final.md` |
| Output SHA-256 / bytes | `5ae65d62c5c4973103d62ece04aea3a75c8c730e0437001a9b4168ef828631a2` / `1159` |

The worker was given only the frozen ordinary-theory profile in the prompt. It had no project paths, source files, web, tool access, historical outputs, or existing HoTT construction.

## 2. Public DiscoveryTrace

The worker selected the obvious universe/univalence interface, but this time explicitly rejected it:

```text
u = U_i
F = idtoeqv : (A=B) → (A≃B), asserted to be an equivalence
Q? = from e:A≃B, form a universe path usable for transport

D-L5: PASS — this is an equivalence-use/transport task.
D-L6: PASS — F being an equivalence supplies an inverse:
  e ↦ idtoeqv⁻¹(e) : A=B
Verdict: DISCOVERY_DIRECT_RULE_ANSWER; no candidate remains.
```

Its only nearby alternative was path induction on an already given path. It kept C/I/O/Done, P2/P3, theorem, inconsistency, UR, and source validation as `UNKNOWN`.

## 3. Master verdict

The result is a clean regression pass for D-L6. H-005 had required the Master to read the Book and recognize that `ua` supplies the inverse. H-006 identified the direct inverse solely from the packet's own `isEquiv(idtoeqv)` statement and refused to promote the task to a candidate.

It does **not** test whether P can locate the intended HoTT line. The prompt asked for one candidate or a direct-answer verdict, so once univalence was screened out the worker was contractually allowed to stop. The remaining broad source profile still included other foundational interfaces, but the protocol did not require a bounded second choice.

```text
D-L5 regression: pass
D-L6 regression: pass
HoTT replay: not passed
new diagnosis: DISCOVERY_DIRECT_PAYMENT_EARLY_STOP
```

## 4. Delta SelfAuditCard

| Field | Record |
|---|---|
| Original units | C11/C14 require a one-pass line, while C09/C13 require the obvious core position rather than a premature detour. |
| Actual action | One broad, no-answer-leak, terminal-output-captured discovery run after D-L6. |
| Alignment | The filter operated correctly and did not manufacture a Q. |
| Deviation class | `IDEA_SPEC_INCOMPLETE`: the discovery protocol treated a rejected first line as final even though its purpose is to select one eligible obvious line. |
| Repair | Add D-L6b/bounded alternate-site continuation: after D-L5/D-L6 rejects a site, examine at most two additional obvious foundation sites in the same response, then return one eligible candidate or an honest no-eligible verdict. |
| Tool impact | P1 discovery and NodeCard/MatchTrace scheduling only; P2/P3, L6 source validation, the HoTT release gate, and P4 remain unchanged. |
| Falsifier | If the bounded continuation forces unrelated enumeration or repeatedly invents candidates after three screened sites, reduce its bound or reject it as overbroad. |

## 5. Boundary

The observed behavior is a prompt-bounded regression fact. It is not evidence of a HoTT defect, a mathematical theorem, a model-internal mechanism, or a successful ZFC/HoTT pattern match.
