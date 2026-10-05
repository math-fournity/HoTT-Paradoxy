# dev-09：当前 `dev` 工作树的远端保存快照

> **目的：** 将研究发起人指定的当前 Git worktree 工作，包括未提交的对话记录文件，保存到独立远端分支 `dev-09`。
>
> **创建基线：** 本地 `dev` HEAD `bda342e6efe054beffc7c83e8eec5c920649ddd3`；该 HEAD 包含本地已提交、但当时尚未推送的 `archive: record dev notes`。
>
> **远端基线：** `origin/dev` = `0131bc6b68927b80b4de2a2cea129c4c7dd59906`。

## 纳入的未提交增量

| 路径 | 字节 | SHA-256 | 身份 |
|---|---:|---|---|
| `dev-notes/0109 - 2026-10-02 - ZFC最大的问题，肯定在于对“时间维度”的把握上.md` | 561987 | `be4957b173c4706301cedcf06f512e2e1470f079f2f976d2a4f01bd1d32c3843` | tracked modification，逐字保留，包括已有尾随空白。 |
| `git-worktree对话录/dev-01 - 20261004T194848Z-01a1083d-3515-7403-9b43-a5e02d8fc2d5-3647494d3660-gui.md` | 1401246 | `f0ec8bf505859fa20164be07d4cc0514182bf85210d1245f6f9aa9fa52b99f5e` | untracked dialogue record。 |
| `git-worktree对话录/dev-02 - 20261004T101101Z-01a10533-7f5c-79b2-8d00-a5d797205ee5-b04cf56b8548-gui.md` | 1261065 | `f57baad95286b0d179654bc30b918f2a78122a170612946c19d0828c410ffaa7` | untracked dialogue record。 |
| `git-worktree对话录/dev-03 - 20261004T103128Z-01a1039a-331b-7c92-acdc-38841283cac8-4ccfd58f1aa3-gui.md` | 1228974 | `266186561316e3ab99668439da6f2496d106426059d1b49d8ccddacc2040bebe` | untracked dialogue record。 |
| `git-worktree对话录/dev-04 - 20261004T102801Z-01a10533-f07b-7d21-ada8-cd136ce61dd5-9c791ac1226d-gui.md` | 1250398 | `506f28eda4574b50b8945ce1b030a53318af990af4ca23efdf5d0722762d8706` | untracked dialogue record。 |
| `git-worktree对话录/dev-06 - 20261004T160420Z-01a106f7-75c0-7dd0-b135-63d0393bd6cf-cd2523908155-gui.md` | 1367236 | `49652da00c783b548cc1bb8cab14a176e6f29be93f395628349196b60f6401d1` | untracked dialogue record。 |
| `git-worktree对话录/dev-07 - 20261004T162033Z-01a10700-dd83-7171-8601-127270b94e9e-a573664c5370-gui.md` | 1339447 | `6578cc852691d5d5350ca0d1e2ac25ab6b8c500df18819f61432fb65531f5614` | untracked dialogue record。 |

## 明确排除

本快照不纳入 `.gitignore` 排除的编译缓存和运行副产物，例如 `.agdai`、`__pycache__`、`.DS_Store`、`.pytest_cache`；也不纳入被项目 AGENTS 明确界定为嵌套历史 repo、非当前工作根的 `AI对话录/` 与 `workspace/`。这些排除项不属于本次 `git status --porcelain=v1 --untracked-files=all` 所呈现的当前可审阅工作树增量。

## 保存方式与验证

1. 从 `bda342e6` 创建独立 branch/worktree `dev-09`，不切换或清理原 `dev` 工作树；
2. 对 tracked diff 使用 Git binary patch 应用到 snapshot worktree；
3. 对 `git-worktree对话录/` 复制原始非忽略文件；
4. 在提交后以 Git blob SHA-256 与本表逐项比对；
5. 只用非 force `git push origin dev-09` 创建远端分支。
