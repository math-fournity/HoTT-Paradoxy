# Cross-source provenance label correction Session

- session_id: `S-GOV-20260912-012-PROVENANCE-LABEL-FIX`
- scope: 修正 384 条 AI response ledger 的来源类别措辞，重新生成/验证跨源 register，并持久化 revision 12 checkpoint
- authorization: 用户已要求完整审计和执行方案；不修改外部源、不恢复 `aistudio-docs`、不删除 nested 历史源
- mathematical_status: `UNCHANGED_FROM_R039_HISTORICAL_SCOPE`
- cognition_status: `PROVENANCE_LABELS_CORRECTED_WITH_SCOPED_SEMANTIC_REVIEW`

## 三方判定

- `core_change`: `NONE`；用户原文和 generation-2 不变。
- `direction_change`: `NONE_SEMANTIC_CHANGE`；只同步 source-class 事实标签和 STATE revision。
- `panorama_change`: `CORRECT_STATUS_LABEL`；总分母和结果内容不变。
- `update_decision`: `TECHNICAL_OWNER`；错误属于 provenance 表述，更新 register/report/STATE，不改 core。
- `cross_conflicts`: `MODEL_CONTEXT_NOT_CERTIFIED`、`WEBGPT_REVISION_40_41`、`LOCALGPT_DIRTY_VS_SNAPSHOT`。
- `unresolved`: `A-AISTUDIO-COVERAGE-001`、`A-HISTORY-LEDGERS-001`、`A-UNDERSTANDING-RECONCILIATION-001`、`A-HISTORICAL-MATH-CLAIMS-001`。

## 结果边界

修正后 384 条 response 明确为 LocalGPT 305 + WebGPT 55 + Gemini 24；这只是来源类别纠正，不是将 384 条都归给 LocalGPT。register 总数仍为 22,226，数学认证和模型理解均未由本 Session 提供。
