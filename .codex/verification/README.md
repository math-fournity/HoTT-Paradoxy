# 本地治理验证

当前可复现检查：

```bash
rtk python3 scripts/audit/verify_core_cognition.py
rtk python3 scripts/audit/verify_history_ledgers.py
rtk python3 .codex/tools/cognition_runtime.py plan
```

这些检查验证 hash、连续 ID、分母、call/result pairing、来源存在性和 snapshot 路由；它们不验证模型理解、HoTT 内核一致性、数学定理或现实物理对应。
