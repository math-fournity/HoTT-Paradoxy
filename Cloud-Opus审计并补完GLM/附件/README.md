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

## 3. 追加（2026-09-27，Lean 重放）

| 文件 | 是什么 | 在哪里被用到 |
|---|---|---|
| `失败捕获-20260927-Lean缺Init配套文件/20260927-COPUS-REPLAY-CG001-UNIVERSE-SET-LEAN-01/`、`…-NEG-01/`（各 5 个文件） | Lean 重放的**首次捕获**，原样留档。选择性解压时漏了 `lib/lean/Init.olean.server`，两次都在读工具链文件时失败（`failed to open file … Init.olean.server`），没有走到任何证明。捕获工具的第一版还把负控制记成了"按预期被拒"，理由不对 | 工具链记录 `HoTT/formal/cloud-opus-glm-audit/LEAN_TOOLCHAIN.linux-x86_64.json` 的 `extraction_incident`；捕获工具 `tools/capture_copus_lean_run.py` 的 `classify_failure`（负控制只在目标文件本身被拒时才算数）及其单测 `tools/test_capture_copus_lean_run.py`（用这两份留档作测试输入）；补齐文件后同 ID 重新捕获的正式运行在 `HoTT/verification/runs/` |
| `工作过程文件/verify-static-终局轮-25个运行.json` | 终局轮全部 25 个 `20260927-COPUS-*` 运行的静态核验（13 通过、12 负控制按预期被拒、0 失败；核验器 sha256 `54375a03…3c86`，未改动） | `00-工作日志.md` Lean 重放条目 |

## 4. 收尾轮补记（2026-09-27）：对上一轮盘点的更正与补入

**更正**：上一轮"git 盘点"只查了会话暂存区。它对仓库外新文件的 `find` 输出被 `head -40` 截断，前 40 行全是系统文件，所以漏看了 `/tmp/claude-0/` 根目录下的过程文件和 `/tmp/claude-0/scratch/` 里的 Agda 草稿。它们大多产生于上下文压缩之前（05:49–06:40）。本轮不截断地重新扫描了整个文件系统，按下表补入，并把这次遗漏登记为审计集 004 片的偏差 #12。

| 文件（`工作过程文件/` 下） | sha256（前 16 位） | 是什么 |
|---|---|---|
| `capture_all.log` | `519b1f8968787192` | 21 个 D2 运行的捕获日志（06:24–06:40） |
| `早期摸底与开发输出/iota1.out`、`iota2.out`、`iota-art.out`、`iota-neg.out`、`stall.out`、`neg-gu.out` | `be8648228ee89c2d`、`96aec398b5a8cfeb`、`7d782c7e6d8c4c2a`、`0cbdac82c0161d86`、`2f01a030fb1771a9`、`db5abc59c0799e56` | 开工时对 GLM 六运行的非 canonical 摸底重跑（05:49）。`neg-gu.out` 就是发现 F-NEG-1（负控制死在作用域检查）的那次输出 |
| `早期摸底与开发输出/r1.out` | `073ffc42739f2c1e` | R1 名称级扫描的早期探查输出（05:49） |
| `早期摸底与开发输出/ks.out` | `96e72ec2effdabb7` | 一般 n 定理首次全量检查的输出（06:14） |
| `早期摸底与开发输出/neg.out`、`c.out` | `fc15757eb1017b12`、`9e7152bde5aefefe` | 修复负控制与负证书的开发期检查输出 |
| `早期摸底与开发输出/report.out` | `634626b267818e98` | HITScan 对全部目标的完整闭包报告（06:18，由草稿 `ReportAll.agda` 产生） |
| `HITScan开发草稿/`（11 个 `.agda`：`ScanExplore`–`ScanExplore6`、`ScanDbg`、`ScanTest`、`ScanKS`、`ScanC71`、`ReportAll`） | 见各文件 | HITScan 的开发草稿。正式版是 `HoTT/formal/cloud-opus-glm-audit/hitscan/`；草稿不是证据，保留以示开发经过 |
| `收尾轮/zeno-replays.log` | `932d2cf1dca1431a` | 芝诺线 16 个 Linux 重放的捕获日志 |
| `收尾轮/verify-static-收尾轮-41个运行.json` | `4813cfcbf09619be` | 全部 41 个 `20260927-COPUS-*` 运行的静态核验（21 通过、20 负控制按预期被拒、0 失败） |
| `收尾轮/verify-zeno-rerun.jsonl` | 见提交 | 芝诺线 16 个重放的逐字节重放核验（`tools/verify_zeno_replays.sh`） |
| `收尾轮/shards-收尾.json` | 见提交 | 收尾提交前分片校验器的输出 |

**没有入库的 Kraus–Sattler 论文副本**：一般 n 对照时读的是 arXiv:1311.4002v3 的摘要页与 ar5iv 全文（2026-09-27 06:06 下载）。该文在 arXiv 采用非独占分发许可（`arxiv.org/licenses/nonexclusive-distrib/1.0/`），只授权 arXiv 分发，所以全文副本不提交进本仓库。所读文件的身份记录如下，引用的原句位置见 `06-一般n外归纳（D3）.md` 与 `ks-universe-tower/CLAIM.md`：

| 文件 | 来源 | 字节 | sha256 |
|---|---|---|---|
| `ks-abs.html` | `https://arxiv.org/abs/1311.4002` | 46015 | `c22770f5f227f7452095ecb49183ef6fc8bd50565b105e535a24396b31345618` |
| `ks-ar5iv.html` | `https://ar5iv.labs.arxiv.org/html/1311.4002` | 330886 | `96e2d078135480f168651af8fe4117cd7ff7c9b59060f12635f1786fa312cea3` |
| `ks.txt`、`ks2.txt` | 上面 ar5iv 页面的两次文本提取 | 49746、48662 | `7c4755b048dbdc1a731d346bc928b9c07c01723e90ac7c1dbdfe1cf834c4cd2c`、`5c98d737d25830513340ac7ef4b5b754d7413507054e81c8242ab5779f305452` |

**本轮其余不入库的临时文件**：
- `cmp.tmp`：阅读副本拼接，用于逐字节比对；
- `lean_capture.sh`：捕获脚本的节选；
- `zeno_appendix.txt`：已写进社区稿 01 附录 A；
- `zeno_runs.txt`：运行清单，已写进 `tools/verify_zeno_replays.sh`；
- `shards2.json`–`shards5.json`：中间的校验输出，只收最终一份；
- `ref-0500`：用于扫描的空时间戳文件。

**会话宿主的文件**（`/tmp/claude-code*.log`、`/tmp/environment-manager*`、`/tmp/mcp-config-*.json`、`/tmp/claude-0/bash-edit-diff/`、`/home/claude/.claude/`、`/root/.claude/`、`/root/.ccr/`）是运行环境自身的日志、配置与凭据，不是本工作的产物，**绝不**提交。

## 5. 自查轮追加（2026-09-27）

| 文件（`工作过程文件/自查轮/` 下） | sha256（前 16 位） | 是什么 |
|---|---|---|
| `lean-controls-capture.log` | `067093379f2344fa` | `tools/capture_lean_controls.sh` 五个运行的捕获输出（每行一个 JSON） |
| `试跑-KernelRoute-leanchecker计时.log` | `61e49d8c3e82def8` | 正式捕获前的试跑：`KernelRoute.lean` 加 `leanchecker --fresh`（重查含 Lean 库在内的全部常量）用时 2 分 35 秒、exit 0；据此决定内核级正对照也跑 `leanchecker --fresh` |

**工具链的变化**：为了让 `import Lean` 可用，从同一本地发布包 `lean-4.34.0-linux.zip`（sha256 `5f14e0f3…`）再解出 `lib/lean/Lean/**`、`lib/lean/Lean.*`、`lib/lean/Std/**`、`lib/lean/Std.*`（`unzip -n`，不覆盖已有文件；解完重算 `lib/lean/Init` 整树哈希，未变）。新记录 `HoTT/formal/cloud-opus-glm-audit/LEAN_TOOLCHAIN_META.linux-x86_64.json` 钉住它们；二进制不入库，理由同 §2。
