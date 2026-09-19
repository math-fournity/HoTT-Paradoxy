# 项目级 codex 治理资产盘点（.codex 与根级治理文件）

## 一、`.codex/` 总体（磁盘 218M）

| 子目录/文件 | 磁盘 | 内容与角色 |
|---|---:|---|
| `cognition/` | 187M | 其中 `checkpoints/` 139 个 checkpoint、6,068 个文件（见 007） |
| `research/hott/` | 30M | STATE.json 840K、sessions/ 188 个会话目录、RESUME/LESSONS/FRONTIER 等 |
| `skills/` | 492K | 本地治理 Skill + 两个业务 Skill（hott-paradox-research 32.9KB、search-sop 11.5KB） |
| `tools/` | 224K | `cognition_runtime.py` 52.6KB（canonical 加载器/checkpoint 引擎） |
| `AGENTS.md`/`README.md` | 4.4K/1.1K | 项目级治理入口（本身不大） |

## 二、治理正文档（上下文口径，est tokens）

| 文件 | est tokens | 屒属层 |
|---|---:|---|
| `.codex/research/hott/STATE.json` | 223,524 | always_full_boot（详见 006） |
| `.codex/skills/hott-paradox-research/SKILL.md` | ≈10,400（32,860B） | research_full |
| `.codex/skills/hott-paradox-search-sop/SKILL.md` | ≈3,800（11,523B） | 执行 SOP（命中时全文） |
| `.codex/skills/hott-local-session-governance/SKILL.md` | 5,833 | always_full_boot |
| `.codex/cognition/PROTOCOL.md` | 4,939 | always_full_boot |
| `.codex/cognition/LOAD_SET.json` | 1,498 | always_full_boot |
| `.codex/skills/SKILL_ROLES.json` | ≈240（911B） | always_full_boot |
| `.codex/research/hott/RESUME.md` | ≈33,000（105,102B） | research_full |
| `.codex/research/hott/LESSONS.md` | ≈20,000（59,984B） | research_full |
| `.codex/research/hott/FRONTIER.md` | ≈13,000（37,304B） | research_full |
| `.codex/research/hott/HOTT-PARADOX-...-COMPLETENESS`（索引+6片） | 16,229 | 系统化任务必读 |

## 三、根级治理与投影文件（上下文口径）

| 文件 | est tokens | 层 |
|---|---:|---|
| `AGENTS.md`（workspace，19,329B） | 6,016 | always_full_boot |
| `README.md` 逻辑文档（索引+4 片） | 8,235 | always_full_boot |
| `MEMORY.md` 逻辑文档（索引+3 片） | 39,716 | always_full_boot（003 片占 27,551） |
| `feature-list.md` | 3,190 | always_full_boot |
| `rulings.md` | 5,094 | always_full_boot |
| `核心认知.md` | 12,191 | always_full_documents（唯一单文件） |
| `方向追踪.md`（索引+5 片） | 13,786 | always_full_documents |
| `全景视野.md`（索引+8 片） | 41,857 | always_full_documents |
| `扩展认知.md`（索引+8 片） | 32,812 | always_full_documents |
| `核心认知.manifest.json` | 43,615 | query_first（不全文常驻） |
| `goal.md` + R4 记录 + 修订片008（active 补充） | 10,630 | active 记录 |

## 四、累积档案层（磁盘/写作累积，非启动加载）

| 区域 | 体量 | 说明 |
|---|---|---|
| `.codex/research/hott/sessions/` | 188 个会话目录；md+json 共 ≈705 万 est tokens / 24.8MB | 每会话 SESSION.md+审计集+RUNS.json（见 007） |
| `.codex/cognition/checkpoints/` | 139 个 / 187M | before/after 全量副本（见 007） |
| `理解章节/` | 166,468 | task_expand 水合池（按记录显式水合） |
| `dev-notes/` | 32 文件 / 370,157 | 用户问答逐字档案（常设规范产物） |
| `docs/quality/` 两合同 | 7,734 | 数学证明门禁 + 分片合同（task_expand） |
| `HoTT/` | ≈1.2 亿 est tokens（磁盘 407MB） | 证明源码+runs（按 claim 显式水合，仅盘面登记） |

## 五、加载机制要点（对成本的影响）

1. **分片不省上下文**：分片解决的是"单文件过大难以导航/编辑"，但 v2 合同规定
   "全文加载 = 索引 + 按 table 顺序全部分片"，runtime 3.6.1 在 plan 中强制展开并
   check 每片覆盖——分片后的逻辑文档总 token 不减反增（索引+每片 marker 头）。
   真正决定成本的是**文档属于哪一层**（always_full vs query_first vs task_expand）。
2. **query_first 层设计良好但用得少**：manifest、SOURCE_MANIFEST、audit 汇总都在
   query_first（按记录命中才提升），这层的存在证明框架本来就有"按需水合"的机制——
   问题在于最大的账本 STATE.json 被放在了 always_full_boot（见 006/009）。
3. **historical_session_auto_load=false** 是对的（历史会话不自动加载），
   但 STATE 内嵌的 174 条 session 记录绕过了这道闸（见 006）。
