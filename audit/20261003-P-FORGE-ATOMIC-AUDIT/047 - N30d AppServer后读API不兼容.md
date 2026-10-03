<!-- governance-shard:v2
logical_id: P_FORGE_ATOMIC_AUDIT_CAMPAIGN
shard_id: 047
index: ../20261003-P-FORGE-ATOMIC-AUDIT.md
-->

# N30d AppServer后读API不兼容

> **AtomicAuditCard：** `N30d / NON_H_SESSION_RUN / APPSERVER_ISOLATION_004 / ATOMIC_AUDIT_COMPLETE_SOURCE_REPORTED_NOT_REPLAYED`。

## 1. 身份、证据与顺序

| 字段 | 记录 |
|---|---|
| `atomic_id` | `N30d`；ISOLATION-004零理论health run。 |
| exact session | `01a0fdd4-36a9-77e3-bd87-63a3d17077ee`，由A0时私有direct wire恢复并写入ledger。 |
| 最小公开来源 | [`ISOLATION-004 NodeCard`](../20261002-P-DAG-CODEX-APPSERVER-ISOLATION-004-NODECARD.md)，SHA-256 `dcdd17a008f0a3743a6e823727ab784f0e0af2de260f750cb735ba060c36dd8f`。 |
| 后续公开佐证 | ISOLATION-005 parent correction：004通过model-visible-input gate并到达App Server，但post-turn `thread/read(includeTurns=true)`被ephemeral lifecycle以`-32600`拒绝。 |
| current raw boundary | 本轮可读输入没有004 private direct wire/terminal event；exact session为历史private evidence的报告身份，`SOURCE_REPORTED_NOT_REPLAYED`。 |

## 2. `AS_RUN`：后读API错误不是理论或模型错误

004冻结了修正后的prompt-input规则、受控auth borrowing、text-only cwd、Terra/Max、`never`与zero-theory marker。
后续记录表明健康流程到达App Server，但额外的ephemeral `thread/read(includeTurns=true)`不兼容，返回`-32600`。
这个错误发生在post-turn inspection，不可被读作prompt、理论、P或模型输出的判词。

```text
Target-Q (as run)    = 未来隔离runner能否提供可信运行证据
Candidate-Q (as run) = NONE；zero-theory health
Control-Q (as run)   = ephemeral post-turn read API compatibility
theory-Q delta       = NONE
```

## 3. 当前合同下的 QConvergenceLink

| 项目 | 当前反事实判词 |
|---|---|
| evidence status | `SOURCE_REPORTED_NOT_REPLAYED`；当前不能复核004 raw wire、exact echo或health marker正文。 |
| QConvergenceLink | `Q_SAFETY_REPAIR`：后读API错误必须作为runner compatibility control，不能污染理论卡。 |
| 合法修复 | 不要求ephemeral `thread/read(includeTurns=true)`；以raw message delta和terminal evidence满足health oracle。 |
| 后继 | N30e用修正wrapper重新做zero-theory health。 |
| 停止条件 | 不把004当general App Server lane资格；仅保留本次API兼容缺口。 |

## 4. 理念对照、偏差与可推翻条件

| 维度 | 判词 |
|---|---|
| 运行/理论分离 | `RUNNER_OR_EVIDENCE_FAILURE`：ephemeral API限制不评价模型、P、HoTT或ZFC。 |
| P/Q共同锻造 | `Q_SAFETY_REPAIR_WITH_SCOPE`：保存实际runner缺口，保护未来有效lane的证据资格。 |
| 偏差分类 | `IDEA_SPEC_INCOMPLETE_REPAIRED`：原health oracle含不兼容的post-turn read。 |
| 证据边界 | NodeCard与后继公开叙述；raw wire目前未重新读取。 |

**falsifier：** 原始004 wire/terminal evidence若表明不同终态、或compatible read实际存在，应重审；N30e的成功不回写N30d。

## 5. 财富、后继与范围

| 字段 | 记录 |
|---|---|
| `Wealth` | `HYPOTHESIS`：runner oracle应只要求其所选lifecycle能实际提供的终态证据，不以不兼容post-read掩盖health结果。 |
| 后继 | N30e health-005；future raw-wire recovery。 |
| 自动动作 | 无；不产生theory Q或声称generic App Server qualified。 |
| current truth effect | `ZFC_SITE_SELECTED / Q-0 UNFORMED / ZFC_Q_NOT_LOCATED`保持。 |
| 审计范围 | 只审N30d公开可见兼容性事实及raw未重放边界。 |

**本卡最终判词：** `RUNNER_OR_EVIDENCE_FAILURE / Q_SAFETY_REPAIR_WITH_SCOPE / SOURCE_REPORTED_NOT_REPLAYED / NO_THEORY_Q`。
