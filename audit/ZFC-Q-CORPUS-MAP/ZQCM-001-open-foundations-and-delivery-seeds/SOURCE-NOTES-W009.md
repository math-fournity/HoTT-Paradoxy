# ZQCM-001 W-009 Source Notes — Altenkirch 2019

> **来源身份：** Thorsten Altenkirch, *Naïve Type Theory*, chapter 5 (2019), DOI [`10.1007/978-3-030-15655-8_5`](https://doi.org/10.1007/978-3-030-15655-8_5).
>
> **证据版本：** author-hosted chapter PDF，SHA-256 `0a7373b12fb109c266254d21f7b775575d73b48e439cfa6b2740a83fcec3bd67`；关键视觉页见 [`VISUAL-REVIEW.md`](VISUAL-REVIEW.md)。
>
> **状态：** FULL_PRIMARY_R_SOURCE_SCREENED / SOURCE_ONLY_VISUAL_CHECK_COMPLETE / NOT_A_ZFC_Q / REMOTE_DERIVATIVE_NOT_QUALIFIED。

## 可消费的来源事实

| Source ID | PDF页 | 来源事实 | 对当前语料的作用 | 禁止外推 |
|---|---:|---|---|---|
| R-W009-01 | 1–2 | 作者将Type Theory／HoTT作为集合论基础的替代性直观入口，随后把成员陈述与静态judgement区分。 | HoTT动机与语言层差异的来源。 | 不把`3∈N`与`3:N`的比较写成ZFC悖论。 |
| R-W009-02 | 15 | 作者说明Σ型existence会显式携带见证，并用choice公式说明这与传统命题读取不同。 | W-005的P5来源对照加固。 | 不等于ordinary ZFC task 有一个未支付的程序化Done。 |
| R-W009-03 | 20 | 作者在**类型论内部的**`Set`上问“何时两个sets相等”，并提出isomorphism／extensionality原则。 | 与表示、结构同一性和既有ZFC同构控制的比较入口。 | `Set`不是这里的ZFC宇宙；表示／同构批评不能跳过具体ZFC编码、actual consumer和same-task控制。 |
| R-W009-04 | 22–23（文本定位） | higher inductive types、propositional truncation和set quotients在类型论内部给出元素／等式的共同生成。 | H0／HoTT机制的背景来源。 | 不以HIT构造本身为ZFC形成规则或ZFC Q。 |
| R-W009-05 | 4 | 作者将`Type : Type`与罗素悖论联系，并把universe hierarchy作为避免循环式universe使用的类型论设计。 | HoTT／类型论如何明确处理Russell风险的一手控制。 | 类型论层级不自动给出ZFC Power Set、累积层级或ordinary consumer的同一机制。 |
| R-W009-06 | 15–17 | 作者区分Σ型中的显式见证与常规命题读法，分析choice、propositional truncation及其隐藏／不能恢复identity的条件。 | P5／存在—交付的构造主义比较来源。 | “传统命题不携带信息”不是ordinary ZFC consumer自己承诺的program-like Done。 |
| R-W009-07 | 20–21 | 作者对**类型论内部**`A,B:Set`的usual encoding给出isomorphism／`extSet`例，并继续区分sets与general types。 | 结构同一性／表示的R-source与既有ETCS／同构控制的比较入口。 | `Set`、`extSet`、isomorphism及其exercise都不是ZFC内部的同一任务consumer。 |
| R-W009-08 | 22–25 | 作者说明equivalence的asymmetric coherence处理、propositional truncation、set quotient、countable choice与HIT对permutable trees/Cauchy reals的内部构造路径。 | HoTT中formation、equality和choice payment的细粒度背景来源。 | 不能由类型论HIT／choice路线推断ZFC有同构的unpaid formation-use。 |
| R-W009-09 | 26–29 | 整数QIT、coherence constructor、normalisation与references都在类型论语义中完成。 | 说明余下全文没有悄然切换到ZFC实际consumer。 | 不将Type内部的normalisation／coherence问题写成ZFC Q。 |

## R→Z→Q 资格状态

W-009强化了两条**待验证的**R路线：存在／choice 的信息读取，以及表示／结构同一性。29页全文与9个关键页复核后，界限更清楚：它给出的是类型论自身的rules、constructors、witnesses、truncation、choice和coherence支付；没有ZFC侧的固定对象、formation、实际consumer或同一Done，因此没有产生ZFC Q。特别是p.20的`Set`／`extSet`讨论需要与本项目既有“具体编码—抽象结构—指定同构”反控制一起消费，不能被包装为对ZFC的结论。
