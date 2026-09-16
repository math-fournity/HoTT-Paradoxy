# PREMISE-001 step-6 omission audit（GEN-001 三族之后的信封外 unknown ingress 登记）

日期：2026-09-16（UTC）
审计对象：PREMISE-001 step-5 已完成的三族 GEN-001 验收单元（E-02 / A-03 / B-01）的**机制空间与覆盖阴影**，不是条目内容。
审计身份：角色 A（AI）结构检索层 + 修订片 009 的强制审计层。**本审计不做 P3/P4 判定，不产生数学结论**（F-011 / MATH_PROOF_BEFORE_DELIVERY_V1）。
触发条件：AGENTS `HOTT_PARADOX_PROGRAMMATIC_COMPLETENESS_V1`「每个 bounded pass 结束必须执行遗漏审计并至少使用一个独立 taxonomy/source/framework/holdout」；
SOP `hott-paradox-search-sop` §5 反思清单第 5 条（信封外候选不得静默丢弃）；
完备性规划 004 片 §六（每轮 Completeness Audit）。

## 一、为什么本轮审计必须换独立来源

step-1 的遗漏审计（`audit/PREMISE-001-V1信封外遗漏审计-20260916.md`）用 `CORE_RULES C01–C18` + `EXTENSIONS E01–E15` 差分**分母**（前提空间）。
本轮审计对象不同：不是"哪些前提没进分母"，而是"**已完成的三个 GEN-001 验收单元在机制空间上留下了什么阴影**"。
因此必须换独立 taxonomy。本轮使用三个独立来源，全部不是建分母用的那一个：

| 独立来源 | 锚点 | 本轮用作什么 |
|---|---|---|
| CE-MAP internalisation 类归约（`audit/CE-MAP机器统观八轴映射与同型归约-20260915.md` §5） | C-228/229/230、C-234/235、C-240；判词 `PATTERN_REDUCED_NOT_CERTIFIED_AS_FULL_TASK_EQUIVALENCE` | 独立 taxonomy：机器已把 6 个候选归约为**一个机制 pattern**（scope promotion）。用来检验三族是否也是同型重复计数 |
| 引擎语义本身（`machine_overview/model.py` / `search.py`，本审计独立复算） | `_witness_separates` 前置 `delay_equivalent`；`separation_kind` 只有 3 值 | 独立 framework：delay 片段的分离机制空间是否已被三族耗尽 |
| 2LTT 自然消费者工作（`audit/2LTT纤维替换自然消费者与crisp退化纤维性消融-20260915.md`） | 判词 `NATURAL_CONSUMERS_FOUND / QUALIFICATION_SCOPE_WIDENING_CAUSES_COLLAPSE / RESTRICTED_INTERFACES_COMPLETE_REAL_TASKS` | 独立 holdout：一个**方向 A**形状的真实候选，检验 GEN-001 链能否消费它 |

## 二、发现

### O-1（机制重叠，三族同型）三族的越界见证 100% 是 delay-equivalent 对，共享同一分离机制族

本审计独立复算（不是引用报告自述）：

| 族 | 越界见证数 | delay-equivalent 对 | value_mismatch | deadline_observation | completion_divergence |
|---|---:|---:|---:|---:|---:|
| E-02（WITNESS-RECOVERABILITY） | 3 | 3/3 | 2 | 1 | 0 |
| A-03（COMPLETION-PROCESS） | 46 | 46/46 | 28 | 10 | 8 |
| B-01（IDENTITY-OBSERVATION-LAYER） | 44 | 44/44 | 28 | 8 | 8 |

证据：`HoTT/generators/GEN-001/GEN-001-{,COMPLETION-PROCESS-,IDENTITY-OBSERVATION-}OUT-OF-ENVELOPE.json` 的 `rows[]`，
逐行 `value_from_json(pair)` 后调 `machine_overview.model.delay_equivalent`（本审计在 worktree 内独立运行，非引用报告数字）。

结构性原因（引擎语义，非巧合）：`search.py:180` 的 `_witness_separates` 前置条件就是
`delay_equivalent(left, right)`——**只有理论判为同一的对才可能成为分离见证**。
因此 delay 片段内**一切**分离天然是"理论识别了一对、某个观察层不同意"的形状，
即 B-01/方向 B 的前提结构。这与 LESSONS 130/131 的记录一致，且现在被三族数据独立确认。

**归类**：`UI-05`（跨 family/version 差分）+ 反遗漏技术 #5（metamorphic：delay 等价是不变量）。
**这不是缺陷**：三族的**文法新颖性**成立（越界理由唯一 BIND_CONTINUATION，机械 PASS），
按修订片 012，**现象新颖性**必须逐族披露——三族的现象新颖性都是 PARTIAL 或更低，
因为"观察层读取被同一性判据抹除的信息"这一现象在 E-02 首族文法中已可表达。

**处置**：登记为 ingress，不删族、不重跑。**族间独立性未证**，继续作为外部审计的优先复核点。
同时给出可证伪条件：若未来在 delay 片段内构造出一个分离见证，其对**不是** delay-equivalent，
则本结论失效（当前引擎语义下不可能，故该条件也等于"引擎换了片段"）。

### O-2（覆盖阴影）delay 片段无法表达方向 A 的候选——一个真实方向 A 候选已在信封外

delay 片段的分离要求 delay-equivalent 对，故只能表达**方向 B**（现实不可完成却把理论对象当作已获得能力）。
**方向 A**（现实可完成而理论化引入额外完成困难）在该片段内**没有对象承担**。

独立 holdout 证据：2LTT 自然消费者工作找到一个真实方向 A 候选——
"未受限内部化"失败，而**受限接口（crisp/global input、degenerate replacement、pointwise fibrant diagram）
完成同一真实任务**（判词 `RESTRICTED_INTERFACES_COMPLETE_REAL_TASKS`，`audit/2LTT纤维替换自然消费者与crisp退化纤维性消融-20260915.md`）。
这正是方向 A 的形状：现实侧（受限输入）可完成，理论侧（无界提升）引入额外困难。
该候选**无法**被当前 GEN-001 链消费，因为 GEN-001 的验收单元全部建在 delay 片段上。

**归类**：`UI-04`（当前 oracle/observation 无法表达的现象）+ 反遗漏技术 #12（coverage shadow）。
**处置**：登记为 ingress，记 `DIRECTION_A_UNREPRESENTABLE_IN_DELAY_FRAGMENT`。
**这是对"机器统观覆盖了两个方向"这一潜在误读的预防**：当前只覆盖方向 B。
修复路径（登记，不由本轮执行）：要么在 delay 片段加一个"现实侧可完成"的正控制轴，
要么把方向 A 候选放到 symbolic/其他片段上跑。二者都超出本轮授权范围（改动冻结引擎）。

### O-3（同族坍缩风险）DIVISIBILITY 三联可能是一个机制，不是三个

CE-MAP 的独立 taxonomy 给出了先例：C-228/229/230、C-234/235、C-240 六个候选被归约为
**一个**机制 pattern（scope promotion：external/pointwise/fiberwise → internal/uniform），
判词 `PATTERN_REDUCED_NOT_CERTIFIED_AS_FULL_TASK_EQUIVALENCE`（`audit/CE-MAP...` §5.1）。
即：机器搜索会把同机制多 consumer 计为多个"新发现"，必须显式归约。

DIVISIBILITY 三联（D-01 区间 / E-04 截断塔 / G-03 高阶路径）在 P3/P4 审计中自评
corpus 风险最高（KC-000043 阻力最强处，三重诱导：语料流利 + 004 表导航 + 用户路径同形），
且 004 表把三者**全部**标为 continuity。若三者共享"可分性被当作能力而非条件"这一个机制，
则跑三个 GEN-001 单元会产出三份同型报告，构成 O-1 式的重复计数放大。

**归类**：`UI-04` + 反遗漏技术 #11（counter-hypothesis：三者可能同型）。
**处置**：**不预先判定**同型（那是 P3/P4，且三条的 P3/P4 已完成、pending 外部审计）。
但要求：**跑 DIVISIBILITY 时必须显式携带同族坍缩披露**——
在 REPORT 里分答修订片 012 §2 三问之外，加答"三成员是否共享同一机制 pattern"，
并在发现共享时按 CE-MAP 先例登记 `PATTERN_REDUCED_NOT_CERTIFIED_AS_FULL_TASK_EQUIVALENCE`，
而不是报三个独立验收单元。

### O-4（信封外入口存在性）开放世界 ingress 清单

按完备性规划 004 片 §二 的七类 UnknownIngress，本轮登记/更新：

| ID | 入口 | 本轮状态 | 处置 |
|---|---|---|---|
| `UI-01` | 新论文/定理/正式化项目 | 未新增（本轮无新来源接入） | 保持；V2 扩版时优先 |
| `UI-02` | 社区实现新版本 | 未新增（Agda 2.8.0 / cubical v0.9 仍为固定工具链） | 保持 |
| `UI-03` | 新自然 consumer | 已有：2LTT 四类真实消费者（LOPS 2018 / Boulier–Tabareau / Swan–Uemura / Reedy） | 登记为 O-2 的 holdout 证据；不进 V1 |
| `UI-04` | 当前 oracle 无法表达的现象 | **新增 2 条**：O-2（方向 A 不可表达）、O-3（同族坍缩未归约） | 本文件登记 |
| `UI-05` | 跨 family/version 差分 | **新增 1 条**：O-1（三族机制重叠） | 本文件登记 |
| `UI-06` | 新反例/正实例/防线 | 未新增（三族的负控制仍为 EXPECTED，无假阳/假阴） | 保持 |
| `UI-07` | 用户语义新修正 | 未新增（KC-000044–046 已进 generation-7，无新修正） | 保持 |

## 三、范围限定——防止三族的"链贯通"被过度解读

三族 `GENERATOR_LINK_DEMONSTRATED_WITH_SCOPE` 的有效范围是：
**给定一个 AI 冻结的任务族，引擎能在声明文法上完整枚举、归约、产出越界见证、并经原生核四路校验。**

它**不覆盖**：
- 方向 A 的候选（见 O-2）；
- 三个任务族在机制层面相互独立（见 O-1）；
- DIVISIBILITY 三联是三个独立现象（见 O-3）；
- 引擎具备自主发现新方向的能力（任务族由 AI 冻结供给，修订片 003 §5 角色纪律）；
- HoTT 全部前提空间（分母 V1 的 remainder=0 只覆盖 A–G 35 条，见 step-1 审计 §四）。

任何把"三族链贯通"读成"机器统观已能发现新悖论"或"两个方向都被覆盖"的推断都超出声明范围。

## 四、处置裁决（SOP §S-5）

- **裁决：`revised`**——需要一次方案修订（不是 no-plan-change）。
  理由：O-2（方向 A 不可表达）与 O-3（同族坍缩）都是**当前方案条款没有要求披露的缺口**，
  会让后续族的报告把覆盖阴影读成覆盖。修订见 `Atria的方案/修订片/013`。
- **ingress 全部登记**：O-1（UI-05）、O-2（UI-04）、O-3（UI-04）、UI-03 更新；不静默丢弃。
- **不重跑三族**：O-1 的披露已在三族 REPORT / FRONTIER / LESSONS 中留痕，
  按 修订片 012 §4「已验收三族按 §4 回填披露不重跑」执行；本审计补的是**跨族层面**的披露，三族报告本身不改。
- **避免重复审计**：本文件 §二 的三来源差分已执行一次；下一 session 不必重跑，直接读 §二/§三。

## 五、证据定位

| 断言 | 证据 |
|---|---|
| 三族越界见证全部 delay-equivalent | 本审计独立运行：`GEN-001-{,COMPLETION-PROCESS-,IDENTITY-OBSERVATION-}OUT-OF-ENVELOPE.json` 的 `rows[]` × `machine_overview.model.delay_equivalent`（worktree `/Volumes/D/HoTT-machine-overview`） |
| 分离机制只有 3 类 | `machine_overview/model.py:separation_kind`（deadline_observation / completion_divergence / value_mismatch） |
| delay-equivalent 是见证前置条件 | `machine_overview/search.py:180` `_witness_separates` |
| bind 恒守 delay 等价 | `machine_overview/model.py:bind_value` + LESSONS 130；本审计复算 positive control `bind_preserves_result_equivalence` 三族均 preserved=True |
| CE-MAP 6 候选归约为 1 pattern | `audit/CE-MAP机器统观八轴映射与同型归约-20260915.md` §5.1 |
| 方向 A 真实候选存在 | `audit/2LTT纤维替换自然消费者与crisp退化纤维性消融-20260915.md` 判词行 + 统一 TaskSpec 表 |
| 三族判词与收据 | `HoTT/generators/GEN-001/GEN-001-INDEX.md`；`HoTT/verification/runs/20260916-VERIFY-GEN001-*` |
| 本审计对应 STATE | revision 163，status `PREMISE_001_STEP5_GEN001_IDENTITY_OBSERVATION_DONE` |

## 六、本审计不声称

- 不声称三族的 P3/P4 判定被推翻（全部仍 `AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT`）。
- 不声称 DIVISIBILITY 三联**确实**同型（O-3 只登记风险与披露要求，不做判定）。
- 不声称方向 A 的 2LTT 候选是"非现实前提"（那是 P3/P4 + GEN-001 + 原生核才能升级的结论）。
- 不声称本审计穷尽了开放世界 ingress（§二 的四条只是本轮可发现的；UI-01/02/06/07 的"未新增"是本轮观察，不是不存在）。
- 本审计无数学结论（F-011；无命题被交付，MATH_PROOF_BEFORE_DELIVERY_V1 不适用）。
