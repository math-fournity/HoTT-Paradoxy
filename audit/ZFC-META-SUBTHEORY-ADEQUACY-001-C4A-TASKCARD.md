# CoreAdequacyTaskCard — C4A：IEP Standard Solution 的 bridge payment

> **状态：** `LOCAL_LEAF_CLOSED / BRIDGE_AUDIT / NOT_A_CORE_VERDICT`。
>
> **父合同：** `C4`；前叶为 [C3B](ZFC-META-SUBTHEORY-ADEQUACY-001-C3B-IEP-APPLICATION-PROMOTION-AUDIT.md)。

## 1. 固定 bridge

```text
Bridge_standard:
  FormalDone_model(S_rich) → OriginDone(Q_physical)
```

它必须分别支付：

```text
input fidelity       : runner/course ↔ mathematical state/parameter;
operation fidelity   : running ↔ trajectory operations;
observation fidelity : physical position ↔ mathematical value;
completion fidelity  : model endpoint/limit ↔ original physical completion.
```

## 2. 强制控制

| control | 目的 |
|---|---|
| `Control+` | 闭连续 real-time model可有 `t=1` 且 trajectory endpoint到达；不能把离散没有最后 stage误报为连续端点不存在。 |
| `Control−` | Norton strict/revised action completion；不能把 model outcome当作 strict last-action completion。 |
| `DifferentTaskControl` | MML formal trajectory是数学对象；physical runner是 IEP application target。 |
| `BridgePaidControl` | model-internal `τ(1)=1 → Done_model` 可以按定义成立；它必须与 physical bridge分开。 |

## 3. 最强反证者与结束条件

最强反证者是一份 Standard Solution source 明确给出 target correspondence／operation preservation／completion equivalence，或明说已改题。若没有，结论只能是 `BRIDGE_PHYSICAL_SCOPE_UNPAID`，不能把来源未写出完整论证改说成数学上的 `¬Bridge`。

本叶必须产出四字段 table和四种控制结论；之后转 C5A，使 `ApplicationAdequacy` 应用于这一具体 bridge。不得直接声称 core failure。

**实际结论。** [C4A result](ZFC-META-SUBTHEORY-ADEQUACY-001-C4A-IEP-STANDARD-SOLUTION-BRIDGE-PAYMENT.md) 发现 model-internal bridge已付、physical source-to-spec bridge未付、strict bridge由 task revision排除；C5A 后继由 [successor scan](ZFC-META-SUBTHEORY-ADEQUACY-001-C4A-SUCCESSOR-SCAN.md) 固定。
