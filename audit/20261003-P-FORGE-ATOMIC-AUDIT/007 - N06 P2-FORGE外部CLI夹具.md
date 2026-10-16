<!-- governance-shard:v2
logical_id: P_FORGE_ATOMIC_AUDIT_CAMPAIGN
shard_id: 007
index: ../20261003-P-FORGE-ATOMIC-AUDIT.md
-->

# N06 P2-FORGE外部CLI夹具

> **AtomicAuditCard：** `N06 / NON_H_SESSION_RUN / R01_P2_FIXTURE / ATOMIC_AUDIT_COMPLETE_WITH_SCOPE`。

## 1. 身份、证据与顺序

| 字段 | 记录 |
|---|---|
| `atomic_id` | `N06` |
| 父粗单元 | R01 第一轮 P2 formation–reentry–polarity fixture。 |
| 前置单位 | N32；其参数错误已单独封存，不能与本次成功运行合并。 |
| exact session | `01a0fca3-9498-71f0-b8d6-255b9a65648b`。 |
| 最小来源 | `audit/20261002-P2-FORGE-001-外部CLI-Terra-Max.md`，SHA-256 `80dd4a1f…982de555`。 |
| 可见环境 | `codex-cli 0.157.0`、请求 Terra/Max、read-only／never、独立 scratch cwd、禁项目／网络／命令和历史名称。 |
| 终态 | P2-F-001/F-002/F-003全部按冻结预期分类；无实际理论 source、kernel或数学结论。 |

## 2. `AS_RUN`：三项 P2 分类夹具

N06 成功区分：

| 夹具 | 实际分类 | 它防止的误读 |
|---|---|---|
| P2-F-001 | `MATCHED / FINITE_SPECIFICATION_CONFLICT_CANDIDATE` | 把未固定逻辑的局部 `q↔¬q`直接说成任意理论矛盾。 |
| P2-F-002 | `GUARD_BLOCKED` | 因为 formation 已经产出 u，就擅自把 u 代回受界 bridge。 |
| P2-F-003 | `MATCHED / NONCONFLICTING_OR_UNDECIDED_FEEDBACK` | 把任意固定点或正极性自代都误报为冲突。 |

```text
Target-Q (as run)    = 未来 Candidate-Q 所需的同一对象 bind/form/bridge/reentry/polarity 判别能力
Candidate-Q (as run) = NONE
Control-Q (as run)   = P2-F-001..003 的合成正负／sanity controls
theory-Q delta       = NONE
```

代理还保留 `↔`、`¬` 与 `ConflictOracle_X` 必须由实际理论逻辑确定的边界，故没有把合成夹具冒充理论匹配。

## 3. 当前合同下的 QConvergenceLink

N06 满足 `Q_CAPABILITY_CALIBRATION_WITH_SCOPE`：它有明确的被校准字段、正／负／sanity controls、停止条件，并在
R02的 CFTT、Climber、Delay实际来源审查中被消费为“哪些 bridge、guard、reentry 或 process 不能伪造”。

| 项目 | 当前判词 |
|---|---|
| 校准层 | `CAL-1 KNOWN_CONTROL`；成功只表明在冻结夹具与本次请求面上能分类。 |
| 被校准字段 | Bind、Form、Bridge域/方向、Reenter合法性、polarity、guard和logic-oracle边界。 |
| QConvergenceLink | `Q_CAPABILITY_CALIBRATION`，不改变任何理论卡的Q状态。 |
| 后续真实消费 | R02固定 CFTT／Climber／Delay source controls；它们仍需各自 AtomicAuditCard，不能由N06替代。 |
| 停止 | 没有固定实际理论 source / same-task consumer 时，N06不能升级为P2对HoTT或ZFC的MatchTrace。 |

N06不是`TOOL_ONLY_DRIFT`，因为其正负分类后来被实际 source control消费；它也不是理论发现，因为Candidate-Q始终为`NONE`。

## 4. 理念对照、偏差与可推翻条件

| 维度 | 判词 |
|---|---|
| 原初三刀构造 | `ALIGNED`：P2按明确的逻辑结构、guard与极性分类，而非关键词匹配。 |
| P/Q 共同锻造 | `ALIGNED_CAPABILITY_CALIBRATION_WITH_SCOPE`。 |
| 运行边界 | N32已隔离参数失败；N06自身有可见session和终态，但仍不等于独立 runtime model receipt或操作系统级盲态证明。 |
| 原初理念受挑战 | `NO`。 |

**falsifier：** 若 R02 的实际来源不能在冻结字段下消费这些控制，或P2将没有合法 Reenter 的受界例子仍报为负性冲突，
则 N06的校准资格下降为`TOOL_ONLY_DRIFT_WITH_SCOPE`。

## 5. 财富、后继与范围

| 字段 | 记录 |
|---|---|
| `Wealth` | `HYPOTHESIS`：未来 theory card 的 P2 match 必须提供实际语言规则、bridge方向、合法回代和理论专属oracle，而不是复用夹具标签。 |
| 后继 | N07 P3-FORGE、N08 P1-FORGE、N09 P3-CIRCLE及R02 source controls。 |
| 自动动作 | 无；CAL-1不授权ZFC Q、HoTT结论、P4或新worker。 |
| 审计范围 | 本卡只审一次成功的夹具分类；N32保持独立的命令失败历史。 |

**本卡最终判词：** `ALIGNED_CAPABILITY_CALIBRATION_WITH_SCOPE / CAL-1_KNOWN_CONTROL / Q_CAPABILITY_CALIBRATION / NO_THEORY_Q`。
