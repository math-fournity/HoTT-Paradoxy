---
archive_schema: "codex-dev-notes-agents-skill/v1"
session_id: "01a0d2f6-400b-70d2-bcd2-ad2b93f2eeae"
first_turn_id: "skill-turn-bc9754f792a843bc89f03e0ac90f2b71"
created_at: "2026-09-24T06:46:05-04:00"
project_root: "/Volumes/D/HoTT_AI_HANDOFF_20260911"
title: "我现在需要你通过充分的Claude Code官方文档的网络调研，制定一个完整的方案，把我们的Codex的项目本地的治理框架安装到我本地的C..."
source: "Codex AGENTS.md + dev-notes-archive Skill"
captured_content: "current_user_prompt,drafted_final_response"
delivery_semantics: "archived_before_final_best_effort"
---

# 我现在需要你通过充分的Claude Code官方文档的网络调研，制定一个完整的方案，把我们的Codex的项目本地的治理框架安装到我本地的C...

> 本文件由 Codex 根据 AGENTS.md 强制路由，在发送 final 前调用 dev-notes-archive Skill 写入。
> 正文保存当前用户提问和 AI 已定稿回复；它不是 Host 对已交付 UI 文本的事后收据。


<!-- conversation-archive-turn: skill-turn-bc9754f792a843bc89f03e0ac90f2b71 prompt_sha256=61b70810cc96541cf10758c36c962deda9a6f751882f1cdf93456e0c9c8d67f8 answer_sha256=6c422474365857fe8ea8372e41c5406c5d684c44ad647acd9260974fa386989b -->
## 2026-09-24 · Turn skill-turn-bc9754f792a843bc89f03e0ac90f2b71

### 用户提问

我现在需要你通过充分的Claude Code官方文档的网络调研，制定一个完整的方案，把我们的Codex的项目本地的治理框架安装到我本地的Claude Code中。注意，我没有额度，所以你无法进行实测。另外需要注意的是，我们的项目本地治理框架中很多文档的内容，其中有些内容可能存在写死成Codex用的，比如一些路径信息，所以你要一一读过才能处理好。有另外一个AI正在进行业务层的工作，但是它不会和你冲突的。

### AI 最终回复

方案已经完成并落盘。**推荐保留根 `AGENTS.md` 和 `.codex/` 作为项目唯一治理权威，再增加 Claude Code 的项目入口、设置和五个 Skill 目录链接。** 同时修正当前可执行文档里的旧宿主绑定与失效路径，完整保留历史原文、研究方法和证据要求。

完整方案在这里：**[Claude Code 项目本地治理安装方案](/Volumes/D/HoTT_AI_HANDOFF_20260911/dev-docs/Claude-Code项目本地治理安装方案-20260924.md)**。它包含五个分片：官方依据与本机基线、逐文件处置、目标布局与工作链、安装与回滚清单、验收与后续接手。

本轮完成了方案和只读取证，**尚未执行安装，也没有调用 Claude 模型进行实测**。

我先核实了本机现场：你已经安装 Claude Code **2.1.281**，已有 Claude 全局治理文件和 **17 个治理 Skill**；全局安装器对其 20 个受管文件的哈希检查仍然通过。用户设置也已经启用了 `CLAUDE.md` 与 `AGENTS.md` 同读，并禁止 `Agent`。因此，本项目接入可以复用这套全局基础，保持其他项目的配置不变。

官方文档确认了项目指令导入、项目 Skill 目录及目录符号链接等机制。方案采用这些原生入口，并把“文件被发现”“正文被读取”“模型理解并执行”“结果通过验证”分开验收。[项目指令与 AGENTS.md](https://code.claude.com/docs/en/memory)、[Skills 的位置与符号链接](https://code.claude.com/docs/en/skills)。

**逐文审阅确实发现了需要处理的内容。** 我全文审阅了 **66 份与接入有关的治理及任务文件**，包括五个项目 Skill、研究 Skill 的全部 Markdown 引用和模板、稳定合同、Goal 正文及当前启动词；另对 71 个文件做了宿主和路径检索，得到 162 条候选命中，再按语义区分。主要发现是：

- 根 `AGENTS.md` 首段仍把全局入口写成 `~/.codex/AGENTS.md`，需要改为当前宿主的全局治理入口。
- **五个可使用的模板仍指向本项目不存在的旧“第五闭包”文件**；部分引用正文还使用“三件套”及旧解包环境的操作说明。
- 研究 Skill 的旧全文重读表述，与当前 PROTOCOL 的收据复认及角色专门重读要求存在重叠，需要逐条统一，保住《最高指示》等明确的全文义务。
- checkpoint 模板没有完整展示当前 writer 要求的 `RUNS.json`、KC 审计和受管分片，不能直接当成有效 payload 使用。
- 研究 Skill 的旧 `MANIFEST.json` 声明版本为 **1.3.3**，当前正文为 **1.9.0**；其 19 个登记项中有 **7 项与现文件不符**。这份历史清单不能认证新安装，应保留其历史身份，另捕获当前安装输入。
- 旧启动词明确指定 **Astra**，还有 Codex Goal 的状态语境。它们需要保留原主体和授权；未来若让 Claude 接手，应另给精确的宿主启动说明。

每份文件的处理办法和理由都列在 **[逐文件审阅与适配处置](</Volumes/D/HoTT_AI_HANDOFF_20260911/dev-docs/Claude-Code项目本地治理安装方案-20260924/002 - 逐文件审阅与适配处置.md>)**。其中也专门说明了应保留的路径：例如项目 `.codex/` 是 canonical 地址，Agda 的绝对路径是本机工具依赖，而 Claude 归档工具使用的 `.codex/dev-notes-skill-locks/` 是有意共享的跨宿主锁；这些都不能机械替换。

拟安装结构已经具体确定：

| 载体 | 作用 |
|---|---|
| 根 `CLAUDE.md` | 导入现有 `AGENTS.md` 和 Claude 项目适配说明 |
| `docs/ai/Claude-Code项目适配.md` | 说明工具、启动、恢复、Goal、归档和验证边界 |
| `.claude/skills/` 下五个相对目录链接 | 让 Claude 原生发现五个现有项目 Skill，正文仍在 `.codex/skills/` |
| `.claude/settings.json` | 声明项目的 `Agent` 禁令，并建议在此项目关闭自动记忆，继续由 repo MEMORY/STATE 保存当前态 |
| 原 `.codex` Python 工具与证据目录 | 继续负责加载、水合、状态事务和研究证据 |

有两个机制差异已经写进完整工作链：**Claude `/goal` 会使用额外模型评价是否续行；Claude `/rewind` 也不能代替项目原子 checkpoint，尤其不能完整撤销 Bash 脚本写入。** 所以第一版不启用自动 Goal 或续行 Hook，状态保存与恢复继续使用项目现有 writer 和 canonical 收据。[Claude Goal](https://code.claude.com/docs/en/goal)、[Checkpointing 的限制](https://code.claude.com/docs/en/checkpointing)。

另外，容量需要认真验证。本轮实际生成的 research 加载计划包含 **54 个文件、2,324,782 个 UTF-8 字节**，其中 STATE 约 1.47 MB。**这些是字节数，不是 Claude token 数，也不能证明所选模型能同时保有全部必读内容。** 方案保留全文要求，T1 按现有热字段合同工作；T2/T3 的真实容量、压缩恢复和语义消费列入额度恢复后的验收，不通过删减四件套来取得表面通过。

**[分阶段安装与回滚清单](</Volumes/D/HoTT_AI_HANDOFF_20260911/dev-docs/Claude-Code项目本地治理安装方案-20260924/004 - 分阶段安装与回滚清单.md>)** 已给出实施顺序：重新核现场 → 修正活跃文档残留 → 建立项目入口与链接 → 离线验收及回滚检查 → 有额度后执行真实 Claude 行为验收。每一步都列了写入范围、判据和失败处置。

目前方案分片结构、链接与格式检查通过，审阅的 66 份源文件哈希在最终检查时未变化；[取证目录](/Volumes/D/HoTT_AI_HANDOFF_20260911/audit/claude-local-governance-20260924/README.md)保存了范围、命令和结果。另一位 AI 的业务文件、研究 STATE、现有配置和 Git 暂存区均未由本轮修改；本轮新增文件尚未提交，未执行 commit、tag 或 push。真实 Claude 的发现、完整读取、压缩恢复、角色遵循和两轮归档验证，全部明确保留为 **`NOT_VERIFIED_NO_CREDITS`**。
