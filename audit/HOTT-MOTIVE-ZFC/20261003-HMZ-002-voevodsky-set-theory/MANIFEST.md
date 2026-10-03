# HMZ-002：Voevodsky 的 ZFC—等价性—类型系统来源分母

> **身份：** `ACTIVE_SOURCE_RUN / FROZEN_DENOMINATOR / READING_AND_RECONSTRUCTION_IN_PROGRESS`。
>
> **前序：** HMZ-001 已在其十个来源范围内闭合，未产生 `CANDIDATE_SEED`。本 run 不是重复 HMZ-001，而是检验
> Voevodsky 更明确的 “problem of equivalence” 与 ZFC/type-system 对比是否给出一个更精确的 R→Z 入口。

## 范围

```text
R focus:
  Voevodsky 对 ZFC-based formalization、equivalence-respecting constructions、
  predicate calculus、constructivity、type-system syntax 的直接说明。

Candidate obligation:
  Do not convert “ZFC lacks a natural equivalence filter” into a P/Q claim
  until a fixed ZFC-side object/formation/consumer/Done and a same-task
  reentry or unpaid completion question exist.
```

## 冻结分母

| ID | 类别 | 来源 | 状态 | 本轮作用 |
|---|---|---|---|---|
| `HMZ-S-012` | A, B, E | Voevodsky, *Univalent Foundations and Set Theory*, ASL 2013. | `READ_RELEVANT_LOCATORS` | UF 与 set-theoretic foundations 的相对一致性、type-system sentences、ZFC as benchmark。 |
| `HMZ-S-013` | B, E | Voevodsky, *Notes on Type Systems*, 2011. | `READ_RELEVANT_LOCATORS` | type-system formation/derivation machinery、universes、well-ordering and standard-isomorphism technical payment. |
| `HMZ-S-014` | A, B, E | Voevodsky, *Univalent Foundations of Mathematics*, Göteborg 2011. | `READ_RELEVANT_LOCATORS` | “problem of equivalence”、ZFC convenience claim、constructivity and consistency comparison. |
| `HMZ-S-010` | C, D, E | Shulman 2008, from HMZ-001 (read-only reused source). | `REUSED_SAME_VERSION` | ZFC class/formula and NBG/global-choice controls; prevents a generic equivalence slogan from becoming Q. |
| `HMZ-S-011` | C, D, E | Isabelle/ZF 2021, from HMZ-001 (read-only reused source). | `REUSED_SAME_VERSION` | actual ZF formalization/payment control. |

## Initial source locators

- `HMZ-S-012`: PDF slides 2–4 and 17–21; the univalent model is described relative to ZFC, and set theory remains a consistency benchmark.
- `HMZ-S-013`: pp. 26–28 describe well-ordered simplicial fibers and standard isomorphisms; pp. 46–50 describe actual type-system formation/inductive data. Reading is technical, so no motive claim will be inferred merely from a construction.
- `HMZ-S-014`: slides 2–5 explicitly frame ZFC convenience and the “problem of equivalence”; slides 9–20 contain the author’s proposed type-system response and its constraints.

## Open checks required before a Q-card

1. **ZFC-side exact object:** find a fixed ZFC presentation of an equivalence-sensitive construction, not a generic “all constructions”.
2. **Actual consumer:** locate input, operation, observation and Done; a statement that a filter is unavailable does not itself make an unpaid task.
3. **P structure:** establish source-supported formation, bridge/reentry or completion/admission behavior; ordinary isomorphism and Choice are not enough.
4. **Controls:** test the source’s own explicit payments—well-ordering, Choice, marking, classes/NBG, metasyntax, or a changed language.

No P-DAG/worker or mathematical conclusion is authorized by this manifest.
