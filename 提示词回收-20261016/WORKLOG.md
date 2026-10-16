# WORKLOG：找回所有研究发起人发给 AI 的提示词（2026-10-16 启动）

> **这份文档是接手契约**：任何 AI 中途接手，读完本文件即可继续，不需要重做侦查。
> 维护纪律：**每完成一步立即更新本文件的进度表和备忘**；中断前把"正在做什么、卡在哪"写进"当前状态"。

## 任务定义（研究发起人 2026-10-16 原话要点）

找回**所有**研究发起人发给 AI 的提示词（用户发出的内容），三个平台：

| 平台 | 对话录位置 | 已有工具 | 本任务要做的 |
|---|---|---|---|
| **Codex** | `~/.codex/sessions/YYYY/MM/DD/rollout-*.jsonl.zst` 与 `~/.codex/archived_sessions/` | `trajectory-gui-ref-export` Skill（按 GUI title 导出 GUI 可见内容，1791 行，canonical 实现在 `/Users/aurolafly/codex-worktrees/pdag-isolated-runner-route/tools/trajectory_gui_ref_export.py`，wrapper 在 `~/.codex/governance-tools/`） | **改写/派生脚本：只导出用户消息**（不做 title 解析、不带 assistant 回复、不带 FileChange） |
| **ZCode** | `~/.zcode/cli/db/db.sqlite`（session/message/part 三表，**比 rollout 文件全**）＋ `~/.zcode/cli/rollout/model-io-sess_*.jsonl` | `~/.zcode/skills/zcode-gui-session-export/`（GLM 2026-10-15 建，sqlite 只读，gui/audit 双模式） | 派生一个 **--only-user** 模式或独立脚本，按项目过滤批量导出全部 HoTT 会话的用户消息 |
| **Claude** | `~/.claude/projects/<路径编码目录>/<session-id>.jsonl`（29 个项目目录，目录名是工作目录全路径的 `-` 编码） | **无现成 Skill**——但 jsonl 格式已被 GLM 会话完全摸清（见下备忘） | 写一个 Claude 版用户消息导出器（格式与 ZCode 版同构） |

**输出位置**：`/Volumes/D/HoTT_AI_HANDOFF_20260911/提示词回收-20261016/`（dev 工作区内）下按平台分子目录。**隐私边界：只导用户消息，不带 AI 回复、思考、工具结果**（研究发起人明确"只把用户发的内容导出出来"）。

## 定位 HoTT 相关对话录的两条路（研究发起人给出的策略）

1. **路径规律**（优先）：对话录内部记录了会话的 cwd。把硬盘上所有 HoTT 工作树的实际全路径列成清单，逐一匹配。
   - Codex rollout：每条 jsonl 的头部 session_meta 含 cwd（待验证具体字段名）。
   - Claude：**projects 目录名就是路径编码**（`/`→`-`，`_`→`-`），29 个目录清单已固化在 `source/claude-projects.txt`。
   - ZCode：db.session 表有 project_id（如 `proj_volumes-d-hott_ai_handoff_20260911`）。
2. **关键词兜底**（简单粗暴但可靠）：对话录必然有工具调用，工具调用大概率含 `HoTT` 字样；再加关键词 `悖论`、`芝诺`、`形式化与机器证明`、`ZFC`。zst 文件用 `zstdcat` 流式扫描，不落盘解压。

## 已固化的知识（GLM 会话 2026-10-15/16 侦查所得，接手者免重查）

### 工作树清单
- `source/worktrees.txt`：`git worktree list` 全量 41 条（2026-10-16 固化）。
- 历史（已删）工作树的化石：`~/.claude/projects/` 的 29 个目录名（`source/claude-projects.txt`，待固化）——其中含已删除的 `godel-q-zfc-z0-full` 嵌套 worktree、`git-worktree-path-4c282f/5657c0`、`9276`、`HoTT-Git-Worktree` 等。
- 更多细节见 `../.claude/goals/CG-010-remaining-formalization-alignment/待你裁定-人话版/15-工作区完备性审计-20261015.md`（Opus 线工作目录里的全面审计）。

### Claude jsonl 格式（已验证，012-Opus 会话实测）
- 每行一个 JSON；用户消息 `type=="user"`，`message.content` 为字符串或块数组（取 `type=="text"` 块）。
- **真实用户输入的判据**：无 `metadata.source`、无 `synthetic` 标记（todo_reminder/agent_listing_delta 等注入都带 source）；`isMeta` 行（命令回显如 `/model`）要排除；`tool_result` 排除。
- 会话 62MB 级别要用 python 流式处理，不能整读。

### ZCode sqlite 结构（已验证）
- `session(id, parent_id, project_id, ...)`——fork 链在 parent_id；`message(id, session_id, time_created, data)`——data 含 role/metadata；`part(message_id, session_id, data)`——type=text 是正文。
- 真实用户消息判据同 Claude（metadata 无 source/synthetic）。rollout JSONL 是另一证据层（本任务可不用）。

### Codex 侧（待接手者验证）
- `~/.codex/sessions/2026/{08,09,10}/<日>/rollout-<时间戳>-<会话id>.jsonl.zst`（按日期组织，zstd 压缩）。
- `~/.codex/archived_sessions/`（内容待查）。
- 原 Skill 的关键函数（可参考复用）：`iter_jsonl_with_offsets`（流式带偏移读 jsonl）、`read_rollout_segment`、`scan_rollout_segments`、`resolve_gui_title`（本任务**不需要** title 解析）。
- **工具决策（GLM 建议，研究发起人可否决）**：不改动 canonical 的 1791 行原 Skill 本体，而是写**派生轻量脚本** `codex_user_prompts_extract.py`（zstdcat 流式 → 提取 user 消息 → 按 cwd/关键词过滤）——原 Skill 按 GUI title 精确导出、我们的场景是全量按项目扫，使用场景不同；派生不污染 canonical。

## 进度表

| # | 步骤 | 状态 | 结果/备注 |
|---|---|---|---|
| 1 | 建工作目录＋WORKLOG | ✅ 2026-10-16 | 本文件 |
| 2 | 固化工作树清单 | ✅ | `source/worktrees.txt`（41 条）＋`source/claude-projects.txt`（28 个目录） |
| 3 | Codex 侧侦查 | ✅ | 516 个 zst（sessions 344＋archived 172）；`payload.cwd` 在首行 session_meta；用户消息=`response_item/message`+`role=="user"`；注入判据（已实证）：前缀 `# AGENTS.md instructions`/`<app-context>`/`<environment_context>`/`<user_instructions>`/`<turn_aborted>`/`# Codex desktop context`/`<permissions`/`<app-signal`/`<external_codex_apps`；**`# Files pasted by the user:` 是用户粘贴，保留并标注** |
| 4 | 写 Codex 派生提取脚本并试跑 | ✅ | `tools/codex_user_prompts_extract.py`（extract/scan/keyword 三模式） |
| 5 | Codex 全量导出 | ✅ | **103 会话、882 条用户提示词** → `codex/`（每会话一文件＋`_INDEX.md`） |
| 6 | Codex 关键词兜底扫描 | ✅ | 332 命中（强弱分层：≥3 关键词 232 个已提取→`codex-related/` 1454 条；弱命中 100 个留 `source/codex-keyword-hits.txt` 待人工） |
| 7 | ZCode 侧批量导出 | ✅ | **46 会话、670 条** → `zcode/`（`tools/zcode_user_prompts_extract.py`） |
| 8 | Claude 侧导出器＋全量导出 | ✅ | **15 个 HoTT 项目目录、61 会话、685 条** → `claude/`（`tools/claude_user_prompts_extract.py`） |
| 9 | 三平台汇总总索引 | ✅ | `_总索引.md`（442 会话、3691 条；含判据备忘与四条待办） |
| 10 | 交付报告 | ✅ | GLM 会话已向研究发起人当面汇报 |

## 当前状态

**全流程完成（2026-10-16）**。遗留四条待办见 `_总索引.md`（ZCode fork 去重、Codex 弱命中复核、Claude 非 HoTT 目录兜底、更早平台不在范围）。产物在 dev 工作区未提交——入库与否由研究发起人裁定。

## 接手指引

1. 读本文件＋`source/` 下已固化的清单。
2. 参考实现：ZCode 侧 `~/.zcode/skills/zcode-gui-session-export/zcode_gui_session_export.py`（结构可直接抄）；Claude 侧参考 GLM 会话 2026-10-15 处理 012-Opus 的方法（`待你裁定-人话版/11-会话GUI转录` 的生产方式）。
3. 隐私纪律：产物只含用户消息；不改任何原始记录；本目录在 dev 工作区，将来入库由研究发起人裁定。
