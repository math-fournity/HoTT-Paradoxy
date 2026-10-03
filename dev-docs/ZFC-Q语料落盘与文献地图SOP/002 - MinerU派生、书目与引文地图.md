<!-- governance-shard:v2
logical_id: ZFC_Q_CORPUS_MAP_SOP
shard_id: 002
index: ../ZFC-Q语料落盘与文献地图SOP.md
-->

# MinerU派生、书目与引文地图

## 1. MinerU 是派生层

已接受原 PDF 才可以进入 MinerU。对当前这种正常公开学术PDF，研究发起人已授权 ZCode 同源的 direct remote standard 解析作为唯一 MinerU 质量通道；本地 `basic` 结果不得再作为本项目的阅读、引用或判断依据。direct remote 不改变本地 App daemon 或配置。每次派生保存：

| 字段 | 要求 |
|---|---|
| MIN ID / ACQ ID | 对应一个已验证原件。 |
| runtime | MinerU executable、版本、完整命令、`direct remote standard` 服务身份和执行收据。 |
| input identity | 原PDF路径与 SHA-256。 |
| scope | 全文、页范围或指定 block；不能把局部 parse 写成全文处理。 |
| output | 原始 zip、展开的 Markdown／JSON 路径、各输出哈希和失败信息。 |
| visual review | `VISUAL-REVIEW.md` 条目、150dpi二值页图路径、页级结果与必要的300dpi仲裁图。 |
| locator | Q相关引文的页和 block，必须回原PDF视觉核对。 |

MinerU Markdown、OCR和索引是阅读帮助，不替代原PDF。公式、表格、图形、页码、关键限定词和Q相关主张必须能回到原页；解析失败、质量层不可用或服务状态异常必须保存。远程解析失败时可继续以原PDF做视觉阅读，但不得静默降级到本地 `basic`。显然敏感的文件不继承本轮公开论文的远程授权。

## 2. 视觉核验：二值页图与高精度仲裁

本项目借用菲尔兹论文库 `AUDIT-SOP.md` 的证据链，但不把“修复每一份 Markdown”误写成当前语料工程的目标。这里的目标是固定远程派生物相对于原PDF的可用范围，使 Q 线索能够追到视觉证据。

1. **先完整远程解析。** 保留未经编辑的 remote zip 及其展开文件；不能用人工改写替代服务的原始输出。
2. **再逐页生成和查看二值页图。** 每页以 Ghostscript `pngmono`／150dpi 渲染，页号与PDF页号一一对应；视觉核验按“渲染→目检→对照对应 MinerU 页段／结构JSON→立即落签”交错进行，不先批量生成结论。被引用或用于页级结果的图放在 batch 的 `visual/<work-id>/150dpi/`，不能只存在于临时目录。
3. **每页至少核对可读性和内容锚点。** 题录页核标题、作者与脚注；正文页核节标题、定义／定理编号、公式和显著符号；文末核参考文献与出版信息。结果只可写 `VISUAL_PASS`、`VISUAL_PASS±`、`SOURCE_PRIORITY` 或 `UNREVIEWED`。`SOURCE_PRIORITY` 表示该段直接从原PDF阅读，不能把 MinerU 文本当作该段的引文依据。
4. **关键位置作高精度核验。** 所有可能进入 Q LeadCard 的定义、命题、公式、量词、完成条件、脚注、图表和引用页，以及150dpi发现差异的页，必须以300dpi页图或裁剪图再检视；图存入 `visual/<work-id>/300dpi/`，并在 `VISUAL-REVIEW.md` 标明PDF页、MinerU定位、差异及处置。
5. **视觉证据不是数学结论。** 它只说明某个派生段可否被用作导航和定位；解释、同一任务、source payment和Q资格仍需回原PDF及后续专门SOP处理。

### 2.1 压缩安全的逐页写回与恢复

视觉阅读会把页面的版面、公式、脚注和限定词暂时放入当前上下文；这不是可恢复证据。`VISUAL-REVIEW.md` 是每个 batch 唯一的持久视觉游标，**一张实际读过的页只有在其行已写入后才取得“已审阅”身份**。

1. 一个 `ReviewUnit` 至少是一张 PDF 页：`Work ID`、PDF页、150dpi图路径、当前阅读层（remote comparative或source-only）、实际核对锚点、结果、300dpi处置和下一步都写入同一页级行。对于关键页，读取300dpi图后立即补写同一行，不把高精度观察留在聊天或临时记忆中。
2. 看完某页后、打开下一页之前，必须以结构化写入把该页追加到 `VISUAL-REVIEW.md`。可以预先生成多张图，但未有页级行的图只处于`RENDERED_UNAUDITED`，不能支持来源解释、筛选、citation、Q lead或“已完成视觉阅读”的句子。
3. 发生上下文压缩、新Session、交接、工具中断或不确定是否已落签时，先读取本 batch 的`VISUAL-REVIEW.md`当前游标和相关`MINERU-DERIVATIVES.md`。没有持久行的先前视觉印象一律作废；从最早的`RENDERED_UNAUDITED`／缺行页回到原PDF页图重审，不能从摘要、assistant文本或私有记忆补写结论。
4. 一个 work 的`SOURCE_ONLY_VISUAL_CHECK_COMPLETE`或`VISUAL_PASS`只可在全部150dpi页均有行、每个关键／异常页均已记录300dpi处置、并且没有`RENDERED_UNAUDITED`余项时写入。远程导出是否存在仍是另一条证据状态，不能因逐页写回而被提高。

这是一项恢复和证据完整性合同，不是对模型记忆、上下文窗口或未来行为的全称保证。它防止的是已发生且可直接避免的错误：把“曾经看过图”误报为“有可追溯的视觉审计”。

## 3. 书目地图

每批维护：

```text
WORK-FAMILIES.md       work identity、报告版本和去重关系
SEARCH-LOG.md          完整 query、日期、平台、命中、分页、访问限制
SCREENING.md           纳入、排除、暂缓与原因
CITATION-NETWORK.md    backward、forward、author和bridge追踪
COVERAGE-MAP.md        理论位置 × 文献轴 × 来源平台 × 时期 × 语言的余项
```

书目数据库命中只是候选记录。arXiv、zbMATH、Crossref、OpenAlex、MathSciNet（若可访问）、PhilPapers、作者／机构页和正式项目 archive 各有不同覆盖；不可将一个平台的结果数当作语料总数。

## 4. 引文与覆盖

每一个 seed work family 必须分别记录：

1. backward citation：参考文献中与理论位置、P字段、consumer或标准防线相关的工作；
2. forward citation：被引工作和后续批评／应用；
3. author／project trace：作者的论文列表、项目档案、正式源码和会议链；
4. bridge trace：从某个理论概念到实际consumer／control所需的缺边。

覆盖地图必须保存 `NOT_SEARCHED`、`SEARCHED_PENDING_SCREEN`、`INCLUDED`、`EXCLUDED_WITH_REASON`、`UNAVAILABLE` 和 `LANGUAGE_LIMIT`，并记录剩余强引用。没有完整 query log 与余项，就不能使用“完全追溯”或“饱和”。

## 5. 质量检查不是论文答辩

本项目采用论文级的可复跑检查，是为了防止随意检索、遗漏强引用或把同一论文的多个版本重复计算。它不要求临床系统综述、不要求完成学位论文、不要求统计效应汇总或假装有人类同行评审。

没有独立信息检索审阅时标 `SEARCH_PEER_REVIEW_NOT_AVAILABLE`；AI第二次阅读、另一个模型输出或下载数量都不替代独立复核。
