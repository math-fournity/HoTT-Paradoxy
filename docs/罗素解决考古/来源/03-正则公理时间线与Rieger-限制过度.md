# 证据 03：正则公理时间线（Q4）+ 「ZF 限制超过悖论所需」文献（Q3 延伸）

> **来源身份**：DOCUMENTED_SOURCE。抓取时间（UTC）：2026-10-17T05:46:03Z。

## 1. Q4：正则公理不在 1908 之内——三条独立来源一致

### 1.1 Wikipedia *Axiom of regularity*（History 节，经 MediaWiki API 取 wikitext 原文）

- URL：https://en.wikipedia.org/wiki/Axiom_of_regularity（抓取 2026-10-17T05:46:03Z）
- 获取方式：`https://en.wikipedia.org/w/api.php?action=parse&page=Axiom_of_regularity&prop=wikitext&format=json`

> „The concept of well-foundedness and rank of a set were both introduced by
> **Dmitry Mirimanoff**. Mirimanoff called a set *x* "regular" (*ordinaire*) if
> every descending chain … is finite. **Mirimanoff however did not consider his
> notion of regularity (and well-foundedness) as an axiom to be observed by all
> sets**…"
> „**Skolem (1923) and von Neumann (1925)** pointed out that non-well-founded
> sets are superfluous and in the same publication von Neumann gives an axiom
> that excludes some, but not all, non-well-founded sets. In a subsequent
> publication, **von Neumann (1929)** gave an equivalent but more complex version
> of the axiom of class foundation…"
> „**The contemporary and final form of the axiom is due to Zermelo (1930).**"

### 1.2 Enderton 1977（行 12633–12636）

> „The **idea first appeared in a 1917 paper by Mirimanoff; the axiom was listed
> explicitly in von Neumann's 1925 paper**."

### 1.3 Wikipedia *Axiom of regularity* §"Regularity and Russell's paradox"

> „**In the presence of the axiom schema of separation, Russell's paradox becomes
> a proof that there is no set of all sets.**"
> „**Russell's paradox yields a proof that there is no "set of all sets" using the
> axiom schema of separation alone, without any additional axioms. In particular,
> ZF without the axiom of regularity already prohibits such a universal set.**"
> „If ZF without regularity is extended by adding regularity to get ZF, then any
> contradiction that followed from the original theory would still follow in the
> extended theory."

**Q4 结论**：正则公理 1917（Mirimanoff 概念）→ 1925（von Neumann 明确列出）→
1929（von Neumann 类形式）→ 1930（Zermelo 定形）。**不是 1908 的一部分**，
且**分离公理独自已足够**得出「不存在全集」——正则与时间线、与罗素悖论的
**解决**都无必要性关系。三来源一致，且与本包 C-434 的「第二道准入门」定位吻合。

## 2. Q3 延伸：Rieger (2008) —— ZF 限制超过悖论所需

- Rieger, A. "Paradox, ZF, and the Axiom of Foundation", in *Vintage
  Enthusiasms: Essays in Honour of J. L. Bell* (2008).
- 本地副本：`搜索原始响应-20261017/rieger-foundation.pdf`，sha256[:16] = ``
- 开放获取 URL：https://eprints.gla.ac.uk/3810/1/JLB.pdf
- 文本抽取：`pdftotext` → `rieger.txt`

### 2.1 对角化诊断（与 C-433 同构）

> „Suppose a is a set, and consider the set
> b = {x ∈ a : x ∉ x}.
> It is easy to see that b ∉ a. So we have a recipe which, for any set a, gives us
> a set which is not a member of a. The set b "diagonalizes out" of a."

### 2.2 核心结论（本包「准入层拒绝 ≠ 解决」的文献侧对应）

> „A suspicion therefore arises that **ZF restricts the notion of set more than is
> necessary to avoid the paradoxes**, and therefore offends against the following
> methodological principle: when forced by paradox to reform a naive concept,
> preserve as much of it as possible."
> „**Summary: it can be rigorously proved that ZF restricts the notion of set more
> than the paradoxes demand.**"

### 2.3 与罗素 1906c 的承接

> „What is demonstrated by the contradictions we have considered is broadly
> this: 'A propositional function of one variable does not always determine a
> class.'（Russell [1906c] pp. 144–5）"

**要点**：Rieger 是抽样中唯一**明确质疑**「需要层级来解决悖论」这一流行信念的
文献，且给出与 C-433 同构的对角化诊断。他的结论是**限制过度**，不是「解决了」。

## 3. 与数学行的对应（供步骤 4 三栏对照表引用）

| 文献说法 | 本包机器命题 |
|---|---|
| Rieger: `b = {x∈a : x∉x}` 有 `b ∉ a`，「对角化出去」 | **C-433** `sep_russell_not_mem`（分离层 `R_A ∉ A`，定理非矛盾） |
| Wikipedia: 分离公理**单独**已足够证明无全集 | **C-433** 为零集合论公理外的纯逻辑内容（公理清单空） |
| Rieger: 正则是**超出悖论所需**的额外限制 | **C-434** `foundation_irrefl`（正则 ⇒ 禁自含，第二道门） |
| Enderton/Wikipedia 时间线：1930 定形，非 1908 | **C-434** 实例化节已标注「库内 𝗭 含正则，非 1908 历史系统」 |
