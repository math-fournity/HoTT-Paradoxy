# CoreAdequacyTaskCard — C0R4：actual policy ingress frontier

> **状态：** `LOCAL_LEAF_CLOSED / SCHEDULING_REPAIR / NOT_A_CORE_VERDICT`。
>
> **父合同：** C5D successor scan；本卡补齐C5D后原应先形成的frontier decision，保留实际执行顺序与偏差。

## 1. 问题

```text
After the C5D bifurcation, which already prepared source or user-owned contract
can legitimately supply the missing actual policy classification without
pretending that a new external source has done so?
```

## 2. 实际调度事实

C0C2作为F-C candidate已经在C5D之后完成来源审计；C5E随后依据用户原任务进行classification。此卡本应在C0C2/C5E之前写入，故记录`FRONTIER_TASKCARD_ORDER_EXECUTION_DEVIATION`；不回写历史为“预先已经按卡执行”。

## 3. 裁定

外部F-C来源不能支付bare-ZFC policy；用户primary source已明确固定`OriginDone`并把IEP resolution作为被审实际P。因此选用C1D + C5E作为actual contract ingress，而不是继续扩张同形foundation source。
