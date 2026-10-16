# project-local governance v3.3.0：分片基础与合同（CP-1 证据）

> 会话：`S-GOV-20260913-094-SHARD-FOUNDATION`（revision 94）
> 范围：逻辑文档加载能力 + 分片合同 + 校验入口；**不含**任何既有文档的迁移（迁移在 CP-2 / revision 95）
> 边界：只改治理与加载结构，不改任何 KC、数学判词、proof source/run/index；不 push

## 1. 本轮建立了什么

| 资产 | 变化 | 作用 |
|---|---|---|
| `.codex/tools/cognition_runtime.py` | 3.2.0 → **3.3.0** | 解析 `governance-shard-index:v2`，把逻辑文档展开为"索引 + 按 table 顺序全部分片"；`check` 必须覆盖每一片；结构错误 fail closed；`MUTABLE` 逻辑文档的分片进入 `HEAD.json.tracked` |
| `.codex/cognition/LOAD_SET.json` | 3.2.0 → **3.3.0** | 新增 `shard_contract`（合同文档、校验入口、300 行软目标非上限） |
| `.codex/cognition/PROTOCOL.md` | v2.3 → **v2.4** | 新增 §3B；§2 第 3 步明确"逐文件读到 EOF"对分片文档 = 索引 + 全部分片 |
| `.codex/skills/hott-local-session-governance/SKILL.md` | 3.2.0 → **3.3.0** | 分片读取/写入不变量、`MEMORY/` 追加目标、`HEAD` 跟踪约束 |
| `AGENTS.md` / `.codex/AGENTS.md` | 新章节 / 新 invariant | 启动路由可发现分片规则；三件套与 proof matrix 的保留项与触发条件 |
| `docs/quality/长治理文档分片与索引合同.md` | 新增 | 项目合同：判定标准、v2 标记与命名、读写算法、校验、迁移程序、已分片/保留项 |
| `scripts/audit/validate_governance_shards.py` | 新增（pin 副本） | 共享 3.16.0 候选校验器，source commit `2e4e4d2`、source sha256 `fb75648…` |
| `scripts/audit/verify_governance_shards.py` | 新增 | sha256 漂移检测 + `--scan` 执行 + `governance-shard-verification/v1` receipt |
| `scripts/audit/shard_migrate_document.py` | 新增 | 一次性迁移工具：内容逐字搬运 + 行对账（默认 dry-run） |
| `.codex/skills/hott-paradox-research/checks/test_cognition_runtime.py` | +5 测试 | 分片展开顺序、全分片覆盖、结构 fail-closed、`HEAD` 跟踪、`SHARD_NOT_IN_CHECKPOINT` |
| `feature-list.md` / `rulings.md` | F-013 / §17 | 需求与用户裁定入口（F-013 在 CP-1 为 `IN_PROGRESS_FOUNDATION_ONLY`，CP-2 后升级） |

## 2. 为什么不是"按行数硬拆"

300 行是写作与换片软目标：超行只产生 `NOTICE`，不是错误、Gate 或清理配额。判定依据是"持续追加、
妨碍定位、稳定入口与长历史混装、存在自然语义边界"。因此本轮迁移（CP-2）只覆盖 6 个活跃且混装的逻辑文档；
已完成审计报告、来源快照、历史交付分卷、`AGENTS.md`、proof matrix 与三件套保持单文件并登记触发条件。

## 3. C01–C10 影响分类（项目本地自维护 Gate）

| ID | 判定 | 说明 |
|---|---|---|
| C01 | UPDATE | `rulings.md` §17 记录用户裁定与五项边界；`feature-list.md` 新增 F-013 |
| C02 | UPDATE | 真值 owner 不变（索引仍在 canonical 路径），但新增长期合同 `docs/quality/长治理文档分片与索引合同.md` |
| C03 | UPDATE | 本地治理 Skill 3.3.0 自包含分片规则；共享 workflow/规范未改 |
| C04 | UPDATE | 根 `AGENTS.md`、`.codex/AGENTS.md`、`LOAD_SET.json`、`PROTOCOL.md` 形成确定性启动路由 |
| C05 | UPDATE | Feature/README/docs 路由更新；`README.md`/`MEMORY.md` 正文迁移在 CP-2 |
| C06 | UPDATE | 新增 validator 副本/包装器与 5 条 runtime 负向测试；复用既有 fresh/projection 校验 |
| C07 | NO_CHANGE | 未改 Codex config、Rules、Hooks、插件、权限或 secret 边界 |
| C08 | NO_CHANGE | 共享主库 `/Users/aurolafly/codex` 未改；3.16.0 仍是候选，已记录版本分歧与再同步触发条件 |
| C09 | UPDATE | runtime/LOAD_SET/PROTOCOL/Skill 版本升位；boundary tag `governance-v3.2.0-pre-sharding` 已建；`governance-v3.3.0` 待 CP-2 后 |
| C10 | UPDATE | 历史 `prepare_*.py` receipt 冻结说明（不批量改写、不重跑）；残余未知见 §5 |

## 4. 验证

CP-1 canonical checkpoint：`.codex/cognition/checkpoints/S-GOV-20260913-094-SHARD-FOUNDATION/result.json`
（`CHECKPOINT_COMMITTED`，revision 94；`model_understanding=NOT_CERTIFIED`、`mathematics=NOT_CERTIFIED`）。

| 检查 | 命令 | 结果 |
|---|---|---|
| 分片结构与软目标 | `python3 -B scripts/audit/verify_governance_shards.py --out <session evidence>/governance-shards-receipt.json` | `PASS`；indexes=0（本轮未迁移）、notices=0；`line_targets_blocking=false` |
| runtime 单测 | `python3 -B .codex/skills/hott-paradox-research/checks/test_cognition_runtime.py` | `Ran 37 tests ... OK`（原 32 + 新增 5 条分片测试） |
| fresh 冷启动 | `python3 -B scripts/audit/verify_fresh_three_way.py` | `PASS_WITH_SCOPE`，revision 94，governance_documents=15、research_documents=20，负向用例 4 项通过；`model_behavior=NOT_RUN` |
| projection 新鲜度 | `python3 -B scripts/audit/verify_projection_freshness.py` | `PASS_WITH_SCOPE`（revision 94 = 投影 revision） |
| 三件套结构与顺序 | `python3 -B scripts/audit/verify_three_way_cognition.py` | `PASS` |
| 数学交付门禁结构 | `python3 -B scripts/audit/verify_math_proof_delivery_governance.py` | `PASS_WITH_SCOPE`（`AGENTS.md` 新增路由章节后 re-pin，带 `revalidation` 说明） |
| core / merge / 跨源 / 历史账本 | `verify_core_cognition.py`、`verify_understanding_merge.py`、`verify_cross_source_reconciliation.py`、`verify_history_ledgers.py` | 全部 `PASS`/`PASS_WITH_SCOPE` |
| HEAD 跟踪 | `plan`（runtime 3.3.0） | `MEMORY.md`/`方向追踪.md`/`全景视野.md` 及 state 文件全部与 `HEAD.json.tracked` 一致 |

## 5. 残余未知与边界

- **fresh model behavior NOT_RUN**：本轮只证明结构与字节层行为，不证明未来模型会正确读写分片。
- **共享主库版本分歧**：`/Users/aurolafly/codex` 仍提供旧 v1/200 行版本，3.16.0 未打 tag；本项目按用户选择 pin 候选副本，
  触发条件：共享主库发布 `governance-v3.16.0` 后重新同步并更新 provenance 头。
- **第二波保留项**：三件套、`HoTT/CLAIM_EVIDENCE_MATRIX.md`、`HoTT/HoTT研究三问…md`、`docs/quality/数学结论机器证明与证据留存规范.md`
  未迁移，触发条件已写入合同 §7。
- 数学目标、E6 consumer、T3 联合递归等研究状态不受本轮影响；未新增或修改任何数学结论。
