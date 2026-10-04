# ZFC-QP-ACTUAL-MAPPING-SOP：M6 的来源收敛——SEP 纠正与 UOU 候选入口

> **身份：** `CONTRIBUTOR_CANDIDATE_NOT_CURRENT / ZFC_PROBLEM_CONVERGENCE_PHASE / SOURCE_CARD_COMPLETENESS_CONTROL / ACTUAL_P_CANDIDATE_SOURCE_MAPPED_WITH_SCOPE`。

## 1. SEP 不是实际未验证 P 的来源实例

H103 的窄卡保留了真实的来源形状：

```text
F = 1/2 + 1/4 + 1/8 + ... 在标准实数拓扑下收敛到 1
D = Achilles 完成全部 supertask steps
promotionClaim = “From this perspective, Achilles actually does complete all
                 of the supertask steps in the limit ...”
```

它准确说明 SEP 确有 completion claim，而非仅有一条极限方程。但 H083 已经审到
同一段落的完整关键上下文：SEP 把 `every-step` 与 `final-action` 明确分开，只肯定
前者，并保留标准拓扑是否适当的疑问。于是 H103 中“冻结卡没有形式定理”的事实，
不能转写成“完整来源没有 payment”。完整来源的可用结论是：

```text
SEP = SOURCE_TASK_CONTRACT_SPLIT_CONTROL
not an actual unverified F -> user-origin-D promotion
```

H103 保留为 `SOURCE_CARD_COMPLETENESS_FAILURE_REPAIRED`。它证明 M6 必须使用足以
判断 source payment 的完整卡，不能把“没有形式定理”误报为“没有来源 payment”。

## 2. H103 的机器检查仍准确，但只检查窄卡标签

[MP-SEP-COMPLETION-PROMOTION-SOURCE-001](../HoTT/formal/zfc-observation-boundary/SepCompletionPromotion-CLAIM.md)
把 H103 的冻结 source card 编码为有限分类数据，并由 Lean 4.34.1 以无公理证明：F、
promotion 和 named D 在**窄卡**中出现；窄卡将 bridge 标签记作 `notSupplied`；
final-action completion 被排除。运行收据为
[SEP-P-SOURCE-001](../HoTT/verification/runs/20261004-MP-SEP-COMPLETION-PROMOTION-SOURCE-001-01/RUN.json)。

这验证的是窄卡标签分类，不能证明 SEP 数学真理、物理运动、完整来源的 payment 状态或
ZFC 定理，也不能推翻 H083 的完整来源控制。

## 3. 新的实际来源候选：UOU《Real Analysis》

Uttarakhand Open University 的课程文本 *Real Analysis*，MT(N)-201 §5.1–§5.3（PDF
物理第 75–76 页，SHA-256 `e8c3e3bb4867b3547f3174f5623d75ea401362ca6f338d195e3723874f4b833b`）
明确把“无穷项级数有有限和”说成 Achilles/tortoise 悖论的解决，并说该有限和给出
Achilles 追上乌龟所需的时间；邻接的 §5.3 又明说不能按通常方式把无限项逐一相加，
并把 series sum 定义为 partial sums 的极限。该来源付清了 F 的数学定义，仍没有
SEP/Norton 式 Done 区分或 task-preserving F→D bridge。H104/H105 已以只读 Terra/Max
source-match、Master 原文复核和 Lean 窄卡分类完成；H106 再以 SEP 的显式 Done
分叉作为 Battle control，裁定 `P_CANDIDATE_UPHELD`：UOU 付清 formal F 的数学定义，
没有付清 F→source-process D 的 task-preserving bridge：

```text
F = infinite series has a finite sum / limit
D = Achilles catches up; the paradox is resolved
promotion = finite sum supplies the time necessary for catch-up
bridge = not supplied on the frozen card
```

它已成为 M6 的第一张实际课程文本候选卡：
`ACTUAL_P_CANDIDATE_CONFIRMED / P_CANDIDATE_UPHELD`。该状态只说该来源卡的 F/D/promotion/bridge
字段齐备；不能单独证明 bare ZFC 采纳 P、ZFC 缺 Q、HoTT B 来自 P，或任何对象层矛盾。

## 4. 收敛线尚待闭合的短链

| 义务 | 当前状态 |
|---|---|
| 实际 ZFC 自身缺 Q | 未来源化。 |
| UOU D 与用户芝诺／圆环 D 同一 | 未证明。 |
| P 到 HoTT B 的 PBacktrace | 未建立。 |
| A 与 B 的形式不相容 | 未建立。 |

这些义务不会让研究回到无边界搜索。它们正是收尾的短链：固定真实来源的
F/D/promotion，再逐项审 Done、bridge、Q 与 H0 provenance。

## 5. M7：实际政策见证与来源前沿

H107–H110 已将这四条短链逐项核证：

| `ActualPolicyWitness` 字段 | H 节点 | 当前 verdict |
|---|---|---|
| `SourceToPolicyBridge` | H107 | `FOUNDATION_SCOPE_NOT_ADOPTION_BRIDGE`。 |
| `QObservationBridge` | H108 | `SOURCE_Q_OBSERVATION_GAP_CANDIDATE`，不是 bare-ZFC 缺 Q。 |
| `PBacktraceBridge` | H109 | `PBACKTRACE_NOT_SOURCE_MAPPED`。 |
| `TruthAdequacyBridge` | H110 | `NORMATIVE_TENSION_SOURCE_MAPPED`，不是 `¬(A∧B)`。 |

`MP-ZFC-ACTUAL-POLICY-WITNESS-001` 规定只有五字段均经来源填充时，条件性政策归谬才可
推出 `False`；`MP-ZFC-ACTUAL-POLICY-FRONTIER-001` 则以内核检查确认目前 H104–H110 的有限分母不能
构造这个 witness。详见 [实际政策见证与有限来源前沿](20261004-ZFC-QP-ACTUAL-POLICY-WITNESS-FRONTIER.md)。

因此 M6/M7 的当前状态为：

```text
ACTUAL_P_CANDIDATE_CONFIRMED_WITH_SCOPE
+ EVIDENCE_FRONTIER_REACHED_WITH_SCOPE
+ NO_ACTUAL_ZFC_Q_OR_INCONSISTENCY_VERDICT
```

## 6. 收敛后的下一动作

以 H105 的 full-card UOU 结果为 anchor，随后只寻找：

1. 同一 UOU source 或其定义段是否给出或否认 F→D 的 bridge；
2. 相同 promotion 形式是否出现在圆环的具体 D；
3. HoTT 的 H0 是否能给出同一个 promotion 的 B provenance。

这是一条狭窄的验证线，不再是无边界的 ZFC 搜索。若新来源不能填 M7 的 adoption、actual-Q、
PBacktrace、formal-incompatibility 或 UOU bridge 字段，按 `TOOL_ONLY_DRIFT` 停止。
