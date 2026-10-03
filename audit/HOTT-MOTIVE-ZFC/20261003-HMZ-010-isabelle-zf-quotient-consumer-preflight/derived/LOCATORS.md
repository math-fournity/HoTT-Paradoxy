# HMZ-S-027：Isabelle/ZF quotient consumer 读取卡

> **派生身份：** `LOCATOR_AND_INTERPRETATION_AID / NOT_A_SOURCE_SUBSTITUTE`。

## I/O / Done

```text
Input:  sets A, relation r, and a unary/binary meta-level operation b.
Formation: A//r is a replacement/image-style set of r``{x} for x∈A.
Consumer: quotientE or a unary/binary quotient-operation lemma.
Observation: a membership assertion, an equality of values/classes, or target type membership.
Done: all explicit assumptions in the lemma, including equiv(A,r), congruence/
      respects, and membership/type obligations, have been supplied.
```

## Source-payment ledger

| Source locator | Payment/guard | What it prevents us from claiming |
|---|---|---|
| `EquivClass.thy:10–12,106–109` | quotient is defined before `quotientI`, whose proof invokes `RepFunI`. | There is no source evidence that an unformed `A//r` validates its own formation. |
| `EquivClass.thy:67–100` | equivalence-class equality is conditional on `equiv(A,r)` and stated memberships. | No arbitrary representative is treated as a quotient operation without relation data. |
| `EquivClass.thy:132–146` | operation on a class assumes `equiv`, `b respects r`, quotient membership and a target typing condition. | No function is silently descended to the quotient. |
| `EquivClass.thy:178–193` | binary operation repeats explicit `equiv`, congruence and membership conditions. | Broader arity does not create a new formation/reentry loop. |
| `HMZ-S-011` manual pp. 25–30 | `RepFun` is functional replacement and comes with `RepFunI/E`. | One may not redescribe this route as the Book's `\mathcal P(A)`-subset route. |

## Route comparison

```text
HoTT Book bridge:   quotient as a set of equivalence classes, presented as a
                    subset of P(A); alternative HoTT construction has a
                    universe/resizing cost.
Isabelle/ZF source: quotient as {r``{x} . x∈A}, built through RepFun;
                    operations require source-stated relation/congruence gates.
Consequence:         same quotient-style goal, different formation route;
                    this source is a payment control, not the missing Power Set
                    consumer for P qualification.
```
