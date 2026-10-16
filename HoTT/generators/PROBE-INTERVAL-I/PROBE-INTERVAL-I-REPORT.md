# PROBE-INTERVAL-I 验收报告：区间 I 设计探针——可写形态与表达界限

> 单元：**设计探针单元（design-probe unit）**，不是生成器族，不是缺口闭合单元。
> 探针对象：Cubical Agda 2.8.0 + cubical v0.9 的**真实区间 I** 上可写哪些分离形态。
> 执行者：AI 全自动（修订片 009/017；`AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT`）
> 执行日：2026-09-17
> 判词：**`INTERVAL_I_SEPARATION_FORMS_FAMILY_AND_COFIBRATION_BOOL_OBSERVER_UNWRITABLE`**
> 引擎提交：`36d27e0`（分支 `feat/machine-overview-m1`）；主 repo 交付物：本目录两件 + 索引行

## 0. 本报告不是什么

- **不是关于区间 I 的数学结论**（F-011 / `MATH_PROOF_BEFORE_DELIVERY_V1`）。本探针
  验收的是一个**语言片段问题**：在固定工具链（Cubical Agda 2.8.0 + cubical v0.9）实际
  提供的消去子、宇宙与 sort 结构下，区间 `I` 上**能写成什么样**的分离，**不能写成什么样**。
  `registers_new_claim: false`，本单元**不进入** `HoTT/CLAIM_EVIDENCE_MATRIX.md`。
- **不是失败**。两种结论都是正面信息（修订片 019 / 020 审计分片 008 在设置本单元时即
  明文要求：「两种结论都是正面信息」）。「Bool 形态可写」会完全闭合缺口 A 并扩大分母；
  「Bool 形态结构性不可写」是关于 I 的**表达界限的正面结论**，它把「DM3 分离语义能否
  保真表达」这一问（EXP-001）收尾为一个**有界负结论**。
- **不是"引擎自主发现"**。探针模块由 AI 设计与冻结供给（003 §5 角色纪律）。
- **不声称**任何 pending-audit 前提的非现实判定成立。
- **不声称**本探针穷尽了 I 上一切可写形态。本探针覆盖三条自然路线（类型族/PathP、
  cofibration 条件、Bool 观察器 + 等式类型），三路线之外是否存在其他形态是**开放**的
  （§6 未闭合项）。

## 1. 探针要回答的问题（来自 STATE next_minimal_verification，revision 168）

缺口 A 闭合单元（revision 168，判词 `DM3_DE_MORGAN_CONFIRMED_NON_BOOLEAN_LIFT`）把
**区间 I 分支留作开放**：DM3 分支确认了 V2 的三个结构性分离（availability / level /
density）可以在**非布尔 De Morgan 代数**上被原生核确认，但 mirror `formal/V2DM3.agda`
是**模型**，不是真实区间 `I`。STATE 的下一单元指引原文：

> 区间 I 分支仍开放——I 的相等不可判定，不能写 Bool 返回的 separates；I 上的分离
> 须以别的形态表达（类型族 / cofibration 条件 / PathP）。这是一个设计探针问题：
> 先确定「I 上能写什么」，若探针结论是 Bool 形态分离在 I 上结构性不可写且替代形态
> 改变分离定义，则登记有界负结论并转 (2)。

本探针即回答「I 上能写什么」。

## 2. 三路探针（全部 observed，可复算）

| 探针 | 模块 | 意图形态 | 退出码 | 核结论 |
|---|---|---|---|---|
| 可写形态 | `formal/IntervalIForms.agda` | (a) I 上类型族 + `PathP`；(b) cofibration 条件 `IsOne` / `Partial (r ∨ ~ r)` / `Partial (r ∧ s)` + 约束模式匹配 | **0** | **KERNEL_ACCEPTED**：形态 (a)(b) 全部可写 |
| Bool 观察器（路线 c2） | `formal/IntervalIBoolDiscriminator.agda` | `I → Bool` 的端点观察器（DM3/点集分离 oracle 的形态） | **42** | **KERNEL_REJECTED_AS_EXPECTED**：`[SplitError.NotADatatype] Cannot split on argument of non-datatype I` |
| 等式类型（路线 c1） | `formal/IntervalIEqualityAttempt.agda` | `PathP (λ i → I) r s`：DM3 oracle 需要量化的 I 上等式类型 | **42** | **KERNEL_REJECTED_AS_EXPECTED**：`[UnequalSorts] IUniv != Type` |

每路探针一个 run 收据目录（`PROBE-INTERVAL-I-FORMS` / `PROBE-INTERVAL-I-BOOL-DISC` /
`PROBE-INTERVAL-I-EQ-ATTEMPT`），各含 `RUN.json` + `stdout.txt` + `stderr.txt` +
`environment.txt` + `command.json` + `source-manifest.json`；退出码、sha256、时长、
期望匹配全部登记。工具链身份与 `VERIFY-GAP-A-DM3-BLI-001` 完全一致
（Agda 2.8.0-3d04bac，sha256 `ac285c19…`；cubical v0.9 pinned，无网络）。

### 2.1 可写形态的具体内容（`IntervalIForms.agda`，核 ACCEPT）

- **(b1)** 全局 cofibration 事实：`IsOne i1` 由 `1=1` 直接给出。
- **(b2)** **分离承担形态**：`endpointCases : (r : I) → Partial (r ∨ ~ r) Bool`——
  在 `(r = i0)` 给 `false`、`(r = i1)` 给 `true`，**无需任何 I 上的可判定相等**：
  端点情形由约束模式匹配提供，重叠情形必须一致。这一条是关键：它在**不判定 r 本身**的
  前提下区分两个端点体制。
- **(b3)** 类型层载体：`endpointFamily : (r : I) → Partial (r ∨ ~ r) Type₁`——
  分片依赖 I 的类型族。
- **(b4)** cofibration 合取可写：`meetCases : (r s : I) → Partial (r ∧ s) Type₁`，
  meet 仅在**双端点约束同时**成立时为 `i1`。
- **(a)** `intervalFamily : I → SSet₂`（载体即 b3 的 partial 类型，真依赖 r）；
  `pathOverConstant : (A : Type ℓ) (x : A) → PathP (λ _ → A) x x` 由
  区间抽象给出。真依赖族上的 `PathP` **类型成型**（成型规则不需要项居住）。

### 2.2 拒绝形态的具体内容（核 REJECT，诊断即证据）

- **路线 c2**（`IntervalIBoolDiscriminator.agda:32.18-20`）：
  `endpointObserver : I → Bool`，对 `i0` / `i1` / 通配子句做模式匹配。
  核拒绝：`Cannot split on argument of non-datatype I`。**`I` 不是可对其做消去的
  归纳类型**——它没有 eliminator，模式匹配只在 cofibration 约束下被允许（b2 的形态）。
- **路线 c1**（`IntervalIEqualityAttempt.agda:16.32-33`）：
  `identityOnI r s = PathP (λ i → I) r s`。核拒绝：`IUniv != Type`。
  **`I : IUniv`，不在 `PathP` 族所需的宇宙 sort 中**，故 I 上等式类型**不可成型**。

两条拒绝路线覆盖了「Bool 观察器」的两条自然来路：要么直接对 I 做模式匹配（c2），
要么先有一个可判定的等式（c1）。**两条都被结构性拒绝**。

## 3. 判词语义

`INTERVAL_I_SEPARATION_FORMS_FAMILY_AND_COFIBRATION_BOOL_OBSERVER_UNWRITABLE`：

- 区间 I 上**可写**的分离形态是**类型族 + `PathP`** 与 **cofibration 条件层**
  （`IsOne` / `Partial` / 约束模式匹配）；
- DM3/点集分离 oracle 所用的**Bool 观察器层在 I 上结构性不可写**（两条来路均被拒）；
- 因此 DM3 分支的分离语义**不能**被翻译成「同一分离在真实区间 I 上的直接提升」——
  它只能被翻译进 **cofibration 层**，而这一翻译**改变了分离的承载定义**（从
  `A → A → Bool` 的可判定观察，变成 `Partial (φ) A` 的约束分片）。

**判词分级**（沿用修订片 019 的分级纪律）：
- 「Bool 观察器不可写」是**关于工具链表达界限的有界负结论**，作用域 = Cubical Agda
  2.8.0 + cubical v0.9 的消去子/宇宙/sort 结构。**falsifier**：一个被核 ACCEPT 的
  非恒常 `I → Bool`，或一个被核 ACCEPT 的 I 上可判定相等。
- 「类型族/cofibration 可写」是**正面可写性证据**（核 ACCEPT 的定义集），
  作用域同上。**falsifier**：核 REJECT 其中任一定义。

## 4. EXP-001 收尾

EXP-001（HoTT 能否保真表达 DM3 分离语义）的结论：

- **保真翻译存在，但改变了承载层**：DM3 的 `separates` 语义可翻译进 cofibration 层
  （b2/b3/b4 是这一翻译的形态证据），但**不是**同一分离在 I 上的直接提升。
- 因此 V2-DM3 的分离结论与真实区间 I 之间的关系被**精确刻画**：DM3 是模型，
  I 上的对应物只能以 cofibration 形态存在，且形态改变带来语义改变（`Partial (φ)`
  的「在约束下分片定义」≠ `Bool` 的「全局可判定观察」）。
- 这**不是**说 HoTT 无法表达相关现象，而是说**表达的层不同**——这一点对后续
  SUPPLY-010（知识谱反观 + 现实对齐断裂供给单元）有直接方法学含义：现实对齐
  断裂的寻找不应假设「理论必须以某一固定形态（如可判定观察）携带某个语义」。

## 5. 与缺口 A / GEN-001 链的关系

- 缺口 A（修订片 018 §3A）的**DM3 分支已闭合**（revision 168）；本探针处理的是
  **区间 I 分支**。探针结论 = 「Bool 形态结构性不可写且替代形态（cofibration）
  改变分离定义」——正是 STATE 指引中「登记有界负结论并转 (2)」的分支。
- 因此：**缺口 A 的区间 I 分支以表达界限正面结论收尾，而非以一个 I 上的
  V2 值解释闭合**。V2-DM3 的 availability / level 见证仍**不得**作为关于区间 I 的
  结论证据（`interval_i_confirmed = false` 继续保持）；density 见证同理。
- 本单元**不是** GEN-001 的验收单元，也不扩大 GEN-001 的分母。
- 下一单元（经 020 审计分片 008 裁决，本探针不改变该裁决）：**SUPPLY-010
  知识谱反观 + 现实对齐断裂供给单元**，目标 = F2 缺口层 7 个来源在手、分母零条的层
  （PAT / LEM / resizing / AC / unique choice / 截断时机判据 / Dedekind-Ω）。

## 6. 未闭合项（不静默丢弃）

- 本探针只覆盖三条自然路线；**是否存在 I 上的第四种分离形态**（既非类型族/PathP、
  非 cofibration、非 Bool 观察器）**开放**。登记为 unknown ingress，不构成结论。
- 「Bool 观察器不可写」是**工具链相对**的：换一个提供区间消去子的实现或未来版本，
  结论可能改变。作用域已固定到 Cubical Agda 2.8.0 + cubical v0.9。
- 缺口 B（12 个 symbolic-horn 文法未跑机械检查）仍开放，与本探针无关，不阻塞。
- 本探针**不**判定任何前提的非现实性（修订片 006 三点保留全部适用：发现路径
  ≠ 证明路径；完整知识谱是要求不是已兑现事实；「非现实」最终落在现实对应上）。
