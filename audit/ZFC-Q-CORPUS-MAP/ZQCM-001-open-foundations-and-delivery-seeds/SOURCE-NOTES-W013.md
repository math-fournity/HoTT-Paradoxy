# ZQCM-001 W-013 Source Notes — Aczel 1978

> **身份：** PRIMARY_SOURCE_SCREENED / CZF_AND_TYPE_THEORETIC_CONTROL / NOT_A_ZFC_Q_CARD。
>
> **原件：** Peter Aczel, *The Type Theoretic Interpretation of Constructive Set Theory*, *Logic Colloquium '77*, Studies in Logic and the Foundations of Mathematics 96 (1978), pp.55–66, DOI [`10.1016/S0049-237X(08)71989-X`](https://doi.org/10.1016/S0049-237X(08)71989-X)。本批保存的公开课程副本及其hash见 [`PDF-VALIDATION.md`](PDF-VALIDATION.md)；页图审读见 [`VISUAL-REVIEW.md`](VISUAL-REVIEW.md)。

## 原页事实

1. **p.1–2：对象与作者目的。** 摘要把工作表述为：在 Martin-Löf 直觉主义类型论中加入一个“sets 的 type”，从而给 constructive set theory 一个 constructive interpretation，并将之称为经典累积层级观念的 constructive version。p.2把 CZF 描述为使用直觉主义逻辑、包含 extensionality 的 ZF 子系统，并明确把问题定为 constructive set theory 中“set”的 constructive meaning。
2. **p.3–5：CZF 与 Power Set 的明确规则关系。** p.3列出CZF的structural及set-existence部分，包括Subset Collection与Infinity。p.4的2.2说明 Power Set 蕴含 Subset Collection，后者蕴含 Exponentiation；2.3给出 Power Set 与 Exponentiation 加上“空集有 Power Set”的等价。p.5的2.4–2.7将这些关系与restricted excluded middle、full separation以及ZF的推演条件分开写明。
3. **p.7–8：集合形成不是无标记的一次性交付。** p.7以`U`的intro／elimination rules给出“type of sets”，把先前引入的、由small type索引的sets变为新set，并写明set recursion的归纳形式。p.8以该规则展示有限集、并集和一个无限集的构成；随后以ordinary/double set recursion定义extensional equality与membership的type，并把“CZF每个定理有效”标为解释工作的目标。
4. **p.9–10：有效性证据与 set-existence rules。** 作者对structural axioms及Pairing、Union、Restricted Separation、Strong/Subset Collection、Infinity分别给出类型论有效性构造。这里的`valid`是该解释的明示语义／构造支付，不可偷换成ordinary ZFC consumer已经预支的完成条件。
5. **p.11：presentation 是显式的交付条件。** 作者把presentation定义为base到set的满射，将“每个set都有presentation”明确列作额外Presentation Axiom，并说它表示set被给予的特定方式。该页同时说明既有`U`中并非总有合适表示，并给出改变CZFI／`U^I`或realizability model的具体补偿路线。

## 对 ZFC Q 的资格边界

这篇文章是与 W-012 的stage／iterative-set话题相邻的一手控制：它说明构造性集合论与类型论已经明确讨论形成、递归、表示和选择支付，也给出 Power Set 与更弱构造原则的精确关系。它**不**给出ZFC不一致、ZFC缺陷或一个已资格化的Q。

原因是：该文的理论对象是CZF及其类型论解释；关键construction、validity和presentation condition都被明确给出或另列为假设／补偿。当前未固定ordinary ZFC内部、同一对象的actual consumer，也没有来源显示该consumer在自己的Done尚未支付时预支使用对象。因此其处置是`PRIMARY_CONTROL_NOT_Q`，仅为`ZQCM-DIR-ITERATIVE-FORMATION`提供可反驳的来源基线。
