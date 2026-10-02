# P-DAG-HOTT-DISCOVERY-008：依赖 Π 类型 h-level 候选的原典核验

> **身份：** `MASTER_PRIMARY_SOURCE_READ / SOURCE_DERIVED_PAYMENT_CONTROL / NO_HOTT_REPLAY_PASS`。

## Frozen candidate

The isolated Terra/Max D-L6b node selected:

```text
u = B : A → Uᵢ
F = dependent Π-formation
Q? = from ∀ a:A, isType(n, B(a)), assess isType(n, Π(a:A) B(a))
```

The node marked P2/P3/C/I/O/Done/source validation `UNKNOWN`. This audit tests only whether the frozen Book-style
HoTT source supplies the stated Q?; it does not introduce a consumer or replace the task.

## Primary source

| Source | Identity and scope |
|---|---|
| Frozen local Book source | `HoTT/theory-schema/upstream/book-578b85cc/hlevels.tex`, SHA-256 `cfa75d289487f91affc4f5a9907857135c8a307b59dbc1cb9e3e9f41399618cc` |
| Definition | lines 32–45 define `isType(n)` and state that inhabitation is being an n-type |
| Exact discharge | lines 171–185, `thm:hlevel-prod`: for `n ≥ -2`, `A : type`, `B : A → type`, if every `B(a)` is an n-type, then `Π(x:A) B(x)` is an n-type |
| Proof dependency stated in source | lines 176–184: induction on n; the inductive step uses function extensionality and closure under equivalence |

The theorem’s hypotheses and conclusion are the candidate’s Q? with the source’s explicit bound `n ≥ -2`. Therefore
the exact Book profile does have a standard proof that discharges the proposed task.

## Verdict

```text
P1 discovery status: MODEL_RECALL_SITE_CANDIDATE was valid as a sealed-output observation
source validation: SOURCE_DERIVED_PAYMENT_CONTROL
candidate tension: NOT_ESTABLISHED
P2/P3/C/I/O/Done: still UNKNOWN / NOT_REQUESTED
HoTT replay release: NOT_PASSED
```

This is not a failure of the isolated runner or a refutation of Pattern P. D-L6 only screens a payment visibly given
in the sealed theory profile; it did not list `thm:hlevel-prod`. The post-discovery source tracer did its intended
job: it found that the prospective native task already has a directly relevant standard theorem. The result becomes a
negative control for the discovery→source-validation split.

## Boundaries and next action

The source establishes a theorem under the stated book assumptions. It does not establish a real-world completion
task, a natural consumer with `C/I/O/Done`, a P2 language-feedback structure, a P3 lifecycle, a UR, a formal
inconsistency, or any claim about all HoTT variants. The next blind discovery node, if later authorized, must use a
new frozen theory profile rather than retrying this answer or retrofitting the result into a P1/P2/P3 convergence.
