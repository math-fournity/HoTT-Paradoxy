# GEN-001-5 · TASK-FAMILY-EXISTENCE-VERSUS-AVAILABILITY

> 能力验收报告（链贯通），**不是数学结论**。`registers_new_claim: false`，不进
> `HoTT/CLAIM_EVIDENCE_MATRIX.md`。依据：方案修订片 003 §4 + 010 §2（F-011）。
> 供给身份：SUPPLY-005 / SUPPLY-009（AI 供给 + 强制审计层，
> pending external audit），**不是用户供给**。角色纪律（003 §5 / 009）：
> 任务族由 AI 冻结；Python 只枚举与归约；只有原生核给 oracle verdict。

## 0. 前提置信度披露（本族专属）

**D-04（Kan 填充）/ G-05（cofibration 可填充设为构造可用）是 PREMISE-001/006 中
置信度最低的一对，并被 PREMISE-001/006 明确标注为「本批中最可能被推翻为『现实』的两条」。**
理由（原文）：可填充性在 cubical 类型论中是 cofibration 的**定义条件**——
成为 cofibration 就意味着可填充；物理产能的排队属于实现层（域外）。
本族的前提判定（ai_verdict=非现实）全部保持 `AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT`，
**本链不升级该判定**。外部审计应优先复核本族。

## 1. 族与前提

| 字段 | 值 |
|---|---|
| task_family | TASK-FAMILY-EXISTENCE-VERSUS-AVAILABILITY |
| premise 成员 | PREMISE-D-04（Kan 填充：存在当作已就位）/ PREMISE-G-05（所有 cofibration 可填充设为构造可用） |
| 共享 omission shape | **存在性被当作可调用的构造资源**（存在=就位）；「存在性 → 可用性」之间的**供给过程**被省略 |
| grammar | `L1-EXISTENCE-v1`（delay_index_max 2 / partner 2 / depth 2 / horizons {0,1,2}） |
| 三个新声明 continuation | `existence_verdict_exists_but_never_available` {T:ω, F:ret1F}<br>`existence_verdict_supply_without_object` {T:ret1F, F:ω}<br>`existence_verdict_avail_opposite_at_frontier` {T:ret2T, F:ret2F} |
| 共享校准 continuation | `deliver_business` / `const_omega`（校准延续，011 §2 允许共享） |

三个 continuation 对 **19 个既有文法**（含 `L1-DIVISIBILITY-v1`）的 continuation map
唯一性 **PASS**，且三者在 map 层**互不相同**（机械复算，见
`GEN-001-EXISTENCE-OUT-OF-ENVELOPE.json`）。

## 2. 执行链（机械可复算）

| 环节 | 结果 |
|---|---|
| inspect-profile | PASS（toolchain / library / source hash 全部对齐 GEN-001-4 同一锁定） |
| create-case | `MS-TASK-GEN001-EXISTENCE-001` case-revision-1，CASE_READY |
| search | 7 atoms × 440 contexts = **5,280** checks，separations_seen **916**，remainder **0**，`COMPLETED_WITHIN_BUDGET`，grammar_violations 0；order_independence_check 统计一致、集合相等 |
| 越界机械检查 | 32 个绑定新 continuation 的规范见证，对 **7 个既有 delay 文法**（含 `L1-DIVISIBILITY-v1`）共 **224/224** 拒绝，理由**全部唯一 BIND_CONTINUATION**；0 个被任何既有文法接受 |
| 负/正控制 | deadline-same-horizon NOT_SEPARATED（期望达成）；bind_preserves_result_equivalence（期望达成）；grammar sensitivity：移除 deadline op 后 contexts 440→380、checks 5280→4560，敏感性确认 |
| 原生核四路校验 | 4 见证 × 4 路 = 全部通过（见 §3） |
| 主 repo 独立复现 | 4 见证全部 exit 0（见 §3） |
| review-correspondence / explain | 4 份 REVIEW_WRITTEN + REPORT_WRITTEN |

规范归约见证分布（58 个）：value_mismatch 24 / completion_divergence 24 /
deadline_observation 10 —— **三机制全覆盖**。绑定新 continuation 的 32 个中，
三个 continuation 各占 12 / 12 / 8。

## 3. 送核见证（3 新构造子 × 3 机制）

四路核 = `verify`（必须 ACCEPTED）/ `controls`（必须 ACCEPTED）/
`negative-control`（必须 exit 42 EXPECTED_TYPE_REJECTION）/ `verify-replay`
（必须精确匹配）。全部在 Cubical Agda 2.8.0 + cubical v0.9 上执行。

| run | witness | 构造子 × 机制 | 语句 | 观察 | 四路核 | 主 repo 复现 |
|---|---|---|---|---|---|---|
| `VERIFY-GEN001-EXISTENCE-WV-0017` | WV-0017 | `supply_without_object` × completion_divergence | pair (ret 0 false, ret 1 false) — delay-equivalent — under race(□, ret 0 true) → bind(□, λ{true↦ret 1 false; false↦ω}) | ω ≠ ret 2 false | verify 0 / controls 0 / neg 42 / replay 精确 | exit 0 |
| `VERIFY-GEN001-EXISTENCE-WV-0018` | WV-0018 | `exists_but_never_available` × completion_divergence | pair (ret 0 false, ret 1 false) — delay-equivalent — under race(□, ret 0 true) → bind(□, λ{true↦ω; false↦ret 1 false}) | ret 2 false ≠ ω | 同上四路全过 | exit 0 |
| `VERIFY-GEN001-EXISTENCE-WV-0043` | WV-0043 | `exists_but_never_available` × deadline_observation | pair (ret 0 false, ret 1 false) — delay-equivalent — under bind(□, λ{true↦ω; false↦ret 1 false}) → deadline 2 | some false ≠ none | 同上四路全过 | exit 0 |
| `VERIFY-GEN001-EXISTENCE-WV-0051` | WV-0051 | `avail_opposite_at_frontier` × value_mismatch | pair (ret 0 false, ret 1 false) — delay-equivalent — under race(□, ret 0 true) → bind(□, λ{true↦ret 2 true; false↦ret 2 false}) | ret 3 false ≠ ret 3 true | 同上四路全过 | exit 0 |

主 repo 独立复现命令（`HoTT/formal/partiality-race-timeout/`，`--ignore-interfaces` 强制重算）：

```
agda --ignore-interfaces --library-file=AGDA_LIBRARIES -l cubical-0.9 -i . Verify.agda
```

复现前提：该目录已有 `MVSupport.agda`（GEN-001-4 随交付物纳入的 support source，
sha256 `07ddec58…`）；本族生成的 `Proof.agda` 导入它，主 repo 复现输出可见
`Checking MVSupport`。

## 4. 现象新颖性披露（修订片 012 §2 三问）

### Q1 本族的现象在旧文法中是否已可部分表达？—— **是，PARTIAL**

机械可复算证据（本报告 §2 同一引擎，旧文法 continuation + 旧操作）：

| 本族新 continuation | 所属现象形状 | 旧文法是否已有同形状 map | 旧操作能否以该形状分离 delay-equivalent 对 |
|---|---|---|---|
| `exists_but_never_available` {T:ω, F:ret1F} | 真分支发散 | **是**：`identity_verdict_never_on_true` {T:ω, F:ret0T}（L1-IDENTITY-OBSERVATION-v1）；`divisibility_verdict_capability_is_unbounded` {T:ω, F:ret2F}（L1-DIVISIBILITY-v1） | 是，completion_divergence |
| `supply_without_object` {T:ret1F, F:ω} | 假分支发散 | **是**：`deliver_business` {T:ret0T, F:ω}（校准共享构造）；`divisibility_verdict_no_object_for_condition` {T:ret2T, F:ω}（L1-DIVISIBILITY-v1） | 是，completion_divergence |
| `avail_opposite_at_frontier` {T:ret2T, F:ret2F} | 同延迟相反值 | 部分：同形状 @index 0 已有（`keeping_result` {T:ret0T, F:ret0F}，L1-DELAY-RACE-DEADLINE-v0）、@index 1 已有（`divisibility_verdict_same_frontier_opposite` {T:ret1T, F:ret1F}，L1-DIVISIBILITY-v1）；**@index 2 的 map 本身确实是新的** | 是，@0/@1 已可 value_mismatch；@2 因 bind 后累加索引 ≥3 而不能被 deadline 分离，只能由 race 分离 |

结论：**文法新颖性干净（唯一 BIND_CONTINUATION），现象新颖性 PARTIAL**。
本族三个 continuation 全部是真/假分支发散形状与同延迟相反值形状的**索引与取值变体**——
这与 GEN-001-4（DIVISIBILITY）的披露同型，且本族的索引空间被前四族进一步填密
（@index 1 的真/假分支发散与同延迟相反值均已被 GEN-001-4 占用，本族必须退到
@index 1 的假分支晚负值与 @index 2 的同延迟相反值）。真正新的东西仍是**组合**：
一个三 continuation 的 verdict 面板，在**一个族内**用三种机械上可区分的形状
渲染同一个 omission shape（存在=可用），并把「可用性窗口」与「供给延迟」
纳入 verdict 语义。按 012 片标 **PARTIAL**，交外部审计复核。

### Q2 新构造子在该现象中承担什么？

它们是 **verdict renderer**：固定理论对「此输入的存在是否等同于可用」的判定内容
（哪一支是「存在但不可用」、可用性判决在哪一格到达、以什么值）。它们不是标签：
改变 map 就改变被观察的值与索引（WV-0051 的 ret 3 false ≠ ret 3 true 是值差，
WV-0043 的 some false ≠ none 是越界差，WV-0017/0018 的 ω ≠ ret 2 false 是完成差）。
但它们所参与的**现象原语**（单侧发散、同延迟相反值、bind 后越界）
各自都已在旧文法可表达。

### Q3 跨族机制重叠 —— 有，登记为 ingress

本族分离机制（race 截断暴露被抹除轮次 / bind 恒守 delay 等价 /
deadline 越界观察）与 GEN-001-1 / -2 / -3 / -4 **共享同一机制族**
（value_mismatch / completion_divergence / deadline_observation）。
step-6 审计已对前四族登记越界见证全部 delay-equivalent；本族不改变该结论，
**族间独立性未证**，登记为 out-of-envelope ingress，不当作结论。

## 5. 同族坍缩（修订片 013 §2.1 Q4）

**判定：D-04 / G-05 在 delay 片段内共享同一机制 pattern → 登记为
`PATTERN_REDUCED_NOT_CERTIFIED_AS_FULL_TASK_EQUIVALENCE`，只报一个验收单元。**

- **共享的机制层**：D-04 与 G-05 的区分层是**全理论中承载「存在即构造可用」的构造**
  （Kan composition 的填充物资源性 / cofibration 定义条件的可填充性），
  而 delay 片段没有 cofibration 结构、没有 composition 操作、没有资源消耗语义——
  两者投影到同一个形状：「存在性判决被当作可调用资源，而供给过程不可观察」。
- **证据**：本族 search 的 916 个分离、58 个规范见证中，**没有任何一个**
  能把 D-04 与 G-05 区分开——片段里根本没有区分它们的对象。
  三个 continuation 表达的是**同一个 omission shape 的三个 facet**
  （哪一支发散 / 可用性判决的延迟 / 前沿索引），不是两个成员的独立编码。
- **因此**：`GEN-001-5` 是**一个**验收单元（两成员作为该 pattern 的实例列出）。
  D-04 / G-05 的**任务等价性未被证明**。
- **外部审计须知**：本族与 GEN-001-4 的关键差别在于**前提置信度**。
  GEN-001-4 的三成员是 corpus 风险最高的一批（语料流利性诱导）；
  本族的两成员是**形式层理由最弱**的一批（可填充性是定义条件）。
  两种风险方向相反，外部审计应分别复核：
  - GEN-001-4：AI 是否因语料熟悉度而**过度判定为非现实**；
  - GEN-001-5：AI 是否因形式层定义的强度而**漏判了现实不对应**。

## 6. 方向覆盖声明（修订片 013 §2.2）

本族的分离机制属**方向 B**（delay-equivalent 对 + 观察层不同意）。
方向 A（现实可完成、理论化引入额外完成困难）在 delay 片段内**无对象承担**
（引擎 `_witness_separates` 的前置条件即 `delay_equivalent`）。
故本报告**不声称覆盖方向 A**。登记：`DIRECTION_A_UNREPRESENTABLE_IN_DELAY_FRAGMENT`。

## 7. 禁止外推

- 本报告**不声称** D-04 / G-05 前提非现实（pending external audit；§0 置信度最低）。
- 本报告**不声称**引擎具备自主发现新方向的能力（任务族由 AI 冻结供给）。
- 本报告**不声称**两成员的任务等价性（§5 PATTERN_REDUCED）。
- 本报告**不声称**开放候选空间被穷尽；也不声称 delay 片段能表达 Kan composition、
  cofibration 结构或资源调度——这些都需要该片段不具备的构造（列为 V2 候选）。
- 本链是**能力验收**（GEN-001 有界生成器验收单元），不是数学结论；
  任何探索实例都不得升级为新数学主张（003 §5）。

## 8. 证据定位

- 文法：`GEN-001-EXISTENCE-GRAMMAR.json`
- 分母 / 枚举 / remainder / 归约：`GEN-001-EXISTENCE-ENUMERATION.json`
- 越界机械证明（32 行 × 7 旧 delay 文法）：`GEN-001-EXISTENCE-OUT-OF-ENVELOPE.json`
- 原生核收据（F-011 五件套）：
  `../../verification/runs/VERIFY-GEN001-EXISTENCE-WV-{0017,0018,0043,0051}/`
  （各含 RUN.json / ATTEMPT.json / runner-manifest.json / kernel 四路五件套 /
  generated sources / main-repo-replay exit 0）
- 引擎内完整收据（含 correspondence review / report / runner snapshot）：
  `/Volumes/D/HoTT-machine-overview/machine-overview/runs/`（同 repo 的
  `feat/machine-overview-m1` 工作树）：`SEARCH-GEN001-EXISTENCE-001`、
  `VERIFY-GEN001-EXISTENCE-{WV-0017,WV-0018,WV-0043,WV-0051}`
- 任务规格：`machine-overview/tasks/MS-TASK-GEN001-EXISTENCE-001.json`（同工作树）
- 前提判定原文：`.codex/research/hott/PREMISE-001/006`（D-04 / G-05 条目，含低置信度标注）
- step-6 审计：`audit/PREMISE-001-STEP6-OMISSION-AUDIT-20260916.md`
