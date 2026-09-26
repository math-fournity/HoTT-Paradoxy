# totality-escalation 修订记录

> 本包的 `CLAIM.md`、`CLAIM-C74.md` 已进入运行收据的源码哈希，不改原文；更正与补充记在这里。

## 2026-09-26（会话 7f138325，交付前回源）

**对象**：`CLAIM.md` “禁止外推”一节第二条，原文：“‘对一切 n，n 层落定者的总体都不是 n 层’（精确上升）只在 n = 0、1 两级有机器证明；一般情形为已知结果（用 Eilenberg–MacLane 型类型），本包不证明。”

**补充来源**：Kraus, Sattler, *Higher Homotopies in a Hierarchy of Univalent Universes*，ACM Transactions on Computational Logic，2015，DOI `10.1145/2729979`（arXiv:1311.4002）。经 sciverse 核对摘要（全文在该库中不可读），原文：

> For Martin-Löf type theory with a hierarchy U0:U1:U2:… of univalent universes, we show that Un is not an n-type. Our construction also solves the problem of finding a type that strictly has some high truncation level without using higher inductive types. In particular, Un is such a type if we restrict it to n-types. We have fully formalized and verified our results within the dependently typed language and proof assistant Agda.

**更正**：
- 括注“用 Eilenberg–MacLane 型类型”只是一种可能的证法。本包 n = 1 一级用的 S¹ 就是 K(ℤ,1)。上面这篇已发表的证明用的是单价宇宙层级，不用高阶归纳类型。
- 一般情形的状态应写作：【来源】已发表并由作者在 Agda 中形式化；本仓库未重放，不作为本仓库的机器证明交付。
- 本包的命题 (a)–(d) 与证据等级不变。
