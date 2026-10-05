# C0C1：基础、数学模型与物理完成之间的来源责任矩阵

> **身份：** `C0C_SOURCE_MATRIX / APPLICATION_ADEQUACY_CRITERION_CANDIDATE / NOT_A_ZFC_AXIOM`。
>
> **TaskCard：** [C0C1](ZFC-META-SUBTHEORY-ADEQUACY-001-C0C1-TASKCARD.md)。
>
> **判词：** `R1_R2_MATHEMATICAL_FOUNDATION_SOURCE_SUPPORTED / R3_APPLICATION_SOURCE_SUPPORTED / R4_REPRESENTATION_ADEQUACY_CRITERION_SOURCE_SUPPORTED / ZFC_INTERNAL_BRIDGE_DUTY_UNPAID / C0C1_LOCAL_LEAF_CLOSED`。

## 1. R1–R4 来源矩阵

| 层 | 来源与其实际立场 | 本项目可用的内容 | 不能推出 |
|---|---|---|---|
| `R1` 内部数学基础 | [SEP: Set Theory](https://plato.stanford.edu/entries/set-theory/) §5：集合论把数学对象／陈述形式化为集合／集合语言；在这个意义上成为数学的 foundation。 | `M` 可构造／表述／证明 `S` 的数学对象和定理。 | M 自动对物理对象作经验判断。 |
| `R2` 数学语义／模型 | [IEP: Foundations of Mathematics](https://iep.utm.edu/fomath/) §3 将 set-theoretic foundation 描述为数学的 shared proof standard 和可研究理论的 controlled environment；Mizar JAR 2018说明 real numbers在 MML 中由普通证明构造。 | internal proof / formal model / relative consistency 的责任边界。 | formal model 已经代表一个具体物理 target。 |
| `R3` 应用主张 | [IEP: Zeno](https://iep.utm.edu/zenos-paradoxes/) 第 68–88、98–104、112–126 行：Standard Solution 把 standard analysis/calculus 与 physical path/time/motion相连，同时承认适切性仍可争论。 | 存在可审计的 application source，不能说所有工作只在内部数学。 | 这个 application source 本身是 bare ZFC 的 object-language theorem。 |
| `R4` 表征／适切性 | [SEP: Scientific Representation](https://plato.stanford.edu/entries/scientific-representation/) 将数学模型到 physical target 的适用性和准确性列为独立问题；模型能产生 target claims需要解释其如何适用于物理世界。 | 当一个 source 把 mathematical S 用于 physical Q 时，要求 target mapping / applicability 不是项目任意加的怪条件。 | ZFC 的每条公理本身承诺、或能自动检查这一 bridge。 |

## 2. 这张矩阵真正改变了什么

它排除了两种相反的错误：

1. **过强归罪。** `R1/R2` 不支付“bare ZFC 内部有一条必须审查物理 motion completion 的公理”。因此不能说 ZFC 的对象语言因未检查 bridge 而不一致，或它已违反一个来源明示的 internal rule。
2. **过弱免责。** `R3/R4` 表明，一旦 Standard Solution 被作为对 physical motion 的解释／解答提出，数学模型到 target 的应用不是可自动免除的问题。该问题不属于单一 MML theorem，也不能由集合编码替代。

可来源支撑的 `Adequacy` 因而必须写成：

```text
ApplicationAdequacy(S, Q_physical, P):
  a source that uses S to support a claim about Q_physical must expose
  the representation/interpretation relation sufficient for that claim,
  including whatever completion predicate it carries.
```

这是一项**应用—表征层**的 adequacy criterion；它不是 “ZFC proves ApplicationAdequacy” 或 “ZFC must internally decide every physical task”。

## 3. 对 C5 的支付与未支付

| C5 所需字段 | 现状 |
|---|---|
| 有非任意的 bridge-audit criterion | `PARTIALLY_PAID`：R4 给出模型到物理 target 的适用性／准确性问题；IEP Zeno显示该问题在当前案例并非凭空加入。 |
| criterion 归为 bare ZFC 内部责任 | `UNPAID`：R1/R2 sources没有这样说。 |
| criterion 可用于审计 physical application policy | `SOURCE_SUPPORTED_WITH_SCOPE`。 |
| actual P / full Q / bridge 的具体字段 | `UNPAID`，仍需 C3B/C4。 |

这使 `Adequacy` 不再是 AI 的无来源偏好，但也阻止它被偷写成 bare ZFC 的新公理。

## 4. 后继含义

下一步必须固定 **actual application policy** 的 P：IEP 标准解法究竟怎样从 rich mathematical model说到 physical Q，及其是否明示 task revision。只有 P 的 source range固定后，C5 才能把上面的 `ApplicationAdequacy` 套到一份具体合同；然后才可做 C4 bridge audit和最终 C6 machine target。
