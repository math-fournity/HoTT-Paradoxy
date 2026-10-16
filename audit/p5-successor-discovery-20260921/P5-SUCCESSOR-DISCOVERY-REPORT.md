# P5-SUCCESSOR-DISCOVERY-001：首次四分支 pass 之后的后继选择

**状态：** `SUCCESSOR_SELECTED_P6_ORIGIN_STRUCTURE_COMPARISON / NO_NEW_HOTT_DEFECT_CLAIM`  
**日期：** 2026-09-21  
**输入状态：** P1、P2、P3 的各自冻结分母均已关闭；P4 未获触发资格。  
**本单元的唯一任务：** 不重复已经审过的 SIP、UniMath、D_ABX_1–3 或旧 proof run；比较新的入口，并选择一个能继续服务最终见证链的、可执行的下一分母。

## 1. 为什么必须继续，而不能把 first pass 当成总目标的停止

“`STOP_BY_DEFAULT`”只能约束**同一个已经冻结的分母**：继续搜索同一个 Book §9.8、同一个 UniMath 调用点或同一批 ABX 直接消费者，不会产生新的判词改变凭据。它不能关闭 active `/goal`，更不能把“未在这些分母找到 K”外推为“HoTT 没有问题”或“圆环研究没有后续”。

本单元纠正的是该控制语义，而不是改写 P1–P3 的结论：

- P1 已把 `RichCurve`、`Input`、`Denotes/Satisfies`、操作和双 Done 固定为一个**受限**的同任务代理；
- P2 只排除了 Book §9.8 的 SIP 自动把裸等价升格为 `Done_s`；
- P3 只审计了一个版本固定的 UniMath SIP 使用；
- P4 仍缺少同一规则的理论—实现语义差异。

因此下一步应寻找**未被上述分母表达的链边**，而不是机械扩大关键词、重跑内核或重复写无命中报告。

## 2. 本次固定的比较问题与防重复边界

### 2.1 固定问题

给定 ABX 的候选接口：

```text
OriginPresentation :=
  (C, p, M, N, e, boundary, closure-spec, operation-spec)
```

其中 `operation-spec` 包含允许过程、trace 与完成条件；`Done_strong` 要求指定 `C,p,e` 或来源保持等价和预注册观察。问题不是“普通同胚是否为假”，而是：**有无一个已有对象理论框架，可以精确承载这些字段，从而使后续 H/R/K 检验不必诉诸未固定的“现实历史”语言？**

### 2.2 防重复锚点

本次已核对下列本地资产：

| 已有资产 | 已经完成的范围 | 对 P5 的约束 |
|---|---|---|
| `ABX行动/003` §1–4 | `OriginPresentation` 只是候选接口；`U`、`Done_weak/Done_strong` 与 K 门槛已明定 | 不把接口本身重新包装为新理论或 HoTT 缺陷 |
| `ABX行动/004` §ABX-1–4 | `RichCurve` 是可检查代理；当前结果仅为表示边界与 K 检索的前置 | 不重做 `RichCurve` 或已存在的正反控制 |
| `H-R-K查找思路整备/005` | 完整 `OriginTop/R`、操作规格和与相对同伦/标记空间/cobordism/cohesion 的比较仍开放 | 对象理论比较是实际缺口，不是凭空新分支 |
| P1–P3 报告 | 受限任务、SIP 规则、UniMath 函子代数消费者已各自结束 | 不将相邻结构理论偷换为已找到 K |

## 3. 学术与社区侦察

本 wave 在选择前做了公开一手文献/社区资料检查，而非只依赖历史 AI 的说法。

1. Douteau 的 *Stratified Homotopy Theory* 将一个分层空间表为带连续映射 `X → P` 的空间，讨论只在**保持分层**的同伦下不变的量；它还说明此类对象与 simplicial-set diagrams 有联系。[论文摘要（arXiv:1908.01366）](https://arxiv.org/abs/1908.01366)
2. Douteau 的后续文章构造固定 poset 上分层空间的模型结构，并以分层同伦群刻画弱等价。[论文摘要（arXiv:1911.04921）](https://arxiv.org/abs/1911.04921)
3. Shulman 的 real-cohesive HoTT 工作在**额外的 cohesive/spatial 类型论**中，以 modalities 区分拓扑结构和同伦结构，并特别讨论“两个圆”的关系。[论文摘要（arXiv:1509.07584）](https://arxiv.org/abs/1509.07584)；作者对该模型与普通 HoTT 的边界说明见 [HoTT 社区文章](https://homotopytypetheory.org/2015/09/25/realcohesion/)。

这些来源没有声明已经解答 ABX 的 `OriginPresentation` 或给出 `H_top/U → Done_strong`。它们的作用是给后继候选提供准确的比较对象，并防止把“几何/分层结构是已知议题”误报为新发现或 HoTT 内部矛盾。

## 4. 四类入口比较

| 候选入口 | 已检查内容与最强反解释 | 对最终目标的价值 | P5 结论 |
|---|---|---|---|
| 新规则/模型：cohesive / real-cohesive HoTT | 它在附加 modality 的系统中显式区分拓扑与同伦；这正是对“普通 HoTT 未自动保留几何过程”的已知边界处理。最强反解释是：它是现成防御/富化模型，不是普通 HoTT 的错误。 | 可作为 P6 的比较控制，避免把缺失结构误称为理论漏洞。 | `KNOWN_DEFENSE_OR_BOUNDARY`；不单独重开 P2。 |
| 真实消费者：再找 SIP 用户 | P3 的 UniMath 函子代数调用已被版本固定审计；无新版本、入口、输入输出承诺时，继续扫描只是同一类关键词扩大。 | 仍是未来 K 的必要路径，但没有获得本 wave 的新分母资格。 | `NO_NEW_ADMISSIBLE_CONSUMER_SELECTED`。 |
| 来源—操作—复原对象理论 | `OriginPresentation` 已列出静态对象、指定点、去点对象、等价/嵌入、边界、闭合规格和过程；本地资产明确承认还没有与既有相对/标记/分层/cohesive 结构的保真比较。 | 直接补最终见证链的 `R_min → 可比较 R_origin` 边，使以后判断实际 K 是否换题成为可能。 | **选择为 P6。** |
| 理论—实现语义差异 | P1–P3 没有同一演算规则在理论与实现上相反的可重放结果。旧类型拒绝和配置差异不能代替该证据。 | 若未来出现，才是 P4；当前无有效输入。 | `NOT_TRIGGERED`。 |

## 5. 选定后继：P6-ORIGIN-STRUCTURE-STRATIFIED-COMPARISON-001

### 候选卡

| 字段 | 固定内容 |
|---|---|
| **要改变的判词** | 从“`RichCurve` 是受限代理，完整 `OriginTop/R` 未固定”推进到“哪些 `OriginPresentation` 字段可由标准标记/分层/相对对象保留，哪些仍需额外 diagram 或过程结构”。 |
| **精确问题** | 将 `(C,p,M,N,e,boundary,closure-spec,operation-spec)` 逐字段比较到：点标记/带基点对象、`X → P` 型分层对象、相对或 cospan/diagram 结构、cohesive 结构。不得预设任何一个框架必然不足或必然足够。 |
| **固定输入与观察** | 输入是 `OriginPresentation` 和当前 `RichCurve`/`Input`/`CurveRun` 代理；观察是字段是否作为对象数据、态射条件或过程/完成关系被承载；不是“看起来像圆/线段”。 |
| **正控制** | `reexpressed` 保留完整 `CurveData` 并满足 `Satisfies`；这防止把“富化结构”误说成不可传输。 |
| **最强反解释** | 可将全部字段编码为一个足够丰富的 diagram 或结构化对象；若该编码成立且结构等价保留所有字段，P6 必须承认普通 H 与富化 R 的差异在该模型中已被显式守住。 |
| **成功产物** | 一份字段—对象—态射—过程矩阵，外加 P7 可形式化的最小 diagram/interface；或一个有据的判定说明为什么当前候选不产生独立对象理论缺口。 |
| **禁止外推** | P6 不证明新拓扑学、HoTT 缺陷、现实复原不可能、或所有分层/相对理论都不足。 |
| **停止条件** | P6 的**比较分母**完成后关闭；若 active goal 仍未完成，须产生其 successor（P7 或另一条有界入口），而不能以“没有理论问题”停止目标。 |

### 为什么 P6 是当前最小而有价值的前进

它不把“现实同一性”直接塞进 HoTT 内部，也不要求先找到一个错误的库调用。它先把用户的要求从 `RichCurve` 的有限代理推进到可与现有数学对象理论逐项比对的规范。这正好服务最终目标的必要链边：只有已知 R 所保留的对象、态射、观察与完成条件，未来才能有意义地问某个 HoTT 规则或消费者是否把 `U(P)` 当成同一任务的充分完成。

同时，这条线有明确的失败模式：若比较表显示既有结构已经足以完整、自然地承载这些字段，结果是一个**防御或重述**，不是失败被隐瞒；后续应转去实际 K 消费者或由独立来源重定 R，而不是继续加形容词。

## 6. 波次反思与总体坐标

1. **新增可定位事实：** P5 把 `STOP_BY_DEFAULT` 的正确适用域固定为“已审分母”，并以公开文献和本地资产确认：分层/黏着结构是邻近而非同一任务；完整 `OriginTop/R` 比较是尚未完成的义务。
2. **判词变化：** P1–P3 的 scoped negative 保持；总计划从“first pass 停止”变为 `P5 complete → P6 active`。
3. **最终目标连接：** 本 wave 位于最终见证链的 R 端：它使“同一任务、来源、操作与完成”的规格可检验，尚未声称理论桥、实际 K、失配或 HoTT 缺陷。
4. **为何不延续旧分母：** SIP、固定 UniMath 调用和 D_ABX_1–3 已有正控制、范围与停止条件。重复它们只增加文件，不改变 K 的判词。
5. **为何延续 P6：** P6 对应本地已登记但未解决的 `OriginTop/R` 比较义务，且有独立数学对象理论作反解释控制；它能减少下一步是否“换题”的风险。
6. **未获资格的方向：** P4 仍未触发；新的实际消费者须先给出版本、入口和真实输入/输出，不能由 SIP 名称或相关论文标题获得资格。

## 7. 结论

`P5-SUCCESSOR-DISCOVERY-001` 已完成其 discovery 分母，并选定 `P6-ORIGIN-STRUCTURE-STRATIFIED-COMPARISON-001`。这不是目标停止，也不是数学结论；它是 active `/goal` 的下一条可执行、可证伪路径。
