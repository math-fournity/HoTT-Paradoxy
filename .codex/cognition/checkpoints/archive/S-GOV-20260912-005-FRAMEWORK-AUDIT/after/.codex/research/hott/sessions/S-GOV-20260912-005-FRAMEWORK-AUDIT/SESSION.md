# 治理框架对比与三件套升级 Session

- session_id: `S-GOV-20260912-005-FRAMEWORK-AUDIT`
- scope: WebGPT 治理框架与顶层本地治理框架的证据比较；三件套初始投影；core 内容边界审计
- authorization: 用户明确要求逐个读取 WebGPT 的 Skill、AGENTS 与治理结果，比较框架并升级当前 repo；本轮不修改 WebGPT workspace、`/Volumes/D/ALL-Markdown`、用户移走的 `aistudio-docs` 或数学源
- mathematical_status: `UNCHANGED_FROM_R039`；本轮没有开始新的 HoTT 数学研究
- cognition_status: `BOUNDED_GOVERNANCE_COMPARISON_WITH_CORE_AUDIT`；工具/文件完整性不证明模型理解

## 本轮读取的决定性来源

- WebGPT：`.codex/AGENTS.md`、两类 Skill、`PROTOCOL.md`、`LOAD_SET.json`、`STATE.json`（91 records）、`FRONTIER/LESSONS/RESUME`、portable governance、R039 结果与 v1.2/v1.3/r040 验证结果、Git history。
- LocalGPT：`/Volumes/D/ALL-Markdown` 当前 branch/HEAD/dirty、HoTT current owners、MEMORY/Feature/rulings、Git 和顶层已保存 source/audit ledger。
- 顶层：`核心认知.md` generation-1（903 KC）、三件套方案、当前 `.codex`、理解章节双目录 inventory 和路径/版本边界。

## 比较结论

WebGPT 在单一 HoTT 工作区的动态研究连续性、91 条 STATE 记录、逐轮结果文件、checkpoint/恢复/交换和 R039 的正反例承载上更成熟；顶层 repo 在跨 LocalGPT/WebGPT/Gemini 的用户原文、跨 repo provenance、四类审计 ledger、理解章节双目录和综合 repo 边界上更强。两者都不能证明模型实际理解或数学真理。详细的逐维度证据表在 `治理框架对比审计与核心认知增补评估-20260912.md`。

## 三件套交叉判定

- `core_change`: `NO`（本轮没有把 AI 结果手工追加到 core；generation-1 保持原 hash）
- `direction_change`: `YES`（新增跨 AI 初始方向 portfolio）
- `panorama_change`: `YES`（新增跨 AI 初始成果/证据 panorama）
- `update_decision`: `UPDATE_DIRECTION_AND_PANORAMA_ONLY; CORE_ADDITION_DESIGN_PENDING_GENERATION_MIGRATION`
- `cross_conflicts`: WebGPT README revision40 vs STATE/MEMORY revision41；WebGPT manifest Skill 1.3.3 vs actual Skill 1.3.4；LocalGPT live dirty vs snapshot
- `unresolved`: WebGPT/LocalGPT 逐条语义 mapping、理解章节最终融合、fresh/compaction 行为和 core generation-2 原文捕获

## 实施与验证

- 新增 `方向追踪.md`、`全景视野.md`、框架比较审计文档和三件套 validator/test。
- `.codex` 固定前三项改为 `核心认知.md`→`方向追踪.md`→`全景视野.md`，runtime 的 required/mutable 集合和三方协议已接入。
- WebGPT 的历史 record 未被删除、重命名或直接写回；投影保持 `INITIAL_INTEGRATED_PROJECTION`。
- checkpoint 由唯一 runtime 从 revision 4 提升到 revision 5，带 before/after/transaction/HEAD 回读；之后还需运行最终 validators 和 Git 检查。
- core 903 条 KC 的全量逐编号回评已保存；本轮只有治理/证据主题被标 `DEEPENED`，其余数学业务单元诚实标 `NOT_TOUCHED`。

## 结果边界

本 Session 的文档、状态和 validator 是治理升级证据，不是 WebGPT 数学结果的重新认证；`model_context` 保持 `NOT_CERTIFIED_BY_TOOL`。`核心认知.md` 是否增加本轮用户治理原文，已形成设计建议但尚未执行 generation-2。
