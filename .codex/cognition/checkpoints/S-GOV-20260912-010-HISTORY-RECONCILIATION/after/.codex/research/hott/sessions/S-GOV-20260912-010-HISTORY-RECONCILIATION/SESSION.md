# 历史覆盖登记、理解章节合并与核心 generation-2 Session

- session_id: `S-GOV-20260912-010-HISTORY-RECONCILIATION`
- scope: 完成双 GPT 历史来源的逐行 reconciliation register、两个理解章节的逐文件非破坏性合并收据、核心认知 generation-1→2 用户原文增补，以及对应 runtime checkpoint
- authorization: 用户已明确要求在完整审计方案后继续执行；不修改 `/Volumes/D/ALL-Markdown`、WebGPT 原 workspace、已移走的 `aistudio-docs` 或 nested 历史源
- mathematical_status: `UNCHANGED_FROM_R039_HISTORICAL_SCOPE`
- cognition_status: `EXHAUSTIVE_SOURCE_REGISTER_WITH_SCOPED_MANUAL_REVIEW`

## 实际执行

1. 生成 `audit/understanding-chapter-merge-manifest.json`：顶层目录 25 文件、nested 目录 24 文件、24 个同名，其中 15 对字节相同，9 个同名差异，顶层独有 C0；所有文件均有 hash、line diff、处置理由、rollback source。顶层 `理解章节/` 作为 canonical，nested 物理源保留，未执行删除。
2. 生成 `audit/cross-source-reconciliation.json` 和人读报告：WebGPT revision 41 的 91 条 STATE record、LocalGPT 384 response、3,146 tool event、16,209 work product、2,396 understanding claim，共 22,226 条逐项登记；每项均有 locator、方向/成果候选链接和显式语义状态。
3. 将 WebGPT R006–R017 的时间/有效交付结果族补入全景入口；保留 `REVIEW_REQUIRED` 和 `NOT_PERFORMED_BY_THIS_REGISTER` 边界。
4. 将用户关于三件套、压缩恢复、跨 LocalGPT/WebGPT 综观和逐文件融合的原文保存到新的 `sources/prompts/` 输入，由生成器生成 `core-cognition-generation-2`；旧 903 个 KC 的 payload/metadata 前缀逐项保持一致，新版本为 913 个 KC。

## 三方判定

- `core_change`: `APPEND_USER_UNIT`；只追加用户原文工作意识/交接要求，不写入 AI 结果或 audit 推断。
- `direction_change`: `STATUS_AND_RESULT_COVERAGE`；从有界初始投影升级为“全量来源登记、保留句级人工复核”的当前状态。
- `panorama_change`: `ADD_RESULT_FAMILIES_AND_MERGE_RECEIPT`；补入 WebGPT 早期结果族和理解章节可追溯合并结果。
- `update_decision`: `MULTIPLE_WITH_REASON`；core、direction、panorama、audit manifest 各自承担唯一职责，不能互相覆盖。
- `cross_conflicts`: `WEBGPT_REVISION_40_41`、`WEBGPT_SKILL_MANIFEST_1.3.3_ACTUAL_1.3.4`、`LOCALGPT_DIRTY_VS_SNAPSHOT`、`SENTENCE_SEMANTIC_REVIEW_PENDING`。
- `unresolved`: `A-AISTUDIO-COVERAGE-001`、`A-UNDERSTANDING-RECONCILIATION-001`、`A-HISTORICAL-MATH-CLAIMS-001`、`A-HISTORY-LEDGERS-001` 的人工句级/数学复核边界、模型实际理解认证。

## 结果边界

本 Session 完成的是来源覆盖登记、当前投影扩展、逐文件 merge receipt 和 core generation migration；规则/owner 路由不是人工数学语义判决，22,226 项的存在和链接不等于模型理解或数学证明。原始源、Git、tool、artifact 和 claim 必须沿 locator 回源；LocalGPT dirty 工作树、aistudio-docs 缺失和 WebGPT 版本漂移继续作为负证据保留。
