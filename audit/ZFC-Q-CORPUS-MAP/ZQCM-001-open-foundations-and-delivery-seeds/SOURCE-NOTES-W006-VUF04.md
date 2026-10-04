# ZQCM-001 W-006 / V-UF-04 Source Notes — Bordg 2019

> **来源身份：** Anthony Bordg, *Univalent Foundations and the UniMath Library*, arXiv:1710.02723v7, dated 2019-11-17. Its title, author and year match the chapter listed as pp. 173–189 in *Reflections on the Foundations of Mathematics*. This acquired 18-page arXiv author version is **not** asserted to be byte-identical to that published pagination.
>
> **证据版本：** arXiv official PDF, SHA-256 `e3c6c206f872395747f11c47caa00643e48340c85a47aa21fdd8a9e477055473`; all 18 source pages and eight key 300dpi pages are recorded in [`VISUAL-REVIEW.md`](VISUAL-REVIEW.md).
>
> **状态：** FULL_AUTHOR_VERSION_UNIMATH_PAYMENT_AND_MOTIVE_CONTROL_SCREENED / SOURCE_ONLY_VISUAL_CHECK_COMPLETE / NOT_AN_ORDINARY_ZFC_CONSUMER / NOT_A_ZFC_Q / REMOTE_DERIVATIVE_NOT_QUALIFIED.

## 可消费的来源事实

| Source ID | PDF页 | 来源事实 | 对当前语料的作用 | 禁止外推 |
|---|---:|---|---|---|
| C-W006-VUF04-01 | 1–4 | 本文把UniMath置于proof checking、certified/type-checked proofs、MLTT、identity types、univalence、universes和h-levels的范围内；这些是作者描述的类型论和库的理论背景。 | 固定本文的主对象是HoTT/UF与Coq/UniMath，不是ZFC的内部操作记录。 | higher identity、universe或univalence术语不能自动转运为ZFC对象、formation或Q。 |
| C-W006-VUF04-02 | 5–8 | 作者将UniMath明确为Coq上的大型形式化数学库，说明其package范围；core/locked内容、UnivalenceAxiom文件、依赖追踪和`Print Assumptions`、以及LEM／AC以type形式保持为additional assumptions，均有明确来源表述。 | 给出一个实际proof-library怎样标出公理、依赖和已支付结果的正向控制。 | 这是UniMath/Coq的proof-layer consumer，不是ordinary ZFC actual consumer；显式公理追踪不能被反写为ZFC已承诺同样的program-like Done。 |
| C-W006-VUF04-03 | 8–11 | 作者说明CategoryTheory package、univalent categories与Rezk completion的范围，又把formalisation、ultimate foundations、库迁移和可扩展性明确区分。 | 形成“formalization practice与基础理论本身须分层”的来源控制。 | library可迁移性、search或协作困难不是对ZFC形成责任的证据，也不是P5预支使用。 |
| C-W006-VUF04-04 | 12–14 | architecture／wholeness、proof structure、library readability、code repair、communication和可折叠细节均作为formalized-library的设计／维护问题提出。 | 识别真实消费者，但把其输入、工作和完成条件限制为Coq/UniMath证明库的可读性、维护和证书。 | 不得把形式化库的工程困难改称ZFC公理层的矛盾、不可完成性或理论级Q。 |
| C-W006-VUF04-05 | 15 | 作者以架构／整体性比喻说数学从axioms向entities/theorems“unfolds”，并将h-level types与sets-based mathematics中homotopy types的呈现作比较，后者被说成较不直接／平滑。 | 这是可追溯的HoTT侧动机／比较表述线索，可为之后独立的`R_i→Z_i`文献地图提供定位。 | 它没有固定ZFC公理、版本、对象、formation、ordinary consumer、operation、observation或Done；不能从比较修辞直接推出ZFC Q。 |
| C-W006-VUF04-06 | 16–18 | Conclusion仍将风险与希望放在formalized-library的架构和持续维护；References提供HoTT、UniMath、Bourbaki集合论与Isabelle形式化的受限回溯入口。 | 将本文界定为来源定位和反控制，而非新work family自动生成器。 | 引用表、Bourbaki书目或结论修辞不单独升级为ZFC候选、Q Lead或数学结论。 |

## R→Z→Q 资格状态

V-UF-04 给出两类有用而彼此不能混同的材料。

第一类是**真实的 UniMath／Coq 消费者与支付边界**：其库包、locked core、`Print Assumptions`、明确列出的Univalence/LEM/AC条件和certificate-oriented proof checking，都使一个类型论形式化任务的依赖与交付范围可见。这是对“存在、可用、完成”在一个实际形式化系统中如何被显式区分和记录的控制来源。

第二类是**HoTT 侧动机／比较语言**：本文确实把h-level types、形式化库、集合基础的表述方式以及从axioms到theorems的“unfolding”放在同一叙述里。但这种语言没有把某个bare ZFC接口固定成同一任务，更没有给出待形成对象、理论内consumer预支使用、未支付Done或P1/P2/P3会合。

当前结论是 `SOURCE_PRECISION_GAIN / UNIMATH_PAYMENT_AND_HOTT_MOTIVE_CONTROL / Q_NOT_QUALIFIED`。后续若要把p.15的比较送入 `HOTT-MOTIVE-ZFC-SOP`，必须先以独立HoTT作者原典和固定ZFC侧来源补出精确的 `R_i → Z_i`；只有同一卡同时提供ordinary ZFC actual consumer、同一对象／操作／观察／Done，并跨过本笔记所示的显式支付边界，才可重开为Q候选。
