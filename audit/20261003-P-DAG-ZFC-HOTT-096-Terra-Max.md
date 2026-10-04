# P-DAG H096：HoTT `QuestioningDelay` 的 QProfile／Done 字段核证

> **身份：** `CONTRIBUTOR_CANDIDATE_NOT_CURRENT / U2_HOTT_CLAIM_FIELD_MAP / SOURCE_MATCH_WITH_TRAJECTORY_RECEIPT / NO_SOURCE_LEVEL_JUDGMENT / NOT_A_ZFC_OR_HOTT_INCONSISTENCY_VERDICT`。

## 1. 节点、输入与运行边界

| 项 | 值 |
|---|---|
| `node_id` | `P-DAG-H096-HOTT-QPROFILE-DONE-FIELD-MAP` |
| 上游 | U0 common assessment candidate；U1 Zeno field map。 |
| task | 只映射 `QuestioningDelay` 形式程序、其解释边界与 H085/KLV scope control。 |
| actor | `gpt-5.6-terra / max`，`source-match`。 |
| 权限 | `governance-regression-fresh`／`approvalPolicy=never`；无 tools、files、web、Git、delegation。 |
| 冻结输入 | [NodeCard](audit/20261003-P-DAG-ZFC-HOTT-096-NODECARD.md) 与 [payload](audit/20261003-P-DAG-ZFC-HOTT-096-PROMPT.md)。 |
| private run | `H096-HOTT-QPROFILE-DONE-FIELD-MAP-20261003`；私有 wire 不进入 Git。 |

行为 receipt：终态 `PASS`，elapsed `70.051s`，`command=0`、`file_change=0`、`approval_request=0`，最终 717 words、E0–E7 完整；thread `01a1050f-2d55-7c62-a021-d2c06077ac26`，turn `01a1050f-2e65-7b13-bf4e-d289e64dac90`。

## 2. TrajectoryReceipt

canonical `session_trajectory.py` 的 `catalog → tree → search → coverage` 确认 private bidirectional App Server wire（454,390 bytes），一 thread、一 completed turn、1,224 个 transport events、零 tool calls。`commandExecution|fileChange|approval` 搜索为零命中。

| 层 | 判词 | 边界 |
|---|---|---|
| L1 | `PASS` | 从 payload 重建的冻结文本 3,717 chars 全量出现在 user input；SHA-256 `a3461796ef821dbc66ef902be9d29e4585df8bb88d20db1a81401ab30b49d14c`。 |
| L2 | `NOT_OBSERVED_EXPECTED` | 节点按合同无工具、无 selected read。 |
| L3 | `NOT_TESTED` | 不是独立 recall 测试。 |
| L4 | `MASTER_REVIEWED_WITH_SCOPE` | 可见结果遵守 formal theorem／interpretation／model scope 的三层区分；reasoning 仅有 Host summary，不作为隐藏推理证据。 |
| L5 | `PASS_WITH_SCOPE` | exact model/effort、输入 gate、E0–E7、零副作用通过；不认证字段结论为数学定理。 |

和 H095 一样，`PERSISTED_ROLLOUT_UNAVAILABLE / BIDIRECTIONAL_APP_SERVER_WIRE_AVAILABLE`；不能因没有 rollout 把该节点说成没有轨迹。

## 3. Worker 映射及 Master 复核

worker 的 E6 为 `no source-level judgment`。它准确拒绝了三种越级：

1. 不把 `Q ≡ never` 写成现实墙钟时间或 HoTT 不一致；
2. 不把 `C-79`／`C-80` 的控制说成对同一原任务的 `revisedResolved`；
3. 不把 H085/KLV 未承诺 `Done_origin` 的范围边界伪写成一笔未支付的 bridge 债。

Master 用 [QuestioningDelay claim record](HoTT/formal/claude-cg001/questioning-delay/CLAIM.md)、[社区审计稿 03](docs/社区审计提交/03-HoTT的芝诺.md)、[C-77–C-83 evidence index](.claude/goals/CG-001-targeted-overview/证据索引.md) 和 [H085](audit/20261003-P-DAG-ZFC-HOTT-085-Terra-Max.md) 复核后同意这一范围判断。

形式上已被内核检查的是：对指定 `Judge`、`Delay` 与 `runFor` 语义，`QuestioningDelay` 在 Cubical `Type ℓ-zero` 上等于 `never`，任意有限燃料都没有答案；有界 h-level 目录及 Lean 的命题式相等控制会按其指定语义停下。这是一个关于**指定程序和指定形式对象**的数学结果。

形式包自己写明：把“对哪一层落定的追问”读作现实／存在性／日常同一性过程，需要 interpretation bridge 和 reality-side premise。社区稿也把 UR 的“不合理”留作研究发起人的判断，并公开要求审计其任务映射。H085 的 ZFC-relative model 来源只完成模型／相对一致性层的任务，没有声称完成这个起源过程。

## 4. H096 的正确保留结论

```text
FORMAL_Q_NEVER_SOURCE_SUPPORTED
FINITE_FUEL_AND_CONTROL_OUTCOMES_SOURCE_SUPPORTED
FORMAL_Q_TO_DONE_ORIGIN_BRIDGE_NOT_PAID
H085_MODEL_DONE_IS_A_DIFFERENT_DECLARED_DONE
NO_SOURCE_LEVEL_originalResolved_FOR_DONE_ORIGIN
NO_SOURCE_LEVEL_revisedResolved_FOR_DONE_ORIGIN
NO_SOURCE_LEVEL_bridgeRequired_FOR_DONE_ORIGIN
NO_SOURCE_CONFLICT_ON_ONE_IDENTICAL_DONE_ORIGIN
```

`bridgeRequired` 在这里不能仅凭“bridge 缺失”获得：该标签要求来源先承诺其 formal result 已经要交付 `Done_origin`。H096 的来源没有作出这个承诺。因此它是一个重要的防假阳性控制，而不是对用户的 UR 读法的否定。

## 5. 对 U2/U3 的约束

若将来有来源明说“`QuestioningDelay` 的 `Q ≡ never` 正在回答日常／现实同一性何时完成”，却未交出保真 bridge，才可把 HoTT 站点标为 `bridgeRequired`。若来源交出同一任务的 bridge 和现实前提，才可评估是否 `originalResolved`。当前材料两者都没有，U3 不得把 `no source-level judgment` 偷换为 `bridgeRequired`。
