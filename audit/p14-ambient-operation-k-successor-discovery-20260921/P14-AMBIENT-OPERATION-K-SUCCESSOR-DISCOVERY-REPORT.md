# P14-AMBIENT-OPERATION-K-SUCCESSOR-DISCOVERY-001：选择实际 HoTT/Agda 的嵌入—同伦语料

**状态：** `SUCCESSOR_SELECTED / PRIETO_CUBIDES_SPHERICAL_MAPS_AGDA_CANDIDATE / P15_NOT_STARTED / NO_NEW_HOTT_DEFECT_CLAIM`

**日期：** 2026-09-21

## 1. 判词改变凭据

P13 已把未来 K 的目标固定为 operation-sensitive 的完成合同：`Done_ambient^fin` 或 `Done_curve`。P14 的问题不再是“是否能再找到一个圆或同胚定义”，而是是否存在一个真实 HoTT/立方/相关使用位置，输入只保留 bare `H_intrinsic`，却把输出当作上述完成之一。

新的公开证据是 Prieto-Cubides 的 CPP 2022 论文及其作者发布的 Agda 形式化页面。该工作明确处理“图嵌入到曲面直至 isotopy”的组合任务，并以 Agda 形式化 HoTT 子语言的 proof-relevant 结构。它与 P8/P9 的 directed source、P11 的 Coq-HoTT Circle/Coeq 以及 P3 的 UniMath SIP consumer 都不同，因此有资格成为一个新的 source denominator。

## 2. 公开与本地侦察

### 公开来源

- [论文预印本](https://arxiv.org/abs/2112.06609) 表明工作以 combinatorial maps 表示图在曲面中的嵌入，并引入 walks 的同伦；它不是点集圆—开区间任务。
- [作者发布的 CPP 2022 Agda 形式化](https://jonaprieto.github.io/synthetic-graph-theory/CPP2022-paper.html) 明确导入 `Map`、`Face`、`HomotopyWalks`、`Spherical` 与 `Spherical-is-enough` 模块；页面声明 Agda `2.6.2.2-442c76b`，最新发布页标记为 2023-01-22、变更短标识 `57c278b4`。
- [Map 模块](https://jonaprieto.github.io/synthetic-graph-theory/lib.graph-embeddings.Map.html) 将 `Map G` 明确定义为每个节点 star 上的 cyclic set；[Spherical 模块](https://jonaprieto.github.io/synthetic-graph-theory/lib.graph-embeddings.Map.Spherical.html) 以 `Map G` 为显式输入定义 `isSphericalMap`；[walk-homotopy 模块](https://jonaprieto.github.io/synthetic-graph-theory/lib.graph-embeddings.Map.Face.Walk.Homotopy.html) 明确接收 map 和 face 来生成同伦关系。

这些是 `KNOWN_RELATED_ACTUAL_HOTT_FORMALISATION`，还不是 K 命中：页面已经显示候选输入含 `Map`/Face 等结构，且论文目标可能根本不同于 P13 的 M/N operation-sensitive Done。正是这些问题留给 P15。

### 本地与历史资产

`LIT-DENOMINATOR-001` 的固定候选表已经出现该 CPP 2022 论文，但状态仅为 `DISCOVERY_UNREVIEWED / ADJACENT_TITLE_SIGNAL`；仓库中没有对应源码审计、版本冻结或 P7 五项判定。这是 `HISTORICAL_UNVERIFIED`，不是已完成工作。P13 的 C-265–C-277 是 operation-aware 对照而不是 HoTT consumer；P8/P9/P11 已审簇继续排除。

## 3. P15 候选卡

| 字段 | 冻结内容 |
|---|---|
| Candidate | `P15-PRIETO-CUBIDES-SPHERICAL-MAPS-AGDA-CORPUS-001` |
| 源身份 | 作者发布的 Agda HTML formalisation，2023-01-22，`57c278b4`，Agda `2.6.2.2-442c76b`；论文 arXiv `2112.06609` / CPP 2022 DOI `10.1145/3497775.3503671` |
| 精确模块 | `CPP2022-paper`、`lib.graph-embeddings.Map`、`Map.Face.Walk.Homotopy`、`Map.Spherical`、`Map.Spherical-is-enough` |
| P13 对照 | `H_intrinsic`、`Done_ambient^fin`、`Done_curve`；候选必须说明它们与 `Map`/walk/spherical conclusion 是否同一任务 |
| P7 K admission | 逐项审计 `K-input`、`K-output`、`K-claim`、`K-forgetting`、`K-version` |
| 正控制 | 若 `Map`、cyclic order、face、walk-homotopy和其他证明对象显式进入输入，则判显式结构保留；不能因“surface implicit”就写成遗忘 |
| 最强反解释 | 论文的“embedding”是组合图论/球面问题，不是指定实平面中 M/N 的 operation-sensitive复原；任务不同本身不是 K |
| 停止 | P15 只审计上述固定发布页面/论文范围；不编译未知源码、不把页面转述当 kernel replay、不扫描整个 HoTT 社区 |

## 4. 波次定位与裁决

1. **最终目标连接：** P14 将 P13 的 operation-sensitive R 合同第一次接到一个公开、实际 HoTT/Agda 形式化的消费者候选。
2. **全局坐标：** P14 是 P3 `K_app` 的 successor discovery；P15 才会判断该消费者是否保结构、任务不同或可能越级。
3. **实际价值：** 它把一个此前只是文献题录的 `DISCOVERY_UNREVIEWED` 项提升为版本、模块、输入/输出和反解释都可检查的候选卡，避免重复 P8/P9/P11。
4. **不继续 P14 的理由：** source identity、候选模块和 P7 admission 已冻结；继续关键词搜索不能替代对这个实际语料的 P15 审计。
5. **裁决：** `SWITCH_BRANCH / SUCCESSOR_SELECTED`。P15 尚未开始；P14 没有发现 K、没有新数学定理、没有实现差异，也没有 HoTT 缺陷结论。

## 5. 禁止外推

- “嵌入到曲面直至 isotopy”这一论文主题不等于用户的圆去点/开区间复原任务。
- 作者发布的 HTML formalisation 与 Agda 版本信息证明可审计 source 身份，不证明本项目已经重放或 kernel-check 其全部源码。
- `Map`/face 明显存在并不自动证明 P15 的所有 K 条件失败；P15 必须逐模块核实。
