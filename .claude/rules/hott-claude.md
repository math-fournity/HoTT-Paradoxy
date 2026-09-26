# Claude Code 在本仓库的工作规则

> 2026-09-24，用户授权 Claude 为 Claude Code 设计自己的机制；本文件由 Claude 编写，只写 Claude 会话专属的替换与补充。根 `AGENTS.md`（与 Codex 共用）仍是项目宪法。涉及研究内容、证据门禁、来源边界、写入权限时，以 AGENTS.md、《核心认知.md》和用户当前指令为准；本文件决定的只是 Claude 用什么机制去执行它们。设计说明见 `dev-docs/Claude-goal-x机制设计-20260924.md`。

## 1. AGENTS.md 里的 Codex 机制，在 Claude 会话中怎么做

| AGENTS.md 中的 Codex 机制 | Claude 会话的做法 |
|---|---|
| 全局 `repo-cognitive-closure` 作为第一语义动作 | 按 `~/.claude/CLAUDE.md` 的“认知闭包优先”执行；长任务用 goal-x |
| 所有 Session 全文读单体《最高指示.md》 | 使用《最高指示-Claude版.md》：它经本目录的链接常驻上下文，并按其 §9 在关键时刻用 Read 重读。原版是它的思想来源，冲突时以原版和核心认知为准 |
| `.codex/skills/*` 与 `.codex/cognition/TASK_ROUTING.md` | Claude 不会自动发现这些 Skill；需要时用 Read 读原文 |
| Codex `/goal` 宿主 | Claude 原生 `/goal` 负责续跑和完成判定；goal-x 负责闭包、状态和恢复 |
| 禁止 Sub Agent（2026-09-17 用户裁定） | Claude 不调用 Agent 工具 |
| dev-notes 对话归档（Codex 全局规则） | Claude 会话不强制；用户要求时再做 |

## 2. 每个会话

1. 先确定用户当前的目标和角色（《最高指示-Claude版》§8）。不因为文件存在就自动启动研究或复活旧 goal。
2. 要解释、评价或纠正用户的悖论观、数学哲学、原意、研究方向选择时，先回读相关 KC 原文和扩展认知分片（AGENTS.md 的 `CORE_SEMANTIC_REALIGNMENT_V1`），再评价；把忠实复述和我的评价分开写。
   **归因是正题**（用户 2026-09-24 修正，逐字见《最高指示-Claude版》§1.3）：不以“归因是下一个故事”推迟或回避归因；用户提到归因或候选已有现象时，直接展开候选前提、竞争归因、能区分它们的证据和我的判断。
3. 研究或审计任务，按 AGENTS.md 的档位加载四件套等材料。数学结论交付前要过 F-011 机器证明门禁。
4. **写入边界**：研究 STATE、MEMORY、方向追踪、全景视野、核心认知以及各 Session 目录，由当前的研究 integrator 维护（2026-09-24 为 Codex Session C，以 STATE 和 MEMORY 核实当前身份）。没有用户明确授权，Claude 不写这些文件，也不改他人未提交的文件。Claude 自己的产物写在 `.claude/`、自己 goal 声明的路径，或用户指定的位置。
5. 不 push、不发布；commit 只在用户授权时按精确路径做。

## 3. goal-x

- 本仓库已开启 goal-x（`.claude/goal-x/project.md`）：会话启动、恢复、压缩后会收到 `[goal-x 回执]`，每条用户消息附一行提醒。
- 回执显示本会话绑定了 goal 时，先调用 goal-x Skill（`resume <ID>`），用 Read 重读闭包文件，写出恢复说明，再继续。局部任务完成不等于 goal 完成。
- Claude 的目标包放在 `.claude/goals/CG-NNN-<slug>/`，与 Codex 的根目录 `goal-N.md` 编号互不占用。

## 4. 总索引（2026-09-24 按用户要求建立）

- `.claude/总索引.md` 是 Claude 在本仓库全部工作、思考与发现的唯一入口：目标包、交接、中继、工作台、证明包、运行、命题，以及 CN 编号的思考与发现笔记（正文在 `.claude/思考与发现/`）。
- **开工时**：做 Claude 线的研究、答“做到哪了、有哪些发现”、或恢复与压缩之后，先按分片表读完总索引全文（索引 + 001–005），再按本文件 §2 读其他闭包。总索引不豁免任何闭包。
- **维护**：每个工作单元结束、会话结束前、上下文接近压缩前、用户纠正或裁定之后，按 `.claude/总索引/001 - 使用与维护规则.md` §3 维护：002 原位更新；003、004 追加登记行；005 只追加。思考和发现先落盘，再登记；只在对话里说过的，不算登记。
- 结构校验：`python3 -B scripts/audit/verify_governance_shards.py`，须为 PASS。
