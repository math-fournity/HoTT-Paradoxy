# ZQCM-001 W-006 / V-UF-02 Source Notes — Ahrens & North

> **来源身份：** Benedikt Ahrens and Paige Randall North, *Univalent Foundations and the Equivalence Principle*, arXiv:2202.01892v1. The title and authors match the chapter listed as pp. 137–150 in *Reflections on the Foundations of Mathematics*. This acquired 14-page arXiv author version is **not** asserted to be byte-identical to that published pagination.
>
> **证据版本：** arXiv official PDF, SHA-256 `e2def8f64237f177470ef594b1eff7e2b51c87a0f7d4628759ebe43194cac352`; all 14 source pages and 11 key 300dpi pages are recorded in [`VISUAL-REVIEW.md`](VISUAL-REVIEW.md).
>
> **状态：** FULL_AUTHOR_VERSION_EQUIVALENCE_PRINCIPLE_AND_H0_SOURCE_PRECISION_SCREENED / SOURCE_ONLY_VISUAL_CHECK_COMPLETE / NOT_A_BARE_ZFC_CONSUMER / NOT_A_ZFC_Q / REMOTE_DERIVATIVE_NOT_QUALIFIED.

## 可消费的来源事实

| Source ID | PDF页 | 来源事实 | 对当前语料的作用 | 禁止外推 |
|---|---:|---|---|---|
| C-W006-VUF02-01 | 1–2 | 作者将equivalence principle定义为在给定对象域中，适当的same-ness下性质应不变；他们以集合论里`1 ∈ ℕ`不随集合同构不变为例，并要求选择合适的domain、properties与structures。 | 这是ZFC／集合论表示性事实进入HoTT动机的原典入口，也提供“非不变性质先检查任务与语言”的强反控制。 | 作者没有把该例称为ZFC矛盾、未支付存在或P命中；它没有固定ordinary ZFC consumer或Done。 |
| C-W006-VUF02-02 | 3–4 | 在category语境，作者以typed language、object equality排除和Theorem 3来界定哪些属性可保持equivalence-invariant；其结果明确依赖特定逻辑语言与表达范围。 | 将结构不变性的论证精确绑定到语言／对象层／可表达性，而非泛化为所有集合论任务的结论。 | 不能把“须排除object equality”直接重述为ZFC缺陷，或把这个typed-language条件偷换为bare ZFC接口。 |
| C-W006-VUF02-03 | 5–7 | equality types、iterated equality、paths、`transport`、`idtoequiv`与Univalence Axiom被列为从MLTT到univalent foundations的机制；作者明确说明纯MLTT、axiom extension与cubical derivation的不同体系位置。 | 提供高精度H0／univalence机制与体系范围来源，供反类比与HOTT-MOTIVE的精确对照。 | 不存在从这些type-level构造到ZFC对象、formation或ordinary consumer的自动保真传输。 |
| C-W006-VUF02-04 | 8–11 | 文章在type-theoretic `Prop`、`Set`、monoid与univalent category内分别陈述／推导equivalence principle；每项带有isProp、coherence、arrow-set、isomorphism和univalence等限定。 | 证明本文的“sets”“monoids”“categories”是有明确类型论定义和条件的内部对象。 | 不能把其中的`Set`、同构或transport词语直接视为ZFC Power Set、集合外延或ZFC实际consumer。 |
| C-W006-VUF02-05 | 12–13 | 作者把更高范畴的结论限定为univalent categories和额外univalence condition，并明说对一般结构定义该条件仍是active research。 | 给出已支付与仍开放问题的精确边界，防止把一般化读成已解决或已反驳。 | “active research”只表明本文所说的特定高阶结构条件仍在研究，不能当作ZFC Q或理论不一致证据。 |
| C-W006-VUF02-06 | 13–14 | References把本文接到HoTT Book、Voevodsky、Cubical Type Theory、Univalent Categories和结构主义／不变性文献。 | 提供受限backward map。 | 书目关系不自动生成新work family、H0结论或ZFC候选。 |

## R→Z→Q 资格状态

V-UF-02 是一份**强 HoTT 动机与机制来源**，但它首先也给出一个重要的反跳跃规则：从“某集合论表达不随同构不变”到“ZFC有理论级问题”之间，作者实际插入了对象域、允许的性质、适当的same-ness、语言限制、univalence条件和具体type-theoretic transport等一系列中间支付。

这篇原典因此有两种可消费价值：

1. 作为 `HOTT-MOTIVE-ZFC-SOP` 的潜在 `R_i` 来源，精准说明equivalence principle为何是HoTT/UF设计动机之一；
2. 作为 `H0→Z0` 与结构主义／extensionality路线的反类比控制：任何声称把其结论投射到ZFC的卡，必须独立固定ZFC侧对象、规则、形成、普通实际消费者、同一操作／观察／Done，并证明没有改变本文的类型论机制。

本文没有给出这样的 `Z_i`，没有出现同一张卡的P1/P2/P3/P5会合，也没有一个ordinary ZFC consumer预支使用待支付对象。当前结论是 `SOURCE_PRECISION_GAIN / EQUIVALENCE_PRINCIPLE_H0_SOURCE_AND_ANTI_ANALOGY_CONTROL / Q_NOT_QUALIFIED`。
