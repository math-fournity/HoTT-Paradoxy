# PREMISE-001 step-6 omission audit（GEN-001 五族之后的信封外 unknown ingress 登记）

日期：2026-09-16（UTC）
审计对象：PREMISE-001 step-5 已完成的**五族** GEN-001 验收单元
（E-02 / A-03 / B-01 / D-01·E-04·G-03 / D-04·G-05）的**机制空间与覆盖阴影**，不是条目内容。
审计身份：角色 A（AI）结构检索层 + 修订片 009 的强制审计层。
**本审计不做 P3/P4 判定，不产生数学结论**（F-011 / MATH_PROOF_BEFORE_DELIVERY_V1）。
触发条件：AGENTS `HOTT_PARADOX_PROGRAMMATIC_COMPLETENESS_V1`
「每个 bounded pass 结束必须执行遗漏审计并至少使用一个独立 taxonomy/source/framework/holdout」；
SOP `hott-paradox-search-sop` §5 反思清单第 5 条（信封外候选不得静默丢弃）；
完备性规划 004 片 §六（每轮 Completeness Audit）；修订片 013 §2.3（本轮起 step-6 最低内容）。

## 一、本轮审计的独立来源（全部不是建分母用的那一个）

| 独立来源 | 锚点 | 本轮用作什么 |
|---|---|---|
| **delay 片段 continuation map 空间清单（本轮新增，定量）** | 49 格 map 空间（7 branch 形状有序对）；8 个含 continuation 文法的 `bind_continuations[]` 去重 | **独立 framework**：穷尽枚举 delay 片段在当前声明界下的 continuation map 全空间，算覆盖率与剩余生产力。这不是分母（前提空间）的复用，而是**生成侧对象空间**的首次定量 |
| 引擎语义本身（`machine_overview/model.py` / `search.py`，本审计独立复算） | `_witness_separates` 前置 `delay_equivalent`（search.py:180）；`separation_kind` 只有 3 值；`bind_value` 索引累加 | 独立 framework：机制空间是否已被五族耗尽；bind 索引累加对 deadline 分离的结构性禁止 |
| 五族交付物本身的差分（各族 OUT-OF-ENVELOPE.json 的 `rows[]` 逐行复算） | 32+44+46+3+… 越界见证；机制分布 24/24/10 等 | 独立 taxonomy：跨族机制差分（本轮五族，前轮三族） |
| 2LTT 自然消费者工作（`audit/2LTT纤维替换自然消费者与crisp退化纤维性消融-20260915.md`） | 判词 `RESTRICTED_INTERFACES_COMPLETE_REAL_TASKS` | 独立 holdout：一个**方向 A**形状的真实候选，检验 GEN-001 链能否消费它（沿用前轮，本轮复核仍未被消费） |

## 二、发现

### O-1（机制重叠，五族同型）越界见证 100% 是 delay-equivalent 对，共享同一分离机制族

本审计独立复算（不是引用报告自述）：五族全部越界见证的 pair 经
`machine_overview.model.delay_equivalent` 判定**全部**为 delay-equivalent；
机制分布只有 `value_mismatch` / `completion_divergence` / `deadline_observation` 三类。

| 族 | 越界见证数 | delay-equivalent | value_mismatch | deadline_observation | completion_divergence |
|---|---:|---:|---:|---:|---:|
| E-02（WITNESS-RECOVERABILITY） | 3 | 3/3 | 2 | 1 | 0 |
| A-03（COMPLETION-PROCESS） | 46 | 46/46 | 28 | 10 | 8 |
| B-01（IDENTITY-OBSERVATION-LAYER） | 44 | 44/44 | 28 | 8 | 8 |
| D-01·E-04·G-03（DIVISIBILITY，GEN-001-4） | 32 | 32/32 | 12 | 4 | 16 |
| D-04·G-05（EXISTENCE，GEN-001-5） | 32 | 32/32 | 12 | 4 | 16 |

后两族的机制分布**完全相同**（12/4/16），进一步支持 O-5 的现象饱和结论。

结构性原因（引擎语义，非巧合）：`search.py:180` 的 `_witness_separates` 前置条件就是
`delay_equivalent(left, right)`——**只有理论判为同一的对才可能成为分离见证**。
因此 delay 片段内**一切**分离天然是"理论识别了一对、某个观察层不同意"的形状，
即方向 B 的前提结构。五族数据（157 个越界见证）独立确认。

**归类**：`UI-05`（跨 family/version 差分）+ 反遗漏技术 #5（metamorphic：delay 等价是不变量）。
**这不是缺陷**：五族的**文法新颖性**成立（越界理由唯一 BIND_CONTINUATION，机械 PASS：
GEN-001-5 为 224/224）。**现象新颖性**逐族披露，五族全部 PARTIAL 或更低。
**处置**：登记为 ingress，不删族、不重跑。**族间独立性未证**，继续作为外部审计优先复核点。
可证伪条件（沿用前轮）：若在 delay 片段内构造出对**不是** delay-equivalent 的分离见证，
本结论失效（当前引擎语义下不可能，故该条件等于"引擎换了片段"）。

### O-2（覆盖阴影）delay 片段无法表达方向 A 的候选——真实方向 A 候选仍在信封外

沿用前轮结论。delay 片段的分离要求 delay-equivalent 对，故只能表达**方向 B**。
**方向 A**（现实可完成而理论化引入额外完成困难）在该片段内**没有对象承担**。
2LTT holdout（受限接口完成同一真实任务）**仍未被** GEN-001 链消费。
**归类**：`UI-04`。**处置**：保持登记 `DIRECTION_A_UNREPRESENTABLE_IN_DELAY_FRAGMENT`。
race-截断机制重叠输入已积累到**五个**（五族）。

### O-3（同族坍缩）已由两族执行确认——两个多成员族全部坍缩

前轮只登记风险（DIVISIBILITY 三联可能同型）。本轮两个多成员族都已执行并给出判定：

| 族 | 成员 | 判定 | 判词 |
|---|---|---|---|
| GEN-001-4（DIVISIBILITY） | D-01 / E-04 / G-03（三成员） | **共享同一机制 pattern** | `PATTERN_REDUCED_NOT_CERTIFIED_AS_FULL_TASK_EQUIVALENCE`，只报一个验收单元 |
| GEN-001-5（EXISTENCE） | D-04 / G-05（两成员） | **共享同一机制 pattern** | 同上；片段内无 cofibration 结构 / composition 操作 / 资源消耗语义可区分 |

**多成员族坍缩率：2/2。** CE-MAP 的先例（C-228/229/230 等六候选归约为一个 pattern）
在 delay 片段被完整复现。这构成对"多成员族=多个独立验收单元"的**系统性否证经验**：
在 delay 片段，多成员族默认应预期坍缩，除非能指出片段内区分成员的构造。
**归类**：`UI-04` + 反遗漏技术 #11。**处置**：已按 013 §2.1 在两族 REPORT 中判定并登记。

### O-4（信封外入口存在性）开放世界 ingress 清单

按完备性规划 004 片 §二 的七类 UnknownIngress，本轮登记/更新：

| ID | 入口 | 本轮状态 | 处置 |
|---|---|---|---|
| `UI-01` | 新论文/定理/正式化项目 | 未新增（本轮无新来源接入） | 保持；V2 扩版时优先 |
| `UI-02` | 社区实现新版本 | 未新增（Agda 2.8.0 / cubical v0.9 仍为固定工具链） | 保持 |
| `UI-03` | 新自然 consumer | 未新增（2LTT 四类真实消费者仍为既有 holdout） | 保持 |
| `UI-04` | 当前 oracle 无法表达的现象 | 已有 2 条（O-2 方向 A、O-3 同族坍缩），本轮**由风险升级为已确认经验**（2/2 坍缩） | 本文件登记；014 片 §2.3 设门槛 |
| `UI-05` | 跨 family/version 差分 | 已有 1 条（O-1），本轮扩展至五族、157 个越界见证 | 本文件登记 |
| `UI-06` | 新反例/正实例/防线 | 未新增（五族的负控制仍为 EXPECTED，无假阳/假阴；GEN-001-5 negative-control exit 42 四路全过） | 保持 |
| `UI-07` | 用户语义新修正 | 未新增（无新用户修正） | 保持 |

### O-5（本轮新发现）delay 片段的生成侧对象空间未耗尽，但现象空间已饱和

**这是本轮最重要的发现，也是对原审计 A3/P0（发现侧缺失）的定量确认。**

delay 片段的 continuation map 空间在当前声明界（`delay_index_max=2`、Bool、含 ω）是
**有限且已知的**：7 个 branch 形状 × 7 = **49** 个 map。本审计穷尽枚举并去重：

| 量 | 值 |
|---|---:|
| map 空间总量 | 49 |
| 全部 8 个含 continuation 文法已用的 distinct map | 18 |
| 未使用的 map | 31（其中 29 个非 const） |
| 剩余 29 个非 const map 的机械生产力 | **29/29 可在分离见证中被绑定**（逐一建探针文法独立复算） |
| `separation_kind` 取值数 | 3（固定，`model.py:separation_kind`） |
| 五族各自覆盖的机制数 | 均为 3/3 |

**两个方向的耗尽状态不同**：

1. **文法层未耗尽**：还有 31 个 map 没有任何族声明过，且剩余 29 个**全部**机械可产见证。
   「delay 片段没有新 continuation 可声明」是**错的**——如果目标是"保持链贯通能力"，
   还能再跑至少 29 个干净验收单元。
2. **现象层已饱和**：`separation_kind` 只有 3 个取值，且**自第一族（E-02）起每族都 3/3 覆盖**。
   五族的 15 个新 continuation 全部是「单侧发散 / 同延迟相反值 / 索引取值移位」
   三个现象原语在 49 格棋盘上的**不同落子**。GEN-001-5 已落到「@index 1 形状被 GEN-001-4 占用、
   必须退到 @index 1 假分支晚负值与 @index 2 同延迟相反值」。

**这意味着**：继续在 delay 片段加族，**文法新颖性（唯一 BIND_CONTINUATION）仍会成立**，
但**现象新颖性会稳定在 PARTIAL 且单调下降**。这正是原审计所担忧的失败模式的定量版本：
「每次'还不够'都正确，每次正确都不通向发现」——现在可以精确说出
「正确的是什么」（文法/枚举/核校验链）与「不通向发现的是什么」（现象层 3 值饱和）。

**bind 索引累加的结构性约束**（LESSONS 134 的独立复算确认）：
`bind(ret n a, f) = ret (n + inner.n + 1, inner.value)`，故 inner.n=2 的分支
bind 后累加索引 ≥3，超出 horizons {0,1,2}，**bind-then-deadline 分离结构上不可能**；
只有 inner.n≤1 打开 `deadline_observation`。这解释了 GEN-001-5 的
`avail_opposite_at_frontier`（两分支 inner.n=2）**只能由 race 分离**（WV-0051），
不能由 deadline 分离。该约束是**生成侧设计纪律**，不是缺陷。

**归类**：`UI-04`（当前 oracle 无法表达的现象：现象层饱和）+
反遗漏技术 #12（coverage shadow）+ #2（ablation：map 空间清单）。
**处置**：登记 `DELAY_FRAGMENT_PHENOMENON_SATURATED`；修订片 014 把它变成
后续 delay 片段新族的强制披露与事前门槛。**不由本轮决定**是否转向 V2 片段
（那是方案层的下一步选择，本审计只提供定量依据）。

## 三、范围限定——防止五族的"链贯通"被过度解读

五族 `GENERATOR_LINK_DEMONSTRATED_WITH_SCOPE` 的有效范围是：
**给定一个 AI 冻结的任务族，引擎能在声明文法上完整枚举、归约、产出越界见证、
并经原生核四路校验 + 主 repo 独立复现。**

它**不覆盖**：
- 方向 A 的候选（O-2）；
- 五族在机制层面相互独立（O-1，且 GEN-001-4/5 机制分布完全相同）；
- 两个多成员族是多个独立现象（O-3，2/2 坍缩）；
- delay 片段的**现象**新颖性（O-5，3 值饱和，五族 PARTIAL 或更低）；
- 引擎具备自主发现新方向的能力（任务族由 AI 冻结供给，修订片 003 §5 角色纪律）；
- HoTT 全部前提空间（分母 V1 的 remainder=0 只覆盖 A–G 35 条，见 step-1 审计 §四）。

任何把"五族链贯通"读成"机器统观已能发现新悖论"或"两个方向都被覆盖"或
"dalay 片段已被穷尽"的推断都超出声明范围。

## 四、处置裁决（SOP §S-5；修订片 013 §2.3）

- **裁决：`revised`**——需要一次方案修订。
  理由：O-5（现象饱和 + 生成侧未耗尽的定量分裂）是当前方案条款没有要求披露的缺口，
  会让后续族的报告把"还能再跑 29 个干净单元"读成"发现侧在推进"。
  修订见 `Atria的方案/修订片/014`（map 空间披露 + 现象饱和声明 + 事前门槛）。
- **ingress 全部登记**：O-1（UI-05，五族）、O-2（UI-04）、O-3（UI-04，2/2 确认）、
  O-5（UI-04，新）；UI-03 保持；不静默丢弃。
- **不重跑五族**：O-1/O-3/O-5 的披露已在五族 REPORT / INDEX / 本审计中留痕，
  按修订片 012 §4「已验收族按 §4 回填披露不重跑」执行；014 片 §4 明确只对后续族生效。
- **避免重复审计**：本文件 §一的四来源差分已执行一次；下一 session 不必重跑 map 空间清单
  （49/18/31 三个数在声明界不变的前提下稳定），直接读 §二。

## 五、证据定位

| 断言 | 证据 |
|---|---|
| map 空间 49 / 已用 18 / 剩 31 | 本审计独立运行：8 个含 continuation 文法的 `bind_continuations[]` 去重（worktree `/Volumes/D/HoTT-machine-overview/machine-overview/grammars/`）；branch 空间 = ω ∪ {ret n b : n∈{0,1,2}, b∈{T,F}} 的有序对 |
| 剩余 29 个非 const map 全部机械可产见证 | 本审计独立运行：逐一建探针文法 → `enumerate_contexts` × `within_grammar_witness` × `separates`，29/29 至少一个机制 |
| 五族越界见证全部 delay-equivalent | 本审计独立运行：各族 `GEN-001-*-OUT-OF-ENVELOPE.json` 的 `rows[]` × `machine_overview.model.delay_equivalent` |
| 机制分布 12/4/16（GEN-001-4/5 完全相同） | `GEN-001-{DIVISIBILITY,EXISTENCE}-ENUMERATION.json` 的 `grammar_preserving_reduction` |
| 分离机制只有 3 类 | `machine_overview/model.py:separation_kind` |
| delay-equivalent 是见证前置条件 | `machine_overview/search.py:180` `_witness_separates` |
| bind 索引累加约束 | `machine_overview/model.py:bind_value` + LESSONS 134；GEN-001-5 WV-0051 只能 race 分离为经验确认 |
| 同族坍缩 2/2 | `GEN-001-DIVISIBILITY-REPORT.md` §5；`GEN-001-EXISTENCE-REPORT.md` §5 |
| 方向 A 真实候选存在且未被消费 | `audit/2LTT纤维替换自然消费者与crisp退化纤维性消融-20260915.md` 判词行 |
| 五族判词与收据 | `HoTT/generators/GEN-001/GEN-001-INDEX.md`；`HoTT/verification/runs/VERIFY-GEN001-*` |
| 本审计对应 STATE | revision 164，status `PREMISE_001_STEP5_GEN001_DIVISIBILITY_DONE`（本审计在第五族链 commit 之后、checkpoint-165 之前执行） |

## 六、本审计不声称

- 不声称五族的 P3/P4 判定被推翻（全部仍 `AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT`；
  GEN-001-5 的 D-04/G-05 是置信度最低一对，本审计不预判外部审计结论）。
- 不声称剩余 31 个 map「不值得」声明（O-5 只登记饱和状态与门槛，不预判结果）。
- 不声称 delay 片段的 map 空间**只有** 49 格（该数依赖当前声明界；提高声明界会扩大空间。
  本片的饱和结论是**现象层**的，不随声明界扩大而改变）。
- 不声称 V2 片段（区间 / 截断塔 / cofibration 模型）一定能产出现象新颖的候选
  （那是未验证的期望，只登记为方向）。
- 不声称本审计穷尽了开放世界 ingress（UI-01/02/06/07 的"未新增"是本轮观察，不是不存在）。
- 本审计无数学结论（F-011；无命题被交付，MATH_PROOF_BEFORE_DELIVERY_V1 不适用）。
