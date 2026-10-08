---
paths:
  - "audit/GUI-ASSET-REAUDIT/**"
  - "认知闭包/GUI-ASSET-REAUDIT-001.md"
  - "dev-docs/GUI导出全量复算重读审计SOP.md"
  - "dev-docs/GUI导出全量复算重读审计SOP/**"
---

# GUI 导出复算：读写这些文件时适用

- 文件路径只从规范索引表、闭包 §2 和 `audit/GUI-ASSET-REAUDIT/manifest2.json` 取，不凭记忆写文件名。
- 压缩之后，先按 SOP 005 §4 执行 CL-BR2（v2 见 006），全部通过前不写入任何东西。
- 不读写 `.claude/`；不运行 `git log`、`git show`、`git blame`、`git reflog`。
- 第一战役的产物与规范在阶段 C 之前不读（SOP 001 §4）。
- 以上是上下文提示，不是强制约束；需要硬拦截的，用 PreToolUse 钩子。
- 任务结束后按 `.claude/压缩后恢复机制/拆除清单.md` 删除本文件。
