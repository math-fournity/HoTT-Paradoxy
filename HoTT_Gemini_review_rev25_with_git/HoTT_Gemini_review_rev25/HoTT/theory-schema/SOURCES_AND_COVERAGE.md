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
