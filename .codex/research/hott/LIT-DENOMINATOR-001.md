<!-- governance-shard-index:v2
logical_id: LIT-DENOMINATOR-001
mode: topical
shard_root: LIT-DENOMINATOR-001
last_shard: LIT-DENOMINATOR-001/005 - 冻结判词、未完成审查与下一批全文.md
append_target: -
soft_line_target: 300
-->

> ⚠️ 逻辑文档索引：全文 = 本索引 + 下方 5 个分片；缺一片即未完成。索引冻结分母身份，分片分别拥有范围、查询、核心 seed、候选分层和后续全文义务。

# LIT-DENOMINATOR-001：HoTT 可计算性与不完备性学术覆盖分母

> 版本：`lit-denominator/v1.0`  
> 截止日：`2026-09-14`  
> 当前判词：`DENOMINATOR_V1_FROZEN / DISCOVERY_18x2_COMPLETE / PRIMARY_CORPUS_REVIEW_IN_PROGRESS / COMPREHENSIVE_COVERAGE_NOT_ACHIEVED`  
> 当前 Goal：`.codex/research/hott/HOTT-MACHINE-OVERVIEW-ACTIVE-GOAL.md`  
> 程序化父级：`.codex/research/hott/HOTT-PARADOX-PROGRAMMATIC-EXPLORATION-COMPLETENESS.md`

本逻辑文档冻结“从 Gödel/Turing/Church 到 2026-09-14 当前研究全面覆盖”的可审计分母。它不把 bibliographic metadata 当作论文内容，不把标题命中当作纳入裁决，也不把本分母完成写成全文研究已经完成。

<!-- governance-shard-table:start -->
| Shard | 文件 | 语义范围 | 状态 |
|---|---|---|---|
| 001 | [范围、渠道与证据语义](<LIT-DENOMINATOR-001/001 - 范围、渠道与证据语义.md>) | 截止日、主题族、来源/场馆、纳入排除、证据等级 | current |
| 002 | [查询分母与机器发现收据](<LIT-DENOMINATOR-001/002 - 查询分母与机器发现收据.md>) | 18 个查询、两个 provider、36 次请求、raw/hash/重放 | current |
| 003 | [预注册核心 Seed 与谱系覆盖槽](<LIT-DENOMINATOR-001/003 - 预注册核心 Seed 与谱系覆盖槽.md>) | 33 个不可因搜索漏检而消失的核心论文/项目 seed | current |
| 004 | [候选分层、反遗漏与 UNCLASSIFIED](<LIT-DENOMINATOR-001/004 - 候选分层、反遗漏与 UNCLASSIFIED.md>) | 1941 候选、32/164/1745 分层、漏检诊断与新增高价值项 | current |
| 005 | [冻结判词、未完成审查与下一批全文](<LIT-DENOMINATOR-001/005 - 冻结判词、未完成审查与下一批全文.md>) | v1 完成范围、仍开放的全文/citation/venue/primary 工作与下一批 | current |
<!-- governance-shard-table:end -->

## 证据入口

- discovery manager：`scripts/audit/build_lit_denominator_discovery.py`
- title triage manager：`scripts/audit/triage_lit_denominator_candidates.py`
- raw/manifest/candidates/triage：`audit/literature/LIT-DENOMINATOR-001/discovery-20260914/`；stable record 默认只水合 `MANIFEST.json` 与 `TRIAGE-RECEIPT.json`，两个大型派生 JSON 按 receipt/hash 查询，不常驻正文
- 旧 41 条地图快照：`audit/imports/machine-overview-computability-20260914/HOTT-NONTERMINATION-MACHINE-OVERVIEW-PLAN.md`
- 用户指定方案：`外部资料/在 HoTT 中寻找“不可停机—不完备性边界”的研究方案：从计算性限制到 Gödel 型自指的可执行路线.md`
