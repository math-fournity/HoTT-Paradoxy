# CoreAdequacyTaskCard — C6D：actual M/S/Q/P/Bridge/Adequacy 的最终内核判词

> **状态：** `LOCAL_LEAF_CLOSED / ACTUAL_CONTRACT_FINALIZATION / CORE_VERDICT_CANDIDATE`。
>
> **父合同：** C1D/C2C/C3C/C4A/C4C/C4D/C5A/C5E；唯一 kernel package是已保存的C-369，H0由C0D1排除。

## 1. 目标命题

在下列**用户任务＋来源认证**前提下，复用 C-369：

```text
applicationClaim ∧ claimsOriginalResolution ∧ requiresBridge
∧ ¬ bridgePaid ∧ ¬ explicitTaskSwitch
→ ApplicationAdequacyFailure.
```

要在source-to-spec table中逐字段支付，而不是把“ZFC支持分析”“级数收敛”或“用户不满意”任意一项单独当作failure。

## 2. 必须运行／回读的控制

- C-369 primary positive + paid-bridge/task-switch/model-only/H0 controls；
- C-369 expected rejection control；
- C-361 continuous limit + closed endpoint positive control；
- C-370 quantized finite completion + premature-stage negative control；
- C-371 normalized completion predicate divergence + negative control；
- C0D1 SameQ_H0 exclusion；
- C0 candidate manifest、所有 source gaps/successor scans及C5E task policy。

## 3. 允许结论

若字段和控制均通过，唯一允许的强结论为：

```text
CORE_ADEQUACY_FAILURE_WITH_SCOPE
  for the user-fixed finite-stage OriginDone and the fixed IEP ZFC-founded
  Standard Solution application contract.
```

它不是 bare ZFC object-language contradiction、无法表示时间、所有连续数学错误、物理时空离散定理、或学界唯一判词。若任一字段未支付，则降级并继续C0，不允许用愿望完成。

**实际结论。** [C6D final contract](ZFC-META-SUBTHEORY-ADEQUACY-001-C6D-ACTUAL-CONTRACT-KERNEL-VERDICT.md)已将user-fixed Q与IEP source contract逐字段映入 C-369 `applicationUnpaid`，并回读C-361/C-370/C-371/C0D1 controls。因此得到的强度为`CORE_ADEQUACY_FAILURE_WITH_SCOPE`：对固定的用户 `OriginDone`、IEP ZFC-founded Standard Solution application和source-backed application adequacy criterion，FormalDone被提升为resolution却未支付user-Q bridge。它的scope与禁止外推在C6D文档中固定；下一步只剩总Gate／Git version-closure审计。
