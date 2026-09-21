# P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-001：最小 R 与 K 准入合同

**状态：** `K_HARNESS_ACCEPTED_WITH_SCOPE / P8_DIRECTED_TYPE_THEORY_IMPLEMENTATION_DISCOVERY_NEXT / NO_NEW_MATHEMATICAL_CLAIM`  
**日期：** 2026-09-21  
**任务：** 把 P6 的字段矩阵变成一个足以判定未来实际消费者 K 是否换题的最小合同；不新增几何模型、不重跑既有证明，也不把规格本身当作 HoTT 缺陷。

## 1. 本 wave 为什么仍值得做

P6 已证明两件互补的事实：

1. 现有结构化/定向对象可以显式承载来源、边界、过程与完成的字段；
2. 裸 `BareCarrier` 或通常同胚不自动携带这些字段。

但“字段矩阵”仍不足以筛选一个实际 K：没有统一的输入、输出和 `Done_s` 合同时，审计者可以在发现某个 HoTT 调用之后才把额外要求补进去。P7 的唯一新增价值是冻结这个**事前**准入合同。

### 学术与本地资产复核决定

本 P7 没有重复网络搜索。P6 刚刚针对本接口的构件完成了有界的一手文献检查：分层、cospan、定向类型论与 cohesive 理论已经覆盖了 P7 所使用的结构名称。P7 不主张一个新理论比较或新外部事实，而是把 P6 的既有对象分解映射到本地 `CurvePresentation`、`RichDiagram`、`CurveRun`、`Input/Satisfies`。重复检索不会改变本 wave 的 `K` 准入命题。

本地侦察确认：这些接口和 C-275–C-279、C-295–C-296、C-320 已经分别保存；P7 只引用它们的已声明范围，不创建第二份同义 formal source。

## 2. 最小 `OriginDirectedDiagram` 规格

下列是**接口规格**，不是声称已在一个特定 proof assistant 中完成的定义：

```text
OriginDirectedDiagram D :=
  Static(D):
    C : ambient / specified closed object
    p : marked point of C
    M ↪ C : punctured or structured subobject
    N ─e→ M : stated equivalence or embedding
    ∂N ─boundary→ C
    closure : ClosedParameter → C
    closure laws: interior agreement + registered endpoint/closure laws

  Process(D):
    trace : Time / directed path / transition family
    operation-spec : allowed operations and preservation obligations

  Observation(D):
    Obs(D, output)
    Done_s(D, output) := the registered strong completion predicate
```

### 结构保持关系 `R_ODD`

`R_ODD(D,E)` 需要一组显式、相容的结构等价/态射：

1. `C,M,N` 的指定结构保持映射；
2. `p`、`M↪C`、`e`、边界和 closure 交换；
3. trace/operation 的合法运输或保留；
4. `Obs` 与 `Done_s` 的保留。

因此 `R_ODD` 不等于“底空间同胚”，也不等于只给 `N≃M`。它允许后来精确回答：某个理论调用是保留全部结构，还是只消耗某个 forgetful image。

### 忘却映射的精确层次

```text
U_bare(D)      = K 真正可见的裸载体、同胚或等价数据
U_static(D)    = 去掉 process/Obs/Done 后的静态图
U_full(D)      = D 本身
```

这些层次不得混用。一个调用如果接收 `U_full(D)`，就已经获得了来源、边界与过程；它不是 ABX 所寻找的“裸输入被升格为强完成”。

## 3. 可执行的 K 准入判别器

一个版本固定的理论规则、库函数、证明器接口或应用调用 `K`，只有同时满足以下条件才可进入未来的同任务失配检验：

| 条件 | 必须有的直接证据 | 不足以满足的材料 |
|---|---|---|
| `K-input` | K 的实际输入只经 `U_bare(D)` 或其明确的 `H_top` 结果获得 | 代码/论文提到同胚、univalence、stratification 或 directed path |
| `K-output` | K 的返回值、定理结论或下游承诺可定位 | 仅证明 `isUnivalent`、存在某个等价或完成一个无关任务 |
| `K-claim` | 调用方确实把该输出作为同一 `Done_s(D,output)` 的完成 | 审计者事后附加 `Done_s`，或只有弱 `Done_weak` |
| `K-forgetting` | K 的输入路径没有已经传入 `p`、boundary、closure、trace、Obs 或 Done 的等价信息 | 输入在源代码中只是一个大 record、函数闭包或隐式上下文，尚未逐字段展开 |
| `K-version` | 精确 repository/paper version、入口、调用链和环境 | 标题、关键词、历史 AI 自述或无版本网页 |

只要任一项失败，结果是 `DEFENSE_PRESERVES_TASK`、`TASK_DISTINCT`、`NOT_A_CONSUMER` 或 `NO_K_WITHIN_DECLARED_DENOMINATOR`，不是 HoTT 缺陷。

## 4. P7 与既有局部控制的映射

| P7 字段/判别 | 可复用资产 | 具体作用 |
|---|---|---|
| 静态 boundary / closure | Lean `CurvePresentation` | completion、端点和 `PresentationEquivalence` 已具体表达。 |
| `U_bare` 与强结构差异 | `BareCarrier` / `RichDiagram.forgetBoundary` | 相同裸载体不自动恢复不同边界/完成图。 |
| `R_ODD` 的正控制 | `ambientTransportEquivalence`、`reversePresentationEquivalence`、Cubical `transportDiagram` | 字段同行运输时，保结构关系可成立。 |
| `Process` | `CurveRun` | 同一 n/m 对在明确过程合同下可有 curve run，而在另一环境 `Success` 合同下不成立。 |
| `Obs/Done_s` | `Satisfies` / `Denotes` / `bareCheckIsInsufficient` | 仅检查 bare target carrier 不足以保证完整闭图观察。 |

这使 P7 的 K 判别器不是新加的哲学要求：每项都能映射到已有代码、已保存 run 的范围，或在未来真实调用中被直接检查。

## 5. 反“同义堆砌”审计

P7 的强反解释是：这份规格可能只是 P6 字段矩阵的重新排版，不能生成任何新的可判定事实。

**审计结果：不是纯 `RESTATEMENT_ONLY`，但只在受限意义上通过。** 新增的是一个事前可否证的 K 准入合同：任何未来候选必须同时通过 `K-input / K-output / K-claim / K-forgetting / K-version` 五项，而不是只因主题相近入场。它没有产生新数学定理、没有发现 K，也没有改变既有 H/R 控制的范围。

因此 P7 的可交付判词是 `K_HARNESS_ACCEPTED_WITH_SCOPE`。这个“通过”只表示未来消费者审计有了可重放的 admission criterion；不表示 `OriginDirectedDiagram` 已被完整形式化，更不表示 HoTT 曾违反此合同。

## 6. 下一分母：P8-DIRECTED-TYPE-THEORY-IMPLEMENTATION-DISCOVERY-001

P8 的任务不是立即指控 directed/simplicial type theory。它先要完成一个新的、版本固定的 discovery 分母：

1. 搜索公开实现、库或论文附带代码，固定一个实际 directed/simplicial type-theory 工具或消费者；
2. 对照 P7 的五项 K 准入条件，判定它是显式保留方向/结构的防御、任务不同，还是有资格成为实际 K；
3. 不把“有 directed path type”或“有 directed univalence 论文”本身当作 K；
4. 若无合格实现/消费者，关闭该 discovery 分母并继续生成不重复的 successor。

P8 值得优先的理由是：P6 说明 `operation-spec` 需要定向结构，而 P7 已把“裸输入 → 强 Done”写成可审计条件。它可以直接检验最接近过程/方向的类型论实践究竟显式付费，还是是否有真正的任务升级。

## 7. 结论与波次坐标

P7 结束的不是 active Goal，而是“把分散的 R 字段收敛为 K admission harness”这一个分母。它的总体坐标是：

```text
R 的字段矩阵（P6）
  → 事前 K 准入合同（P7）
  → 版本固定的 directed-type-theory 实现/消费者 discovery（P8）
```

它保留最关键的双向纪律：完整结构被显式传入时，理论可以正确保留任务；只有真实消费者将 `U_bare` 当作 `Done_s` 时，才可能形成 HoTT 相关的失配证据。
