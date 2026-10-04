# `dev-03` 当前 Worktree 发布快照

> **身份：** `PUBLICATION_SNAPSHOT_PREPARED / SOURCE_BRANCH_CANDIDATE / NOT_YET_PUSHED`。
>
> **目的：** 将当前 worktree `codex/zfc-observation-boundary-proof` 的项目成果完整纳入一个
> 可恢复、可审阅的 `dev-03` Git 快照，而不是只发布其既有 HEAD。

## 冻结范围

源 branch 与基线由同目录的 machine-readable
[`20261004-DEV03-WORKSPACE-SNAPSHOT.json`](20261004-DEV03-WORKSPACE-SNAPSHOT.json) 固定。
该 manifest 为每个被纳入的 tracked modification 与 nonignored untracked 文件保留路径、模式、
字节数和 SHA-256。

发布包含：

1. 当前 branch 的全部既有提交；
2. manifest 所列全部 tracked modifications；
3. manifest 所列全部 nonignored untracked 项目文件；
4. 本次冻结工具与本说明本身。

这是一份当前 worktree 的内容快照；它不从另一个 worktree 的 `dev` 或 `main` 取文件，也不
重写它们。

## `/tmp` 与运行资产边界

本轮实际 Lean 源码和 capture 脚本位于 `HoTT/formal/zfc-observation-boundary/`，运行收据位于
`HoTT/verification/runs/`。它们都在工作树内，并将进入 Git。

`/tmp/zfc_actual_witness_stdout` 和 `/tmp/zfc_actual_frontier_stdout` 只是最近一次 Lean
核验产生的 617 与 698 字节 stdout 重复副本；它们不是源码、不含唯一证据，也不作为发布输入。
保存的 canonical stdout 已位于相应 `HoTT/verification/runs/` receipt。

仓库历史快照和旧运行记录中若含 `/tmp/...` 字符串，保留其原字节作为历史证据；它们不构成
当前 code path，也不表示本次发布依赖临时目录。

## 明确不纳入的 ignored 项

当前 ignored 分母只包含 Python `__pycache__` 与 `dev-notes/.dev-notes-skill-stage/` 的私有、
提交前归档 staging 文件。二者均可重新生成或仅供尚未发送的本地归档流程使用，不是项目源码、
数学证明、来源证据或运行收据。它们在 manifest 中逐路径记录为 excluded，不能静默消失。

## 提交与推送验收

提交前必须：

1. 在独立 `dev-03` worktree 中按 manifest 比对路径与 SHA-256；
2. 审阅完整 staged diff，识别 binary、大文件、删除和历史快照；
3. 运行相称的 Lean、Python、Pattern-P 和 governance 验证；
4. 保存 `git diff --check` 的结果。若为了保持现有工作树字节而存在已知 Markdown trailing-space
   问题，必须如实写入提交收据，不能以未审阅的批量格式化改变来源；
5. 确认 `origin/dev-03` 尚未出现同名 ref 后，使用非强制 refspec 推送；
6. 用 `git ls-remote` 验证远程 OID 与本地 `dev-03` HEAD 一致。

`dev`、`main`、其它 worktree 和远程既有分支均不在本发布动作的修改范围内。
