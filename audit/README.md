# 审计资产入口

`user-message-disposition.jsonl`、`ai-response-ledger.jsonl`、`tool-event-ledger.jsonl`、`webgpt-section-ledger.jsonl`、`gemini-thought-ledger.jsonl`、`gemini-execution-ledger.jsonl`、`work-product-ledger.jsonl` 和 `claim-evidence-ledger.jsonl` 是本次历史整合生成的 machine-managed ledger。`ledger-summary.json` 与 `verification-report.json` 给出分母和结构校验，但不认证数学真理或 AI 理解。

生成/核验入口：

```bash
rtk python3 scripts/audit/build_history_ledgers.py
rtk python3 scripts/audit/verify_history_ledgers.py
rtk python3 scripts/audit/build_core_cognition.py
rtk python3 scripts/audit/verify_core_cognition.py
```

LocalGPT 的 raw trajectory 仅在 ignored `private-audit/`，公共 ledger 只保留完整可见回答或 bounded tool head + canonical locator；需要全文时回到 `/Users/aurolafly/codex/tools/session_trajectory.py` 和私有原件。
