# 全局 codex 治理层成本盘点（~/.codex）

## 一、常驻层：`~/.codex/AGENTS.md`

| 指标 | 值 |
|---|---|
| 字节 | 66,117 |
| 行数 | 787 |
| CJK 字符 | 14,995 |
| **est tokens** | **≈ 20,474** |
| H2 章节数 | 29 |

这是 Codex 宿主**每个会话自动注入**的常驻指令（不同于项目文件需要显式读取），
即任何 repo、任何任务，先付 2 万 tokens 的全局宪法。29 个章节中与通用行为相关的
大块包括：按任务领域表达（L5）、Sub Agent 治理、认知闭包（L133/510 两处主题重叠）、
Session 启动与压缩恢复、文件变更前 Git 基线、治理框架自维护 Gate、项目认知强制 Skill
路由、AI 项目目录与领域 Skill 路由、vNext 合同路由、zvec-grep 两节等
（节名清单可直接 `grep -n '^## ' ~/.codex/AGENTS.md` 复核）。

**结构性观察**：这份文件同时承担"宪法+路由表+操作 SOP+产品事实"四种角色，且按
append-only 习惯增长（14 次修订可见于 `~/.codex/.git`）。它的 29 节里只有少数几节
对任意给定任务真正相关——常驻的是全集。

## 二、按需层：`~/.codex/skills/` 盘点

全部 md 文件 49 个、≈154,780 tokens（含 `.system` 系统技能与非治理技能）。治理相关两族：

**repo-* 治理/领域家族（16 个，共 ≈44,780 tokens）**：

| Skill | est tokens | | Skill | est tokens |
|---|---:|---|---|---:|
| repo-cognition-governance | 8,048 | | repo-verification-risk | 2,504 |
| repo-cognitive-closure | 7,733 | | repo-legacy-reconstruction | 2,107 |
| repo-subagent-governance | 3,624 | | repo-ai-system-governance | 1,881 |
| web-codex-governance-bootstrap | 3,167 | | repo-system-design | 1,885 |
| repo-agent-session-trajectory | 2,676 | | repo-structure-migration | 1,758 |
| repo-acp-multi-client-control | 2,546 | | repo-detailed-design | 1,725 |
| auditable-cognitive-closure | 1,659 | | repo-operations-lifecycle | 1,531 |
| repo-requirements-decisions | 1,528 | | repo-bootstrap-governance | 1,575 |
| repo-data-migration | 1,330 | | （dev-notes-archive 等） | — |

全局 AGENTS 的路由规则要求：非平凡 repo 任务必读 `repo-cognitive-closure`（7,733），
持久化写回再读 `repo-cognition-governance`（8,048），trajectory 分析再读
`repo-agent-session-trajectory`（2,676）——**典型治理任务的按需 Skill 增量为 ≈10–19K tokens**，
叠加在常驻 20.5K 与项目层义务之上。

**非治理大文件（顺带登记，不属于治理成本）**：`new-github-zcode`（≈24,880）与
`new-github`（≈24,194）两个 Skill 各 92KB；`.system` 系统技能若干。

## 三、磁盘层（非上下文成本，仅记录量级）

| 目录 | 大小 | 内容 |
|---|---:|---|
| `~/.codex/sessions/` | 5.2G | Codex 原始会话记录（全局，全部项目合计） |
| `~/.codex/worktrees/` | 1.1G | 并行 worktree |
| `~/.codex/plugins/` | 343M | 插件缓存 |
| `~/.codex/archived_sessions/` | 106M | 归档会话 |
| `~/.codex/skills/` | 1.3M | Skill 正文（上文已按 token 计） |

这些不进上下文，但说明同一治理习惯在宿主侧的累积形态；5.2G 的 sessions 也是
"真实消耗复核"的原始材料来源（见 011）。

## 四、全局层小结

- 每会话固定底价：**≈20.5K（常驻 AGENTS）+ 按需 Skill 1.6–4.5 万**。
- 全局层的最大问题是**宪法不分层**：29 节全量常驻，没有"核心 10 节常驻 + 领域节按需路由"
  的结构（对比：项目层已有分片与 LOAD_SET 分层机制，全局层反而没有）。
- 本报告不改动全局层；分层建议见 010 杠杆 G7。
