# ZQCM-001 W-006 / V-CMP-01 Source Notes — Barton & Friedman 2018

> **来源身份：** Neil Barton and Sy-David Friedman, *Set Theory and Structures*, author-hosted prepublication dated 2018-08-07; matching the title/authors of the 2019 volume chapter *Reflections on the Foundations of Mathematics*, pp. 223–253. The acquired 27-page author version is not asserted to be byte-identical to the published pagination.
>
> **证据版本：** author-hosted public PDF, SHA-256 `e8116b22aa72c5741e68c2dff9059652770741abde9aec51b31e4f91eb1ea5f7`; all 27 source pages and 16 key 300dpi pages are recorded in [`VISUAL-REVIEW.md`](VISUAL-REVIEW.md).
>
> **状态：** FULL_AUTHOR_PREPUBLICATION_COMPARATIVE_CONTROL_SCREENED / SOURCE_ONLY_VISUAL_CHECK_COMPLETE / ZFCS_NBGS_AND_UNIVERSE_PAYMENT_CONTROL / NOT_A_ZFC_Q / REMOTE_DERIVATIVE_NOT_QUALIFIED.

## 可消费的来源事实

| Source ID | PDF页 | 来源事实 | 对当前语料的作用 | 禁止外推 |
|---|---:|---|---|---|
| C-W006-VCMP01-01 | 1–2 | 作者把 material set theory 与 category-theoretic language 并置：前者可看内部 membership structure，后者看对象在更宽关系中的角色；论文明确问 material set theory 能否提供有关 structures 的信息。 | 将本文固定为 foundations-comparison / representation source，而非普通 ZFC 操作记录。 | 该问题、摘要或作者动机不构成 ZFC 的 formation、consumer 或 Q。 |
| C-W006-VCMP01-02 | 4–6 | 作者区分 material 与 categorical set theory，并把 set-theoretic representation 的 coding 依赖、category-theoretic isomorphism 的语境依赖与“structural similarity”分别说明。 | 为 identity／representation 分支提供一手竞争读法：表示差异先需区分任务与语言。 | “两种呈现不同”不自动表示 ZFC 不能完成同一任务。 |
| C-W006-VCMP01-03 | 7 | 对 category foundations 的一个反对意见被表述为其公理只给条件、没有 existential claims；作者以 ZFC 的 Infinity、Power Set、Replacement 都作 existential claims 作为对照，并提出ETCS/CCAF等回应。 | Power Set 是显式出现的理论接口，但这里是基础比较与竞争回答。 | 不能把作者对“existential claim”的陈述误写成 Power Set 的存在性追问尚未支付，或直接写成 P/Q 命中。 |
| C-W006-VCMP01-04 | 11–14 | independence、forcing、multiple universes 与模型解释都被作为 set-theoretic / categorical比较中的限制与回应处理；Grothendieck universe明确要求含自然数、传递性、pair／Power Set／union closure等条件，并连到 inaccessible universe、class-theoretic解释及 export back to V 的范围。 | 强 payment control：此处的 Power Set closure、universe、model transfer与结论范围由额外结构和特定解释明示承担。 | 不把 universe／模型讨论改写成 bare ZFC 或 ordinary ZFC consumer 的同一任务。 |
| C-W006-VCMP01-05 | 16–18 | canonical representative 的问题以不同 ordered-pair encodings及 `5∈7` 的 von Neumann／Zermelo difference 展开；Theorem 8的ETCS不变性明确限于无constants且只有指定集合自由变量的公式；作者将其写成一种有限语言范围的修复。 | 这是表示独立性、规范选择与同构不变性的精确控制，直接限制“表征差异就是理论悖论”的读法。 | 无固定 ordinary ZFC actual consumer、未支付 Done 或 formation-use reentry；不能成为 Q。 |
| C-W006-VCMP01-06 | 17 | 作者转述Voevodsky关于 ZFC 对 univalent languages 保持一致性保障角色的话。 | 是 HoTT–ZFC 关系的来源级背景，可与 HOTT-MOTIVE 既有来源对照。 | 该角色描述没有提供保真 `H0→Z0` 或同一任务的 ZFC 候选。 |
| C-W006-VCMP01-07 | 19–23 | 作者为结构主义目的引入三排序的 ZFCS 与 NBGS：明确写出Power Set等ZFCS公理，并附加structural richness / radical richness axioms；Theorem 18的invariance依赖这些语言、模型、witness、well-founded membership replacement与参数范围条件。 | 强反控制：为了获得特定结构性／isomorphism-invariance结果，作者换入了具有额外对象、排序和richness支付的理论框架。 | ZFCS/NBGS 不是 bare ZFC 的 ordinary consumer；不能把其由公理保证的镜像／替换描述成 ZFC 未付的自指过程。 |
| C-W006-VCMP01-08 | 23–24 | 结论把non-arbitrary representation、cardinality与多个开放问题保留在 `structural richness`、ambient material resources与未来研究的条件下。 | 把本文的最终身份固定为比较／模型建构／开放问题的来源，而不是理论级负结论。 | 书目与开放问题不自动产生新的work family、Q Lead或ZFC缺陷。 |

## R→Z→Q 资格状态

V-CMP-01 给出一个更精确的 representation / structuralism control：它确实把 material set theory、Power Set、canonical representation、ETCS、Grothendieck universes、ZFCS/NBGS与HoTT/UF的关系放到同一篇来源中，但每一个可能被误读为“ZFC 失败”的位置都带有范围、模型、语言、class、universe或structural-richness条件。本文没有交付一个版本固定的 ordinary ZFC actual consumer，也没有给出同一对象的 formation、预支使用、未支付 Done 或 P1/P2/P3 会合。

当前结论是 `SOURCE_PRECISION_GAIN / REPRESENTATION_AND_PAYMENT_CONTROL / Q_NOT_QUALIFIED`。它应作为未来 ordinary ZFC consumer 调查的反控制：任何声称由 canonical representation、Power Set、universe 或 structural invariance 得到 Q 的候选，都必须说明自己没有换到本文的 ZFCS/NBGS／ETCS／Grothendieck-universe task，且为何同一对象、操作、观察与 Done 仍未被来源直接支付。
