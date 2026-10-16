# P6-ORIGIN-STRUCTURE-STRATIFIED-COMPARISON-001：来源—操作—复原对象的比较

**状态：** `PARTIAL_REUSE / COMPOSITE_STRUCTURED_DIRECTED_DIAGRAM_CANDIDATE / P7_ORIGIN_DIAGRAM_SPEC_NEXT / NO_NEW_HOTT_DEFECT_CLAIM`  
**日期：** 2026-09-21  
**任务：** 比较 ABX 的 `OriginPresentation` 与已有的带标记、分层、相对 diagram/cospan、定向路径和 cohesive 结构；判明已有资产已经覆盖什么、仍缺什么，并避免把“富化表示存在”或“裸表示忘记字段”误写成 HoTT 缺陷。

## 1. 判词改变凭据与本次范围

P5 已冻结 P6 的问题：`RichCurve` 是来源—闭图的受限代理，尚未说明用户所需的完整来源—操作—复原任务能否由已有对象理论自然承载。本单元的判词只可能在下列两种方向上变化：

1. 若已有的单一结构已经自然承载全部字段，则“需要新的对象理论接口”的说法必须降格为 `KNOWN_DEFENSE_OR_REPRESENTATION`；
2. 若每个单一静态比较对象只承载一个真子集、而已有的结构化/定向组合给出可组合的承载方式，则下一步应当定义精确组合接口，不再泛称“现实历史”。

**本单元不检验** HoTT 内部矛盾、实际 K、完整物理复原、任何全称不可能定理，或新的证明助手实现差异。

## 2. 已有本地资产：P6 不是从零开始

P6 的本地侦察发现两组已经存在的、彼此互补的形式资产。它们是 `PARTIAL_REUSE`，不是 P6 已完成的全部对象理论。

| 资产 | 已检查的精确内容 | 对 P6 的作用 | 严格边界 |
|---|---|---|---|
| Lean `StructuredCurve.lean`，C-275–C-277 | `CurvePresentation` 显式保存开参数曲线、闭参数 completion、嵌入、连续性与内点一致；`PresentationEquivalence` 明确要求环境、参数、端标签和 completion 交换。裸 `BareCarrier` 有具体同胚，但不存在该具体强等价，也没有从任意 bare equivalence 自动运输端点重合。 | 给出 `boundary` 与一部分 `closure-spec` 的真实结构化正反控制。 | 这是经典实点集几何；它没有完整 `C,p,M,N,e,operation-spec,Done`，不等于 HoTT 的实际消费者。 |
| Cubical `GeometricBoundaryObservation.agda`，C-278–C-279 | `RichDiagram = Σ A, Bool → A` 显式保存边界图；忘记图后载体路径为 `refl`，却没有单一裸恢复；`ua` 与 `ΣPathP` 在**连同边界函数运输**时产生 Rich path。 | 给出原生 HoTT/Cubical 中“数据保留则可运输、忘却则不免费恢复”的窄控制。 | `Coord` 与 `Bool → Coord` 只是整数边界观察，不是整个实数圆、过程或用户的全部来源关系。 |
| `NativeSourceContract` / `NativeTaskIntegration` | `Satisfies` 区分 carrier 与闭图，`CurveRun` 以时间、联合连续、切片、初末图和空间界表达一个过程合同。 | 说明 `Done` 与 `operation-spec` 已有局部机器化，不必另造同义代码。 | `CurveRun` 是外部于 `CurvePresentation` 的合同；目前没有统一的 `OriginPresentation` 接口把它们全部联结。 |

本 P6 复核了上述 Lean/Cubical 源码的当前 SHA-256 与保存 run 的 source manifest：两套主要输入均匹配其保存的 `KERNEL_ACCEPTED_WITH_SCOPE` 收据。运行记录本身仍标为 `LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`，所以本报告不把它们升级为跨版本闭合的新数学结论。

## 3. 学术与社区比较对象

本 wave 重新查阅了与 P6 精确问题相关的公开研究，而不是从标题推断结论。

| 结构族 | 文献中的最小数据 | 与 P6 的关系 | 不能由它自动得到的东西 |
|---|---|---|---|
| 带标记/带基点空间 | 对象加指定点或指定子对象。 | 可表达 `C,p`，但“p 从 C 被去掉”、给定 `N→M`、边界图和操作都必须另加。 | 来源操作、trace、`Done`。 |
| `P`-分层空间 | `X → P`；等价/同伦需保持分层。 | 可把 `p` 或去点部分标成不同层，防止普通同伦随意遗忘该层。 | 单独的 `X→P` 不提供给定 `e:N→M`、一个执行过程或完成标准。Douteau 的工作把分层对象与保持分层的同伦作为独立研究对象。[Douteau](https://arxiv.org/abs/1908.01366) |
| exit-path 分层理论 | 除分层外可用 exit-path 构造记录由分层约束的方向性。 | 说明分层结构可有比静态分层更丰富的路径层。 | 仍须预注册什么算 execution、什么观察算完成；这些不由普通同胚或 `X→P` 免费决定。[Haine](https://arxiv.org/abs/1811.01119) |
| 相对/structured cospan | 一个 cospan 是显式图 `L(a) → x ← L(b)`；decorated cospan 还能在中间对象附加数据。 | 可直接容纳 `M ↪ C ← {p}`，并继续加入 `N → M`、端点/边界映射和 completion decoration。 | cospan 本身不是时间过程；trace 与 Done 仍需作为 decoration 或 time-indexed diagram 加入。[Baez–Courser](https://arxiv.org/abs/1911.04630), [Baez–Courser–Vasilakopoulou](https://arxiv.org/abs/2101.09363) |
| 定向空间 / directed paths | d-space 是空间加一族在组合等操作下封闭的定向路径。 | 精确对应 `operation-spec`/trace 的候选承载；它避免把方向性压成可逆普通路径。 | 指定 `C,p,M,N,e` 和 `Done` 仍是附加数据或谓词。[Grandis](https://arxiv.org/abs/math/0111048) |
| 定向类型论 | 新的 homomorphism type former 试图表示范畴态射和定向路径；这是一种额外类型论结构。 | 说明“过程/方向”有成熟的类型论研究路线，不能草率说为不可形式化。 | 它不是基本 HoTT 的自动含义；使用它必须明确理论扩展与消费者。[North](https://arxiv.org/abs/1807.10566), [Gratzer–Weinberger–Buchholtz](https://arxiv.org/abs/2407.09146) |
| real-cohesive HoTT | 以额外 modalities 区分拓扑与同伦结构。 | 是“几何信息不应自动压成纯同伦信息”的已知模型控制。 | 它不自动指定本任务的删点来源、执行 trace 或 `Done_s`，也不是普通 HoTT 的内部缺陷。[Shulman](https://arxiv.org/abs/1509.07584) |

## 4. `OriginPresentation` 字段矩阵

当前候选接口是：

```text
OriginPresentation :=
  (C, p, M, N, e, boundary, closure-spec, operation-spec)
```

下表的“可承载”始终表示“在显式加入该字段后可承载”，不表示某一理论会从裸同胚自动推导它。

| 字段 | 现有本地结构 | 带标记 / 分层 | 相对或 cospan diagram | 定向/过程结构 | P6 判定 |
|---|---|---|---|---|---|
| `C` 指定闭合对象 | `Plane` 与 completion 的像仅部分给出 | 带基点空间或 `X→P` 的底空间可承载 | cospan apex 可取 `C` | 可作为 d-space 的底空间 | 可承载，但必须作为显式对象字段。 |
| `p` 指定被去掉点 | 具体模型有 `pole`，一般 `CurvePresentation` 没有此字段 | 带标记/零维 strata 可承载 | `{p}→C` 直接承载 | 不是定向路径自身给出的 | `p` 不能从 bare carrier 推回；需要标记/inclusion。 |
| `M` 去点呈现 | `mPresentation` 是局部具体呈现 | 可作为子空间/stratum | `M↪C` 是 diagram 的一条箭头 | 可给 `M` 加定向路径 | 需要与 `C,p` 的关系，而非只给抽象同胚类型。 |
| `N` 与 `e:N→M` | `nPresentation` 与 `concreteBareHomeomorph` 已出现，但 `e` 不在 generic record 中 | 单层标记不足 | `N→M→C` 可显式保存；可要求 `e` 为等价/嵌入 | 可在 `N` 上再指定可行路径 | 单一 pointed/stratified object 不够；diagram 是自然候选。 |
| `boundary` | Lean `boundary : Bool→Plane`、Cubical `Bool→Coord` 已精确承载 | 必须另加 boundary map | 可写为 `∂N→C` 或 decoration | 可指定路径端点 | 已有强 `PARTIAL_REUSE`，但不是完整对象。 |
| `closure-spec` | `completion`、连续性、内点一致已承载；`BoundaryCoincident` 是一个观察 | 层/标记本身不含 completion | 可作为 diagram 的 map/commuting condition | 可要求过程末态满足 | 目前只覆盖“闭图”子规格，未覆盖完整指定 `C,p,e`。 |
| `operation-spec` / trace | `presentationAt`、`CurveRun` 已在相邻合同中承载，但不在 `CurvePresentation` 自身 | 静态标记/分层本身不含执行 | 需 time-indexed 或 decorated diagram | d-space/定向类型论最贴近该字段 | 不能从普通同胚、univalence 或静态 stratification 自动获得。 |
| Observation / `Done_s` | `Satisfies`、`BoundaryCoincident` 是两类局部观察 | 需要明确谓词 | 需要 decoration/acceptance relation | 需要预注册终止/成功谓词 | 绝非任一上述对象自动生成。 |

## 5. P6 的关键结论

### 5.1 不是“必须发明新拓扑学”

现有数学确实提供了足够丰富的构件：标记对象保留点，分层对象保留 strata，cospan/relative diagram 保留指定嵌入与边界图，定向结构保留过程方向，cohesive 模态保留额外几何层。因而“无法表示来源或过程”不是可成立的总判词。

### 5.2 也不是“普通同胚已经完成全部任务”

同样明确的是：每一类单一、较弱的数据只保留矩阵中的一部分。当前本地正反控制已经说明，若只忘记到 `BareCarrier`，端点重合/闭图不随 bare equivalence 自动运输；若连同结构字段运输，则结构保持等价可以成立。故真正的断点是**忘却后的任务升级是否发生**，不是普通 `H_top` 本身逻辑矛盾。

### 5.3 最小充分对象候选

P6 选择的最小后继不是一个新“空间类型”，而是一个组合接口：

```text
OriginDirectedDiagram :=
  static diagram:     M ↪ C ← {p},  N ─e→ M,  ∂N ─boundary→ C
  closure decoration: closure-spec with its specified commuting laws
  process decoration: directed/time-indexed trace satisfying operation-spec
  observation layer:  Obs and Done_s
```

这只是**P7 的规格候选**。它没有声称这一对象已经被完整形式化，也没有声称它不可由任何现有框架编码。它的价值在于把“现实同一任务”拆成可审查的对象、箭头、过程和完成层。

## 6. 波次反思与下一选择

1. **最终目标连接：** P6 服务最终见证链的 R 端，固定未来 K 审计必须观察的字段；它不越级为 HoTT 缺陷证明。
2. **新增事实：** 本地 C-275–C-279 已经是 `OriginPresentation` 的局部静态结构和运输控制；社区已有分层、cospan、定向与 cohesive 方案。此前“尚未比较”不等于“尚未有结构”。
3. **反解释是否成立：** 成立。一个 decorated、time-indexed/定向 structured diagram 可以原则上承载全部字段；任何后续工作都必须允许该模型成为防御。
4. **为何不继续 P6：** 已有比较对象、字段矩阵、正控制、反解释和范围结论均已固定。继续增加同义数学名词不会改变其判词。
5. **为何需要 P7：** 当前 `OriginPresentation` 仍是散列在 `RichCurve`、`CurvePresentation`、`RichDiagram` 与 `CurveRun` 中的候选接口。P7 应只写一个最小、可映射到这些既有资产的 `OriginDirectedDiagram` 规格，并明确 `U`、`Obs`、`Done_s` 与保结构态射；不得重写现有几何或另造一份同义证明。

## 7. P6 结论

`P6-ORIGIN-STRUCTURE-STRATIFIED-COMPARISON-001` 以 `PARTIAL_REUSE` 完成。它给出的不是 HoTT 败诉结论，而是一个更严格的研究边界：**用户所关心的差异可由现有对象理论的组合结构表达；裸同胚不是组合结构的替身；是否存在 HoTT 的实际 K 把前者当成后者，仍须另行证明。**

当前 successor 是 `P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-001`。
