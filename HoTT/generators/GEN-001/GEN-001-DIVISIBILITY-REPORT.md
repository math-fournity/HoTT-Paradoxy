# GEN-001-4 · TASK-FAMILY-DIVISIBILITY-CONDITION-OR-CAPABILITY

> 能力验收报告（链贯通），**不是数学结论**。`registers_new_claim: false`，不进
> `HoTT/CLAIM_EVIDENCE_MATRIX.md`。依据：方案修订片 003 §4 + 010 §2（F-011）。
> 供给身份：SUPPLY-004 / SUPPLY-006 / SUPPLY-008（AI 供给 + 强制审计层，
> pending external audit），**不是用户供给**。角色纪律（003 §5 / 009）：
> 任务族由 AI 冻结；Python 只枚举与归约；只有原生核给 oracle verdict。

## 1. 族与前提

| 字段 | 值 |
|---|---|
| task_family | TASK-FAMILY-DIVISIBILITY-CONDITION-OR-CAPABILITY |
| premise 成员 | PREMISE-D-01（区间稠密性）/ PREMISE-E-04（截断塔可延伸）/ PREMISE-G-03（高阶相等无限迭代） |
| 共享 omission shape | 可分性被当作**无条件能力**而非**条件**：「在条件 c 下不可分」在系统内没有对象承担 |
| grammar | `L1-DIVISIBILITY-v1`（delay_index_max 2 / partner 2 / depth 2 / horizons {0,1,2}） |
| 三个新声明 continuation | `divisibility_verdict_capability_is_unbounded` {T:ω, F:ret2F}<br>`divisibility_verdict_no_object_for_condition` {T:ret2T, F:ω}<br>`divisibility_verdict_same_frontier_opposite` {T:ret1T, F:ret1F} |
| 共享校准 continuation | `deliver_business` / `const_omega`（校准延续，011 §2 允许共享） |

三个 continuation 对 17 个既有文法的 continuation map 唯一性 **PASS**（机械复算，
见 `GEN-001-DIVISIBILITY-OUT-OF-ENVELOPE.json`）。

## 2. 执行链（机械可复算）

| 环节 | 结果 |
|---|---|
| inspect-profile | PASS（toolchain / library / source hash 全部对齐 GEN-001-3 同一锁定） |
| create-case | `MS-TASK-GEN001-DIVISIBILITY-001` case-revision-1，CASE_READY |
| search | 7 atoms × 440 contexts = **5,280** checks，separations_seen **916**，remainder **0**，`COMPLETED_WITHIN_BUDGET`，grammar_violations 0 |
| 越界机械检查 | 32 个绑定新 continuation 的规范见证，对 **6 个既有 delay 文法** 共 **192/192** 拒绝，理由**全部唯一 BIND_CONTINUATION**；0 个被任何既有文法接受 |
| 负/正控制 | deadline-same-horizon NOT_SEPARATED（期望达成）；bind_preserves_result_equivalence（期望达成）；grammar sensitivity：移除 deadline op 后见证数 58→48，敏感性确认 |
| 原生核四路校验 | 4 见证 × 4 路 = 全部通过（见 §3） |
| 主 repo 独立复现 | 4 见证全部 exit 0（见 §3） |
| review-correspondence / explain | 4 份 REVIEW_WRITTEN + REPORT_WRITTEN |

规范归约见证分布（58 个）：value_mismatch 24 / completion_divergence 24 /
deadline_observation 10 —— **三机制全覆盖**。绑定新 continuation 的 32 个中，
三个 continuation 各占 8 / 8 / 16。

## 3. 送核见证（3 新构造子 × 3 机制）

四路核 = `verify`（必须 ACCEPTED）/ `controls`（必须 ACCEPTED）/
`negative-control`（必须 exit 42 EXPECTED_TYPE_REJECTION）/ `verify-replay`
（必须精确匹配）。全部在 Cubical Agda 2.8.0 + cubical v0.9 上执行。

| run | witness | 构造子 × 机制 | 语句 | 观察 | 四路核 | 主 repo 复现 |
|---|---|---|---|---|---|---|
| `VERIFY-GEN001-DIVISIBILITY-WV-0025` | WV-0025 | `no_object_for_condition` × completion_divergence | pair (ret 0 false, ret 1 false) — delay-equivalent — under race(□, ret 0 true) → bind(□, λ{true↦ret 2 true; false↦ω}) | ω ≠ ret 3 true | verify 0 / controls 0 / neg 42 / replay 精确 | exit 0 |
| `VERIFY-GEN001-DIVISIBILITY-WV-0026` | WV-0026 | `same_frontier_opposite` × value_mismatch | pair (ret 0 false, ret 1 false) — delay-equivalent — under race(□, ret 0 true) → bind(□, λ{true↦ret 1 true; false↦ret 1 false}) | ret 2 false ≠ ret 2 true | 同上四路全过 | exit 0 |
| `VERIFY-GEN001-DIVISIBILITY-WV-0027` | WV-0027 | `capability_is_unbounded` × completion_divergence | pair (ret 0 false, ret 1 false) — delay-equivalent — under race(□, ret 0 true) → bind(□, λ{true↦ω; false↦ret 2 false}) | ret 3 false ≠ ω | 同上四路全过 | exit 0 |
| `VERIFY-GEN001-DIVISIBILITY-WV-0051` | WV-0051 | `same_frontier_opposite` × deadline_observation | pair (ret 0 false, ret 1 false) — delay-equivalent — under bind(□, λ{true↦ret 1 true; false↦ret 1 false}) → deadline 2 | some false ≠ none | 同上四路全过 | exit 0 |

主 repo 独立复现命令（`HoTT/formal/partiality-race-timeout/`，`--ignore-interfaces` 强制重算）：

```
agda --ignore-interfaces --library-file=AGDA_LIBRARIES -l cubical-0.9 -i . Verify.agda
```

复现前提：该目录新纳入 `MVSupport.agda`（profile 声明的 support source，
sha256 `07ddec58…`），本次随交付物提交。

## 4. 现象新颖性披露（修订片 012 §2 三问）

### Q1 本族的现象在旧文法中是否已可部分表达？—— **是，PARTIAL**

机械可复算证据（本报告 §2 同一引擎，旧文法 continuation + 旧操作）：

| 本族新 continuation | 所属现象形状 | 旧文法是否已有同形状 map | 旧操作能否以该形状分离 delay-equivalent 对 |
|---|---|---|---|
| `capability_is_unbounded` {T:ω, F:ret2F} | 真分支发散 | **是**：`identity_verdict_never_on_true` {T:ω, F:ret0T}（L1-IDENTITY-OBSERVATION-v1） | 是，completion_divergence |
| `no_object_for_condition` {T:ret2T, F:ω} | 假分支发散 | **是**：`deliver_business` {T:ret0T, F:ω}（校准共享构造） | 是，completion_divergence |
| `same_frontier_opposite` {T:ret1T, F:ret1F} | 同延迟相反值 | 部分：同形状 @index 0 已有（`keeping_result` {T:ret0T, F:ret0F}，L1-DELAY-RACE-DEADLINE-v0）；**@index 1 的 map 本身确实是新的** | 是，@0 已可 value_mismatch；@1 给出 bind-then-deadline 分离 |

结论：**文法新颖性干净（唯一 BIND_CONTINUATION），现象新颖性 PARTIAL**。
本族三个 continuation 中，两个是真/假分支发散形状的**索引与取值变体**
（完成分支从"立即"变为"晚两格"，或发散分支的对称方向改变），
第三个是"同延迟相反值"从 index 0 到 index 1 的移位。真正新的东西是**组合**：
一个三 continuation 的 verdict 面板，在**一个族内**用三种机械上可区分的形状
渲染同一个 omission shape（能力 vs 条件），并把"完成分支的分辨率极限"
纳入 verdict 语义。这与 GEN-001-3 的披露结构同型（层依赖现象的一半旧文法已可表达），
按 012 片标 **PARTIAL**，交外部审计复核。

### Q2 新构造子在该现象中承担什么？

它们是 **verdict renderer**：固定理论对"此输入是否可分"的判定内容
（哪一支是"能力可达"的、在哪一格分辨率极限、以什么值）。它们不是标签：
改变 map 就改变被观察的值与索引（WV-0026 的 ret 2 false ≠ ret 2 true 是值差，
WV-0051 的 some ≠ none 是越界差）。但它们所参与的**现象原语**
（单侧发散、同延迟相反值、bind 后越界）各自都已在旧文法可表达。

### Q3 跨族机制重叠 —— 有，登记为 ingress

本族分离机制（race 截断暴露被抹除轮次 / bind 恒守 delay 等价 /
deadline 越界观察）与 GEN-001-1 / -2 / -3 **共享同一机制族**
（value_mismatch / completion_divergence / deadline_observation）。
step-6 审计已对前三族登记 93/93 越界见证全部 delay-equivalent（O-1）；
本族不改变该结论，**族间独立性未证**，登记为 out-of-envelope ingress，不当作结论。

## 5. 同族坍缩（修订片 013 §2.1 Q4）

**判定：共享同一机制 pattern → 登记为 `PATTERN_REDUCED_NOT_CERTIFIED_AS_FULL_TASK_EQUIVALENCE`，只报一个验收单元。**

- **共享的机制层**：D-01 / E-04 / G-03 在 delay 片段内**无可观察差异**。
  三者的区分层是**全理论中承载"无界可分能力"的构造**（区间 / 截断塔 /
  identity type 的可迭代性），而 delay 片段没有区间、没有截断塔、
  没有高阶 path 迭代——三者全部投影到同一个形状：
  「无界 delay 能力 vs 有界观察层」。
- **证据**：本族 search 的 916 个分离、58 个规范见证中，**没有任何一个**
  能把 D-01 与 E-04 或 G-03 区分开——片段里根本没有区分它们的对象。
  三个 continuation 表达的是**同一个 omission shape 的三个 facet**
  （哪一支发散 / 完成分支的延迟 / 前沿索引），不是三个成员的独立编码。
- **因此**：`GEN-001-4` 是**一个**验收单元（三成员作为该 pattern 的实例列出）。
  D-01 / E-04 / G-03 的**任务等价性未被证明**（CE-MAP 的归约标准要求
  机器可复算的机制层差异，本片段无法提供）。
- **外部审计须知**：这三条是 PREMISE-001/006 中 corpus_self_audit 最高的一批
  （G-03 三重诱导：语料流利 + 004 表导航 + 用户路径同形；D-01/E-04 同族诱导）。
  本报告的**前提判定**（ai_verdict=非现实）全部 `AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT`，
  本链只验收"该 omission shape 可被机器枚举与原生核校验"，**不升级前提判定**。

## 6. 方向覆盖声明（修订片 013 §2.2）

本族的分离机制属**方向 B**（delay-equivalent 对 + 观察层不同意）。
方向 A（现实可完成、理论化引入额外完成困难）在 delay 片段内**无对象承担**
（引擎 `_witness_separates` 的前置条件即 `delay_equivalent`）。
故本报告**不声称覆盖方向 A**。登记：`DIRECTION_A_UNREPRESENTABLE_IN_DELAY_FRAGMENT`。

## 7. 禁止外推

- 本报告**不声称** D-01 / E-04 / G-03 前提非现实（pending external audit）。
- 本报告**不声称**引擎具备自主发现新方向的能力（任务族由 AI 冻结供给）。
- 本报告**不声称**三成员的任务等价性（§5 PATTERN_REDUCED）。
- 本报告**不声称**开放候选空间被穷尽；也不声称 delay 片段能表达区间稠密性、
  截断塔或高阶迭代——这些都需要该片段不具备的构造（列为 V2 候选）。
- 本链是**能力验收**（GEN-001 有界生成器验收单元），不是数学结论；
  任何探索实例都不得升级为新数学主张（003 §5）。

## 8. 证据定位

- 文法：`GEN-001-DIVISIBILITY-GRAMMAR.json`
- 分母 / 枚举 / remainder / 归约：`GEN-001-DIVISIBILITY-ENUMERATION.json`
- 越界机械证明（32 行 × 6 旧 delay 文法）：`GEN-001-DIVISIBILITY-OUT-OF-ENVELOPE.json`
- 原生核收据（F-011 五件套）：
  `../../verification/runs/VERIFY-GEN001-DIVISIBILITY-WV-{0025,0026,0027,0051}/`
- 引擎内完整收据（含 correspondence review / report / runner snapshot）：
  `/Volumes/D/HoTT-machine-overview/machine-overview/runs/`（同 repo 的
  `feat/machine-overview-m1` 工作树）：`SEARCH-GEN001-DIVISIBILITY-001`、
  `VERIFY-GEN001-DIVISIBILITY-{001,WV-0025,WV-0026,WV-0027,WV-0051}`
- 任务规格：`machine-overview/tasks/MS-TASK-GEN001-DIVISIBILITY-001.json`（同工作树）
- 前提判定原文：`.codex/research/hott/PREMISE-001/006`（D-01 / E-04 / G-03 条目）
- step-6 审计：`audit/PREMISE-001-STEP6-OMISSION-AUDIT-20260916.md`（O-3 由本报告 §5 答复）
