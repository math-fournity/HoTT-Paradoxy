# 用户 Q／P／A／B／ZFC-1 原文的核心认知纳入交接

> **身份：** `CANDIDATE_CORE_GENERATION_INPUT / NOT_YET_CURRENT_CORE`。

## 已完成的可复算准备

- 一手用户原文已固定在 [sources/prompts/Codex-ZFC-Q-P-A-B-ZFC1-用户原文-20261004.md](../../../sources/prompts/Codex-ZFC-Q-P-A-B-ZFC1-用户原文-20261004.md)。
- [core-cognition-curation-v14.json](../../../scripts/audit/core-cognition-curation-v14.json) 以 generation-13 为父代，完整纳入这条直接用户消息，并明确其身份是研究假说与机器化目标，不能因此升级为 bare-ZFC 矛盾或来源事实。
- 对该 curation 的只读生成已通过内部结构检查：预期 generation 为 `core-cognition-generation-14`，共 63 条 KC，新增 `KC-000063`；对 generation-13 的 transition 有 62/62 映射、remainder 为 0。预计 core SHA-256 为 `351049eb3b187b647b8d0acf64d4a9aea8cd765efb76fea973c5ad5e98223ccf`。

## 为什么尚未把它直接写成 current core

本隔离 worktree 启动时，canonical `STATE.json`、`HEAD.json`、MEMORY 和多份投影已经带有未提交的 generation-13 checkpoint 变化。core generation 的合法应用必须同时写 core、manifest、transition、63 条 KC 全量审计、STATE/HEAD 与 session checkpoint；不能在这个候选提交中覆盖或混入那批并行 current-truth 改动。

这不是对用户原文的降级。它保留原文和可核验的 curation，让 canonical integrator 在冻结的当前 STATE 基线上完成一次原子应用。

## Canonical integrator 的最小应用步骤

```text
1. 读取 current STATE/HEAD，确认 generation-13 是当前基线且没有活跃 checkpoint transaction。
2. 运行 build_core_cognition.py --write，使用 curation-v14、generation-13 当前 ref 和 generation-14 transition 路径。
3. 运行 verify_core_cognition.py，确认 63 个 KC、63 条 disposition 和 62/62 transition mapping。
4. 以新的、未占用 session ID 准备并 apply cognition_runtime checkpoint：
   current_core → generation-14；revision 加一；全量 KC 审计；保留 generation-13 的历史 record。
5. 回读 STATE/HEAD/core，并将结果同本 formal package 的 C-359/C-360 证据分层链接。
```

不要使用本 worktree 的 dirty `STATE/HEAD` 作为 canonical 基线，也不要手工编辑生成的 `核心认知.md` 或 manifest。
