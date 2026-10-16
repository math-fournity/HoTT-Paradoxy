# HoTT 非现实性悖论的不可停机机器统观方案

> 文档角色：当前研究方案与动态路线图  
> 版本：`nontermination-machine-overview-plan/v1.12`  
> 状态：`ACTIVE`  
> 当前所有者：机器统观研究线  
> 首次冻结日期：2026-09-14  
> 适用工作树：`/Volumes/D/HoTT-machine-overview`  
> 当前分支：`feat/machine-overview-m1`  
> 更新方式：每完成一个可复核实验单元或发生一次重要反证，原位修订当前判断，并在文末保留简洁的版本日志。

## 1. 研究目的

本方案把“不可停机”提升为 HoTT 非现实性悖论机器统观的一条主轴，但不预先把任何未完成的关联写成定理。它要系统回答五个相互区分的问题：

1. 在 HoTT、立方类型论及其社区证明工具中，哪些计算、归约、证明检查或证明搜索过程可能不完成？
2. 其中哪些只是通用计算理论现象，哪些依赖 HoTT 特有或立方类型论特有的结构？
3. 用户提出的两类非现实性方向，是否能通过“完成性差异”得到具体、可运行、可缩减的见证？
4. Gödel 不完备性、对角化、可表示性、自指、反射与 Löb 条件，能否在某个社区 HoTT 框架中形成对象层实例，而不仅是外部类比？
5. 一个被观察为不完成的证明进程，何时能够支持数学结论，何时只能支持关于某次执行、某个实现或某项控制设置的有限陈述？

本研究的最终成果不是“找到一个会一直运行的程序”。目标是得到一份可复现的结构化解释：精确指出理论规则、程序表示、证明任务、观察量、现实对应和非完成行为之间的因果链；并通过对照、消融、跨框架复核和反例来确定每条结论的适用范围。

本文件拥有不可停机/Gödel 主线的动态执行状态；完整候选空间、程序化激发方法、开放世界未知入口和跨路线阶段验收由
`/Volumes/D/HoTT_AI_HANDOFF_20260911/.codex/research/hott/HOTT-PARADOX-PROGRAMMATIC-EXPLORATION-COMPLETENESS.md`
及其 5 个 shards 统一拥有。系统化研究必须先
读取该规划，不得让本文件的一条纵向路线再次遮蔽 Path/HIT/univalence/modalities/2LTT、现实消费者、反解释或未知发现。

## 2. 中心研究假说及其当前证据地位

### 2.1 总假说

用户提出的工作假说是：

> 第一类非现实性方向——理论构造引入了现实对象所不具有的无限细分、无限前提或额外完成义务；第二类非现实性方向——理论在未先询问计算合法性或可计算性的情况下，把某个对象、证明或能力纳入推演。两者在足够具体的程序化表现中，都可能汇聚为某种完成性断裂，包括归约不完成、证明检查不完成、证明搜索不完成或运行不完成。直指循环是这一汇聚的最小形态之一。

当前证据等级：`RESEARCH_THESIS_TO_BE_TESTED`。

这不是已经证明的 HoTT 元定理。研究必须允许以下反证结果出现：

- 某个候选只有资源消耗增长，没有数学上的非终止性；
- 某个候选是通用语言或证明器现象，移除 HoTT 构造后仍完整存在；
- 某个候选是生产性无限对象，在每个有限观察下都完成；
- 某个候选只来自显式关闭终止性判定的控制设置；
- 某个候选没有与现实活动保持同一任务、同一输入或同一观察量；
- 某个 Gödel 类结果只能在元理论中表述，尚不能成为所选 HoTT 实现中的对象层定理。

### 2.2 两类方向的可检验化

**方向 A：理论新增完成义务。** 固定一个现实任务与可观察结果，构造与之对应的形式任务；然后判断理论表示是否额外引入稠密索引、无限细化、全局一致性、规范形计算或高阶路径相容义务，使形式过程无法在与现实任务相同的观察边界内完成。

**方向 B：未先询问计算合法性。** 固定一个对象构造、证明构造或反射构造，检查框架是否在缺少终止性、生产性、可判定性或可实现性证明义务时仍允许它进入可计算推演；再判断后续判断相等、规范化、引用自身或证明自身性质时是否出现非完成。

这两个方向可以共享完成性观察器，但必须分别保留任务对应、理论依赖和因果归属，不能因为都出现超时就合并成同一个结论。

## 3. 术语与观察层级

研究中的“不可停机”必须拆成以下不同现象；任何报告都要明确自己观察的是哪一项：

| 层级 | 研究对象 | 可观察事件 | 不能直接推出 |
|---|---|---|---|
| `E0` | 固定命令的一次运行 | 在预先声明的时间或资源窗内未返回 | 数学上的永不终止 |
| `E1` | 证明搜索或自动化策略 | 搜索树持续扩张、未找到证明或反证 | 命题不可判定；固定证明不能被内核检查 |
| `E2` | 项归约、规范化、定义相等判定 | 归约未达到所需规范形 | 程序运行语义一定发散 |
| `E3` | 证明检查 | 内核为核验给定证明而被迫执行未完成的归约 | 理论整体不一致；HoTT 特有缺陷 |
| `E4` | 宏、战术或反射程序 | 元程序执行未完成 | 对象理论的项本身不终止 |
| `E5` | 编译或运行程序 | 对固定输入的执行不完成 | 证明检查不完成；现实对应已建立 |
| `E6` | 生产性无限对象 | 整体无最终端点，但每个有限观察均完成 | 失败；矛盾；非生产性循环 |
| `E7` | 数学不可判定性 | 不存在解决某类全部输入的总算法 | 每个实例都不完成；某次超时证明了不可判定性 |
| `E8` | Gödel 不完备性 | 满足精确条件的形式系统存在不可证真句或无法内部证明某类一致性主张 | 程序超时；理论矛盾；现实对应 |

“时间”保留为运动、时空连续性及现实过程的广义要素；“时序”用于事件的先后、依赖、因果、可见性与执行顺序。芝诺类方向可能针对时间被数轴稠密性重新表示后的异化，而并非只针对离散时序。机器实验如果只检查调用顺序，就不能声称已经检验了时间连续性问题。

## 4. 资格等级：何时可以说“找到”

每个候选按照下列等级逐步资格化：

| 等级 | 判据 | 允许的结论措辞 |
|---|---|---|
| `N0 OBSERVATION_LIMIT` | 固定环境、输入和观察窗，进程未完成；保留退出状态与原始输出 | “在该观察窗内未完成” |
| `N1 CAUSAL_CONTROLS` | 正控制、负控制和至少一项因果消融区分输入错误、普通慢执行与目标机制 | “非完成与所列因素组合一致” |
| `N2 ORDINARY_CONFIGURATION` | 不依赖手工撤销框架通常要求的终止性、生产性或一致性条件 | “在该框架通常接受的配置中复现” |
| `N3 HOTT_ESSENTIALITY` | 移除 HoTT/立方特有结构后现象消失，或有形式化归约证明该结构不可删 | “HoTT/立方结构是见证的必要组成” |
| `N4 NATURAL_CONSUMER` | 真实库定理、规范化器、反射器、HIT/路径消费者或典型工作流自然触发现象 | “在冻结的自然使用场景中出现” |
| `N5 REALITY_CORRESPONDENCE` | 固定同一任务、输入、观察量和完成标准，论证现实过程与理论过程的差异 | “现实相对非现实性候选得到对应支持” |
| `N6 MACHINE_PROVED_CLAIM` | 精确命题、假设和禁止外推已由相称的证明内核检查并留存收据 | “在所列范围内获得机器证明” |

一个候选可以在不同维度分别获得等级。例如，它可以在计算因果上达到 `N1`，在 HoTT 必要性上仍停留于 `N0`，在 Gödel 对应上仍为 `QUESTION`。

### 4.1 本项目判定“有效发现”的最低组合

要把结果称为“HoTT 非现实性悖论的程序化见证”，至少需要：

- `N1` 因果控制；
- `N2` 通常配置；
- `N3` HoTT 或立方结构必要性；
- `N4` 自然消费者；
- `N5` 同任务现实对应；
- 数学性措辞还必须达到 `N6`。

低于这个组合的结果仍然有研究价值，但只能称为校准、表示边界、实现现象、候选或未决义务。

## 5. 社区实现的分母与层级

“完整”必须相对于公开、冻结、可复核的实现分母来定义。初始分母如下；后续按版本、构建条件和研究价值修订。

### 5.1 Tier A：已具备当前机器执行条件

| 框架 | 当前角色 | 首轮任务 |
|---|---|---|
| Agda Cubical v0.9 / Agda 2.8.0 | 主执行框架；原生 Path、HIT、univalence 相关库 | 归约、反射、定义相等、终止性、自然消费者扫描 |
| 精确历史 CCTT forcing-tick 分支 | 时间/时序与 forcing tick 表示边界的历史复现 | tick irrelevance、quotation、反射与归约观察 |
| agda-unimath 冻结提交 `7b81411d` | 大型社区形式化库样本 | 自然定义、递归模式、等价/完备化相关消费者筛选 |

### 5.2 Tier B：需要资格化、构建或版本固定

| 框架 | 研究价值 | 资格化问题 |
|---|---|---|
| Coq-HoTT | intensional Coq/Rocq 上的 HoTT 库；不同内核与选项 | 构建版本、`-noinit`/`-indices-matter`、归约和终止边界 |
| UniMath | 大型 univalent mathematics 工程 | 计算内容与命题内容的分离、自然消费者、自动化完成性 |
| MetaRocq | quotation、反射、可验证检查器、对象层/元层连接 | 可表示语法、证明谓词、强规范化假设边界、Löb 路线 |
| Arend | 以 HoTT 为基础的证明助理与编程语言 | termination、interval/path 计算、meta 执行 |
| cubicaltt | 直接立方类型论实验实现 | canonicity、evaluation、HIT 与 path computation |
| redtt / cooltt | Cartesian cubical type theory、NbE 和 elaboration | 规范化、相等判定与实现完成性 |

### 5.3 Tier C：历史对照

| 框架 | 研究角色 |
|---|---|
| HoTT-Agda | 早期 `--without-K --rewriting` 路线的历史差异 |
| Lean 2 HoTT 模式 | 历史原生 HoTT/HIT 设计对照 |
| Lean 3/4 | 只用于一般递归、元编程和证明器对照；不作为当前原生 HoTT 框架 |

框架分母的每次增删都要记录版本、来源、原因和对“完整性”措辞的影响。

## 6. 候选空间

### 6.1 方向 A：理论新增完成义务

候选族包括：

1. **稠密参数化与有限运动任务**：现实任务只需要到达或越过一个观察阈值，形式任务却要求遍历、构造或核验稠密索引上的全部中间结构。
2. **无限相干义务**：有限可实施操作被提升为需要无限层高阶路径相容的数据。
3. **完成化与极限对象**：现实中的逐步可观察过程，被表示为先取得一个完成对象再使用；检验其构造或消去是否暗中要求完成无限计算。
4. **商、高阶归纳类型与计算规则**：对象层等价压缩了差异，但后续消费者为恢复代表或判定计算内容而引入无法完成的工作。
5. **定义相等中的全局规范化要求**：局部现实判断被转化为必须比较大项、高阶路径项或反射生成项的规范形。

每个候选都必须带有现实端任务规格，避免缩减时把消费者删掉而悄然换题。

### 6.2 方向 B：未先询问计算合法性

候选族包括：

1. **显式递归项进入定义相等**：构造可自我展开的项，再由类型检查迫使它与另一规范形比较。
2. **反射程序生成或重建递归定义**：区分“反射能观察语法”“反射能声明对象”“新对象进入归约”三个阶段。
3. **不透明递归与透明递归的差别**：比较同一自指结构在不可展开和可展开状态下的证明检查行为。
4. **部分性单子/延迟类型**：区分可表示“可能不完成”与证明器自身不完成；检查商去除步数信息后是否产生观察义务。
5. **一般递归编码**：检查 well-founded recursion、sized types、guarded recursion、partiality 与显式终止断言的边界。
6. **证明搜索与自动化**：单独研究搜索非完成，不能把它冒充给定证明的内核检查非完成。

### 6.3 Gödel、对角化与自我指涉分支

Gödel 分支不以“制造一个循环”作为完成标准。它需要逐层完成以下证明义务：

1. **系统对象固定**：明确是哪一个可递归呈现、表达力足够且一致性条件明确的理论或内核片段。
2. **语法对象化**：在系统内或经过已证明保真的编码表示项、类型、上下文、推导或证明对象。
3. **可替换与可对角化**：构造 substitution/diagonal operation，并证明表示忠实性。
4. **证明谓词表示**：定义 `Prov_T` 或相应可检查推导关系，并证明所需的可表示性条件。
5. **导出条件**：明确使用 Gödel、Hilbert–Bernays–Löb 或 Lawvere 不动点路线中的哪组前提。
6. **对象层定点句**：得到与“自身不可证”“若可证则……”或特定计算不完成断言对应的句子。
7. **外部元理论结论**：区分对象层可写、对象层可证、元层真、元层不可证和机器已检查五种状态。
8. **HoTT 必要性分析**：判断构造是否仅依赖一般算术/递归语法，还是 univalence、Path、HIT、截断或模态结构在其中不可删。
9. **现实对应**：只有在同一任务、同一观察和明确解释下，才讨论其非现实性含义。

可优先尝试的三条具体路线：

- `G1 MetaRocq/Coq-HoTT`：借助 quotation 与证明对象表示，建立最接近显式 Gödel 编码的路线；
- `G2 Agda Cubical 内嵌小理论`：先在 Agda 中定义一个可递归检查的对象语言及其推导，再判断哪些结果能在 cubical 模式中复用；
- `G3 Lawvere 不动点路线`：研究 point-surjective/弱点满条件、对角映射与 HoTT 中同伦化等价之间的关系，避免把普通集合论不动点定理仅换名为 HoTT 结果。

### 6.4 外部研究方案的交叉综合与路线修订

用户指定的外部方案已经全文读取并保存为 byte-identical 本地快照：

- 原位置：`/Volumes/D/HoTT_AI_HANDOFF_20260911/外部资料/在 HoTT 中寻找“不可停机—不完备性边界”的研究方案：从计算性限制到 Gödel 型自指的可执行路线.md`；
- 读取身份：主工作树 untracked 文件，1115 行、54,342 bytes；
- SHA-256：`a1d541e551f001bbb6c204ae673a583e00098dd0b69c2308e54738d488db2613`；
- 稳定快照：`machine-overview/literature/snapshots/在HoTT中寻找不可停机不完备性边界-20260914.md`；
- 来源索引：`machine-overview/literature/README.md`。

该方案给出了三条应直接纳入当前计划的主链：

1. **Cubical Agda 对象机器线**：在标准终止性、覆盖性和正性检查全部启用的片段中定义确定性机器、`Halts`、`DoesNotHaltWithin` 与 `Diverges`。第一步同时机器证明一个停机实例和一个显式循环实例；第二步才以 universal machine/diagonal 或既有 many-one reduction 证明不存在统一停机判定器。
2. **Coq-HoTT Gödel/Rosser 线**：先把普通对象理论的 syntax、quotation、substitution、proof checker 与 `Provable` 移植到 HoTT 兼容层；再完成 fixed point/Rosser。只有之后才编码 `MiniHoTT` 本身，不能从“HoTT 内证明 PA 不完备”跳到“HoTT 自己不完备”。
3. **元层搜索对照线**：用可受界的 proof enumerator 与外层部分计算展示“证明合成可能不完成、给定证明的内核核验仍完成”。该线服务层级区分，不能独自成为 HoTT 悖论结论。

该方案建议的数学对象定义被采纳为 U3/U4 的首个形式规格：

\[
\mathrm{Halts}(M,x)
:=\left\|\sum_{n:\mathbb N}\mathrm{Final}(\delta_M^n(\mathrm{init}(x)))\right\|_{-1},
\]

\[
\mathrm{Diverges}(M,x)
:=\prod_{n:\mathbb N}\neg\mathrm{Final}(\delta_M^n(\mathrm{init}(x))).
\]

这里的命题截断只保留“存在有限停机步数”的命题内容；具体发散证明本身必须是终止的证明项。随后要证明的全称边界是

\[
\neg\prod_{M,x}\mathrm{Dec}(\mathrm{Halts}(M,x)),
\]

而不是用运行超时替代该定理。

该方案的 `R0–R5` 结果层级与本计划的 `E0–E8`/`N0–N6` 互补：`R0` 是运行观察，`R1` 是具体发散的形式证明，`R2` 是停机不可判定性，`R3` 是 HoTT 内证明对象理论不完备，`R4` 是元理论证明一个精确 HoTT calculus 不完备，`R5` 才是 trusted HoTT 推出底类型。最终报告会同时使用两套坐标：`R*` 表示数学结论种类，`N*` 表示一个现实相对候选的资格完成度。

**保留的关键张力**：外部方案把“HoTT 内可表达、但不存在统一总算法解决的命题族”提议为 *non-reality boundary witness*。当前项目不直接接受这一命名提升。一般不可判定性和不完备性说明形式系统不能由一台全局决定器穷尽；要成为用户所说的现实相对非现实性悖论，还必须通过 `N5`：固定现实任务、理论任务、同一输入、同一观察量与同一完成标准，并证明理论表示恢复、预先保留或新增了什么。这个差异将作为最终报告的核心哲学裁决之一。

## 7. 学术文献地图

状态词约定：`PRIMARY_ENTRY_FOUND` 表示已定位一手论文或官方项目入口；`ABSTRACT_CHECKED` 表示已核摘要/书目信息；`FULL_TEXT_TO_READ` 表示尚需全文提取精确前提；`EXPERIMENT_MAPPED` 表示已对应到机器实验；`FORMAL_DEPENDENCY` 表示预期成为形式命题的直接依赖。

| ID | 传统/主题 | 文献或项目 | 当前取得的精确意义 | 对本研究的作用 | 状态 |
|---|---|---|---|---|---|
| `LIT-TURING-1936` | 可计算性 | Turing, *On Computable Numbers, with an Application to the Entscheidungsproblem*[^S01] | 机器计算与判定问题的经典起点；需要按原文区分 circle-free、satisfactory number 与后来的 halting 表述 | 建立一般不可判定性基线，防止把有限观察当作停机定理 | `PRIMARY_ENTRY_FOUND; FULL_TEXT_TO_READ` |
| `LIT-CHURCH-1936` | 不可判定性 | Church, *An Unsolvable Problem of Elementary Number Theory*[^S02] | λ-可定义性与不可解性经典来源 | 与 Turing 路线交叉核对“算法不存在”的范围 | `PRIMARY_ENTRY_FOUND; FULL_TEXT_TO_READ` |
| `LIT-GODEL-1931` | 不完备性 | Gödel, *Über formal unentscheidbare Sätze…*[^S03] | 形式系统中的算术化、对角化与不可判定命题 | Gödel 分支的原始前提与结论来源 | `PRIMARY_ENTRY_FOUND; FULL_TEXT_TO_READ; FORMAL_DEPENDENCY` |
| `LIT-KLEENE-RECURSION` | 自指/定点 | Kleene, *On Notation for Ordinal Numbers*；Moschovakis 的前提展开[^S25] | 第二递归定理在 Kleene 1938 短文 §2 末尾出现；现代形式给出程序索引的计算定点 | 连接“代码化自指”与实际递归程序，并为 Gödel 分支提供程序侧对角机制 | `PRIMARY_ENTRY_FOUND; MODERN_STATEMENT_CHECKED; FULL_TEXT_TO_READ` |
| `LIT-POST-1944` | 递归可枚举性 | Post, *Recursively Enumerable Sets of Positive Integers and Their Decision Problems*[^S26] | 递归可枚举集合、归约与不可解度的经典系统化 | 区分半判定、枚举、全决定和不可解度层级 | `PRIMARY_ENTRY_FOUND; FULL_TEXT_TO_READ` |
| `LIT-RICE-1953` | 程序语义性质 | Rice, *Classes of Recursively Enumerable Sets and Their Decision Problems*[^S04] | 非平凡语义性质的一般不可判定性 | 限定自动寻找器能够完备决定的属性范围 | `PRIMARY_ENTRY_FOUND; FULL_TEXT_TO_READ` |
| `LIT-RADO-1962` | 忙海狸 | Radó, *On Non-Computable Functions*[^S05] | 由有限机器空间的最大值构造不可计算函数；原文强调该构造不依赖枚举所有可计算函数 | 设计有限尺寸但完成时间不可统一计算的压力族；不能冒充 HoTT 必要性 | `PUBLISHER_ENTRY_CHECKED; ABSTRACT_CHECKED` |
| `LIT-LOB-1955` | 可证明性逻辑 | Löb, *Solution of a Problem of Leon Henkin*[^S06] | 内部可证明性与自指的固定点约束 | Gödel/反射分支的导出条件与反误读基线 | `PRIMARY_ENTRY_FOUND; FULL_TEXT_TO_READ; FORMAL_DEPENDENCY` |
| `LIT-LAWVERE-1969` | 范畴定点 | Lawvere, *Diagonal Arguments and Cartesian Closed Categories*[^S07] | 用闭笛卡尔范畴中的点满条件统一对角论证 | 探索 HoTT/∞-群胚语境中定点论证的精确移植义务 | `PRIMARY_ENTRY_FOUND; FULL_TEXT_TO_READ` |
| `LIT-CAPRETTA-2005` | 部分性/共归纳 | Capretta, *General Recursion via Coinductive Types*[^S08] | 以 coinductive partial elements 表示一般递归 | 区分“在类型内表示非完成”与“检查器本身不完成” | `ABSTRACT_CHECKED; FULL_TEXT_TO_READ; EXPERIMENT_MAPPED` |
| `LIT-ABEL-FOETUS` | 终止性分析 | Abel, *foetus—Termination Checker for Simple Functional Programs*[^S09] | 依赖型函数程序的终止分析传统 | 为 Agda 终止性检查与控制实验提供历史基线 | `PRIMARY_COPY_FOUND; FULL_TEXT_TO_READ` |
| `LIT-SCT-2001` | 终止性判定 | Lee, Jones, Ben-Amram, *The Size-Change Principle for Program Termination*[^S27] | 若每条无限调用序列都迫使良基数据发生无限下降，则程序终止；局部 size-change graph 可组成判定程序 | 建立自动终止审查器、保守拒绝和可组合控制维度 | `PUBLISHER_ENTRY_CHECKED; ABSTRACT_CHECKED` |
| `LIT-GDTT-2016` | guarded dependent type theory | Bizjak et al., *Guarded Dependent Type Theory with Coinductive Types*[^S10] | later modality、clock/guarded recursion 与 coinduction | 生产性无限对象和普通循环的核心区分 | `ABSTRACT_CHECKED; FULL_TEXT_TO_READ; EXPERIMENT_MAPPED` |
| `LIT-CLOCKED-2017` | clocked type theory | Bahr et al., *The Clocks Are Ticking: No More Delays!*[^S11] | clock quantification、强规范化和 canonicity 路线 | CCTT forcing tick 实验的直接理论背景 | `PRIMARY_ENTRY_FOUND; FULL_TEXT_TO_READ; EXPERIMENT_MAPPED` |
| `LIT-PRODUCTIVE-2009` | 生产性 | Atkey & McBride, *Productive Coprogramming with Guarded Recursion*[^S12] | guarded recursion 支撑有限观察的生产性 | `E6` 与真正归约不完成的对照 | `PRIMARY_ENTRY_FOUND; FULL_TEXT_TO_READ; EXPERIMENT_MAPPED` |
| `LIT-PARTIALITY-REVISITED` | 部分性商 | *Partiality, Revisited*[^S13] | 部分性表示及商/延迟结构的类型论处理 | 检验 tick/step irrelevance 是否只消去外延步数而保留元层完成差异 | `PRIMARY_ENTRY_FOUND; FULL_TEXT_TO_READ` |
| `LIT-CUBICAL-CANONICITY` | 立方类型论元理论 | Huber, *Canonicity for Cubical Type Theory*[^S28] | 在其精确理论中，只有 name variables 的上下文中的自然数项判断性等于某个 numeral；证明使用有类型确定性操作语义 | 给“立方计算天然导致非完成”的宽泛主张提供直接反约束，并确定自然数闭项探针的预期 | `PUBLISHER_COPY_CHECKED; ABSTRACT_CHECKED; FORMAL_DEPENDENCY` |
| `LIT-CUBICAL-NORMALIZATION` | 立方类型论元理论 | Sterling & Angiuli, *Normalization for Cubical Type Theory*[^S29] | 为 univalent Cartesian cubical type theory 建立 normalization，并推出判断相等可判定与类型构造子单射性 | 把搜索焦点转向精确理论范围之外的扩展、反射和消费者，而不是预设核心判断相等不完成 | `PRIMARY_ENTRY_FOUND; ABSTRACT_CHECKED; FULL_TEXT_TO_READ; FORMAL_DEPENDENCY` |
| `LIT-AGDA-TERMINATION` | 实现语义 | Agda termination checking 与 reflection 文档[^S30] | 终止性审查、透明/不透明递归以及 reflection `normalise` 的官方行为合同 | 解释当前三因素探针并固定各控制组的实现语义 | `OFFICIAL_DOCUMENTATION_CHECKED; EXPERIMENT_MAPPED` |
| `LIT-GODEL-COQ-2005` | 不完备性机器化 | O'Connor, *Essential Incompleteness of Arithmetic Verified by Coq*[^S31] | 形式化一阶逻辑、primitive recursive functions、数值编码及表示定理，机器核验 Gödel–Rosser 不完备性；其正文明确记录 substitution trace 技巧与 unary self-code 的巨大归约成本 | 为 G1/G2 的最小对象化部件、工程规模和当前 Nat code 成本观察提供直接范本 | `PRIMARY_PDF_DOWNLOADED_HASHED; RELEVANT_SECTIONS_READ; FORMAL_DEPENDENCY` |
| `LIT-GODEL-ISABELLE-2014` | 不完备性机器化 | Paulson, *A Machine-Assisted Proof of Gödel’s Incompleteness Theorems for the Theory of Hereditarily Finite Sets*[^S32] | 以 hereditarily finite set theory 机器化第一、第二不完备性定理 | 为第二不完备性、内部一致性陈述与元层条件提供对照 | `REPOSITORY_ENTRY_CHECKED; ABSTRACT_CHECKED; FULL_TEXT_TO_READ` |
| `LIT-SYNTHETIC-INCOMPLETENESS-2021` | synthetic computability | Kirst & Hermes, *Synthetic Undecidability and Incompleteness of First-Order Axiom Systems in Coq*[^S37] | 通过从 H10/PCP 的 many-one reductions 机器化 PA/ZF 片段的语义与演绎 entailment 不可判定，并抽象出可扩展公理化的不完备性条件 | 提供 R2→R3 的 reduction 路线，避免重复全部低层机器编码；同时要求把标准模型等附加假设显式化 | `PRIMARY_PDF_DOWNLOADED_HASHED; RELEVANT_SECTIONS_READ` |
| `LIT-GODEL-WITHOUT-TEARS-2023` | synthetic incompleteness | Kirst & Peters, *Gödel’s Theorem Without Tears*[^S38] | step-indexed partial functions + EPF、self-return predicates、strong separation 与 extension 直接构造 classifier 不完成的 index 和 independent sentence | 已移植为 Cubical Agda 条件性 synthetic essential incompleteness 核；作者 Coq 源的最终目标已在固定历史环境中两次干净构建并资格化关键定理 | `PRIMARY_PDF_DOWNLOADED_HASHED; SOURCE_REPO_PINNED; CORE_THEOREMS_READ; AUTHOR_COQ_NATIVE_BUILD_EXACT_REPLAYED; EXPERIMENT_MAPPED` |
| `LIT-COQ-UNDECIDABILITY-LIBRARY` | 机器化 reduction graph | Coq Library of Undecidability Proofs[^S39] | 含 Turing、Minsky、FRACTRAN、λ-calculus、proof-theoretic target 的可重放 many-one reductions，明确区分 seed/advanced/target problems | 为有限 ProgramCode、Minsky halting 与跨模型 reduction 提供成熟源码分母 | `OFFICIAL_PROJECT_FOUND; SOURCE_QUALIFICATION_PENDING` |
| `LIT-TWO-LEVEL-TT` | HoTT 自身元理论 | Annenkov, Capriotti, Kraus & Sattler, *Two-Level Type Theory and Applications*[^S40] | 外层严格类型论作为 inner HoTT 的内部化元理论；某些元理论陈述不能直接在 inner HoTT 中表达 | 为 R4 MiniHoTT/HoTT syntax、strict substitution 与同层表示代价提供直接学术框架 | `PRIMARY_PDF_DOWNLOADED_HASHED; RELEVANT_SECTIONS_READ; FORMAL_DEPENDENCY` |
| `LIT-CT-CUBICAL-ASSEMBLIES` | Church thesis 与 univalence | Swan & Uemura, *On Church’s Thesis in Cubical Assemblies*[^S41] | Church thesis 不成立于完整 cubical assemblies model；作者构造反射子宇宙，使 Church thesis 在其中成立并与 univalent type theory 相容 | 说明 synthetic incompleteness 与 univalence 不先验冲突，同时迫使每个 HoTT 实例明确其 universe/modality 与 EPF 适用域 | `PRIMARY_PDF_DOWNLOADED_HASHED; ABSTRACT_AND_MODEL_ROLE_READ; FORMAL_DEPENDENCY` |
| `LIT-ROCQ-TYPECLASSES` | 自动证明搜索 | Rocq 9.x Typeclasses reference[^S33] | `typeclasses eauto` 默认使用 depth-first search；未给 depth 时搜索无界；可显式设深度、迭代加深与 debug trace | 为 Coq-HoTT reflective-subuniverse 搜索不完成提供官方实现语义，并把有限深度拒绝与观察窗区分 | `OFFICIAL_DOCUMENTATION_CHECKED; EXPERIMENT_MAPPED` |
| `LIT-FIRST-CLASS-TYPECLASSES` | 自动证明搜索 | Sozeau & Oury, *First-Class Type Classes*[^S34] | Coq 类型类机制的原始工程/学术背景 | 解释自动实例登记如何把数学结构转化为 proof-search graph | `AUTHOR_ENTRY_CHECKED; FULL_TEXT_TO_READ` |
| `LIT-HOTT-LIBRARY-PAPER` | Coq-HoTT | Bauer et al., *The HoTT Library*[^S35] | Coq 中形式化基本 HoTT、univalence、HIT、synthetic homotopy theory、category theory 与 modalities | 固定第二主平台的理论范围；连接当前 reflective-subuniverse 实验 | `ABSTRACT_CHECKED; OFFICIAL_SOURCE_CHECKED; EXPERIMENT_MAPPED` |
| `LIT-HOTT-MODALITIES` | HoTT modalities | Rijke, Shulman & Spitters, *Modalities in Homotopy Type Theory*[^S36] | 在 HoTT 中发展 reflective subuniverses、modalities、factorization systems 和 localization HIT | 判断自动化递归中的数学结构来源，并避免把搜索策略等同于 modality 理论 | `ABSTRACT_CHECKED; FULL_TEXT_TO_READ; EXPERIMENT_MAPPED` |
| `LIT-CUBICAL-AGDA` | 社区实现 | Agda Cubical library[^S14] | Agda 中 cubical type theory、univalence、HIT 的主流实验库 | Tier A 主执行分母 | `OFFICIAL_PROJECT_FOUND; EXPERIMENT_MAPPED` |
| `LIT-COQ-HOTT` | 社区实现 | Coq-HoTT[^S15] | Coq/Rocq 上的 HoTT 库与特定内核选项；commit `cc618472…` 已在 Rocq 9.0.1 完整构建 | 跨内核复核、自然 proof-search consumer 与 Gödel 移植 | `OFFICIAL_PROJECT_FOUND; NATIVE_BUILD_QUALIFIED; FIRST_EXPERIMENT_REPLAYED` |
| `LIT-UNIMATH` | 社区实现 | UniMath[^S16] | 大型 univalent mathematics 工程 | 自然消费者与计算内容审查 | `OFFICIAL_PROJECT_FOUND; BUILD_TO_QUALIFY` |
| `LIT-AGDA-UNIMATH` | 社区实现 | agda-unimath[^S17] | Agda 中 univalent mathematics | Tier A 大型库样本 | `OFFICIAL_PROJECT_FOUND; EXPERIMENT_PENDING` |
| `LIT-HOTT-AGDA` | 历史实现 | HoTT-Agda[^S18] | 早期 Agda HoTT 库及 rewriting 路线 | 历史差异对照 | `OFFICIAL_PROJECT_FOUND; HISTORICAL_ONLY` |
| `LIT-AREND` | 社区实现 | Arend[^S19] | 基于 HoTT 的证明助理与编程语言 | termination/meta/path 交叉实现 | `OFFICIAL_PROJECT_FOUND; BUILD_TO_QUALIFY` |
| `LIT-CUBICALTT` | 社区实现 | cubicaltt[^S20] | 直接立方类型论实现，含 univalence/HIT | 评价直接执行语义与 Agda 实现差异 | `OFFICIAL_PROJECT_FOUND; BUILD_TO_QUALIFY` |
| `LIT-REDTT` | 社区实现 | redtt[^S21] | Cartesian cubical type theory 实验实现 | NbE/相等检查对照 | `OFFICIAL_PROJECT_FOUND; BUILD_TO_QUALIFY` |
| `LIT-COOLTT` | 社区实现 | cooltt[^S22] | Cartesian cubical type theory、NbE 与 elaboration | 当前实现的规范化边界 | `OFFICIAL_PROJECT_FOUND; BUILD_TO_QUALIFY` |
| `LIT-METAROQ` | 反射/验证 | MetaRocq[^S23] | quotation、对象语言表示和可验证检查器；若使用强规范化等假设须逐项登记 | Gödel对象化和反射路线的优先框架 | `OFFICIAL_PROJECT_FOUND; FULL_TEXT_TO_READ; BUILD_TO_QUALIFY` |
| `LIT-HOTT-LEAN2` | 历史实现 | Lean 2 HoTT/HIT 文档[^S24] | 历史原生 HoTT 模式 | 实现谱系对照 | `OFFICIAL_SOURCE_FOUND; HISTORICAL_ONLY` |

## 8. 机器统观体系

机器统观由七个相互约束的部件组成：

1. **来源与工具链资格器**：固定框架版本、编译器、库树、构建命令、平台和哈希；区分社区源码、项目派生源码与实验探针。
2. **候选规格器**：每个 `TaskSpec` 固定方向 A/B/Gödel、对象层/元层、输入、消费者、观察量、完成标准、允许构造和禁止外推。
3. **有类型候选生成器**：在框架允许的语法与类型规则内生成候选；搜索空间需要声明完备域，不能把有限枚举写成无限域完备性。
4. **受界执行器**：分别运行检查、规范化、反射、证明搜索、编译和程序执行；记录 CPU/墙钟、内存、退出状态、stdout/stderr 和重复结果。
5. **任务保持缩减器**：缩减非完成候选时保留原始消费者、同一观察量和关键 HoTT 构造；任何移除都形成因果消融记录。
6. **对应审查器**：恢复、预先保留、新增三分登记现实对象与理论对象的差异，显式标记尚无现实语义的构造。
7. **Gödel 义务追踪器**：把语法编码、替换、证明谓词、导出条件、定点句、元理论假设和 HoTT 必要性分别建项，阻止用“出现自循环”跳过中间证明义务。

结果索引的最小字段为：`case_id`、`revision`、`framework`、`direction`、`phenomenon_layer`、`source_hashes`、`consumer`、`observation`、`controls`、`ablation`、`rerun`、`hott_essentiality`、`reality_correspondence`、`godel_obligations`、`evidence_grade`、`verdict`、`prohibited_extrapolation`。

### 8.1 完备性必须按量词分层

本方案使用“完备”时必须指明分母，不能把下列六种主张互相替换：

1. `COMP-1` 流程结构完备：候选经历资格化、冻结、生成、执行、缩减、核验、对应审查、重放和索引；
2. `COMP-2` 冻结文法枚举完备：固定 TaskSpec、grammar 与 bound 内的全部良类型候选被遍历；
3. `COMP-3` 冻结资料分母完备：预先声明的源码/论文集合与观察维度被逐项处理；
4. `COMP-4` 候选归约完备：目标候选类中的每个对象都能保真归约到当前 grammar；
5. `COMP-5` HoTT 专属机制链完备：精确 HoTT 规则、不可完成定理、自然消费者与现实任务差异全部贯通；
6. `COMP-6` 全局发现/否定完备：算法总能找到任意存在的悖论，并在不存在时停机给出否定证书。

当前 `COMP-1` 已在 strict-v2 链成立。`PF-CUBICAL-CANDIDATE-COVERAGE-001` 已对一个精确 bounded `never/now/later` grammar 机器证明 `COMP-2`：全部 `Raw n` 候选进入 `allRaw n`，规范化保持 convergence、deadline observation、horizon 与 expected observation，每个 reduced candidate 进入 canonical space；其它 `COMP-2/3` 主张仍只在逐项声明的冻结切片成立。`COMP-4/5` 未建立；`COMP-6` 既未建立，也不是包含一般部分计算后合理的总算法目标。Turing/Rice/Gödel 文献给出的元理论约束要求系统采用公平枚举、正反证书与 `UNRESOLVED` 状态，而不是把 timeout 或无命中改写为全局否定。

完备性审计的当前 owner 是：

`machine-overview/evaluations/NONTERMINATION-OVERVIEW-COMPLETENESS-AUDIT-001/REPORT.md`。

跨全部 TheoryConstruct、激发算子、consumer、oracle 与框架的父级覆盖包络见：

`/Volumes/D/HoTT_AI_HANDOFF_20260911/.codex/research/hott/HOTT-PARADOX-PROGRAMMATIC-EXPLORATION-COMPLETENESS.md`。
本计划每次新增候选或负结论，都要定位到该
规划的八轴张量并说明未触达 axes、out-of-envelope 检查和下一 bounded successor。

## 9. 实验协议

### 9.1 冻结顺序

每项评价按以下顺序执行：

1. 写 `SCOPE.json`，固定问题、来源、版本、探针、预期观察和资格门；
2. 运行现有协调器自检与工作区校验；
3. 生成 `FREEZE.json`，哈希 evaluator、scope、工具链和输入；
4. 冻结后才生成正式候选与决定文件；
5. 执行首轮与逐字节重放；
6. 由独立 `verify --rerun` 重跑并核所有哈希；
7. 形成报告和索引；
8. 只有新 revision 才能改变冻结范围。

### 9.2 观察窗的语义

`timeout` 或退出码 124 只表示过程在给定观察窗内没有完成。要提高结论强度，必须补足：

- 至少两次独立运行；
- 相同输入与环境的逐字节结果或被解释的非确定性；
- 正常完成正控制；
- 快速拒绝负控制；
- 单因素或最小组合消融；
- 更长观察窗或增长曲线，用于排除普通固定延迟；
- 数学证明，若要从有限观察提升为“永不终止”或“该类问题不可判定”。

### 9.3 完成性三因素模型

当前校准采用三个因素：

1. 存在自递归或可自我展开的项；
2. 该项被声明为可供定义相等计算展开；
3. 某项证明检查迫使它达到不同的规范形。

三个因素同时出现时，当前精确 Agda 探针在观察窗内未完成。任一因素移除后分别出现生产性停止边界、有限类型拒绝或快速接受。这个三因素模型当前只具有 `N1` 校准地位；由于关键探针依赖显式终止断言，尚未达到 `N2`。

### 9.4 现实对应协议

每个非现实性候选必须回答：

- 现实活动是什么？
- 输入和输出是什么？
- 现实活动何时算完成？
- 理论表示增加、删除或预先假定了什么？
- 非完成发生在对象层、证明层、搜索层还是实现层？
- 如果使用另一个等价表示，现象是否仍存在？
- 该差异是时间连续性、事件时序、信息可得性还是计算资源的差异？

对应审查不自动给出哲学裁决；它只使主张的缺口和依赖可见。

## 10. 阶段路线图

### U0：方案、术语与文献基线

**目标**：形成完整路线、来源分母、资格等级和可追溯文献索引。  
**产物**：本文档；首轮来源清单；未解决书目表。  
**完成条件**：Turing—Gödel—Kleene—Rice—Löb—Lawvere—termination—partiality—guarded recursion—cubical normalization 的主要谱系均有一手来源入口，且每项都有对应机器问题。  
**当前状态**：`IN_PROGRESS`；Kleene、Post、Radó、size-change、cubical canonicity/normalization、Kirst–Hermes/Kirst–Peters/O’Connor 三组不完备性材料、2LTT、Church thesis/cubical assemblies、Rocq typeclass search、Coq-HoTT 与 modalities 来源已补齐；Kirst–Peters 作者 Coq 源已固定提交、两次干净构建并资格化关键定理。尚需 Robinson/SLD 原始来源、一般终止性综述、MetaRocq 论文、Minsky/halting formalization及 HoTT 内部不完备性相关工作的定向检索。

### U1：反射、tick 与证明检查非完成的因果校准

**目标**：完成 CCTT/Agda 的反射边界和完成性三因素实验。  
**产物**：`REFLECTED-TICK-REDUCTION-OBSERVER-001` 的冻结、运行、重放、报告和测试。  
**完成条件**：10 个探针全部符合冻结预期；独立 rerun；明确 `N0/N1` 与 `N2–N6` 缺口。  
**当前状态**：`COMPLETE_WITH_LIMITS`。  
**当前运行摘要**：revision 5 run deterministic SHA `69db8953ea10d57ca81bc0fca0eaca74d97c4063ed606cec94bead3f8667829b`；现实相对结论 `NOT_ESTABLISHED`；Gödel 结论 `GENERIC_SELF_REDUCTION_CALIBRATION_ONLY`。Revision 1 的 `ba808d…` run 保留，但其完整 `HoTT/formal` 树分母已从 83 文件演化到 99 文件，验证器按设计报告 stale；不是旧 probe 结果被反驳。
**独立复核**：revision 5 把当前 99-file/384,804-byte formal tree 保存为含逐文件 hash 的冻结来源快照，不再让未来无关 formal-tree 增长使旧 probe replay 失效；10 个探针每项分类与预注册期望一致，首轮/内置 replay/独立 `--rerun` 的原始输出逐字节一致。Revision 2/3 的路径与 Agda module qualification 失败均有保留收据，不计入数学结果。

### U2：社区框架资格化

**目标**：使 Tier B 中优先框架具备可重复构建和最小探针运行条件。  
**顺序**：Coq-HoTT → MetaRocq → UniMath → cooltt/cubicaltt → Arend → redtt。  
**完成条件**：每个入选框架有版本哈希、构建收据、最小正负控制；不能构建者有精确阻塞证据。  
**当前状态**：`IN_PROGRESS`。Coq-HoTT commit `cc6184729bf8572a1d188c7a46f8d224f40bcceb` 已用 Rocq 9.0.1 完整构建，build tree=4451 files / 74,553,091 bytes / SHA `f54181b1…d2ee`；`COQ-HOTT-REFLECTIVE-TYPECLASS-RECURSION-001` 的 8 个探针已首轮、重放、独立 rerun 全部一致。MetaRocq 尚未构建。

### U3：跨框架完成性矩阵

**目标**：对项归约、定义相等、反射、证明搜索、对象机器运行、生产性分别建立可比实验；并落实外部方案的 Cubical `Machine → Halts/Diverges → undecidability` 主链。  
**完成条件**：至少两个独立内核家族完成同一 TaskSpec 的可比运行；每个候选明确 HoTT 必要性。  
**当前状态**：`IN_PROGRESS / R1_REACHED`。`PF-CUBICAL-MACHINE-HALTING-001` 已在 Agda 2.8.0 + Cubical v0.9 中机器证明一个立即停机程序的 `Halts`、一个固定循环程序的 `Diverges`，以及 `¬ Halts loopProgram initial`；canonical run `20260914-CUBICAL-MACHINE-HALTING-001` 已索引并逐字节重放。尚缺有限 `ProgramCode`、universal evaluator 与 diagonal/reduction，所以 R2 undecidability 未建立；跨第二内核同题移植也未完成。

### U4：Gödel 与代码化自指

**目标**：完成至少一条 G1/G2/G3 路线的对象语言、证明谓词和对角义务；若不能完成，给出最小未决节点。  
**完成条件**：不得以一般递归循环替代不完备性；每个前提、对象层句子和元层结论均可定位。  
**当前状态**：`IN_PROGRESS / CONDITIONAL_SYNTHETIC_CORE_PLUS_EFFECTIVE_CLASSIFIER_MACHINE_PROVED / AUTHOR_COQ_Q_INSTANCE_REPLAYED_WITH_PREMISES`。既有 ERCF3-T3 已有 repaired `Tm`/`Fml` Nat coding、decoder、substitution-on-code 和 diagonal-instance shape；新的五包链则从另一侧完成实际 proof relation：`PF-CUBICAL-GODEL-PROOF-CHECKER-001` 定义小型对象逻辑、unindexed `RawProof` 与总 Bool checker，并证明 checker soundness 和 indexed derivation 擦除 completeness；`PF-CUBICAL-GODEL-PROOF-SERIALIZATION-001` 把 proof tree 往返序列化；`PF-CUBICAL-GODEL-FORMULA-BITCODE-001` 与 `PF-CUBICAL-GODEL-PROOF-BITCODE-001` 给出自定界有限 Bool 码；`PF-CUBICAL-GODEL-NAT-PROOF-CODE-001` 最终证明 `RawProof → ℕ` 的往返解码、单射、自然数域总 checker 的 commutation，以及 `NatChecked φ` 与 `⊢ φ` 的双向连接。五包 canonical runs 均已索引、冻结并 exact replay。在其旁，`PF-CUBICAL-SYNTHETIC-INCOMPLETENESS-001` 已机器证明：显式 `Universal θ` 下任何 self-return separator 都在构造出的 index 上数学发散；带有效 proof/refutation classifier 且 strong-separating 的 formal system 因而产生 independent sentence，并把结论传给 extensions。`PF-CUBICAL-GODEL-PROOF-SEARCH-CLASSIFIER-001` 又从自然数 proof code 穷举构造 `proofClassifier`，以 Boolean semantics 证明 K/S/MP consistency、跨 stage 确定性和 proof/refutation 双向对应，得到 `HilbertSystem : FormalSystem Fml negF`。因此 classifier 参数已经在当前小型 calculus 上消去。

Kirst–Peters 作者 Coq 源 `cd7d849…` 的 `fol_incompleteness.vo` 已在 Coq 8.15.2 历史依赖环境中从两个独立干净 worktree 构建；1,284 个稳定 `.vo/.vos/.vok/.glob` 产物及最终目标逐文件 exact，独立资格化模块加载 `self_halting_diverge`、`recursively_separating_diverge`、`insep_essential_incompleteness`、`epf_mu_ctq` 与 `Q_incomplete` 并 exact replay。该外部实例精确显示：`Q_incomplete` 仍要求 Peirce、`CTQ`、理论包含 `Qeq`、可枚举性与一致性；`epf_mu_ctq` 仍要求 `is_universal theta_mu`。因此本地最小缺口仍是**universality + strong separation/representability + exact HoTT calculus**；当前 K/S/MP 语言没有算术与相应公理，不能提供这项实例，作者的 Robinson `Q` 实例也没有把其对象理论改成 HoTT。

### U5：自然消费者、留出集与反证搜索

**目标**：在预先冻结的社区代码与留出任务中寻找自然触发，测试研究者是否因已知候选而过拟合。  
**完成条件**：报告发现、未发现与不可执行三类结果；候选缩减保持消费者；至少一次盲化或留出集复核。  
**当前状态**：`PENDING`。

### U6：学术级综合报告

**目标**：把理论史、计算实验、HoTT 实现、Gödel 分支、现实对应和所有负结论整合为一篇可独立审阅的报告。  
**完成条件**：见第 11 节；关键数学结论满足本 repo 的机器证明门禁。  
**当前状态**：`PENDING`。

## 11. 最终报告结构与验收

最终报告计划采用以下结构：

1. 问题意识：抽象、否定现实前提与非现实性推演；
2. 时间与时序的区分；
3. 两类悖论方向及完成性总假说；
4. 从 Turing、Church、Gödel 到 Rice、Kleene、Löb、Lawvere 的理论谱系；
5. 类型论中的规范化、一般递归、部分性、共归纳、guarded recursion 与生产性；
6. HoTT/立方类型论社区实现全景；
7. 机器统观系统、冻结协议和证据等级；
8. 每个候选族的实验、消融和缩减；
9. Gödel 分支的对象层构造与未决义务；
10. 自然消费者与跨框架比较；
11. 现实对应：时间、时序、运动、计算与完成；
12. 反证、失败实例与此前没有找到 HoTT 缺陷的原因；
13. 已成立结论、候选、未知和后续可证问题。

“完整、完备”的可审计含义是：

- 对冻结的框架分母逐项给出已执行、不可执行或不适用的证据；
- 对冻结的候选族逐项给出结果与资格等级；
- 对核心文献谱系逐项给出一手来源、精确前提、与实验的映射；
- 对每项正面结论给出反例尝试和禁止外推；
- 对每个数学性断言给出相称的机器证明或明确降级；
- 对未完成项目给出最小阻塞节点，不能用总体性措辞遮盖缺口。

## 12. 当前基线判断

目前已经建立一个很简单但严格受限的事实：显式允许自递归定义参与判断性归约后，给定一个迫使该项与不同规范形比较的证明目标，精确 Agda 进程在 4 秒观察窗内未完成；同一项的自等式快速完成，不透明版本快速被类型规则拒绝，guarded 无限流在 delay 边界上完成规范化。Reflection 对该递归项执行 `normalise` 时也在同一观察窗内未完成。

这个结果证明了不可停机方向是可执行的机器研究路径，也证明“写出一个令证明进程不完成的代码”本身并不困难。它尚未证明 HoTT 的非现实性悖论，原因是：

- 核心非完成探针使用了显式终止断言，未达到 `N2`；
- 移除 HoTT/立方特有构造后，同类自递归机制仍成立，未达到 `N3`；
- 冻结社区源码中尚未找到自然消费者，未达到 `N4`；
- 尚无同任务现实对应，未达到 `N5`；
- 4 秒观察是运行证据，不是永不终止的机器证明，未达到 `N6`；
- 自递归校准没有建立 Gödel 编码、证明谓词或导出条件，因此不是 Gödel 不完备性实例。

这组负限制决定下一步不能继续堆叠更多人为循环，而要优先寻找通常配置下的自然消费者，并把 Gödel 对象化义务放进可执行框架。

## 13. 方案更新规则

每个自然工作单元结束后必须回答：

1. 新结果提高了哪个资格等级？
2. 它减少了哪个关键未知？
3. 它是否只是重复一个通用计算理论现象？
4. 它是否改变框架分母或候选优先级？
5. 它是否迫使修订总假说？
6. 下一项最小可验证工作是什么？

若答案只增加局部细节而不提高资格等级、不减少关键未知，就停止该局部深化，返回未贯通的主链。

## 14. 更新日志

### 2026-09-14 — v1.0

- 建立不可停机机器统观的完整首版方案。
- 把用户关于两类悖论汇聚于完成性断裂的认识登记为待检验总假说。
- 建立 `E0–E8` 现象层级与 `N0–N6` 资格等级。
- 固定首轮社区实现分母和 A/B/Gödel 三条候选空间。
- 纳入从 Turing、Church、Gödel 到现代 partiality、guarded recursion、cubical/HoTT 实现的首轮文献地图。
- 登记 `REFLECTED-TICK-REDUCTION-OBSERVER-001` 的现有运行结论及其五项关键缺口。

### 2026-09-14 — v1.1

- 完成 U1 的独立 `verify --rerun`：10/10 探针分类和原始输出均与冻结运行一致。
- 补齐 Kleene 1938、Post 1944、Radó 1962、size-change termination 的一手书目信息。
- 纳入立方类型论 canonicity 与 normalization 结果，把它们作为宽泛非完成假说的反约束。
- 纳入 Coq 与 Isabelle 中不完备性定理机器化工作的直接范本，细化 Gödel 分支的工程义务。
- 更新优先级：U1 之后先寻找通常配置中的自然消费者，并并行建立 MetaRocq/Coq-HoTT 的对象化路线。

### 2026-09-14 — v1.2

- 全文读取用户指定的 1115 行外部方案，保存 SHA-256 固定的 byte-identical 快照并建立 `machine-overview/literature/README.md`。
- 采纳 Cubical Agda `Machine → Halts/Diverges → NoUniversalHaltingDecider`、Coq-HoTT Gödel/Rosser、MiniHoTT 自编码和元层 proof-search 对照三线；保留“一般不可判定性不自动通过现实对应门”的张力。
- Coq-HoTT `cc618472…` 在 Rocq 9.0.1 下完整构建并保存 build receipt；当前源码 675 tracked entries，构建树 4451 files。
- 完成 `COQ-HOTT-REFLECTIVE-TYPECLASS-RECURSION-001`：普通配置有限失败；普通实例/resolve 登记达到观察边界；有限深度 trace 显示递进 `O_functor` 义务；已知等价完成；一般类型类递归复现。
- 当前资格为 `N0 PASS / N1 PASS / N2 FAIL / N3 FAIL / N4 PARTIAL / N5 FAIL / N6 FAIL`；结果是社区 HoTT 自动化递归边界，不是 HoTT 理论悖论或 Gödel 实例。
- 下一最小主链从继续制造元层循环改为：先在 Cubical Agda 标准检查片段中机器证明具体 `Halts`/`Diverges`，同时为 MetaRocq/Coq-HoTT 的 syntax/substitution/provability 路线做资格化。

### 2026-09-14 — v1.3

- 修复 canonical Agda capture 对 linked worktree 的根判定：使用 `git rev-parse` 固定 top-level/git-dir/common-dir/HEAD/branch；主 checkout、linked worktree、子目录和非 repo 两正两负测试通过。
- 新增 `HoTT/formal/cubical-machine-halting/MachineHalting.agda` 和精确 `CLAIM.md`：确定性两计数器指令、configuration、total step、finite iterate、`Halts`、`Diverges`。
- `PF-CUBICAL-MACHINE-HALTING-001` 机器证明 `MP-CMH-HALTS-001`、`MP-CMH-DIVERGES-001`、`MP-CMH-NOT-HALTS-001`；run exit 0 / stderr 0，claim matrix 已索引，index rows 已冻结，独立 rerun `EXACT_EXIT_STDOUT_STDERR_MATCH`。
- 研究等级首次从 R0 运行观察提升到 `R1 CERTIFIED_DIVERGENCE`：被证明不停止的是对象机器，证明项与内核检查均完成。
- 明确 R2 缺口：当前 `Program = ℕ → Instr` 尚无有限语法编码、enumeration、decode、universal evaluator 或 standard reduction；一个具体 loop 不推出停机问题不可判定。
- 明确 Gödel 缺口：尚无证明谓词、derivability conditions 或 fixed-point sentence。下一步并行推进 finite ProgramCode/universal simulation 与现有 ERCF3 repaired syntax 之上的 provability representation。

### 2026-09-14 — v1.4

- 重开 C8/T3 Gödel 线：本轮用户明确要求持续寻找 HoTT 中的 Gödel 不完备性，满足旧文档“新的元数学原文改变方向”的重开条件；旧 `GATED` 历史结论仍保留为当时状态。
- 新增 `PF-CUBICAL-GODEL-PROOF-CHECKER-001`：总 Bool checker 的 soundness、indexed derivation 的 erase/check completeness、`Checked` 与 derivation 双向函数、命题截断 `Provable` 以及正负控制全部 machine checked。
- 该包没有用 `ProvRepresentability.repr` 一类对象推导 constructor 假定表示性，而是先证明真实 raw proof checking；因此把旧“证明谓词接口”推进为可执行关系。
- 五个 claims 已进入 canonical run `20260914-CUBICAL-GODEL-PROOF-CHECKER-001`，matrix 6 rows 冻结，独立 rerun exact match。
- 文献地图加入 Kirst–Hermes 2021、Kirst–Peters 2023、Coq undecidability reduction graph 与 2LTT；下一决策是“完整数值编码路线”与“synthetic reduction 路线”并行比较。
- Gödel 状态仍为 `INFRASTRUCTURE_ONLY`：没有 object-level representability、diagonal sentence 或 unprovability theorem，禁止使用“HoTT 的 Gödel 定理已完成”。

### 2026-09-14 — v1.5

- 把 Gödel 基础设施从 raw checker 贯通到自然数证明码：新增 postfix proof serialization、自定界公式位码、自定界 proof 位码和自然数 proof code 四包；连同 v1.4 checker 包形成五段可独立重放的 source/run/index 链。
- `PF-CUBICAL-GODEL-NAT-PROOF-CODE-001` 机器证明 proof-bit 前缀稳定性、Bool-list→ℕ 编码的已知长度往返与长度界、`decodeProofNat (codeProof p) ≡ just p`、`codeProof` 单射、`checkProofNat` commutation、`NatChecked φ → ⊢ φ` 与 `⊢ φ → NatChecked φ`，以及一正一负控制。
- canonical run `20260914-CUBICAL-GODEL-NAT-PROOF-CODE-001`：Agda 2.8.0-3d04bac + Cubical v0.9，exit 0、stderr 0；matrix 6 rows 冻结；独立 rerun 为 `EXACT_INDEX_SNAPSHOT_MATCH` 与 `EXACT_EXIT_STDOUT_STDERR_MATCH`。
- 发现并修正一项验证设计问题：在 Agda 的一元自然数表示中，直接归约大型 concrete proof code 会出现指数级资源成本；改用最小 K proof 与无效码 `0` 后，全量核验约 19 秒完成。该现象登记为表示/归约成本，不作为不可停机或不完备性证据。
- Gödel 路线当前精确边界：外部 proof predicate 已有效呈现并数值化；对象语言仍只是小型命题演算，没有足够算术、对象层 representability、fixed-point sentence 或 incompleteness theorem。下一最小包转向算术对象语言与 representability 接口。

### 2026-09-14 — v1.6

- 下载、哈希、提取并核对 Kirst–Hermes 2021、Kirst–Peters 2023、O’Connor 2005、2LTT 与 Swan–Uemura 五组一手 PDF；原件/文本/页数/提取器身份进入外置文献 cache manifest。
- 固定 Kirst–Peters accompanying Coq repository at commit `cd7d8490f8542bfe85658c465bcb26b2ed163f53`，直接读取 partial function、EPF、formal-system classifier 与 abstract incompleteness 源码。
- 新增 `PF-CUBICAL-SYNTHETIC-INCOMPLETENESS-001`：以真实 step-indexed `core : ℕ → OptionBool` 定义确定性部分计算；在显式 `Universal θ` 下构造任何 self-return separator 的具体发散 index；从 strong separation 构造 independent sentence，并把结论传给 formal-system extensions。
- canonical run `20260914-CUBICAL-SYNTHETIC-INCOMPLETENESS-001`：exit 0 / stderr 0，matrix 6 rows 冻结，独立 rerun exact；源文件无 `postulate` 或终止性绕行声明。
- 当前 Gödel 结论第一次超过“编码基础设施”：抽象 essential-incompleteness 核已 machine proved；但它仍是条件定理，`Universal`、有效 classifier 与 strong separation 尚未由当前小型对象理论或 exact HoTT calculus 实例化。
- Swan–Uemura 约束了下一步：Church thesis 的 HoTT 适用域必须绑定到具体 cubical/univalent 模型或反射子宇宙；不得把它无条件添加到任意 HoTT 实现。

### 2026-09-14 — v1.7

- 扩展 canonical Agda capture：新增显式、去重、repo-contained 的 `--include-dir`，使跨 formal-package imports 的精确 include 路径进入 `RUN.json` 与 source manifest；缺失目录、普通文件、symlink 与 `..` 路径均在运行前拒绝；回归 4/4 PASS。
- 新增 `PF-CUBICAL-GODEL-PROOF-SEARCH-CLASSIFIER-001`：Boolean semantics 证明 K/S/MP calculus 的 `bot` 不可导与正反不可并证；stage `n` 检查 Nat proof code `n` 的正反两侧；每项成功结果与 checker 接受双向对应；跨任意 stages 的结果确定。
- 构造 `proofClassifier φ : PartBool`，机器证明 `⇓ true ↔ ⊢ φ` 与 `⇓ false ↔ ⊢ negF φ`，最终得到 `HilbertSystem : FormalSystem Fml negF`。这消去了 v1.6 synthetic theorem 的 effective-classifier 参数。
- canonical run `20260914-CUBICAL-GODEL-PROOF-SEARCH-CLASSIFIER-001`：11 个 source-manifest files、2 个 include dirs、exit 0 / stderr 0、matrix 5 rows frozen、独立 exact replay。
- 当前决定性缺口：`Universal θ` 与 `StronglySeparates HilbertSystem (SelfReturns θ true) (SelfReturns θ false) r`。由于当前语言只有 atom/bot/imp 且仅 K/S axioms，任意 atoms 不可直接导出；必须引入足够算术/表示性或选择另一 exact object theory，不能把 strong separation 作为 constructor 假定。

### 2026-09-14 — v1.8

- 全套 selftest 首次随新 formal packages 增长到 84 项时发现旧 reflection/termination run 的完整 `HoTT/formal` tree denominator 失效；验证器正确返回 `REFLECTED_TICK_TREE_CHANGED`，而非错误沿用旧全树结论。
- 保留两个真实 refresh 失败：revision 2 的 probes 位于 evaluator 允许根之外，零 native probes；revision 3 位于允许根内但 Agda module name 与相对路径不符，20 次调用均在模块解析阶段 exit 42。两者均有 failure receipt，不冒充目标探针结果。
- Revision 4 在生成 probe 前重新冻结当前 `HoTT/formal` 99 files / 384,804 bytes / tree SHA `925765a8…1ad4`，并使用 top-level `Rev4*` 文件/模块匹配修复路径。
- Run `20260914-REFLECTED-TICK-REDUCTION-OBSERVER-004` 的 10 个探针全部符合原预期，独立 rerun 10/10 exact；当前 deterministic SHA `c1fcde82…8b2f`。结论仍是 implementation-level reflection/termination calibration，未因 Gödel 基础设施加入而升级。

### 2026-09-14 — v1.9

- 审查 revision 4 后发现：把 live `HoTT/formal` 全树作为每次 replay 的动态依赖，会让以后每个无关证明包再次使运行 stale。该行为适合 freshness 提醒，不适合作为长期可重放收据。
- Revision 5 把 99-file formal tree 转为 hash-pinned 历史来源快照：逐文件 bytes/SHA、aggregate identity、50 个 Agda/literate sources、annotation regex 与 0 matches 全部冻结；live project formal tree 不再是动态 `trees[]` 依赖。
- Run `20260914-REFLECTED-TICK-REDUCTION-OBSERVER-005` 再次得到 10/10 preregistered classes 和 10/10 independent exact rerun；freeze `49c190d0…0cd0`、decisions `3493a929…7271`、run `69db8953…829b`。
- 这项修订只校正证据量词与生命周期，不改变数学判词；未来新增 formal packages 不再伪装成旧 operational probe 的语义变化。

### 2026-09-14 — v1.10

- 新增六层完备性语义：strict-v2 的流程闭环与冻结 grammar/denominator 内的相对完备性，和仍未建立的候选归约、HoTT 专属机制链及全局发现完备性明确分离；完整审计进入 `NONTERMINATION-OVERVIEW-COMPLETENESS-AUDIT-001`。
- 在固定 `coq-synthetic-incompleteness@cd7d849…` 上使用 Coq 8.15.2 与固定历史依赖，从两个独立干净 worktree 原生构建 `FOL/Incompleteness/fol_incompleteness.vo`；两次 stdout/stderr、1,284 个稳定内核产物及最终 `.vo` 精确一致。
- 独立资格化模块加载五个核心常量并 exact replay；`Print Assumptions` 没有发现未列出的全局公理，但定理签名中的 `is_universal theta_mu`、`CTQ`、Peirce、extension/strong separation、包含 `Qeq`、enumerability 与 consistency 仍是显式前提。
- 该复现确认本地 Cubical synthetic 包抓住了作者定理的结构骨架，同时把剩余缺口从笼统的“需要 Gödel”收窄为：为 exact HoTT calculus 建立 universality/算术解释、proof enumeration、strong representability 与现实对应。
- 当前全套 coordinator selftest 为 90/90，workspace validate 为 VALID、0 errors；作者 Coq replay 专项 4/4，Cubical Gödel 专项 6/6，capture 专项 4/4，reflection revision-5 专项 8/8。

### 2026-09-14 — v1.11

- 新增 `PF-CUBICAL-CANDIDATE-COVERAGE-001`，第一次把完备性审计中的 `COMP-2` 做成当前 repo 的 Cubical Agda 定理，而不只依赖协调器运行计数。
- 对每个 bound `n`，机器证明 `allRaw n` 覆盖精确 `never/now/laterR` grammar；`normalize` 把显式 later syntax 化为 R041 canonical `Delay Bool`，并保持 convergence 与所有 deadline observations。
- `reduceCandidate` 原样保留 horizon 与 expected observation，保持 actual observation；每个 reduced candidate 均进入 `canonicalSpace`。五个 claims 已进入 run `20260914-CUBICAL-CANDIDATE-COVERAGE-001`，matrix 6 rows 冻结，独立 rerun exact。
- Agda 接受 coverage theorem，同时保留 `UnsupportedIndexedMatch` 诊断：`allRaw-complete` 不声明在 transported indexed input 上的 judgemental reduction，当前包也没有此类 consumer。该限制进入 claim、run non-goals 与专项测试。
- 这一进展不关闭 `COMP-4`：当前仍无定理把所有相关 HoTT 悖论候选保真归约到 `Raw n`；它也不关闭 HoTT 专属性或现实对应。全套 selftest 随 4 项专项回归增长为 94/94。

### 2026-09-14 — v1.12

- 将本文件明确降为不可停机/Gödel 动态执行 owner；项目运行目录新增五分片父级
  `HOTT-PARADOX-PROGRAMMATIC-EXPLORATION-COMPLETENESS`，覆盖八轴搜索张量、14 个 HoTT 构造族、14 个激发算子、
  A/B/Gödel/时间与反解释候选族、六类 generator、oracle 组合、UnknownIngress、遗漏/holdout 和 P0–P9 阶段。
- 系统化 TaskSpec 必须定位 TheoryConstruct×AbstractionChange×RealityOrTask×Consumer×ObservationLayer×
  CompletionProperty×Oracle×Framework，并记录 finite remainder/infinite fairness/reduction preservation、未触达 axes 与
  bounded successor；无命中继续只在具名分母内成立。
- 项目运行目录的 AGENTS、`hott-paradox-research` 1.9.0 与 `hott-local-session-governance` 3.7.0 安装该消费合同；开放世界未知
  通过新来源/版本/实现/consumer、dimension/operator/oracle、差分、反例与现实对应进入，新发现必须修旧 envelope。
- 该变化是研究规划与治理，不新增数学 claim；当前 worktree 仍 `LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`，主线 current owners
  与 checkpoint 留给 canonical integrator。

## Sources

[^S01]: Alan M. Turing, “On Computable Numbers, with an Application to the Entscheidungsproblem,” *Proceedings of the London Mathematical Society* 42 (1936–1937), 230–265, [publisher entry](https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/plms/s2-42.1.230), DOI: `10.1112/plms/s2-42.1.230`.
[^S02]: Alonzo Church, “An Unsolvable Problem of Elementary Number Theory,” *American Journal of Mathematics* 58(2) (1936), 345–363, [archival PDF](https://www.cis.upenn.edu/~cis5110/Church-UnsolvableProblemElementary-1936.pdf).
[^S03]: Kurt Gödel, “Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I,” *Monatshefte für Mathematik und Physik* 38 (1931), 173–198, [publisher entry](https://doi.org/10.1007/BF01700692), DOI: `10.1007/BF01700692`.
[^S04]: Henry Gordon Rice, “Classes of Recursively Enumerable Sets and Their Decision Problems,” *Transactions of the American Mathematical Society* 74(2) (1953), 358–366, DOI: [`10.1090/S0002-9947-1953-0053041-6`](https://doi.org/10.1090/S0002-9947-1953-0053041-6).
[^S05]: Tibor Radó, “On Non-Computable Functions,” *Bell System Technical Journal* 41(3) (1962), 877–884, [publisher entry](https://onlinelibrary.wiley.com/doi/abs/10.1002/j.1538-7305.1962.tb00480.x), DOI: `10.1002/j.1538-7305.1962.tb00480.x`.
[^S06]: Martin Hugo Löb, “Solution of a Problem of Leon Henkin,” *Journal of Symbolic Logic* 20(2) (1955), 115–118, [JSTOR entry](https://www.jstor.org/stable/2266895), DOI: `10.2307/2266895`.
[^S07]: F. William Lawvere, “Diagonal Arguments and Cartesian Closed Categories,” in *Category Theory, Homology Theory and Their Applications II* (1969), [Theory and Applications of Categories reprint](https://www.tac.mta.ca/tac/reprints/articles/15/tr15abs.html), [PDF](https://www.tac.mta.ca/tac/reprints/articles/15/tr15.pdf), DOI: `10.1007/BFb0080769`.
[^S08]: Venanzio Capretta, “General Recursion via Coinductive Types,” *Logical Methods in Computer Science* 1(2:1) (2005), [journal entry](https://lmcs.episciences.org/2265), [arXiv](https://arxiv.org/abs/cs/0505037), DOI: `10.2168/LMCS-1(2:1)2005`.
[^S09]: Andreas Abel, “foetus—Termination Checker for Simple Functional Programs,” [author-hosted report](https://andreasabel.github.io/foetus-report/foetus.pdf).
[^S10]: Aleš Bizjak et al., “Guarded Dependent Type Theory with Coinductive Types,” [arXiv:1601.01586](https://arxiv.org/abs/1601.01586).
[^S11]: Patrick Bahr et al., “The Clocks Are Ticking: No More Delays!,” LICS 2017, [author entry](https://bahr.io/pubs/entries/bahr17lics.html), [paper](https://bahr.io/pubs/files/bahr17lics-paper.pdf).
[^S12]: Robert Atkey and Conor McBride, “Productive Coprogramming with Guarded Recursion,” [author entry](https://bentnib.org/productive.html).
[^S13]: Thorsten Altenkirch, Nils Anders Danielsson, and Nicolai Kraus, “Partiality, Revisited,” [University of Birmingham research entry](https://research.birmingham.ac.uk/en/publications/6910f65c-896e-4b9d-b727-4c7af60700da).
[^S14]: Agda community, [Cubical library](https://github.com/agda/cubical).
[^S15]: HoTT community, [Coq-HoTT](https://github.com/HoTT/Coq-HoTT).
[^S16]: UniMath community, [UniMath](https://github.com/UniMath/UniMath).
[^S17]: UniMath community, [agda-unimath](https://github.com/UniMath/agda-unimath/).
[^S18]: HoTT community, [HoTT-Agda](https://github.com/HoTT/HoTT-Agda).
[^S19]: JetBrains Research, [Arend](https://github.com/JetBrains/Arend).
[^S20]: Carlo Angiuli, Anders Mörtberg, et al., [cubicaltt](https://github.com/mortberg/cubicaltt).
[^S21]: RedPRL, [redtt](https://github.com/RedPRL/redtt).
[^S22]: RedPRL, [cooltt](https://github.com/RedPRL/cooltt).
[^S23]: MetaRocq project, [MetaRocq](https://github.com/MetaRocq/metarocq).
[^S24]: Lean project, [Lean 2 HoTT/HIT documentation](https://github.com/leanprover/lean2/blob/master/hott/hit/hit.md).
[^S25]: S. C. Kleene, “On Notation for Ordinal Numbers,” *Journal of Symbolic Logic* 3(4) (1938), 150–155, DOI: [`10.2307/2267778`](https://doi.org/10.2307/2267778); Yiannis N. Moschovakis, “Kleene’s Amazing Second Recursion Theorem,” *Bulletin of Symbolic Logic* 16(2) (2010), 189–239, [publisher entry](https://www.cambridge.org/core/journals/bulletin-of-symbolic-logic/article/abs/kleenes-amazing-second-recursion-theorem/7ABD80C4DDD01A643217D8CD5E8268CD), DOI: `10.2178/bsl/1286889124`.
[^S26]: Emil L. Post, “Recursively Enumerable Sets of Positive Integers and Their Decision Problems,” *Bulletin of the American Mathematical Society* 50 (1944), 284–316, [AMS PDF](https://www.ams.org/bull/1944-50-05/S0002-9904-1944-08111-1/S0002-9904-1944-08111-1.pdf), DOI: `10.1090/S0002-9904-1944-08111-1`.
[^S27]: Chin Soon Lee, Neil D. Jones, and Amir M. Ben-Amram, “The Size-Change Principle for Program Termination,” *POPL 2001*, 81–92, [ACM DOI](https://doi.org/10.1145/360204.360210), DOI: `10.1145/360204.360210`. A secondary CiNii record exposes a conflicting prefix; the ACM/dblp/proceedings citation is used here.
[^S28]: Simon Huber, “Canonicity for Cubical Type Theory,” *Journal of Automated Reasoning* 63 (2019), 173–210, [paper copy](https://d-nb.info/1165123304/34), DOI: `10.1007/s10817-018-9469-1`; [arXiv:1607.04156](https://arxiv.org/abs/1607.04156).
[^S29]: Jonathan Sterling and Carlo Angiuli, “Normalization for Cubical Type Theory,” *LICS 2021*, 1–15, [LICS entry](https://lics.siglog.org/2021/SterlingAngiuli-NormalizationforCub.html), [arXiv:2101.11479](https://arxiv.org/abs/2101.11479).
[^S30]: Agda documentation, [Termination Checking](https://agda.readthedocs.io/en/v2.6.1/language/termination-checking.html) and [Reflection](https://agda.readthedocs.io/en/v2.5.2/language/reflection.html). Version-specific source behavior remains pinned by each evaluation rather than inferred from these documentation snapshots.
[^S31]: Russell O’Connor, “Essential Incompleteness of Arithmetic Verified by Coq,” TPHOLs 2005, [arXiv:cs/0505034](https://arxiv.org/abs/cs/0505034), [project page](https://r6.ca/Goedel/goedel1.html), DOI: `10.1007/11541868_16`.
[^S32]: Lawrence C. Paulson, “A Machine-Assisted Proof of Gödel’s Incompleteness Theorems for the Theory of Hereditarily Finite Sets,” *Review of Symbolic Logic* 7(3) (2014), 484–498, [Cambridge repository record](https://www.repository.cam.ac.uk/items/bda52431-26e0-4e86-8d63-409bcedd4617), DOI: `10.1017/S1755020314000112`; later archival preprint: [arXiv:2104.14260](https://arxiv.org/abs/2104.14260).
[^S33]: The Rocq Prover, [Typeclasses reference](https://rocq-prover.org/doc/master/refman/addendum/type-classes.html); the current experiment uses the pinned 9.0.1 implementation, while this living manual entry is retained as current documentation and version differences remain explicit.
[^S34]: Matthieu Sozeau and Nicolas Oury, “First-Class Type Classes,” TPHOLs 2008, LNCS 5170, 278–293, [author publication entry](https://sozeau.gitlabpages.inria.fr/www/research/coq/classes.en.html).
[^S35]: Andrej Bauer, Jason Gross, Peter LeFanu Lumsdaine, Michael Shulman, Matthieu Sozeau, and Bas Spitters, “The HoTT Library: A Formalization of Homotopy Type Theory in Coq,” CPP 2017, 164–172, [arXiv:1610.04591](https://arxiv.org/abs/1610.04591), DOI: [`10.1145/3018610.3018615`](https://doi.org/10.1145/3018610.3018615).
[^S36]: Egbert Rijke, Michael Shulman, and Bas Spitters, “Modalities in Homotopy Type Theory,” *Logical Methods in Computer Science* 16(1) (2020), [arXiv:1706.07526](https://arxiv.org/abs/1706.07526).
[^S37]: Dominik Kirst and Marc Hermes, “Synthetic Undecidability and Incompleteness of First-Order Axiom Systems in Coq,” *ITP 2021*, LIPIcs 193, 23:1–23:20, [publisher entry and CC-BY PDF](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITP.2021.23), DOI: `10.4230/LIPIcs.ITP.2021.23`.
[^S38]: Dominik Kirst and Benjamin Peters, “Gödel’s Theorem Without Tears — Essential Incompleteness in Synthetic Computability,” *CSL 2023*, [Dagstuhl entry and CC-BY PDF](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CSL.2023.30), DOI: `10.4230/LIPIcs.CSL.2023.30`; [accompanying Coq source](https://github.com/uds-psl/coq-synthetic-incompleteness).
[^S39]: Saarland University Programming Systems Lab et al., [Coq Library of Undecidability Proofs](https://github.com/uds-psl/coq-library-undecidability), official source repository and problem/reduction index.
[^S40]: Danil Annenkov, Paolo Capriotti, Nicolai Kraus, and Christian Sattler, “Two-Level Type Theory and Applications,” [arXiv:1705.03307](https://arxiv.org/abs/1705.03307).
[^S41]: Andrew W. Swan and Taichi Uemura, “On Church’s Thesis in Cubical Assemblies,” *Mathematical Structures in Computer Science* 31(10), 1185–1204, [arXiv:1905.03014](https://arxiv.org/abs/1905.03014), DOI: `10.1017/S0960129522000068`.
