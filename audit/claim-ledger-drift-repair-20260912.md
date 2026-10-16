# N14(a)：claim 账本行锚漂移的有界修复

> 文档身份：`CURRENT EVIDENCE HYGIENE / DRIFT_DETECTION_IMPLEMENTED`
> 日期：2026-09-12
> 触发：S059 打开的 `A-CLAIM-LEDGER-DRIFT-001`
> 结论：**有界修复完成**——新增只读漂移检查工具与 owner-document hash sidecar；全量检查 2,396 条 claim：`MATCH=327`、`PREFIX=550`、`CONTAINED=1490`、`DRIFTED=29`、`LINE_OUT_OF_RANGE=0`、`MISSING_FILE=0`。漂移全部集中在两份被更新过的"当前边界"文档（`理解章节/README.md` 14 条、`理解章节/C0-当前整合审计与证据边界-20260912.md` 15 条）。账本本身保持历史快照，不做静默改写；重抽取保留为显式后续决定。

## 1. 修复内容

| 工件 | 作用 |
|---|---|
| `scripts/audit/verify_claim_ledger_anchors.py` | 只读检查：逐条把 `claim_line` 的**当前**文本与账本文本比对，分类 `MATCH` / `PREFIX` / `CONTAINED` / `DRIFTED` / `LINE_OUT_OF_RANGE` / `MISSING_FILE`，并写机器可读报告 |
| `audit/claim-ledger-owner-hashes-20260912.json` | 24 份 owner 文档的 SHA-256/字节/行数/claim 数的 sidecar；未来 owner 被编辑时可通过 hash 对比发现 |
| `audit/claim-ledger-drift-check-20260912.json` | 本次检查的完整结果（含 29 条漂移样例、逐 owner 统计） |

说明：`PREFIX`/`CONTAINED` 覆盖"账本记录的是行内片段/句子片段"与"当前行包含该文本"的正常情况；只有 `DRIFTED` 表示行锚文本已不再匹配。

## 2. 检查结果

| 状态 | 条数 |
|---|---:|
| `MATCH` | 327 |
| `PREFIX` | 550 |
| `CONTAINED` | 1,490 |
| `DRIFTED` | **29** |
| `LINE_OUT_OF_RANGE` | 0 |
| `MISSING_FILE` | 0 |

漂移分布：`理解章节/README.md` 14 条、`理解章节/C0-当前整合审计与证据边界-20260912.md` 15 条——两份都是"当前索引/边界"文档，在账本建立后被改写（generation-2 → generation-3/4 与索引更新），因此行锚与文本漂移。典型样例（`drift_examples`）：

- `CL-001823`：账本为"用户授权的本次工作是…顶层初始化为新 Git repo…"，当前 C0 同一行已是重写后的段落；
- `CL-001832`：账本为"父线程纳入 core"，当前 C0 该行为"继续用于 LocalGPT 历史/trajectory 审计"。

其余 22 份 owner 文档未出现 `DRIFTED`（其被抽 claim 的文本仍在当前行内或为其前缀）。

## 3. 政策（引用规则）

1. 引用任何 claim 行（尤其来自 README/C0 的 29 条漂移项）时，**必须先核 owner 文档当前内容**，账本文本只作历史快照；
2. owner 文档被编辑后，运行 `verify_claim_ledger_anchors.py` 并对比 sidecar hash 即可机械发现漂移；
3. 全量重抽取 2,396 条 claim（含把 owner-doc hash 写入账本本身）仍是可选的后续决定；本轮只实现检测与政策，不改写历史账本。

## 4. issue 处置

`A-CLAIM-LEDGER-DRIFT-001` → **`CLOSED_WITH_SCOPE`**：漂移已定位（29 条）、检测已机械化（工具 + sidecar）、引用政策已固定；剩余（账本内嵌 hash / 全量重抽取）作为独立可选项，不阻塞当前证据队列。

## 5. 证据与哈希

| 工件 | 说明 |
|---|---|
| `scripts/audit/verify_claim_ledger_anchors.py` | 只读检查脚本（可复跑） |
| `audit/claim-ledger-owner-hashes-20260912.json` | owner hash sidecar（24 份文档） |
| `audit/claim-ledger-drift-check-20260912.json` | 本次检查报告（统计 + 29 条样例） |
| `audit/claim-evidence-ledger.jsonl` | 快照账本（未修改；sha 记录在 sidecar 的 `ledger_sha256`） |
