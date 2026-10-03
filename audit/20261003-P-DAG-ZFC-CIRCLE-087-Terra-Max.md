# P-DAG H087：IEP 的 ZFC—实分析—芝诺 Standard Solution 来源审计

> **身份：** `CONTRIBUTOR_CANDIDATE_NOT_CURRENT / ACTUAL_C_LANE_SOURCE / MODEL_BRIDGE_PARTIAL_PAYMENT / Q_BRIDGE_CANDIDATE / SUPERSEDED_ON_EXPLICIT_DONE_FIELD_BY_H091 / NOT_A_ZFC_INCONSISTENCY_OR_FINAL_Q`。
>
> **节点：** `P-DAG-SOURCE-087-ZFC-CIRCLE-IEP-STANDARD-SOLUTION-LIFT`。
>
> **来源：** [Internet Encyclopedia of Philosophy, “Zeno’s Paradoxes”](https://iep.utm.edu/zenos-paradoxes/)，accessed 2026-10-03。

## 1. 为什么 H087 改变了研究状态

此前 H083 的 SEP *Supertasks* 虽有 Achilles completion claim，却没有把 ZFC 本身作为基础层消费者。IEP 的 Standard Solution 段落第一次给出同一来源内的完整候选链：

```text
ZFC with Choice（来源称为实分析的多数基础）
  → 标准实分析／微积分、实数连续统
  → 连续时间与位置的运动模型
  → Achilles 在有限时间内到达目标、芝诺获得间接解决
```

IEP同时说：连续运动以实数时间到实数位置的函数建模，位置函数应连续、通常可微；真实分析和微积分在物理科学的时间和运动处理中成功；Standard Solution 的倡导者认为 Achilles 可以在有限时间内穿越实际无穷多个子路径。它还将 ZFC-with-Choice描述为实分析的多数基础，并说该基础“indirectly resolves”Zeno。

这使“是否有实际 `C/I/O/Done` consumer”不再是空缺。问题转为：这条链的模型付款是否保持了用户所问的原过程完成条件。

## 2. H087 的冻结分析与初步判词

| 桥字段 | IEP 在 H087 冻结摘录中实际给出 | 当时仍未从摘录得到 |
|---|---|---|
| `Representation` | 实数时间、实数位置、线性连续统、连续／可微运动。 | 具体原跑步任务到模型的明示表示关系。 |
| `Operation` | 微积分、实际无穷子路径在有限时间的处理。 | 哪一个端点／完成谓词是该任务的操作性判据。 |
| `Observation` | 有限时间、无穷路径、连续统、物理科学使用。 | 区分到达和相关未完成状态的明确观察规则。 |
| `Done` | 该来源声称 Achilles 到达目标、问题获得解决。 | 摘录中尚未出现“无最后一步”如何改变Done的全文段落。 |
| `Payment` | 连续模型、ZFC基础、数学物理成功、承认争议。 | 同一原任务的Done保持定理／契约。 |

Terra/Max 的公开 MatchTrace 因而给出：P1有真实`C/I/O/Done`，P2不适用，P3-C是**模型付款但未给明示相同任务Done保持**。它没有把模型付款误说成 ZFC 定理，也没有把来源的“间接解决”误说成形式矛盾。

## 3. 这个初判为什么必须被 H091 修正

H087只使用了窄摘录。随后直接读同页的相关段落，发现 IEP 明说：面对“没有最后一步，旅行如何完成”，Standard Solution 的回答是**旅行不需要最后一步**，并把反对这一点的直觉列为接受 Standard Solution 必须放弃的代价。

因此本报告的“未发现明示Done条款”只对 H087 冻结摘录成立，不能作为整个 IEP 页面的结论。H091是这份来源的有效Done-field修正：IEP不是完全没有支付，它**显式替换／改写**了最后一步完成条件；它仍没有证明这个被改写的条件与研究发起人固定的强`Done_origin`是同一条件。

## 4. TrajectoryReceipt

private direct App Server wire经canonical `session_trajectory.py`的`catalog → tree → search → coverage`审读：一个session、一个turn、1390事件、正常`completed`。exact model/effort、`approvalPolicy=never`、permission profile、prompt-input gate和零副作用均由runner收据记录。

| 层 | 判词 | 范围 |
|---|---|---|
| L1 | `NOT_FULLY_CERTIFIED` | 隔离runner的prompt-input gate确认冻结payload；wire没有完整AGENTS正文，不能声称完整指令注入已由trajectory正文证明。 |
| L2 | `NOT_OBSERVED_EXPECTED` | source-match禁止tool；runner与trajectory search均为零command/file/approval。 |
| L3 | `NOT_TESTED` | 不是fresh recall节点。 |
| L4 | `MASTER_REVIEWED_WITH_SCOPE` | 输出保持ZFC foundation/context与过程解释的分层，未伪造P2或形式矛盾。 |
| L5 | `NODE_ACCEPTED_WITH_SCOPE` | 只接受该窄摘录的来源匹配；H091已改变其Done字段的可用范围。 |

## 5. H087 的可保留结论

H087保留一项重要正结果：**确有一个权威参考来源将 ZFC-supported real analysis、连续运动模型、标准解和 Achilles 的到达声明连在同一条来源链中。**这意味着后续研究不再只是在理论外部猜测“ZFC是否为极限理论放行”；它能审一个真实消费者。

但此来源的最后结论只能与 H091 合并后使用：`SOURCE_DONE_REPLACEMENT_EXPLICIT / PAYMENT_PARTIAL / SAME_TASK_IDENTITY_NOT_PROVED`。它还不是 ZFC 的形式问题，更不是已完成的 Q。
