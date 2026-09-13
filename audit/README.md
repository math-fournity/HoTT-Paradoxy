# 审计资产入口

`user-message-disposition.jsonl`、`ai-response-ledger.jsonl`、`tool-event-ledger.jsonl`、`webgpt-section-ledger.jsonl`、`gemini-thought-ledger.jsonl`、`gemini-execution-ledger.jsonl`、`work-product-ledger.jsonl` 和 `claim-evidence-ledger.jsonl` 是历史整合生成的 machine-managed ledger。`ledger-summary.json` 与 `verification-report.json` 给出分母和结构校验，但不认证数学真理或 AI 理解。`治理框架自反馈行为分析与未来优化依据-20260912.md` 拥有操作行为反思；`治理框架跨压缩连续性独立复审与精简升级方案-20260912.md` 是 current 分层加载方案；`核心认知generation-3与加载治理v3实施证据-20260912.md` 保存最近已封存版本，`核心认知generation-4与自反理论经济研究实施证据-20260912.md` 保存本轮 incremental core、C4、STATE/loader/C01–C10 和验证边界。旧框架对比与 generation-2 实施方案在 `history/governance-v2.1.0/`，只作历史证据。`方向追踪.md` 与 `全景视野.md` 是人读投影，不替代 ledger。

`数学结论机器证明交付门禁实施证据-20260912.md` 拥有 F-011 的 source/run/index 合同、C01–C10、正负向静态验证和历史兼容边界。它证明治理路由已实现，不证明任何数学命题，也不证明所有未来模型一定遵循。

`ERCF-1-2机器证明实施证据-20260912.md` 拥有 F-011 生效后的第一个真实数学 proof package：`MP-ERCF-001`/`C-59`–`C-66` 的形式命题、Lean 4.33.1 final indexed run、源码/输出哈希、重放结果和禁止外推。它证明一般 `Type` 值因子化骨架，不是 HoTT 原生证明或 HoTT 悖论；当前未提交，状态为 `MACHINE_PROVED_LOCAL_UNCOMMITTED`。

`ERCF-截断防御机器证明实施证据-20260912.md` 拥有首个 HoTT 原生信息经济判别：Agda 2.8.0/Cubical v0.9 的 squash-HIT `C-67`–`C-70`、官方 release asset/外置缓存哈希、五次预检谱系、final run/exact replay 和索引演进修复。结果是 `DEFENSE_WORKS`：命题截断允许 proposition consumer，并阻断逐点保真的 Bool witness extraction；不是 HoTT 悖论。

本轮新增的综合证据入口：

- `understanding-chapter-merge-manifest.json`：两个理解章节目录的逐文件 hash/diff/canonical/rollback 处置；nested 历史源不删除。
- `cross-source-reconciliation.json`：WebGPT 91 条 STATE record + LocalGPT 四类 ledger 共 22,226 条逐项 locator/register；原始 JSON 是按需审计底座，不是三件套每轮全文输入。
- `cross-source-reconciliation-report.md`：上述 register 的人读分母、映射模式和语义边界。
- `core-cognition-generation-3-transition-20260912.json`：generation-2 的 913 个旧 KC 到 generation-3 的逐项映射/退出理由，remainder=0；旧代由 `governance-v2.1.0` 恢复。
- `core-cognition-generation-4-transition-20260912.json`：generation-3 的 27 个 KC 到 generation-4 的逐项映射，27/27 为 `PRESERVED_EXACT`，remainder=0；新增 9 个单元来自 hash-pinned 当前用户原文。
- `fresh-three-way-verification-20260912.json`：新 Python 进程对 governance/research profile、三件套 EOF/hash、显式 task hydration 和 fail-closed 负向演练的收据；模型行为明确 NOT_RUN。
- `verify_projection_freshness.py`：只读核对 STATE revision、三件套 revision、core generation/hash、merge manifest、cross-source 输入 hash 和 fresh receipt。
- `core-cognition-generation-transition-20260912.json`：generation-1→2 的原文输入、前缀 identity 和回退 commit。

生成/核验入口：

```bash
rtk python3 scripts/audit/build_history_ledgers.py
rtk python3 scripts/audit/verify_history_ledgers.py
rtk python3 scripts/audit/build_core_cognition.py --transition-from-ref governance-v3.0.0  # 默认只检查当前 generation-4
rtk python3 scripts/audit/build_core_cognition.py --transition-from-ref governance-v3.0.0 --write
rtk python3 scripts/audit/verify_core_cognition.py
rtk python3 scripts/audit/verify_three_way_cognition.py
rtk python3 scripts/audit/verify_understanding_merge.py
rtk python3 scripts/audit/verify_cross_source_reconciliation.py
rtk python3 scripts/audit/verify_fresh_three_way.py
rtk python3 scripts/audit/verify_projection_freshness.py
rtk python3 scripts/audit/test_math_proof_delivery_governance.py
rtk python3 scripts/audit/verify_math_proof_delivery_governance.py
rtk python3 scripts/audit/verify_formal_proof_run.py --run-dir HoTT/verification/runs/20260912-MP-ERCF-001-02 --rerun
rtk python3 scripts/audit/verify_formal_proof_run.py --run-dir HoTT/verification/runs/20260912-MP-ERCF-TRUNC-001-01 --rerun
```

LocalGPT 的 raw trajectory 仅在 ignored `private-audit/`，公共 ledger 只保留完整可见回答或 bounded tool head + canonical locator；需要全文时回到 `/Users/aurolafly/codex/tools/session_trajectory.py` 和私有原件。
