# CoreAdequacyTaskCard — C5A：source-backed ApplicationAdequacy contract

> **状态：** `LOCAL_LEAF_CLOSED / ADEQUACY_CONTRACT_FIXED / NOT_A_CORE_VERDICT`。
>
> **父合同：** `C5`；输入为 [C0C1](ZFC-META-SUBTHEORY-ADEQUACY-001-C0C1-FOUNDATION-ADEQUACY-SOURCE-INVENTORY.md) 与 [C4A](ZFC-META-SUBTHEORY-ADEQUACY-001-C4A-IEP-STANDARD-SOLUTION-BRIDGE-PAYMENT.md)。

## 1. 待固定的非任意 contract

```text
ApplicationAdequacy(P, Q_physical) requires:
  if P claims a mathematical model resolves Q_physical,
  then either
    (a) a completion-preserving target bridge is supplied, or
    (b) a different/revised task is explicitly declared and original resolution
        is not claimed.
```

来源角色：IEP给 actual physical application P；SEP Scientific Representation 给模型到物理 target适用性的独立责任；Norton给 explicit task-switch control。这个 contract **不**是 ZFC 公理，也不评价所有数学模型。

## 2. 成功/反证条件

| 条件 | 意义 |
|---|---|
| `BridgePaid` | 目标、操作、观察、completion relation 有 source-to-spec payment。 |
| `ExplicitTaskSwitch` | source明确改写任务，并不宣称 original Q 已解决。 |
| `AdequacyFailure` | P claims original physical resolution，同时 RequiresBridge，且无 bridge／无 task switch。 |
| strongest falsifier | a source shows P did not claim original physical resolution, or supplies bridge, or explicitly switches tasks. |

C5A 只能建立一个 **来源范围内的规范合同**。C6 才能把固定事实写成 Lean core theorem / controls；不得在此 leaf 声称 ZFC failure。

**实际结果。** C5A fixed contract 已由 C6A source-certified kernel package消费；结果与下一个 independent-formalization route见 C6A result/scan。
