# 附件说明

> 2026-09-27；Cloud-Opus 审计会话。用户要求"你的所有工作的所有涉及到的文档和代码必须确保进入了repo目录并被git追踪"。本目录收存交付正文之外、但在工作中实际产生或使用过的文件：原样复制，逐字节核对过，下表给 sha256。它们是过程记录，证据身份以正文与运行收据为准。

## 1. 收存的文件

| 文件 | sha256（前 16 位） | 字节 | 是什么 | 在哪里被用到 |
|---|---|---|---|---|
| `11-首轮核验结果（IOTA-SYNTAX-01不一致）.json` | `a81967ea7d19eec0` | 36463 | 第一轮逐字节重放核验的完整结果（20/21 一致） | `01` §5；`00-工作日志.md` 06:48–07:05 条；审计集 004 片偏差 #3 |
| `首次捕获-20260927-COPUS-REPLAY-GLM-IOTA-SYNTAX-01/`（5 个文件） | stdout `ffcfb0f695eb189c` | — | 该运行的首次捕获：新建 XDG 数据目录后的第一次调用，stdout 多出 19 行内建模块检查 | 同上 |
| `20260926-Session问答原文存档（用户上传，GLM-Auditor会话）.md` | `9e55cc48ad7c66ae` | 61597 | 用户在本会话上传的 GLM-Auditor 会话问答存档（504 行；由 GLM-5.3-Flash 按用户要求整理，用户从 TUI 复制），原上传文件名 `e66deea1-20260926-Session______.md` | `12-GLM-Auditor认知评审（人话版）.md` 的输入；`00-工作日志.md`"GLM-Auditor 认知评审"条 |
| `工作过程文件/verify-static.json` | `eb92328092da9d8b` | 37528 | 首次静态核验输出（06:48）：多出的 postulate 子串检查把注释误判为违规 | 审计集 004 片偏差 #2 |
| `工作过程文件/verify-static-final.json` | `835c6122d07de69f` | 37525 | 修正后的最终静态核验输出（07:25），21/21 通过 | 同上 |
| `工作过程文件/verify-rerun.log` | `40c611ac1b02e88a` | 2058 | 第一轮 `--rerun` 核验的终端日志 | 偏差 #3 |
| `工作过程文件/verify-rerun2.log` | `14d1e0c0b0ff8e4d` | 2098 | 第二轮 `--rerun` 核验的终端日志（21/21 逐字节一致） | `11-收据核验结果.json` 的同轮日志 |
| `工作过程文件/iota01-now.stdout` | `b3f1585af179b8a6` | 9356 | 诊断 IOTA-SYNTAX-01 不一致时的现场重跑输出，用来与首次捕获做 diff | 偏差 #3 |
| `工作过程文件/push.log` | `5cc288bed8714ee6` | 235 | 第二次推送（`14b92d18..d16cd81c`）的输出 | 推送留痕 |
| `工作过程文件/shards.json` | `40bb92f350f4b797` | 3050 | 终局轮提交前分片校验器的输出（PASS） | `00-工作日志.md` 终局轮条目 |
| `工作过程文件/unfold-check/CatalogOfSetsTwoSteps.agda` | `60e86487cd19b3fc` | 572 | 暂存区里最初的一行检查（KS 5.10 在 n = 0 展开为"装集合的目录是群胚、不是集合"） | 已入库为正式证明包 `HoTT/formal/cloud-opus-glm-audit/ks-universe-tower/CatalogOfSetsTwoSteps.agda`（COPUS-KS-C06，运行 `20260927-COPUS-KS-CATALOG-OF-SETS-01`）；这里保留原件 |
| `工作过程文件/unfold-check/out.txt` | `ee85074bb87b5f819` | 311 | 上面那次暂存区检查的输出（exit 0） | 同上 |

## 2. 没有收存的东西，以及理由

| 东西 | 理由 |
|---|---|
| 暂存区的 `dir.md`、`pan.md`、`ec-008-009.md` | 读四件套时拼接的阅读副本，已核对与仓库中 `方向追踪`、`全景视野`、`扩展认知` 008–009 的拼接**逐字节相同** |
| 暂存区的 `pan-b.md`、`pan-c.md`、`pan-d.md` | 全景视野的行摘录，已核对每一行都在仓库原文中 |
| 暂存区的 `commit1.txt`–`commit3.txt` | 提交信息草稿，与提交 `0845a2dc`、`14b92d18`、`f8488038` 的提交信息相同（只差末尾一个空行） |
| 暂存区 `unfold-check/KSUniverseTower.agda` | 仓库文件的副本，sha256 相同（`a2ad0fc6…a202`） |
| 各证明目录下的 `*.agdai`、`tools/__pycache__/` | Agda 与 Python 自动生成的缓存，已被 `.gitignore` 排除；可随时由源码重建 |
| `/home/user/toolchain/`（Agda 二进制与发布包、cubical 库、XDG 缓存） | 第三方发布物，不是本工作的文档或代码。来源 URL、字节数与 sha256 记录在 `HoTT/formal/cloud-opus-glm-audit/TOOLCHAIN.linux-x86_64.json`，复现方法见 `01` §4；若需要把二进制本身也纳入版本管理，建议用 Git LFS 或发布附件，而不是普通提交 |
| 会话宿主的日志与配置（`/root/.cache`、`/root/.claude*`、`/etc` 下的文件） | 运行环境自身的文件，不是本工作的产物 |
