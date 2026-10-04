# ZQCM-001 W-006 / V-UF-05 Source Notes — Rodin 2018

> **来源身份：** Andrei Rodin, *Models of HoTT and the Constructive View of Theories* (2018-03-05 PhilSci-Archive author preprint). The title, author, opening abstract and subject matter match the chapter listed as pp. 191–219 in *Reflections on the Foundations of Mathematics*. The acquired 40-page author preprint is **not** asserted to be byte-identical to that published pagination.
>
> **证据版本：** PhilSci-Archive author preprint, SHA-256 `8da304c14e2e968673d1bace05d67d4a93858741ab4f15312e29ac1dbdc7fa84`; all 40 source pages and ten key 300dpi pages (1, 8, 12–14, 18–20, 34, 37) are recorded in [`VISUAL-REVIEW.md`](VISUAL-REVIEW.md).
>
> **状态：** `FULL_AUTHOR_PREPRINT_HOTT_MODEL_THEORY_AND_POWER_SET_RULE_VS_EXISTENTIAL_SOURCE_SCREENED / SOURCE_ONLY_VISUAL_CHECK_COMPLETE / HOTT_MOTIVE_AND_POWER_SET_RULE_VS_EXISTENTIAL_SOURCE_SEED / NOT_AN_ORDINARY_ZFC_CONSUMER / NOT_A_ZFC_Q / REMOTE_DERIVATIVE_NOT_QUALIFIED`.

## 可消费的来源事实

| Source ID | PDF页 | 来源事实 | 对当前语料的作用 | 禁止外推 |
|---|---:|---|---|---|
| C-W006-VUF05-01 | 1–8 | 文章提出以 methods 而非仅 statements/models 表示科学理论的“constructive view”；它区分 justification、heuristic discovery、explicit knowledge-how、rules/algorithms 与标准 Tarski/Hilbert 架构。作者同时把这定位为科学理论表示的哲学／方法论提案。 | 这是可追溯的 HoTT 创建动机与方法表示来源，说明本文的首要对象是科学理论与 HoTT/MLTT，而不是 bare ZFC 的内部计算。 | “方法”“过程”或“algorithm”词语不能自动提供ZFC对象形成、ordinary consumer、same task或P5预支使用。 |
| C-W006-VUF05-02 | 9–13 | 作者给出 syntactic rule、finite derivation、axiom/hypothesis/rule、formal theory 与外部 verification 的区分；pp.12–13 对 usual foundations 和 effective proof checking 的批评属于作者的认识论／元逻辑论证，并明确区分 ZFC-formalizability 与 informal-proof correctness。 | 将“proof checking”类 HoTT 动机固定为来源主张和比较边界，避免把哲学批评误当作已推出的 ZFC 矛盾。 | 本文没有在此固定 ZFC 中的证明器、输入、运行、观察或完成条件；不能把它当作本项目对ZFC的机器证明或Q。 |
| C-W006-VUF05-03 | 14 | 作者把给定集合的 `P(A)` 比作可被“thought of”作出的 set-theoretic construction，又说这种 set-theoretic construction 缺少可表示 extra-logical methods 的 formal rules；Power Set axiom 被表述为对任意 given set 的 powerset 存在保证。 | 这是当前 Power Set 站位最接近的一份作者性 **R/source seed**：它直接给出“规则式构造”与“存在公理”之间的对照，足以导向后续的版本固定 ZFC 侧核查。 | 这并非ZFC内部不一致、也不证明Power Set不能被使用。本文未给同一bare-ZFC consumer、operation、observation、Done或模式P会合，不能称Q。 |
| C-W006-VUF05-04 | 15–25 | 文章把 Hilbert–Tarski、Gentzen、MLTT、Curry–Howard、judgement/proposition、identity type、h-level、truncation、Univalence 和 Cubical Type Theory 分层讨论。pp.18–20把 `a:A` 的 proof/construction/realizer/BHK-task readings 和 intensional identity 的多层结构放在类型论内部。 | 形成 HoTT 侧的完成／identity／higher-structure动机背景，并把它与ZFC侧Power Set语句隔开。 | 类型论中的 proof、identity、path或“unlimitedly continue”不保真地转运为ZFC的时间、Power Set形成或Q。 |
| C-W006-VUF05-05 | 26–35 | 作者说明其 HoTT model theory 仍在当时的 work-in-progress 状态；pp.31–32将ZF作为研究HoTT模型的 established foundational basis，并将UF作为可选的自身元理论。pp.33–35讨论 contextual categories、generic model 与 Initiality Conjecture，后者在写作时仍被报告为open的 framework-building problem。 | 这是理论／元理论分层的强反控制：Z(F)在该文是外置模型基础，而不是被展示为从内部预支未形成对象。 | 不能把external ZF modeling、UF meta-theory选择、initiality conjecture或旧时态的open-status倒转为ZFC自身的ordinary consumer或当前数学结论。 |
| C-W006-VUF05-06 | 36–37 | 结论把 proposed constructive view 明说为 imprecise，并将用HoTT表示科学理论称为 philosophical speculation rather than concrete technical proposal；文中对standard set-theoretic/first-order setting 的不足是作者性比较主张。 | 给出这份R-source自身的证据上限，并防止其成为“HoTT优于ZFC”的无条件结论。 | 不得把作者的比较、愿景或有效形式化期待写成社区共识、ZFC形式矛盾、ordinary ZFC actual consumer或Q。 |
| C-W006-VUF05-07 | 38–40 | References连接Cartmell、Lawvere、Martin-Löf、HoTT Book、proof-theoretic semantics、truth-making、Tarski和Tsmentzis等材料。 | 形成HoTT模型论与建构主义的受限backward map；其中条目可在符合冻结语料准入规则时独立取得和资格化。 | 引用表不是被引作品内容、版本证据、ZFC实际消费者或Q Lead。 |

## R→Z→Q 资格状态

Rodin 的第14页给出一个值得保留、但必须严格降格的来源结构：在作者关于科学理论方法表示的语境中，`P(A)`可被谈作一种构造，Power Set axiom 却被作为对其存在的保障；作者认为前者不携带可表达 extra-logical methods 的规则。这个对照能作为未来 `R_i → Z_i` 的种子，因为它直接点到了 Power Set，而不是只泛泛比较“集合论”和“类型论”。

它尚未形成 `Z_i`，更没有形成 `Q_i`。原因不是该对照不重要，而是本文没有固定 bare ZFC 内同一个对象的 formation、ordinary consumer、操作、观察和Done；其主任务是科学理论的表示与HoTT模型论，且正文把Z(F)作为外部模型基础，把很多比较明确保留为哲学推测。因此当前结论为：

```text
HOTT_MOTIVE_AND_POWER_SET_RULE_VS_EXISTENTIAL_SOURCE_SEED
  / ORDINARY_ZFC_CONSUMER_MISSING
  / SAME_TASK_AND_PAYMENT_MISSING
  / Q_NOT_QUALIFIED
```

下一项可证伪行动不是把这个作者的语言外推为ZFC缺陷，而是寻找一个版本固定的 ordinary bare-ZFC consumer，并检验它是否同时满足：给定 `u`、formation `F`、操作、观察和Done；其使用是否真的依赖尚未支付的形成；以及它能否避开本文和 V-SET-01 所展示的外置模型／元理论／支付边界。否则这份来源继续只作为 Power Set 邻域的动机与防跳跃控制。
