# R039 来源与阅读范围

1. Xavier Leroy, *Semantics of divergence, second part*, Module Partiality.
   https://xavierleroy.org/cdf-mech-sem/CDF.Partiality.html
   实际web阅读全文的相关定义与证明：delay/omega与归纳terminates L8—59；equi、terminates_equi、diverges_equi L86—159；受限单边跳过与自然数索引L160—202。用于区分有限跳过与无限单边跳过，以及共同收敛的正向实现。非HoTT原生代码；本轮没有在Coq重编译。文档正文引用仅用自己的转述；不是原始字节下载存档。
2. HoTT Book固定commit 578b85cc8d586b1677ec4335148adeb443057d24, hits.tex §6.10。
   https://raw.githubusercontent.com/HoTT/book/578b85cc8d586b1677ec4335148adeb443057d24/hits.tex
   本地文件HoTT/theory-schema/upstream/book-578b85cc/hits.tex。集合商递归需要尊重关系，不能为不保持返回值/必然完成的源操作免费提供下降。
3. Rob van Glabbeek, Bas Luttik, Nikola Trčka, *Branching Bisimilarity with Explicit Divergence*, arXiv:0812.3068；Fundamenta Informaticae 93(4), 2009。
   https://arxiv.org/abs/0812.3068
   阅读摘要/作者出版页面，用于明确“额外保持发散”是既有语义区分。本轮F/S的普通弱互模拟证明由正文直接给出，没有声称读过整篇PDF或实现其全部branching条件。arXiv HTML获取失败。
4. Thorsten Altenkirch, Nils Anders Danielsson, Nicolai Kraus, *Partiality, Revisited*, arXiv:1610.09254 / FoSSaCS 2017。
   https://arxiv.org/abs/1610.09254
   仅摘要：Delay、强/弱等价、可数选择与HoTT启发的QIIT部分性单子。没有以摘要认证本轮全部规则，没有宣称全篇或代码审计完成。arXiv HTML获取失败。

全部网络核对日期2026-09-11。容器原始下载独立失败，见artifacts/r039/sources/FETCH_RECEIPT.json；web读取成功与容器下载失败不是同一次操作。未编造源hash，实际本地固定Book源码哈希由RESEARCH_MANIFEST登记。
