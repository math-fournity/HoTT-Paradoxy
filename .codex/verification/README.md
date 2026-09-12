# 本地治理验证

当前可复现检查：

```bash
rtk python3 scripts/audit/verify_core_cognition.py
rtk python3 scripts/audit/test_core_cognition.py
rtk python3 scripts/audit/verify_history_ledgers.py
rtk python3 scripts/audit/verify_three_way_cognition.py
rtk python3 .codex/tools/cognition_runtime.py plan --profile governance
rtk python3 .codex/tools/cognition_runtime.py plan --profile research
rtk python3 .codex/tools/cognition_runtime.py query --record A-AISTUDIO-COVERAGE-001
```

这些检查验证 generation-3 的精确原文/88-message disposition/913-row transition、hash、连续 ID、call/result pairing、profile/task snapshot、三件套固定顺序、历史 Session 不自动复活和方向↔成果引用；它们不验证模型理解、HoTT 内核一致性、数学定理或现实物理对应。fresh AI 行为必须另行授权并记录 model/host/version。
