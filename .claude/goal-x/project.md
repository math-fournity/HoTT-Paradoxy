# goal-x 项目配置（HoTT 仓库）

> 由 `~/.claude/skills/goal-x/goalx.py` 的两个全局 hook 读取，改动立即生效。“prompt-reminder”一节附在每条用户消息旁；“closure”一节在会话启动、恢复、压缩后连同文件指纹列出。删除本文件即关闭本仓库的 goal-x 提醒。

## prompt-reminder
本仓库约定：回答涉及用户悖论观、数学哲学、原意解释、HoTT 理论分析或研究方向取舍的问题之前，先回读相关 KC 原文与扩展认知分片，并按《最高指示-Claude版》工作（研究时先发现后核证）；数学结论须过 F-011 机器证明门禁；Claude 不调用 Agent 工具；研究 STATE、MEMORY、方向追踪、全景视野由当前研究 integrator 维护，Claude 未获授权不写。Claude 的全部工作、思考与发现登记在 `.claude/总索引.md`：先落盘再登记，每个工作单元结束时按其 001 §3 维护。

## closure
```goal-x-closure
# 路径 | 用途
最高指示-Claude版.md | 已随 .claude/rules 常驻；研究或审计的新理论单元、压缩或恢复后首次研究前用 Read 重读
.codex/cognition/TASK_ROUTING.md | 确定任务与角色
MEMORY/001 - 当前执行队列.md | 当前队列与研究 integrator 身份
核心认知.md | 涉及用户原意、方向判断或研究时全文读（研究还需按 AGENTS.md 读完四件套）
.claude/总索引.md | Claude 全部工作、思考与发现的入口；做 Claude 线的工作前读全文（索引 + 001–005），结束时按 001 §3 维护
```
