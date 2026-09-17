# GAP-A 验收报告：缺口 A 闭合——非布尔 De Morgan 代数上的 V2 结构分离

> 单元：**缺口闭合单元（gap-closure unit）**，不是生成器族（修订片 018 §3(A) 登记）
> 任务族：`TASK-FAMILY-GAP-A-INTERVAL-ORACLE-DE-MORGAN`（文法 `V2-DM3-A-v1`，backend `v2-dm3`）
> 执行者：AI 全自动（修订片 009/017；`AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT`）
> 执行日：2026-09-17
> 判词：**`DM3_DE_MORGAN_CONFIRMED_NON_BOOLEAN_LIFT`**（`interval_i_confirmed = false`）
> 引擎提交：`776e6b7`（分支 `feat/machine-overview-m1`）；主 repo 交付物：本目录四件 + 索引行

## 0. 本报告不是什么

- **不是关于真实区间 I 的结论**。判词明确写 `interval_i_confirmed = false`：本单元确认的是
  **V2 的三个结构性分离（availability / level / density）可以在一个非布尔 De Morgan 代数
  上由原生核确认**，而**不是**它们在 Cubical Agda 的区间 `I` 上成立。`I` 的相等不可判定，
  无法写返回 `Bool` 的 `separates`——这正是必须先用 DM3 的原因（修订片 015 §5 / 018 §3A）。
- **不是新的数学结论**（F-011 / `MATH_PROOF_BEFORE_DELIVERY_V1`）。本单元验收的是
  「模型层分离能否脱离点集专属律、在 De Morgan 代数上被原生核确认」这一**工程/可信度问题**。
  唯一登记的否定性机械事实是：**布尔律 `x ∧ ¬x = 0` 对这三个结构性分离不是必需的**——
  由 `boolLawIndependence` 单元在 DM3 上由原生核确认，作用域 = `formal/V2DM3.agda` 定义的
  代数 DM3，不提升到所有 De Morgan 代数，更不提升到 `I`。
- **不是"引擎自主发现"**。任务族、文法、DM3 解释均由 AI 冻结供给（003 §5 角色纪律）。
- **不声称**任何 pending-audit 前提（D-04 / G-05 等）的非现实判定成立。

## 1. 缺口的定义与本单元闭合了哪一半

修订片 018 §3(A) 登记的缺口 A：

> mirror `formal/V2Cofibration.agda` 定义 `Face = Point → Bool`（**点集模型**）。点集模型
> 验证布尔律 `f ∧ ¬f = 0`，而区间 `I` 是该律**失效**的 De Morgan 代数；mirror §10 用 DM3
> 反模型自证点集模型对 De Morgan 代数**可靠但不完备**。因此 V2-1 的全部 kernel 见证
> **一律不得作为关于区间 I 的结论证据**。

缺口 A 的原始任务表述（018 §5）：*构造 DM3 **或真实区间**（min/max/neg）上的 V2 值解释，
使结构性分离可由原生核在 De Morgan 代数上确认。* 本单元闭合 **DM3 这一分支**，并把
「真实区间 I 上的解释」登记为仍然开放的子问题（§7）。

闭合方式：把 V2 的三条结构轴（availability / level / density）从点集面格**搬到标准非布尔
De Morgan 代数 DM3**（三元链 `0 < a < 1`，`~a = a`，故 `a ∧ ¬a = a ≠ 0`）上重新解释，
然后由 Cubical Agda 2.8.0 原生核在 `formal/V2DM3.agda` 上逐项确认。

## 2. 链的实际运行（全部 observed，可复算）

| 阶段 | 产物 | 结果 |
|---|---|---|
| 冻结任务族 | `GAP-A-DM3-GRAMMAR.json`（文法 `V2-DM3-A-v1`，backend `v2-dm3`） | 命中门槛 **G-b（availability）+ G-c（level）+ G-a（density）**，全部**脱离点集面格**、落到非布尔 De Morgan 代数；DM3 = 三元链 `0<a<1`，`~a=a`；结构 op = `supply(d)` / `fill` / `tower(level)` / `between(a,b)`；`ret(n,b,d,level)` 四轴值，55 个 ground values |
| 引擎枚举 | search run `SEARCH-GAP-A-DM3-001` | 40 contexts × 1,404 等价对 = **56,160 pair-context checks**；`complete_within_declared_grammar=true`；`grammar_violations=0`；**remainder=0**（两项预算均未耗尽，无截断） |
| grammar-preserving 归约 | 同上 run | **9,720** 个原始分离 → **396** 个规范归约见证（每步重检文法成员资格与分离性）；分离种类直方图：availability 1,944 / density 2,592 / level 5,184 |
| 越界证明（作用域化） | `GAP-A-DM3-OUT-OF-ENVELOPE.json` | **392/392** 作用域内见证被全部 7 个既有 delay 文法 + 1 个点集 V2 文法拒绝；族内拒因唯一（§4）；4 条 level-ingress 如实登记 |
| 非嵌入检查 | 同上 | 16³ = **4,096** 个候选函数穷举：**0** 个保 meet 与 neg 的 DM3→点集面格嵌入（模型分离，有限穷举负检查） |
| 原生核校验 | 4 个 verify run + 1 个 BLI 单元 | 每个含 4 路 kernel 收据；BLI 单元确认布尔律非必需（§3） |
| 收据化 | 引擎 `runs/SEARCH-GAP-A-DM3-001/`、`runs/VERIFY-GAP-A-DM3-WV-*/`、`runs/VERIFY-GAP-A-DM3-BLI-001/` | RUN.json + kernel stdout/stderr/environment/command + 生成 Agda + source-manifest + witness-manifest（sha256 见 §6） |

**校准与声明见证**（`calibration_match.status = ALL_PRESENT`）：三个校准见证
`WV-A-availability` / `WV-L-level` / `WV-D-density` 在归约集中全部出现，且
`declared_witness_check.all_match = true`（Python canonical 语义与记录逐项一致），
两个同值控制（`CTRL-A-same-value` / `CTRL-D-same-value`）正确判 `separated = false`。

## 3. 原生核结果（Cubical Agda 2.8.0 + cubical v0.9，mirror `formal/V2DM3.agda`）

### 3.1 四路核校验（4 个 kernel 见证）

| verify run | 见证 | 校准锚 | 机制 | 绑定 continuation | verify | controls | negative-control | verify-replay |
|---|---|---|---|---|---|---|---|---|
| `VERIFY-GAP-A-DM3-WV-0230` | WV-0230 | `WV-A-availability` | availability | supply+fill | exit 0 | ACCEPTED | **exit 42（须被拒）** | EXACT_EXIT_STDOUT_STDERR_MATCH |
| `VERIFY-GAP-A-DM3-WV-0041` | WV-0041 | `WV-L-level` | level | tower | exit 0 | ACCEPTED | **exit 42** | EXACT_EXIT_STDOUT_STDERR_MATCH |
| `VERIFY-GAP-A-DM3-WV-0158` | WV-0158 | `WV-D-density` | density | between | exit 0 | ACCEPTED | **exit 42** | EXACT_EXIT_STDOUT_STDERR_MATCH |
| `VERIFY-GAP-A-DM3-WV-0001` | WV-0001 | —（补足第 4 见证） | level | tower | exit 0 | ACCEPTED | **exit 42** | EXACT_EXIT_STDOUT_STDERR_MATCH |

四见见证覆盖三个机制族（availability / level / density），`cross_check` 在任何 kernel 运行前
先重算并断言每个见证的分离性、机制、观察值与记录一致（`DENOMINATOR_SINGLE_SOURCE`，
修订片 016 §3）；`replay` 两次运行的退出码、stdout、stderr 全部精确匹配。

### 3.2 布尔律独立性单元（本单元的核心新事实）

`VERIFY-GAP-A-DM3-BLI-001`（`kind = GAP_A_DM3_BOOLEAN_LAW_INDEPENDENCE`）：

- **问题**：V2 的结构性分离能否在一个布尔律**失效**的 De Morgan 代数中产生？
- **回答**：`answer = YES for availability / level / density (kernel-confirmed)`。
- **判定**：`KERNEL_BLI_PASS`——`bli-verify = KERNEL_ACCEPTED`；
  `bli-negative-control = KERNEL_REJECTED_AS_EXPECTED (exit 42)`；
  `bli-verify-replay = EXACT_EXIT_STDOUT_STDERR`。
- **登记的否定性事实**：`the boolean law x && ~x = 0 is not needed: the density separation
  holds in DM3 while dm3Meet da (dm3Neg da) = da != d0, both kernel-checked`。
- **推翻条件（可操作）**：kernel ACCEPT `BLIFalsify.agda`（即证明
  `dm3Meet da (dm3Neg da) ≡ d0`）将推翻本判定。
- **作用域**：`registers_new_claim = false`，唯一登记的机械事实是上述**否定性**事实，
  作用域 = `formal/V2DM3.agda` 定义的 DM3；**不声称**对所有 De Morgan 代数成立，
  **不声称**对区间 `I` 成立。

## 4. 越界检查与作用域化（诚实披露）

- **作用域内 392/392 见证被全部 8 个既有文法拒绝**（7 个 delay 文法 + 1 个点集 V2 文法）。
- **族内拒因唯一**（精确陈述，避免误读 `scoped_reasons_unique = 0`）：
  - delay 族：392/392 见证每人恰持一个拒因——`UNKNOWN_OP:supply`（216）/
    `UNKNOWN_OP:tower`（104）/`UNKNOWN_OP:between`（72）；
  - 点集族：392/392 见证每人恰持一个拒因——`VALUE_OUT_OF_DECLARED_RANGE:left`（312）/
    `VALUE_OUT_OF_DECLARED_RANGE:right`（80）；
  - **跨族拒因不同**（不可解析的 op vs 不可表示的 DM3 坐标），故
    `scoped_all_reasons_unique = false`。这是**更强**的证据（两族各自结构性地无法承载），
  不是更弱。
- **ingress 披露（4 条）**：4 条 level 见证经共享 `tower` 机制被点集 V2 文法接受
  （DM3 坐标 = 0 落在点集声明的面内，tower 层级在点集声明内）。`level_observation` 机制
  与点集片段共享，这些见证 **L1 不可见但点集可复现**，按 011/012 纪律登记为 ingress，
  **不计入**越界分母。全部 availability 与 density 见证均为 scoped（其 op 与 DM3 坐标
  点集文法无法承载，见非嵌入检查）。
- **非嵌入检查**：`NO meet-and-negation-preserving embedding of DM3 into the point-set
  boolean face lattice exists`——16³ = 4,096 个候选函数穷举，保 meet 与 neg 者 **0** 个。
  `proof_kind = model_exhaustive_negative_check`；作用域 = 两个被声明的有限结构，
  **不是**关于真实区间 I 的命题（F-011）。
- **作用域边界（缺口 B，未变化）**：12 个 symbolic-horn 文法为 schema 级
  `BACKEND_MISMATCH`，本单元未对其跑机械检查——是作用域边界，不是已证不相交。

## 5. 判词的升级语义（外部审计请优先看这里）

V2-1 首族链的 4 个 kernel 见证全部声明 `POINT_SET_MIRROR_MODEL_KERNEL_CONFIRMED`
（点集模型内成立）。本单元把 **availability / level / density 三个机制**从该声明
**升级**为：

```text
oracle_scope                        = DM3_DE_MORGAN_CONFIRMED_NON_BOOLEAN_LIFT
interval_i_confirmed                = false
boolean_law_needed                  = false   (kernel-confirmed negative fact, scope = DM3)
conclusion_evidence_about_interval_I = false
gap_a_dm3_branch_closed             = true
gap_a_interval_i_branch_open        = true
registers_new_claim                 = false   (唯一登记 = 布尔律非必需，否定性机械事实)
```

**升级了什么**：这三个分离**不再依赖点集面格的序**，也不再依赖布尔律；它们在
`x ∧ ¬x = a ≠ 0` 的代数中依然由原生核确认。这直接回应了修订片 018 §4 的教训
（"是否需要点集专属律"是 V2 后续族的第一排序键）：availability 与 level 两个机制
在本单元被证明**解释无关、结构层**；density 在 DM3 上用链序表达，**仍是模型层**
（DM3 是 I 的一个模型，不是 I）。

**没有升级什么**：本判词**不声称**任何分离在真实区间 `I` 上成立。DM3 与点集面格
都是**模型**；`I` 是另一个模型，且其上的分离无法用 `Bool` 返回值表达
（相等不可判定）。「DM3 结果能否提升回 `I`」仍是开放问题（§7）。

**对父目标的净推进（诚实记账）**：机器统观的**验证侧**再次按收据完成一次有界闭合
（分母 remainder=0、族内拒因唯一、四路核、BLI）；**发现侧**没有任何推进——本单元
不产生新的数学命题，不产生新的悖论候选，前提判定全部保持
`AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT`。任何把本判词读成"HoTT 的非现实前提被找到了"
的解读都是误读。

## 6. KEY_ADJUDICATION_AUDIT_TRAIL（017 §3）

本单元的每个关键判定都带可审计链（`question` / `verdict` / `verdict_reason` /
`falsifier` / `audit_status = AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT`），存于每个
verify run 的 `RUN.json`。推翻条件可操作：

- 推翻四路核判定：kernel ACCEPT `Falsify.agda`，或 REJECT `Verify.agda`，或 replay 不匹配。
- 推翻 BLI 判定：kernel ACCEPT `BLIFalsify.agda`（即 `dm3Meet da (dm3Neg da) ≡ d0`）。
- 推翻越界判定：任一既有文法接受某作用域内见证。
- 推翻非嵌入判定：给出一个保 meet 与 neg 的 DM3→点集面格函数。
- 推翻判词升级：证明某分离在 DM3 上必需布尔律（与 BLI 单元冲突）。

`depends_on`（回滚清单）：`SEARCH-GAP-A-DM3-001`、4 个 `VERIFY-GAP-A-DM3-WV-*`、
`VERIFY-GAP-A-DM3-BLI-001`、`machine-overview/formal/V2DM3.agda`、
`machine-overview/machine_overview/v2_dm3*.py`、`grammars/v2-dm3-a-v1.json`、
本报告与三个 JSON 交付物。

**全量见证清单的可审计性**：396 条归约见证清单（`witness-manifest.json`，206,712 bytes）
保留在引擎工作树（分支 `feat/machine-overview-m1`，commit `776e6b7`）；主 repo 只存
sha256 与统计（`GAP-A-DM3-ENUMERATION.json`）。外部审计可凭 sha256 在引擎工作树核验
任一条见证。

## 7. 剩余开放问题与下一单元（AI 全自动，017 纪律）

1. **真实区间 I 上的解释（缺口 A 的另一半，仍开放）**：DM3 是 I 的一个**非布尔模型**，
   但不是 I。`I` 的相等不可判定，因此不能写返回 `Bool` 的 `separates`；I 上的分离必须
   以别的形态表达（类型族 / cofibration 条件 / PathP，而非 Bool 观察）。这是一个
   **设计探针**问题：先确定「I 上能写什么」，再决定是否可验收。**若探针结论是
   「Bool 形态的分离在 I 上结构性不可写，且替代形态改变了分离的定义」**，则登记为
   有界负结论，转下一项。
2. **V2 第二族（结构性优先，修订片 018 §4 教训）**：G-c 层级塔的**独立供给**
   （`level_observation` 已在本单元被证明解释无关、结构层，是最干净的下一族）；
   G-a 稠密族需要序，优先级低。或 SUPPLY-010 新任务族。
3. 每个单元完成后：`checkpoint --apply` + 修订片登记 + goal-1 指针同步，全部 git 提交。
