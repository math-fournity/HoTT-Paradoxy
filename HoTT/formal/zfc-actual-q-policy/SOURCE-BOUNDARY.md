# 实际来源边界：ZFC、Standard Solution 与用户的强 P

> **身份：** `SOURCE_CARD / SOURCE_BOUNDARY_CONTROL / NOT_A_KERNEL_THEOREM_OR_COMMUNITY_POLICY_CERTIFICATE`。

## 1. 可固定的来源事实

本轮重新读取的 [Internet Encyclopedia of Philosophy, “Zeno’s Paradoxes”](https://iep.utm.edu/zenos-paradoxes/) 当前版本支持以下有限事实：

| 来源段落 | 可以支持 | 不能支持 |
|---|---|---|
| §2，约 L180、L184、L289–L290 | 该文将收敛、actual infinity、连续物理路径和跑者有限时间到达目标连在一起；它明确回答“没有最后一步也能完成”。 | 用户圆环的 `OriginDone` 已获支付；一个形式极限自动证明历史／现实过程已完成。 |
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
| Standard Solution 对自身 Zeno runner task 的完成政策 | `SOURCE_ESTABLISHED_WITH_SCOPE` | IEP 直接说 runner reaches goal、有限时间完成，SEP/Norton说明其 Done 语义和范围。 |
| 数学共同体实际采用跨圆环／HoTT 的强 `MathematicalIllusionP` | `SOURCE_UNOBSERVED` | Standard Solution 的 local policy 不等同于对用户圆环和 HoTT Q 的统一 `formalDone → originDone` 政策。 |
| `A ↔ AdmittedP` | `SOURCE_UNOBSERVED` | 当前文本没有给这个等价。 |
| 严格 Zeno／圆环与 fixed Cubical Agda Q 的 `TaskEquiv` | `SOURCE_UNOBSERVED` | 这是最强反类比控制，需要逐字段的实际过程映射。 |
| Zeno→圆环／HoTT 的 `PolicyScopeWitness` | `SOURCE_UNOBSERVED` | 现有来源分别选择其完成语义，尚未说明同一个强 P 为什么跨三个任务共同适用。 |

## 3. 与既有 Q0／Q1／Q2 的一致性

这张卡不推翻已有研究。它再次得到同一个收紧结论：

```text
IEP 支持：ZFC-supported standard analysis 在其 runner task 中被用于判定到达目标。
IEP 不支持：用户圆环强 Done 或 HoTT Q 已由该局部政策无桥地支付。
```

这与 [ZFC-CIRCLE-Q0](../../../audit/20261003-ZFC-CIRCLE-Q0-连续统完成与圆环复原候选卡.md)、[Q1](../../../audit/20261003-ZFC-CIRCLE-Q1-元理论子理论过程边界候选卡.md) 和 [Q2](../../../audit/20261003-ZFC-HOTT-Q2-时间观察完备性比较卡.md) 的 `Q-1_SEED`／`SOURCE_BRIDGE_DEFENSE` 边界一致。它意味着：当前可以机器证明“若强 P、范围 witness 和 B 被支付会怎样”；严格 same actual Q 是其中一条充分控制，但不能把任何一个外部前提伪装成已由 IEP 或 ZFC 本身给出。

2026-10-04 的扩展来源分母进一步显示：Norton、SEP 与 Roberts 都公开区分 `Done_strict`／`Done_revised` 或 final-action completion／all-steps completion。IEP 同时提供 local runner-policy 的实际来源文本。这形成 `SOURCE_ZENO_POLICY_ESTABLISHED_WITH_SCOPE + SOURCE_TASK_CONTRACT_SPLIT`，仍不构成跨圆环与 HoTT 的政策范围证明。见 [芝诺来源完成政策卡](../../../audit/20261004-ZFC-ACTUAL-Q-ZENO-SOURCE-COMPLETION-CARD.md)、[P 的来源范围审计](../../../audit/20261004-ZFC-ACTUAL-Q-POLICY-SCOPE-SOURCE-DENOMINATOR.md) 与[三方完成模式卡](../../../audit/20261004-ZFC-ACTUAL-Q-TRIAD-COMPLETION-MAPPING.md)。

`C-362` 还给出一个机器化的语言边界控制：membership-only base theory 对外加 `originDone` 的真值不作判断，直到某个 specification/bridge 被支付。它不将这条一般事实归因于 ZFC 的实际实践，也不证明用户圆环 Done 在 ZFC 中不可定义；它只解释为什么来源卡必须指出那个定义或 bridge，而不能从“ZFC 能表示集合”推断它已经审查了过程完成。
