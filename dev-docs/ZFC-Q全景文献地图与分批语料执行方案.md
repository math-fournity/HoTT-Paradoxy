# ZQCM-002：ZFC Q 全景文献地图与分批语料执行方案

> **身份：** `ACCEPTED_EXECUTION_PLAN / RESEARCH_PROFILE_GOVERNED / ZFC-Q-CORPUS-MAP-SOP_CONSUMER / CANDIDATE_NOT_CURRENT`。
>
> **计划名：** `ZQCM-002 — ZFC Q 全景文献地图与分批语料工程`。
>
> **唯一调用 SOP：** `ZFC-Q-CORPUS-MAP-SOP`。
>
> **父结果：** 把 ZQCM-001 的冻结来源控制扩展成跨理论位置、时期、来源平台、作者群、引文网络、实际消费者与反控制的可追溯地图，服务定位 ZFC Q；不以地图规模本身宣称 Q、矛盾或世界范围绝对穷尽。

## 1. 操作性目标

“翻查所有 ZFC 文献”在开放世界中没有可验证的绝对终点。本计划把它转译为一个可完成、可扩展的地图工程：

1. 固定一个明示的理论位置×来源类型×时期×语言×数据库的地图分母；
2. 对每条高优先级路线形成可重算 query、work-family 去重、纳入／排除／访问余项与引文边；
3. 将每个取得的原件按既有 acquisition→PDF验证→remote-MinerU或视觉→source screen→Q lead 流程处理；
4. 对地图外的强反例、作者原典和真实消费者执行 out-of-envelope 审计；
5. 只把满足 `R/Z/Q/E`、same-task、source payment 与模式 P 条件的来源交给专门候选工程。

阶段完成只表示地图分母已经闭合。它不会宣布“所有 ZFC 文献已经读完”“ZFC 没有问题”或“ZFC Q 已定位”。

## 2. 地图分母

| Axis | 需要覆盖的家族 | 典型入口 | 对 Q 的作用 |
|---|---|---|---|
| A：基础形成 | Zermelo/Fraenkel/von Neumann、Separation、Replacement、Power Set、Foundation、Infinity、Choice、cumulative hierarchy | 原始论文、标准教材、历史／哲学研究、正式公理库 | 固定理论内对象、formation与已知防线。 |
| B：总体与阶段 | potential/actual hierarchy、impredicativity、Vicious Circle、reflection、truth/schema、classes与universes | Feferman、Linnebo、Koepke–Koerwien、集合论哲学和证明论来源 | 检查“完成总体／阶段可用性”是否能形成同一任务。 |
| C：语义与独立性 | forcing、models、independence、inner models、large cardinals、determinacy、cardinal arithmetic | Cohen、Gödel、Jech、Kunen、Woodin、Shelah及正式项目 | 区分模型支付、相对一致性和裸 ZFC 消费者。 |
| D：真实消费者 | ordinary set-theoretic practice、proof checking、formal libraries、computable/formal constructions、category/ETCS consumers | Isabelle/ZF、Metamath、Lean/Mathlib、数学实践访谈、具体论文本体 | 寻找 `u/F/C/operation/observation/Done`，避免把模型层当消费者。 |
| E：外部对照 | HoTT/UF、MLTT、CZF/IZF、realizability、category-theoretic foundations、structuralism | HoTT作者原典、Aczel、Shulman、Maddy、Voevodsky等 | 形成 `R_i→Z_i→Q_i` 或反类比／payment control。 |

每个 family 还按时期、语言、论文类型（原典／教材／综述／形式化项目／实际consumer）、平台（arXiv、作者、机构、出版社、zbMATH、OpenAlex、Crossref、MathSciNet／PhilPapers若可访问）与获取状态切分。不能让某一个平台的结果数代替整个分母。

## 3. 执行波次

| Wave | 交付 | 最小判别行动 | 停止／重开 |
|---|---|---|---|
| M0：地图骨架 | family taxonomy、query dictionary、数据库／作者／引文入口、去重键、语言/时期边界 | 为 A–E 各建立一张可执行的查询卡和覆盖行 | A–E 每轴均有入口、query 与余项；新理论位置才可扩轴。 |
| M1：基础形成原典 | A 轴的原典、标准防线和 Power Set/Replacement/Separation 近邻来源 | 每一公理簇至少有来源链与反控制 | 只在取得新原典或发现未覆规则时扩展。 |
| M2：总体与阶段 | B 轴的 potential/actual、impredicativity、truth/schema、reflection 文献 | 将“阶段性”固定到某种 ZFC formation/consumer，而非哲学词汇 | 未保留 same-task 则记 control/seed 并停止同义扩张。 |
| M3：语义与独立性 | C 轴的 forcing/model/independence/large-cardinal 文献 | 分离 meta-model 支付与 ordinary bare-ZFC consumer | 每条路线都有 model/payment disposition 或新的 consumer ingress。 |
| M4：实际消费者 | D 轴的数学实践与形式化消费者 | 形成版本固定 `u/F/C/I/O/Done` source card | 无同层 consumer 仅作为控制；出现它才进入 Q 资格化。 |
| M5：外部反投影 | E 轴和 HOTT-MOTIVE 文献地图 | 精确 `R_i→Z_i→Q_i` 卡或 anti-analogy | 动机不等于缺陷；无保真传输则保持控制。 |
| M6：引文与越界审计 | 双向引文、作者群、out-of-envelope 文献和强反例 | 每条强引用有 disposition；未搜领域显式为 remainder | 覆盖表的 `NOT_SEARCHED` 必有合理访问／语言／优先级说明。 |

每一波只建立一个或多个冻结 batch。批次可并行作为地图条目被登记，但 acquisition、写入和 current owner 仍由唯一 Master 顺序裁决。

## 4. 单篇处理合同

每份接受的 PDF 沿既有 `ZFC-Q-CORPUS-MAP-SOP` 处理：

```text
work identity → acquisition/version/hash → remote MinerU (or explicit failure)
→ 150dpi page-by-page visual record → 300dpi critical-page review
→ Source Notes → screening / citation / coverage / Q lead disposition
```

若远程 MinerU 结果不可得，原 PDF 的页级视觉阅读继续是可用主阅读层；它不得被描述为 MinerU 转码成功。当前官方 CDN 的 TLS 证书问题属于派生层外部阻塞，不降低已存原件视觉证据。

## 5. Q 资格与负控制

一篇文献仅因提到“Power Set”“无穷”“基础危机”“存在”“模型”或“Russell”不能成为 Q。准入至少要求：

1. 固定 ZFC 变体与理论内一等对象；
2. 固定 formation 和来源定义的 consumer；
3. 固定相同 subject、operation、observation 和 Done；
4. 明示标准回答、模型/证明/支付层和反控制；
5. 只有存在 formation-use reentry、未支付 completion 或模式 P 的其他合格结构时，才进入专门 Q 工作。

`P-FORGE-SOP`、P-DAG、worker、Power Set station切换和数学 STATE 不由这个计划自动启动。

## 6. 地图完成判据

`ZQCM-002` 可标为 `MAP_COMPLETE_WITH_SCOPE` 仅当：

1. A–E 每轴和 M0–M6 每波均有可审计覆盖行、查询记录或明确不适用判词；
2. 已选入的 work family 都有 acquisition／版本／不可得 disposition；
3. 所有高优先级 backward/forward/author/bridge 引文都被筛选、延期或排除并写明原因；
4. 覆盖表列出语言、访问、版本、平台和未搜索余项；
5. 每个 Q lead 都有接受、拒绝、control 或等待新来源的状态；
6. 执行一次独立的 out-of-envelope／强反例检索；
7. Findings 区分地图完成、来源筛读完成、候选资格与数学结论。

这一状态仍只是“给定地图分母已闭合”。新增 DOI、作者原典、可得全文、实际消费者、理论位置或可复核反例会按新 batch 重开。

## 7. 目标调用词

后续 `/goal` 使用：

```text
按照SOP=`ZFC-Q-CORPUS-MAP-SOP`，执行计划=`ZQCM-002 — ZFC Q 全景文献地图与分批语料工程`，从 M0 开始，逐波冻结、处理、审计并写回，直至所有 M0–M6 波次达到 MAP_COMPLETE_WITH_SCOPE 或留下明确可重开的外部余项；不以论文数量、关键词命中或单一数据库结果替代覆盖判据。
```

## 8. 当前第一行动

M0 的第一个可验动作是建立 A–E family 的查询字典与来源平台矩阵，先登记现有 ZQCM-001/HOTT-MOTIVE work family，确定它们覆盖哪些 cell，再以 remainder 驱动新 batch。它必须先证明地图有什么尚未覆盖，不能先按模型熟悉的关键词随机下载论文。
