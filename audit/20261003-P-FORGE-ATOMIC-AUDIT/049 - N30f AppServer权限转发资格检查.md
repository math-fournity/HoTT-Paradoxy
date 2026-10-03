<!-- governance-shard:v2
logical_id: P_FORGE_ATOMIC_AUDIT_CAMPAIGN
shard_id: 049
index: ../20261003-P-FORGE-ATOMIC-AUDIT.md
-->

# N30f AppServer权限转发资格检查

> **AtomicAuditCard：** `N30f / NON_H_MASTER_DECISION / APPSERVER_CAPABILITY_INSPECTION / ATOMIC_AUDIT_COMPLETE_WITH_SCOPE`。

## 1. 身份、证据与顺序

| 字段 | 记录 |
|---|---|
| `atomic_id` | `N30f`；Master host-capability source inspection，未启动worker。 |
| 最小来源 | [`P-DAG App Server 资格检查`](../20261002-P-DAG-AppServer-资格检查.md)，SHA-256 `4854dfb88f2769dfe6911caa49138090d79bdb1555668a629485bdbda1c4f95d`。 |
| 检查对象 | local `codex-cli 0.157.0` App Server schema、shared `agent_session_broker.py` source定位与permission forwarding。 |
| 直接事实 | schema有model/sandbox/approval字段；shared broker的`new_session()`传cwd/ephemeral/model/permissions/approvalPolicy等，但未将schema `sandbox`转发到`thread/start`。 |
| 终态 | `APP_SERVER_PERMISSION_FORWARDING_NOT_QUALIFIED`；未开App Server worker、未改shared repo/config/host。 |

## 2. `AS_RUN`：schema有字段，不等于实际worker获得权限

P-DAG理论worker被要求read-only、approval=`never`。App Server schema支持这些参数，不证明shared broker facade在当前版本
把sandbox实际转发或thread/turn实际回显。因此N30f正确拒绝用prompt里写“只读”代替环境权限证据。

```text
Target-Q (as run)    = 未来P-DAG理论运行能否有可信权限/隔离证据
Candidate-Q (as run) = NONE；纯host capability inspection
Control-Q (as run)   = schema field存在与broker forwarding/actual echo的差分
theory-Q delta       = NONE
```

## 3. 当前合同下的 QConvergenceLink

| 项目 | 当前反事实判词 |
|---|---|
| runner资格 | generic shared broker的sandbox forwarding未资格化，不能承担本项目read-only research worker。 |
| QConvergenceLink | `Q_SAFETY_REPAIR`：阻止未回显的权限配置成为理论节点或Q证据的隐含前提。 |
| 重新资格化 | 精确转发sandbox/sandboxPolicy/approvalPolicy、无害thread实际echo、observer ACL/private wire/cancel-terminal cleanup smoke。 |
| N30e关系 | exact direct wrapper health lane不自动资格化generic shared broker。 |
| 停止条件 | 未满足实际echo前，不启动该broker承载的理论worker。 |

## 4. 理念对照、偏差与可推翻条件

| 维度 | 判词 |
|---|---|
| 配置/运行区分 | `ALIGNED_WITH_SCOPE`：schema、adapter源码和实际runtime echo逐层分开。 |
| P/Q共同锻造 | `Q_SAFETY_REPAIR_WITH_SCOPE`：运行权限是理论证据的前置条件，非Q增量。 |
| 偏差分类 | `ALIGNED`；无worker启动，故不将未资格化设施说成失败模型。 |
| 证据边界 | 本机schema/source inspection；不证明App Server永远不能用或所有broker无资格。 |

**falsifier：** 一个审查过的adapter若实际转发并回显sandbox/approval，且满足observer/terminal证据要求，N30f的范围应收窄；仅改schema文档不够。

## 5. 财富、后继与范围

| 字段 | 记录 |
|---|---|
| `Wealth` | `HYPOTHESIS`：权限字段必须沿source→adapter→runtime echo闭合，才能把隔离runner作为P-DAG证据环境。 |
| 后继 | N31 P1-HOTT；后续worker只能复用已资格化exact lane或先重资格化。 |
| 自动动作 | 无；不改shared broker、不启动worker、不产生理论Q。 |
| current truth effect | `ZFC_SITE_SELECTED / Q-0 UNFORMED / ZFC_Q_NOT_LOCATED`保持。 |
| 审计范围 | 只审N30f host capability source inspection。 |

**本卡最终判词：** `ALIGNED_WITH_SCOPE / Q_SAFETY_REPAIR_WITH_SCOPE / APP_SERVER_PERMISSION_FORWARDING_NOT_QUALIFIED / NO_THEORY_Q`。
