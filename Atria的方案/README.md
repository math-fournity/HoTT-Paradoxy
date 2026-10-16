# Atria 的方案（入口说明）

> 本文件只是目录入口，**不是**分片索引。完整的逻辑文档是同目录下的
> [`修订片.md`](修订片.md)（governance-shard-index:v2）。

## 这里有什么

- [`修订片.md`](修订片.md)：逻辑文档索引（v2 分片合同），含 5 个修订片的完整表。
- [`修订片/`](修订片)：5 个修订片正文，每片引用 GPT 方案 v2.1 的原片，只写需变更或新增的条款。

## 修订片一览

| 片 | 修订对象 | 对应发现 |
|---|---|---|
| 001 — FR-001 路径不可对称与契约身份修复 | GPT 003 片 §1/§4/§6 + 新增 §12 | A1, A4 |
| 002 — EC-001 证据契约修复工作包（新增） | GPT 003 片 §9 前置新增 | A2, A4 |
| 003 — GEN-001 有界生成器验收单元（新增） | GPT 002 片工作包表 + 007 片 §3 | A3 |
| 004 — L2 并行交付态与验收门裁定前置 | GPT 010 片 §9/§11 + 008 片 §11 | A6 |
| 005 — 里程碑重排、EXP 提前与截止日处置 | GPT 009 片 + 008 片 §10 | A7, A8 |
| 006 — 发现引擎：语义重定向作为八轴搜索策略 | GPT 007 片 §2/§3 增补 | 报告集 08 |

发现的依据见 [`../Atria的审计报告集/`](../Atria的审计报告集/)（8 份报告 + `evidence/commands/`
下的独立复算收据）。

## 身份

`USER_REQUESTED_OPTIONAL_REVISION / INCREMENTAL_PATCHES_OVER_GPT_V21 /
NOT_PROJECT_CURRENT_QUEUE_UNTIL_CANONICAL_WRITEBACK / NO_NEW_MATH_CLAIM /
LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`

采纳条件（沿用 GPT 010 片 §11）：是否写入 project current queue、是否授权 Git commit、
是否改变根 Goal 门、是否降低 natural/source-grounded consumer 资格、是否设立 L2 并行交付态
——均仅用户可裁定。
