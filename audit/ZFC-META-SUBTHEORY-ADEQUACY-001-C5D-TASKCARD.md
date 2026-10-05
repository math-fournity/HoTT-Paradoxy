# CoreAdequacyTaskCard — C5D：completion classification bifurcation 的来源—内核控制

> **状态：** `LOCAL_LEAF_CLOSED / SOURCE_CLASSIFICATION_CONTROL / NOT_A_CORE_VERDICT`。
>
> **父合同：** C5C；冻结 IEP的“resolution”和“final step is mistaken”文本、user/C2C `OriginDone`、C-369 source-to-spec table及其已保存 Lean run。

## 1. 问题

```text
Can the fixed source facts by themselves choose between C-369's
applicationUnpaid failure case and taskSwitchControl defense case when the
user's finite-stage OriginDone is held fixed?
```

## 2. 最小形式规格

| reading | C-369 case | 可由内核检查 | 不由内核决定 |
|---|---|---|---|
| `resolution-reading` | `applicationUnpaid` | unpaid original-resolution case is failure。 | IEP的resolution是否等于user OriginDone。 |
| `task-switch-reading` | `taskSwitchControl` | explicit revised task is not failure。 | IEP是否实际放弃original Q。 |

## 3. 停止与后继

若同一来源给出唯一的 user-Q classification，则进入actual C6 route。若两个source facts并存但没有policy选择，记录`CLASSIFICATION_UNDERDETERMINED_WITH_SCOPE`，恢复F-A2为live并转C0 frontier，不能把任一control当实际bare-ZFC verdict。

**实际结论。** [C5D bifurcation card](ZFC-META-SUBTHEORY-ADEQUACY-001-C5D-COMPLETION-CLASSIFICATION-BIFURCATION.md)对已验证 C-369 的`applicationUnpaid`与`taskSwitchControl`作source-to-spec重用：同一IEP页面的resolution/final-step文本没有唯一选出任一case。故F-A2保持actual-policy classification live；C0B4/B5的独立F-B工作不撤回，C0C2保持PARKED_READY，后继为C0R4。
