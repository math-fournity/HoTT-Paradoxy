# 证据 04：Zermelo 1908 的动机排序（Q3）

> **来源身份**：DOCUMENTED_SOURCE。抓取时间（UTC）：2026-10-17T05:47:38Z。
> 本问的关键文献 G. H. Moore, *The Origins of Zermelo's Axiomatization of Set
> Theory*, Historia Mathematica 5 (1978) 有 Springer 付费墙（抓取返回 303 →
> idp.springer.com 授权页，**未取得全文**）。改以 Kanamori 的开放论文为主要证据，
> 它与 SEP、Hallett 相互独立且可交叉验证。

## 1. Kanamori, *The Mathematical Import of Zermelo's Well-Ordering Theorem*

- 本地副本：`搜索原始响应-20261017/kanamori.pdf`，sha256[:16] = `4beaff3922ba472a`
- 来源 URL：https://www.tau.ac.il/~corry/teaching/philosophy/download/kanamori.pdf
- 文本抽取：`pdftotext` → `kanamori.txt`（行号定位）

### 1.1 1908a 的**首要目的**是良序定理，不是悖论（行 830–834）

> „**The main purpose of Zermelo's [1908a] axiomatization of set theory, the
> first full-scale such axiomatization, was to buttress his [1908] proof by making
> explicit its underlying set-existence assumptions.** The salient axioms were the
> generative Power Set and Union Axioms, the Axiom of Choice of course, and
> the Separation Axiom. **These incidentally could just as well have been motivated
> by the first [1904] proof.**"

**要点**：分离公理在这里被描述为「附带地（incidentally）也可由 1904 年证明激发」——
**悖论不是 1908a 的首要动机**。这支持 Q3 的假说：Zermelo 的动机是良序定理优先。

### 1.2 独立发现的实证（Husserl Nachlass，行 486–490）

> „**Zermelo's independent discovery of the argument for Russell's Paradox is
> substantiated in a note dated 16 April 1902 found in the Nachlass of the
> philosopher Edmund Husserl.** According to the note, Zermelo pointed out that
> any set M containing all of its subsets as members, i.e., with P(M) ⊆ M, is
> "inconsistent" by considering {x ∈ M | x ∉ x}."

**要点**：Zermelo 独立发现的原始形式**不是**「所有不属于自身的集合的类」，而是
**「若 P(M) ⊆ M 则 M 不一致」**——即 **Cantor 式幂集对角**，与标准 Russell 形式
不同。这一细节对步骤 4 有价值：Zermelo 自始就是在**给定集合内切割**的框架里思考
（正是 C-433 的形状），而不是无界概括。

### 1.3 1908a 的第一个结果（行 543–548）

> „In Zermelo's axiomatization paper [1908a], **the first result of his axiomatic
> theory was just the result in the Husserl note, that every set M has a subset
> {x ∈ M | x ∉ x} not a member of M, with the consequence that there is no
> universal set.** Modern texts of set theory usually take the opposite tack,
> showing that there is no universal set by reductio to Russell's Paradox."

**要点（极强的考古证据）**：Zermelo 1908a 的**第一个定理**就是本包 **C-433**
（`R_A ∉ A`）。而且 Kanamori 指出**现代教科书走的是相反路线**——用罗素悖论反证
无全集，而 Zermelo 本人是**正面构造**出「从 M 中缺失的那个子集」。
这正是步骤 4 对照表第三栏「未支付的诠释跳跃」的文献侧锚点：
**教科书把 Zermelo 的正面定理重述成了反证法的悖论叙事。**

## 2. 交叉验证

| 来源 | 对动机的表述 | 一致性 |
|---|---|---|
| Kanamori（行 830） | 主要目的 = 支撑 1908 良序证明；分离公理「附带地」 | 良序优先 |
| SEP *Early Development* §3 | „The impressive polemics which surrounded his **Well-Ordering Theorem**, and the … problem posed by the foundations of mathematics, led Zermelo to concentrate on axiomatic set theory." | 两者并列，良序在先 |
| SEP *Zermelo's Axiomatization* §2.2.3 | „there is little doubt that this line of criticism greatly influenced the shape of the second proof given in 1908" | 批评（良序证明的）塑造了 1908 |
| Hallett（SEP §1） | „It is clear above all that Zermelo's intention was to reveal the fundamental nature of the theory of sets and to preserve its achievements, while at the same time providing a general replacement for the CP." | 中性：保留成果 + 替换概括原则 |

**Q3 结论（PARTIAL）**：**良序定理优先**有 Kanamori 的明确表述 + SEP 两条旁证支持；
但 Moore 1978（本问的权威专著）**未取得全文**，故判定为 PARTIAL，不作「已确证」。
「无界概括」一词的命名史**未检索到可靠出处**（见证书盲区）。

## 3. 与数学行的对应

- Kanamori 所述 1908a 第一结果 ⟷ **C-433** `sep_russell_not_mem`（`R_A ∉ A`）。
- Husserl 笔记形式「P(M) ⊆ M ⇒ 不一致」⟷ 与 **C-435**（无界概括 ⇒ False）同族，
  但 Zermelo 的原始形式是**有界**的（在给定 M 内切割），不是无界概括。
