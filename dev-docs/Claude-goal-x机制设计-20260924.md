# Claude Code 的 goal-x 机制与《最高指示-Claude版》设计说明

> HUMAN_EDITED；2026-09-24；Claude（Opus 5.5）编写；身份：已安装的设计，**未经新会话或真实压缩验证**。用户当天授权 Claude 为 Claude Code 自行设计机制，并要求先研究 Codex 如何把 `/goal` 任务与全局、本地治理结合。本文件是设计说明与验收记录，不是研究结论，不改变 Codex 侧任何规则。

## 1. 用户要解决的问题

用户的原话要点：Claude 会跨越压缩边界，而《最高指示.md》这类工作意识的目的，是让 AI 在每个必要的时候，包括压缩之后、回答某一类问题之前，都主动加载它、与它对齐，对抗“死犟”。用户不要复杂的治理框架（此前装过一套，已全部移除），要的是借鉴 Codex“把 `/goal` 任务变成本地治理中一种特殊 Skill”的做法，设计 Claude Code 自己的 goal-x 任务机制；可以另写一份《最高指示-Claude版.md》。同一天用户还要求打开自动压缩，并把边界设在上下文的 80%。

## 2. Codex 是怎样做的（本次研究结论）

一个 Codex 长任务由五层接起来：

1. **全局规则**（`~/.codex/AGENTS.md`）：任何工作的第一个语义动作是建立认知闭包；新会话、压缩恢复、角色变化后，先按固定链路重建再做业务判断。`GOAL_TASK_LOCAL_GOVERNANCE_V1` 规定什么任务值得打包：直接做 / 复用 / 打包 / 只准备。
2. **全局 Skill**：`repo-cognitive-closure` 负责“消费认知”（确定要知道什么、加载、在决策点检查、失效后重建）；`repo-cognition-governance` 负责“供给认知”（把新事实写回唯一 owner）。
3. **项目入口**：根 `AGENTS.md` 加 `.codex/cognition/TASK_ROUTING.md`，决定“这是哪个任务、什么角色、读哪个 Skill 和哪个 goal 文件”。
4. **任务包**：角色 Skill（执行 / 审计），单文件 `goal-N.md`（开工与恢复闭包、权限、完成门），不超过 4000 字符的启动词，以及对应的审计包。
5. **宿主 `/goal`**：把启动词粘贴在 `/goal` 之后；宿主在空闲边界继续推进，模型只有在证据支持时才能把 goal 标为完成。

**认知闭包**的意思是：为了这一次请求，影响结论的关键问题、事实、约束、来源、冲突和未知都已识别，决定性证据已真正读到，剩下的未知不会推翻结论或已让结论降级。它不是“读过一些文件”，而是任务相对的最小充分集合。它要在全过程持续维护：压缩、用户纠正、阶段变化都会让一部分失效，必须回原文重建；新认知要写回唯一 owner。Codex 的全部机制，都是为了让这个闭包在对的时刻被重建、被使用。

Codex 方案的弱点也清楚：对“压缩后重读”的保证几乎全靠文字规则，模型是否照做只能事后审计；而且它的整套路由很重，一个会话开工要读很多文件。

## 3. Claude Code 自带的能力（官方文档核实）

| 能力 | 对本设计的意义 | 来源 |
|---|---|---|
| 原生读取 `AGENTS.md` 作为项目指令；`.claude/rules/*.md` 与它并列加载，不会顶替它；项目 `CLAUDE.md` 若存在则默认只读 `CLAUDE.md` | 不新建项目 `CLAUDE.md`，Claude 专属规则放 `.claude/rules/` | [memory](https://code.claude.com/docs/en/memory) |
| 压缩后：系统提示、`CLAUDE.md`、记忆重新加载；最近修改的至多 5 个文件被重读；调用过的 Skill 正文重新注入（每个前 5,000 token，合计 25,000） | 常驻规则天然跨压缩；Skill 与 GOAL.md 把要紧内容放在前面 | [context-window](https://code.claude.com/docs/en/context-window)、[skills](https://code.claude.com/docs/en/skills) |
| `SessionStart` hook 在启动、恢复、清空、压缩后触发，输出进入上下文；`UserPromptSubmit` hook 可在每条消息旁附加上下文；官方建议写成事实陈述，不要写成“系统命令” | 回执与提醒只写事实和指针，指令本身放在用户可审阅的文件里 | [hooks](https://code.claude.com/docs/en/hooks) |
| 原生 `/goal <条件>`：每个会话一个，条件不超过 4000 字符；每轮结束由小模型只读对话判断是否达成；恢复会话时自动恢复；桌面版可用 | 续跑与完成判定交给它，goal-x 不再造续跑机制；完成条件要写成对话里看得见的证据 | [goal](https://code.claude.com/docs/en/goal) |
| Skill 可在渲染时用 `` !`命令` `` 注入当前数据；可用 `$ARGUMENTS` 传参 | goal-x Skill 调用时自动带出本会话绑定的目标状态 | [skills](https://code.claude.com/docs/en/skills) |
| `autoCompactWindow`：上下文涨到多满时触发压缩（10 万至 100 万）；Opus 4.7 及以后在 Anthropic API 上原生 100 万窗口，未设置时约在 96.7 万处压缩 | 设为 800000 即 80% 边界 | [model-config](https://code.claude.com/docs/en/model-config) |

Bash 工具的环境里有 `CLAUDE_CODE_SESSION_ID`，hook 输入里有 `session_id`，因此目标包可以按会话绑定。

## 4. 设计

**原则**：用原生能力承担“保证”，文件只承担“说明”。指令放在用户能审阅的文件里；hook 只注入事实（绑定了哪个 goal、闭包文件当前指纹、下一步）。不建语义判定 hook、不建数据库、不建常驻代理。

### 4.1 组件

| 路径 | 作用 | 为什么需要 |
|---|---|---|
| `~/.claude/settings.json` | `autoCompactEnabled: true`、`autoCompactWindow: 800000`；注册两个全局 hook | 用户要求的 80% 压缩边界；hook 是压缩后唯一能确定性注入的通道 |
| `~/.claude/CLAUDE.md` | 五条跨项目原则：认知闭包优先、压缩后重建、四层证据、长任务用 goal-x、不扩大授权 | 常驻且跨压缩；不含任何项目立场 |
| `~/.claude/skills/goal-x/SKILL.md` | goal-x 工作法：何时打包、new / resume / checkpoint / close / audit | 调用后正文跨压缩保留；渲染时带出当前目标状态 |
| `~/.claude/skills/goal-x/goalx.py` | 仅用标准库的辅助脚本：建包、绑定会话、检查点、结案、回执，以及两个 hook 入口 | 状态只经脚本写入；hook 出错时静默退出，只记日志 |
| `~/.claude/skills/goal-x/templates/` | GOAL.md（单体闭包，要紧内容在前 5,000 token）、LAUNCH.md（`/goal` 启动条件）、AUDIT.md（独立审计） | 对应 Codex 的 goal-N、启动词、审计包 |
| `最高指示-Claude版.md` | Claude 会话的操作版《最高指示》 | 见第 5 节 |
| `.claude/rules/hott-claude.md` | 本仓库的 Claude 专属规则：Codex 机制的对应做法、写入边界、goal-x 用法 | 与 AGENTS.md 并列常驻，跨压缩 |
| `.claude/rules/最高指示-Claude版.md` | 指向根目录文件的符号链接 | 让 Claude 版常驻上下文，正文只有一份 |
| `.claude/goal-x/project.md` | 本仓库开启 goal-x：每条消息附带的提醒、会话开工闭包清单 | 删除即关闭；改动立即生效 |
| `.claude/goals/` | Claude 目标包目录（`CG-NNN-<slug>/`） | 与 Codex 根目录 `goal-N.md` 编号互不占用 |

### 4.2 三条流程

**新建与开工**：`/goal-x new <slug>` 建包并填写 GOAL.md 与 LAUNCH.md；用户在新会话粘贴 `/goal <LAUNCH 全文>`；第一轮我调用 `goal-x resume <ID>`：绑定会话、打印回执、用 Read 重读闭包、写恢复说明，然后开工。每个自然单元记一次检查点。只有完成门审计表出现在对话里、并执行 `close --status COMPLETE` 之后，原生 `/goal` 的评估模型才会判定达成。

**压缩或恢复之后**：`SessionStart` hook 注入 `[goal-x 回执]`，内容包括绑定的 goal、阶段、下一步、上次检查点、压缩次数、闭包文件的当前指纹；同时把压缩次数记进 STATE 和 LOG。常驻规则和全局 CLAUDE.md 说明看到回执后先 resume、重读、写恢复说明。调用过的 goal-x Skill 正文也会被原生机制重新注入。这对应 Codex 在 issue #19910 中发现的问题：压缩后模型把局部任务完成误当成整个 goal 完成。回执明确写着“局部任务完成不等于 goal 完成”。

**回答某一类问题之前**：`UserPromptSubmit` hook 在每条消息旁附一行本仓库约定（约 200 字），提示在回答涉及用户悖论观、数学哲学、原意、HoTT 理论分析、研究方向取舍的问题前先回读 KC 与扩展认知，并按《最高指示-Claude版》工作。是否适用由我判断；hook 不做语义判断。

### 4.3 与 Codex 的对应

| Codex | Claude |
|---|---|
| 全局 AGENTS 加 `repo-cognitive-closure` | `~/.claude/CLAUDE.md` 加 goal-x Skill 的 resume 流程 |
| TASK_ROUTING 加角色 Skill | 仍读 TASK_ROUTING 原文；Claude 的专属规则在 `.claude/rules/` |
| `goal-N.md` 单体闭包 | `.claude/goals/CG-NNN-*/GOAL.md` |
| 不超过 4000 字的 `/goal` 启动词 | `LAUNCH.md`，粘贴给原生 `/goal`（同样 4000 字符上限） |
| 靠规则要求压缩后重读 | `SessionStart` hook 回执、常驻规则、Skill 自动重新注入，三者叠加 |
| checkpoint 事务加 STATE | 本仓库研究 STATE 仍归当前 integrator；goal-x 只管 Claude 自己的 STATE.json 与 LOG.md |

## 5. 《最高指示-Claude版》

原版第七稿 83,629 字节、503 行，为 Astra 写成，要求每个理论单元全文重读，并答 14 题、做三次重新呈现。Claude 版 202 行，约 1.96 万字节，变化如下：

- **保留**：两段用户原话（程序从原版逐字提取，已核对字节一致）、找茬姿态、先发现后核证、种子句、五盏探照灯、现实对齐、多约束求解、A/B 方向、多尺度、X_i 与 X_h 分层、核证约束、F-011、角色化使用、两类真实偏差。
- **新增**：开头列出 Opus 自己最可能的五种“死犟”，并配一张“第一反应→先做什么”的触发表。
- **压缩**：14 题和三次呈现压成五项可见检查加一次人话重讲；24 维审计只在正式交付时用，日常压成两项自检。
- **加载方式**：经 `.claude/rules/` 常驻，压缩后自动回来；在新理论单元、压缩后首次研究、回答原意类问题之前用 Read 重读（已实测 Read 对未改动的文件仍返回全文）。

冲突时以原版和《核心认知.md》为准。

## 6. 刻意不做的事

- 不新建项目 `CLAUDE.md`：它会让 Claude 默认不再读 AGENTS.md。
- 不改 AGENTS.md、rulings.md、README、dev-docs/README.md：它们有其他会话尚未提交的修改。登记待这些修改提交后再做，或由用户决定。
- 不写研究 STATE、MEMORY、四件套：当前研究 integrator 是 Codex Session C。
- 不做续跑用的 Stop hook：原生 `/goal` 已提供。
- 不做关键词触发的语义 hook、不建数据库、不装常驻代理。
- 不把 `.codex/skills` 链接进 `.claude/skills`：它们是 Codex 角色的工作法，Claude 需要时直接 Read。

## 7. 验证记录

已验证（2026-09-24，本会话）：
- `goalx.py` 在临时仓库中跑通 new、编号递增、排他创建、bind、status、checkpoint、context、close，以及结案后不再出现在回执中。
- 两个 hook 入口在未开启的仓库输出 0 字节；输入坏 JSON 时以 0 退出并记日志；单次约 70 毫秒。
- 在本仓库模拟 startup、compact、UserPromptSubmit 三种输入，输出分别为 533、533、205 字符，闭包指纹正确。
- `~/.claude/settings.json` 经 `jq` 校验；两段用户原话与原版逐字节一致，1.2 段与 KC-000048 一致。

- `UserPromptSubmit` hook 在安装会话里实际触发：设置热加载后，用户的下一条消息旁出现了 `[goal-x] 本仓库约定……` 的提醒。
- 第一个目标包 `.claude/goals/CG-001-targeted-overview/` 已写好：启动文字 1,349 字符；必要内容块约 3,700 字符；9 个闭包文件都存在。

**未验证**：
- 桌面版在**新会话**里是否实际触发 `SessionStart` hook 并注入回执。
- 真实压缩后回执是否出现、我是否照做。
- 新建的 `~/.claude/skills/` 目录要在重启后才会被识别，所以 `/goal-x` 要到新会话才能调用。
- 自动压缩设置是否已对本会话生效（按文档，用户设置会热加载，但未实测）。

这些要在下一个新会话里看：开头是否出现 `[goal-x 回执]`，`/goal-x status` 能否调用。

## 8. 回滚

删除以下新增项即可完全撤回，不影响 Codex 侧任何文件：
- `~/.claude/CLAUDE.md`
- `~/.claude/skills/goal-x/`
- `~/.claude/settings.json` 中的 `hooks` 一节（压缩设置可单独保留）
- `最高指示-Claude版.md`
- `.claude/`
- 本文件

只想关闭本仓库的提醒和开工闭包，删除 `.claude/goal-x/project.md` 即可。
