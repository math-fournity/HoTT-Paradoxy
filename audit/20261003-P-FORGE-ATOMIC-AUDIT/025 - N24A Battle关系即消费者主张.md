<!-- governance-shard:v2
logical_id: P_FORGE_ATOMIC_AUDIT_CAMPAIGN
shard_id: 025
index: ../20261003-P-FORGE-ATOMIC-AUDIT.md
-->

# N24A Battle关系即消费者主张

> **AtomicAuditCard：** `N24A / NON_H_SESSION_RUN / BATTLE_001_ADVOCATE / ATOMIC_AUDIT_COMPLETE_WITH_SCOPE`。

## 1. 身份、证据与顺序

| 字段 | 记录 |
|---|---|
| `atomic_id` | `N24A`；F24 Battle-001 的B-A advocate，非整个Battle的裁决。 |
| 父粗单元 | P1 L2b consumer-contract争议的动态DAG Battle；N24B挑战、N24C仲裁尚是独立原子单位。 |
| exact session | `01a0fd1b-039b-77e1-895a-b5ff743ce497`。 |
| 最小来源 | [`P-DAG-BATTLE-001`](../20261002-P-DAG-BATTLE-001-Terra-Max.md)，SHA-256 `8719c90b38635d79422631eb6c734d9edcedb673052ef9807bae417148967eb7`；冻结中性ZFC card与L2b。 |
| 可见输入/权限 | `BATTLE_PACK`；fresh `gpt-5.6-terra / max / read-only / never`；只读prompt内source/claim，不读项目、网络、分支或历史。 |
| trajectory 边界 | 报告保存session、prompt/result SHA和公开立场摘要；当前没有可重放exact-ID raw trajectory。prompt正文、逐事件工具、L1--L4和隐藏reasoning为 `UNAVAILABLE_WITH_SCOPE`。 |
| 实际终态 | advocate为 `RELATION_AS_MINIMAL_CONSUMER` 提出最强支持，但公开承认source缺output representation、evaluator、witness format和Done。 |

## 2. `AS_RUN`：最强主张仍需要卡外约定

N24A保留了中性card真实给出的对象、`P(a)`、`P(P(a))`和membership relation，并展开：

```text
a∈P(P(a)) ⇒ a⊆P(a) ⇒ ∀x∈a, x⊆a.
```

这支持一个有限主张：该relation可在不加入公式编码、satisfaction或无限制comprehension的条件下被陈述与展开。
但若要把它升级成 `RELATION_AS_MINIMAL_CONSUMER`，advocate必须加上“每个atomic membership assertion都算P1 consumer”
这一source之外的 convention；它自己也记录card没有I/O/Done。

```text
Target-Q (as run)    = Power Set静态card是否已有source-supplied consumer，能使P1 candidate进入共同锻造
Candidate-Q (as run) = a∈P(P(a)) 的 relation-as-consumer 假设
Control-Q (as run)   = relation对象原生性与source缺I/O/Done之间的张力
theory-Q delta       = Q_STATUS_UNINFERABLE_FROM_EVIDENCE；advocate不是最终source verdict
```

## 3. 当前合同下的 QConvergenceLink

当前L2b明确禁止从裸relation自动获得 `C`。因此N24A不能单独产生或保留Candidate-Q：

| 项目 | 当前反事实判词 |
|---|---|
| `C` 字段 | relation原生不等于source-defined judgment/task/operation；输入、output/Done或handoff仍缺。 |
| Candidate-Q | 该advocate假设在source合同下未支付，不能交给P2/P3。 |
| QConvergenceLink | `Q_SAFETY_REPAIR_WITH_SCOPE`：公开暴露了必须额外加入的convention，保护P1不把它暗中写进理论。 |
| 后继 | N24B必须逐字段挑战该convention；N24C仅以source和L2b裁决。 |
| 停止条件 | 未出现source定义的membership consumer I/O/Done时，relation-as-consumer停为假设。 |

## 4. 理念对照、偏差与可推翻条件

| 维度 | 判词 |
|---|---|
| Battle角色忠实性 | `ALIGNED_ROLE_WITH_SCOPE`：advocate给出最强可辩读法，也披露它需要的额外约定；不能继承challenger/arbiter的结论。 |
| P/Q共同锻造 | `Q_STATUS_UNINFERABLE_AS_RUN / Q_SAFETY_REPAIR_CURRENT`：单方立场不计作Q发现，但使隐藏consumer假设可审。 |
| 偏差分类 | `ALIGNED`；没有把convention伪称为source事实。 |
| 证据边界 | 单一Battle角色的公开立场，非数学证明、非ZFC consumer事实、非模型内部因果解释。 |

**falsifier：** 若冻结source实际定义 `(a,p₂)` membership judgement的input/output/Done，使atomic assertion无需另加convention就可作consumer，则N24A的“extra convention”界限应撤回；这不会单独证明更广ZFC Q。

## 5. 财富、后继与范围

| 字段 | 记录 |
|---|---|
| `Wealth` | `HYPOTHESIS`：关系可作为consumer的最强读法必须被source契约或独立challenge检验，不能因对象层可写即通过。 |
| 后继 | N24B challenger、N24C arbiter；版本固定的actual consumer source。 |
| 自动动作 | 无；不把advocate立场写成`ZFC_Q_LOCATED`或启动新worker。 |
| current truth effect | `ZFC_SITE_SELECTED / Q-0 UNFORMED / ZFC_Q_NOT_LOCATED`保持。 |
| 审计范围 | 只审N24A公开advocate输出；不审不可见trajectory/reasoning，也不代替整个Battle。 |

**本卡最终判词：** `ALIGNED_ROLE_WITH_SCOPE / Q_STATUS_UNINFERABLE_AS_RUN / Q_SAFETY_REPAIR_CURRENT / NO_THEORY_Q`。
