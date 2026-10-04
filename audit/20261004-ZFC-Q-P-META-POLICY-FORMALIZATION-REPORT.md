# ZFC-Q-P：社区完成政策元模型、机器证明与来源映射前沿

> **身份：** `CONTRIBUTOR_CANDIDATE_NOT_CURRENT / MACHINE_PROVED_CONDITIONAL_META_POLICY / ACTUAL_ZFC_MAPPING_OPEN`。

## 1. 这次真正形式化了什么

本次将用户的链条写成一个裸 Lean 4 元政策演算：

```text
Q-missing → permits(P) → adopts(P)
A ↔ P                  (作为显式 policy rule)
P → A ∧ B              (作为显式 policy rule)
want(A) ∧ reject(B)    (作为价值判断)
formal-incompatibility(A,B)  (只有它能导出 False)
```

其中 P 的最终工作定义是：**未验证的完成提升**。它把 formal/model completion F 当成 origin-process Done D，同时没有 source-verified、task-preserving 的 F→D bridge。它不是极限等式、实际无穷或端点的数学存在本身；这些最多是 F 的候选输入。新增的 `CompletionPromotionSite` 与 `completionPromotionP_lacks_verified_bridge` 将这个区别写进 Lean。

形式源码是 [CommunityObservationPolicy.lean](../HoTT/formal/zfc-observation-boundary/CommunityObservationPolicy.lean)，精确主张在 [claim 文件](../HoTT/formal/zfc-observation-boundary/CommunityObservationPolicy-CLAIM.md)。

形式化采取的关键翻译是：

```text
“ZFC-1 = ZFC+A = ZFC+P”
    ↓
baseZFC+A 与 baseZFC+P 在明确 A→P、P→A 规则下
具有相同的 operational consequences。
```

这比把两个实际 ZFC 公理集合写成字面相等更忠实：用户的命题涉及数学共同体的实际完成政策，而不是声称 `A` 与 `P` 是同一个 ZFC 公式。

## 2. 机器证明的七组结论

| Lean 结论 | 已形式证明的内容 | 不可外推 |
|---|---|---|
| `zfcPlusA_sameOperationalConsequences_as_zfc1` | 显式 A↔P 规则使两种 policy extension 的后果等价。 | 实际社区或实际 ZFC 有这些规则。 |
| `zfc1_derives_A_and_B` | 显式 P→A、P→B 规则给出 A 与 B 的合取后果。 | 实际 P 确实导向 A、B。 |
| `PBacktrace.exposes_P` | 若 B 的保存 provenance 是 P→B 分支，则可回溯到 P。 | 每个实际 B 都有该 provenance。 |
| `Q_absence_activates_operational_P` | 只有在缺 Q、允许 P、采纳 P 都作为字段给出时，P 被激活。 | bare ZFC 缺 Q 或实际允许 P。 |
| `admitted_P_can_be_marked_illusory` | 被采纳的 P 可与“无计算／现实 bridge”的独立 audit 并存。 | P 实际不可计算或反现实。 |
| `zfc1_produces_normative_tension` | 想要 A、拒绝 B 的 values 与 A、B derivation 形成政策张力。 | 已得到逻辑 `False`。 |
| `object_level_false_requires_formal_incompatibility` | 只有另给 A、B 正式不相容，才可以从该模型推出 `False`。 | “不想要 B”本身等于形式否定。 |

## 3. 当前能回源的部分与尚未填入 Lean 的部分

| 项 | 当前来源身份 | 可进入模型的状态 |
|---|---|---|
| A | `main` README 记录“教科书的回答是极限”，IEP 也称 Standard Solution 为被广泛接受的处理。 | `SOURCE_REPORTED_RESOLUTION_JUDGMENT`；仍须固定到底是哪一个 Zeno／圆环 Done。 |
| HoTT 数学核 | `QuestioningDelay` 的 `Q ≡ never` 是有范围、已机器检查的形式事实。 | `FORMAL_CHECKED_WITH_SCOPE`；不能自动等于 B。 |
| B | “不合理”是研究发起人的 UR 判断与项目解释。 | `USER_INTERPRETATION / NOT_YET_POLICY_CONSEQUENCE`。 |
| Q | 用户提出的“时间维度观察力不完备”候选。 | `Q_CANDIDATE_ONLY`。 |
| P | 用户提出的数学幻觉／反现实前提候选。 | `P_NOT_SOURCE_MAPPED`。 |
| A↔P | 尚无实际共同体 policy 规则。 | `A_P_EQUIVALENCE_UNPROVED`。 |
| P→B | 尚无同一任务的 provenance bridge。 | `P_TO_B_UNPROVED`。 |
| A⊥B | B 当前是“不想要”的规范性结果，不是形式否定。 | `FORMAL_INCOMPATIBILITY_NOT_ESTABLISHED`。 |

## 4. 与上一条同 Q 路线的关系

上一轮 [U6 终局](20261004-ZFC-HOTT-QPROFILE-MAPPING-U3-U4-U6-TERMINAL.md) 已经证明，不能把 IEP／SEP／Bathfield 与 `QuestioningDelay` 直接当作同一个完整 QProfile。本轮没有绕过该控制。

新模型反而把下一阶段需要的实物讲得更严：若要从“社区获得 A、又遇到 B”回溯 P，必须有实际的 `PBacktrace`，不能仅仅把两个表面相似的故事排在一起。

独立 Terra/Max 的范围审计 [H098](20261004-P-DAG-ZFC-QP-098-Terra-Max.md) 复核了同一边界：当前形式化只支持条件性政策定理，不能据此认定实际 ZFC 缺 Q、实际共同体采用 P，或已经得到对象层矛盾。

## 5. 当前最强且最诚实的表述

> 若未来来源证明：一个实际 ZFC／数学共同体完成政策因缺少 Q 而采纳 P，P 在同一 policy 中既带来 A 又带来 B，并且 B 与 A 在给定形式系统中不相容，那么 `MP-ZFC-COMMUNITY-OBSERVATION-POLICY-001` 给出从该事实链到政策张力乃至条件性 `False` 的机器检查骨架。

目前只有骨架与其所有未付输入被机器检查；实际 Q/P/A/B 映射仍是开放的来源与同一任务研究。

## 6. 实现迭代与版本边界

初稿在直接 Lean 检查时因规则构造子的无意义隐式参数、以及转换证明的变量消去写法而被拒绝；这些是形式化实现错误，不支持任何数学结论。修正为无冗余构造子并使用等式 cases 后，最终源码增加了 `PBacktrace`：只有保存了 P→B provenance，才允许把 B 回溯到 P。

最终权威运行是 `20261004-MP-ZFC-COMMUNITY-OBSERVATION-POLICY-001-05`：它包含完整的八项 claim ID、最终 P 定义／provenance 源码和用户原文链接，Lean 4.34.1 exit 0，十一个打印定理均报告不依赖公理。此前 `-01` 是不含 provenance 增量的有效早期源码快照，`-02`／`-03`是源码已补 provenance 后、但 capture claim list 尚未补足的有效检查快照，`-04`是 P 定义细化前的完整 claim-ID 快照；它们均保留为历史运行。
