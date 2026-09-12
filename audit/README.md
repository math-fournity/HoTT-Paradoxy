# 审计资产入口

`user-message-disposition.jsonl`、`ai-response-ledger.jsonl`、`tool-event-ledger.jsonl`、`webgpt-section-ledger.jsonl`、`gemini-thought-ledger.jsonl`、`gemini-execution-ledger.jsonl`、`work-product-ledger.jsonl` 和 `claim-evidence-ledger.jsonl` 是本次历史整合生成的 machine-managed ledger。`ledger-summary.json` 与 `verification-report.json` 给出分母和结构校验，但不认证数学真理或 AI 理解。`治理框架对比审计与核心认知增补评估-20260912.md` 拥有本轮 WebGPT/当前框架的逐维度审计；`治理框架自反馈行为分析与未来优化依据-20260912.md` 拥有本轮操作行为、框架捕获/遗漏和候选优化的反思审计；`治理框架跨压缩连续性独立复审与精简升级方案-20260912.md` 独立审计全量重放模型、量化当前 105 文档 load graph，并给出“当前启动 + 任务水合 + 历史归档”的精简目标设计；`方向追踪.md` 和 `全景视野.md` 是跨 AI 的人读投影，不替代这些原始 ledger。

本轮新增的综合证据入口：

- `understanding-chapter-merge-manifest.json`：两个理解章节目录的逐文件 hash/diff/canonical/rollback 处置；nested 历史源不删除。
- `cross-source-reconciliation.json`：WebGPT 91 条 STATE record + LocalGPT 四类 ledger 共 22,226 条逐项 locator/register；原始 JSON 是按需审计底座，不是三件套每轮全文输入。
- `cross-source-reconciliation-report.md`：上述 register 的人读分母、映射模式和语义边界。
- `fresh-three-way-verification-20260912.json`：新进程完整 load graph、三件套 EOF/hash 和 fail-closed 负向演练收据。
- `verify_projection_freshness.py`：只读核对 STATE revision、三件套 revision、core generation/hash、merge manifest、cross-source 输入 hash 和 fresh receipt。
- `core-cognition-generation-transition-20260912.json`：generation-1→2 的原文输入、前缀 identity 和回退 commit。

生成/核验入口：

```bash
rtk python3 scripts/audit/build_history_ledgers.py
rtk python3 scripts/audit/verify_history_ledgers.py
rtk python3 scripts/audit/build_core_cognition.py  # 默认沿用当前 manifest generation；显式回建旧代时再传 --generation
rtk python3 scripts/audit/verify_core_cognition.py
rtk python3 scripts/audit/verify_three_way_cognition.py
rtk python3 scripts/audit/verify_understanding_merge.py
rtk python3 scripts/audit/verify_cross_source_reconciliation.py
rtk python3 scripts/audit/verify_fresh_three_way.py
rtk python3 scripts/audit/verify_projection_freshness.py
```

LocalGPT 的 raw trajectory 仅在 ignored `private-audit/`，公共 ledger 只保留完整可见回答或 bounded tool head + canonical locator；需要全文时回到 `/Users/aurolafly/codex/tools/session_trajectory.py` 和私有原件。
