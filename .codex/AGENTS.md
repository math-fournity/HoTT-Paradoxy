# `.codex` 治理树导航页

> v5（2026-09-18）：本页**只导航，不复述任何规则/数字/不变量**——一切规则的唯一权威是
> 下表 owner 文档；历史版本的复述式不变量清单（含已漂移的 generation 数字）由
> 本导航页取代，Git 历史可回溯。目录名为历史遗留，不构成宿主绑定：任何能读文件
> + 执行 `python3` 的宿主（Codex CLI / ZCode Desktop / 其他）共用本树。

| 路径 | 唯一职责 |
|---|---|
| `../AGENTS.md`（repo 根） | 宪法与分档路由（T0–T3）——更高层入口 |
| `cognition/PROTOCOL.md` | 执行合同（会话生命周期步骤、档位深度、invariant 章、审计与 checkpoint 规则） |
| `cognition/LOAD_SET.json` | 机读加载清单（层归属 + v5 tier 扩展键） |
| `skills/SKILL_ROLES.json` | 三角色名册（governance/business/execution） |
| `skills/hott-local-session-governance/SKILL.md` | 治理 SOP 差异层（BLOCKED 协议、审计集格式、历史覆盖分母） |
| `skills/hott-paradox-research/SKILL.md` | 业务研究方法论 |
| `skills/hott-paradox-search-sop/SKILL.md` | 方案执行 SOP（goal-1.md 索引） |
| `tools/cognition_runtime.py` | canonical 加载器/checkpoint 引擎（`plan`/`read`/`check`/`query`/`checkpoint`） |
| `research/hott/STATE.json` | 机器真值账本（身份与分母从 `current_core` 动态取得） |
| `research/hott/sessions/`、`cognition/checkpoints/` | 会话档案与事务收据（不自动常驻） |
| `../docs/quality/*.md` | 分片合同、数学证明门禁等稳定规范 |

硬入口不变量（仅为指针，正文见 owner）：四件套全文加载与顺序 → `LOAD_SET.always_full_documents`；
数学结论交付门禁 → 根 AGENTS `MATH_PROOF_BEFORE_DELIVERY_V1` + `docs/quality/数学结论机器证明与证据留存规范.md`；
checkpoint 原子性与唯一收据 → `PROTOCOL` invariant 章。
