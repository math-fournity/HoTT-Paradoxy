# HMZ-002：Voevodsky 的 ZFC—等价性—类型系统来源分母

> **身份：** `CLOSED_SOURCE_RUN_WITH_SCOPE / FROZEN_DENOMINATOR / EQUIVALENCE_BOUNDARY_RECONSTRUCTED`。
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
| `HMZ-S-015` | E | Ahrens & North, *Univalent Foundations and the Equivalence Principle*, 2022. | `READ_RELEVANT_LOCATORS` | 精确区分 ZFC 中允许的非不变表述、抽象数学所需的 equivalence principle 与 typed-language criterion。 |
| `HMZ-S-010` | C, D, E | Shulman 2008, from HMZ-001 (read-only reused source). | `REUSED_SAME_VERSION` | ZFC class/formula and NBG/global-choice controls; prevents a generic equivalence slogan from becoming Q. |
| `HMZ-S-011` | C, D, E | Isabelle/ZF 2021, from HMZ-001 (read-only reused source). | `REUSED_SAME_VERSION` | actual ZF formalization/payment control. |
| `HMZ-S-009` | D, E | Mumford 1965, from HMZ-001 (read-only reused source). | `REUSED_SAME_VERSION` | family/maps payment control for structural classification. |

### 分母修订 A：独立 equivalence literature

`HMZ-S-015` 是本 run 的必要比较来源：它直接讨论 equivalence principle、给出 set-theoretic
non-invariance 例子，并说明需要何种语言约束。它没有新增理论靶；它用于核对 Voevodsky 的 2011 描述不能被
写成“ZFC 自己答不出的问题”。

## Initial source locators

- `HMZ-S-012`: PDF slides 2–4 and 17–21; the univalent model is described relative to ZFC, and set theory remains a consistency benchmark.
- `HMZ-S-013`: pp. 26–28 describe well-ordered simplicial fibers and standard isomorphisms; pp. 46–50 describe actual type-system formation/inductive data. Reading is technical, so no motive claim will be inferred merely from a construction.
- `HMZ-S-014`: slides 2–5 explicitly frame ZFC convenience and the “problem of equivalence”; slides 9–20 contain the author’s proposed type-system response and its constraints.

## 已执行的 Q 检查

1. **ZFC-side exact object:** `HMZ-Z-008` fixes the source-supported object as a set-coded structure together with a representation-sensitive property; it is not a generic “all constructions”.
2. **Actual consumer:** sources provide statement/selection/family tasks and their Done; no source treats the non-invariant property as structural delivery.
3. **P structure:** no source supplies a same-object formation-before-existence bridge, reentry or admission/Done cycle.
4. **Controls:** Ahrens/North's typed-language criterion, Shulman's NBG/global Choice, Mumford maps and Voevodsky's well-ordering are explicit payments.

### Run verdict

```text
R_SOURCE_REPORTED = YES
ZFC_EQUIVALENCE_REPRESENTATION_BOUNDARY = SOURCE_SUPPORTED
P_QUALIFIED_Q = NO
H0→Z0 TRANSPORT = NOT_FORMED
DENOMINATOR_COMPLETE_WITH_SCOPE = YES
```

No P-DAG/worker or mathematical conclusion was authorized or run.
