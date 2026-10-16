<!-- governance-shard:v2
logical_id: P_FORGE_ATOMIC_AUDIT_CAMPAIGN
shard_id: 008
index: ../20261003-P-FORGE-ATOMIC-AUDIT.md
-->

# N07 P3-FORGE外部CLI夹具

> **AtomicAuditCard：** `N07 / NON_H_SESSION_RUN / R01_P3_FIXTURE / ATOMIC_AUDIT_COMPLETE_WITH_SCOPE`。

## 1. 身份、证据与顺序

| 字段 | 记录 |
|---|---|
| `atomic_id` | `N07` |
| 父粗单元 | R01 第一轮 P3 admission／completion fixture。 |
| exact session | `01a0fca5-f826-7cd0-9731-09428db42c6d`。 |
| 最小来源 | `audit/20261002-P3-FORGE-001-外部CLI-Terra-Max.md`，SHA-256 `dbf9ac00…6e3bf43ae`。 |
| 可见环境 | `codex-cli 0.157.0`、请求 Terra/Max、read-only／never、独立 scratch cwd、禁项目／网络／命令和历史名称。 |
| 终态 | P3-A/B/Bc均按冻结语义分层，未声明任何实际理论具有该状态机。 |

## 2. `AS_RUN`：三种过程读法的区分

| 夹具 | 实际分类 | 防止的误读 |
|---|---|---|
| P3-A | `ADMISSION_ORDER_CYCLE_CANDIDATE` 且 `CONSTRUCTION_SEMANTICS_NOT_SUPPLIED` | 将合成依赖图自动归于朴素集合论、HoTT或ZFC的实际状态。 |
| P3-B | `FINITE_STAGES_REMAIN_PENDING` | 从某次有限观察尚未Done推出全称“不终止”。 |
| P3-Bc | `COMPLETION_CONTROL_PRESENT` | 从存在终步推出所有调度都会完成。 |

```text
Target-Q (as run)    = 未来理论卡中是否存在 source-declared pending/admission/Done 的判别能力
Candidate-Q (as run) = NONE
Control-Q (as run)   = synthetic cycle, finite-pending, explicit-final-step cases
theory-Q delta       = NONE
```

P3-A 的关键正确性恰在于同时保留“若有依赖边则可能形成 cycle”和“夹具没有实际理论来源，所以不能称构造语义已给”。

## 3. 当前合同下的 QConvergenceLink

N07 有三种相互排斥的结果、至少一个正控制和两个阻断过度外推的控制；它满足受限的
`Q_CAPABILITY_CALIBRATION`：

| 项目 | 当前判词 |
|---|---|
| 校准层 | `CAL-1 KNOWN_CONTROL`，只覆盖这一冻结的合成过程语义。 |
| 被校准字段 | `Draft/NeedBuild/NeedEval/OperatorUse/Admitted/BuildDone`、依赖边、finite observation、终步与schedule边界。 |
| QConvergenceLink | `Q_CAPABILITY_CALIBRATION`，不会改变任何理论 Candidate-Q。 |
| 后续消费 | 实际 P3 source cards对静态公理、proof witness、有限桥和缺 lifecycle 的来源逐一使用这些拒绝条件。 |
| 停止 | 没有 source transition 或同一任务 ConstructionBridgeCard，P3必须停在`CONSTRUCTION_SEMANTICS_NOT_SUPPLIED`。 |

N07不产生“时间维度问题”。它使后续审计可以区别实际构造资格循环、有限尚未完成、调度缺口和纯外部耗时。

## 4. 理念对照、偏差与可推翻条件

| 维度 | 判词 |
|---|---|
| 原初 P3 目标 | `ALIGNED_WITH_SCOPE`：状态与边必须被逐项给出，不能由直觉补造。 |
| P/Q 共同锻造 | `ALIGNED_CAPABILITY_CALIBRATION_WITH_SCOPE`。 |
| 运行边界 | 有 session 与可见终态；不等于理论 source、kernel或所有模型的能力证明。 |
| 原初理念受挑战 | `NO`。 |

**falsifier：** 若后继实际来源在没有 state/transition evidence时仍必须被P3判为 admission cycle，或显式终步在相同
调度条件下仍不能构成 completion control，则本卡的校准结论应被重审。

## 5. 财富、后继与范围

| 字段 | 记录 |
|---|---|
| `Wealth` | `HYPOTHESIS`：理论外 construction read若要支持P3，必须先交付同一对象、输入、operation、observation和Done的桥。 |
| 后继 | N08 P1-FORGE、N09 P3-CIRCLE，以及后续 P3 source cards。 |
| 自动动作 | 无；不启动新理论 node、P4或数学结论。 |
| 审计范围 | 只审N07的分类能力，不将任何夹具状态机归给具体理论。 |

**本卡最终判词：** `ALIGNED_CAPABILITY_CALIBRATION_WITH_SCOPE / CAL-1_KNOWN_CONTROL / Q_CAPABILITY_CALIBRATION / NO_THEORY_Q`。
