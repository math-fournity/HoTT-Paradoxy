# P-DAG-HOTT-DISCOVERY-008：隔离 App Server 上的 D-L6b HoTT 盲态发现收据

> **身份：** `BLIND_DISCOVERY_EXECUTION_OBSERVATION / MODEL_RECALL_SITE_CANDIDATE / NOT_A_HOTT_RESULT`。

## 1. Frozen identity and runner result

| Field | Value |
|---|---|
| NodeCard | [HOTT-DISCOVERY-008 NodeCard](20261002-P-DAG-HOTT-DISCOVERY-008-APPSERVER-NODECARD.md) |
| Prompt identity | H-007 D-L6b Prompt, SHA-256 `a2f6b018d0f547d88b8f886c0b6010109c33598b20cce2017dc169444dc2c918`, 2592 bytes |
| Runner wrapper | `scripts/pattern_p_appserver_blind_discovery.py`, SHA-256 `a09194bd03b7c177d134e013a14db0458c597d46047622b76f31abacf5eecd7e` |
| Method / runtime | clean `breadth-terms-3.12.1` method worktree; `governance-v3.26.0` App Server isolation route |
| Requested / echoed actor | `gpt-5.6-terra / max`; isolated cwd; `governance-regression-fresh`; `approvalPolicy=never`; all five exact echoes true |
| Prompt / credential gates | model-visible prompt gate `PASS`; controlled local auth borrow; post-borrow deny gate `PASS`; no source auth content/hash/size in public summary |
| Terminal | completed in 44.288 seconds; final 1731 bytes / 226 words / SHA-256 `cb08e3cff29b4c1819c5da86354e5d9e6ef9f23a16711c272f06109af6103dc1` |
| Side effects | command=0, file-change=0, approval-request=0; no remaining borrowed `auth.json`; no live App Server process |

The private raw prompt-input, wire, stderr, final text and home receipt remain under the run-scoped private experiment
root. This public audit contains only the task-requested public D0–D5 trace and safe execution facts.

## 2. Exact public DiscoveryTrace

> D0 — Scope: only the stated ordinary HoTT profile and Pattern-P screens. Exclude project history, implementations, annotations, consumers, defects, and unstated source facts.
>
> D1 — Screened sites:
>
> 1. Identity/transport: \(u=p:A=B\); \(F\) is identity elimination and transport. Q?: transfer \(z:P(A)\) to \(P(B)\). D-L5 passes as a native transport task. D-L6: `DISCOVERY_DIRECT_RULE_ANSWER`, since transport along \(p\) is visibly supplied by \(F\).
>
> 2. Univalence: \(u=e:A\simeq B\); \(F\) is that `idtoeqv` is an equivalence. Q?: obtain a path \(A=B\) from \(e\). D-L5 passes as native equivalence-use. D-L6: `DISCOVERY_DIRECT_RULE_ANSWER`, through the inverse of `idtoeqv`.
>
> 3. Dependent product: \(u=B:A\to U_i\); \(F\) is dependent \(\Pi\)-formation. Q?: from fiberwise `isType(n,B(a))`, assess `isType(n, Π(a:A) B(a))`. D-L5 passes. D-L6 does not visibly supply an h-level witness, closure rule, or computation establishing that judgment.
>
> D2 — `MODEL_RECALL_SITE_CANDIDATE`: \(u=B:A\to U_i\), \(F=\Pi\)-formation, Q? as in site 3. Nearby rejected alternative: transport along an identity path, directly paid by transport.
>
> D3 — Prospective native task: determine whether and how fiberwise h-level data yields h-level data for the dependent product at the displayed level. The final candidate is not directly paid by \(\Pi\)-formation itself: the profile gives function formation, but no explicit h-level-preservation witness or rule.
>
> D4 — C/I/O/Done, P2/P3, theorem, inconsistency, UR, and source validation: UNKNOWN.
>
> D5 — An explicit source rule, constructor, computation principle, or supplied witness establishing h-level preservation for dependent products would falsify the final non-direct assessment.

Master schema check on the SHA-pinned final text: D0–D5 headings all present; `MODEL_RECALL_SITE_CANDIDATE` count=1;
`NO_MODEL_RECALL_CANDIDATE / DIRECT_PAYMENT_ONLY` count=0. The wrapper was subsequently tightened so future runs
enforce this condition mechanically; that later wrapper revision is not retroactively substituted for the H-008 SHA.

## 3. What this node supports

The run supports only these execution and discovery claims:

1. The repaired App Server lane can run this sealed Prompt without the earlier visible global-instruction/tool-injection
   event.
2. D-L6b was actually exercised: two directly paid native sites were retained as controls, then the response screened
   one later obvious foundation site rather than stopping at univalence.
3. The agent supplied a bounded, public reason for selecting a non-direct **source-validation candidate** and for
   rejecting the nearby transport site.

It does **not** support that dependent products fail to preserve h-levels, that book-style HoTT contains a defect,
that this is a natural consumer, that P2/P3 match, that a same-task `C/I/O/Done` card exists, that the trace is a
UR, or that the HoTT replay release gate has passed. The next permissible node is a source tracer with the exact
candidate, including a check whether standard Π/h-level results directly discharge it.

## 4. Delta SelfAuditCard

| Field | Record |
|---|---|
| Original expectation | A sufficiently explicit D-L5/D-L6/D-L6b Pattern-P prompt should let Terra/Max search its theory knowledge for an obvious foundation position without traversing project answers. |
| Actual result | The trace first rejected direct transport and univalence payments, then selected dependent Π/h-level preservation as a candidate and named a falsifier. |
| Alignment | `EXECUTION_ALIGNMENT / DISCOVERY_OBSERVATION_ONLY`; it tests P1 selection behavior, not a mathematical proposition. |
| New evidence gap | P1 validation needs the exact HoTT source for Π/h-level formation/preservation, then a source-defined `C/I/O/Done`; P2/P3 remain untested for this card. |
| Reopen / falsifier | If the primary source supplies the h-level result as an immediate standard consequence in the relevant profile, classify this candidate `SOURCE_DIRECT_PAYMENT_CONTROL`; if it does not, freeze the actual task/consumer before any P2/P3 node. |
