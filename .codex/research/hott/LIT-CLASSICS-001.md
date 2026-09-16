<!-- governance-shard-index:v2
logical_id: LIT-CLASSICS-001
mode: topical
shard_root: LIT-CLASSICS-001
last_shard: LIT-CLASSICS-001/006 - 当前判词、缺口与下一机器工作包.md
append_target: -
soft_line_target: 300
-->

> ⚠️ 逻辑文档索引：全文 = 本索引 + 下方 6 个分片；缺一片即未完成，按表顺序读取；300 行只是软目标，不是上限。

# LIT-CLASSICS-001：从经典可计算性到 HoTT 不完备性前提

状态：`PRIMARY_RELEVANT_SECTIONS_REVIEWED_WITH_SCOPE / MINERU_16_UNIQUE_GROUPS_IMPORTED / KLEENE_SCAN_AND_TEXT_REVIEWED / ROSSER_PRIMARY_BODY_VISUALLY_AND_TEXT_REVIEWED / POST_PRIMARY_BODY_EXTRACTED_VISUALLY_AND_TEXT_REVIEWED / LIT_CLASSICS_IN_PROGRESS`

截止日：2026-09-14。

本逻辑文档承担 `LIT-DENOMINATOR-001` 之后的第一批 primary-corpus review。它不把论文报道的定理冒充本 repo 已机器重放的结论；所有外部数学结果均保持 `SOURCE_REPORTED_NOT_REPLAYED`，本 repo 的机器结论仍只由 `HoTT/CLAIM_EVIDENCE_MATRIX.md` 与对应 run 支持。

<!-- governance-shard-table:start -->
| Shard | 文件 | 语义范围 | 状态 |
|---|---|---|---|
| 001 | [范围、来源身份与转换证据](<LIT-CLASSICS-001/001 - 范围、来源身份与转换证据.md>) | primary 来源、PDF/MinerU 身份、读取状态与 OCR 边界 | current |
| 002 | [Turing与Church：可计算、通用机与不可判定](<LIT-CLASSICS-001/002 - Turing与Church：可计算、通用机与不可判定.md>) | 标准描述、通用机、circle-free、λ/recursive、normal form 与 Entscheidung | current |
| 003 | [Gödel、Rosser与Löb：算术化、独立句与自担保](<LIT-CLASSICS-001/003 - Gödel、Rosser与Löb：算术化、独立句与自担保.md>) | 第一／第二不完备性前提、Rosser 强化与 Löb 条件 | current |
| 004 | [Kleene、Post、Rice与Lawvere：定点、半判定与语义边界](<LIT-CLASSICS-001/004 - Kleene、Post、Rice与Lawvere：定点、半判定与语义边界.md>) | s-m-n/递归定理、r.e.、Rice 与范畴对角 | current |
| 005 | [现代机器化对照与R2-R4前提](<LIT-CLASSICS-001/005 - 现代机器化对照与R2-R4前提.md>) | O’Connor、Kirst 系列、2LTT、cubical assemblies | current |
| 006 | [当前判词、缺口与下一机器工作包](<LIT-CLASSICS-001/006 - 当前判词、缺口与下一机器工作包.md>) | 综合、候选、R2/R4 接口与未完成分母 | current |
<!-- governance-shard-table:end -->

本轮的核心结论不是“经典文献已经证明 HoTT 有悖论”，而是已经把此前含混的计算／自指路线拆成可检查的前提链，并定位到两个 HoTT 特有的分层问题：`EPF/Church thesis` 的 universe/modality 适用域，以及 self-syntax／metatheory 的 inner/outer 边界。2026-09-14 已取得并逐页核对 Rosser 1936 原文，又从 BAMS 1944 年 5 月整期扫描抽取 Post 印刷页 284–316，核定其来源边界并全文首读；Rosser 与 Post primary-body 缺口均已关闭，其余经典 coverage、引用链和机器重放仍开放。
