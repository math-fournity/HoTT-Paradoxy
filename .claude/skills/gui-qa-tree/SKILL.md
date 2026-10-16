---
name: gui-qa-tree
description: 从 Codex rollout 导出分支子文件夹中的编号化问答文档，按分叉节点回溯，并校验逐轮标注、分支卡、综合与抽样审计。用于 GUI 导出问答树综合重读（v3）的导出、分组标注、校验与审计。
---

# GUI 问答树（gui-qa-tree）

## 何时使用

- 需要把某个 GUI 对话的谱系导出为问答文档（每轮一份），并按分支与分叉节点组织。
- 需要从一个分支的末尾倒着回溯到分叉节点，逐轮标注“这一轮 AI 在做什么”。
- 需要校验标注的覆盖、引文的逐字性、身份字段、分支卡、综合文件与抽样审计。

## 步骤

0. **开工、压缩或恢复之后，先读规范与闭包**：用 Read 读完 `dev-docs/GUI导出问答树SOP.md`（索引与 001–006 六片）和 `认知闭包/GUI-QA-TREE-001.md`，记下各片 EOF，再按闭包 §2 的恢复算法确定进度。2026-10-08 起它们不再随 CLAUDE.md 自动导入（见根 `CLAUDE.md` 第二节）。
1. 导出（仅在源变化时）：`python3 -I -B audit/GUI-SYNTH-REDO/tools/qa_tree_export.py --force`
2. 抽样（只做一次，且须在标注开始之前；2026-10-08 已完成）：`python3 -I -B audit/GUI-SYNTH-REDO/tools/check_annotations.py --stage sample`
3. 读分支：先读 `audit/GUI-SYNTH-REDO/qa/<分支>/_branch.json`（父分支与分叉节点），再从该分支的最大编号倒着读到 0001（到分叉节点即止）。
4. 标注：按 `dev-docs/GUI导出问答树SOP/003 - 阅读与标注规则（v3）.md` §6 的分组，每轮一行 JSON 写入 `audit/GUI-SYNTH-REDO/annotations/<单元>[.<部分>].jsonl`。
5. 校验：`python3 -I -B audit/GUI-SYNTH-REDO/tools/check_annotations.py --stage annotations --unit <单元> [--docs NNNN-NNNN]`；dev-08 的四部分都完成后，不带 `--docs` 再查一次。
6. 分支卡（该分支标注 PASS 之后）：写 `audit/GUI-SYNTH-REDO/cards/<分支>.md`，校验 `--stage cards --unit <分支>`。
7. 综合（所有分支卡 PASS 之后）：写 `audit/GUI-SYNTH-REDO/synthesis/` 的五个文件，校验 `--stage synthesis`。
8. 审计（由另一个会话完成）：独立标注抽样轮到 `audits/<单元>.auditor.jsonl`，然后 `--stage audit --unit <单元>`。

## 边界

- 只读 `~/.codex` 与 `~/codex-worktrees/...` 中的工具和数据；不修改它们。
- 不修改 `audit/GUI-SYNTH-REDO/qa/`；不 commit；不调用子代理（Agent 工具）。
- 不读第一战役的产物，也不读其他 worktree 的文件（见 SOP 006 §2）。
- 标注者与审计者必须是不同的会话；`model` 不得为 GLM-5.3 家族。
