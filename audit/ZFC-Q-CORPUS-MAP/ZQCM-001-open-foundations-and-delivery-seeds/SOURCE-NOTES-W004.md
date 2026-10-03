# ZQCM-001 W-004 Source Notes — Fontanella, Geoffroy, Matthews 2024

> **身份：** FULL_PRIMARY_REALIZABILITY_LARGE_CARDINAL_CONTROL_SCREENED / SOURCE_ONLY_VISUAL_CHECK_COMPLETE / NOT_A_ZFC_Q。
>
> **原件：** `originals/Fontanella_Geoffroy_Matthews_2024_Realizability_Models_for_Large_Cardinals_LIPIcs_CSL2024_28.pdf`；DOI `10.4230/LIPIcs.CSL.2024.28`；CSL 2024, Article 28, pp.28:1–28:18；18页；SHA-256 `425e910298e062118483af2ba3de9f0cbfc397cd5ca6ace5484bdbeb6286fc0f`。
>
> **阅读边界：** official remote MinerU attempt `MIN-REMOTE-QUAL-004` returned `server_not_running`; no local service was started. This note uses the original PDF’s 18 source-only page records `VR-W004-001` through `018` and 300dpi checks on pp.1–7, 10, 13.

## 原件给出的精确结构

1. **pp.1–2：研究对象是条件性模型构造。** 文章将 realizability 说明为 proof/program correspondence，但明确把 ZF 及四类 large-cardinal axioms 的模型构造置于相对一致性假设之下。p.2还明确说，对于相关 AC realizability model，何为 explicit realizer 仍不清楚。
2. **pp.3–6：程序语义有清晰的外加载体。** 构造以 model `V` of ZF、realizability algebra `A`、`λ_c`-terms、stacks、processes、truth/falsity values、`ZF_ε`和其two membership relations为输入。`ZF_ε`被说明为ZF的conservative extension；realizability theory另依赖一组被选定的realizers与一致性条件。
3. **pp.7–9：ground-model 到 realizability-model 的迁移并不保持直接表示。** reish names／recursive names和relativization用于把ground-model properties移入模型；p.7明确说该方法一般不提供ground-model elements的straightforward interpretation。模型的对象、操作和观察层因此已不同于bare ZFC ordinary practice。
4. **pp.10–12：large cardinal 结果进一步依赖大型前提。** inaccessible、Mahlo、weak Power Set、second-order Collection及相对一致性被逐项写明；它们用于表明相应结构在realizability model中可被保持，不是从bare ZFC无条件取得的对象。
5. **pp.13–16：classes、Choice、embeddings与GB扩展均显式支付。** GB／`GB_ε`、two-sorted language、Class Separation／Collection、Choice、Löś theorem、elementary embeddings和critical points是构造的可见条件。文末将更大的realizability algebra情形保留为开放问题。
6. **pp.17–18：引用边界。** Krivine、Friedman、Kunen、Matthews 2023 (W-008)、Rathjen、Setzer、Suzuki与Williams等提供后续bibliographic leads；它们不自动成为ordinary ZFC consumer证据。

## 对 P5 与 ZFC Q 的处置

本来源加强了一个已出现的控制：**ZF-related proof/program semantics 可以在明确的realizability model中构造。** 因此“ZF必然没有计算或程序语义”不能作为未经限定的P5攻击句。

它同样没有满足本项目的Q门：

- 语义对象是`V`、`A`、`ZF_ε`／`GB_ε`、names、terms、stacks和模型语言的组合；
- large-cardinal结果依赖相对一致性、Choice、class structure或embedding等额外条件；
- source没有固定 ordinary bare ZFC 中同一对象、同一操作、同一观察和program-like Done的actual consumer；
- 也没有来源事实显示该ordinary consumer在Done未支付时预支使用对象。

当前处置为`MODEL_SEMANTIC_PAYMENT_CONTROL_NOT_Q`。未来只有一个版本固定的 ordinary ZFC consumer 同时跨越模型／语言／支付边界并保留同一任务时，才重新打开专门bridge；重复的realizability、large-cardinal或model关键词不重开。
