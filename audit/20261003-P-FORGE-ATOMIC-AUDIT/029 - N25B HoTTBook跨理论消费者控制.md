<!-- governance-shard:v2
logical_id: P_FORGE_ATOMIC_AUDIT_CAMPAIGN
shard_id: 029
index: ../20261003-P-FORGE-ATOMIC-AUDIT.md
-->

# N25B HoTTBook跨理论消费者控制

> **AtomicAuditCard：** `N25B / NON_H_SESSION_RUN / SOURCE_001_CROSS_THEORY_CONTROL / ATOMIC_AUDIT_COMPLETE_WITH_SCOPE`。

## 1. 身份、证据与顺序

| 字段 | 记录 |
|---|---|
| `atomic_id` | `N25B`；SOURCE-001的S-B math control tracer。 |
| 父粗单元 | 与N25A并列的公开source tracer；职责是提供跨理论的consumer正控制，不能填ZFC卡。 |
| exact session | `01a0fd24-e017-7330-8f84-cc677ee47132`。 |
| 最小来源 | [`P-DAG-SOURCE-001`](../20261002-P-DAG-SOURCE-001-Terra-Max.md)，SHA-256 `a7b7f70e08aab6c37fee8244a583a357ff47542e961c9809e6364a6ac744f0b6`；HoTT Book `first-edition-611-ga1a258c` §10.3 Lemma 10.3.7 的报告级locator。 |
| 可见输入/权限 | `PRIMARY_WEB_SOURCE`；fresh `gpt-5.6-terra / max / read-only / never`；可读公开一手来源，不读项目。 |
| trajectory 边界 | 当前保存session、prompt/result hash与source摘要；无可重放exact-ID raw trajectory，L1--L4/hidden reasoning为 `UNAVAILABLE_WITH_SCOPE`。 |
| 实际终态 | `QUALIFYING_MATH_CONSUMER`，明确标为跨理论control。 |

## 2. `AS_RUN`：正控制说明什么，不说明什么

S-B定位HoTT Book的一个明确consumer形状：`P(B):=(B→Prop)`，显式假设 `g:P(B)→B`，构造predecessor-image subset并以
`g`消费，最后得到well-founded recursive `f:A→B` 的方程。这个source显示：power-set样对象可以确实拥有清楚的
`C/I/O/Done`，因此“有consumer”不是无法落实的抽象口号。

但它属于HoTT Book，拥有自己的`T/u/F/C/I/O/Done`；不能作为ZFC、Mathlib ZFSet或Power Set静态card的consumer证据。

```text
Target-Q (as run)    = P1是否能用版本固定source辨认真实consumer contract
Candidate-Q (as run) = NONE；该卡只作跨理论控制
Control-Q (as run)   = HoTT Book的P(B)/g/recursive-equation consumer
theory-Q delta       = NONE
```

## 3. 当前合同下的 QConvergenceLink

| 项目 | 当前反事实判词 |
|---|---|
| 被校准字段 | source版本、object、输入、consumer、operation、output/Done与真实使用链的明确性。 |
| Target-Q | 未来目标理论中必须找到的同层consumer/obligation形状。 |
| Candidate-Q | `NONE`；跨理论正控制不得进入ZFC的`T/u/F/C/Q/I/O/Done`。 |
| QConvergenceLink | `Q_CAPABILITY_CALIBRATION_WITH_SCOPE`：说明P1可以在源中识别具体consumer，但不为目标理论填字段。 |
| 停止条件 | source层/理论变体不同即停止迁移；不能因“都像幂集”将其作为ZFC Q。 |

这个控制直接防止两种错误：把“没有找到ZFC consumer”说成P1无法识别consumer，或把HoTT Book正构造挪到ZFC上
造成虚假共同Q。

## 4. 理念对照、偏差与可推翻条件

| 维度 | 判词 |
|---|---|
| 同一任务与层级 | `ALIGNED_WITH_SCOPE`：保留cross-theory relation作为控制，不将其伪称目标理论的consumer。 |
| P/Q共同锻造 | `Q_CAPABILITY_CALIBRATION_WITH_SCOPE`：校准P1 source识别能力，不改变任何ZFC Candidate-Q。 |
| 偏差分类 | `ALIGNED`；跨理论材料被明确隔离，未发生target-layer偷换。 |
| 证据边界 | source tracer报告与版本locator；未对HoTT Book全文或理论结果作本仓重放。 |

**falsifier：** 若报告定位的HoTT Book结构并非显式consumer、或N25B将它错误标作ZFC source，则本卡应重审；即使control成立，也不构成target theory证据。

## 5. 财富、后继与范围

| 字段 | 记录 |
|---|---|
| `Wealth` | `HYPOTHESIS`：真实consumer卡可被正面识别；未来目标理论source必须独立提供同层I/O/Done，不能借control代替。 |
| 后继 | N25C/N25D 对Mathlib ZFSet卡的同层P2/P3映射。 |
| 自动动作 | 无；不启动新worker、不产生HoTT或ZFC Candidate-Q。 |
| current truth effect | `ZFC_SITE_SELECTED / Q-0 UNFORMED / ZFC_Q_NOT_LOCATED`保持。 |
| 审计范围 | 只审N25B cross-theory control，不审不可见trajectory/reasoning或HoTT Book的数学内容。 |

**本卡最终判词：** `ALIGNED_WITH_SCOPE / Q_CAPABILITY_CALIBRATION_WITH_SCOPE / CROSS_THEORY_CONSUMER_CONTROL / NO_THEORY_Q`。
