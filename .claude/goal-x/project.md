# goal-x 项目配置（HoTT 仓库）

> 由 `~/.claude/skills/goal-x/goalx.py` 的两个全局 hook 读取，改动立即生效。“prompt-reminder”一节附在每条用户消息旁；“closure”一节在会话启动、恢复、压缩后连同文件指纹列出。删除本文件即关闭本仓库的 goal-x 提醒。

## prompt-reminder
本仓库按根 `CLAUDE.md` 第一节的实用主义原则工作：以任务的认知闭包和方案为依托维护任务文档，不在 GPT 遗留的治理框架上花时间。解释用户原意前回读相关原文（`核心认知.md`、`sources/prompts/`）；数学结论交付前要有 repo 内的机器证明；Claude 不调用 Agent 工具；共享文件按需最小改动，提交按精确路径。工作单元结束时，在任务包与 `.claude/总索引.md` 各记一笔。

## closure
```goal-x-closure
# 路径 | 用途
最高指示-Claude版.md | 已随 .claude/rules 常驻；研究或审计的新理论单元、压缩或恢复后首次研究前用 Read 重读
核心认知.md | 用户原文权威；涉及用户原意或研究方向时读相关条目，跨主题时全文读
.claude/总索引.md | Claude 工作的登记入口；开工时读索引页与 002 现状段，结束时登记
```
