# 顶层综合 repo 适配说明

本目录的 `references/`、`templates/` 和部分业务 Skill 正文是从 WebGPT 工作目录快照收录的历史研究方法。它们的 `/mnt/data`、`workspace`、第五闭包和旧 `hott-session-governance` 路径属于当时环境的历史 locator，不是当前运行根，也不能覆盖顶层 `AGENTS.md`、`.codex/cognition/LOAD_SET.json`、`核心认知.md` 或 `.codex/research/hott/STATE.json`。

当前入口映射：

| 历史 WebGPT 角色 | 当前顶层 owner |
|---|---|
| 第五闭包/用户哲学原文 | `核心认知.md`（每次全文加载） |
| HoTT 三问 | `HoTT/HoTT研究三问-找什么-怎么找-凭什么-20260909.md` |
| 跨 Session governance | `.codex/skills/hott-local-session-governance/SKILL.md` |
| 动态状态 | `.codex/research/hott/STATE.json` |
| 加载合同 | `.codex/cognition/LOAD_SET.json`、`.codex/cognition/PROTOCOL.md` |
| canonical cognition runtime | `.codex/tools/cognition_runtime.py` |
| 历史回答/工具/产物证据 | `audit/`；LocalGPT raw 只在 ignored `private-audit/` |
| 研究知识与旧 AI 工作史 | `理解章节/`、`HoTT/`、`sources/` |

使用历史参考时，先按当前 LOAD_SET 完成全文 core 和动态状态恢复，再把历史 reference 中的叙事当作方法来源；遇到路径、版本、数量或结论冲突，保留冲突并回到当前顶层实物、Git 和 audit ledger。旧 reference 中的“第五闭包”不等于当前 `核心认知.md`，旧 AI 自述也不等于当前验证。
