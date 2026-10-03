# HMZ-001：HoTT 创建动机的第一原典分母

> **身份：** `CLOSED_SOURCE_RUN_WITH_SCOPE / FROZEN_FIRST_CORPUS / DENOMINATOR_COMPLETE_WITH_SCOPE`。
>
> **项目：** `HOTT-MOTIVE-ZFC-INVESTIGATION`。
>
> **SOP：** `HOTT-MOTIVE-ZFC-SOP` v1.1。

## 1. 本轮问题与边界

本轮只调查一件事：HoTT／Univalent Foundations 的创建者和早期权威文本实际上怎样说明
“为什么已有基础还需要 HoTT／UF”，以及这些说明是否已经足以把某项 **ZFC 内部规则、形成方式或真实消费者**
送入 `R_i → Z_i → Q_i` 的后两步。

本轮不调查或断言：

- ZFC 的一致性、完备性或“总体是否有问题”；
- HoTT 的内部规则是否错误；
- 任何数学命题或现实相对 UR 已成立；
- Power Set、Extensionality、Choice、Replacement 中的任一项已经成为本项目的 Q。

`H0 → Z0 → Q0` 也只作传输资格检查，不能以词面上的“相同”“对象”“完成”建立对应。

## 2. 冻结身份

| 字段 | 值 |
|---|---|
| Run ID | `20261003-HMZ-001-primary-motives` |
| 工作树 | `/Users/aurolafly/.codex/worktrees/ff3b/HoTT_AI_HANDOFF_20260911` |
| 冻结 Git HEAD | `772e0fca80baf4627f782a054ca0b4a7d31ae5be` |
| 调查日期 | 2026-10-03 |
| 读者角色 | `RESEARCH_GENERATION`：来源调查与候选生成 |
| 归档权限 | 当前 `/goal` 的 `HOTT-MOTIVE-ZFC-SOP` 调用授权公开来源调查、公开原件归档、R/Z/Q／控制卡与覆盖记录；没有启动 worker、P-DAG、STATE mutation 或数学证明。 |
| 停止条件 | 首批分母已经形成来源定位、R 卡、Z disposition、控制与明确的 `MUST_FOLLOW` 队列；未完成的强引用或缺少理论层／消费者来源时，不把本轮写成 `DENOMINATOR_COMPLETE_WITH_SCOPE`。 |

## 3. 冻结来源分母

同一来源可以承担多个 A–E 角色，但仍只保有一个 `HMZ-S` 身份。`READ` 的意思是：**本轮用到的精确页、
段或源码 locator 已经实际读取**；它不是整本书或整套文献已经通读。

| ID | 类别 | 来源 | 本轮状态 | 作用 |
|---|---|---|---|---|
| `HMZ-S-001` | A, B, E | *Homotopy Type Theory: Univalent Foundations of Mathematics*，The Univalent Foundations Program，2013；本仓库锁定源码 commit `578b85cc…`。 | `READ_RELEVANT_LOCATORS` | 结构同一性、高阶归纳类型、proof assistant、category-theoretic consumer、HoTT 内部的 ZFC 累计层级。 |
| `HMZ-S-002` | A, B | Vladimir Voevodsky, *Univalent Foundations Project*，2010。 | `READ_RELEVANT_LOCATORS` | 直接公理化 homotopy types、Coq 中的基础、构造性与机器执行目标。 |
| `HMZ-S-003` | A | Vladimir Voevodsky, *Univalent Foundations*，IAS talk slides，2014-03-26。 | `READ_RELEVANT_LOCATORS` | 对既有基础、谓词逻辑、2-theories 与日常机器验证的个人动机陈述。 |
| `HMZ-S-004` | A, E | Vladimir Voevodsky, *The Origins and Motivations of Univalent Foundations*，IAS，2014。 | `READ_VIA_WEB` | 作者的回顾性解释；直接 HTTP 下载受 Cloudflare 挑战阻断，已记录 URL、日期和可见内容，不假装有本地原件。 |
| `HMZ-S-005` | E | Steve Awodey, *Type theory and homotopy*，arXiv:1010.1810，2010。 | `READ_RELEVANT_LOCATORS` | 区分一般 intensional type theory 的计算性质与 UF 特有动机。 |
| `HMZ-S-006` | A, E | Steve Awodey, Álvaro Pelayo, Michael A. Warren, *Voevodsky’s Univalence Axiom in homotopy type theory*，arXiv:1302.4731，2013。 | `READ_RELEVANT_LOCATORS` | 对“official foundations”、direct definitions、机器实现的独立当期说明。 |
| `HMZ-S-007` | C | Metamath Proof Explorer 的 `ax-ext`、`ax-pow`、`pwex`、`rankpw`、`ax-reg` 页面。 | `READ_RELEVANT_LOCATORS / PROOF_FORMALIZATION_ONLY` | 固定 Extensionality／Power Set 的一份可检索形式呈现；不能把它误作 ZFC 的完整语义、历史原典或真实消费者。 |
| `HMZ-S-009` | D, E | David Mumford, *Picard Groups of Moduli Problems*，1965。 | `READ_RELEVANT_LOCATORS / VISUAL_SOURCE_CHECKED` | 同构类、universal family、automorphisms 与明确 mapping data 的实际数学消费者／标准防线。 |
| `HMZ-S-010` | C, D, E | Michael A. Shulman, *Set Theory for Category Theory*, arXiv:0810.1279v2，2008。 | `READ_RELEVANT_LOCATORS` | ZFC classes-as-formula、不能量化 classes、meta-language、NBG payment、global choice 的实际 category-theory uses。 |
| `HMZ-S-011` | C, D, E | Lawrence C. Paulson, *Isabelle’s Logics: FOL and ZF*，Isabelle2021-1，2021。 | `READ_RELEVANT_LOCATORS` | ZF as FOL、Replacement scheme、practical named syntax、actual Isabelle/ZF formalization。 |

### 分母修订 A：已冻结的 `MUST_FOLLOW` 来源进入

`HMZ-S-010` 与 `HMZ-S-011` 是原冻结清单中的 `HMZ-MF-001` 与 `HMZ-MF-003` 的直接来源支付，而不是
事后扩大主题。它们只让“ZFC / predicate language”及“ZFC formalization”从空泛标签变成可定位来源；不增加
一个新的理论靶，也不把本 run 的 `NO_CANDIDATE_SEED` 改为命中。

## 4. 必须追踪而尚未完成的来源

这些并非“以后也许看看”的广义愿望，而是本轮的明确余项；因此本轮不能自称已完成冻结分母。

| ID | 为什么必须追踪 | 需要什么才算处理 |
|---|---|---|
| `HMZ-MF-001` | Voevodsky 对“谓词逻辑过于有限”与“不能直接表达 2-theories 对象”的陈述，需要一个能定位语法／编码／实践成本的理论层来源。 | `CLOSED_WITH_SCOPE`: Shulman 给出 ZFC large-class quantification / meta-language 的精确实例；它不等同于 Voevodsky 的具体 2-theory 例，但已足以检验本 run 的 R→Z language bridge。 |
| `HMZ-MF-002` | 结构同一性动机需要一个 ZFC 或 set-theoretic consumer，才能测试“同构分类是否被偷偷当作具体且自然的交付”。 | `CLOSED_WITH_SCOPE_NO_HIT`: Mumford 与 Shulman 两个真实消费者都明示 family/maps 或 Choice 的支付；当前分母没有相同 Done 的未付 consumer。 |
| `HMZ-MF-003` | “日常可机器验证”的动机需要把 ZFC 本身、其 proof formalization、proof search 与实际交付严格分层。 | `CLOSED_WITH_SCOPE`: Isabelle/ZF 给出一阶 ZF、Replacement scheme、实际 formalization 与 practical syntax；没有来源支持“存在被错误提升为可执行交付”的同一任务。 |
| `HMZ-MF-004` | 若考虑 Power Set 站位，必须找到 HoTT 动机到 Power Set 的**来源支持桥**，并完成 formation 与 consumer 检查。 | `CLOSED_WITH_SCOPE_NO_BRIDGE`: 检查本 run 的 HoTT Book set-theory locators、Voevodsky／APW 原典和公开关键词结果，只得到 Power Set 的技术讨论，未得到 R→Power Set 的同一任务来源桥。 |

## 5. 当前结论的许可范围

本 run 可以报告“首批原典中出现了结构同一性、直接表达高阶对象、基础语言／日常形式化的动机”，以及
“Shulman 的 ZFC/NBG 区分与 Isabelle/ZF 是可定位的标准支付”。它只能把这些报告为
`R_SOURCE_REPORTED`、`SOURCE_SUPPORTED_REPRESENTATION_BOUNDARY` 或 `SOURCE_PAYMENT`。
本 run 当前**不能**报告已找到 `ZFC_Q`，也不能报告 `H0 → Z0` 已有对应物。
