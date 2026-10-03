<!-- governance-shard:v2
logical_id: P_FORGE_ATOMIC_AUDIT_CAMPAIGN
shard_id: 129
index: ../20261003-P-FORGE-ATOMIC-AUDIT.md
-->

# N33 校准来源层与站位Master修订

> **AtomicAuditCard：** `N33 / NON_H_MASTER_DECISION / R13_CAL_SOURCE_LAYER_STATION_REPAIR / ATOMIC_AUDIT_COMPLETE_WITH_SCOPE`。

N33 是一次可核查的 Master 方法决定，而不是 worker 运行或数学来源。Git commit `f51a205a` 在 H074/H075 已有的
reflection 控制之后，新增 `PCalibrationConvergenceCard`、`SourceLayerCoverageMatrix` 和 Power Set station 状态机，
用来阻止三种误报：把已知 fixture 当作新发现、把 proof/formalization layer 当作语义或数学实践、把 Round stop 当作
自动换站。它直接改变 P/Q 的准入与停止语义，故属于原子分母；其本身只保护固定卡的分类，不生成 ZFC Candidate-Q。

## 1. 身份、证据与当时态

| 字段 | 记录 |
|---|---|
| `atomic_id / parent` | `N33 / R13`。 |
| unit kind | `NON_H_MASTER_DECISION`；没有 session、thread、turn、模型输出、工具调用或隐藏推理可供读取。 |
| raw identity | `f51a205a4c87a84a0b6a87e41f3c3eb98519d82d`，`research: tighten P calibration and station controls`，author/commit time `2026-10-03 02:33:16 -0400`。 |
| 直接 evidence | 该commit新增 [校准／来源层／站位调整审计](<../20261003-P-FORGE-CALIBRATION-STATION-ADJUSTMENT.md>) 和三刀013，并修订 P-FORGE SOP、Feature 与 rulings。原 commit diff固定了这一次决策，而后续文件只用于消费证据。 |
| 实际修订 | `CAL-0..4` 分开输入完整性、已知控制、独立接口、来源存活 prospective Q 与同卡会合；`L-A..L-E` 分开规则、proof/formalization、model/semantic、mathematical practice 与 construction bridge；`S1..S5` 分开 Round stop 与站位退出审查。 |
| 当时保护对象 | H074/H075 reflection chain、Power Set `Q-0 UNFORMED`、以及“proof layer／station状态不能冒充Theory-Q”的固定风险。 |

## 2. `AS_RUN`：改变分类合同，不改变理论 Q

N33的直接 source audit 已将 H074/H075 读取为：H074是独立 interface 的 blind site，H075在 Isabelle/ZF proof-theory
source中以 theorem/proof Done 直接支付该 reflection task。N33由此把其身份固定为：

```text
Target-Q (as run)    = 防止已有控制被错写成来源存活的理论 Candidate-Q 或站位转换
Candidate-Q (as run) = NONE
Control-Q (as run)   = H074/H075 reflection site + theorem payment；Power Set station record
actual action         = create CAL / source-layer / station classification contract
Q-state delta         = Q_SAFETY_REPAIR
```

它没有运行新的来源检索，不能证明 CAL-3/CAL-4、L-C/L-D/L-E覆盖、station switch、HoTT/ZFC结论或数学定理。
它所能支持的是：从该 commit 起，后续 ForgeIntent 必须显式报告校准目标、来源层和 station impact；没有增量时应停在
`REPEATED_GUARD_NO_NEW_FORGE_INTENT`。

## 3. 当前合同下的反事实与消费证据

今天审同一动作时，N33满足 `Q_SAFETY_REPAIR` 的条件：它指向固定H074/H075与 Power Set Q-0 卡，明确了误报类型，
并规定以后需要通过相称的来源／station字段回归。它不是 `Q_CAPABILITY_CALIBRATION`，因为它不测试P对数学接口的
行为；也不是 `TOOL_ONLY_DRIFT`，因为R12与当前A2回接实际使用它限制了 CAL、source layer和station的判词。

```text
CURRENT_CONTRACT = IDEA_SPEC_INCOMPLETE_REPAIRED / Q_SAFETY_REPAIR_WITH_SCOPE
consumption       = R12 retains CAL-2_CONTROL_ONLY / L-B proof-theory payment / NO_STATION_CHANGE
forbidden upgrade = CAL-3/CAL-4, L-C/L-D/L-E coverage, ZFC Candidate-Q, station switch
```

这个“消费”只证明当前历史分母中的行为约束；它不保证未来每个 Agent 或新节点都会自动遵守N33的字段。

## 4. 偏差、财富与重开

| 字段 | 记录 |
|---|---|
| 偏差分类 | `IDEA_SPEC_INCOMPLETE_REPAIRED`：此前校准、来源层与站位状态可被混写；N33以最小分类合同分开它们。 |
| QConvergenceLink | `Q_SAFETY_REPAIR_WITH_SCOPE`：保护H074/H075及Power Set站位的既有身份，Theory-Q状态不变。 |
| 财富 | `HYPOTHESIS`：未来独立接口只有跨过已付proof layer、保留active positive obligation及同一任务P2/P3或consumer事实，才可能从CAL-2升至CAL-3。 |
| 停止边界 | N33不自动启动新ForgeIntent、worker、网络、station switch、新刀或数学证明。 |
| 重开条件 | 当前后续审计实际绕过CAL/source-layer/station字段；一个未被N33分类覆盖的来源层或站位决策改变P/Q准入；或H074/H075的源事实被推翻。 |

**本卡最终判词：** `IDEA_SPEC_INCOMPLETE_REPAIRED / NON_H_MASTER_DECISION / CAL_SOURCE_LAYER_STATION_CONTRACT / Q_SAFETY_REPAIR_WITH_SCOPE / NO_THEORY_Q`。
