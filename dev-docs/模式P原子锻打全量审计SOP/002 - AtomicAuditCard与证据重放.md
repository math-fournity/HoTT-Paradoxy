<!-- governance-shard:v2
logical_id: PATTERN_P_FORGE_ATOMIC_AUDIT_SOP
shard_id: 002
index: ../模式P原子锻打全量审计SOP.md
-->

# AtomicAuditCard与证据重放

## 1. 一张卡的最低内容

每个 `D_atomic` 成员必须恰有一张 `AtomicAuditCard`。卡的书写是来源受限的兵棋推演，不是对旧文字的润色。
至少保留以下字段：

```text
atomic_id / unit_kind / parent coarse unit / chronological position
raw identity: H number, session/thread/turn, source hash, 或 no-ID identity rationale
evidence locators / source layer / sampling_state / visible permissions and inputs
as-run P specification and Q state before
actual action / actual output or failure / actual state change
as-run QConvergenceLink verdict / same-task evidence / falsifier
counterfactual under the current P-FORGE contract
alignment and deviation classification / affected later units
Wealth: HYPOTHESIS | READY_FOR_FORGE_INTENT | REJECTED, plus no-auto-start boundary
card status / reopen trigger / verification and exact Git commit
```

`parent coarse unit` 仅帮助把原子卡回接 R01--R13；它不能让一个父单元的判词覆盖任何未审子项。没有
`QConvergenceLink` 的历史单位也必须被审：卡要如实写明当时没有这个字段，再判断它是后来补上的规格缺口、
可指向固定卡的安全修复，还是脱离 Q 的工具漂移。

## 2. 当时态重放与当前合同的反事实

每张卡必须有两个明确分栏：

| 分栏 | 问题 | 禁止事项 |
|---|---|---|
| `AS_RUN` | 在该单位发生时，实际可见的 P 规格、输入、来源、Q 状态、输出和终态是什么？ | 不用后来的修复填空，不把后来规则写成旧运行已经满足 |
| `CURRENT_CONTRACT_COUNTERFACTUAL` | 按当前 P-FORGE 与三刀合同重新执行，它需要补什么字段、控制或来源？结果会怎样被分类？ | 不把反事实当成历史事实，也不重写原始收据 |

这种分栏正是“锻刀与找 Q 是同一过程”的审计方法：一方面保留某次当时的真实 P/Q 成熟度，另一方面问清楚
后来锻出的刀为何会拒绝、校正或重开该单位。二者不同不是失败；它可能是 `IDEA_SPEC_INCOMPLETE` 或
`EXECUTION_DEVIATION` 的证据。

## 3. P/Q 判词

每张卡须为 `AS_RUN` 和必要时的当前反事实分别选择下列之一，并给出具体字段与同一任务证据：

| 判词 | 含义 |
|---|---|
| `Q_GENERATE` | 在固定对象／formation 上首次产生可审的 Candidate-Q 或其片段。 |
| `Q_NARROW` | 来源、guard 或反控制有界排除一个候选或候选族。 |
| `Q_BRIDGE` | P2 或 P3 在同一冻结卡上补出受来源支持的 bridge、reentry 或 admission 片段。 |
| `Q_CONVERGE` | 三刀在同一 `T/u/F/C/Q/I/O/Done` 会合；它仍不是数学矛盾结论。 |
| `Q_REJECT` | 当前来源在限定范围内直接支付、阻断或正常完成候选。 |
| `Q_CAPABILITY_CALIBRATION` | 成对 fixture 校准可供下一真实卡使用的 P 字段；不推进任何理论卡。 |
| `Q_SAFETY_REPAIR` | 修复明确保护一张已冻结卡免于误报的运行、字段或证据问题。 |
| `TOOL_ONLY_DRIFT` | 没有 Q 状态／候选空间变化，也不能保护固定卡；不能算作 P-FORGE 发现推进。 |
| `Q_STATUS_UNINFERABLE_FROM_EVIDENCE` | 证据不足以诚实分类；记录缺口，不从沉默推出负结论。 |

一个 `Q_NARROW` 或 `Q_REJECT` 是有价值的，只要它明确缩小了同一候选空间。一个长报告、一次模型回答、一个
Git commit 或一个新字段本身不是 Q 增量。

## 4. 公开 evidence 与 trajectory 纪律

有 App Server 或其它可审计 session 的单位，先建立 `TrajectoryReceipt`：

```text
catalog → tree → filtered scan/search → necessary inspect/context → coverage
```

卡中记录 source view、session/thread/turn、prompt/source/output、工具与审批、终态、private extract mode，以及
L1--L5 层的可见事实。没有 persisted rollout 时如实写
`PERSISTED_ROLLOUT_UNAVAILABLE / BIDIRECTIONAL_APP_SERVER_WIRE_AVAILABLE`；不可从最终回答倒推被隐藏的推理。
Host 仅暴露 summary 时，summary 是可审证据，reasoning 仍为 `OPAQUE/UNAVAILABLE`。

非 session 的早期记录同样需要公开证据链：原报告、明确输入、可见输出、Git 时间线与其无法提供的 identity。
缺一个关键证据时，卡的结论为 `EVIDENCE_INSUFFICIENT_WITH_SCOPE`，不靠模型常识、后续叙述或多数意见补齐。

## 5. 偏差、财富与重开

每张卡只可使用以下偏差分类：

```text
ALIGNED
EXPECTED_CALIBRATION_FAILURE
IDEA_SPEC_INCOMPLETE
EXECUTION_DEVIATION
RUNNER_OR_EVIDENCE_FAILURE
ORIGINAL_IDEA_CHALLENGED
```

最后一项必须逐字指向原初用户主张、同一任务的直接反例，并排除规格或运行解释。普通的模型未命中、超时、
来源缺口或 Q 被 guard 支付，都不构成对原初理念的反例。

`Wealth` 是把每张兵棋推演留下的未来探索价值显式保存下来的字段：

| 状态 | 允许含义 |
|---|---|
| `HYPOTHESIS` | 一个可回源的思路，但尚不能构成 ForgeIntent。 |
| `READY_FOR_FORGE_INTENT` | 已有同一任务、候选、证据缺口和最小控制，可供研究发起人另行决定是否启动。 |
| `REJECTED` | 被同一任务来源或反控制有界关闭。 |

财富不会自动启动 worker、网络、Battle、新刀或目标切换。卡的 `reopen_trigger` 必须具体，例如新的一手 source、
identity 去重反证、相同任务 consumer、或直接推翻本卡 source fact 的证据。
