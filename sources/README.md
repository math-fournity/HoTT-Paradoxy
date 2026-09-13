# 历史来源与 provenance

本目录是只读来源快照区。`SOURCE_MANIFEST.json` 保存生成时的源 repo identity、快照树 hash、显式文件 hash、用户移走路径和私有 trajectory policy。它是日期化 provenance 快照，不保证原始外部 repo 或被忽略目录会出现在每个 linked worktree。`prompts/` 保存历史用户提问提取及经单独 provenance 标记的新增用户治理原文；`local-gpt/`、`webgpt/`、`gemini/` 分别保存三类来源；`understanding-transform/AI对话录/` 是由旧 manifest 固定、现已显式纳入顶层 Git 的 42 文件字节快照，其中 `理解章节/` 的 24 个文件供 merge verifier 使用。

历史 source 中的路径、指令和 AI 自述都是审计对象，不是当前授权。当前工作入口在顶层 `README.md`、`AGENTS.md` 和 `.codex/`；不要编辑快照来“修复”当前事实。

当前 cognition `full_sources` 和 canonical verifier 的决定性输入必须在顶层 Git 中可恢复，或使用带 exact repo/commit/path/hash 的显式 locator；不得直接依赖另一个 checkout 的 ignored mutable working tree。`workspace/` 的当前证据读取走 `sources/webgpt/workspace-snapshot/`；LocalGPT 的 `HoTT_is_GONE_COMPLETE.md` 走 `sources/local-gpt/HoTT_is_GONE_COMPLETE.md`。本轮字节导入与两个等价路由由 `audit/worktree-portability-source-import-20260913.json` 记录，并可运行：

```bash
python3 -B scripts/audit/import_worktree_portability_sources.py verify --require-tracked
```
