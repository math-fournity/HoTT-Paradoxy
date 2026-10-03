# ZQCM-001 W-011 Source Notes — Klev 2019

> **来源身份：** Ansten Klev, *A Comparison of Type Theory with Set Theory*, chapter 12 (2019), DOI [`10.1007/978-3-030-15655-8_12`](https://doi.org/10.1007/978-3-030-15655-8_12).
>
> **证据版本：** author-hosted public preprint，SHA-256 `3c3555f3325f49857e92002dca14aa5e5343d54368daf81dbeffefefa5bb676e`；关键视觉页见 [`VISUAL-REVIEW.md`](VISUAL-REVIEW.md)。
>
> **状态：** PARTIAL_PRIMARY_COMPARATIVE_SOURCE_SCREENED / NOT_A_ZFC_Q / REMOTE_DERIVATIVE_NOT_QUALIFIED。

## 可消费的来源事实

| Source ID | PDF页 | 来源事实 | 对当前语料的作用 | 禁止外推 |
|---|---:|---|---|---|
| C-W011-01 | 1 | 作者明确将“set theory”限定为标准公理集合论，即ZFC或其变体；论文自称讨论概念差别。 | 把比较对象从泛泛“set theory”缩窄到可追溯的ZFC范围。 | 范围限定不等于对任何ZFC公理的反例。 |
| C-W011-02 | 1 | 摘要区分sets/types、syntax、functions、identity，并提出extensionality不等于sets identity criterion的作者论证。 | identity／extensionality路线的一手文献入口。 | 作者结论还不是本项目所需的P、same-task或Q。 |
| C-W011-03 | 16–17 | 函数的well-definedness所预设的identity与propositional identity之间，作者提出一个逻辑语法层的循环论证；其比较落在Martin-Löf type theory的judgemental identity。 | P2的逻辑语言／形成先后研究的竞争源与精确反控制。 | 不能把type-theoretic judgemental identity直接等同于ZFC的时间、形成或计算承诺。 |
| C-W011-04 | 17 | 作者明确把论证依赖限定为judgemental/propositional identity的逻辑语法范畴差异，并说明规则会随类型论版本变化。 | 防止把特定type theory论证伪装成一般元数学定理。 | 不能直接支持或否定ZFC Q。 |
| C-W011-05 | 18 | 作者把外延性写为关于universe `V` 的普通谓词逻辑公式，论证其等号已预设`V`上的identity criterion，故外延性不单独表达该准则。 | `EXTENSIONALITY_SITE_SEED`：一个明确ZFC基础接口及其“预设同一性”问题表述。 | 仍是哲学／逻辑语法论证；缺ZFC内部形成、实际consumer、同一任务Done和P再入，不能升级为Q。 |

## R→Z→Q 资格状态

W-011比一般“HoTT优于集合论”的说法更精确，因为它真正指定ZFC范围，并在p.18给出 `EXTENSIONALITY_SITE_SEED`。然而其主论证仍在Martin-Löf type theory的judgement／proposition框架内。要使任何site seed成为ZFC候选，仍需独立建立：一个ZFC内部对象与形成规则、该对象的实际consumer、同一输入／操作／观察／Done，以及P的未支付再入或上升结构。当前结论是 `SOURCE_PRECISION_GAIN / EXTENSIONALITY_SITE_SEED / Q_NOT_QUALIFIED`。
