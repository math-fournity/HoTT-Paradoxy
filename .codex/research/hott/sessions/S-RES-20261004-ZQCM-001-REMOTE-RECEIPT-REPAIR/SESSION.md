# S-RES-20261004-ZQCM-001-REMOTE-RECEIPT-REPAIR

> **角色／档位：** `MECHANICAL_EVIDENCE_REPAIR / T1 / NO_MATHEMATICAL_CLAIM`。
>
> **关联 Goal：** `ZFC-Q-CORPUS-MAP-SOP`。
>
> **分支身份：** `CANDIDATE_NOT_CURRENT`；本 session 只修复候选语料档案的处理链收据，不改写 canonical `dev` 的数学 STATE、MEMORY 或当前方向投影。
>
> **状态：** `ALL_DESIGNATED_SOURCE_READING_WORK_VERSIONS_NOW_HAVE_DIRECT_REMOTE_ATTEMPT_RECEIPTS / REMOTE_OUTPUT_NONE / SOURCE_ONLY_VISUAL_EVIDENCE_RETAINED`。

## 触发与实际动作

Goal 完成审计发现 ACQ-005、009、010、011、019、020、022已有原PDF逐页视觉和来源筛读，却缺少每份的 direct remote MinerU 收据。先读取`mineru server status --json`：MinerU 4.0.8的shared server为`running:false`、无队列。随后对七份固定主阅读PDF逐份执行`/Volumes/D/toolchain-cache/mineru-venv/bin/mineru parse --remote --json --wait 60 <PDF>`。

七次请求全部返回exit 1 / `server_not_running`；没有启动、重配或接管共享服务，也没有产生远程zip、Markdown、JSON或其他派生输出。精确命令、哈希、结果和ACQ关联在`MINERU-DERIVATIVES.md`的`MIN-REMOTE-CLOSEOUT-001`至`007`。

## 证据边界与时序

这七份PDF原有的source-only视觉审读早于本次补齐的remote失败收据，故该时间顺序偏离通常的remote-then-visual链。该偏差已写入`VISUAL-REVIEW.md`，并且没有被隐藏：由于请求没有产生任何remote输出，既有视觉条目仍只证明原PDF页图的阅读，不证明MinerU派生物，也不改变任何来源或ZFC Q结论。

本单元只完成处理链的证据补齐。它不产生新文献、新Q lead、P-DAG、数学证明或理论结论。随后必须重新跑ZQCM-001的完成审计，确认该补齐没有留下新的可处理输入。

## 重新完成审计

| Goal 要求 | 当前权威证据 | 判词 |
|---|---|---|
| 冻结范围中的 work family 有完整、替代、访问限制或排除处置 | `MANIFEST` §5.1 与 `WORK-FAMILIES.md`：15 个 family；`ACQUISITION.md`：23 条处置。 | PASS |
| 已接受的 PDF 有身份与版本证据 | `PDF-VALIDATION.md`：21 条文件／版本核验行。 | PASS |
| 每个进入来源筛选的主阅读版本有 direct-remote MinerU 收据 | `MINERU-DERIVATIVES.md`：20 个 accepted work-version 均有 `MIN-REMOTE*` 行；本单元补齐7条。 | PASS；所有remote结果为无输出失败收据。 |
| 原件页级视觉和来源筛读覆盖可得工作 | `VISUAL-REVIEW.md`、`SCREENING.md`、`ACQUISITION.md`：每个可得 work family 有固定主阅读版本与来源筛读；同一work的非主报告不会被误称为逐页读过。 | PASS，且时序修正已明示。 |
| citation、coverage、Q lead 和 remainder 都有持久 owner | `CITATION-NETWORK.md`、`COVERAGE-MAP.md`、`Q-LEADS.md`和`FINDINGS.md`均为冻结状态，`FORWARD_PENDING`仅是历史目录。 | PASS |
| 当前没有新可获取／可资格化输入 | `SEARCH-LOG.md` S-016：W-012仍403；W-014仍无机构全文；V-SET-03保持已核访问限制；新direct-successor W-015已筛读。 | PASS within frozen scope |

该表支持把当前 Goal 标记为完成：它证明的是用户指定的冻结语料已经没有需要立即处理的下一项。它不把将来的公开版本、actual-consumer来源或新的formation/payment证据排除在研究之外；这些均按`MANIFEST` §5.1重新准入。
