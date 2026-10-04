# ZFC-HOTT-Q-UNIFORMITY-SOP U0：共同完成授权状态与初始 QProfile 映射卡

> **身份：** `CONTRIBUTOR_CANDIDATE_NOT_CURRENT / U0_FROZEN_CONTRACT / COMMON_ASSESSMENT_STATE_CANDIDATE / ORIGINAL_PROCESS_STATE_NOT_YET_IDENTIFIED`。

## 1. 本轮共同候选任务 `u`

本轮不把芝诺的运动过程与 HoTT 的逐层相同追问强行说成同一个对象过程。能由当前材料共同化的任务是更高一层的完成授权问题：

```text
u_assess = 当一个理论／基础框架取得 formal 或 model 输出时，
           它是否有资格把该输出交付为某个原过程任务已经完成？
```

相应的候选状态形状是：

```text
AssessmentState =
  (TheoryContext, ProcessTask, Formalization, FormalOutput,
   Done_formal, Done_origin, SourceJudgment, BridgeEvidence)
```

这只是`COMMON_ASSESSMENT_STATE_CANDIDATE`。它不是“芝诺跑步 = HoTT 宇宙追问”的同一性断言；之后必须证明两站点各自的`ProcessTask`、`Done`和`BridgeEvidence`能被这同一评估任务忠实承接。

## 2. 冻结来源分母

| 站点 | 冻结直接材料 | 角色 |
|---|---|---|
| Zeno | IEP *Zeno’s Paradoxes*（Standard Solution、无最后一步、ZFC基础语境）；SEP *Supertasks*；Bathfield 2018 pp.12–13 | 原过程、数学模型、修订Done和独立批评的来源分母。 |
| HoTT | `docs/社区审计提交/03-HoTT的芝诺.md`；`QuestioningDelay` C-77–C-80；C-81–C-83对照；KLV H085 | 内部程序、用户UR解释、对照、以及ZFC-relative模型范围控制。 |
| Meta | `MP-ZFC-META-OBSERVATION-CONSISTENCY-001` | 条件性O1–O5/QProfile政策定理；不是实际映射证据。 |

## 3. 初始字段卡

| 字段 | Zeno 站点 | HoTT 站点 | 当前证据身份 |
|---|---|---|---|
| `TheoryContext` | IEP 把ZFC-with-Choice列为实分析的多数基础；Standard Solution使用连续时间、位置、微积分。 | Cubical Agda 的类型理论与QuestioningDelay；KLV仅给`ZFC + 两个不可达基数`相对模型控制。 | `SOURCE_SUPPORTED`，但两个理论上下文不相同。 |
| `ProcessTask` | 连续／顺序运动中的到达与“有没有最后一步”。 | “两个东西以什么方式相同”是否在有限层了结的追问。 | `SOURCE_SUPPORTED`为各自任务；跨站同一性`UNKNOWN`。 |
| `Formalization` | 级数、实数连续统、连续位置模型。 | `Delay`追问程序、h-level、universe／product／truncation。 | `SOURCE_SUPPORTED`。 |
| `Done_formal` | 级数收敛、有限时长或连续模型的到达。 | `Q ≡ never`／有限燃料无输出；有界目录停止。 | `SOURCE_SUPPORTED`，但输出形状不同。 |
| `Done_origin` | 用户所审的原顺序过程完成；IEP改写为“不需最后一步”的完成。 | 用户UR中的“是不是同一个，本来一句话的事”得到了结。 | `CANDIDATE_INTERPRETATION`。 |
| `Judgment` | IEP完整语境最接近`revisedResolved`；Bathfield提出顺序任务批评。 | 用户／项目读法提出`bridgeRequired`候选；没有ZFC来源将此任务正式判为`bridgeRequired`。 | `SOURCE_SUPPORTED`与`CANDIDATE_INTERPRETATION`混合，不能比较为相反源级判词。 |
| `requiresBridge` | `true`候选：连续／极限模型与原顺序Done之间需桥。 | `true`候选：内部never与现实／同一任务解释之间需桥。 | 两侧均为`CANDIDATE_INTERPRETATION`，未获相等证明。 |
| `bridgePaid` | IEP有模型付款与Done改写；共同任务保持未见。 | `QuestioningDelay`的解释bridge不是定理；KLV不承担`Done_H`。 | `PARTIAL/UNKNOWN`与`NOT_PAID_BY_CURRENT_SOURCE`，不相等。 |
| `originalTaskPreserved` | IEP未给连续Done与顺序Done的共同State等价。 | HoTT程序到UR原任务不是内核定理。 | 两侧`UNKNOWN`，未知相同不构成相等证据。 |
| O1/O2 | 明确有。 | 明确有程序、层级和有界正控制。 | 可比较为“形式资源存在”，不等于完整profile。 |
| O3/O4/O5 | O3有来源内Done替换；O4/O5未见共同任务验证／元审查责任。 | O3有程序与解释边界的分层；O4/O5未由ZFC来源承担。 | `PROFILE_MATCH_NOT_YET_PROVED`。 |

## 4. U0 判词

```text
COMMON_ASSESSMENT_STATE_CANDIDATE
ORIGINAL_PROCESS_STATE_NOT_YET_IDENTIFIED
PROFILE_MATCH_NOT_YET_PROVED
NO_ACTUAL_OPPOSITE_SOURCE_JUDGMENTS
```

这张卡完成U0，但没有完成U1–U5。它把下一步缩成三个可证伪问题：

1. IEP的“解决芝诺”究竟是不是对原`Done_origin`的`originalResolved`，还是对明确修订后的`revisedResolved`？
2. HoTT的内部`never`证据能否由一个来源定义的共同过程桥提升为`bridgeRequired`判词，而不是仅有用户／项目解释？
3. 两种原过程能否由同一`AssessmentState`保存对象、操作、观察和Done，或是否有一个字段被来源证实不同？

下一自然单元必须从U1和U2的source-field map开始；不能直接进入U5。
