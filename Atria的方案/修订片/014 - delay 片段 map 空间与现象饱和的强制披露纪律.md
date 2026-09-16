# 修订片 014 · delay 片段 map 空间与现象饱和的强制披露纪律

来源：step-6 omission audit after GEN-001 五族（`audit/PREMISE-001-STEP6-OMISSION-AUDIT-20260916-2.md`，O-5）。
身份：方案修订（reflection=step6-audit-revised）。本片**不做 P3/P4 判定，不产生数学结论**（F-011）。

## 1. 问题（证据，机械可复算）

delay 片段的 continuation map 空间在当前声明界（`delay_index_max=2`、Bool、含 ω）
是**有限且已知的**：7 个 branch 形状 × 7 = **49** 个 map（含 const map）。
五族执行后：

| 量 | 值 | 复算方式 |
|---|---:|---|
| map 空间总量 | 49 | 7 branch 形状（ω / ret 0..2 × T/F）的有序对 |
| 全部文法已用的 distinct map | 18 | 8 个含 continuation 的文法的 `bind_continuations[]` 去重 |
| 未使用的 map | 31 | 49 − 18；其中 29 个是非 const map |
| 剩余 29 个非 const map 的机械生产力 | **29/29 可在分离见证中被绑定** | 逐一建探针文法 → `enumerate_contexts` × `within_grammar_witness` × `separates`（本审计独立复算） |
| `separation_kind` 取值数 | 3（固定） | `machine_overview/model.py:separation_kind` |
| 五族各自覆盖的机制数 | 均为 3/3 | 各族 REPORT §2 |

**结论（两个方向的耗尽状态不同）**：

1. **文法层未耗尽**：还有 31 个 map 没有任何族声明过，且剩余 29 个全部机械可产见证。
   「delay 片段没有新 continuation 可声明」是**错的**。
2. **现象层已饱和**：`separation_kind` 只有 3 个取值，且**自第一族（E-02）起每族都 3/3 覆盖**。
   五族的 15 个新 continuation 全部是「单侧发散 / 同延迟相反值 / 索引取值移位」
   三个现象原语在 49 格棋盘上的**不同落子**。GEN-001-5 的披露已经记录到这一点：
   @index 1 的形状被 GEN-001-4 占用，本族必须退到 @index 1 假分支晚负值与
   @index 2 同延迟相反值。

这正是原审计 A3/P0（发现侧缺失）在 delay 片段上的**定量确认**：
瓶颈不是「机器找不到可枚举的新对象」，而是「新对象在现象层不新」。
继续在同一片段加族，文法新颖性（唯一 BIND_CONTINUATION）仍会成立，
但现象新颖性会稳定在 PARTIAL 且单调下降。

## 2. 新增强制纪律（本片生效，适用于 delay 片段的每一个新 GEN-001 单元）

### 2.1 map 空间披露（REPORT 必答，机械可复算）

每个 delay 片段的新族 REPORT 必须给出：

- 本族声明前后的 **map 空间覆盖率**（`已用 distinct map / 49`）；
- 本族新 map 是否落在**已使用形状**（单侧发散 / 同延迟相反值 / 索引取值移位）上；
- 若全部落在已使用形状，现象新颖性不得标高于 **PARTIAL**（012 片三问 Q1 的下界）。

### 2.2 现象饱和声明（INDEX 禁止外推段必答）

`HoTT/generators/GEN-001/GEN-001-INDEX.md` 的禁止外推段必须登记：

> `DELAY_FRAGMENT_PHENOMENON_SATURATED`：`separation_kind` 的 3 个取值
> 已被既有族全部覆盖；delay 片段内新增族的**现象新颖性上限是 PARTIAL**，
> 无论 map 新颖性多干净。

### 2.3 后续 delay-fragment 族的事前门槛

在 delay 片段**再**冻结一个新族之前，必须先回答：
「该族的 omission shape 是否必须由 delay 片段承担？」
若答案为否（例如需要区间、截断塔、cofibration 结构、composition 操作），
则该族应登记为 **V2 候选**（010 §3），而不是继续在 delay 片段加族。
本条**不禁止**继续加族，只要求门槛显式化，防止「干净但同型」的验收单元无限累积。

## 3. 对现有条款的影响

| 条款 | 影响 |
|---|---|
| 012 片 §2 Q1（现象新颖性） | 补 2.1：必须给 map 覆盖率与形状归类；全落旧形状则 ≤ PARTIAL |
| 013 片 §2.2（方向覆盖声明） | 补 2.2：INDEX 必须登记现象饱和 |
| 011 片（越界理由唯一） | 不变（机械纪律不动） |
| 006 片（发现引擎：语义重定向作八轴搜索策略） | **加强**：O-5 是 006 片所设发现侧的 delay 片段投影定量证据；发现侧的下一步应优先在 V2 片段（区间/截断塔/cofibration 模型）实现语义重定向策略，而不是继续加密 delay 片段棋盘 |
| 009 片（P3/P4 自动化 + 外部审计） | 不变；本片全部进审计层 |

## 4. 已验收五族的处置（不重跑）

- 五族的执行链不重跑；map 覆盖率由本片 §1 一次性给出（18/49），写入审计文件。
- 五族 REPORT **不补改**（012/013 在其执行时已生效；GEN-001-5 的 Q1 已自觉落到
  「全部是索引取值变体」的 PARTIAL 判定，与本片 §1 结论一致）。
- 本片**只对后续 delay 片段新族**生效。

## 5. 本片不声称

- 不声称五族应被合并或作废（文法新颖性成立，机械 PASS）。
- 不声称剩余 31 个 map「不值得」声明（2.3 只要求门槛显式化，不预判结果）。
- 不声称 delay 片段的 continuation map 空间**只有** 49 格——该数依赖当前声明界
  （`delay_index_max=2`、Bool、含 ω）；提高声明界会扩大空间，本片的饱和结论
  是**现象层**（`separation_kind` 3 值）的，不随声明界扩大而改变。
- 不声称 V2 片段一定能产出现象新颖的候选（那是未验证的期望，只登记为方向）。
- 本片无数学结论（F-011）。
