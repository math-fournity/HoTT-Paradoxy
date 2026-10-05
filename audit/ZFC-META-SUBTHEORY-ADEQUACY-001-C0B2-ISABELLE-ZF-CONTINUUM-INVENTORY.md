# C0B2：Isabelle2025-2 Session ZF 的连续统候选盘点

> **身份：** `C0B_INDEPENDENT_FORMALIZATION_INVENTORY / BOUNDED_NEGATIVE / NOT_A_GLOBAL_ABSENCE_CLAIM`。
>
> **TaskCard：** [C0B2](ZFC-META-SUBTHEORY-ADEQUACY-001-C0B2-TASKCARD.md)。
>
> **判词：** `NO_ADMISSIBLE_CONTINUUM_CHAIN_IN_ISABELLE2025_2_ZF_SESSION_WITH_SCOPE / C0B2_LOCAL_LEAF_CLOSED`。

## 1. 冻结来源

| source | current identity | directly observed |
|---|---|---|
| [Isabelle Session ZF index](https://isabelle.in.tum.de/dist/library/FOL/ZF/index.html) | 页面标题 `Session ZF (Isabelle2025-2)`；本轮读取。 | 该 session列出 ZF_Base、ordinal、natural numbers、arithmetic、cardinal、ZF、AC、Zorn、ZFC等 theory。 |
| [Theory ZF](https://isabelle.in.tum.de/dist/library/FOL/ZF/ZF.html) | official current rendered theory。 | 自称“Everything Except AC”；导入 List/IntDiv/CardinalArith，并给迭代、ordinal limit与transfinite recursion。 |
| [Theory ZFC](https://isabelle.in.tum.de/dist/library/FOL/ZF/ZFC.html) | official source search result。 | `ZFC imports ZF InfDatatype`；它不是 `HOL/Real` 或 `HOL-Analysis` session。 |

## 2. 分母内的正反事实

`FOL/ZF` 当前 session 确实是一个独立于 Mizar 的 ZF/ZFC formal foundation lane，并且包含 sequence-like iteration、ordinal limit和choice-related theories。这是正面事实。

但是冻结的 **Session ZF theory list** 没有出现 real-number construction、Cauchy/Dedekind reals、real sequences、epsilon-limit、continuous real function、derivative或continuous trajectory chain。搜索命中的 Isabelle reals、limits和analysis页面属于 `HOL`/`HOL-Analysis`，不是这条 `FOL/ZF` session；它们不能被偷接为 Isabelle/ZF 的 S。

因此对于本 TaskCard 要求的

```text
M = FOL/ZF/ZFC Session
S = real / sequence / limit / continuous trajectory theorem chain
```

当前 version-fixed denominator 只有 M 的 foundation侧，没有足以进入 C1/C2 的 S。`Limit`在该 session中是 ordinal-limit case，不能仅按名字替换为实分析极限。

## 3. 有界负结论

```text
NO_ADMISSIBLE_CONTINUUM_CHAIN_IN_ISABELLE2025_2_ZF_SESSION_WITH_SCOPE
```

这不意味着 Isabelle、ZF、ZFC或任何版本的 Isabelle都不能形式化 real analysis；它也不表示 HOL reals有缺陷。它只排除把当前 official `FOL/ZF` session 直接当作本 SOP 的独立 continuous-model S 来源。

## 4. 对候选宇宙的影响

C0B2 收窄了一个独立 formalization candidate，而没有改变 C6A 的 Mizar-based conditional verdict。现在该 route应退役为本版本的 bounded negative；下一个最高判别项是 F-E 的 actual defense／paid bridge source，不能因为独立库没命中就停止 Goal。
