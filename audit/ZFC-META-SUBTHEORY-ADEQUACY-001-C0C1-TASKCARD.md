# CoreAdequacyTaskCard — C0C1：基础理论的解释／保真／应用责任来源盘点

> **状态：** `LOCAL_LEAF_CLOSED / ADEQUACY_SOURCE_DISCOVERY / NOT_A_CORE_VERDICT`。
>
> **父合同：** `C0C`，由 [C2B successor scan](ZFC-META-SUBTHEORY-ADEQUACY-001-C2B-SUCCESSOR-SCAN.md) 触发。

## 1. 问题

不再问集合论能否表示轨迹。问题是：一手或严肃学术来源是否明确规定，基础理论 M 在支撑一个数学模型 S 的应用时，要对哪一类保真负责？本卡将四个层次分开：

```text
R1 internal derivability      : M proves/constructs S objects and theorems;
R2 semantic interpretation    : an interpretation/model preserves a mathematical structure;
R3 mathematical applicability : S is used to model a target domain;
R4 task-completion promotion  : S's FormalDone licenses OriginDone.
```

只有来源真正把 R3/R4 纳入基础责任，才可能支付本 SOP 的 `Adequacy` 字段。R1/R2 不能通过名称自动上升。

## 2. 冻结来源分母与可否证条件

| 来源族 | 准入标准 | 非准入的相似材料 |
|---|---|---|
| set-theory foundation sources | 明说 foundations 的目标、解释/建模范围，或明确限定其责任。 | 只说明对象可编码为集合。 |
| semantic interpretation / model sources | 明说 interpretation preserves what properties, and是否包括外部 task/application。 | 只给 syntax/semantics truth theorem。 |
| IEP Standard Solution source | 明说从 standard real analysis/ZFC 到 physical motion 的 application claim。 | 只给单个级数公式。 |
| philosophy of applied mathematics | 明说 mathematical model 到目标现象的 adequacy/representation condition。 | 把一般哲学术语当作 ZFC 公理。 |

**最强反证者。** 若所有来源只到 R1/R2，或明说 physical/application responsibility 在 foundation 外，则不得把 `AdequacyRequiresBridge` 加到 M；必须把它作为一个开放的规范提议并转向另一个 actual M/S/P candidate。

## 3. 本叶结束条件

至少给出一张 R1–R4 的 source matrix；每张来源卡必须标明是否达到 R3／R4。若出现 source gap，关闭的是 adequacy-source route，不是 Goal；successor scan 需在 `C0B2`（独立 formalization）和 `C3B`（actual application policy）之间选择下一项。

**实际结论。** [C0C1 result](ZFC-META-SUBTHEORY-ADEQUACY-001-C0C1-FOUNDATION-ADEQUACY-SOURCE-INVENTORY.md) 给出了 source-supported `ApplicationAdequacy` criterion，却明确排除把它写成 ZFC internal axiom；下一个 actual-P leaf见 [successor scan](ZFC-META-SUBTHEORY-ADEQUACY-001-C0C1-SUCCESSOR-SCAN.md)。
