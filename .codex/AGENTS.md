# `.codex` 本地治理入口

本目录是当前顶层 repo 的项目级 Codex 治理资产，不是全局 `~/.codex` 的替代品。先读顶层 `AGENTS.md`，再全文读 `.codex/skills/hott-local-session-governance/SKILL.md`、`.codex/cognition/LOAD_SET.json`、`.codex/cognition/PROTOCOL.md` 和动态 `STATE.json`。

四件套 invariant：每次新 Session、再次进入、跨 repo 接手和压缩恢复，都必须按固定顺序全文加载
`核心认知.md` → `方向追踪.md` → `全景视野.md` → `扩展认知.md`（AI 阐释层，`essay-role:v1`；`核心认知.md` 是唯一用户原文权威）。`核心认知.md` 拥有用户原始研究意识；`方向追踪.md`
拥有跨 LocalGPT/WebGPT 的候选组合与下一判别动作；`全景视野.md` 拥有研究结果、正反例、失败和未知的
可读综合投影；三者不得互相覆盖成为“最新版”。

分片 invariant：命中 `governance-shard-index:v2` 的 canonical 路径是逻辑文档索引，不是摘要。读取时先读完整
shard table、`last_shard` 与 `append_target`，再按任务读 owner/append shard；"全文加载"对分片文档意味着
索引 + 按 table 顺序全部分片，缺任一片即未完成全文加载。写入时 topical 改 owner shard、sequential 追加到
`append_target`，新建 shard 必须与索引行、`last_shard`、`append_target` 在同一 commit 或同一 checkpoint
事务中更新。300 行只是软目标，不是上限；当前已分片 `README.md`、`MEMORY.md`、`理解章节/C1`–`C4`、
`方向追踪.md`（5 片）、`全景视野.md`（8 片）——两个投影的大表按家族拆行分片、每片自带表头，身份字段
（marker 块、`source_state_revision`、`projection_generation`、`semantic_status`）留在索引；`核心认知.md`
仍是四件套中唯一单文件。每个索引前 15 行带首屏 banner（`> ⚠️ 逻辑文档索引：全文 = 本索引 + 下方 N 个分片；缺一片即未完成`），
由 `scripts/audit/verify_governance_shards.py` 机械检查。合同见 `docs/quality/长治理文档分片与索引合同.md`。

核心 invariant：当前 generation 与 KC 分母从 `STATE.current_core`/manifest 动态取得（本轮 generation-7，46 个 KC）；用户直接原文单元由 hash-pinned curation lineage+生成器管理，不手工改写；全部 record
在 STATE 全文中可见，但只有 lifecycle 给予当前任务资格，evidence review 不得自动复活历史 Session。治理任务用
governance profile，数学研究用 research profile，底层证据按 stable ID 显式水合。每轮结束仍产生当前全部
`KC-*` 回评；旧回评归档而不常驻。工具只能证明字节覆盖、引用和版本边界，不能证明模型理解或数学真理。

业务研究入口是 `.codex/skills/hott-paradox-research/SKILL.md`。方案执行与方案演化 SOP 入口是 `.codex/skills/hott-paradox-search-sop/SKILL.md`（由 `goal-1.md` 索引驱动；角色登记见 `.codex/skills/SKILL_ROLES.json` 的 execution role）。历史 WebGPT `.codex` 框架在 `sources/webgpt/workspace-snapshot/.codex/`，只作为参考来源。

Record 关系 invariant：`depends_on` 只用于会传播 stale 的验证依赖；谱系、动机、接续和叙事归属使用
`research_parent`/`related_records`，不会递归水合。显式 task plan 必须检查 `hydration_diagnostics`；query-first
账本被间接提升为正文或计划无法在宿主上下文中完整装配时，不得只凭 `review_required=[]` 宣称可接手。

Checkpoint invariant：每次 applied checkpoint 必须原子包含 `SESSION.md`、`RUNS.json` 与当前 generation 的全量、
有序 `CORE_COGNITION_AUDIT.md`，并以 `.codex/cognition/checkpoints/<session-id>/result.json` 的
`CHECKPOINT_COMMITTED` 为唯一应用收据。`POST-CHECKPOINT.json` 是派生摘要，不得自证；历史缺失不回填伪造。

<!-- math-proof-delivery-gate:v1 -->
数学结论交付还必须执行根 `AGENTS.md` 的 `MATH_PROOF_BEFORE_DELIVERY_V1`：精确形式命题与证明源码进入 `HoTT/formal/`，实际 kernel 运行和原始结果进入 `HoTT/verification/runs/<run-id>/`，索引进入 `HoTT/CLAIM_EVIDENCE_MATRIX.md`。无法形成这些本地持久证据时，只能交付 `QUESTION/CONJECTURE/HEURISTIC/PAPER_ONLY/SOURCE_REPORTED_NOT_REPLAYED`，不得写成当前 AI 已证明的数学结论；`/tmp` 只可承载可删除缓存，不能成为唯一证据位置。
