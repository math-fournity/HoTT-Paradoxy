<!-- governance-shard:v2
logical_id: P_FORGE_ATOMIC_AUDIT_CAMPAIGN
shard_id: 045
index: ../20261003-P-FORGE-ATOMIC-AUDIT.md
-->

# N30b 空CodeHome认证失败

> **AtomicAuditCard：** `N30b / NON_H_DOCUMENTED_EXECUTION / RUNNER_ISOLATION_AUTH_BOUNDARY / ATOMIC_AUDIT_COMPLETE_WITH_SCOPE`。

## 1. 身份、证据与顺序

| 字段 | 记录 |
|---|---|
| `atomic_id` | `N30b`；zero-theory empty `CODEX_HOME` runner health execution。 |
| 父粗单元 | H-007 access leak之后的CLI隔离资格化；只测试认证与输入边界，不含理论材料。 |
| 最小来源 | [`P-DAG-RUNNER-ISOLATION-002-RESULT`](../20261002-P-DAG-RUNNER-ISOLATION-002-RESULT.md)，SHA-256 `69640d68de95c14edc918270ed0442808f2d616d66b72f1d3a2e996d2a4ce517`。 |
| 可见环境 | empty mode-0700 temporary `CODEX_HOME`、独立scratch cwd、`--ephemeral`、`--ignore-user-config`、`--ignore-rules`、read-only/never、Terra/Max request；唯一prompt为health marker。 |
| 实际终态 | banner回显请求字段；模型采样前反复 `401 Unauthorized`，无terminal answer/tool event/final file。 |
| credential boundary | 未读取、复制、链接、记录或挂载用户认证内容；keyring路径未完成认证。 |

## 2. `AS_RUN`：认证失败不检验盲态，更不检验理论

```text
Target-Q (as run)    = 将来blind P-DAG理论节点能否在隔离环境中产生可审证据
Candidate-Q (as run) = NONE；唯一prompt无理论材料
Control-Q (as run)   = no model sample / no tool / 401 pre-sampling failure
theory-Q delta       = NONE
```

本次不能证明空home的隔离是否足够，因为没有获得可观察模型采样。复制用户file-auth到临时home被明确排除：它会让
同一process family接触不应暴露的认证材料，不能作为“修复”。

## 3. 当前合同下的 QConvergenceLink

| 项目 | 当前反事实判词 |
|---|---|
| runner资格 | `RUNNER_ISOLATION_NOT_QUALIFIED`；认证失败前没有样本，不可用作blind theory lane。 |
| QConvergenceLink | `Q_SAFETY_REPAIR`：保护未来blind发现不被未资格化CLI lane污染或冒充no-cheat evidence。 |
| 可接受修复 | 独立认证的隔离home，或实际回显model/effort/read-only/never/context的App Server harness。 |
| 禁止修复 | 复制/软链用户认证文件到model-readable temporary home。 |
| 停止条件 | 无可用认证时停止blind理论node；Master source分析不替代独立replay。 |

## 4. 理念对照、偏差与可推翻条件

| 维度 | 判词 |
|---|---|
| 运行/理论分离 | `RUNNER_OR_EVIDENCE_FAILURE`：401只证明这次认证未通过，不能归因模型、P或理论。 |
| P/Q共同锻造 | `Q_SAFETY_REPAIR_WITH_SCOPE`：运行隔离是未来Q判断可信度的前提，不是Q增量。 |
| 偏差分类 | `ALIGNED`：保持credential boundary，不以便利绕过隔离。 |
| 证据边界 | zero-theory health receipt；无模型行为、无上下文隔离实测、无数学结论。 |

**falsifier：** 若同一隔离配置获得认证并保存无理论health run的实际model/context/permission evidence，N30b的“不合格runner”范围应重审；不同配置须有新ID。

## 5. 财富、后继与范围

| 字段 | 记录 |
|---|---|
| `Wealth` | `HYPOTHESIS`：no-cheat实验须同时有认证边界、输入边界和实际采样收据；少一项不等于合格lane。 |
| 后继 | N30c prompt-input gate、N30d/e App Server health、N30f capability inspection。 |
| 自动动作 | 无；不启动blind theory worker、不产生HoTT/ZFC Candidate-Q。 |
| current truth effect | `ZFC_SITE_SELECTED / Q-0 UNFORMED / ZFC_Q_NOT_LOCATED`保持。 |
| 审计范围 | 只审N30b认证失败与隔离边界。 |

**本卡最终判词：** `RUNNER_OR_EVIDENCE_FAILURE / Q_SAFETY_REPAIR_WITH_SCOPE / NO_MODEL_SAMPLE / RUNNER_ISOLATION_NOT_QUALIFIED`。
