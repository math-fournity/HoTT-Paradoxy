<!-- governance-shard:v2
logical_id: ZFC_Q_CORPUS_MAP_SOP
shard_id: 002
index: ../ZFC-Q语料落盘与文献地图SOP.md
-->

# MinerU派生、书目与引文地图

## 1. MinerU 是派生层

已接受原 PDF 才可以进入 MinerU。每次派生保存：

| 字段 | 要求 |
|---|---|
| MIN ID / ACQ ID | 对应一个已验证原件。 |
| runtime | 本地 MinerU executable、版本和命令。 |
| input identity | 原PDF路径与 SHA-256。 |
| scope | 全文、页范围或指定 block；不能把局部 parse 写成全文处理。 |
| output | Markdown／JSON／zip 路径、输出哈希和失败信息。 |
| locator | Q相关引文的页和 block，必要时回原PDF视觉核对。 |

MinerU Markdown、OCR和索引是阅读帮助，不替代原PDF。公式、表格、图形、页码、关键限定词和Q相关主张必须能回到原页；解析失败、质量层不可用或服务状态异常必须保存，而不是静默降级。

## 2. 书目地图

每批维护：

```text
WORK-FAMILIES.md       work identity、报告版本和去重关系
SEARCH-LOG.md          完整 query、日期、平台、命中、分页、访问限制
SCREENING.md           纳入、排除、暂缓与原因
CITATION-NETWORK.md    backward、forward、author和bridge追踪
COVERAGE-MAP.md        理论位置 × 文献轴 × 来源平台 × 时期 × 语言的余项
```

书目数据库命中只是候选记录。arXiv、zbMATH、Crossref、OpenAlex、MathSciNet（若可访问）、PhilPapers、作者／机构页和正式项目 archive 各有不同覆盖；不可将一个平台的结果数当作语料总数。

## 3. 引文与覆盖

每一个 seed work family 必须分别记录：

1. backward citation：参考文献中与理论位置、P字段、consumer或标准防线相关的工作；
2. forward citation：被引工作和后续批评／应用；
3. author／project trace：作者的论文列表、项目档案、正式源码和会议链；
4. bridge trace：从某个理论概念到实际consumer／control所需的缺边。

覆盖地图必须保存 `NOT_SEARCHED`、`SEARCHED_PENDING_SCREEN`、`INCLUDED`、`EXCLUDED_WITH_REASON`、`UNAVAILABLE` 和 `LANGUAGE_LIMIT`，并记录剩余强引用。没有完整 query log 与余项，就不能使用“完全追溯”或“饱和”。

## 4. 质量检查不是论文答辩

本项目采用论文级的可复跑检查，是为了防止随意检索、遗漏强引用或把同一论文的多个版本重复计算。它不要求临床系统综述、不要求完成学位论文、不要求统计效应汇总或假装有人类同行评审。

没有独立信息检索审阅时标 `SEARCH_PEER_REVIEW_NOT_AVAILABLE`；AI第二次阅读、另一个模型输出或下载数量都不替代独立复核。
