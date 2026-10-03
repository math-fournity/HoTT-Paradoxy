# ZQCM-001 W-011 Source Notes — Klev 2019

> **来源身份：** Ansten Klev, *A Comparison of Type Theory with Set Theory*, chapter 12 (2019), DOI [`10.1007/978-3-030-15655-8_12`](https://doi.org/10.1007/978-3-030-15655-8_12).
>
> **证据版本：** author-hosted public preprint，SHA-256 `3c3555f3325f49857e92002dca14aa5e5343d54368daf81dbeffefefa5bb676e`；关键视觉页见 [`VISUAL-REVIEW.md`](VISUAL-REVIEW.md)。
>
> **状态：** FULL_PRIMARY_COMPARATIVE_SOURCE_SCREENED / SOURCE_ONLY_VISUAL_CHECK_COMPLETE / NOT_A_ZFC_Q / REMOTE_DERIVATIVE_NOT_QUALIFIED。

## 可消费的来源事实

| Source ID | PDF页 | 来源事实 | 对当前语料的作用 | 禁止外推 |
|---|---:|---|---|---|
| C-W011-01 | 1 | 作者明确将“set theory”限定为标准公理集合论，即ZFC或其变体；论文自称讨论概念差别。 | 把比较对象从泛泛“set theory”缩窄到可追溯的ZFC范围。 | 范围限定不等于对任何ZFC公理的反例。 |
| C-W011-02 | 1 | 摘要区分sets/types、syntax、functions、identity，并提出extensionality不等于sets identity criterion的作者论证。 | identity／extensionality路线的一手文献入口。 | 作者结论还不是本项目所需的P、same-task或Q。 |
| C-W011-03 | 16–17 | 函数的well-definedness所预设的identity与propositional identity之间，作者提出一个逻辑语法层的循环论证；其比较落在Martin-Löf type theory的judgemental identity。 | P2的逻辑语言／形成先后研究的竞争源与精确反控制。 | 不能把type-theoretic judgemental identity直接等同于ZFC的时间、形成或计算承诺。 |
| C-W011-04 | 17 | 作者明确把论证依赖限定为judgemental/propositional identity的逻辑语法范畴差异，并说明规则会随类型论版本变化。 | 防止把特定type theory论证伪装成一般元数学定理。 | 不能直接支持或否定ZFC Q。 |
| C-W011-05 | 18 | 作者把外延性写为关于universe `V` 的普通谓词逻辑公式，论证其等号已预设`V`上的identity criterion，故外延性不单独表达该准则。 | `EXTENSIONALITY_SITE_SEED`：一个明确ZFC基础接口及其“预设同一性”问题表述。 | 仍是哲学／逻辑语法论证；缺ZFC内部形成、实际consumer、同一任务Done和P再入，不能升级为Q。 |
| C-W011-06 | 2–15 | 论文把sets/types、syntax、judgements与functions逐段作为概念比较；p.2明确将它限制为conceptual而非technical comparison，p.8–13把类型论的judgement/context与对象语言集合论区分，p.13–15讨论functionhood与application的比较。 | 说明本文提供的是对理论语言的作者性读法，而不是某个ordinary ZFC consumer的运行、证明或形成记录。 | “集合论没有 judgement”或“函数定义预设关系”不能直接等于ZFC的P字段、时间张力或Q。 |
| C-W011-07 | 16–18 | identity章节先以type-theoretic primitive function application和judgemental identity论证，再把外延性写作predicate-logical formula；作者明说该论证依赖逻辑语法类别区分而非不同类型论版本的具体规则。 | 把`EXTENSIONALITY_SITE_SEED`的来源层固定为比较性逻辑语法／哲学论证。 | 不能把Klev的前提替换为ZFC对象语言内的formation-use循环。 |
| C-W011-08 | 19–21 | concluding remarks把集合论与类型论称为不同的conceptual architecture／ideology，并承认set theory作为基础已经相当成功；文末references包含Aczel 1978（已入W-013）和Klev 2018b等相邻来源。 | 反控制：该作者比较不等于“ZFC理论失败”；只提供下一轮作者／思想史追踪入口。 | 引用书目本身不提供actual consumer或Q。 |

## R→Z→Q 资格状态

W-011比一般“HoTT优于集合论”的说法更精确，因为它真正指定ZFC范围，并在p.18给出 `EXTENSIONALITY_SITE_SEED`。21页全文与关键页复核后，界限更强：本文并没有交付ordinary ZFC内部的对象形成、actual consumer、同一输入／操作／观察／Done或P的未支付再入／上升结构；它反复把自己的工作限定为概念／逻辑语法比较，并在结语认可set theory作为基础的实际成功。当前结论是 `SOURCE_PRECISION_GAIN / EXTENSIONALITY_SITE_SEED / Q_NOT_QUALIFIED`。下一轮只有固定版本的ZFC actual consumer能重开这条线。
