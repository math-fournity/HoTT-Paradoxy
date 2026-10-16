# Markov反向中的输入数据与选择来源

本单元审查固定原生Dedekind基线中的反向：从BookMarkov到非零实数的apartness。重点是具体有理界序列、整列数据的mere存在和每个精度的mere存在之间的类型区别；本文记录来源与假设用途，不用文献替代本轮正式内核收据。

## 本地固定库

实际全文读取以下三个模块：

- `real-numbers/arithmetically-located-dedekind-cuts.lagda.md`：`close-bounds-ℝ`给p、q和q<p+ε、p∈L、q∈U；`is-arithmetically-located-ℝ`逐ε返回截断存在。
- `real-numbers/rational-approximates-of-real-numbers.lagda.md`：有理近似类型与above/below/general存在定理；返回的`is-inhabited/type-trunc-Prop`没有被默认为选定数据。
- `foundation/axiom-of-countable-choice.lagda.md`：`level-ACℕ lzero`只对自然数索引的小集合族给选择的mere存在。没有在本模块中提供该原则的实例。

库树仍为`3787fb34df15515246da11b90b609d3a2063f15e234f19c1e7f64553c4990f57`，no-erasure父commit7b81411d。其他有理加减与集合接口按实际所用符号读取，依赖完整性由主run树hash和本地manifest负责，不声称阅读了库内每个模块全文。

## 本轮代码中三层输入

1. `RationalBoundSequence x`：每个自然数n给具体上下界及宽度<1/(n+1)证据。
2. `MereBoundSequence x`：整列数据的截断存在。目标apartness是命题，可合法消去这一截断。
3. `pointwiseMereBounds x n`：每个n各有界的截断存在，直接来自库的located性。`countableChoiceGivesMereBounds`显式使用`level-ACℕ lzero`将其接到第2层。

没有把第3层直接作为第1层输入，也没有选择全体实数的一份全局近似函数。本单元不声称可数选择是唯一或必要的办法。

## 外部一手文献对照（只按实际已读范围）

检索在2026-09-21进行；搜索返回的百科、问答和二手页面仅作发现线索，不用于理论结论。

- Auke B. Booij，*Extensional constructive real analysis via locators*，arXiv:1805.06781v5。已读摘要及HTML §1、§2.1、§2.2、§3.1可见段落；未称全文已读。作者明确区分locatedness的性质与locator的结构，同一实数可带不同locators。本轮界序列未与其locator做形式互译；此对照不能证明本项目的独立性。[固定版本正文](https://arxiv.org/html/1805.06781v5)，[书目信息](https://arxiv.org/abs/1805.06781v5)。
- Andrej Bauer、Paul Taylor，*The Dedekind Reals in Abstract Stone Duality*（2009）：只读作者站点索引/摘要和章节路由，确认当前库的参考来源；没有把ASD结论当作HoTT定理或完成跨演算翻译。[作者页面](https://www.paultaylor.eu/ASD/dedras/index.html)。
- Joan Rand Moschovakis，*Markov's Principle, Markov's Rule and the Notion of Constructive Proof*，2018修订稿：只查看引言与§2的可见内容。其区分原则、规则和不同形式系统；没有将关于HA等系统的结果移植为本HoTT基线的不可证性。[作者稿](https://www.math.ucla.edu/~joan/kreiselmarkovcorr.pdf)。

没有复制整篇非开放许可论文进入本地公开审阅包，也没有用网页抓取时间充当定理产生时间。

## 当前开放边界

未取得不加数据供给/选择时对所有任意Dedekind实数的反向；未证明Markov或选择相对当前基线独立，也未证明选择必要。即使条件反向过核，仍须回原G01/G02审查同任务和实际能力承诺。
