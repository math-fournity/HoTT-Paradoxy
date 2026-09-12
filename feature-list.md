# Feature / 当前需求状态

本文件是当前 feature 状态 owner；历史来源中的“已完成”不自动改变这里的状态。

| ID | 需求 | 当前状态 | 证据/下一步 |
|---|---|---|---|
| F-001 | 顶层目录成为综合 Git repo，保留原嵌套来源边界 | IMPLEMENTED | `git log`、`.gitignore`、`audit/governance-impact.md` |
| F-002 | 保存 LocalGPT、WebGPT、Gemini 来源快照和 provenance | IMPLEMENTED_WITH_SCOPE | `sources/SOURCE_MANIFEST.json`；私有 trajectory 仅在 ignored `private-audit/` |
| F-003 | 三份用户悖论/元数学认知原文按时间和语义单元组成连续编号 `核心认知.md`；现有 generation-2 治理 supplemental 保留为历史，但未来一般治理过程不得继续进入 core | VERIFIED_WITH_SCOPE_AND_INGESTION_BOUNDARY | `rulings.md` §2–§3、§9；`核心认知.manifest.json`、`scripts/audit/verify_core_cognition.py`、`audit/core-cognition-generation-transition-20260912.json`；generation-2、913 KC，前 903 KC identity 保持，本轮不重写现有 KC |
| F-004 | 记录所有可见 AI response、tool event、work product、claim-evidence | VERIFIED_WITH_SCOPE | 四类主 ledger + WebGPT/Gemini 专项 ledger + `audit/cross-source-reconciliation.json`；句级语义裁决仍明确待人工复核 |
| F-005 | 建立顶层 `.codex` 本地治理：每次新 Session/压缩恢复按 `核心认知.md`→`方向追踪.md`→`全景视野.md` 全文加载；核心作为用户反训练惯性的上下文工程，方向/全景作为全局统筹面；并提供动态状态、三方交叉审视、结束逐 KC 回评和可恢复 checkpoint | IMPLEMENTED_MECHANICALLY_WITH_OVERBROAD_LOAD_GRAPH | `rulings.md` §9–§11、`.codex/`、STATE revision 12、runtime plan、三方 validator、fresh/负向 receipt；三件套已固定但当前 105 文档 load graph 过宽，模型实际摄入/理解仍未认证 |
| F-006 | 以审计结果更新 `理解章节/`，达到交接/博士论文级而非摘要级 | IN_PROGRESS_WITH_FILE_LEVEL_MERGE | 已新增 C0、历史边界层、逐文件 merge manifest 和 canonical 顶层选择；2,396 条 claim 的句级语义/数学 owner 修订仍待下一波 |
| F-007 | 不恢复用户移走的 `aistudio-docs`，明确替代材料覆盖是否可证明 | VERIFIED_BOUNDARY | 缺源 validator 失败；coverage 仍 `NOT_PROVEN` |
| F-008 | 未来每个工作单元按核心认知逐编号评估方向 | VERIFIED_WITH_SCOPE | `.codex/cognition/PROTOCOL.md`、三件套交叉合同、session `CORE_COGNITION_AUDIT.md`；当前 generation-2 的 913 KC 均有回评 |
| F-009 | 以 `方向追踪.md` 和 `全景视野.md` 统筹两个 GPT 的历史方向/成果，并与 `核心认知.md` 交叉决定更新归属；不把 AI 结果写入用户原文 | EXHAUSTIVE_REGISTER_WITH_SCOPED_SEMANTIC_REVIEW | `方向追踪.md`、`全景视野.md`、`audit/cross-source-reconciliation.json`、审计/方案；22,226 行均可发现和回源，2,396 条 claim 的直接语义仍开放 |
| F-010 | 治理精简必须永久保留三件套当前逻辑全文作为每次压缩恢复的不可替代输入；只能将三件套之外的机器索引、历史收据和任务证据分层查询/按需加载，行为测试不能替代全文输入 | REQUIREMENT_ACCEPTED_DESIGN_REVISED_NOT_IMPLEMENTED | SRC：`rulings.md` §9–§11及其用户原文；DES：`audit/治理框架跨压缩连续性独立复审与精简升级方案-20260912.md` v2；IMP：当前 LOAD_SET 已保证三件套在前三项但仍过宽；VER：需未来 full-trio input receipt + fresh AI behavior 双轨验收 |
