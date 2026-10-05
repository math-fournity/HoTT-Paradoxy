# C2A：FOTG 几何级数候选的原任务保真审计

> **身份：** `CORE_ADEQUACY_TASK_CARD / C2_TASK_FIDELITY_AUDIT / SOURCE_COMPONENT_MATCH / FULL_Q_UNPAID`。
>
> **父卡：** [C1B Mizar geometric source-to-spec card](20261005-ZFC-META-SUBTHEORY-ADEQUACY-C1B-MIZAR-GEOMETRIC-SOURCE-TO-SPEC-CARD.md)。

## 1. 要审计的两个任务

| Q 的字段 | IEP Standard Solution 的 runner task | Mizar `SERIES_1` 的几何级数 theorem | 判词 |
|---|---|---|---|
| 输入 | runner、goal／tortoise、physical path、time、positive finite speed；subpaths (d_1,d_2,ldots)。 | real (a)、real sequence、partial sums。 | 不是同一输入域。 |
| 操作 | 在连续时空中以速度移动；actual infinity of non-overlapping subpaths。 | 对 `a GeoSeq` 的 partial sums、convergence 和 `Sum` 做实分析推理。 | 级数是模型组件，运动操作未被该 theorem 表示。 |
| 观察 | runner reaches/overtakes goal in finite time；finite distance／time；path与time是linear continuum。 | `Partial_Sums` 按公式趋近，`Sum(a GeoSeq)=1/(1-a)`。 | finite-sum observation可对应；arrival/time/path observation缺失。 |
| 完成 | IEP 的 Standard Solution 称目标仍可达到，且明确不接受“必须有最后 step”的要求。 | sequence summable、有有限 sum。 | `FormalDone_component` 有；`OriginDone` 未由 theorem 给出。 |

IEP 的冻结 HTML 原件把这些层同时写出：

- 第 303 行：runner path 是 physical continuum，在 positive finite speed 下完成；速度是距离对时间的 derivative。
- 第 317 行：(1/2+1/4+1/8+cdots) 的 partial sums 渐近有限值，并特别说这不要求有人进行无限时间的手工加法。
- 第 354–359 行：Dichotomy runner 的 (1/2,1/4,1/8,ldots) 子路径；标准解法说级数和为 1，最后 step 直觉被拒绝。

Mizar `SERIES_1:Th22/Th24` 精确支付中间的几何 partial-sum relation。C-361 在 Lean/Mathlib 中重新运行通过，独立核对了相同 (s_n=1-2^{-n}) 的极限结论与“无有限自然数 stage 已到 1”；它还给闭实数时间端点到达正控制。

## 2. C2 判词

```text
GEOMETRIC_SERIES_COMPONENT_MATCHED
RUNNER_TRAJECTORY_TIME_OPERATION_UNMAPPED
ORIGINAL_DONE_NOT_IDENTIFIED_WITH_SERIES_DONE
FULL_Q_TASK_FIDELITY_UNPAID
```

因此这条候选已足以用于下一阶段的 **P component** 与 **Bridge** 审计，但不足以说 Mizar theorem 本身解答、反驳或重述了完整芝诺任务。

## 3. 它如何约束 C3/C4

IEP 的确给出 `P_component`：有限几何和被用于说明 finite distance，继而称 runner 可以完成；这不是 AI 杜撰的 promotion。

但这一 promotion 还依赖 IEP 同页的连续 path、time、speed、derivative 与 point-event 模型。Mizar `Th22/Th24` 没有这些字段。故：

```text
P_component exists
≠
ActualPromotion : FormalDone_full → OriginDone_full
```

既有 Norton source card进一步给出一个独立控制：Standard Solution 对“需要最后 step”明确回答否，因而严格 Done 的 bridge没有被支付。C2A 不把这一点升级成“连续端点必然不能到达”；C-361的闭时间端点正控制正排除了这个错误外推。

## 4. 反证与后继

**可推翻本卡的材料：** 一份版本固定的源或经可重放形式化，逐字段给出 runner trajectory/time/speed 到 series 的解释，并证明该解释同时保持观察和 `OriginDone`，而不是只保留总和。

**下一项最小行动：** `C3A-FOTG-GEOMETRIC-PROMOTION-AND-BRIDGE`。它将 IEP 的 promotion 原句、Norton 的 explicit task switch 与 C-361/C-362 controls 放进一张 source-to-spec 表，问此 FOTG candidate 是否有 full promotion，还是只是一项 component promotion；如果后者，登记 `FULL_PROMOTION_UNPAID` 并转向其他 `F-A/F-B` 候选或 F-C adequacy source。

这张卡不作 bare ZFC 数学结论，也不宣称芝诺、圆环、HoTT H0已经是同一完整 Q。
