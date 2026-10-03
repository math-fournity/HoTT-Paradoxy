# HOTT-MOTIVE-ZFC：第一阶段来源综合

> **身份：** `CROSS_RUN_SYNTHESIS / THREE_FROZEN_DENOMINATORS / PROJECT_ACTIVE / NOT_A_ZFC_Q_OR_MATH_CLAIM`。
>
> **覆盖对象：** HMZ-001、HMZ-002、HMZ-003；17 个不同 `HMZ-S` 来源身份，另有跨 run 的精确复用。

## 1. 这三轮实际完成了什么

本项目不是在问“哪一篇文章说 ZFC 有问题”。它把 HoTT/UF 的创立动机拆成：

```text
R_i：作者/权威来源说出的设计动机
  → Z_i：ZFC、集合论实践、形式化或元语言中的精确对象/formation/consumer
  → Q_i：只有在同一任务、未付义务与模式 P 条件都满足时才成立
```

三轮合起来，已覆盖三个主要动机族：

| 轮次 | 主要原典问题 | ZFC-side 精确化 | 本轮 Q 处置 |
|---|---|---|---|
| [HMZ-001](20261003-HMZ-001-primary-motives/MANIFEST.md) | 结构同一性、直接高阶描述、机器基础、sets/homotopy types。 | ZFC class-as-formula；NBG；Mumford family；Metamath/Isabelle formalization。 | class/meta-language 是表示边界；Mumford/Choice/语法均为显式支付；当时 Power Set 尚没有 R bridge，后由 HMZ-009 单独预检。 |
| [HMZ-002](20261003-HMZ-002-voevodsky-set-theory/MANIFEST.md) | Voevodsky 的 `problem of equivalence`。 | representation-sensitive property；abstract structural language；FOLDS/typed language/NBG/Choice。 | equivalence discipline 是来源支持的语言约束；没有同一对象的 formation/reentry/Done 张力。 |
| [HMZ-003](20261003-HMZ-003-formalization-delivery/MANIFEST.md) | 类型纪律、归约计算、proof-assistant practicality。 | Isabelle/ZF 的 `Inf`、`Pow`、`Replace`、`The`、derived rules；axiom vs computation。 | 命名常量、唯一性/单值条件和规则是显式 formation payment；HoTT 自身亦有 axioms 阻断 computation。 |

这三轮每一轮都保存了 `MANIFEST`、`SOURCE-CATALOG`、R/Z/Q 卡、真实 consumer 控制、coverage 和 findings，
并固定公开原件的 URL、版本、哈希、页／行 locator 与派生阅读材料。

## 2. 三种“有问题”的东西必须分开

### A. 来源支持的表示边界

这是真实、可报告的来源结果：

- 纯 ZFC 的 class-as-formula 方式不能在对象语言中量化 classes；
- ZFC 语言容许 representation-sensitive、非 equivalence-invariant 的表述；
- raw axioms 可以只断言存在，因此实际形式化增加名称、条件和派生规则；
- set-coded / untyped 表述与 richer type discipline 在错误预防、语法和计算上有不同成本。

这些是 **表示、语言或工程接口的边界**。它们不自动是理论的数学矛盾、现实相对 UR 或模式 P 命中。

### B. 来源显示的支付

在三轮中，理论或实际消费者并非一律假装没有成本。相反，来源公开支付了所需结构：

| 支付 | 来源作用 |
|---|---|
| NBG 的 class language／meta-language | 把大范畴量化从纯 ZFC 的对象语言移到带 class 的语言或元层。 |
| ordinary/global Choice | 构造 skeleton、inverse equivalence、product functor 等时选择代表或对象。 |
| maps／family data | Mumford 不把 coarse moduli classification 当作 universal family。 |
| typed language / FOLDS criterion | 把 structural/equivalence-invariant properties 与任意表述分开。 |
| named ZF constants、single-valued / unique rules | 将 raw-existence axiom 变成实际 formalization 接口。 |
| well-ordering | 在 Voevodsky 的技术模型中使 standard isomorphism 有明示的唯一性条件。 |
| HoTT implementation boundary | HoTT Library 记录某些 axioms 也会阻断 computation。 |

这不是“ZFC 获得了总免疫”。它只说明：对已冻结的具体任务，来源中已经写出了 payment，不能把同一任务的完成困难由 AI 偷加进去。

### C. 模式 P 所需、目前仍未出现的结构

一个合格 Q 至少需要同一理论层的：

```text
u：对象语言的一等对象
F：形成/交接接口
C：真实 consumer
I/O/Done：输入、操作、观察、完成条件
P2/P3：source-supported reentry、admission或未付完成结构
```

第一阶段的所有候选都在这一步停止：

| 入口 | 阻断位置 |
|---|---|
| class / large category | 类不是 ZFC 内对象；meta-language 或 NBG 是明确换层。 |
| equivalence invariant property | “任意性质”与“structural property”有不同 Done；语言 criterion 是明确支付。 |
| chosen representative / skeleton | Choice、maps、well-ordering 或标记被明确要求。 |
| `Inf`、`Pow`、`Replace` | 名称、axiom、单值／唯一性条件和 derived rules 已公开交付；没有 reentry。 |
| Power Set | 初始三轮没有 `R → u/F/C/Done` bridge；HMZ-009 后有 Book-level quotient construction bridge，HMZ-010 已给 `RepFun` route 的 actual consumer/payment control，HMZ-012又固定 finite-process / infinite-totality reality bridge，但仍缺保留 \(\mathcal P(A)\)-subset route 的 same-Done、P-qualified未付 completion。 |
| `H0 → Z0` | HMZ-013 的 universe-model / Grothendieck route 给出来源化反类比：model/large-cardinal scope、smallness switch与同一对象控制均不保留 HoTT H0 的 subject/process/observation/Done。 |

所以第一阶段的总结果是：

```text
SOURCE-SUPPORTED ZFC BOUNDARIES: YES
P-QUALIFIED ZFC Q: NO
H0→Z0 TRANSPORT: NOT FORMED
“ZFC has no Q”: NOT INFERRED
```

## 3. 对原始研究目的的自审

用户不是要一份“ZFC 很灵活”的辩护，也不是要把任何技术不便都称为悖论。P 的作用是检查：某个基础理论是否在
同一任务中先把未形成、未支付或仍须合法性追问的对象交给后续使用。

第一阶段确实对这个问题做了更严格的准备：它把最容易误报的四种假阳性——语言限制、class 量化、代表选择、
existence-to-name interface——逐项固定为有来源的控制。它没有完成的是发现一个 `u/F/C/I/O/Done` 同时保真、
且存在 P2/P3 张力的实际 ZFC consumer。

因此，第一阶段既不是“已经找到 ZFC Q”，也不是“锻刀与发现脱钩”。每一张 `Q-R`、`SOURCE_PAYMENT` 或
`ANTI_ANALOGY_CONTROL` 都是对 P 的负校准：它说明哪一种表面花纹不能让 Q 涌现。接下来若继续，必须让新来源
有机会改变这个判词，不能只重复已知 payment。

## 4. 后续 source admission：只有四种来源值得进入下一轮

下一份分母只有满足以下至少一项时才建立：

1. **未付真实 consumer：** 来源中的 ZFC-side consumer 声称与已支付任务相同的 Done，却没有实际提供其所需
   witness、maps、choice、marking、formation 或 language payment；
2. **形成—使用交错：** 资料显示某个对象的合法性／存在仍需追问时，该对象已在同一理论层被算符、判断或
   consumer 使用；
3. **Power Set-subset route：** 在 HMZ-009/010/012 之后，新来源必须同时保留 \(\mathcal P(A)\)-subset formation、版本固定的 actual consumer和同一任务的 `u/F/C/I/O/Done`，或给出真正的 formation-use/admission structure；
4. **H0 transport bridge：** 有 ZFC 一等对象能保留 H0 的 subject、process、observation 与 Done，并逐门通过
   T0–T5。

若一份材料只再次说明“HoTT 更方便”“ZFC 是一阶语言”“需要 choice”或“类型系统防错”，则它不进入新的
run；这些已在第一阶段有来源和控制。

## 5. 仍开放、但尚未获准成为 Q 的研究入口

| 入口 | 为什么仍值得看 | 当前缺口 |
|---|---|---|
| Voevodsky 2006 *homotopy λ-calculus* 等早期技术原典 | 可能提供与构造／表达有关的不同作者语言。 | 必须先显示它产生不同于三轮的 R，并有 ZFC-side counterpart。 |
| ZFC actual consumer corpus | 只有真实 mathematical/formal consumer 才能决定 payment 是否被静默省略。 | 尚未发现同一 Done 的未付案例。 |
| Power Set / Replacement | 它们仍是明显理论承诺，也是既有 P-FORGE 的保留站位。 | HMZ-009 已固定 Power Set–quotient technical bridge；HMZ-010 证明 `RepFun` route 的 consumer已有显式 payment；HMZ-012把“时间”收紧成 finite Done vs formal Done 的可验证 mismatch。仍缺保留 \(\mathcal P(A)\)-subset formation的同一 `C/I/O/Done` consumer，也不授权从来源调查直接启动 P-DAG。 |
| H0→Z0 | 用户提出的最强传输路线。 | T0–T5 尚未形成正向对象。 |

本文件是第一阶段来源综合，不是项目完成收据。项目仍处于 `ACTIVE / SOURCE_ADMISSION_REQUIRED`；下一步由新的
可审来源触发，而不是由“目前未命中”的焦虑或更多同义检索触发。

## 6. 预检收据：Hλ 没有触发完整 successor run

Voevodsky 2006 的 [Hλ 预检](20261003-HMZ-004-hlambda-preflight/MANIFEST.md)已完成。它确实包含不同的技术语汇：
proof compiler、受算法验证的子系统、扩张产生 ZF proof obligation、model-level 与 type-system-level 的差别。
但本身没有给出 ZFC-side 同一 `u/F/C/I/O/Done`，也没有 source-supported P2/P3。因此它被归档为
`ADMISSION_REJECTED_WITH_SCOPE`，而非被错误登记为一份“Q 发现”或无边界完整 run。

Makkai 1996 的 [anafunctor 预检](20261003-HMZ-005-makkai-anafunctor-preflight/MANIFEST.md)则检验了另一条、
更接近真实消费者的线：从“每对对象存在一个积”到“给每对对象选定一个 ordinary product functor”。来源明确写出
这个 ordinary-output task 的 simultaneous Choice，并用 output contract 不同的 product anafunctor 作为 canonical
替代；更强 Cartesian-closed 任务又明确使用 SCSA。它因此给出 `EXPLICIT_CHOICE_PAYMENT + OUTPUT_CONTRACT_CHANGE`，
而非同一 Done 的未付 consumer；同样是 `ADMISSION_REJECTED_WITH_SCOPE`。

这两份预检促成一项 SOP 澄清：相关关键词或一个实际 consumer 本身不足以开启完整 run；只有新 `R_i`、精确
ZFC-side `u/F/C/I/O/Done`、未付同一 Done 或 formation-use交错才足够。预检保存否定性控制和重开条件，不能被
合并进“已读完三轮”的分母。

Voevodsky 2011 的 [WoLLIC 预检](20261003-HMZ-006-wollic-machine-preflight/MANIFEST.md)则给出一条新的作者级
`R-MACHINE` 原话：ZFC-based proof-assistant formalization 曾导致“不自然构造”。它没有列出被指的项目、编码或
同一 Done，故不能从修辞直接造 Z-card；状态是 `PAIRING_SOURCE_REQUIRED`。这条线的下一步不是再找同义讲演，而是
寻找被作者话语实际指向的具名 ZFC-in-Coq attempt 或另一份同一任务技术原典。

这个配对随后以 [HMZ-007 Werner ZFC-in-CIC](20261003-HMZ-007-werner-zfc-coq-pair/MANIFEST.md) 闭合为一个
独立冻结分母。Werner 并非被 WoLLIC 明确点名，因而保留 `CANDIDATE_PAIRING_NOT_ATTRIBUTED`；但其论文和源码给出
精确的 `Ens`／Power／Replacement／Russell consumers。结果不是 Q：full ZFC 在该 model 中以 EM + TTDA/TTCA 等
non-computational Choice principles 支付，Russell 只反证一个假定的 universal `Ens` container，Power 又是 host CIC/Prop
construction。因此它把“ZFC-in-Coq不自然”从泛称压到可反驳的具体 task，并得出 `SOURCE_PAYMENT +
ANTI_ANALOGY_CONTROL`。

`R-HIGHER` 的 [HMZ-008 Set/ZF semantic run](20261003-HMZ-008-higher-hits-set-semantics/MANIFEST.md) 则把
“directly”进一步校正为 task-interface 词。Lumsdaine–Shulman 的 HIT 模型要求 fibrancy、stability、local-universes
等明确语义工作；Swan 同时给出 ZF 内正面的 image-preserving QW/HIT constructions，以及另一类 QW-type 的 ZF
nonexistence/cardinal边界。该交叉结果说明：Set/ZF semantic construction 有正有负，却没有与 HoTT formation rule
同一 Done 的未付消费者；因此是 `MODEL_SEMANTIC_PAYMENT + ASSUMPTION_BOUNDARY`，不是 ZFC Q 或 H0 transport。

最后，[HMZ-009 HoTT Book Power Set—quotient 预检](20261003-HMZ-009-book-powerset-quotient-preflight/MANIFEST.md)补上了
第一阶段原先刻意保留的狭窄缺口：Book 的集合论式 quotient 确实把 equivalence classes 写为 \(\mathcal P(A)\) 的子集，
并与 \(A\sslash R\) 和 set-quotient 比较。这是 `CONSTRUCTION_BRIDGE_PARTIAL`，不是已完成的 `R→Z→Q`：Book 未交付
bare-ZFC actual consumer，且其 own universe/resizing 与 external/internal 路线都被显式标为成本。因此本轮只升级为
`PAIRING_SOURCE_REQUIRED`；下一个来源必须固定同一 quotient task 的 ZFC-side consumer 和 payment ledger，不能用更多 Power Set
术语替代它。

[HMZ-010 Isabelle/ZF quotient consumer 预检](20261003-HMZ-010-isabelle-zf-quotient-consumer-preflight/MANIFEST.md)随后提供了
这个 pairing test：`EquivClass.thy` 不是只说 quotient 存在，而是定义 \(A//r\)、给出 introduction/elimination 和 class-level
operations。然而它的 formation 是 `RepFun`／functional replacement，而不是 Book 所述 \(\mathcal P(A)\)-subset route；且 `equiv`、
congruence、membership 与 type contracts 都明示。结论因而是 `ACTUAL_CONSUMER + F_ROUTE_MISMATCH + SOURCE_PAYMENT /
ADMISSION_REJECTED_WITH_SCOPE`。这并不恢复“Power Set 没有 bridge”的旧结论，而是把下一入口进一步收窄到**同一 Power Set-subset
route**的 actual consumer，或一个能显示未付 formation-use 的来源。

[HMZ-012 totality/partition reality-source run](20261003-HMZ-012-totality-partition-reality-source/MANIFEST.md)进一步把 Dochtermann
2011 的有限分类 Done、无限 complete partition、Power Set-forming class collection 和 rational-class object use 纳入冻结分母。
它确实让“时间维度”变成一个可引用的 source bridge；但 paper自称 conceptual metaphor，ZFC formation sources说的是 sethood，
Isabelle consumer又换成 `RepFun`。因此 `Done_h` 与 `Done_z` 未被证明相同，且无P2/P3。HMZ-012的保真结局为
`REALITY_TASK_TO_TOTALITY_CONSTRUCTION_BRIDGE / SAME_TASK_NOT_ESTABLISHED / P_REQUALIFICATION_REQUIRED`；它为未来的同一任务证据定义了精确缺口，而非建立Q。

[HMZ-013 universe-shift H0 preflight](20261003-HMZ-013-universe-shift-h0-preflight/MANIFEST.md)检查了另一条非 quotient 的 H0 入口。Voevodsky 2013将 \(U_i\) 的 model 置于“ZFC with \(\omega+2\) universes”，Shulman 2008则以inaccessible \(\kappa\) 的 \(V_\kappa\) 和 universe-juggling 讨论实际 category-theory consumer。后者明确保留了“同一个 \(G\) 未必跨 universe 保持”的 guard。故这一对来源提供 `TECHNICAL_CORRESPONDENCE + EXPLICIT_SCOPE/IDENTITY_PAYMENT`，但不保留 same task、P2/P3或H0 transport，判`ADMISSION_REJECTED_WITH_SCOPE`。
