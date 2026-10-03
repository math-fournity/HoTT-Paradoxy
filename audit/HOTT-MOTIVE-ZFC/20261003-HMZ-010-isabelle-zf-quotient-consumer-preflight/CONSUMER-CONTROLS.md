# HMZ-010：actual consumer、formation route 与模式 P 控制

## 1. 这个来源真正完成的任务

`EquivClass.thy` 不只定义一个名词。它形成 `A//r`，证明成员的 introduction/elimination 原理，说明当 \(r\) 是 equivalence relation 时商类如何覆盖、相交或相等；随后只有在 `b respects r` 的条件下，才把 unary/binary operations 交给商类使用。

| 比较项 | HMZ-009 Book route | HMZ-010 Isabelle/ZF route | 结论 |
|---|---|---|---|
| 输入 | \(A,R\) 与 equivalence classes | \(A,r\) 与 `equiv(A,r)` | quotient-style task is comparable. |
| formation | Power Set-subset description | `{r``{x}. x∈A}` via `RepFun` / functional replacement | **F differs.** |
| consumer | textbook comparison of quotient constructions | operational lemmas for class-level unary/binary operations | actual consumer exists only at proof-formalization layer. |
| Done | quotient compared with `A/R` / class construction | lemma conclusion after all relation/congruence/type premises | Done is source-explicit. |

## 2. P1/P2/P3 与同一任务

```text
P1 L0: PASS_WITH_SCOPE — Isabelle/ZF set objects and the quotient interface are fixed.
P1 L1: PASS_WITH_SCOPE — RepFun formation and quotientI/E are explicit.
P1 L2: PASS_WITH_SCOPE — UN_equiv_class and later lemmas are actual consumers.
L2c: PASS_WITH_SCOPE — object, formation, consumer and Done all remain in the
  proof-formalization layer; this cannot be promoted to bare ZFC semantics.
P2: NOT_APPLICABLE — no source-reported same-object negative reentry.
P3: NOT_APPLICABLE — no pending/admission lifecycle or unfulfilled Done.
same-formation test against HMZ-009: FAIL — the Book's P(A)-subset route is
  not the source's functional-replacement route.
H0→Z0: FAIL/UNFORMED — higher sameness process and its observation/Done are
  not preserved by a set quotient library.
```

## 3. Positive and negative controls

| Control | Source-grounded result |
|---|---|
| `C+` — formation before use | `quotientI/E` follow the definition and `RepFunI`; every operation receives membership hypotheses. |
| `C+` — respect relation before descent | `UN_equiv_class` and its type theorem require `b respects r`; binary analogues require `respects2`. |
| `C−` — Power Set route cannot be silently substituted | Book's \(\mathcal P(A)\)-subset construction and Isabelle's `RepFun` formation are distinct `F` values. |
| `C−` — proof library is not bare ZFC | all evidence is an Isabelle/ZF theorem source with meta-level syntax, tactics and named rules. |

The source payment therefore blocks the candidate in this preflight. It does **not** prove that every ZFC quotient consumer, every Power Set consumer, or the overall ZFC theory has the same payment.
