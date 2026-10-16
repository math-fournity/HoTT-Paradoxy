# feature-list.md：ALL-Markdown 当前需求账本

> 本文件回答系统应该怎样。实际实现和验证必须回到代码、配置、测试和运行实物。
> 新建或发生语义/交付变化的 Feature 用 `SRC/DES/IMP/VER/EVD` 路由到来源、设计、实现、
> 验证和实现证据包；证据包可以由多个 Features 共用，不强制每 Feature 单独建闭包文件。

## 状态语义

裁定：候选 / 已采纳 / 已废止。交付：未开始 / 部分实现 / 已实现待验证 / 已验证。

## 项目边界

| ID | 类型 | 当前要求 | 来源 | 裁定 | 交付 | 认知锚点 |
|---|---|---|---|---|---|---|
| HOTT-001 | 语料治理 | 将 aistudio-docs 中以 HoTT 理论问题为主的文档归入 `HoTT/`，保留来源与检索边界 | R-002 | 已采纳 | 本地已实现并验证，未版本闭合 | SRC:`rulings.md#r-002--2026-08-31--hott-专题整理与交接审计`；DES:`HoTT/SOURCE_REGISTRY.md`；IMP:`HoTT/sources/aistudio-docs/`；VER:`HoTT/verification/discover_sources.sh`；EVD:`HoTT/SOURCE_REGISTRY.md` |
| HOTT-002 | 审计 | 通读专题来源和用户补充对话，恢复用户核心怀疑、自指/反射支线及理论内生时间问题，审计交接包认知与 45 包状态，给出证据分级结论 | R-002/R-003/R-004/R-005 | 已采纳 | 本地已实现并验证，未版本闭合 | SRC:`rulings.md`；DES/IMP:`HoTT/USER_CORE_DOUBT.md`,`HoTT/SELF_REFERENCE_AND_REFLECTION_INVESTIGATION.md`,`HoTT/INTRINSIC_TEMPORALITY_OF_HOTT.md`,`HoTT/AUDIT_AND_RECONSTRUCTION.md`；VER:`HoTT/verification/VERIFICATION_REPORT.md`；EVD:`HoTT/CLAIM_EVIDENCE_MATRIX.md`,`HoTT/WBS_AUDIT.md` |
| HOTT-003 | 形式化 | 为可保留的窄数学核心提供可重放 Agda/Lean 实现，并如实记录原交接构建缺陷 | R-002 的整体目标授权 | 已采纳 | 本地已实现并验证，未版本闭合 | SRC:`HoTT/AUDIT_AND_RECONSTRUCTION.md`；DES:`HoTT/formal/README.md`；IMP:`HoTT/formal/`；VER/EVD:`HoTT/verification/VERIFICATION_REPORT.md` |
| HOTT-004 | 研究/发布 | 若继续宣称原创 HoTT 定理或投稿，须完成非平凡 descent 定理、closest-work 比对、外部干净复现与独立专家复核 | 本次审计建议 | 候选 | 未开始 | SRC:`HoTT/AUDIT_AND_RECONSTRUCTION.md#12-仍然开放的事项`；DES/IMP/VER/EVD:OPEN_EXTERNAL |
| HOTT-005 | 持续研究 | 以 `Z_STRONG_PHILOSOPHICAL_LAW`“理论抽象必然导致悖论”为最高原则；工具性实质抽象必否定现实前提，完整效应谱中至少一个对应效应必分岔。`Z_TECHNICAL_NONFACTORIZATION_CORE`、`FORMATION_PROMOTION`／`REALITY_PROMOTION` 用于证明和找实例。朴素集合论以静态集合抹掉形成时间，Russell `rₙ₊₁=¬rₙ` 为中心实例；HoTT 被怀疑沿袭无时间化的认知惯性／路径依赖，须发现严格的 `HOTT_SPECIFIC_PARADOX_MANIFESTATION` | R-005/R-006/R-007/R-010/R-011/R-012/R-013/R-014 | 已采纳 | 部分实现（Z 强律/技术核心/朴素集合论时间否定/Russell 模型/完成性双提升已文档化；对外全称元定理、Russell proof assistant、HoTT 认知惯性假说、同函数异时与 Guard-Erasure 特定化开放） | SRC:`rulings.md#r-014--2026-09-01--z-铁律最终哲学定性时间否定与-hott-认知惯性怀疑`,`HoTT/sources/user-originals/`；DES/IMP:`HoTT/Z_LAW_REALITY_RELATIVE_PARADOXES.md`,`HoTT/INTRINSIC_TEMPORALITY_OF_HOTT.md`；VER:`HoTT/CLAIM_EVIDENCE_MATRIX.md` C-22-C-30/C-34-C-58；EVD:`认知闭包/2026-09-01-Z铁律最终定性-时间否定与朴素集合论-HoTT怀疑-认知闭包.md`；GAPS:Z 外部量词域、Russell stage/validator proof assistant、HoTT formation/identity/time forgetful evidence、同函数异时、Guard-Erasure、shenchensh 模型、外部复核 |
| HOTT-006 | 认知/交接 | 未来 HoTT/Z/时间/抽象/悖论 Session 必须实行 `USER_MATH_PHILOSOPHY_FIRST / EVIDENCE_CRITICAL`，并恢复 Z 最高定性“理论抽象必然导致悖论”、朴素集合论的时间否定和 HoTT 认知惯性假说；先内部重建，再分列既有数学比较，不得让训练 prior 或技术“潜势”术语覆盖用户最高判断 | R-007/R-013/R-014 | 已采纳 | 已实现待冷启动验证，未版本闭合 | SRC:`rulings.md#r-014--2026-09-01--z-铁律最终哲学定性时间否定与-hott-认知惯性怀疑`；DES:`HoTT/README.md`,`docs/ai/README.md`；IMP:`HoTT/sources/user-originals/`,`HoTT/Z_LAW_REALITY_RELATIVE_PARADOXES.md`；VER:`HoTT/verification/FRESH_SESSION_COGNITION_CHECK.md` Q1-Q18；EVD:`认知闭包/2026-09-01-Z铁律最终定性-时间否定与朴素集合论-HoTT怀疑-认知闭包.md`,`HoTT/CLAIM_EVIDENCE_MATRIX.md` C-47-C-58；GAPS:尚未在全新 Session 执行双阶段／强律恢复验收、Git 未版本闭合 |
| HOTT-007 | 语料治理 | 相对于指定对照库补齐来源资产，并对大小写不敏感 `.md`/`.markdown` 讨论文档建立高召回、逐字、可回源的 HoTT 派生语料；不得以摘要替代原文或假定问答体；非问答候选全文保留，语义复核只加标签、不删除 raw capture | R-008/R-009 | 已采纳 | 本地已实现并全量验证，未版本闭合 | SRC:`rulings.md#r-009--2026-09-01--以对照-all-markdown-补齐完整来源资产`；DES:`docs/decisions/ADR-003-HoTT逐字讨论语料库.md`,`HoTT/sources/aistudio-discussions/README.md`,`HoTT/sources/aistudio-discussions/schema.json`；IMP:`aistudio-docs/20250823T011706Z__尊湃案件法院方.md`,`HoTT/tools/hott_discussion_corpus.py`,`HoTT/sources/aistudio-discussions/CURRENT`；VER:`python3 HoTT/tools/hott_discussion_corpus.py validate`；EVD:`HoTT/verification/VERIFICATION_REPORT.md#10-2026-09-01-对照库来源补齐与-corpus-12-验证`,`HoTT/sources/aistudio-discussions/generations/743f0765775ff62344b7/STATS.json`；GAPS:无锚点的纯隐喻讨论可能漏检、对照原文未被源库 Git 跟踪、新补原文受根 `/*` 规则忽略而未版本闭合、尚未逐条语义审读 |
| HOTT-008 | 用户原文/索引 | 保存指定《宇宙编程学》第三版 MinerU 全文和全部图片，按自然悖论/解答链生成逐字独立文档；显式悖论族命中必须被正文或明确 navigation/incidental 排除覆盖，不能用摘要代替原作 | R-011 | 已采纳 | 本地已实现并验证，未版本闭合 | SRC:`rulings.md#r-011--2026-09-01--最终抽象必然悖论目标与-matrix-全部悖论原文提取`；DES:`HoTT/sources/user-originals/matrix-book-paradoxes/README.md`；IMP:`HoTT/tools/matrix_book_paradox_extract.py`,`HoTT/sources/user-originals/matrix-book-paradoxes/CURRENT`；VER:`python3 HoTT/tools/matrix_book_paradox_extract.py validate`；EVD:`HoTT/sources/user-originals/matrix-book-paradoxes/generations/a18a4dcec701895cc959/MANIFEST.json`,`认知闭包/2026-09-01-HoTT-Z理论抽象必然悖论与Matrix悖论源-认知闭包.md`；GAPS:隐喻性未命名悖论可能漏检、原文主张未自动升级为数学/物理结论、外部源曾在本轮动态改写、Git 未版本闭合 |
| HOTT-009 | 理论参考/研究基础 | 建立权威来源可追溯、范围明确且持续补齐的 HoTT Theory Schema；覆盖核心规则、主要派生理论、语义/相干性、跨呈现计算、元理论、扩展与时间审查接口，区分来源/目录覆盖与逐证明完成 | R-015/R-016 | 已采纳 | 部分实现（v0.2 已完成本轮外部比较后获准的文档补充；21 份基线原文和105节入口保留；全书逐定理、全部变体规则与独立审查开放；未版本闭合） | SRC:`rulings.md#r-016--2026-09-09--schema-补充与-webcodex-chat-交接`；DES:`HoTT/THEORY_SCHEMA.md`；IMP:`HoTT/theory-schema/`；VER/EVD:`HoTT/theory-schema/SOURCES_AND_COVERAGE.md` §9；GAPS:G01–G08 |
| GOV-001 | 治理 | 正式 Git repo 保持根追踪文件、docs topic 入口和当前组件路由完整 | 全局治理规范 | 已采纳 | 本地已实现并验证，未版本闭合 | SRC:`AGENTS.md`；DES/IMP:`README.md`,`docs/README.md`；VER:`validate_governance_repo.sh`；EVD:`MEMORY.md` |

## 锚点合同

- `SRC`：ruling/spec/issue；`DES`：stable design/ADR；`IMP`：code/config/schema/runtime；
  `VER`：test/run/receipt；`EVD`：逐 Feature claim-to-asset-to-evidence 报告或等价 evidence bundle。
- `已验证` 必须五类可解析；缺失类别要显式降级，不能用“见相关文件”或 Feature 状态替代证据。
- 既有自由文本锚点在被触碰前可标 `LEGACY_PARTIAL`；没有直接证据时不要补猜。
- “本地已实现并验证，未版本闭合”表示当前工作树中有直接运行证据，但尚无最终业务 commit；
  不得据此声称其他 worktree、机器或外部发布已恢复。
