# 实际来源边界：ZFC、Standard Solution 与用户的强 P

> **身份：** `SOURCE_CARD / SOURCE_BOUNDARY_CONTROL / NOT_A_KERNEL_THEOREM_OR_COMMUNITY_POLICY_CERTIFICATE`。

## 1. 可固定的来源事实

本轮重新读取的 [Internet Encyclopedia of Philosophy, “Zeno’s Paradoxes”](https://iep.utm.edu/zenos-paradoxes/) 当前版本支持以下有限事实：

| 来源段落 | 可以支持 | 不能支持 |
|---|---|---|
| §2，约 L67–79 | 该文称今日专家广泛接受至少一种以 calculus 为工具的 Standard Solution；它以连续运动、实时间位置函数和实际无穷的数学框架描述运动。 | 用户圆环的 `OriginDone` 已获支付；一个形式极限自动证明历史／现实过程已完成。 |
| §2，约 L100–113 | 该文把 Zermelo–Fraenkel set theory 的发展与实分析基础联系起来，并把“ZFC with Choice 是实分析等领域的适当基础、间接解决芝诺”的看法归为 majority view。 | bare ZFC 有一个关于运动、时间或每个子理论 process completion 的内建验收政策。 |
| §2，约 L123–132 | 文本说明 Standard Solution 推荐以与 Zeno 不同的概念与理论处理问题，并承认其理由依赖可用性、科学理论和充分性判断。 | `originalResolved` 与用户指定 `Done_strong` 相等，或 `A ↔ P` 已被来源证明。 |
| §5，约 L309–336 | 文本明确列出 Standard Solution 要放弃的直觉，并将“有限时间是否完成无限 task/actions”列为持续争论。 | “无最后离散步骤”已无条件被证明等价于原过程完成。 |

这些是来源文本的转述，不是 Lean／Agda theorem。网页事实在 2026-10-04 复核；后续引用应重新核对页面版本和段落。

## 2. 对 Q／P／A／B 表的当前赋值

| 字段 | 当前最强判词 | 原因 |
|---|---|---|
| ZFC-supported real-analysis / Standard-Solution 叙述存在 | `SOURCE_ESTABLISHED` | IEP 明示集合论、实分析和 Standard Solution 的关联。 |
| 用户圆环过程的 `State/input/step/observe/originDone` | `SOURCE_INAPPLICABLE` | IEP 讨论 Achilles／Dichotomy；它没有定义用户圆环的指定恢复合同。 |
| IEP 对原圆环 `Done_formal → OriginDone` 的 bridge | `SOURCE_UNOBSERVED` | 它没有同一状态域的 circle-process bridge。 |
| IEP 是否改写或修订问题语言 | `SOURCE_ESTABLISHED` | 它明说采用不同概念与理论，且列出需放弃的直觉。 |
| 数学共同体实际采用 Lean 的强 `MathematicalIllusionP` | `SOURCE_UNOBSERVED` | Standard Solution／majority-view 叙述不等同于对每个 `formalDone` 的 `originDone` 证明政策。 |
| `A ↔ AdmittedP` | `SOURCE_UNOBSERVED` | 当前文本没有给这个等价。 |
| Zeno／圆环与 fixed Cubical Agda Q 的 `TaskEquiv` | `SOURCE_UNOBSERVED` | 需要逐字段的实际过程映射。 |

## 3. 与既有 Q0／Q1／Q2 的一致性

这张卡不推翻已有研究。它再次得到同一个收紧结论：

```text
IEP 支持：ZFC-supported standard analysis 被称为 Standard Solution 的来源叙述。
IEP 不支持：用户圆环强 Done 已由极限／集合论无桥地支付。
```

这与 [ZFC-CIRCLE-Q0](../../../audit/20261003-ZFC-CIRCLE-Q0-连续统完成与圆环复原候选卡.md)、[Q1](../../../audit/20261003-ZFC-CIRCLE-Q1-元理论子理论过程边界候选卡.md) 和 [Q2](../../../audit/20261003-ZFC-HOTT-Q2-时间观察完备性比较卡.md) 的 `Q-1_SEED`／`SOURCE_BRIDGE_DEFENSE` 边界一致。它意味着：当前可以机器证明“若强 P、same actual Q 和 B 被支付会怎样”，但不能把其中任何一个外部前提伪装成已由 IEP 或 ZFC 本身给出。
