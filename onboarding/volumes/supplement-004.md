

===== SOURCE HoTT/theory-schema/SEMANTICS_AND_COHERENCE.md | SHA256 bbfe8c452d0ce1cc44fd0f898a86b51f305ad0cfcbf44be04ce0d27d6cb68c98 | LINES 1-145/145 =====
# 语法、语义模型与相干性

类型：HUMAN_EDITED；Theory Schema v0.2，2026-09-09。
本页吸收外部 Schema 的有效建议，回到一手资料限定主张；不是可执行的模型实现或机器检查证书。
研究问题与最终归因分开：这些结构提供考察接口，不自动证明时间悖论。

## S01 · 四种对象分别是什么

| 对象 | 例子 | 判断它的依据 |
|---|---|---|
| 理论概念 | identity、equivalence、univalence | 定义、性质及采用的假设 |
| 形式呈现 | book A.2/A.3、CCHM、Cartesian cubical | 具体语法、判断、形成/消去/计算规则 |
| 语义模型 | simplicial/cubical 模型、适当模型范畴 | 解释构造与验证定理 |
| 实现产物 | proof assistant 内核、库中的某个定义 | 精确版本、选项、源码和实际验证 |

同名不代表同定义；同一命题可证明不代表同样计算；有模型不代表存在相应高效求值器。

## S02 · 从语法进入模型

常用组织方式把上下文解释为对象、替换解释为态射、依赖类型解释为上下文上的族/纤维结构、
项解释为截面。判断相等需要与所选严格解释相适配，不能随意只解释成“同伦相等”就结束。

一个模型声明至少记录：

```text
解释哪个理论配置；
解释 Γ、A、a、替换和判断相等的方式；
支持哪些类型构造/宇宙/额外公理；
重索引时保持哪些等式；
外部集合论或范畴论假设；
验证定理的位置与不覆盖的扩展。
```

这是一份阅读与证据合同，不是新数据库格式。

## S03 · CwF 的基本组织

Category with families（CwF）可用下列基本数据理解：

- 一个上下文范畴及终对象；
- 每个 Γ 的类型集合 Ty(Γ)，每个类型 A 的项集合 Tm(Γ,A)；
- 沿替换 σ:Δ→Γ 的重索引 A[σ]、a[σ]；
- 与恒等、复合相容的替换等式；
- 上下文扩张 Γ.A、投影 p，以及泛型变量 q；
- 相应配对的普遍性质。

这是常见的严格/集合值 CwF 图景。高阶或内部 CwF 需要改变相等/相干性层级，不能默认为同一份
数据。Comprehension categories 用纤维化及 display maps 组织类似关系；contextual categories
有其上下文长度/扩张结构。它们相互关联，但不是不附条件的同义词。

来源：[Lumsdaine–Warren](https://arxiv.org/abs/1411.1736v2)；
[Chen 的高阶内部模型](https://arxiv.org/abs/2503.05790v2)。本页基本结构是解释性提要，不重证转换定理。

## S04 · 为什么需要语义相干性

语法要求反复替换遵守明确等式；某些几何/范畴构造却只在同构或等价意义下稳定。
如果没有说明怎样协调，不能直接宣称模型已经解释了全部严格语法。

Local-universes 构造从具有所需弱稳定逻辑结构、并满足相应基范畴条件的 comprehension category，
构造等价的 split 结构，使选择的逻辑结构在重索引下严格稳定。它解决特定的相干性问题，
不意味着所有模型、所有新构造、所有 HIT 都无需再审。[原论文摘要及假设](https://arxiv.org/abs/1411.1736v2)

“strictification”不是删除时间的同义词。若要研究它是否遗忘了某个目标观察量，必须另外定义
该观察量及实际解释；不能单凭“严格化”名称推断因果。

## S05 · 三种相干性

| 类别 | 内容 | 不可混淆 |
|---|---|---|
| 内部高阶相干性 | 路径结合、单位、逆及其高阶见证 | 不是“所有证明相同” |
| 语义替换相干性 | 类型/项构造随替换与重索引的相容性 | 不是一次程序执行的时间顺序 |
| Cubical 边界相干性 | composition/filler 与各面、端点、维度替换相容 | 几何维度不自动等于物理时间 |

迭代 identity 带有弱高阶群胚结构的论证，应分别回到
[Lumsdaine](https://arxiv.org/abs/0812.0409) 与
[van den Berg–Garner](https://arxiv.org/abs/0812.0298)；
模型替换回到 S04；cubical 计算回到具体 composition 规则。
后两份高阶群胚论文在本版作为一手来源定位，未在本轮逐证明阅读。

## S06 · 模型图谱与验证边界

| 模型/构造 | 验证或组织什么 | 不能推成什么 |
|---|---|---|
| 适当 Quillen 模型范畴 | 用路径对象/纤维化解释 identity 的同伦性质 | 任意模型范畴自动支持全部单价宇宙/HIT |
| Simplicial 模型 | 特定单价类型论及相对一致性 | 可执行的正规化算法、任意额外公理的模型 |
| Cubical 模型 | 在具体立方范畴上的类型/路径/填充解释 | 不同 cube categories 完全相同 |
| Local universes | 特定弱稳定结构的严格化 | 一个全新的物理或同伦对象模型 |
| Grothendieck (∞,1)-topos 的呈现 | 可选择解释带严格单价宇宙 HoTT 的模型范畴呈现 | 所有 elementary ∞-topos 语言对应已终结，或任意扩展同时获验证 |
| Cell-monad HIT 语义 | 相应允许类的高阶归纳构造 | 任意高阶归纳/递归规格都合法 |

一手入口：
[Awodey–Warren](https://arxiv.org/abs/0709.0248)；
[Kapulkin–Lumsdaine](https://arxiv.org/abs/1211.2851)；
[BCH](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.TYPES.2013.107)；
[CCHM](https://arxiv.org/abs/1611.02108)；
[Lumsdaine–Shulman](https://arxiv.org/abs/1705.07088)；
[Shulman](https://arxiv.org/abs/1904.07004v2)。

Shulman 结论的准确重点是“Grothendieck (∞,1)-topos 的某个 Quillen 模型范畴呈现解释相应理论”，
不能压成对象语言中的 Type = ∞-groupoid。语义证书需要确切理论配置；本文没有声称复现模型。

## S07 · 内部模型、反射与无限相干性

三条新增路线与用户过去的自指/生成/反射问题相关：

- [Chen 2025 v2](https://arxiv.org/abs/2503.05790v2)：split 2-coherent wild CwF，
  讨论语法与标准宇宙模型，以及一种 2-coherent reflection 的内部化。不是所有层级完整自解释。
- [Kolomatskaia–Shulman 2024 v2](https://arxiv.org/abs/2311.18781v2)：Displayed Type Theory
  的多模态结构与 display/dependency 原语，用来构造半单纯类型。不是 bare HoTT 无扩展的结论。
- [Gratzer–Weinberger–Buchholtz 2026 v2](https://arxiv.org/abs/2407.09146v2)：通过模态和新增
  推理原则构造相应 universe 的 directed univalence。不是普通 universe univalence 的改名。

本版核对的是作者、版本、摘要中的对象与结论范围，未逐证明重建。它们可以提供探索线索，也
可以限制过强的“不可能自指/不可能有向”断言；不能预先当作支持或否定用户哲学的总证据。

## S08 · 关系应怎样记录

| 关系 | 精确含义 | 证据要求 |
|---|---|---|
| 定义使用 | 选定定义的表达式引用某概念 | 具体定义与表示 |
| 证明使用 | 这份证明使用某假设 | 证明体/推导 |
| 逻辑推出 | 在明确背景下得到结论 | 定理及完整假设 |
| 必要性/独立性 | 去掉假设后不能一般推出 | 分离模型或相应不可能性证明 |
| 等价表示 | 两个类型/规格在条件下等价 | 映射与逆/纤维等价证据 |
| 语义验证 | 某模型满足某组规则 | 解释及 soundness |
| 计算实现 | 某呈现提供特定归约行为 | 精确规则/内核行为 |
| 严格化 | 弱结构可替换为适当严格结构 | 定理及输入条件 |
| 翻译/保守性 | 配置间映射及保留的结论 | 不能只靠共同术语或同名库 |
| 历史先后 | 文献或实现的时间谱系 | 没有逻辑推出效力 |

**证明使用不等于假设必要。**定义依赖也相对于选定表示：用 half-adjoint 定义 isEquiv 与用
contractible fibers 定义它，直接依赖图未必相同。qinv 数据不自动与 isEquiv 类型等价。

## S09 · 使用时的最小问题

一个候选涉及模型、相干性或跨系统操作时，问：

1. 原始理论配置是什么，目标配置是什么？
2. 哪个关系是定义、推导、模型验证或计算实现？
3. 需要保留什么，已经证明保留什么？
4. 未知差异是否影响“悖论确实存在”，还是仅影响最终归因？
5. 这个新接口是否有助于实际候选，还是只是可选的资料扩充？

本页不引入 JSON-LD 平台、双证明助手工程或全模型形式化作为探索前置。


===== END SOURCE CHUNK | EOF=true =====


===== SOURCE HoTT/theory-schema/SOURCES_AND_COVERAGE.md | SHA256 44221bfaa5f199c34627f4ec5bcd9764a8ea48523be2be22f9876765eae35701 | LINES 1-313/313 =====
# 一手来源、覆盖范围与验证记录

类型：HUMAN_EDITED；v0.2；2026-09-09。维护者为本项目研究文档维护者。
这是来源登记与覆盖证据，不是数学定理数据库；表格不替代原文。本文支撑 HOTT-009 的文档化状态，
不提高 HOTT-005 的悖论证明状态。

## 1. 来源固定与许可

上游：The Univalent Foundations Program，*Homotopy Type Theory: Univalent Foundations of Mathematics*。

- 官方入口：[HoTT Book](https://homotopytypetheory.org/book/)；
- 官方代码库：[HoTT/book](https://github.com/HoTT/book)；
- 本轮 `git ls-remote` 返回的 HEAD/master：`578b85cc8d586b1677ec4335148adeb443057d24`；
- 下载 URL 使用此完整 commit，不使用浮动 master；
- 21 个文本文件，共 1,634,747 bytes；
- 全部来源原字节保留，无本地内容修改；不是全部 Git 历史，也不是完整可编译书籍工程；
- 上游许可：[CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)，原始声明在
  [上游 README 快照](upstream/book-578b85cc/README.md)。
- 本 Schema 中对 HoTT Book 的中文转述、规则归纳与目录改编注明作者来源，并遵循该许可；
  许可不表示上游审阅或认可我们的研究结论。没有执行对外发布。

我们保存完整章节原文，既便于 future Session 回源，也防止 Schema 的选择性组织替代原始理论。

## 2. 文件原字节清单

| 文件 | bytes | SHA-256 | 位置 |
|---|---:|---|---|
| `README.md` | 5251 | `79d6220e154e2774e6682eefb923bd8a26d7f7e6ded3dd49b0d3a87f44c5e81b` | [本地](upstream/book-578b85cc/README.md) / [上游](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/README.md) |
| `basics.tex` | 155111 | `516b469d7356e9d20df5539e726a0468760f9fa7b7f440b9c054981e803d7533` | [本地](upstream/book-578b85cc/basics.tex) / [上游](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/basics.tex) |
| `categories.tex` | 108084 | `141332f0b27d5ab055419e02bada9664561758d129ebe4d52e43bb8e290b275f` | [本地](upstream/book-578b85cc/categories.tex) / [上游](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/categories.tex) |
| `equivalences.tex` | 56163 | `037dce18db74526a3f7148c353bb5459da1c4b65e046780a208de39633df1722` | [本地](upstream/book-578b85cc/equivalences.tex) / [上游](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/equivalences.tex) |
| `formal.tex` | 51643 | `e621484e2e457e70536a92367cca452f34df8ecfc9a17a3bdf0e4ee67e5f0cec` | [本地](upstream/book-578b85cc/formal.tex) / [上游](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/formal.tex) |
| `front.tex` | 5459 | `784de150ef5e64967618c712fe81f40ac41f6fa0b68f5a02b76ce23a5306b4c4` | [本地](upstream/book-578b85cc/front.tex) / [上游](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/front.tex) |
| `hits.tex` | 133916 | `d43dac381da7f978fb1d2ff6c2c2d3cca7f9b0dab90c96cd20815c13e7ab8454` | [本地](upstream/book-578b85cc/hits.tex) / [上游](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/hits.tex) |
| `hlevels.tex` | 112113 | `cfa75d289487f91affc4f5a9907857135c8a307b59dbc1cb9e3e9f41399618cc` | [本地](upstream/book-578b85cc/hlevels.tex) / [上游](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/hlevels.tex) |
| `homotopy.tex` | 156051 | `c3b15506e3237564e9f76376668bac1e2d57e80db680f924d11edd10e0af4a32` | [本地](upstream/book-578b85cc/homotopy.tex) / [上游](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/homotopy.tex) |
| `induction.tex` | 94673 | `475792764d6f41ea2269a4f7ced701bb54220bb404a29af0160f3141eb5316c1` | [本地](upstream/book-578b85cc/induction.tex) / [上游](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/induction.tex) |
| `introduction.tex` | 55229 | `a1319432c822d71ee54cd8edd644d3bce1c8d816bd9f2ff6111b8d3db8e28ac4` | [本地](upstream/book-578b85cc/introduction.tex) / [上游](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/introduction.tex) |
| `logic.tex` | 80409 | `76ac2e06ffa133ede0612584fef4b9c81d698d4e0b7a4ec683131448edfed2f2` | [本地](upstream/book-578b85cc/logic.tex) / [上游](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/logic.tex) |
| `macros.tex` | 32134 | `822b658eb6e2f74e9c8557c607de08b151ff3b8174fc3dc8fdba3a9a21d23fe3` | [本地](upstream/book-578b85cc/macros.tex) / [上游](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/macros.tex) |
| `main.labelnumbers.first-edition` | 78855 | `16ff1b8c75b4864467b41c18be1db9d54005012f7d7b77177ba8eda4f3b0b476` | [本地](upstream/book-578b85cc/main.labelnumbers.first-edition) / [上游](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/main.labelnumbers.first-edition) |
| `main.tex` | 10082 | `d7040138bd803cefb4c714b5b83dcc1599e589b19f0c188b479c902a2f638dc2` | [本地](upstream/book-578b85cc/main.tex) / [上游](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/main.tex) |
| `preface.tex` | 3912 | `6dd80d576634b081b32f7c89e302eae9222170d997d4d8bbf9701ae73f05890c` | [本地](upstream/book-578b85cc/preface.tex) / [上游](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/preface.tex) |
| `preliminaries.tex` | 138454 | `c459282fc0b789cd6f11a4a7bf401fcb1074c12c417b63fccdeee25927ed99d9` | [本地](upstream/book-578b85cc/preliminaries.tex) / [上游](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/preliminaries.tex) |
| `reals.tex` | 190590 | `f5e4803e17abdb2fbb75a6ebd30022a9587a914711f3ca77dc8fcce50fda39e7` | [本地](upstream/book-578b85cc/reals.tex) / [上游](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/reals.tex) |
| `references.bib` | 42754 | `40068943869f35b6627894f3183f3e0be071abf7b54ad4e88b7b4d5904f5f9a0` | [本地](upstream/book-578b85cc/references.bib) / [上游](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/references.bib) |
| `setmath.tex` | 103732 | `c9684dffba31892b12839e60eac769706faa2301b7fba7b930f5acf4b097563e` | [本地](upstream/book-578b85cc/setmath.tex) / [上游](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/setmath.tex) |
| `symbols.tex` | 20132 | `17d0ca29a5a42f2d658afb432b97b019e09e6f324d83cfff725c7936db3da70c` | [本地](upstream/book-578b85cc/symbols.tex) / [上游](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/symbols.tex) |

首次下载所有命令 exit 0。SHA 是本地下载物的身份指纹，不单凭它宣称与远端再次独立比对通过；
二次核对的实际结果见 §6。

## 3. 主要呈现的覆盖

| 上游范围 | Schema 条目 | 阅读/整理程度 |
|---|---|---|
| Formal Preliminaries | C01–C03 | 全文已读，判断/上下文/绑定归纳 |
| A.1 First presentation | C01/C04–C11/C17/C18 | 全文已读，W/η/convertibility 差异明确 |
| A.2 Contexts | C02 | 全文已读 |
| A.2 Structural rules | C03 | 全文已读；替换/弱化与省略合同性规则有说明 |
| A.2 Type universes | C04 | 全文已读 |
| A.2 Dependent function types | C05 | 全文已读，formation/introduction/elimination/β/η |
| A.2 Dependent pair types | C06 | 全文已读；无 judgmental Σ-η |
| A.2 Coproduct types | C07 | 全文已读 |
| A.2 Empty type | C08 | 全文已读；无 introduction/computation |
| A.2 Unit type | C08 | 全文已读；无 judgmental η |
| A.2 Natural number type | C09 | 全文已读 |
| A.2 Identity types | C11/C12 | 全文已读 |
| A.2 Definitions | C17 | 全文已读 |
| A.3 Function extensionality and univalence | C14/C15 | 全文已读，公理常量与命题性计算分开 |
| A.3 Circle | C16 | 全文已读，点/路径计算分开 |
| A.4 Basic metatheory / Notes | C18 / 扩展页 | 全文已读；基础与扩展的适用域不混同 |

此处覆盖的是规则家族，不是书中所有定理已经重新证明，也不证明书中省略的全部一般 HIT 规则
已经被填满。

## 4. 全书 11 章、105 个编号 section 的来源索引

以下清单由锁定源码每章的 `\\section{` 顺序核出。标题保留 TeX 原形，以避免翻译导致源定位
不一致；中文主题解读见 [派生结构页](DERIVED_STRUCTURES.md)。链接为固定 commit + 精确起始行，
全节正文在对应本地快照中。

**覆盖计数口径**：编号 section，不含 subsection、Notes、练习、引言未编号段落与附录。附录另见 §3。
105/105 表示来源入口没有漏掉该口径内的节，不表示已全文阅读 105 节或逐证明验收。

| 书中节号 | 原始标题 | 上游精确位置 |
|---|---|---|
| 1.1 | `Type theory versus set theory` | [preliminaries.tex:4](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/preliminaries.tex#L4) |
| 1.2 | `Function types` | [preliminaries.tex:175](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/preliminaries.tex#L175) |
| 1.3 | `Universes and families` | [preliminaries.tex:358](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/preliminaries.tex#L358) |
| 1.4 | `Dependent function types (\texorpdfstring{$\Pi$}{Π}-types)` | [preliminaries.tex:437](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/preliminaries.tex#L437) |
| 1.5 | `Product types` | [preliminaries.tex:530](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/preliminaries.tex#L530) |
| 1.6 | `Dependent pair types (\texorpdfstring{$\Sigma$}{Σ}-types)` | [preliminaries.tex:728](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/preliminaries.tex#L728) |
| 1.7 | `Coproduct types` | [preliminaries.tex:870](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/preliminaries.tex#L870) |
| 1.8 | `The type of booleans` | [preliminaries.tex:959](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/preliminaries.tex#L959) |
| 1.9 | `The natural numbers` | [preliminaries.tex:1062](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/preliminaries.tex#L1062) |
| 1.10 | `Pattern matching and recursion` | [preliminaries.tex:1205](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/preliminaries.tex#L1205) |
| 1.11 | `Propositions as types` | [preliminaries.tex:1266](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/preliminaries.tex#L1266) |
| 1.12 | `Identity types` | [preliminaries.tex:1547](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/preliminaries.tex#L1547) |
| 2.1 | `Types are higher groupoids` | [basics.tex:210](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/basics.tex#L210) |
| 2.2 | `Functions are functors` | [basics.tex:683](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/basics.tex#L683) |
| 2.3 | `Type families are fibrations` | [basics.tex:748](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/basics.tex#L748) |
| 2.4 | `Homotopies and equivalences` | [basics.tex:969](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/basics.tex#L969) |
| 2.5 | `The higher groupoid structure of type formers` | [basics.tex:1191](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/basics.tex#L1191) |
| 2.6 | `Cartesian product types` | [basics.tex:1238](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/basics.tex#L1238) |
| 2.7 | `\texorpdfstring{$\Sigma$}{Σ}-types` | [basics.tex:1393](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/basics.tex#L1393) |
| 2.8 | `The unit type` | [basics.tex:1534](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/basics.tex#L1534) |
| 2.9 | `\texorpdfstring{$\Pi$}{Π}-types and the function extensionality axiom` | [basics.tex:1568](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/basics.tex#L1568) |
| 2.10 | `Universes and the univalence axiom` | [basics.tex:1706](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/basics.tex#L1706) |
| 2.11 | `Identity type` | [basics.tex:1809](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/basics.tex#L1809) |
| 2.12 | `Coproducts` | [basics.tex:1931](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/basics.tex#L1931) |
| 2.13 | `Natural numbers` | [basics.tex:2070](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/basics.tex#L2070) |
| 2.14 | `Example: equality of structures` | [basics.tex:2165](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/basics.tex#L2165) |
| 2.15 | `Universal properties` | [basics.tex:2360](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/basics.tex#L2360) |
| 3.1 | `Sets and \texorpdfstring{$n$}{n}-types` | [logic.tex:11](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/logic.tex#L11) |
| 3.2 | `Propositions as types?` | [logic.tex:159](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/logic.tex#L159) |
| 3.3 | `Mere propositions` | [logic.tex:255](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/logic.tex#L255) |
| 3.4 | `Classical vs.\ intuitionistic logic` | [logic.tex:353](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/logic.tex#L353) |
| 3.5 | `Subsets and propositional resizing` | [logic.tex:451](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/logic.tex#L451) |
| 3.6 | `The logic of mere propositions` | [logic.tex:558](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/logic.tex#L558) |
| 3.7 | `Propositional truncation` | [logic.tex:598](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/logic.tex#L598) |
| 3.8 | `The axiom of choice` | [logic.tex:701](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/logic.tex#L701) |
| 3.9 | `The principle of unique choice` | [logic.tex:801](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/logic.tex#L801) |
| 3.10 | `When are propositions truncated?` | [logic.tex:852](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/logic.tex#L852) |
| 3.11 | `Contractibility` | [logic.tex:938](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/logic.tex#L938) |
| 4.1 | `Quasi-inverses` | [equivalences.tex:34](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/equivalences.tex#L34) |
| 4.2 | `Half adjoint equivalences` | [equivalences.tex:148](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/equivalences.tex#L148) |
| 4.3 | `Bi-invertible maps` | [equivalences.tex:376](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/equivalences.tex#L376) |
| 4.4 | `Contractible fibers` | [equivalences.tex:417](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/equivalences.tex#L417) |
| 4.5 | `On the definition of equivalences` | [equivalences.tex:493](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/equivalences.tex#L493) |
| 4.6 | `Surjections and embeddings` | [equivalences.tex:513](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/equivalences.tex#L513) |
| 4.7 | `Closure properties of equivalences` | [equivalences.tex:602](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/equivalences.tex#L602) |
| 4.8 | `The object classifier` | [equivalences.tex:785](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/equivalences.tex#L785) |
| 4.9 | `Univalence implies function extensionality` | [equivalences.tex:897](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/equivalences.tex#L897) |
| 5.1 | `Introduction to inductive types` | [induction.tex:9](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/induction.tex#L9) |
| 5.2 | `Uniqueness of inductive types` | [induction.tex:147](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/induction.tex#L147) |
| 5.3 | `\texorpdfstring{$\w$}{W}-types` | [induction.tex:253](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/induction.tex#L253) |
| 5.4 | `Inductive types are initial algebras` | [induction.tex:381](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/induction.tex#L381) |
| 5.5 | `Homotopy-inductive types` | [induction.tex:566](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/induction.tex#L566) |
| 5.6 | `The general syntax of inductive definitions` | [induction.tex:752](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/induction.tex#L752) |
| 5.7 | `Generalizations of inductive types` | [induction.tex:949](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/induction.tex#L949) |
| 5.8 | `Identity types and identity systems` | [induction.tex:1071](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/induction.tex#L1071) |
| 6.1 | `Introduction` | [hits.tex:8](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/hits.tex#L8) |
| 6.2 | `Induction principles and dependent paths` | [hits.tex:105](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/hits.tex#L105) |
| 6.3 | `The interval` | [hits.tex:353](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/hits.tex#L353) |
| 6.4 | `Circles and spheres` | [hits.tex:429](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/hits.tex#L429) |
| 6.5 | `Suspensions` | [hits.tex:551](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/hits.tex#L551) |
| 6.6 | `Cell complexes` | [hits.tex:718](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/hits.tex#L718) |
| 6.7 | `Hubs and spokes` | [hits.tex:771](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/hits.tex#L771) |
| 6.8 | `Pushouts` | [hits.tex:883](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/hits.tex#L883) |
| 6.9 | `Truncations` | [hits.tex:1048](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/hits.tex#L1048) |
| 6.10 | `Quotients` | [hits.tex:1183](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/hits.tex#L1183) |
| 6.11 | `Algebra` | [hits.tex:1466](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/hits.tex#L1466) |
| 6.12 | `The flattening lemma` | [hits.tex:1755](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/hits.tex#L1755) |
| 6.13 | `The general syntax of higher inductive definitions` | [hits.tex:2041](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/hits.tex#L2041) |
| 7.1 | `Definition of \texorpdfstring{$n$}{n}-types` | [hlevels.tex:27](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/hlevels.tex#L27) |
| 7.2 | `Uniqueness of identity proofs and Hedberg's theorem` | [hlevels.tex:236](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/hlevels.tex#L236) |
| 7.3 | `Truncations` | [hlevels.tex:447](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/hlevels.tex#L447) |
| 7.4 | `Colimits of \texorpdfstring{$n$}{n}-types` | [hlevels.tex:776](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/hlevels.tex#L776) |
| 7.5 | `Connectedness` | [hlevels.tex:1065](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/hlevels.tex#L1065) |
| 7.6 | `Orthogonal factorization` | [hlevels.tex:1378](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/hlevels.tex#L1378) |
| 7.7 | `Modalities` | [hlevels.tex:1665](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/hlevels.tex#L1665) |
| 8.1 | `\texorpdfstring{$\pi_1(S^1)$}{π₁(S¹)}` | [homotopy.tex:309](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/homotopy.tex#L309) |
| 8.2 | `Connectedness of suspensions` | [homotopy.tex:795](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/homotopy.tex#L795) |
| 8.3 | `\texorpdfstring{$\pi_{k \le n}$}{π\_(k≤n)} of an \texorpdfstring{$n$}{n}-connected space and \texorpdfstring{$\pi_{k < n}(\Sn ^n)$}{π\_(k<n)(Sⁿ)}` | [homotopy.tex:886](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/homotopy.tex#L886) |
| 8.4 | `Fiber sequences and the long exact sequence` | [homotopy.tex:938](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/homotopy.tex#L938) |
| 8.5 | `The Hopf fibration` | [homotopy.tex:1175](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/homotopy.tex#L1175) |
| 8.6 | `The Freudenthal suspension theorem` | [homotopy.tex:1558](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/homotopy.tex#L1558) |
| 8.7 | `The van Kampen theorem` | [homotopy.tex:1879](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/homotopy.tex#L1879) |
| 8.8 | `Whitehead's theorem and Whitehead's principle` | [homotopy.tex:2340](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/homotopy.tex#L2340) |
| 8.9 | `A general statement of the encode-decode method` | [homotopy.tex:2542](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/homotopy.tex#L2542) |
| 8.10 | `Additional Results` | [homotopy.tex:2647](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/homotopy.tex#L2647) |
| 9.1 | `Categories and precategories` | [categories.tex:46](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/categories.tex#L46) |
| 9.2 | `Functors and transformations` | [categories.tex:281](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/categories.tex#L281) |
| 9.3 | `Adjunctions` | [categories.tex:478](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/categories.tex#L478) |
| 9.4 | `Equivalences` | [categories.tex:539](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/categories.tex#L539) |
| 9.5 | `The Yoneda lemma` | [categories.tex:872](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/categories.tex#L872) |
| 9.6 | `Strict categories` | [categories.tex:1073](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/categories.tex#L1073) |
| 9.7 | `\texorpdfstring{$\dagger$}{†}-categories` | [categories.tex:1128](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/categories.tex#L1128) |
| 9.8 | `The structure identity principle` | [categories.tex:1205](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/categories.tex#L1205) |
| 9.9 | `The Rezk completion` | [categories.tex:1366](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/categories.tex#L1366) |
| 10.1 | `The category of sets` | [setmath.tex:36](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/setmath.tex#L36) |
| 10.2 | `Cardinal numbers` | [setmath.tex:683](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/setmath.tex#L683) |
| 10.3 | `Ordinal numbers` | [setmath.tex:887](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/setmath.tex#L887) |
| 10.4 | `Classical well-orderings` | [setmath.tex:1278](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/setmath.tex#L1278) |
| 10.5 | `The cumulative hierarchy` | [setmath.tex:1445](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/setmath.tex#L1445) |
| 11.1 | `The field of rational numbers` | [reals.tex:37](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/reals.tex#L37) |
| 11.2 | `Dedekind reals` | [reals.tex:85](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/reals.tex#L85) |
| 11.3 | `Cauchy reals` | [reals.tex:668](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/reals.tex#L668) |
| 11.4 | `Comparison of Cauchy and Dedekind reals` | [reals.tex:1778](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/reals.tex#L1778) |
| 11.5 | `Compactness of the interval` | [reals.tex:1876](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/reals.tex#L1876) |
| 11.6 | `The surreal numbers` | [reals.tex:2466](https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/reals.tex#L2466) |

## 5. 实际阅读深度

本轮正文已全文阅读：formal.tex；main.tex；上游 README。理论主干定点展开：

- basics.tex §2.9–2.10：函数外延性、单价性与命题计算；
- equivalences.tex §4.4–4.5：contractible fibers、ishae 与最终等价定义；
- logic.tex §3.4–3.5、§3.7–3.8：LEM、resizing、截断与 AC；
- induction.tex §5.6：一般归纳定义的正性、反例及 resizing 条件；
- hits.tex §6.13 及其 Notes：构造顺序、端点自然性与通用语法边界；
- categories.tex §9.1 定义段：precategory 与普通 hom-set；
- hlevels.tex §7.1 定义段：同伦层级递归；
- reals.tex §11.2 定义/宇宙段：Dedekind cut 与 Ω 选择。

其余主章节：已保存全文并检查全部 section 入口，但未声称全部证明读完。
macros、labelnumbers、references 等是定位/释义辅助来源，不宣称全部逐行语义审读。

扩展来源的具体阅读程度在 EXTENSIONS_AND_METATHEORY 中逐项标注；论文目录/摘要级证据不能替代
需要使用的正式规则。

## 6. 验证记录与可复现范围

本轮执行的来源获取与检查：

```sh
rtk proxy git ls-remote https://github.com/HoTT/book.git HEAD refs/heads/master
rtk proxy shasum -a 256 HoTT/theory-schema/upstream/book-578b85cc/formal.tex
rtk proxy rg -n '^\\(section|subsection)' HoTT/theory-schema/upstream/book-578b85cc/formal.tex
rtk proxy git diff --check
```

直接 HTTP 下载地址的模式：
`https://raw.githubusercontent.com/HoTT/book/578b85cc8d586b1677ec4335148adeb443057d24/<file>`。
GitHub commits API 曾返回 HTTP 403，随后用公开 Git ls-remote 固定 commit。
二次远端字节核对第一次遇到 TLS 连接错误，未视为通过；重试结果在收工核验段登记。

机械验收包括：21 文件哈希、105 节号/文件/起始行与源码一致、C01–C18/D01–D12/E01–E10/
T01–T06 的定位、所有相对本地文件链接存在、Markdown fence 配对与 whitespace，以及旧原文/
研究规范/闭包不被修改。

这些检查不能证明中文转述无误或所有依赖齐全；核心语义由逐规则阅读检查，独立专家/机器化
规则复核仍开放。

### 6.1 本轮收工核验

| 核验 | 实际结果 | 证明边界 |
|---|---|---|
| 固定 commit 的首次来源下载 | 21/21 exit 0 | 原文已取得 |
| 二次从同一 commit 下载到内存后比 SHA | 重试后 21/21 相同，failed=[] | 第一次 TLS 失败保留为失败记录；未覆盖本地来源 |
| 本地来源 SHA 与 §2 清单 | 21/21 相同 | 来源完整性，不证明数学 |
| 编号节覆盖 | 105/105 节号、文件、起始行对应 | 仅目录覆盖，不是逐证明审查 |
| 核心/派生/扩展定位 | C01–C18、D01–D12、E01–E10 连续 | 入口存在，E09/E10 仍只是发现路线 |
| 相对本地链接与 fence | 12 份相关文档检查无失败 | 文档可达/结构，不是语义终审 |
| 原文/研究规范/矩阵/ZCore/第五闭包/三问文档 | 6 个保护哈希未变化 | 本轮未篡改这些既有资产 |
| 既有 Git index | 仍为 16 项 R100 | 未新增 stage/commit/push |
| whitespace | git diff --check 通过 | 另对未跟踪新文档做直接结构检查 |

核验环境：`/Volumes/D/ALL-Markdown`，Git HEAD `dc1e369a6a7493dd6671016c295e8f04f2231aa3`，
dirty/untracked。以 Node 只读检查文档/哈希/节号，curl 读取固定原始 URL。没有运行全书构建、
形式证明编译或独立专家审查。

## 7. 已知缺口与后续完成标准

| ID | 缺口 | 它阻塞什么 | 何时补 |
|---|---|---|---|
| G01 | 全书逐定理前提/依赖尚未逐项审计 | “所有书中结论都已核完” | 候选实际使用相应定理时先核；系统审计另按范围推进 |
| G02 | 一般 HIT/高阶归纳-递归无本项目完整规则实现 | “任意 HIT 合法/全部已形式化” | 选定允许语法与具体文献/实现后 |
| G03 | E02–E08 未全部展开原始规则 | 完整跨变体比较/no-go | 候选选择该系统时展开 |
| G04 | E09/E10 仅发现路线 | 全领域穷尽 | 用户研究范围或实际依赖要求时 |
| G05 | 无独立专家逐规则审阅 | 社区权威认证、无误终审 | 独立审查后 |
| G06 | 无本轮 proof assistant/全书编译 | 机器语义验证/运行能力 | 有具体源码规格与工具链时 |
| G07 | 全部业务资产尚未提交 | 跨 clone 可恢复 | 用户明确决定 Git 版本化时 |
| G08 | 现实桥梁与候选仍待证明 | “已找到最终 HoTT 悖论” | 回到 Z owner 的具体候选验收 |

“权威来源已固定”不等于“全部研究已完成”。把 G01–G08 明确写出来，是这份 Schema 可靠性的一部分。

## 8. 责任与变更边界

- 理论事实：固定上游来源 → CORE_RULES/DERIVED_STRUCTURES 的解释；
- 版本/扩展：EXTENSIONS_AND_METATHEORY；
- 我们的问题：TEMPORAL_AUDIT_MAP，不能回写污染上游原文；
- 覆盖与阅读证据：本页；
- 用户要求：rulings R-015、Feature HOTT-009；
- 当前行动与下一步：MEMORY；
- 原有数学主张裁决：CLAIM_EVIDENCE_MATRIX，未因 Schema 自动升级。

本轮 T01–T05/T08/T22–T24 更新需求、领域参考和路由；T13 只新增文档/来源核验，不改数学证明状态；
T06–T07/T09–T12/T14–T21/T25–T26 无新架构、运行、数据库、权限或 AI 行为合同变更。
无 commit/push/发布、无 subagent、无修改历史归档。

## 9. v0.2 外部 Schema 比较后的补充

外部材料：`外部资料/An Authoritative Theory Schema for Homotopy Type Theory.md`，65427 bytes，
SHA-256 `fda74232288bd31dd52835593ec18f5e64d6cdeeb826a4fe89cd904e537494e0`。
它是外部 AI 的综合与建议，不是定理证明或官方规范；本项目不改该文件。原会话引用标记不能替代
独立来源，采纳内容改用下面的一手 URL/版本。

| 来源 | 版本/核查深度 | 本版去向 |
|---|---|---|
| [Local universes](https://arxiv.org/abs/1411.1736v2) | v2；摘要中的输入条件和严格化结论 | S03/S04 |
| [Strict univalent universes](https://arxiv.org/abs/1904.07004v2) | v2；Grothendieck (∞,1)-topos 的呈现结论 | S06 |
| [Modalities](https://arxiv.org/abs/1706.07526v6) | v6；摘要与 Book 第7章的概念/规则；未重证全集 | D07 |
| [Cubical Agda](https://agda.readthedocs.io/en/latest/language/cubical.html) | 实际页面 Agda2.9.0；PathP/transp/J/HIT 段 | 核心跨呈现表、E13 |
| [CHM HIT](https://arxiv.org/abs/1802.01170v2) | v2；摘要列出的允许类与计算性质 | E12 |
| [Cartesian CHTT III](https://arxiv.org/abs/1712.01800) | 原始 arXiv 版本；摘要结构与 universe/pretype 区分 | E11 |
| [2-Coherent Internal Models](https://arxiv.org/abs/2503.05790v2) | v2；摘要，2-coherent 范围不外推 | S07/E14 |
| [Displayed Type Theory](https://arxiv.org/abs/2311.18781v2) | v2；摘要，多模态与 SST | S07/E14 |
| [Directed univalence](https://arxiv.org/abs/2407.09146v2) | v2；摘要，新增模态/原则与结论 | S07/E14 |
| [Univalence without funext](https://arxiv.org/abs/2605.00812v2) | v2；摘要，标准/较弱 categorical 原则分离 | C14 补充、E15 |
| [Lean Eq](https://lean-lang.org/doc/reference/latest/Basic-Propositions/Propositional-Equality/) / [Prop](https://lean-lang.org/doc/reference/latest/The-Type-System/Propositions/) | 官方页面当前签名/证明无关性，未运行新内核测试 | 实现限制表 |

Awodey–Warren、弱高阶群胚论文、BCH 与 Coq-HoTT 实现论文作为一手阅读路线补入；不声称本轮全文
审读它们。本文原21文件/105节覆盖仍是 Book 基线，不把新增 URL 计成已保存全文或全部验证。

采纳：语义层、三类相干性、关系类型、跨呈现计算、h-level 对照、模态细分、近期内部/有向研究。
校准：qinv 不自动与 isEquiv 等价；proof-uses 不等于 assumption-necessary；普通 Lean Eq 不能
充当高阶 Id；所有 localization 不自动具备指定 modality；“最佳后端”不是数学定理。
未采纳为当前工程：知识图谱数据库、完整双后端、全书/全模型机器形式化作为探索前置。

本版规则与主题说明已补齐上述计划；全领域逐证明、所有扩展完整语法、本地计算符合性仍是 G01–G06。
核心ID仍C01–C18，派生D01–D12，扩展到E01–E15，新增S01–S09。没有因文档增加提高悖论证明状态。

===== END SOURCE CHUNK | EOF=true =====


===== SOURCE HoTT/theory-schema/TEMPORAL_AUDIT_MAP.md | SHA256 072d3adaa8340180b9c63a4b3fa205b589a289db98f290e47982e824909d5f83 | LINES 1-133/133 =====
# 时间维度与现实相对悖论的理论审查地图

类型：HUMAN_EDITED；v0.2。此文件是**研究使用层**，不是 HoTT 原始定义的一部分。
用户原意与最高研究目标仍由 [用户原文](../sources/user-originals/Z铁律-抽象-圆环-时间维度-用户原始论述-20260901.md)
和 [Z 研究规范](../Z_LAW_REALITY_RELATIVE_PARADOXES.md) 拥有；本文不把哲学预期写成 HoTT 已证缺陷。

## 1. 先区分四种“顺序”

当前工作顺序：先发现并确认具体悖论，再研究最终错误前提与修复。可先提出故事、直觉和构造；
确认时核实际推演与同一任务中的冲突，不要求探索前已证明完整归因。用户最新原文见
[第五闭包 §19](../../认知闭包/2026-09-01-Z铁律最终定性-时间否定与朴素集合论-HoTT怀疑-认知闭包.md#discovery-before-attribution-full)。

- 推导树的先决关系：使用规则前须有前提推导；
- 上下文/定义的依赖顺序：类型或构造子只能引用许可范围内的数据；
- 求值顺序：选定归约策略下的操作步骤；
- 现实时间：设备、事件、截止期、因果和历史。

HoTT 对前两项已经有明确要求，基础归约也有操作方向。第四项未自动成为所有裸 judgment 的
不可擦除坐标。我们的目标是找具体差异，不能把四项压成“有/没有时间”的单一按钮。

## 2. 六个实际审查接口

六个接口是定位工具，不是只许研究六个问题。始终保留：先后/依赖、落定/可用性、生成资格、
持续过程/完成态、执行成本、历史来源、不可逆方向、自指反射、运动可分性九类方向。稠密性、
物理运动和成本都只是分支，不能因最近讨论而覆盖其它方向。

| ID | 理论接口 | 要检查的现实条件 | 必须给出的证据 | 正确拒绝/反例 |
|---|---|---|---|---|
| T01 | C02/C03/C10/C16 形成与依赖 | 尚未落定数据是否先被使用 | 一个真正通过所选规则、却不符合指定准入制度的构造，或一条明确限制定理 | 未声明变量、非正性构造被拒绝，不是理论失败 |
| T02 | C05/C14 函数相等 | 同输出但按期可用性/成本不同 | 程序语法、语义映射、cost、点态相等与 funext、现实承诺 | Runtime 规格被正确拒绝，只说明裸函数不足 |
| T03 | C11/C12 identity/transport | 不可逆过程是否被误作可逆路径 | 明确的过程→路径解释及不能逆执行的依据 | 普通函数/关系可非可逆，不能只展示 p⁻¹ 就宣判 |
| T04 | C06/C15/D09 结构同一性 | 生成历史、原作与复制品 | 带来源对象→裸结构、同表示异历史见证 | 加回 provenance 后等价需保它，说明限制相对表示 |
| T05 | D02/D03/D07 截断/存在/反射 | 是否从“仅存在”无条件交付具体见证 | 某个真实消去/提取声称，及其缺失侧条件 | 截断本来就不许可任意提取；省略限制是使用错误 |
| T06 | C09/C18 与 E03/E04 阶段/固定点 | 动态合法轨道是否被压成静态稳定值 | 真正 source/target、翻译、更新律保持及阶段压平条件 | 静态保存整个序列不会自动迫使所有阶段同值 |

Schema 的工作不是让每行都得到“失败”，而是让每行能得到准确结论：保留、丢失、拒绝、不能
下降、解释越界，或尚无证据。

## 3. 一条已贯通的审查链：同函数异时

研究配置：书式 HoTT 的自然数与函数外延性，加**外部明确指定**的未优化执行语义。

```text
C09 允许结构递归的 fast / slow
  → 证明每个输入的输出相等
  → C14 得到函数 identity
  → 比较两个程序实现的成本/截止期
  → 假设仅由函数语义可以精确恢复每种实现的成本
  → 同一函数必须给同一成本，与实现差异不符
```

结论是该恢复要求不成立。不能把最后一步当成 HoTT 核心原本提供的 Runtime 函数。
可用 C06 把程序语法/轨迹/成本放入更丰富对象；也可研究 E08 的原生成本规则。

当前状态沿用原研究：纸笔候选和文献支持，不是本轮新增形式化证明。Schema 增加的是精确
rule-to-question 路径，而不是新的悖论验收。

## 4. 更接近“计算合法性”的接口：阶段压平

```text
x(n+1)=F(x(n))
所有 x(n) 都被要求等于同一个 collapsed 值
同时保留原更新关系
⇒ collapsed=F(collapsed)
```

这条条件引理已在项目 [ZCore.agda](../formal/self-contained/ZCore.agda) 中。第二行是额外实质前提，
不是“表达式里没有写 t”的自动后果。

与 E03/E04 接轨还缺真正的翻译。一个把 guarded 对象编码成序列的 HoTT 表示可以保留阶段；
不能用“静态数学”一词排除这种可能。

## 5. 形成顺序已经有了，还能研究什么？

依然可以研究：

- 变量作为逻辑假设可用，与现实中值是否已经产生之间的差异；
- 类型检查保证的构造资格，与限定预算/资源下的交付资格之间的差异；
- 归约参与判断相等，与完整轨迹是否属于最终对象 identity 之间的差异；
- HIT 构造子书写依赖顺序，与对象表示的运行时生成历史之间的差异；
- 可证明有某项，与能否在当前知识/时间/设备条件下取得它之间的差异。

但每一种差异都要明确它是否属于理论实际承诺。不能因为我们提出了一个更强的现实要求，就说
理论违反了自己的规则。

## 6. 反向审计：哪些发现必须使某个候选降级？

1. 所谓悖论表达式没有类型；
2. 要取消 universe、正性、消去或时钟条件才能得到冲突；
3. 把命题相等当作判断相等；
4. 把所有函数当作可逆路径；
5. 把截断的见证忘却当作理论仍承诺返回见证；
6. 仅在我们强行增加“所有阶段同值”后才出现固定点；
7. 换用同一个 HoTT 内的丰富结构后，原来的“不可能表达”主张失效；
8. 理论根本没有作出被反驳的现实承诺；
9. 旧 AI 的描述与固定一手规则不符；
10. 某篇后续论文已经处理了被我们当作全领域未解的问题。

降级不等于丢弃原始讨论；应保留原文和失败原因。一个被正确否定的候选减少了关键未知，比把它
改名成更宏大的“悖论”更有用。

## 7. 一次 Schema 使用的结果应是什么

从探索推进到确认时，按所需证据逐步填写短记录即可，不要求最初猜想就填满最终归因：

```text
所选系统与公理：
对应 C/D/E 条目：
表达式、上下文、宇宙：
所用规则和原始来源：
目标现实任务及必要条件：
理论实际结论：
解释/完成性提升发生在哪一步：
反例或不保留见证：
恢复条件后的对照：
尚未证明的部分：
```

“恢复条件后的对照”服务后续归因/修复；若尚未完成，不阻塞已有具体冲突的有界确认。
结论用普通话说明：是理论限制、解释越界、正确拒绝，还是规则层不相容。
用户的最高哲学命题不因 Schema 形成而得到全称证明；HoTT 内部一致性也不是当前研究唯一判据。

## 8. 最小推进建议

新增语义/相干性与内部模型为自指、阶段依赖和跨呈现差异增加了入口。它们不自动是时间的同义物，
也不预设已经产生悖论。按候选需要使用语义页 S01–S09 与扩展 E11–E15，不另建无限准备工程。

先利用核心接口完成一个候选的整个证据链，再按它实际用到的定理/变体深化 Schema。
不要等到所有数学分支和所有未来扩展都读完才允许研究；也不要因着急找悖论而跳过当前候选依赖
的核心规则和侧条件。

本轮已提供这样的理论定位能力。未完成的全书逐证明审查与跨变体规则展开由来源覆盖页准确登记，
不是隐藏在“权威且完整”四个字后面。

===== END SOURCE CHUNK | EOF=true =====


===== SOURCE HoTT/theory-schema/upstream/README.md | SHA256 356f9f25e44c6ccacb19e354267fcf7ea56986038c25348916cbd378b766fb81 | LINES 1-12/12 =====
# HoTT Book 一手来源快照

来源：The Univalent Foundations Program，HoTT/book。

固定上游 commit：`578b85cc8d586b1677ec4335148adeb443057d24`。

目录 `book-578b85cc/` 保存从该 commit 下载的原始文本，保持上游字节，不手工改写。
这是选定理论章节与定位辅助文件的只读证据快照，不是完整 Git clone，也不是可编译的全书工程。
来源原文沿用上游 CC BY-SA 3.0；许可原文见该目录 README.md。本文档与 Schema 的解释不是上游认可或背书。

具体文件、SHA、覆盖和阅读范围由 `../SOURCES_AND_COVERAGE.md` 登记。变更来源必须另选明确 commit，
不得把 master 的后来变化静默覆盖到当前版本。

===== END SOURCE CHUNK | EOF=true =====


===== SOURCE HoTT/theory-schema/upstream/book-578b85cc/README.md | SHA256 79d6220e154e2774e6682eefb923bd8a26d7f7e6ded3dd49b0d3a87f44c5e81b | LINES 1-72/72 =====
This is a textbook on informal homotopy type theory.
It is part of the [Univalent foundations of mathematics](http://www.math.ias.edu/sp/univalent)
project that took place at the Institute for Advanced Study in 2012/13.

## License

This work is licensed under the
[Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0/).

## Distribution

Compiled and printed versions of the book are available at the
[homotopy type theory website](http://homotopytypetheory.org/book),
and nightly builds are available on the
[github wiki](https://github.com/HoTT/book/wiki/Nightly-Builds).

## Editing the book

This book is not a community project, but we do welcome our readers to suggest improvements. The best way to propose an edit is to [open a pull request](https://github.com/HoTT/book/compare) with your suggested change. You can also [open an issue](https://github.com/HoTT/book/issues/new/choose) if you do not have a concrete proposal yet. The issues and the pull requests are dedicated to improvements, questions, and other issues pertaining to the HoTT book itself. General discussions about homotopy type theory and topics related to the wider HoTT community are welcome at the [homotopytypetheory google group](https://groups.google.com/g/homotopytypetheory) or at the [HoTT zulip](https://hott.zulipchat.com). For further directions about editing the book, see the [guidelines for contributions](https://github.com/HoTT/book/blob/master/CONTRIBUTING.md)

## Code of conduct

For many, the HoTT book is their introduction to our subject and our diverse community, including people from any nationality, gender identity, sexual orientation, race, color, ability, and background. In order to ensure for everyone a welcoming and inclusive environment in our discussions, we follow the guidelines of the [GitHub code of conduct](https://docs.github.com/en/site-policy/github-terms/github-community-forum-code-of-conduct). You can expect from the authors and any participant that we are kind and respectful in discussions, that we use inclusive language, and that we do our best to understand each other's different perspectives. It might not always be that we accept the change in the way you proposed it, but we always value your input, regardless of your level of experience or status within the community.

## Prerequisites and compilation

To compile the book for yourself you need a fairly new version of LaTeX.
[Texlive](http://www.tug.org/texlive/) 2012 is confirmed to work. You might need
to install some packages; see `main.tex` for packages that are used by the book.

[BasicTeX](http://www.tug.org/mactex/morepackages.html), which is a minimalistic
version of MacTeX, is confirmed to work once the following packages have been
installed: `tlmgr`, `install`, `braket`, `comment`, `courier`, `enumitem`,
`helvetic`, `mathpazo`, `nextpage`, `ntheorem`, `palatino`, `rsfs`, `stmaryrd`,
`symbol`, `titlesec`, `wallpaper`, `wasy`, `wasysym`, `xstring`, `zapfding`.

You also need the `make` utility. The book is a fairly complex piece of LaTeX
code. Also, the file `version.tex` is generated on the fly, so you will need the
`make` utility with which you can compile the main files, as follows:

* `make hott-online.pdf` -- the book appropriate for online reading, with colors and green links
* `make hott-ebook.pdf` -- the book with small margins, suitable for ebook readers
* `make hott-ebook-wide.pdf` -- the book with small margins, suitable for ebook readers, wider page
* `make hott-ebook-narrow.pdf` -- the book with small margins, suitable for ebook readers, narrower page
* `make hott-letter.pdf cover-letter.pdf` -- the book in black & white, letter paper format,
   for printing at home, as well as a color cover (just two pages)
* `make hott-a4.pdf cover-a4.pdf` -- the book in black & white, A4 paper format,
   for printing at home, as well as a color cover (just two pages)
* `make hott-arxiv.pdf` -- the version that is uploaded to arXiv
* `make hott-letter-exercises.pdf` -- the book in black & white, letter paper format, but with exercises one-per-page
* `make hott-a4-exercises.pdf` -- the book in black & white, A4 paper format, but with exercises one-per-page
* `make hott-ustrade.pdf cover-lulu-hardcover.pdf cover-lulu-paperback.pdf` --
   the book in US Trade format, without cover, used for the bound copy available
   at http://lulu.com/
* `make exercise_solutions.pdf` -- (some) solutions to exercises
* `make errata.pdf` -- errata for the HoTT Book, first edition

Note: once `make` is run so that `version.tex` is generated, you need not run `make` every time you make
a change to the source file. You can just perform the usual LaTeX cycle from your favorite editor.

#### Compiling without `make`

If you do not have `make` (for example, because you are on MacOS and you did not
install the XCode command-line utilities), you can still fake it as follows.
Create the file `version.tex` and put in it (where "Joe Hacker" should be
replaced with your name):

    \newcommand{\OPTversion}{Joe-Hacker-version}

Then use whatever tools you normally do to compile LaTeX. The main LaTeX files are called 
`hott-XXX.tex`. But you really should have `make`, you know.


===== END SOURCE CHUNK | EOF=true =====


===== SOURCE HoTT/theory-schema/upstream/book-578b85cc/equivalences.tex | SHA256 037dce18db74526a3f7148c353bb5459da1c4b65e046780a208de39633df1722 | LINES 1-1118/1118 =====
\chapter{Equivalences}
\label{cha:equivalences}

We now study in more detail the notion of \emph{equivalence of types} that was introduced briefly in \cref{sec:basics-equivalences}.
Specifically, we will give several different ways to define a type $\isequiv(f)$ having the properties mentioned there.
Recall that we wanted $\isequiv(f)$ to have the following properties, which we restate here:
\begin{enumerate}
\item $\qinv(f) \to \isequiv (f)$.\label{item:beb1}
\item $\isequiv (f) \to \qinv(f)$.\label{item:beb2}
\item $\isequiv(f)$ is a mere proposition.\label{item:beb3}
\end{enumerate}
Here $\qinv(f)$ denotes the type of quasi-inverses to $f$:
\begin{equation*}
  \sm{g:B\to A} \big((f \circ g \htpy \idfunc[B]) \times (g\circ f \htpy \idfunc[A])\big).
\end{equation*}
By function extensionality, it follows that $\qinv(f)$ is equivalent to the type
\begin{equation*}
  \sm{g:B\to A} \big((f \circ g = \idfunc[B]) \times (g\circ f = \idfunc[A])\big).
\end{equation*}
We will define three different types having properties~\ref{item:beb1}--\ref{item:beb3}, which we call
\begin{itemize}
\item half adjoint equivalences,
\item bi-invertible maps,
  \index{function!bi-invertible}
  and
\item contractible functions.
\end{itemize}
We will also show that all these types are equivalent.
These names are intentionally somewhat cumbersome, because after we know that they are all equivalent and have properties~\ref{item:beb1}--\ref{item:beb3}, we will revert to saying simply ``equivalence'' without needing to specify which particular definition we choose.
But for purposes of the comparisons in this chapter, we need different names for each definition.

Before we examine the different notions of equivalence, however, we give a little more explanation of why a different concept than quasi-invertibility is needed.

\section{Quasi-inverses}
\label{sec:quasi-inverses}

\index{quasi-inverse|(}%
We have said that $\qinv(f)$ is unsatisfactory because it is not a mere proposition, whereas we would rather that a given function could ``be an equivalence'' in at most one way.
However, we have given no evidence that $\qinv(f)$ is not a mere proposition.
In this section we exhibit a specific counterexample.

\begin{lem}\label{lem:qinv-autohtpy}
  If $f:A\to B$ is such that $\qinv (f)$ is inhabited, then
  \[\eqv{\qinv(f)}{\Parens{\prd{x:A}(x=x)}}.\]
\end{lem}
\begin{proof}
  By assumption, $f$ is an equivalence; that is, we have $e:\isequiv(f)$ and so $(f,e):\eqv A B$.
  By univalence, $\idtoeqv:(A=B) \to (\eqv A B)$ is an equivalence, so we may assume that $(f,e)$ is of the form $\idtoeqv(p)$ for some $p:A=B$.
  Then by path induction, we may assume $p$ is $\refl{A}$, in which case $f$ is $\idfunc[A]$.
  Thus we are reduced to proving $\eqv{\qinv(\idfunc[A])}{(\prd{x:A}(x=x))}$.
  Now by definition we have
  \[ \qinv(\idfunc[A]) \jdeq
  \sm{g:A\to A} \big((g \htpy \idfunc[A]) \times (g \htpy \idfunc[A])\big).
  \]
  By function extensionality, this is equivalent to
  \[ \sm{g:A\to A} \big((g = \idfunc[A]) \times (g = \idfunc[A])\big).
  \]
  And by \cref{ex:sigma-assoc}, this is equivalent to
  \[ \sm{h:\sm{g:A\to A} (g = \idfunc[A])} (\proj1(h) = \idfunc[A])
  \]
  However, by \cref{thm:contr-paths}, $\sm{g:A\to A} (g = \idfunc[A])$ is contractible with center $(\idfunc[A],\refl{\idfunc[A]})$; therefore by \cref{thm:omit-contr} this type is equivalent to $\idfunc[A] = \idfunc[A]$.
  And by function extensionality, $\idfunc[A] = \idfunc[A]$ is equivalent to $\prd{x:A} x=x$.
\end{proof}

\noindent
We remark that \cref{ex:qinv-autohtpy-no-univalence} asks for a proof of the above lemma which avoids univalence.

Thus, what we need is some $A$ which admits a nontrivial element of $\prd{x:A}(x=x)$.
Thinking of $A$ as a higher groupoid, an inhabitant of $\prd{x:A}(x=x)$ is a natural transformation\index{natural!transformation} from the identity functor of $A$ to itself.
Such transformations are said to form the \define{center of a category},
\index{center!of a category}%
\index{category!center of}%
since the naturality axiom requires that they commute with all morphisms.
Classically, if $A$ is simply a group regarded as a one-object groupoid, then this yields precisely its center in the usual group-theoretic sense.
This provides some motivation for the following.

\begin{lem}\label{lem:autohtpy}
  Suppose we have a type $A$ with $a:A$ and $q:a=a$ such that
  \begin{enumerate}
  \item The type $a=a$ is a set.\label{item:autohtpy1}
  \item For all $x:A$ we have $\brck{a=x}$.\label{item:autohtpy2}
  \item For all $p:a=a$ we have $p\ct q = q \ct p$.\label{item:autohtpy3}
  \end{enumerate}
  Then there exists $f:\prd{x:A} (x=x)$ with $f(a)=q$.
\end{lem}
\begin{proof}
  Let $g:\prd{x:A} \brck{a=x}$ be as given by~\ref{item:autohtpy2}.  First we
  observe that each type $\id[A]xy$ is a set.  For since being a set is a mere
  proposition, we may apply the induction principle of propositional truncation, and assume that $g(x)=\bproj
  p$ and $g(y)=\bproj{p'}$ for $p:a=x$ and $p':a=y$.  In this case, composing with
  $p$ and $\opp{p'}$ yields an equivalence $\eqv{(x=y)}{(a=a)}$.  But $(a=a)$ is
  a set by~\ref{item:autohtpy1}, so $(x=y)$ is also a set.

  Now, we would like to define $f$ by assigning to each $x$ the path $\opp{g(x)}
  \ct q \ct g(x)$, but this does not work because $g(x)$ does not inhabit $a=x$
  but rather $\brck{a=x}$, and the type $(x=x)$ may not be a mere proposition,
  so we cannot use induction on propositional truncation.  Instead we can apply
  the technique mentioned in \cref{sec:unique-choice}: we characterize
  uniquely the object we wish to construct.  Let us define, for each $x:A$, the
  type
  \[ B(x) \defeq \sm{r:x=x} \prd{s:a=x} (r = \opp s \ct q\ct s).\]
  We claim that $B(x)$ is a mere proposition for each $x:A$.
  Since this claim is itself a mere proposition, we may again apply induction on
  truncation and assume that $g(x) = \bproj p$ for some $p:a=x$.
  Now suppose given $(r,h)$ and $(r',h')$ in $B(x)$; then we have
  \[ h(p) \ct \opp{h'(p)} : r = r'. \]
  It remains to show that $h$ is identified with $h'$ when transported along this equality, which by transport in identity types and function types (\cref{sec:compute-paths,sec:compute-pi}), reduces to showing
  \[ h(s) = h(p) \ct \opp{h'(p)} \ct h'(s) \]
  for any $s:a=x$.
  But each side of this is an equality between elements of $(x=x)$, so it follows from our above observation that $(x=x)$ is a set.

  Thus, each $B(x)$ is a mere proposition; we claim that $\prd{x:A} B(x)$.
  Given $x:A$, we may now invoke the induction principle of propositional truncation to assume that $g(x) = \bproj p$ for $p:a=x$.
  We define $r \defeq \opp p \ct q \ct p$; to inhabit $B(x)$ it remains to show that for any $s:a=x$ we have
  $r = \opp s \ct q \ct s$.
  Manipulating paths, this reduces to showing that $q\ct (p\ct \opp s) = (p\ct \opp s) \ct q$.
  But this is just an instance of~\ref{item:autohtpy3}.
\end{proof}

\begin{thm}\label{thm:qinv-notprop}
  There exist types $A$ and $B$ and a function $f:A\to B$ such that $\qinv(f)$ is not a mere proposition.
\end{thm}
\begin{proof}
  It suffices to exhibit a type $X$ such that $\prd{x:X} (x=x)$ is not a mere proposition.
  Define $X\defeq \sm{A:\type} \brck{\bool=A}$, as in the proof of \cref{thm:no-higher-ac}.
  It will suffice to exhibit an $f:\prd{x:X} (x=x)$ which is unequal to $\lam{x} \refl{x}$.

  Let $a \defeq (\bool,\bproj{\refl{\bool}}) : X$, and let $q:a=a$ be the path corresponding to the nonidentity equivalence $e:\eqv\bool\bool$ defined by $e(\bfalse)\defeq\btrue$ and $e(\btrue)\defeq\bfalse$.
  We would like to apply \cref{lem:autohtpy} to build an $f$.
  By definition of $X$, equalities in subset types (\cref{subsec:prop-subsets}), and univalence, we have $\eqv{(a=a)}{(\eqv{\bool}{\bool})}$, which is a set, so~\ref{item:autohtpy1} holds.
  Similarly, by definition of $X$ and equalities in subset types we have~\ref{item:autohtpy2}.
  Finally, \cref{ex:eqvboolbool} implies that every equivalence $\eqv\bool\bool$ is equal to either $\idfunc[\bool]$ or $e$, so we can show~\ref{item:autohtpy3} by a four-way case analysis.

  Thus, we have $f:\prd{x:X} (x=x)$ such that $f(a) = q$.
  Since $e$ is not equal to $\idfunc[\bool]$, $q$ is not equal to $\refl{a}$, and thus $f$ is not equal to $\lam{x} \refl{x}$.
  Therefore, $\prd{x:X} (x=x)$ is not a mere proposition.
\end{proof}

More generally, \cref{lem:autohtpy} implies that any ``Eilenberg--Mac Lane space'' $K(G,1)$, where $G$ is a nontrivial abelian\index{group!abelian} group, will provide a counterexample; see \cref{cha:homotopy}.
The type $X$ we used turns out to be equivalent to $K(\mathbb{Z}_2,1)$.
In \cref{cha:hits} we will see that the circle $\Sn^1 = K(\mathbb{Z},1)$ is another easy-to-describe example.

We now move on to describing better notions of equivalence.

\index{quasi-inverse|)}%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Half adjoint equivalences}
\label{sec:hae}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\index{equivalence!half adjoint|(defstyle}%
\index{half adjoint equivalence|(defstyle}%
\index{adjoint!equivalence!of types, half|(defstyle}%

In \cref{sec:quasi-inverses} we concluded that $\qinv(f)$ is equivalent to $\prd{x:A} (x=x)$ by discarding a contractible type.
Roughly, the type $\qinv(f)$ contains three data $g$, $\eta$, and $\epsilon$, of which two ($g$ and $\eta$) could together be seen to be contractible when $f$ is an equivalence.
The problem is that removing these data left one remaining ($\epsilon$).
In order to solve this problem, the idea is to add one \emph{additional} datum which, together with $\epsilon$, forms a contractible type.

\begin{defn}\label{defn:ishae}
  A function $f:A\to B$ is a \define{half adjoint equivalence}
  if there are $g:B\to A$ and homotopies $\eta: g \circ f \htpy \idfunc[A]$ and $\epsilon:f \circ g \htpy \idfunc[B]$ such that there exists a homotopy
  \[\tau : \prd{x:A} \map{f}{\eta x} = \epsilon(fx).\]
\end{defn}

Thus we have a type $\ishae(f)$, defined to be
\begin{equation*}
  \sm{g:B\to A}{\eta: g \circ f \htpy \idfunc[A]}{\epsilon:f \circ g \htpy \idfunc[B]} \prd{x:A} \map{f}{\eta x} = \epsilon(fx).
\end{equation*}
Note that in the above definition, the coherence\index{coherence} condition relating $\eta$ and $\epsilon$ only involves $f$.
We might consider instead an analogous coherence condition involving $g$:
\[\upsilon : \prd{y:B} \map{g}{\epsilon y} = \eta(gy)\]
and a resulting analogous definition $\ishae'(f)$.

Fortunately, it turns out each of the conditions implies the other one:

\begin{lem}\label{lem:coh-equiv}
For functions $f : A \to B$ and $g:B\to A$ and homotopies $\eta: g \circ f \htpy \idfunc[A]$ and $\epsilon:f \circ g \htpy \idfunc[B]$, the following conditions are logically equivalent:
\begin{itemize}
\item $\prd{x:A} \map{f}{\eta x} = \epsilon(fx)$
\item $\prd{y:B} \map{g}{\epsilon y} = \eta(gy)$
\end{itemize}
\end{lem}
\begin{proof}
  It suffices to show one direction; the other one is obtained by replacing $A$, $f$, and $\eta$ by $B$, $g$, and $\epsilon$ respectively.
  Let $\tau : \prd{x:A}\;\map{f}{\eta x} = \epsilon(fx)$.
  Fix $y : B$.
  Using naturality of $\epsilon$ and applying $g$, we get the following commuting diagram of paths:
\[\uppercurveobject{{ }}\lowercurveobject{{ }}\twocellhead{{ }}
  \xymatrix@C=3pc{gfgfgy \ar@{=}^-{gfg(\epsilon y)}[r] \ar@{=}_{g(\epsilon (fgy))}[d] & gfgy \ar@{=}^{g(\epsilon y)}[d] \\ gfgy \ar@{=}_{g(\epsilon y)}[r] & gy
  }\]
Using $\tau(gy)$ on the left side of the diagram gives us
\[\uppercurveobject{{ }}\lowercurveobject{{ }}\twocellhead{{ }}
  \xymatrix@C=3pc{gfgfgy \ar@{=}^-{gfg(\epsilon y)}[r] \ar@{=}_{gf(\eta (gy))}[d] & gfgy \ar@{=}^{g(\epsilon y)}[d] \\ gfgy \ar@{=}_{g(\epsilon y)}[r] & gy
  }\]
Using the commutativity of $\eta$ with $g \circ f$ (\cref{cor:hom-fg}), we have
\[\uppercurveobject{{ }}\lowercurveobject{{ }}\twocellhead{{ }}
  \xymatrix@C=3pc{gfgfgy \ar@{=}^-{gfg(\epsilon y)}[r] \ar@{=}_{\eta (gfgy)}[d] & gfgy \ar@{=}^{g(\epsilon y)}[d] \\ gfgy \ar@{=}_{g(\epsilon y)}[r] & gy
  }\]
However, by naturality of $\eta$ we also have
\[\uppercurveobject{{ }}\lowercurveobject{{ }}\twocellhead{{ }}
  \xymatrix@C=3pc{gfgfgy \ar@{=}^-{gfg(\epsilon y)}[r] \ar@{=}_{\eta (gfgy)}[d] & gfgy \ar@{=}^{\eta(gy)}[d] \\ gfgy \ar@{=}_{g(\epsilon y)}[r] & gy
  }\]
Thus, canceling all but the right-hand homotopy, we have $g(\epsilon y) = \eta(g y)$ as desired.
\end{proof}

However, it is important that we do not include \emph{both} $\tau$ and $\upsilon$ in the definition of $\ishae (f)$ (whence the name ``\emph{half} adjoint equivalence'').
If we did, then after canceling contractible types we would still have one remaining datum --- unless we added another higher coherence condition.
In general, we expect to get a well-behaved type if we cut off after an odd number of coherences.

Of course, it is obvious that $\ishae(f) \to\qinv(f)$: simply forget the coherence datum.
The other direction is a version of a standard argument from homotopy theory and category theory.

\begin{thm}\label{thm:equiv-iso-adj}
  For any $f:A\to B$ we have $\qinv(f)\to\ishae(f)$.
\end{thm}
\begin{proof}
Suppose that $(g,\eta,\epsilon)$ is a quasi-inverse for $f$. We have to provide
a quadruple $(g',\eta',\epsilon',\tau)$ witnessing that $f$ is a half adjoint equivalence. To
define $g'$ and $\eta'$, we can just make the obvious choice by setting $g'
\defeq g$ and $\eta'\defeq \eta$. However, in the definition of $\epsilon'$ we
need start worrying about the construction of $\tau$, so we cannot just follow our nose
and take $\epsilon'$ to be $\epsilon$. Instead, we take
\begin{equation*}
\epsilon'(b) \defeq \opp{\epsilon(f(g(b)))}\ct (\ap{f}{\eta(g(b))}\ct \epsilon(b)).
\end{equation*}
Now we need to find
\begin{equation*}
\tau(a): \ap{f}{\eta(a)}=\opp{\epsilon(f(g(f(a))))}\ct (\ap{f}{\eta(g(f(a)))}\ct \epsilon(f(a))).
\end{equation*}
Note first that by \cref{cor:hom-fg}, we have
%$\eta(g(f(a)))\ct\eta(a)=\ap{g}{\ap{f}{\eta(a)}}\ct\eta(a)$ and hence it follows that
$\eta(g(f(a)))=\ap{g}{\ap{f}{\eta(a)}}$. Therefore, we can apply
\cref{lem:htpy-natural} to compute
\begin{align*}
\ap{f}{\eta(g(f(a)))}\ct \epsilon(f(a))
& = \ap{f}{\ap{g}{\ap{f}{\eta(a)}}}\ct \epsilon(f(a))\\
& = \epsilon(f(g(f(a))))\ct \ap{f}{\eta(a)}
\end{align*}
from which we get the desired path $\tau(a)$.
\end{proof}

Combining this with \cref{lem:coh-equiv} (or symmetrizing the proof), we also have $\qinv(f)\to\ishae'(f)$.

It remains to show that $\ishae(f)$ is a mere proposition.
For this, we will need to know that the fibers of an equivalence are contractible.

\begin{defn}\label{defn:homotopy-fiber}
  The \define{fiber}
  \indexdef{fiber}%
  \indexsee{function!fiber of}{fiber}%
  of a map $f:A\to B$ over a point $y:B$ is
  \[ \hfib f y \defeq \sm{x:A} (f(x) = y).\]
\end{defn}

In homotopy theory, this is what would be called the \emph{homotopy fiber} of $f$.
The path lemmas in \cref{sec:computational} yield the following characterization of paths in fibers:

\begin{lem}\label{lem:hfib}
  For any $f : A \to B$, $y : B$, and $(x,p),(x',p') : \hfib{f}{y}$, we have
  \[ \big((x,p) = (x',p')\big) \eqvsym \Parens{\sm{\gamma : x = x'} f(\gamma) \ct p' = p} \qedhere\]
\end{lem}

\begin{thm}\label{thm:contr-hae}
  If $f:A\to B$ is a half adjoint equivalence, then for any $y:B$ the fiber $\hfib f y$ is contractible.
\end{thm}
\begin{proof}
  Let $(g,\eta,\epsilon,\tau) : \ishae(f)$, and fix $y : B$.
  As our center of contraction for $\hfib{f}{y}$ we choose $(gy, \epsilon y)$.
  Now take any $(x,p) : \hfib{f}{y}$; we want to construct a path from $(gy, \epsilon y)$ to $(x,p)$.
  By \cref{lem:hfib}, it suffices to give a path $\gamma : \id{gy}{x}$ such that $\ap f\gamma \ct p = \epsilon y$.
  We put $\gamma \defeq \opp{g(p)} \ct \eta x$.
  Then we have
  \begin{align*}
    f(\gamma) \ct p & = \opp{fg(p)} \ct f (\eta x) \ct p \\
    & = \opp{fg(p)} \ct \epsilon(fx) \ct p \\
    & = \epsilon y
  \end{align*}
  where the second equality follows by $\tau x$ and the third equality is naturality of $\epsilon$.
\end{proof}

We now define the types which encapsulate contractible pairs of data.
The following types put together the quasi-inverse $g$ with one of the homotopies.

\begin{defn}\label{defn:linv-rinv}
  Given a function $f:A\to B$, we define the types
    \begin{align*}
      \linv(f) &\defeq \sm{g:B\to A} (g\circ f\htpy \idfunc[A])\\
      \rinv(f) &\defeq \sm{g:B\to A} (f\circ g\htpy \idfunc[B])
    \end{align*}
  of \define{left inverses}
  \indexdef{left!inverse}%
  \indexdef{inverse!left}%
  and \define{right inverses}
  \indexdef{right!inverse}%
  \indexdef{inverse!right}%
  to $f$, respectively.
  We call $f$ \define{left invertible}
  \indexdef{function!left invertible}%
  \indexdef{function!right invertible}%
  if $\linv(f)$ is inhabited, and similarly \define{right invertible}
  \indexdef{left!invertible function}%
  \indexdef{right!invertible function}%
  if $\rinv(f)$ is inhabited.
\end{defn}

\begin{lem}\label{thm:equiv-compose-equiv}
  If $f:A\to B$ has a quasi-inverse, then so do
  \begin{align*}
    (f\circ \blank) &: (C\to A) \to (C\to B)\\
    (\blank\circ f) &: (B\to C) \to (A\to C).
  \end{align*}
\end{lem}
\begin{proof}
  If $g$ is a quasi-inverse of $f$, then $(g\circ \blank)$ and $(\blank\circ g)$ are quasi-inverses of $(f\circ \blank)$ and $(\blank\circ f)$ respectively.
\end{proof}

\begin{lem}\label{lem:inv-hprop}
  If $f : A \to B$ has a quasi-inverse, then the types $\rinv(f)$ and $\linv(f)$ are contractible.
\end{lem}
\begin{proof}
  By function extensionality, we have
  \[\eqv{\linv(f)}{\sm{g:B\to A} (g\circ f = \idfunc[A])}.\]
  But this is the fiber of $(\blank\circ f)$ over $\idfunc[A]$, and so
  by \cref{thm:equiv-compose-equiv,thm:equiv-iso-adj,thm:contr-hae}, it is contractible.
  Similarly, $\rinv(f)$ is equivalent to the fiber of $(f\circ \blank)$ over $\idfunc[B]$ and hence contractible.
\end{proof}

Next we define the types which put together the other homotopy with the additional coherence datum.\index{coherence}%

\begin{defn}\label{defn:lcoh-rcoh}
For $f : A \to B$, a left inverse $(g,\eta) : \linv(f)$, and a right inverse $(g,\epsilon) : \rinv(f)$, we denote
\begin{align*}
\lcoh{f}{g}{\eta} & \defeq \sm{\epsilon : f\circ g \htpy \idfunc[B]} \prd{y:B} g(\epsilon y) = \eta (gy), \\
\rcoh{f}{g}{\epsilon} & \defeq \sm{\eta : g\circ f \htpy \idfunc[A]} \prd{x:A} f(\eta x) = \epsilon (fx).
\end{align*}
\end{defn}

\begin{lem}\label{lem:coh-hfib}
For any $f,g,\epsilon,\eta$, we have
\begin{align*}
\lcoh{f}{g}{\eta} & \eqvsym {\prd{y:B} \id[\hfib{g}{gy}]{(fgy,\eta(gy))}{(y,\refl{gy})}}, \\
\rcoh{f}{g}{\epsilon} & \eqvsym {\prd{x:A} \id[\hfib{f}{fx}]{(gfx,\epsilon(fx))}{(x,\refl{fx})}}.
\end{align*}
\end{lem}
\begin{proof}
Using \cref{lem:hfib}.
\end{proof}

\begin{lem}\label{lem:coh-hprop}
  If $f$ is a half adjoint equivalence, then for any $(g,\epsilon) : \rinv(f)$, the type $\rcoh{f}{g}{\epsilon}$ is contractible.
\end{lem}
\begin{proof}
  By \cref{lem:coh-hfib} and the fact that dependent function types preserve contractible spaces, it suffices to show that for each $x:A$, the type $\id[\hfib{f}{fx}]{(gfx,\epsilon(fx))}{(x,\refl{fx})}$ is contractible.
  But by \cref{thm:contr-hae}, $\hfib{f}{fx}$ is contractible, and any path space of a contractible space is itself contractible.
\end{proof}

\begin{thm}\label{thm:hae-hprop}
  For any $f : A \to B$, the type $\ishae(f)$ is a mere proposition.
\end{thm}
\begin{proof}
  By \cref{ex:prop-inhabcontr} it suffices to assume $f$ to be a half adjoint equivalence and show that $\ishae(f)$ is contractible.
  Now by associativity of $\Sigma$ (\cref{ex:sigma-assoc}), the type $\ishae(f)$ is equivalent to
  \[\sm{u : \rinv(f)} \rcoh{f}{\proj{1}(u)}{\proj{2}(u)}.\]
  But by \cref{lem:inv-hprop,lem:coh-hprop} and the fact that $\Sigma$ preserves contractibility, the latter type is also contractible.
\end{proof}

Thus, we have shown that $\ishae(f)$ has all three desiderata for the type $\isequiv(f)$.
In the next two sections we consider a couple of other possibilities.

\index{equivalence!half adjoint|)}%
\index{half adjoint equivalence|)}%
\index{adjoint!equivalence!of types, half|)}%

\section{Bi-invertible maps}
\label{sec:biinv}

\index{function!bi-invertible|(defstyle}%
\index{bi-invertible function|(defstyle}%
\index{equivalence!as bi-invertible function|(defstyle}%

Using the language introduced in \cref{sec:hae}, we can restate the definition proposed in \cref{sec:basics-equivalences} as follows.

\begin{defn}\label{defn:biinv}
  We say $f:A\to B$ is \define{bi-invertible}
  if it has both a left inverse and a right inverse:
  \[ \biinv (f) \defeq \linv(f) \times \rinv(f). \]
\end{defn}

In \cref{sec:basics-equivalences} we proved that $\qinv(f)\to\biinv(f)$ and $\biinv(f)\to\qinv(f)$.
What remains is the following.

\begin{thm}\label{thm:isprop-biinv}
  For any $f:A\to B$, the type $\biinv(f)$ is a mere proposition.
\end{thm}
\begin{proof}
  We may suppose $f$ to be bi-invertible and show that $\biinv(f)$ is contractible.
  But since $\biinv(f)\to\qinv(f)$, by \cref{lem:inv-hprop} in this case both $\linv(f)$ and $\rinv(f)$ are contractible, and the product of contractible types is contractible.
\end{proof}

Note that this also fits the proposal made at the beginning of \cref{sec:hae}: we combine $g$ and $\eta$ into a contractible type and add an additional datum which combines with $\epsilon$ into a contractible type.
The difference is that instead of adding a \emph{higher} datum (a 2-dimensional path) to combine with $\epsilon$, we add a \emph{lower} one (a right inverse that is separate from the left inverse).

\begin{cor}\label{thm:equiv-biinv-isequiv}
  For any $f:A\to B$ we have $\eqv{\biinv(f)}{\ishae(f)}$.
\end{cor}
\begin{proof}
  We have $\biinv(f) \to \qinv(f) \to \ishae(f)$ and $\ishae(f) \to \qinv(f) \to \biinv(f)$.
  Since both $\ishae(f)$ and $\biinv(f)$ are mere propositions, the equivalence follows from \cref{lem:equiv-iff-hprop}.
\end{proof}

\index{function!bi-invertible|)}%
\index{bi-invertible function|)}%
\index{equivalence!as bi-invertible function|)}%

\section{Contractible fibers}
\label{sec:contrf}

\index{function!contractible|(defstyle}%
\index{contractible!function|(defstyle}%
\index{equivalence!as contractible function|(defstyle}%

Note that our proofs about $\ishae(f)$ and $\biinv(f)$ made essential use of the fact that the fibers of an equivalence are contractible.
In fact, it turns out that this property is itself a sufficient definition of equivalence.

\begin{defn}[Contractible maps] \label{defn:equivalence}
  A map $f:A\to B$ is \define{contractible}
  if for all $y:B$, the fiber $\hfib f y$ is contractible.
\end{defn}

Thus, the type $\iscontr(f)$ is defined to be
\begin{align}
  \iscontr(f) &\defeq \prd{y:B} \iscontr(\hfib f y)\label{eq:iscontrf}
  % \\
  % &\defeq \prd{y:B} \iscontr (\setof{x:A | f(x) = y}).
\end{align}
Note that in \cref{sec:contractibility} we defined what it means for a \emph{type} to be contractible.
Here we are defining what it means for a \emph{map} to be contractible.
Our terminology follows the general homotopy-theoretic practice of saying that a map has a certain property if all of its (homotopy) fibers have that property.
Thus, a type $A$ is contractible just when the map $A\to\unit$ is contractible.
From \cref{cha:hlevels} onwards we will also call contractible maps and types \emph{$(-2)$-truncated}.

We have already shown in \cref{thm:contr-hae} that $\ishae(f) \to \iscontr(f)$.
Conversely:

\begin{thm}\label{thm:lequiv-contr-hae}
For any $f:A\to B$ we have ${\iscontr(f)} \to {\ishae(f)}$.
\end{thm}
\begin{proof}
Let $P : \iscontr(f)$. We define an inverse mapping $g : B \to A$ by sending each $y : B$ to the center of contraction of the fiber at $y$:
\[ g(y) \defeq \proj{1}(\proj{1}(Py)). \]
We can thus define the homotopy $\epsilon$ by mapping $y$ to the witness that $g(y)$ indeed belongs to the fiber at $y$:
\[ \epsilon(y) \defeq \proj{2}(\proj{1}(P y)). \]
It remains to define $\eta$ and $\tau$. This of course amounts to giving an element of $\rcoh{f}{g}{\epsilon}$. By \cref{lem:coh-hfib}, this is the same as giving for each $x:A$ a path from $(gfx,\epsilon(fx))$ to $(x,\refl{fx})$ in the fiber of $f$ over $fx$. But this is easy: for any $x : A$, the type $\hfib{f}{fx}$
is contractible by assumption, hence such a path must exist. We can construct it explicitly as
\[\opp{\big(\proj{2}(P(fx))(gfx,\epsilon(fx))\big)} \ct \big(\proj{2}(P(fx)) (x,\refl{fx})\big). \qedhere \]
\end{proof}

It is also easy to see:

\begin{lem}\label{thm:contr-hprop}
  For any $f$, the type $\iscontr(f)$ is a mere proposition.
\end{lem}
\begin{proof}
  By \cref{thm:isprop-iscontr}, each type $\iscontr (\hfib f y)$ is a mere proposition.
  Thus, by \cref{thm:isprop-forall}, so is~\eqref{eq:iscontrf}.
\end{proof}

\begin{thm}\label{thm:equiv-contr-hae}
  For any $f:A\to B$ we have $\eqv{\iscontr(f)}{\ishae(f)}$.
\end{thm}
\begin{proof}
  We have already established a logical equivalence ${\iscontr(f)} \Leftrightarrow {\ishae(f)}$, and both are mere propositions (\cref{thm:contr-hprop,thm:hae-hprop}).
  Thus, \cref{lem:equiv-iff-hprop} applies.
\end{proof}

Usually, we prove that a function is an equivalence by exhibiting a quasi-inverse, but sometimes this definition is more convenient.
For instance, it implies that when proving a function to be an equivalence, we are free to assume that its codomain is inhabited.

\begin{cor}\label{thm:equiv-inhabcod}
  If $f:A\to B$ is such that $B\to \isequiv(f)$, then $f$ is an equivalence.
\end{cor}
\begin{proof}
  To show $f$ is an equivalence, it suffices to show that $\hfib f y$ is contractible for any $y:B$.
  But if $e:B\to \isequiv(f)$, then given any such $y$ we have $e(y):\isequiv(f)$, so that $f$ is an equivalence and hence $\hfib f y$ is contractible, as desired.
\end{proof}

\index{function!contractible|)}%
\index{contractible!function|)}%
\index{equivalence!as contractible function|)}%

\section{On the definition of equivalences}
\label{sec:concluding-remarks}

\indexdef{equivalence}
We have shown that all three definitions of equivalence satisfy the three desirable properties and are pairwise equivalent:
\[ \iscontr(f) \eqvsym \ishae(f) \eqvsym \biinv(f). \]
(There are yet more possible definitions of equivalence, but we will stop with these three.
See \cref{ex:brck-qinv} and the exercises in this chapter for some more.)
Thus, we may choose any one of them as ``the'' definition of $\isequiv (f)$.
For definiteness, we choose to define
\[ \isequiv(f) \defeq \ishae(f).\]
\index{mathematics!formalized}%
This choice is advantageous for formalization, since $\ishae(f)$ contains the most directly useful data.
On the other hand, for other purposes, $\biinv(f)$ is often easier to deal with, since it contains no 2-dimensional paths and its two symmetrical halves can be treated independently.
However, for purposes of this book, the specific choice will make little difference.

In the rest of this chapter, we study some other properties and characterizations of equivalences.
\index{equivalence!properties of}%


\section{Surjections and embeddings}
\label{sec:mono-surj}

\index{set}
When $A$ and $B$ are sets and $f:A\to B$ is an equivalence, we also call it as \define{isomorphism}
\indexdef{isomorphism!of sets}%
or a \define{bijection}.
\indexdef{bijection}%
\indexsee{function!bijective}{bijection}%
(We avoid these words for types that are not sets, since in homotopy theory and higher category theory they often denote a stricter notion of ``sameness'' than homotopy equivalence.)
In set theory, a function is a bijection just when it is both injective and surjective.
The same is true in type theory, if we formulate these conditions appropriately.
For clarity, when dealing with types that are not sets, we will speak of \emph{embeddings} instead of injections.

\begin{defn}\label{defn:surj-emb}
  Let $f:A\to B$.
  \begin{enumerate}
  \item We say $f$ is \define{surjective}
    \indexsee{surjective!function}{function, surjective}%
    \indexdef{function!surjective}%
    (or a \define{surjection})
    \indexsee{surjection}{function, surjective}%
    if for every $b:B$ we have $\brck{\hfib f b}$.
  \item We say $f$ is an \define{embedding}
    \indexdef{function!embedding}%
    \indexsee{embedding}{function, embedding}%
    if for every $x,y:A$ the function $\apfunc f : (\id[A]xy) \to (\id[B]{f(x)}{f(y)})$ is an equivalence.
  \end{enumerate}
\end{defn}

In other words, $f$ is surjective if every fiber of $f$ is merely inhabited, or equivalently if for all $b:B$ there merely exists an $a:A$ such that $f(a)=b$.
In traditional logical notation, $f$ is surjective if $\fall{b:B}\exis{a:A} (f(a)=b)$.
This must be distinguished from the stronger assertion that $\prd{b:B}\sm{a:A} (f(a)=b)$; if this holds we say that $f$ is a \define{split surjection}.
\indexsee{split!surjection}{function, split surjective}%
\indexsee{surjection!split}{function, split surjective}%
\indexsee{surjective!function!split}{function, split surjective}%
\indexdef{function!split surjective}%
(Since this latter type is equivalent to $\sm{g:B\to A}\prd{b:B} (f(g(b))=b)$, being a split surjection is the same as being a \emph{retraction} as defined in \cref{sec:contractibility}.)
\index{retraction}%
\index{function!retraction}%

The axiom of choice from \cref{sec:axiom-choice} says exactly that every surjection \emph{between sets} is split.
However, in the presence of the univalence axiom, it is simply false that \emph{all} surjections are split.
In \cref{thm:no-higher-ac} we constructed a type family $Y:X\to \type$ such that $\prd{x:X} \brck{Y(x)}$ but $\neg \prd{x:X} Y(x)$;
for any such family, the first projection $(\sm{x:X} Y(x)) \to X$ is a surjection that is not split.

If $A$ and $B$ are sets, then by \cref{lem:equiv-iff-hprop}, $f$ is an embedding just when
\begin{equation}
  \prd{x,y:A} (\id[B]{f(x)}{f(y)}) \to (\id[A]xy).\label{eq:injective}
\end{equation}
In this case we say that $f$ is \define{injective},
\indexsee{injective function}{function, injective}%
\indexdef{function!injective}%
or an \define{injection}.
\indexsee{injection}{function, injective}%
We avoid these word for types that are not sets, because they might be interpreted as~\eqref{eq:injective}, which is an ill-behaved notion for non-sets.
It is also true that any function between sets is surjective if and only if it is an \emph{epimorphism} in a suitable sense, but this also fails for more general types, and surjectivity is generally the more important notion.

\begin{thm}\label{thm:mono-surj-equiv}
  A function $f:A\to B$ is an equivalence if and only if it is both surjective and an embedding.
\end{thm}
\begin{proof}
  If $f$ is an equivalence, then each $\hfib f b$ is contractible, hence so is $\brck{\hfib f b}$, so $f$ is surjective.
  And we showed in \cref{thm:paths-respects-equiv} that any equivalence is an embedding.

  Conversely, suppose $f$ is a surjective embedding.
  Let $b:B$; we show that $\sm{x:A}(f(x)=b)$ is contractible.
  Since $f$ is surjective, there merely exists an $a:A$ such that $f(a)=b$.
  Thus, the fiber of $f$ over $b$ is inhabited; it remains to show it is a mere proposition.
  For this, suppose given $x,y:A$ with $p:f(x)=b$ and $q:f(y)=b$.
  Then since $\apfunc f$ is an equivalence, there exists $r:x=y$ with $\apfunc f (r) = p \ct \opp q$.
  However, using the characterization of paths in $\Sigma$-types, the latter equality rearranges to $\trans{r}{p} = q$.
  Thus, together with $r$ it exhibits $(x,p) = (y,q)$ in the fiber of $f$ over $b$.
\end{proof}

\begin{cor}
  For any $f:A\to B$ we have
  \[ \isequiv(f) \eqvsym (\mathsf{isEmbedding}(f) \times \mathsf{isSurjective}(f)).\]
\end{cor}
\begin{proof}
  Being a surjection and an embedding are both mere propositions; now apply \cref{lem:equiv-iff-hprop}.
\end{proof}

Of course, this cannot be used as a definition of ``equivalence'', since the definition of embeddings refers to equivalences.
However, this characterization can still be useful; see \cref{sec:whitehead}.
We will generalize it in \cref{cha:hlevels}.


% \section{Fiberwise equivalences}
\section{Closure properties of equivalences}
\label{sec:equiv-closures}
\label{sec:fiberwise-equivalences}
\index{equivalence!properties of}%


% We end this chapter by observing some important closure properties of equivalences.
We have already seen in \cref{thm:equiv-eqrel} that equivalences are closed under composition.
Furthermore, we have:

\begin{thm}[The 2-out-of-3 property]\label{thm:two-out-of-three}
  \index{2-out-of-3 property}%
  Suppose $f:A\to B$ and $g:B\to C$.
  If any two of $f$, $g$, and $g\circ f$ are equivalences, so is the third.
\end{thm}
\begin{proof}
  If $g\circ f$ and $g$ are equivalences, then $\opp{(g\circ f)} \circ g$ is a quasi-inverse to $f$.
  On the one hand, we have $\opp{(g\circ f)} \circ g \circ f \htpy \idfunc[A]$, while on the other we have
  \begin{align*}
    f \circ \opp{(g\circ f)} \circ g
    &\htpy \opp g \circ g \circ f \circ \opp{(g\circ f)} \circ g\\
    &\htpy \opp g \circ g\\
    &\htpy \idfunc[B].
  \end{align*}
  Similarly, if $g\circ f$ and $f$ are equivalences, then $f\circ \opp{(g\circ f)}$ is a quasi-inverse to $g$.
\end{proof}

This is a standard closure condition on equivalences from homotopy theory.
Also well-known is that they are closed under retracts, in the following sense.

\index{retract!of a function|(defstyle}%

\begin{defn}\label{defn:retract}
A function $g:A\to B$ is said to be a \define{retract}
of a function $f:X\to Y$ if there is a diagram
\begin{equation*}
  \xymatrix{
    {A} \ar[r]^{s} \ar[d]_{g}
    &
    {X} \ar[r]^{r} \ar[d]_{f}
    &
    {A} \ar[d]^{g}
    \\
    {B} \ar[r]_{s'}
    &
    {Y} \ar[r]_{r'}
    &
    {B}
  }
\end{equation*}
for which there are
\begin{enumerate}
\item a homotopy $R:r\circ s \htpy \idfunc[A]$.
\item a homotopy $R':r'\circ s' \htpy\idfunc[B]$.
\item a homotopy $L:f\circ s\htpy s'\circ g$.
\item a homotopy $K:g\circ r\htpy r'\circ f$.
\item for every $a:A$, a path $H(a)$ witnessing the commutativity of the square
\begin{equation*}
  \xymatrix@C=3pc{
    {g(r(s(a)))} \ar@{=}[r]^-{K(s(a))} \ar@{=}[d]_{\ap g{R(a)}}
    &
    {r'(f(s(a)))} \ar@{=}[d]^{\ap{r'}{L(a)}}
    \\
    {g(a)} \ar@{=}[r]_-{\opp{R'(g(a))}}
    &
    {r'(s'(g(a)))}
  }
\end{equation*}
\end{enumerate}
\end{defn}

Recall that in \cref{sec:contractibility} we defined what it means for a type to be a retract of another.
This is a special case of the above definition where $B$ and $Y$ are $\unit$.
Conversely, just as with contractibility, retractions of maps induce retractions of their fibers.

\begin{lem}\label{lem:func_retract_to_fiber_retract}
If a function $g:A\to B$ is a retract of a function $f:X\to Y$, then $\hfib{g}b$ is a retract of $\hfib{f}{s'(b)}$
for every $b:B$, where $s':B\to Y$ is as in \cref{defn:retract}.
\end{lem}

\begin{proof}
Suppose that $g:A\to B$ is a retract of $f:X\to Y$. Then for any $b:B$ we have the functions
\begin{align*}
\varphi_b &:\hfiber{g}b\to\hfib{f}{s'(b)}, &
\varphi_b(a,p) & \defeq \pairr{s(a),L(a)\ct s'(p)},\\
\psi_b &:\hfib{f}{s'(b)}\to\hfib{g}b, &
\psi_b(x,q) &\defeq \pairr{r(x),K(x)\ct r'(q)\ct R'(b)}.
\end{align*}
Then we have $\psi_b(\varphi_b({a,p}))\equiv\pairr{r(s(a)),K(s(a))\ct r'(L(a)\ct s'(p))\ct R'(b)}$.
We claim $\psi_b$ is a retraction with section $\varphi_b$ for all $b:B$, which is to say that for all $(a,p):\hfib g b$ we have $\psi_b(\varphi_b({a,p}))= \pairr{a,p}$.
In other words, we want to show
\begin{equation*}
\prd{b:B}{a:A}{p:g(a)=b} \psi_b(\varphi_b({a,p}))= \pairr{a,p}.
\end{equation*}
By reordering the first two $\Pi$s and applying a version of \cref{thm:omit-contr}, this is equivalent to
\begin{equation*}
\prd{a:A}\psi_{g(a)}(\varphi_{g(a)}({a,\refl{g(a)}}))=\pairr{a,\refl{g(a)}}.
\end{equation*}
For any $a$, by \cref{thm:path-sigma}, this equality of pairs is equivalent to a pair of equalities. The first components are equal by $R(a):r(s(a))= a$, so we need only show
\begin{equation*}
\trans{R(a)}{K(s(a))\ct r'(L(a))\ct R'(g(a))} = \refl{g(a)}.
\end{equation*}
But this transportation computes as $\opp{g(R(a))}\ct K(s(a))\ct r'(L(a))\ct R'(g(a))$, so the required path is given by $H(a)$.
\end{proof}

\begin{thm}\label{thm:retract-equiv}
  If $g$ is a retract of an equivalence $f$, then $g$ is also an equivalence.
\end{thm}
\begin{proof}
  By \cref{lem:func_retract_to_fiber_retract}, every fiber of $g$ is a retract of a fiber of $f$.
  Thus, by \cref{thm:retract-contr}, if the latter are all contractible, so are the former.
\end{proof}

\index{retract!of a function|)}%

\index{fibration}%
\index{total!space}%
Finally, we show that fiberwise equivalences can be characterized in terms of equivalences of total spaces.
To explain the terminology, recall from \cref{sec:fibrations} that a type family $P:A\to\type$ can be viewed as a fibration over $A$ with total space $\sm{x:A} P(x)$, the fibration being the projection $\proj1:\sm{x:A} P(x) \to A$.
From this point of view, given two type families $P,Q:A\to\type$, we may refer to a function $f:\prd{x:A} (P(x)\to Q(x))$ as a \define{fiberwise map} or a \define{fiberwise transformation}.
\indexsee{transformation!fiberwise}{fiberwise transformation}%
\indexsee{function!fiberwise}{fiberwise transformation}%
\index{fiberwise!transformation|(defstyle}%
\indexsee{fiberwise!map}{fiberwise transformation}%
\indexsee{map!fiberwise}{fiberwise transformation}
Such a map induces a function on total spaces:

\begin{defn}\label{defn:total-map}
  Given type families $P,Q:A\to\type$ and a map $f:\prd{x:A} P(x)\to Q(x)$, we define
  \begin{equation*}
    \total f  \defeq \lam{w}\pairr{\proj{1}w,f(\proj{1}w,\proj{2}w)} : \sm{x:A}P(x)\to\sm{x:A}Q(x).
  \end{equation*}
\end{defn}

\begin{thm}\label{fibwise-fiber-total-fiber-equiv}
Suppose that $f$ is a fiberwise transformation between families $P$ and
$Q$ over a type $A$ and let $x:A$ and $v:Q(x)$. Then we have an equivalence
\begin{equation*}
\eqv{\hfib{\total{f}}{\pairr{x,v}}}{\hfib{f(x)}{v}}.
\end{equation*}
\end{thm}
\begin{proof}
  We calculate:
\begin{align}
  \hfib{\total{f}}{\pairr{x,v}}
  & \jdeq \sm{w:\sm{x:A}P(x)}\pairr{\proj{1}w,f(\proj{1}w,\proj{2}w)}=\pairr{x,v}
  \notag \\
  & \eqv{}{} \sm{a:A}{u:P(a)}\pairr{a,f(a,u)}=\pairr{x,v}
  \tag{by~\cref{ex:sigma-assoc}} \\
  & \eqv{}{} \sm{a:A}{u:P(a)}{p:a=x}\trans{p}{f(a,u)}=v
  \tag{by \cref{thm:path-sigma}} \\
  & \eqv{}{} \sm{a:A}{p:a=x}{u:P(a)}\trans{p}{f(a,u)}=v
  \notag \\
  & \eqv{}{} \sm{u:P(x)}f(x,u)=v
  \tag{$*$}\label{eq:uses-sum-over-paths} \\
  & \jdeq \hfib{f(x)}{v}. \notag
\end{align}
The equivalence~\eqref{eq:uses-sum-over-paths} follows from \cref{thm:omit-contr,thm:contr-paths,ex:sigma-assoc}.
\end{proof}

We say that a fiberwise transformation $f:\prd{x:A} P(x)\to Q(x)$ is a \define{fiberwise equivalence}%
\indexdef{fiberwise!equivalence}%
\indexdef{equivalence!fiberwise}
if each $f(x):P(x) \to Q(x)$ is an equivalence.

\begin{thm}\label{thm:total-fiber-equiv}
Suppose that $f$ is a fiberwise transformation between families
$P$ and $Q$ over a type $A$.
Then $f$ is a fiberwise equivalence if and only if $\total{f}$ is an equivalence.
\end{thm}

\begin{proof}
Let $f$, $P$, $Q$ and $A$ be as in the statement of the theorem.
By \cref{fibwise-fiber-total-fiber-equiv} it follows for all
$x:A$ and $v:Q(x)$ that
$\hfib{\total{f}}{\pairr{x,v}}$ is contractible if and only if
$\hfib{f(x)}{v}$ is contractible.
Thus, $\hfib{\total{f}}{w}$ is contractible for all $w:\sm{x:A}Q(x)$ if and only if $\hfib{f(x)}{v}$ is contractible for all $x:A$ and $v:Q(x)$.
\end{proof}

\index{fiberwise!transformation|)}%


\section{The object classifier}
\label{sec:object-classification}

In type theory we have a basic notion of \emph{family of types}, namely a function $B:A\to\type$.
We have seen that such families behave somewhat like \emph{fibrations} in homotopy theory, with the fibration being the projection $\proj1:\sm{a:A} B(a) \to A$.
A basic fact in homotopy theory is that every map is equivalent to a fibration.
With univalence at our disposal, we can prove the same thing in type theory.

\begin{lem}\label{thm:fiber-of-a-fibration}
  For any type family $B:A\to\type$, the fiber of $\proj1:\sm{x:A} B(x) \to A$ over $a:A$ is equivalent to $B(a)$:
  \[ \eqv{\hfib{\proj1}{a}}{B(a)} \]
\end{lem}
\begin{proof}
  We have
  \begin{align*}
    \hfib{\proj1}{a} &\defeq \sm{u:\sm{x:A} B(x)} \proj1(u)=a\\
    &\eqvsym \sm{x:A}{b:B(x)} (x=a)\\
    &\eqvsym \sm{x:A}{p:x=a} B(x)\\
    &\eqvsym B(a)
  \end{align*}
  using the left universal property of identity types.
\end{proof}

\begin{lem}\label{thm:total-space-of-the-fibers}
  For any function $f:A\to B$, we have $\eqv{A}{\sm{b:B}\hfib{f}{b}}$.
\end{lem}
\begin{proof}
  We have
  \begin{align*}
    \sm{b:B}\hfib{f}{b} &\defeq \sm{b:B}{a:A} (f(a)=b)\\
    &\eqvsym \sm{a:A}{b:B} (f(a)=b)\\
    &\eqvsym A
  \end{align*}
  using the fact that $\sm{b:B} (f(a)=b)$ is contractible.
\end{proof}

\begin{thm}\label{thm:nobject-classifier-appetizer}
For any type $B$ there is an equivalence
\begin{equation*}
\chi:\Parens{\sm{A:\type} (A\to B)}\eqvsym (B\to\type).
\end{equation*}
\end{thm}
\begin{proof}
We have to construct quasi-inverses
\begin{align*}
\chi & : \Parens{\sm{A:\type} (A\to B)}\to B\to\type\\
\psi & : (B\to\type)\to\Parens{\sm{A:\type} (A\to B)}.
\end{align*}
We define $\chi$ by $\chi((A,f),b)\defeq\hfiber{f}b$, and $\psi$ by $\psi(P)\defeq\Pairr{(\sm{b:B} P(b)),\proj1}$.
Now we have to verify that $\chi\circ\psi\htpy\idfunc{}$ and that $\psi\circ\chi \htpy\idfunc{}$.
\begin{enumerate}
\item Let $P:B\to\type$.
  By \cref{thm:fiber-of-a-fibration},
$\hfiber{\proj1}{b}\eqvsym P(b)$ for any $b:B$, so it follows immediately
that $P\htpy\chi(\psi(P))$.
\item Let $f:A\to B$ be a function. We have to find a path
\begin{equation*}
\Pairr{\tsm{b:B} \hfiber{f}b,\,\proj1}=\pairr{A,f}.
\end{equation*}
First note that by \cref{thm:total-space-of-the-fibers}, we have
$e:\sm{b:B} \hfiber{f}b\eqvsym A$ with $e(b,a,p)\defeq a$ and $e^{-1}(a)
\defeq(f(a),a,\refl{f(a)})$.
By \cref{thm:path-sigma}, it remains to show $\trans{(\ua(e))}{\proj1} = f$.
But by the computation rule for univalence and~\eqref{eq:transport-arrow}, we have $\trans{(\ua(e))}{\proj1} = \proj1\circ e^{-1}$, and the definition of $e^{-1}$ immediately yields $\proj1 \circ e^{-1} \jdeq f$.\qedhere
\end{enumerate}
\end{proof}

\noindent
\indexdef{object!classifier}%
\indexdef{classifier!object}%
\index{.infinity1-topos@$(\infty,1)$-topos}%
In particular, this implies that we have an \emph{object classifier} in the sense of higher topos theory.
Recall from \cref{def:pointedtype} that $\pointed\type$ denotes the type $\sm{A:\type} A$ of pointed types.

\begin{thm}\label{thm:object-classifier}
Let $f:A\to B$ be a function. Then the diagram
\begin{equation*}
  \vcenter{\xymatrix{
      A\ar[r]^-{\vartheta_f} \ar[d]_{f} &
      \pointed{\type}\ar[d]^{\proj1}\\
      B\ar[r]_{\chi_f} &
      \type
      }}
\end{equation*}
is a pullback\index{pullback} square (see \cref{ex:pullback}).
Here the function $\vartheta_f$ is defined by
\begin{equation*}
 \lam{a} \pairr{\hfiber{f}{f(a)},\pairr{a,\refl{f(a)}}}.
\end{equation*}
\end{thm}
\begin{proof}
Note that we have the equivalences
\begin{align*}
A & \eqvsym \sm{b:B} \hfiber{f}b\\
& \eqvsym \sm{b:B}{X:\type}{p:\hfiber{f}b= X} X\\
& \eqvsym \sm{b:B}{X:\type}{x:X} \hfiber{f}b= X\\
& \eqvsym \sm{b:B}{Y:\pointed{\type}} \hfiber{f}b = \proj1 Y\\
& \jdeq B\times_{\type}\pointed{\type}
\end{align*}
which gives us a composite equivalence $e:A\eqvsym B\times_\type\pointed{\type}$.
We may display the action of this composite equivalence step by step by
\begin{align*}
a & \mapsto \pairr{f(a),\; \pairr{a,\refl{f(a)}}}\\
& \mapsto \pairr{f(a), \; \hfiber{f}{f(a)}, \; \refl{\hfiber{f}{f(a)}}, \; \pairr{a,\refl{f(a)}}}\\
& \mapsto \pairr{f(a), \; \hfiber{f}{f(a)}, \; \pairr{a,\refl{f(a)}}, \; \refl{\hfiber{f}{f(a)}}}\\
& \mapsto \pairr{f(a), \; \pairr{\hfiber{f}{f(a)}, \; \pairr{a,\refl{f(a)}}}, \; \refl{\hfiber{f}{f(a)}}}.
\end{align*}
Therefore, we get homotopies $f\htpy\proj1\circ e$ and $\vartheta_f\htpy \proj2\circ e$.
\end{proof}



\section{Univalence implies function extensionality}
\label{sec:univalence-implies-funext}

\index{function extensionality!proof from univalence}%
In the last section of this chapter we include a proof that the univalence axiom implies function
extensionality. Thus, in this section we work \emph{without} the function extensionality axiom.
The proof consists of two steps. First we show
in \cref{uatowfe} that the univalence
axiom implies a weak form of function extensionality, defined in \cref{weakfunext} below. The
principle of weak function extensionality in turn implies the usual function extensionality,
and it does so without the univalence axiom (\cref{wfetofe}).

\index{univalence axiom}%
Let $\type$ be a universe; we will explicitly indicate where we assume that it is univalent.

\begin{defn}\label{weakfunext}
The \define{weak function extensionality principle}
\indexdef{function extensionality!weak}%
asserts that there is a function
\begin{equation*}
\Parens{\prd{x:A}\iscontr(P(x))} \to\iscontr\Parens{\prd{x:A}P(x)}
\end{equation*}
for any family $P:A\to\type$ of types over any type $A$.
\end{defn}

The following lemma is easy to prove using function extensionality; the point here is that it also follows from univalence without assuming function extensionality separately.

\begin{lem} \label{UA-eqv-hom-eqv}
Assuming $\type$ is univalent, for any $A,B,X:\type$ and any $e:\eqv{A}{B}$, there is an equivalence
\begin{equation*}
\eqv{(X\to A)}{(X\to B)}
\end{equation*}
of which the underlying map is given by post-composition with the underlying function of $e$.
\end{lem}

\begin{proof}
  % Immediate by induction on $\eqv{}{}$ (see \cref{thm:equiv-induction}).
  As in the proof of \cref{lem:qinv-autohtpy}, we may assume that $e = \idtoeqv(p)$ for some $p:A=B$.
  Then by path induction, we may assume $p$ is $\refl{A}$, so that $e = \idfunc[A]$.
  But in this case, post-composition with $e$ is the identity, hence an equivalence.
\end{proof}

\begin{cor}\label{contrfamtotalpostcompequiv}
Let $P:A\to\type$ be a family of contractible types, i.e.\ \narrowequation{\prd{x:A}\iscontr(P(x)).}
Then the projection $\proj{1}:(\sm{x:A}P(x))\to A$ is an equivalence. Assuming $\type$ is univalent, it follows immediately that post-composition with $\proj{1}$ gives an equivalence
\begin{equation*}
\alpha : \eqv{\Parens{A\to\sm{x:A}P(x)}}{(A\to A)}.
\end{equation*}
\end{cor}

\begin{proof}
  By \cref{thm:fiber-of-a-fibration}, for $\proj{1}:(\sm{x:A}P(x))\to A$ and $x:A$ we have an equivalence
  \begin{equation*}
    \eqv{\hfiber{\proj{1}}{x}}{P(x)}.
  \end{equation*}
  Therefore $\proj{1}$ is an equivalence whenever each $P(x)$ is contractible. The assertion is now a consequence of  \cref{UA-eqv-hom-eqv}.
\end{proof}

In particular, the homotopy fiber of the above equivalence at $\idfunc[A]$ is contractible. Therefore, we can show that univalence implies weak function extensionality by showing that the dependent function type $\prd{x:A}P(x)$ is a retract of $\hfiber{\alpha}{\idfunc[A]}$.

\begin{thm}\label{uatowfe}
In a univalent universe $\type$, suppose that $P:A\to\type$ is a family of contractible types
and let $\alpha$ be the function of \cref{contrfamtotalpostcompequiv}.
Then $\prd{x:A}P(x)$ is a retract of $\hfiber{\alpha}{\idfunc[A]}$. As a consequence, $\prd{x:A}P(x)$ is contractible. In other words, the univalence axiom implies the weak function extensionality principle.
\end{thm}

\begin{proof}
Define the functions
\begin{align*}
  \varphi &: (\tprd{x:A}P(x))\to\hfiber{\alpha}{\idfunc[A]},\\
  \varphi(f) &\defeq (\lam{x} (x,f(x)),\refl{\idfunc[A]}),
\intertext{and}
  \psi &: \hfiber{\alpha}{\idfunc[A]}\to \tprd{x:A}P(x), \\
  \psi(g,p) &\defeq \lam{x} \trans {\happly (p,x)}{\proj{2} (g(x))}.
\end{align*}
Then $\psi(\varphi(f))=\lam{x} f(x)$, which is $f$, by the uniqueness principle for dependent function types.
\end{proof}

We now show that weak function extensionality implies the usual function extensionality.
Recall from~\eqref{eq:happly} the function $\happly (f,g) : (f = g)\to(f\htpy g)$ which
converts equality of functions to homotopy. In the proof that follows, the univalence
axiom is not used.

\begin{thm}\label{wfetofe}
  \index{function extensionality}%
Weak function extensionality implies the function extensionality \cref{axiom:funext}.
\end{thm}

\begin{proof}
We want to show that
\begin{equation*}
\prd{A:\type}{P:A\to\type}{f,g:\prd{x:A}P(x)}\isequiv(\happly (f,g)).
\end{equation*}
Since a fiberwise map induces an equivalence on total spaces if and only if it is fiberwise an equivalence by \cref{thm:total-fiber-equiv}, it suffices to show that the function of type
\begin{equation*}
\Parens{\sm{g:\prd{x:A}P(x)}(f= g)} \to \sm{g:\prd{x:A}P(x)}(f\htpy g)
\end{equation*}
induced by $\lam{g:\prd{x:A}P(x)} \happly (f,g)$ is an equivalence.
Since the type on the left is contractible by \cref{thm:contr-paths}, it suffices to show that the type on the right:
\begin{equation}\label{eq:uatofesp}
\sm{g:\prd{x:A}P(x)}\prd{x:A}f(x)= g(x)
\end{equation}
is contractible.
Now \cref{thm:ttac} says that this is equivalent to
\begin{equation}\label{eq:uatofeps}
\prd{x:A}\sm{u:P(x)}f(x)= u.
\end{equation}
The proof of \cref{thm:ttac} uses function extensionality, but only for one of the composites.
Thus, without assuming function extensionality, we can conclude that~\eqref{eq:uatofesp} is a retract\index{retract!of a type} of~\eqref{eq:uatofeps}.
And~\eqref{eq:uatofeps} is a product of contractible types, which is contractible by the weak function extensionality principle; hence~\eqref{eq:uatofesp} is also contractible.
\end{proof}

\sectionNotes

The fact that the space of continuous maps equipped with quasi-inverses has the wrong homotopy type to be the ``space of homotopy equivalences'' is well-known in algebraic topology.
In that context, the ``space of homotopy equivalences'' $(\eqv AB)$ is usually defined simply as the subspace of the function space $(A\to B)$ consisting of the functions that are homotopy equivalences.
In type theory, this would correspond most closely to $\sm{f:A\to B} \brck{\qinv(f)}$; see \cref{ex:brck-qinv}.

The first definition of equivalence given in homotopy type theory was the one that we have called $\iscontr(f)$, which was due to Voevodsky.
The possibility of the other definitions was subsequently observed by various people.
The basic theorems about adjoint equivalences\index{adjoint!equivalence} such as \cref{lem:coh-equiv,thm:equiv-iso-adj} are adaptations of standard facts in higher category theory and homotopy theory.
Using bi-invertibility as a definition of equivalences was suggested by Andr\'e Joyal.

The properties of equivalences discussed in \cref{sec:mono-surj,sec:equiv-closures} are well-known in homotopy theory.
Most of them were first proven in type theory by Voevodsky.

The fact that every function is equivalent to a fibration is a standard fact in homotopy theory.
The notion of object classifier
\index{object!classifier}%
\index{classifier!object}%
in $(\infty,1)$-category
\index{.infinity1-category@$(\infty,1)$-category}%
theory (the categorical analogue of \cref{thm:nobject-classifier-appetizer}) is due to Rezk (see~\cite{Rezk05,lurie:higher-topoi}).

Finally, the fact that univalence implies function extensionality (\cref{sec:univalence-implies-funext}) is due to Voevodsky.
Our proof is a simplification of his.
\cref{ex:funext-from-nondep} is also due to Voevodsky.

\sectionExercises

\begin{ex}\label{ex:two-sided-adjoint-equivalences}
  Consider the type of ``two-sided adjoint equivalence\index{adjoint!equivalence} data'' for $f:A\to B$,
  \begin{narrowmultline*}
    \sm{g:B\to A}{\eta: g \circ f \htpy \idfunc[A]}{\epsilon:f \circ g \htpy \idfunc[B]}
    \narrowbreak
    \Parens{\prd{x:A} \map{f}{\eta x} = \epsilon(fx)} \times
    \Parens{\prd{y:B} \map{g}{\epsilon y} = \eta(gy) }.
  \end{narrowmultline*}
  By \cref{lem:coh-equiv}, we know that if $f$ is an equivalence, then this type is inhabited.
  Give a characterization of this type analogous to \cref{lem:qinv-autohtpy}.

  Can you give an example showing that this type is not generally a mere proposition?
  (This will be easier after \cref{cha:hits}.)
\end{ex}

\begin{ex}\label{ex:symmetric-equiv}
  Show that for any $A,B:\UU$, the following type is equivalent to $\eqv A B$.
  \begin{equation*}
    \sm{R:A\to B\to \type}
    \Parens{\prd{a:A} \iscontr\Parens{\sm{b:B} R(a,b)}} \times
    \Parens{\prd{b:B} \iscontr\Parens{\sm{a:A} R(a,b)}}.
  \end{equation*}
  Can you extract from this a definition of a type satisfying the three desiderata of $\isequiv(f)$?
\end{ex}

\begin{ex} \label{ex:qinv-autohtpy-no-univalence}
  Reformulate the proof of \cref{lem:qinv-autohtpy} without using univalence.
\end{ex}

\begin{ex}[The unstable octahedral axiom]\label{ex:unstable-octahedron}
  \index{axiom!unstable octahedral}%
  \index{octahedral axiom, unstable}%
  Suppose $f:A\to B$ and $g:B\to C$ and $b:B$.
  \begin{enumerate}
  \item Show that there is a natural map $\hfib{g\circ f}{g(b)} \to \hfib{g}{g(b)}$ whose fiber over $(b,\refl{g(b)})$ is equivalent to $\hfib f b$.
  \item Show that $\eqv{\hfib{g\circ f}{c}}{\sm{w:\hfib{g}{c}} \hfib f {\proj1 w}}$.
  \end{enumerate}
\end{ex}

\begin{ex}\label{ex:2-out-of-6}
  \index{2-out-of-6 property}%
  Prove that equivalences satisfy the \emph{2-out-of-6 property}: given $f:A\to B$ and $g:B\to C$ and $h:C\to D$, if $g\circ f$ and $h\circ g$ are equivalences, so are $f$, $g$, $h$, and $h\circ g\circ f$.
  Use this to give a higher-level proof of \cref{thm:paths-respects-equiv}.
\end{ex}

\begin{ex}\label{ex:qinv-univalence}
  For $A,B:\UU$, define
  \[ \mathsf{idtoqinv}_{A,B} :(A=B) \to \sm{f:A\to B}\qinv(f) \]
  by path induction in the obvious way.
  Let \textbf{\textsf{qinv}-univalence} denote the modified form of the univalence axiom which asserts that for all $A,B:\UU$ the function $\mathsf{idtoqinv}_{A,B}$ has a quasi-inverse.
  \begin{enumerate}
  \item Show that \qinv-univalence can be used instead of univalence in the proof of function extensionality in \cref{sec:univalence-implies-funext}.
  \item Show that \qinv-univalence can be used instead of univalence in the proof of \cref{thm:qinv-notprop}.
  \item Show that \qinv-univalence is inconsistent (i.e.\ allows construction of an inhabitant of $\emptyt$).
    Thus, the use of a ``good'' version of $\isequiv$ is essential in the statement of univalence.
  \end{enumerate}
\end{ex}

\begin{ex}\label{ex:embedding-cancellable}
  Show that a function $f:A\to B$ is an embedding if and only if the following two conditions hold:
  \begin{enumerate}
  \item $f$ is \emph{left cancellable}, i.e.\ for any $x,y:A$, if $f(x)=f(y)$ then $x=y$.\label{item:ex:ec1}
  \item For any $x:A$, the map $\apfunc f: \Omega(A,x) \to \Omega(B,f(x))$ is an equivalence.\label{item:ex:ec2}
  \end{enumerate}
  (In particular, if $A$ is a set, then $f$ is an embedding if and only if it is left-cancellable and $\Omega(B,f(x))$ is contractible for all $x:A$.)
  Give examples to show that neither of~\ref{item:ex:ec1} or~\ref{item:ex:ec2} implies the other.
\end{ex}

\begin{ex}\label{ex:cancellable-from-bool}
  Show that the type of left-cancellable functions $\bool\to B$ (see \cref{ex:embedding-cancellable}) is equivalent to $\sm{x,y:B}(x\neq y)$.
  Give a similar explicit characterization of the type of embeddings $\bool\to B$.
\end{ex}

\begin{ex}\label{ex:funext-from-nondep}
  The \textbf{na\"{i}ve non-dependent function extensionality axiom} says that for $A,B:\type$ and $f,g:A\to B$ there is a function $(\prd{x:A} f(x)=g(x)) \to (f=g)$.
  \indexdef{function extensionality!non-dependent}%
  Modify the argument of \cref{sec:univalence-implies-funext} to show that this axiom implies the full function extensionality axiom (\cref{axiom:funext}).
\end{ex}

% Local Variables:
% TeX-master: "hott-online"
% End:

===== END SOURCE CHUNK | EOF=true =====


===== SOURCE HoTT/theory-schema/upstream/book-578b85cc/front.tex | SHA256 784de150ef5e64967618c712fe81f40ac41f6fa0b68f5a02b76ce23a5306b4c4 | LINES 1-168/168 =====
%%%%%%%%%%%%%%%%%%%% Cover page %%%%%%%%%%%%%%%%%%%%

\newgeometry{noheadfoot,bindingoffset=-5pt,top=0pt,bottom=0pt,inner=0pt,outer=0pt}%
\ifOPTcover
\setcounter{page}{-1} % Otherwise we end up having two pages numbered 1
\newlength{\coverheight}
\setlength{\coverheight}{\OPTcoverheight}
\newlength{\coverwidth}
\setlength{\coverwidth}{\OPTcoverwidth}
\input{frontpage}
\ThisLLCornerWallPaper{1.1}{\OPTfrontimage}
\pagecolor{covercolor}
\frontpage
\newpage
% Reset page counter, cover page does not count
\ifpdf
\nopagecolor
\else
\pagecolor{white}
\fi
\cleartooddpage
\else
\fi

%%%%%%%%%%%%%%%%%%%% Bastard page %%%%%%%%%%%%%%%%%%%%
\ifOPTbastard
\cleartooddpage
\hbox{}
\vspace{0.2\textwidth}
{\centering
\makebox[\OPTbastardwidth][s]{
\fontsize{\OPTbastardtitlefont}{\OPTbastardtitlefont}\fontshape{n}\selectfont%
\textbf{Homotopy Type Theory}}\par
\vspace*{\OPTbastardtitleskip}
\makebox[\OPTbastardwidth][s]{
\fontsize{\OPTbastardsubtitlefont}{\OPTbastardsubtitlefont}\fontshape{n}\selectfont%
\textit{Univalent Foundations of Mathematics}}\par
}
\else
\fi

%%%%%%%%%%%%%%%%%%%% Title page %%%%%%%%%%%%%%%%%%%%
\cleartooddpage
\hbox{}\vfill
{\centering
\makebox[\OPTtitlewidth][s]{\fontsize{\OPTtitletitlefont}{\OPTtitletitlefont}\fontseries{b}\selectfont%
Homotopy Type Theory}\par
\vspace*{\OPTtitletitleskip}
\makebox[\OPTtitlewidth][s]{\fontsize{\OPTtitlesubtitlefont}{\OPTtitlesubtitlefont}\fontshape{it}\selectfont%
Univalent Foundations of Mathematics}\par
\vspace*{\OPTtitleskip}
{\fontsize{\OPTtitleauthorfont}{\OPTtitleauthorfont}\fontshape{n}\selectfont%
The Univalent Foundations Program\par
\vspace*{\OPTtitleauthorskip}
Institute for Advanced Study\par
}
\vspace*{\OPTtitleskip}
\vspace*{\OPTtitleskip}
\includegraphics[width=\OPTtitlewidth]{\OPThalftorus}\par
}

\vfill
\hbox{}

\clearpage
%%% Restore page style
\restoregeometry

%%%%%%%%%%%%%%%%%%%% Copyright page %%%%%%%%%%%%%%%%%%%%
\hbox{}
\vfill
\input{version.tex}
{\small
\noindent
\emph{``Homotopy Type Theory: Univalent Foundations of Mathematics''}\\
\copyright\ 2013 The Univalent Foundations Program

\medskip
\noindent
Book version: \texttt{\OPTversion}

\medskip
\noindent
MSC 2010 classification:
\texttt{03-02},
\texttt{55-02},
\texttt{03B15}

\bigskip
\footnotesize

\noindent
This work is licensed under the
\textbf{\emph{Creative Commons Attribution-ShareAlike 3.0 Unported License.}}
%
To view a copy of this license, visit
\url{http://creativecommons.org/licenses/by-sa/3.0/}.

\bigskip

\noindent
This book is freely available at \url{http://homotopytypetheory.org/book/}.

\bigskip

\noindent
\emph{\textbf{\small Acknowledgment}}

\medskip

\noindent
Apart from the generous support from the Institute for Advanced Study, some contributors
to the book were partially or fully supported by the following agencies and grants:
%
\begin{itemize}
\item Association of Members of the Institute for Advanced Study: a grant to the Institute for Advanced Study % Dan Grayson
% SLOVENIA
\item Agencija za raziskovalno dejavnost Republike Slovenije:  % Andrej's Slovenian agency
\href{http://www.sicris.si/search/prg.aspx?id=6120}{P1--0294},
\href{http://www.sicris.si/search/prj.aspx?id=7109}{N1--0011}.

\item Air Force Office of Scientific Research:
  FA9550-11-1-0143, and % Steve's ASFOR
  FA9550-12-1-0370.  % Bob's ASFOR
  {
    \setlength{\parskip}{0pt}
    \begin{quote}
      \noindent\scriptsize
      This material is based in part upon work supported by the AFOSR under the above awards.
      Any opinions, findings, and conclusions or recommendations expressed in this publication are those of the author(s) and do not necessarily reflect the views of the AFOSR.
    \end{quote}
  }

\item Engineering and Physical Sciences Research Council: % Thorsten and students
   \href{http://gow.epsrc.ac.uk/NGBOViewGrant.aspx?GrantRef=EP/G034109/1}{EP/G034109/1}, % Reusability and dependent types
   \href{http://gow.epsrc.ac.uk/NGBOViewGrant.aspx?GrantRef=EP/G03298X/1}{EP/G03298X/1}. % Theory and Application of Induction Recursion

\item European Union's 7th Framework Programme under grant agreement nr.\ 243847 (%
\href{http://wiki.portal.chalmers.se/cse/pmwiki.php/ForMath/ForMath/}{ForMath}). %% several Europeans, via Bas

\item National Science Foundation:
  \href{http://www.nsf.gov/awardsearch/showAward.do?AwardNumber=1001191}{DMS-1001191}, %% Steve's NSF, including Chris and Kristina
  \href{http://www.nsf.gov/awardsearch/showAward.do?AwardNumber=1100938}{DMS-1100938}, %% Vladimir's NSF
  \href{http://www.nsf.gov/awardsearch/showAward.do?AwardNumber=1116703}{CCF-1116703}, %% Foundations and Applications of Higher-Dimensional Directed Type Theory
  and
  \href{http://www.nsf.gov/awardsearch/showAward.do?AwardNumber=1128155}{DMS-1128155}. %% IAS support for Mike Shulman, copied from our %% paper by Dan Licata
  {
    \setlength{\itemsep}{0pt}
    \begin{quote}
      \noindent\scriptsize
      This material is based in part upon work supported by the
      National Science Foundation under the above awards.  Any opinions,
      findings, and conclusions or recommendations expressed in this
      material are those of the author(s) and do not necessarily reflect the
      views of the National Science Foundation.
    \end{quote}
  }
\item The Simonyi Fund: a grant to the Institute for Advanced Study          %% Dan Grayson
  \end{itemize}


}
\cleartooddpage

%%% Local Variables:
%%% mode: latex
%%% TeX-master: "hott-online"
%%% End:

===== END SOURCE CHUNK | EOF=true =====
