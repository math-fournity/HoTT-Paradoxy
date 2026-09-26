# Claude 目标包（goal-x）

每个子目录 `CG-NNN-<slug>/` 是一个 Claude Code 长任务的目标包：`GOAL.md`（单体开工与恢复闭包）、`LAUNCH.md`（粘贴到原生 `/goal` 之后的启动条件，不超过 4000 字符）、`STATE.json` 与 `LOG.md`（只由 `goalx.py` 写入），以及可选的 `AUDIT.md`。

用 `/goal-x new <slug>` 创建，用 `/goal-x resume <ID>` 接续。机制说明见 `dev-docs/Claude-goal-x机制设计-20260924.md`；工具在 `~/.claude/skills/goal-x/`。这里的编号与 Codex 的根目录 `goal-N.md` 互不占用。
