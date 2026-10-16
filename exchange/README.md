# 顶层增量交流总目录

这里承载未来从 WebGPT/其他 AI/外部工作树传回顶层 repo 的**增量**研究或审计包。每个 round 使用独立目录，必须带 base HEAD、源快照/删除清单、前后 hash、请求、研究结果、验证 receipt 和未决项；不覆盖历史 round，不把 ZIP 存在本身当作完整性证明。

当前目录只是协议入口，历史 WebGPT 的 `workspace/exchange/` 保留在 `sources/webgpt/workspace-snapshot/`。增量接收前先读 `.codex/cognition/PROTOCOL.md`、根 `AGENTS.md` 和 `sources/SOURCE_MANIFEST.json`，确认 source repo、写入授权和冲突处理。
