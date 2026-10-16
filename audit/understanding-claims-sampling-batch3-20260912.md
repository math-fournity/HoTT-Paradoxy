# N14(b) 审计：understanding claim 第三批（低覆盖 owner 加深）

> 文档身份：`CURRENT AUDIT EVIDENCE / BOUNDED_SAMPLE_BATCH_3 (32/2,396)`
> 日期：2026-09-12
> 触发：S059 路由的 N14(b)（第三批分层抽样）
> 抽样规则（`scripts/audit/sample_understanding_claims_batch3.py`，确定性）：按"前两批抽样比最低"的 owner 排序（比例升序、同比例按路径），取前 8 个 owner，各等距取 4 条（剔除前两批），共 32 条。

## 0. 计数与分布

| 项 | 值 |
|---|---|
| 选中 owner（抽样比） | A2 0.86%、B5 1.04%、A9 1.56%、读遍账本 1.64%、全量精读 2.26%、A4 2.56%、审计锚点 2.56%、A1 3.00% |
| 第三批样本 | 32（每 owner 4） |
| 第三批判词 | `SUPPORTED=22`、`SUPERSEDED_BY_MACHINE_RESULT=0`、`UNSUPPORTED=0`、`PENDING=10` |
| 三批累计 | 122/2,396（5.09%）：`SUPPORTED=65`、`SUPERSEDED=12`、`UNSUPPORTED=0`、`PENDING=45` |
| E6 检查 | 第三批仍未出现 natural-use chain |
| 漂移检查 | 本批全部 32 条经 `verify_claim_ledger_anchors.py` 复核，无 `DRIFTED`（漂移仅在 README/C0，见 N14(a) 报告） |

## 1. 逐条判词

| # | claim | owner/行 | 判词 | 依据/理由 |
|---|---|---|---|---|
| 1 | `CL-000323` | A2 L3 | `SUPPORTED` | 轮次路由元数据 |
| 2 | `CL-000351` | A2 L21 | `PENDING` | 解释性叙述（程序视角/不可停机类比） |
| 3 | `CL-000381` | A2 L41 | `PENDING` | 解释性对照（芝诺 vs shenchensh） |
| 4 | `CL-000410` | A2 L69 | `PENDING` | 写作 AI 的"我的理解" |
| 5 | `CL-001723` | B5 L3 | `SUPPORTED` | 历史 transform 边界横幅存在 |
| 6 | `CL-001746` | B5 L17 | `PENDING` | R039 Delay+有限预算正例：历史 `FINITE_CHECKED`，本 repo 未重放 |
| 7 | `CL-001771` | B5 L43 | `SUPPORTED` | "历史机器验证标注为 AI 自述"的状态记录与审计结果一致 |
| 8 | `CL-001795` | B5 L72 | `PENDING` | 账本内计数（20=1+3+16）；上下文依赖 |
| 9 | `CL-000883` | A9 L3 | `SUPPORTED` | 轮次路由元数据 |
| 10 | `CL-000899` | A9 L25 | `SUPPORTED` | W14 引文记录 |
| 11 | `CL-000915` | A9 L43 | `PENDING` | 评价性表述（治理层次标志） |
| 12 | `CL-000931` | A9 L63 | `SUPPORTED` | "压缩是常态、加载每轮重做"已是现行实践（三件套每轮重载） |
| 13 | `CL-002214` | 读遍账本 L3 | `SUPPORTED` | 历史读态横幅存在 |
| 14 | `CL-002260` | 读遍账本 L61 | `SUPPORTED` | 算术闭合 56−2+1=55 可核 |
| 15 | `CL-002306` | 读遍账本 L116 | `SUPPORTED` | 44 个 SESSION.md 与方案 39 的口径误差已记录 |
| 16 | `CL-002352` | 读遍账本 L140 | `SUPPORTED` | "无剩余项、aistudio-docs 永久排除"与 F-007 边界一致 |
| 17 | `CL-001947` | 全量精读 L3 | `SUPPORTED` | 制定时间记录 |
| 18 | `CL-001991` | 全量精读 L70 | `SUPPORTED` | git 走查记录（44+8 提交） |
| 19 | `CL-002035` | 全量精读 L106 | `SUPPORTED` | 7 项新细节清单存在 |
| 20 | `CL-002079` | 全量精读 L135 | `PENDING` | 计划条目（10a） |
| 21 | `CL-000529` | A4 L3 | `SUPPORTED` | 轮次路由元数据 |
| 22 | `CL-000539` | A4 L11 | `SUPPORTED` | 四层时间区分/`temporally unindexed` 由 `OUT-L-TIME-BOUNDARY`（`VERIFIED_WITH_SCOPE`）拥有 |
| 23 | `CL-000549` | A4 L27 | `SUPPORTED` | 用户逐字引文 |
| 24 | `CL-000558` | A4 L37 | `SUPPORTED` | G13 引文与用户"逻辑关系=无时序关系"的框架记录 |
| 25 | `CL-002175` | 审计锚点 L3 | `PENDING` | 口径：句级账本 2369 与本 repo 2,396 claims 不同（同 `CL-001951`） |
| 26 | `CL-002184` | 审计锚点 L13 | `SUPPORTED` | G:ALL 8 commit 记录 |
| 27 | `CL-002194` | 审计锚点 L19 | `SUPPORTED` | `reviews/SILENT-STEPS-001/PROOF_NOTE.md` 路径存在 |
| 28 | `CL-002204` | 审计锚点 L25 | `PENDING` | trajectory 链条目；本批未重核 |
| 29 | `CL-000115` | A1 L3 | `SUPPORTED` | 轮次路由元数据 |
| 30 | `CL-000140` | A1 L19 | `SUPPORTED` | 用户引文（"好好定义否定"） |
| 31 | `CL-000165` | A1 L37 | `SUPPORTED` | 用户原文（芝诺/合取前提），与 core KC-000004/20 一致 |
| 32 | `CL-000190` | A1 L67 | `PENDING` | 写作 AI 的"我的理解" |

## 2. 结论

1. 第三批 32 条无 `UNSUPPORTED`、无 `SUPERSEDED`；22 条直接 `SUPPORTED`（路由元数据、引文、可核计数、已实现实践），10 条 `PENDING` 全为解释性表述、账本内计数与计划/轨迹条目。
2. 低覆盖 owner 加深后，"待裁决"的结构与批次二一致：**待裁决的主体是表述类型**（解释、计划、轨迹指针、口径），而不是未知事实或与既有证据冲突的主张。
3. 三批累计 122/2,396（5.09%）：`SUPPORTED=65`、`SUPERSEDED=12`、`UNSUPPORTED=0`、`PENDING=45`；**E6 连续三批未出现**。

## 3. 下一步

- 证据队列常规推进：按 owner 抽样比继续加深（下一优先：A0 3.5%、A11 5.2%、A8 3.0% 等），或对 `PENDING` 中的"口径类"条目做一次性口径统一（2369 vs 2396 等）；
- 备选：ERCF-3 T3（Gödel 句，仍按 C8 停止条件 gated）。

## 4. 证据与哈希

| 工件 | 说明 |
|---|---|
| `audit/understanding-claim-sample-batch3-20260912.json` | 第三批样本（32 条，含选择表与原文节选） |
| `scripts/audit/sample_understanding_claims_batch3.py` | 低覆盖 owner 抽样脚本（确定性） |
| `audit/claim-ledger-drift-check-20260912.json` | 本批复核使用的漂移检查报告 |
| `audit/understanding-claims-sampling-20260912.md` / `...-batch2-...md` | 前两批报告（对照） |
