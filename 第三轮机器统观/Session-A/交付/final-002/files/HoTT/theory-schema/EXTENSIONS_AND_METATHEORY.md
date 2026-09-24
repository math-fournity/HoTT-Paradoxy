# 扩展理论、语义模型与元理论边界

类型：HUMAN_EDITED；v0.2。此页是**一手来源支持的分界地图**，不是每个扩展的完整规则手册。
书式核心来源已锁定 commit；本页论文入口按明确题名/arXiv ID 登记，必要时另固定具体版本和源码。
不能从摘要中的存在性结果外推完整规则兼容性。

## 1. 理论配置不等于单个名称

一个可审查配置至少包含：

```text
语法与判断 + 宇宙方案 + 类型构造
+ identity / judgmental equality / reduction
+ 允许的归纳与 HIT 范围
+ 额外公理
+ 采用的操作/指称语义
+ 如使用实现，则其版本与选项
```

本页用 E01–E15 作为本项目定位标签，不声称是社区标准分类；它们也不是可以任意相加的插件。

## E01 · 书式公理化 HoTT

**来源**：[锁定 formal.tex](upstream/book-578b85cc/formal.tex)，A.2+A.3。

- 依赖类型论基础，内部 identity；显式的单价性/函数外延性公理常量；
- 指定 HIT 的点/路径构造及相应消去、计算；
- A.3 不为单价性常量自动加入 cubical 计算；
- A.1/A.2 的 judgmental η 差异不能忽略。

**不可外推**：基础系统正规化证明已经覆盖任意 HIT；书中历史开放问题仍代表全部后续理论。

## E02 · CCHM Cubical Type Theory

**来源**：Cohen–Coquand–Huber–Mörtberg，
[Cubical Type Theory: a constructive interpretation of the univalence axiom](https://arxiv.org/abs/1611.02108)。

采用 cubical 结构给路径与单价性计算解释；函数外延性和单价性在相应系统中可证明。论文还讨论
圆、命题截断等扩展。

**审查用途**：检查书式公理常量造成的计算问题，是否在此配置被不同规则处理。
**不可外推**：cubical interval 是物理时间；全部 cubical 变体规则相同；任意 clock/HIT 都已自动支持。
**阅读状态**：论文摘要/范围已核；完整具体规则、composition/Glue 与本项目程序成本比较未逐条展开。

## E03 · Guarded Dependent Type Theory

**来源**：Bizjak 等，
[Guarded Dependent Type Theory with Coinductive Types](https://arxiv.org/abs/1601.01586)。

这是特定的 extensional dependent type theory；later modality、clock quantifiers 和 delayed
substitutions 用于 guarded recursion、生产性和 coinductive types。

**审查用途**：时间性使用纪律可以进入类型形成与消去，不只是显式的数值 t。
**不可外推**：它就是书式 intensional HoTT；增加一个 t 下标等于拥有它的规则；任意递归因此合法。
**阅读状态**：一手范围已核；全部 clock 引入/消去侧条件尚待所选任务展开。

## E04 · Guarded Cubical Type Theory

**来源**：Birkedal 等，
[Guarded Cubical Type Theory: Path Equality for Guarded Recursion](https://arxiv.org/abs/1606.05223v2)。

论文将 guarded 递归与 cubical path equality 结合，处理 guarded recursive constructions 的外延性，
并给出模型及原型实例。

**审查用途**：这是 Guard-Erasure 候选可能采用的来源配置之一，不是已存在的目标翻译。
**不可外推**：从有 guarded 系统，直接推出标准 HoTT 错误；忽略论文年代，把其中实现状态当成当前全部实现。
**阅读状态**：题名、作者、版本、摘要范围已核；严格 source→target translation 未建立。

## E05 · Guarded Computational Type Theory

**来源**：Sterling–Harper，
[Guarded Computational Type Theory](https://arxiv.org/abs/1804.09098)。

已有项目时间研究将其作为 clocks 与计算解释的比较路线；不是 E03/E04 的自动别名。
**状态**：本轮作为既有一手参考路线保留，未重新读取全文；任何详细规则主张在使用前重读来源。
**边界**：不把该路线登记视为已经证明跨系统 clock erasure 或全部时间可观察量结论。

## E06 · Directed / Simplicial Type Theory

**来源**：Riehl–Shulman，
[A type theory for synthetic ∞-categories](https://arxiv.org/abs/1705.07442v5)。

论文公理化 directed interval，使用 shapes 与 extension types，定义 Segal/Rezk types 及相关
范畴结构，提供适合非可逆箭头的合成语言。

**审查用途**：区分 identity/groupoid 层与真正有方向的 morphism。
**不可外推**：普通 HoTT 函数均可逆；所有有向箭头就是物理因果；directed automatically means clocked。
**阅读状态**：摘要及版本变更范围已核；完整规则与操作成本未展开。

## E07 · Two-Level Type Theory

**来源**：Annenkov–Capriotti–Kraus–Sattler，
[Two-Level Type Theory and Applications](https://arxiv.org/abs/1705.03307)。

把内层 HoTT 与外层具有 UIP 的类型论分开，可用于表达某些内层的元理论问题。它提供的是明确的
分层接口，不是把两个相等概念偷偷合并。

**审查用途**：用户自指/元观察者支线；哪层能表达语法、图式、半单纯类型或证明资格。
**不可外推**：全同层自解释已经解决；外层 UIP 因而也能放到内层所有类型上。
**阅读状态**：一手摘要已核；不宣称完整反射/一致性内部化。

## E08 · Cost-aware：CATT 与 calf

**来源**：
[Cost-Aware Type Theory](https://arxiv.org/abs/2011.03660)，
[A cost-aware logical framework](https://arxiv.org/abs/2107.04663v2)。

CATT 引入原生成本；calf 区分 intension/extension 并把成本作为计算效应处理。它们直接支持
“输出行为”和“计算成本”是不同研究维度的分层。

**审查用途**：同函数异时的参照与修复结构。
**不可外推**：两者是同一个系统；它们所有规则都与 univalent HoTT 核心兼容；成本就是物理毫秒。
**阅读状态**：一手摘要/范围已核；此处没有复制整套系统或宣称本地实现。

## E09 · Linear / Quantitative / Effectful 路线

**状态：DISCOVERY_ROUTE，非已固定演算。**

资源使用次数、效应顺序与定量成本值得比较，但不能仅凭“线性/定量”几个词给出统一规则。
在某候选实际需要这些能力时，必须先选定论文、版本、上下文制度、消去/计算规则及与 identity 的关系。
当前没有把任意这类路线说成已证 HoTT 扩展。

## E10 · Cohesive / Modal 等其它扩展

**状态：DISCOVERY_ROUTE，非全领域目录。**

数学中的空间结构、模态与物理应用还存在其它研究路线。本版保留入口位置，不在未经一手规则
核查时声称完整覆盖。第 7 章 modalities 不等于这些扩展的全部规则。

## E11 · Cartesian Cubical Computational Type Theory

**来源**：[Angiuli–Hou–Harper](https://arxiv.org/abs/1712.01800)。该具体呈现包含累积的 univalent
Kan universes、缺少 Kan 结构的 pretypes 与 exact equality 等；不等同 CCHM 或普通 book HoTT。
**阅读状态**：题名/作者/摘要范围已核；精确操作语义、宇宙规则、canonicity 证明待实际候选使用时展开。

## E12 · CHM 的计算 HIT 扩展

**来源**：[Coquand–Huber–Mörtberg 2018 v2](https://arxiv.org/abs/1802.01170v2)。针对论文所列球、
torus、suspension、truncation、pushout，给出语法/语义与包括高阶构造子的 judgmental 计算。
**边界**：不推出任意 HIT/HIIT/归纳-递归规格全部合法。摘要与允许类已核，未重建全部规则。

## E13 · Cubical Agda 的具体实现配置

**来源**：[官方 Cubical 文档](https://agda.readthedocs.io/en/latest/language/cubical.html)，本轮显示
Agda 2.9.0。它实现 CCHM 的一个变体，分离 transp/hcomp 并提供 Glue、PathP、HIT 等。
**边界**：`--cubical`、erased、no-glue 等选项不能混同；版本、库 commit、module/symbol 与实际运行
必须分别记录。核心页的跨呈现表补了 Path-J 的计算差异；本项目未安装/升级或运行这个新后端。

## E14 · 内部模型与半单纯/有向扩展

具体三条路线见 [语义页 S07](SEMANTICS_AND_COHERENCE.md#s07--内部模型反射与无限相干性)：
Chen 的 2-coherent internal models、Displayed Type Theory、directed univalence in simplicial HoTT。
**状态**：一手摘要/版本已核；各自附加规则不放入 E01 核心。不能合称“所有自指问题已解决”。

## E15 · 单价性强度区分

[Cavallo–Höfer 2026 v2](https://arxiv.org/abs/2605.00812v2) 的 categorical univalence 较弱，
不一般蕴含函数外延性。标准 universe univalence 的 Book 定理继续成立。
**状态**：已核摘要与版本；分离模型细节未本地重证，不把标题当成标准 UA 失败。

## 2. 元理论事实必须带系统标签

| 编号 | 一手来源 | 可保留的范围 | 不支持什么 |
|---|---|---|---|
| M01 | [Kapulkin–Lumsdaine, Simplicial Model](https://arxiv.org/abs/1211.2851) | 为相应单价类型论构造 simplicial 模型；一致性是相对外部假设的结论 | 任意 HIT/任意扩展都已同时有模型；绝对无前提一致性 |
| M02 | [Lumsdaine–Shulman, Semantics of higher inductive types](https://arxiv.org/abs/1705.07088) | 给一类 HIT 的语义研究与构造 | 所有可能高阶递归规格都合法 |
| M03 | [Huber, Canonicity for Cubical Type Theory](https://arxiv.org/abs/1607.04156) | 对论文系统给出 canonicity；使用相应操作语义 | 任意公理化 HoTT、任意附加公理与全部 cubical 变体都获得同一结论 |
| M04 | [Coquand–Huber–Sattler, Canonicity and homotopy canonicity](https://arxiv.org/abs/1902.06572) | 后续具体 cubical 系统的结果定位 | 仅凭标题即可免去阅读精确假设 |

M01/M03 的摘要性结论本轮已核；M02 题名/来源已核，详细允许类待展开；M04 作为检索发现入口，
本轮未逐定理阅读。没有项目本地重证或独立专家验收。

## 3. 禁止混淆的六种层次

1. **规则确实存在**与**当前实现支持**；
2. **有模型**与**具有计算解释**；
3. **正规化**与**有限可行性/实际资源界限**；
4. **canonicity**与**每个证明搜索都能成功终止**；
5. **clock/later 的逻辑阶段**与**物理时间**；
6. **某系统可以加入某结构**与**原裸表示已经保留该结构**。

一篇论文证明“有这样的系统”，不能被转述成“所有称为 HoTT 的系统都是这样”。一篇书中的历史
开放问题，也不能被转述成“后来没有人解决任何相关问题”。

## 4. 实现对应与最小符合性检查

| 实现 | 可以承担的角色 | 不能默认声称 |
|---|---|---|
| Coq-HoTT | 书式公理化呈现的库与历史实践参照 | 标题含 HoTT 就等于内核原生计算 UA/HIT |
| 普通 HoTT-Agda | without-K 等具体配置下的形式化参照 | 与 Cubical Agda 的路径/计算相同 |
| Cubical Agda | 计算 UA/HIT 的候选执行后端 | 对每项研究都是“最佳”，或已在本项目配置并运行 |
| Lean 4 | 可作元理论、编码及一般数学论证的工具 | 原生 Eq 即 HoTT 高阶 identity；把对象移到 Type 就解决 |
| Lean 2 HoTT、RedPRL/redtt | 历史/研究型呈现线索 | 无版本检查即可用于当前稳定运行 |

Lean 的普通 Eq 对任意 Sort 的对象都取值于 Prop，而 Prop 具有证明无关性；因此直接用它替代
HoTT 高阶 identity 会改变理论。参见 [Eq](https://lean-lang.org/doc/reference/latest/Basic-Propositions/Propositional-Equality/)
和 [Prop](https://lean-lang.org/doc/reference/latest/The-Type-System/Propositions/)。编码层与元理论层要明确区分。

Coq 实现的一手研究入口：[The HoTT Library](https://arxiv.org/abs/1610.04591)。本轮没有核当前
Coq/RedPRL 安装、所有命令行选项或运行健康，故不把外部 AI 的“当前最好/已安装”判断照搬为事实。

实际选择一个后端后，按当前候选需要检三层：命题成立、judgmental 计算、边界/高阶相干性。
例如检查 J β、ua/transport、圆的点与 loop 计算分别是什么地位。三层测试是相称的核验工具，
不是先做完双后端和高级同伦全集才允许探索。未运行的测试始终标“未运行”。

## 5. 下一次展开某个变体时要填什么

在实际研究候选命中该路线时，补齐：精确版本、原始 judgment、上下文结构、宇宙、形成/引入/
消去/计算、相等制度、额外公理、语义、已证明元理论、实现证据、与 E01 的映射及不保留项。

目前没有为所有 E 条目填满这些字段，因此完整跨变体 Theory Schema 仍在建设；该开放性是
如实记录，不是可以用空壳条目冒充完成。
