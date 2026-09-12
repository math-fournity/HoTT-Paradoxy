# `.codex` 本地治理入口

本目录是当前顶层 repo 的项目级 Codex 治理资产，不是全局 `~/.codex` 的替代品。先读顶层 `AGENTS.md`，再全文读 `.codex/skills/hott-local-session-governance/SKILL.md`、`.codex/cognition/LOAD_SET.json`、`.codex/cognition/PROTOCOL.md` 和动态 `STATE.json`。

三件套 invariant：每次新 Session、再次进入、跨 repo 接手和压缩恢复，都必须按固定顺序全文加载
`核心认知.md` → `方向追踪.md` → `全景视野.md`。`核心认知.md` 拥有用户原始研究意识；`方向追踪.md`
拥有跨 LocalGPT/WebGPT 的候选组合与下一判别动作；`全景视野.md` 拥有研究结果、正反例、失败和未知的
可读综合投影；三者不得互相覆盖成为“最新版”。

核心 invariant：generation-3 的 27 个用户直接原文单元由 curation+生成器管理，不手工改写；全部 record
在 STATE 全文中可见，但只有 lifecycle 给予当前任务资格，evidence review 不得自动复活历史 Session。治理任务用
governance profile，数学研究用 research profile，底层证据按 stable ID 显式水合。每轮结束仍产生当前全部
`KC-*` 回评；旧回评归档而不常驻。工具只能证明字节覆盖、引用和版本边界，不能证明模型理解或数学真理。

业务研究入口是 `.codex/skills/hott-paradox-research/SKILL.md`。历史 WebGPT `.codex` 框架在 `sources/webgpt/workspace-snapshot/.codex/`，只作为参考来源。
