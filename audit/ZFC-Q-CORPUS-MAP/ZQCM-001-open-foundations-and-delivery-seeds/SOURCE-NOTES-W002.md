# ZQCM-001 W-002 Source Notes — de Jong 2023

> **身份：** `FULL_PRIMARY_PREDICATIVE_UF_AND_POWER_SET_PAYMENT_CONTROL_SCREENED / SOURCE_ONLY_VISUAL_CHECK_COMPLETE / NOT_A_ZFC_Q`。
>
> **原件：** Tom de Jong, *Domain Theory in Constructive and Predicative Univalent Foundations*, arXiv `2301.12405v8`；192页；SHA-256 `1a6d697a3c1ea6183017b70b7f185cdcc6571e51597af521b4eb8f2895e1b160`；[`PDF-VALIDATION.md`](PDF-VALIDATION.md) 中的 `ZQCM-ACQ-002` 已确认它为官方 arXiv 版本。
>
> **阅读边界：** `MIN-REMOTE-QUAL-009` 返回 `FAILED_SERVER_NOT_RUNNING`，没有产生可消费的 remote MinerU 导出，也没有启动或重配可能与桌面应用共享的服务。本记录只消费原 PDF 的 `VR-W002-001`–`VR-W002-192`；关键定义、量词、公式、完成条件、formalisation 范围和结论页另有150dpi之后的300dpi复核，详见 [`VISUAL-REVIEW.md`](VISUAL-REVIEW.md)。

## 原件给出的精确结构

1. **pp.59–76：predicative domain theory 不是把经典总对象直接交付。** 作者以 universe 参数、subsingleton/proposition、directed family 和 local smallness重新表述 dcpo。p.60 说明某个朴素 dcpo 读法会导向 weak excluded middle；p.61 区分“存在一个共同上界”与为每对索引指定一个 `k`；p.63 的 powerset dcpo、p.68 的 `is-defined`／`value`、p.69 的逻辑等价和 type equivalence 都明确携带其相应的 universe、truncation、univalence 或 structure 条件。

2. **pp.77–86：递归、极限与未给定 witness 有原生支付。** least fixed point 写为 \(\mu(f)=\bigsqcup_n f^n(\bot)\)，并在 PCF 模型中表示一般递归与 bottom。p.80 的一般 directed 情形先证明依赖尚未选定共同上界 `k` 的表达式为常量，之后才经 propositional-truncation factorisation 使用它；对 \(I=\mathbb N\) 才可明确选取 `i+j`。这是一条直接的 `P5` 反控制：来源没有预支使用一个尚未交付的选择。

3. **pp.87–121：存在、结构、商和有限性都被分层处理。** structural continuity 含指定的 approximation data，continuity 只要求命题截断后的存在，pseudocontinuity又进一步改变其存在位置；p.97–99明确列出反向蕴含所需的 global Choice 或 Choice。p.90–91将 powerset 的 compact elements 精确识别为 Kuratowski finite subsets。p.105说明 list-to-powerset map 不为 embedding，有限子集纳入小 universe 需要 set replacement，而 lifting 的 small compact basis 与 propositional resizing 等价。

4. **pp.122–138：PCF 的实际语义消费者有明确的完成合同。** p.127–128给出 PCF 的 operational／denotational semantics、partial-element interpretation 和小步关系；p.129–130先区分 raw inductive pre-relation 与经 truncation 后的 proposition-valued relation。p.132的 computational adequacy 以 `is-defined(⟦t⟧)` 为前提，才推出归约到 `value(⟦t⟧,p)` 所给 numeral。p.134明确说构造性等待可无限期、固定 timeout 不给足够步数；要保证结果，应向 adequacy 提供 totality proof。p.135–137再把 definedness 化为可给有限步数的 semidecidability，并列出可判等、single-valuedness和可判 fibre 的前提。

5. **pp.139–156：Power Set、Replacement、smallness 与 totality 的关系被作者显式限制。** p.139–148把 large/nontrivial complete posets、decidable equality、weak/full excluded middle和resizing逐一联系，但都是 predicative UF 内部的 if-and-only-if 条件。p.140–143区分“对所有 subsets 有上确界”和“对所有小 index families 有上确界”；对 powerset，`A≠B` 与给出 \(x\in B, x\notin A\) 不是同一强度。p.153直接说 set replacement 与 small set quotients 等价；p.154–155又区分 covered subset 与 small subset，并说明从前者到后者需要 replacement。这里最有价值的过程事实是：最小不动点的自然数轨道可以是 `U₀`-covered，但在没有 set replacement 时并不自动是 `U₀`-small。

6. **pp.157–163：formalisation 和开放问题的边界有来源自身的说明。** Coq/UniMath 的 `Type-in-Type` 设定不能自动核验作者关心的 universe 条件，因此相关部分在 Agda/TypeTopology 中单独形式化；p.158还明示某些应用尚未形式化。结语最后把“propositional resizing 能否具有 computational interpretation”列为一个基础而开放的问题。它是 univalent-foundations 的来源问题，不能替换成已经定位的 ZFC Q。

## 对模式 P、Power Set 与 ZFC Q 的处置

W-002 是一份强的 **payment control**，而不是 ordinary ZFC 的反例来源：

- **P1/P2：** source 反复将 universe relative object、raw structure、truncated property、specified witness、relation 与 quotient 分开；不能从“有某种存在”跳到“同一对象可在同一层按任意方式使用”。
- **P5：** `is-defined`、`value`、totality proof、finite reduction witness、constant-before-truncation-factorisation 和 covered-vs-small 都给出了明确的交付先后关系。来源没有出现 ordinary ZFC consumer 在自己的 program-like Done 尚未支付时预支使用对象。
- **Power Set／Replacement：** 该文提供的不是“Power Set 出问题”的证据，而是未来任何候选必须跨越的控制：powerset construction、small set quotient、set replacement、universe location、membership decidability及实际消费者的 Done 必须在同一张卡里保留；不能把 types 内的 `𝒫_𝒱(X)`、CZF式规则、模型层或证明助手实现静默投影为 ZFC 的同一任务。
- **H0→Z0：** universe-level identity、truncation与univalence的机制属于类型论侧；它们可帮助定义需要防止的错误类比，不能直接给出 ZFC 侧对应物。

当前处置为 `FULL_PRIMARY_PREDICATIVE_UF_AND_POWER_SET_PAYMENT_CONTROL_SCREENED / NOT_A_ZFC_Q`。重开条件是一个版本固定的 **ordinary ZFC** 来源或实际消费者，同时固定对象、formation、操作、观察与 Done，并显示其形成／使用交错或未付完成条件没有被同一任务中的 Power Set、Replacement、明确 witness、模型、语言层或指定规则直接支付。

## 已登记的受限后向入口

pp.164–180的书目提供了可追溯入口，包括 de Jong/Escardó 的 set quotient／set replacement、semidecidability、small ordinals、PCF formalisation和 TypeTopology work。它们仅被登记到 `ZQCM-NET-007` 的候选分母；题名、引用关系或同作者关系本身不能扩张为新 work family 或 Q Lead。
