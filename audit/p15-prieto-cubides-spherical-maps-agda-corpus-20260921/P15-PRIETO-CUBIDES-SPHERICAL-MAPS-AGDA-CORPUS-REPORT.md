# P15-PRIETO-CUBIDES-SPHERICAL-MAPS-AGDA-CORPUS-001：固定 Agda 语料的 K_app 审计

**状态：** `NOT_A_CONSUMER_WITHIN_FIXED_P15_PAGES / DEFENSE_EXPLICIT_MAP_FACE_WALK_SPHERICAL_DATA / TASK_DIFFERENT_FROM_P13_MN_DONE / P16_FOURTH_SUCCESSOR_DISCOVERY_NEXT / NO_NEW_HOTT_DEFECT_CLAIM`

**日期：** 2026-09-21

## 1. 判词改变凭据

P14 只冻结了候选身份，尚不知道其 HoTT/Agda 形式化是否会把 bare `H_intrinsic` 当成 P13 的 `Done_ambient^fin` 或 `Done_curve`。P15 读取固定论文上下文和五个作者发布页面，发现该语料的核心关系始终以组合图的 `Map G`、face、walk、节点判定和 spherical witness 为参数；它没有将原圆去点 `M/N` 的内在同胚作为输入，也不输出 P13 的两个复原完成条件。

这使 P15 成为一个新的、版本固定的实际消费者分母的有界否定结果，而不是关于 HoTT 或所有嵌入理论的否定结果。

## 2. 固定公开来源的直接读数

- [论文摘要](https://arxiv.org/abs/2112.06609) 说它以 combinatorial maps 表示图到曲面的嵌入（surface 保持隐含），并研究 walk homotopy、normal form 和 spherical maps；这已经与 P13 的点集 `M/N`、整平面有限 homeomorphism 或逐时曲线 embedding 是不同对象域。
- [发布总页](https://jonaprieto.github.io/synthetic-graph-theory/CPP2022-paper.html) 标明 Agda `2.6.2.2-442c76b`、页面版本 2023-01-22、提交短标识 `57c278b4`，并显式导入 Map、Face、walk homotopy、Spherical 和 Spherical-is-enough。结果表将 `Map`、`isSphericalMap` 与 `spherical-equiv` 逐项列为论文内容。
- [Map 页面](https://jonaprieto.github.io/synthetic-graph-theory/lib.graph-embeddings.Map.html) 定义 `Map G` 为对每个 node 的 `Star G` 给出的 `CyclicSet`；同页把它别名为 `CombinatorialEmbedding`、`RotationSystem`、`CellularEmbedding` 和 `CombinatorialSurface`。这不是 bare graph-equivalence，更不是 bare `H_intrinsic`。
- [walk-homotopy 页面](https://jonaprieto.github.io/synthetic-graph-theory/lib.graph-embeddings.Map.Face.Walk.Homotopy.html) 的 `HomotopyWalks` 模块显式接受 `𝕄 : Map G`。其中 `collapse` 明确接受 `Face G 𝕄`。操作所需的 map/face 数据没有被隐去。
- [Spherical 页面](https://jonaprieto.github.io/synthetic-graph-theory/lib.graph-embeddings.Map.Spherical.html) 定义 `isSphericalMap : Map G → Type`，所以球面判词仍由具体 map 参数化。
- [Spherical-is-enough 页面](https://jonaprieto.github.io/synthetic-graph-theory/lib.graph-embeddings.Map.Spherical-is-enough.html) 的 normalisation 模块显式接受 `M : Map G` 和 `M-is-spherical : isSphericalMap G M`；`spherical-equiv` 也是固定同一个 `M` 上两个球面规格的 equivalence。

## 3. P7 五项判定

| 项 | 固定页面中的事实 | 判词 |
|---|---|---|
| `K-input` | `Map G` 给出每个 star 的 cyclic structure；homotopy 与 spherical/normalisation 模块还显式接收 map、face、walk、节点判定及 spherical witness。 | `FAILS_BARE_H_INPUT` |
| `K-output` | 输出是 walk-homotopy、normal form、`isSphericalMap` 与固定 `M` 上两个 sphere specs 的 equivalence。 | `NOT_P13_DONE_AMBIENT_OR_CURVE` |
| `K-claim` | 论文讨论组合图嵌入与 walk/spherical 性质；固定页面没有声称 bare M/N 内在同胚完成 P13 的有限环境复原或曲线变形任务。 | `NO_P13_COMPLETION_CLAIM_FOUND_WITHIN_FIXED_PAGES` |
| `K-forgetting` | `U G` 出现在 underlying graph/walk 上，但 `Map` 仍是每个关键模块的显式参数；`Face G M` 与 `M-is-spherical` 也被传入。固定范围内没有 bare `H_intrinsic → Done` 的桥。 | `NO_BARE_H_TO_DONE_BRIDGE_FOUND_WITHIN_FIXED_PAGES` |
| `K-version` | 五页共同显示 2023-01-22、Agda `2.6.2.2-442c76b` 与 `57c278b4`；审计仅覆盖这个发布视图。 | `VERSION_PINNED_SOURCE_INSPECTED_WITH_SCOPE` |

## 4. 正控制、反解释与范围

**正控制。** `Map` 的 cyclic order、`Face G M`、显式 `M-is-spherical` 和由 `M` 参数化的 relation 是结构保持的可见证据；它们正是 P7 要求不能悄悄丢失的工作数据。

**最强反解释。** 论文把 surface 留为隐含，并把 graph embedding 说成 up to isotopy。这证明它是与 P13 相邻的抽象实践，却不证明它声称了 P13 的同一完成任务。表面坐标未在输入中出现，和将 bare `H_intrinsic` 当成 `Done_ambient^fin` 或 `Done_curve` 是不同的命题。

**本地侦察复用。** P14 已对相同 DOI 的本地 LIT 分母做完整定位，结论是旧项仅为 `DISCOVERY_UNREVIEWED / ADJACENT_TITLE_SIGNAL`。P15 不重跑该检索；它只把该冻结定位与本轮固定页面逐项读数相连。

## 5. 波次定位与裁决

1. **最终目标连接：** P15 检验了一个真正的 HoTT/Agda 形式化是否把用户的 operation-sensitive R 合同降为 bare equivalence；结果没有发现这条桥。
2. **全局坐标：** 这是 P3 `K_app` 的一个 version-pinned consumer audit，既不替代 P1 的 R 合同，也不触发 P4 implementation-fidelity 分支。
3. **实际价值：** 它给出比标题或论文摘要更强的输入/输出证据，并把“surface implicit”同“任务所需结构被遗忘”区分开。
4. **为何停止本分母：** 已冻结五页都显示同一结构保留模式；再作同义词搜索不会改变 P7 判定。它不停止 active goal。
5. **下一选择：** `P16-FOURTH-SUCCESSOR-DISCOVERY-001` 必须从未审的实际 HoTT/立方/相关消费者中选一个新的版本冻结分母，优先寻找含 equivalence/transport/embedding 但输入、输出可能更接近 bare H 与过程性 Done 的调用链；必须重新做公开与本地侦察，不能重审本语料。
6. **裁决：** `CLOSE_WITH_SCOPE / NOT_A_CONSUMER_WITHIN_FIXED_P15_PAGES / SWITCH_BRANCH_TO_P16_SUCCESSOR_DISCOVERY`。

## 6. 禁止外推

- 这不是“所有 HoTT 图论或所有 isotopy 形式化都会保留足够结构”的定理。
- 这不是作者发布 Agda 项目的 kernel replay；本轮没有编译、下载或克隆源码。
- 未找到 P13 的 K 不等于 HoTT 没有任何实际消费者问题，也不构成 HoTT 缺陷结论。
