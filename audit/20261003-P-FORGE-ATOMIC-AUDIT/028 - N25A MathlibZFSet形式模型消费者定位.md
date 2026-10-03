<!-- governance-shard:v2
logical_id: P_FORGE_ATOMIC_AUDIT_CAMPAIGN
shard_id: 028
index: ../20261003-P-FORGE-ATOMIC-AUDIT.md
-->

# N25A MathlibZFSet形式模型消费者定位

> **AtomicAuditCard：** `N25A / NON_H_SESSION_RUN / SOURCE_001_FORMAL_SOURCE_TRACER / ATOMIC_AUDIT_COMPLETE_WITH_SCOPE`。

## 1. 身份、证据与顺序

| 字段 | 记录 |
|---|---|
| `atomic_id` | `N25A`；SOURCE-001 的S-A formal source tracer。 |
| 父粗单元 | Battle-001后第一次版本固定的Power Set consumer source定位；N25C/N25D将在同一冻结card上分别做P2/P3映射。 |
| exact session | `01a0fd24-e045-7e53-b290-ae608e851408`。 |
| 最小来源 | [`P-DAG-SOURCE-001`](../20261002-P-DAG-SOURCE-001-Terra-Max.md)，SHA-256 `a7b7f70e08aab6c37fee8244a583a357ff47542e961c9809e6364a6ac744f0b6`；Mathlib4 `v4.16.0` commit `a6276f4c6097675b1cf5ebd49b1146b735f38c02`的报告级固定source定位。 |
| 可见输入/权限 | `PRIMARY_WEB_SOURCE`；fresh `gpt-5.6-terra / max / read-only / never`；允许公开一手来源，不读项目。 |
| trajectory 边界 | 报告保存session、prompt/result hash、版本和可见source事实；无当前可重放exact-ID raw trajectory，L1--L4/hidden reasoning为 `UNAVAILABLE_WITH_SCOPE`。 |
| 实际终态 | `QUALIFYING_FORMAL_CONSUMER_WITH_SCOPE`。 |

## 2. `AS_RUN`：获得真实C/I/O/Done，但层级是形式化模型

S-A定位的卡是 Mathlib `ZFSet`：source header把它说成Lean underlying type theory中的 ZFC (+ Choice) model，
不是标准ZFC本身。报告所固定的接口为：

```lean
u = powerset (prod x y)
F = powerset / mem_powerset
C = funs x y := ZFSet.sep (IsFunc x y) u
O = funs x y : ZFSet
Done = mem_funs : f ∈ funs x y ↔ IsFunc x y f
```

它第一次使P1的`C/I/O/Done`缺口在**形式化模型层**得到真正来源支付：`u`被命名的下游构造消费，membership criterion给出proof/use contract。
但source并未给native nontrivial positive Q、P2 reentry、P3 lifecycle或理论缺陷；S-A也没有fresh Lean编译。

```text
Target-Q (as run)    = Power Set站位是否有来源定义consumer，能够使P1不再依赖裸relation
Candidate-Q (as run) = NONE；source只支付formal-consumer接口，未产生同一任务未支付义务
Control-Q (as run)   = N24C的中性card consumer gap；ZFSet model layer与standard-ZFC层的区分
theory-Q delta       = Q_NARROW_WITHOUT_CANDIDATE_Q
```

## 3. 当前合同下的 QConvergenceLink

| 项目 | 当前反事实判词 |
|---|---|
| `C/I/O/Done` | 该Mathlib模型card通过L2b形式consumer门；source层必须明记为formal ZFC model。 |
| Candidate-Q | `NONE`；有consumer不等于该consumer要求一项未支付的positive obligation。 |
| QConvergenceLink | `Q_NARROW_WITHOUT_CANDIDATE_Q`：取消“中性card没有任何consumer”的笼统说法，同时禁止把formal model层升级为standard ZFC Q。 |
| 后继 | N25C/N25D只消费同一冻结ZFSet card，检查P2/P3，不得重选T/u/F/C。 |
| 停止条件 | 若没有native nontrivial Q、active demand或同一任务Done gap，source card只作control，不进入共同Q。 |

N25A是对P1的真实来源推进，而非单独“发现了Q”。它改善的是候选入口的证据资格，使未来卡必须说清一个consumer
究竟处在标准理论、模型、库还是数学实践哪个层。

## 4. 理念对照、偏差与可推翻条件

| 维度 | 判词 |
|---|---|
| 层级忠实性 | `ALIGNED_WITH_SCOPE`：形式化ZFSet model、其Lean proof/use contract与标准ZFC严格分开。 |
| P/Q共同锻造 | `Q_NARROW_WITHOUT_CANDIDATE_Q`：来源缺口被缩小，Candidate-Q仍为NONE。 |
| 偏差分类 | `ALIGNED`；真实consumer定位修复N24的source gap，未夸张为ZFC语义结论。 |
| 证据边界 | 版本固定source inspection和报告级tracer；没有本仓Lean replay、ZFC一致性或现实过程证据。 |

**falsifier：** 若固定source并非ZFSet形式化模型、或`funs`不实际消费`powerset(prod x y)`、或`mem_funs`不提供所述proof/use contract，则本卡L2b判词应重审。即使该接口成立，也需另有来源事实才能使它成为standard-ZFC或共同Q证据。

## 5. 财富、后继与范围

| 字段 | 记录 |
|---|---|
| `Wealth` | `READY_FOR_FORGE_INTENT`：形式化model consumer可作受控来源卡；其下一步是同卡P2/P3映射或寻找目标层的native Q，不能跳层。 |
| 后继 | N25B跨理论control；N25C P2-A；N25D P3-A。 |
| 自动动作 | 无；不启动新worker、不将ZFSet模型的consumer写成ZFC Q。 |
| current truth effect | `ZFC_SITE_SELECTED / Q-0 UNFORMED / ZFC_Q_NOT_LOCATED`保持。 |
| 审计范围 | 只审N25A source tracer，不审不可见trajectory/reasoning或Mathlib全部实现。 |

**本卡最终判词：** `ALIGNED_WITH_SCOPE / Q_NARROW_WITHOUT_CANDIDATE_Q / QUALIFYING_FORMAL_CONSUMER_WITH_SCOPE / NO_COMMON_Q`。
