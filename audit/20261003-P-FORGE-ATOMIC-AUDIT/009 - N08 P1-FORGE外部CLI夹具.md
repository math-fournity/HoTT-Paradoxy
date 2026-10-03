<!-- governance-shard:v2
logical_id: P_FORGE_ATOMIC_AUDIT_CAMPAIGN
shard_id: 009
index: ../20261003-P-FORGE-ATOMIC-AUDIT.md
-->

# N08 P1-FORGE外部CLI夹具

> **AtomicAuditCard：** `N08 / NON_H_SESSION_RUN / R01_P1_FIXTURE / ATOMIC_AUDIT_COMPLETE_WITH_SCOPE`。

## 1. 身份、证据与顺序

| 字段 | 记录 |
|---|---|
| `atomic_id` | `N08` |
| 父粗单元 | R01 P1 premise/operation/observation/Done fixture。 |
| exact session | `01a0fca9-2ca7-76b2-b5fc-14812da9f046`。 |
| 最小来源 | `audit/20261002-P1-FORGE-001-外部CLI-Terra-Max.md`，SHA-256 `65f85daf…9a021b28e`。 |
| 可见环境 | `codex-cli 0.157.0`、请求 Terra/Max、read-only／never、独立 scratch cwd、禁项目／网络／命令和历史名称。 |
| 终态 | 对芝诺和圆环都给出位置/Done边界，明确 `NOT_READY_FOR_PARADOX_CLAIM`。 |

## 2. `AS_RUN`：前提、过程、观察与 Done 的控制

N08 对芝诺的冻结过程保留：每个有限 halving 步之后仍有正剩余；最小步长＋终步改变的是过程前提，而不是
同一连续过程的答案。对圆环，它区分：

```text
weak Done   = bare N compactification
strong Done = source/boundary/operation observations preserved under reconnect operation
```

并把 missing formal relation、admissible repair、origin-preserving equivalence与可行性证明列为缺口。

```text
Target-Q (as run)    = 未来理论/现实任务卡必须保住原对象、操作、观察与Done的能力
Candidate-Q (as run) = NONE
Control-Q (as run)   = 离散终步对连续halving的任务切换；bare compactification对强圆环Done的任务切换
theory-Q delta       = NONE
```

## 3. 当前合同下的 QConvergenceLink

N08具有配对的 premise/Done controls：它证明 P1 不会把极限、阈值、紧化或单纯闭包自动写成原任务完成。因此：

| 项目 | 当前判词 |
|---|---|
| 校准层 | `CAL-1 KNOWN_CONTROL`，只覆盖冻结的芝诺／圆环任务合同。 |
| 被校准字段 | TheoryVariant、NativePremise、Operation、Observation、Done、ControlVariant与同一任务比较。 |
| QConvergenceLink | `Q_CAPABILITY_CALIBRATION`，使未来 Candidate-Q 必须携带相同任务证据。 |
| 后续消费 | 圆环来源审计与 HoTT/现实任务映射在后续来源卡中消费强Done／任务切换约束。 |
| 停止 | 无来源保持的对象、操作、观察与Done时，任何“悖论”或现实相对结论必须停止。 |

N08不证明芝诺、圆环、极限或现实过程的哲学／数学结论；它只校准 P1 的任务忠实性门。

## 4. 理念对照、偏差与可推翻条件

| 维度 | 判词 |
|---|---|
| 原初任务忠实性要求 | `ALIGNED_WITH_SCOPE`：拒绝把控制模型的不同 Done 偷换为原任务的完成。 |
| P/Q 共同锻造 | `ALIGNED_CAPABILITY_CALIBRATION_WITH_SCOPE`。 |
| 运行边界 | 有可见 session/终态，但无现实同一性证明、圆环原典形式关系或数学证明。 |
| 原初理念受挑战 | `NO`。 |

**falsifier：** 若一个 control variant 能在不改变冻结对象、输入、操作、观察或 Done 的条件下完成同一任务，
或 bare compactification被来源证明保留强Done，则本卡的 task-switch classification必须重审。

## 5. 财富、后继与范围

| 字段 | 记录 |
|---|---|
| `Wealth` | `HYPOTHESIS`：未来理论 Q 卡必须先写 X_i／X_h、operation、observation与Done，才可比较连续/离散、理论/现实或来源/表示。 |
| 后继 | N09 P3-CIRCLE和后续圆环原典、HoTT card的任务忠实性审查。 |
| 自动动作 | 无；不启动数学证明、现实判定、P4或新理论 node。 |
| 审计范围 | 只审P1夹具分类能力。 |

**本卡最终判词：** `ALIGNED_CAPABILITY_CALIBRATION_WITH_SCOPE / CAL-1_KNOWN_CONTROL / Q_CAPABILITY_CALIBRATION / NO_THEORY_Q`。
