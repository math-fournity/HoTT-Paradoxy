# CoreAdequacyTaskCard — C2B：IEP 连续运动模型与 MML `S_rich` 的 Q／FormalDone 对齐

> **状态：** `LOCAL_LEAF_CLOSED / SOURCE_TO_SPEC_FIDELITY / NOT_A_CORE_VERDICT`。
>
> **父合同：** `C2`；前叶为 [C0B1](ZFC-META-SUBTHEORY-ADEQUACY-001-C0B1-MIZAR-CONTINUOUS-MODEL-INVENTORY.md)。

## 1. 精确问题

IEP Standard Solution 的模型有 real time / position、continuous path 与 derivative-style speed。MML 已有 real-domain continuous/differentiable functions。C2B 要判断这是不是一个保真的**数学模型合同**，并严格分开它与物理／过程完成：

```text
Q_model = real-parameterized mathematical trajectory;
FormalDone = a named MML continuity/differentiability/endpoint result;
Q_physical = actual runner and physical continuum;
OriginDone = Q_physical's original completion predicate.
```

## 2. 固定输入和反证条件

| 项 | 固定值 |
|---|---|
| `M` | TG/MML 5.94.1493, as C1A. |
| `S_rich` | NFCONT_4, NCFCONT1, ORDEQ_02, INTEGR26;仅选择能够提供具体 trajectory witness或 theorem identity的部分。 |
| `Q_model` source | IEP §2，尤其 physical continuum / position function / derivative / speed 段。 |
| mandatory control | C-361 endpoint control 与 C-362 strict/revised contract，只作控制。 |
| strongest falsifier | 找不到 MML 中连续的 real-parameterized trajectory的具体 witness/theorem；或 IEP 的物理输入／完成要求不能由该 MML fragment 保真表示。 |
| prohibited conclusion | “数学连续函数存在”不等于真实运动完成、ZFC physical adequacy 或已经支付 bridge。 |

## 3. 本叶结束条件

必须完成 source-to-spec table，包含 `time / position / continuity / derivative-speed / endpoint / physical interpretation / completion` 八列。只有数学字段已付且物理／completion字段明确未付，才可称受限 fidelity；若数学 witness也不付，则标 `MODEL_MISMATCH` 并回 C0B2/C0C1。

**实际结论。** [C2B result](ZFC-META-SUBTHEORY-ADEQUACY-001-C2B-IEP-MIZAR-CONTINUOUS-QCONTRACT.md) 支付了 mathematical trajectory model，未支付 physical Q／OriginDone；下一后继见 [successor scan](ZFC-META-SUBTHEORY-ADEQUACY-001-C2B-SUCCESSOR-SCAN.md)。
