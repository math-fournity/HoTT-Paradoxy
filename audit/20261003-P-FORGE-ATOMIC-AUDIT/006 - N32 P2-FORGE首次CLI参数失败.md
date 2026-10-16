<!-- governance-shard:v2
logical_id: P_FORGE_ATOMIC_AUDIT_CAMPAIGN
shard_id: 006
index: ../20261003-P-FORGE-ATOMIC-AUDIT.md
-->

# N32 P2-FORGE首次CLI参数失败

> **AtomicAuditCard：** `N32 / NON_H_DOCUMENTED_EXECUTION / PRE_N06_RUNNER_CONTROL / ATOMIC_AUDIT_COMPLETE_WITH_SCOPE`。

## 1. 身份、证据与顺序

| 字段 | 记录 |
|---|---|
| `atomic_id` | `N32` |
| 父单位 | N06 P2-FORGE external CLI fixture；N32发生在其成功 session 之前。 |
| 顺序 | 同一报告明确的 first attempt → corrected second attempt；N32 必须先于 N06 审计。 |
| 最小来源 | `audit/20261002-P2-FORGE-001-外部CLI-Terra-Max.md`，SHA-256 `80dd4a1f…982de555`。 |
| 运行身份 | 第一次命令因全局 CLI 参数位置错误在模型启动前退出；没有 session、模型输出、工具调用或理论输出。 |
| 后继 | N06 使用修正后的 `--no-daemon`、`-m`、effort、sandbox 与 approval 参数，才产生保存的 Terra/Max session。 |

## 2. `AS_RUN`：失败的范围

N32没有消费 P2 fixture 的 Bind/Form/Bridge/Reenter 内容。唯一可见事实是：第一条命令的参数布局不满足 CLI 的调用要求，
导致模型未启动；第二条命令才开始实际 fixture run。

```text
Target-Q / Candidate-Q / Control-Q = NONE
P2 semantic result                 = NONE
model identity / terminal output   = NONE
failure identity                   = CLI invocation / pre-sampling runner error
```

因此它既不能支持“P2 没有命中”，也不能支持“模型拒绝了 fixture”，更不能支持任何 HoTT、ZFC 或理论结论。

## 3. 当前合同下的 QConvergenceLink

N32 的唯一合法 P-FORGE 作用是保护 N06：没有将模型启动前的命令错误与 P2 的分类输出区分开，会把“没有结果”误报为
P2失败或负理论证据。

| 项目 | 当前判词 |
|---|---|
| 被保护卡 | `N06 / P2-F-001..003` fixture card。 |
| QConvergenceLink | `Q_SAFETY_REPAIR`，只保护后继卡的证据身份。 |
| Q state | 不变；没有理论 Candidate-Q 或控制 Q 的语义判词。 |
| runner verdict | `RUNNER_OR_EVIDENCE_FAILURE / PRE_SAMPLING_PARAMETER_LAYOUT_ERROR`。 |
| 回归 | N06 的成功 session必须与此失败分开保留，不能回写为一次连续成功。 |

这不是 `TOOL_ONLY_DRIFT`：它有一张明确受保护的 N06 卡和可观察的错误→修正关系；同时它不构成发现能力、来源证据或理论进展。

## 4. 理念对照、偏差与可推翻条件

| 维度 | 判词 |
|---|---|
| 原初理念 | `NOT_TESTED`：模型未采样，无法评价模式 P。 |
| 规格／执行 | `RUNNER_OR_EVIDENCE_FAILURE`，不是理论或 P1/P2/P3 规格失败。 |
| P/Q 共同锻造 | `Q_SAFETY_REPAIR`，以固定后继卡为边界。 |
| 原初理念受挑战 | `NO`。 |

**falsifier：** 若第一条命令事实上已启动模型、产生终态或形成与N06不同的可审输出，则 N32必须扩展为独立模型运行；
当前来源明确说它在模型启动前退出。

## 5. 财富、后继与范围

| 字段 | 记录 |
|---|---|
| `Wealth` | `REJECTED`：错误参数布局不是新理论入口或新刀具花纹。 |
| 后继 | N06 才审 P2 三项 fixture 的语义分类。 |
| 自动动作 | 无；不启动 retry、worker或来源检索。 |
| 审计范围 | 只记录一次已发生的运行失败与证据分层。 |

**本卡最终判词：** `RUNNER_OR_EVIDENCE_FAILURE / Q_SAFETY_REPAIR_FOR_N06 / NO_MODEL_SAMPLE / NO_THEORY_Q`。
