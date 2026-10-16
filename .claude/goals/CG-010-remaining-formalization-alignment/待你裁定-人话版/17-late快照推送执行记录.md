# 17　三客户端排查与 late-snapshot 推送执行记录

> **执行人**：GLM 会话。**指令**：研究发起人 2026-10-15——查 opencode 的工作树存储目录；整理所有与 HoTT 相关的工作树与分支并**全部推送到改名后的远端** `https://github.com/math-fournity/ZFC-Failure`。

## 一、排查结论（本轮新增排查）

- **opencode 无集中式 worktree 目录**（`~/.local/share/opencode` 与 `~/.config/opencode` 均无 worktrees 结构）；它的唯一 HoTT 工作区是 `/Volumes/D/HoTT_AI_HANDOFF_20260911-opencode/repo`——独立 clone、只读镜像（fetch 指向主 repo、push 刻意 DISABLED、main 领先官方 0 提交）。**无遗漏**。
- **`HoTT-literature-cache` / `HoTT-machine-overview-cache` 的嵌套 git**（boulier-tabareau-thesis、agda-flat、cooltt、cubicaltt、agda-guarded-forcing-ticks、coq-synthetic-incompleteness 等）：**外部上游项目的 clone，全部干净（0 本地修改）**——是依赖源码缓存，不是 HoTT 工作分支，按指令语义不推送。
- `HoTT独立答复`（无 git）、`HoTT_AI_HANDOFF_20260911.zip`（235MB 快照）：无工作树语义，记录在案。

## 二、远端改名确认与本地同步

- `ZFC-Failure` 与旧 `HoTT-Paradoxy` **同 101 分支、完全同构——确认是同一仓库改名**。
- 主 repo `origin` URL 已更新为新地址。
- fetch 时发现**远端 main 已前进**到 `7498ef49`（"留给数学社区的思考题"，本地此前没有的对象）；本地 main 已快进。

## 三、late-snapshot 执行（全部成功）

对 16 号审计判定"快照后增量"的全部工作区建 `snapshot/20261015-late-*` 分支并推送，共 **12 个**，远端回读全部在列：

| 分支 | 内容量 |
|---|---|
| late-codex-4407 / ff3b / 05ef / wflow-gui-lineage-kb / a38d | 1–10 项 |
| late-codex-bcc2 / d814 | 各 30 |
| late-codex-a329-dev02 / 3d2f-dev04 / 10c8 | 36 / 70 / 72 |
| late-machine-overview | **229 项**（见下"超限剔除"） |
| late-semantic-overview | .gitattributes（见下） |

## 四、两个超限文件的处理（如实记录）

`machine-overview` 与 `semantic-overview` 各有一个 **`archive/objects.pack`（206.95MB）**，超过 GitHub 单文件 100MB 硬限制，无法推送：

- **machine-overview**：snapshot 剔除该文件后推送其余 229 项；文件保留在磁盘 `/Volumes/D/HoTT-machine-overview/archive/objects.pack`，剔除事实写入提交信息。
- **semantic-overview**：只提交 `.gitattributes` 修改；`objects.pack` 的 staged 修改保留在磁盘（同样超限）。**如需异地保存这两个 207MB 文件，需要 GitHub LFS 或其他通道，请研究发起人裁定。**

## 五、过程中的误判修正与事故恢复（诚实记录）

1. **reaudit-testrun"快照后新增 3 个文件"撤销**：收编时发现其内容与旧 snapshot 分支（`309748468`）**逐字一致**——那 3 个文件早已保存。15 号审计 🟡-2 的新增部分撤销，只剩"其独立 repo 自身远端待核"一项。
2. **主检出短暂切到临时分支**：收编操作在主检出执行时 `git switch` 到了临时 snapshot 分支；因 cp 的文件与该分支内容完全一致，切回 dev 时被 git 自动清理——**主检出零污染**（CG-007 原有 dirty 原封未动）。空临时分支已删。教训：此类操作应在临时 worktree 做，不在主检出。

## 六、最终状态

- 远端 `ZFC-Failure`：原有 101 分支＋**12 个 late-snapshot 分支**＋`claude/012-opus-w8` 前进到 `6b371884`（本目录 14–17 号文件入库）。
- 各参与快照的 worktree 工作树已转干净（内容封板在 late 分支）。
- 未处置（待研究发起人）：两个 207MB 的 `archive/objects.pack` 的异地保存通道；magpie repo；`~/.codex` 治理仓库的 dirty；z0-full 中低残余风险（16 号）。

---

*执行记录由 GLM 会话 2026-10-15 落盘；全部推送结果可用 `git ls-remote origin | grep late` 复验。*
