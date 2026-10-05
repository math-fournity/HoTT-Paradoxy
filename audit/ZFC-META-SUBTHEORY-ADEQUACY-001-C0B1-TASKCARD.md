# CoreAdequacyTaskCard — C0B1：Mizar TG/MML 的连续运动子理论盘点

> **状态：** `LOCAL_LEAF_CLOSED / CANDIDATE_UNIVERSE_REFINEMENT / NOT_A_CORE_VERDICT`。
>
> **父合同：** `C0B`；触发原因是 [C3A](ZFC-META-SUBTHEORY-ADEQUACY-001-C3A-IEP-MIZAR-PROMOTION-AUDIT.md) 表明 `SERIES_1` 仅覆盖数学级数、未覆盖 IEP 的 physical continuum 模型。

## 1. 单一可否证问题

在 C1A 已固定的同一 TG/MML 分母中，是否存在版本固定的 article/theorem chain，能够实际覆盖下列至少三个 IEP field：

```text
continuous real-valued trajectory / real time parameter /
continuity or differentiability (speed proxy).
```

这不是问“能否在集合论编码路径”；也不是要求 MML 给出物理学。它只判定是否有一个更丰富、仍可精确定位的**数学 S**，以便下一轮不再用 `SERIES_1` 冒充整个 continuous-motion model。

## 2. 固定约束

| 项 | 约束 |
|---|---|
| `M` | 同 C1A：Mizar TG/MML 5.94.1493。 |
| 搜索分母 | 官方 MML current article/source pages；最多选择三条相连的 source identities。 |
| required evidence | 每条必须有 article identity、定义／theorem locator、它覆盖的 IEP field、以及未覆盖字段。 |
| strongest falsifier | 未找到一个把 real parameter、trajectory与连续／导数放进同一 formal source relation的链；或找到的对象只在 general topology／analysis 中存在但没有对应 trajectory interpretation。 |
| prohibited inference | 任何 trajectory/continuity source 都不自动支付 physical reality、OriginDone、P、Bridge 或 Adequacy。 |

## 3. 局部停止与后继

若找到符合条件的 fragment，建立 rich-S candidate 并转 C2B；若没有，关闭仅 Mizar 的 richer-S route，转 `C0C1`（adequacy source）或 `C0B2`（独立 ZF/ZFC formalization）。无论结果都不得重开 proof checker 路线或停止 Goal。

**实际结论。** [C0B1 result](ZFC-META-SUBTHEORY-ADEQUACY-001-C0B1-MIZAR-CONTINUOUS-MODEL-INVENTORY.md) 找到 `S_rich` mathematical fragment；它未付 physical interpretation，当前自动后继见 [successor scan](ZFC-META-SUBTHEORY-ADEQUACY-001-C0B1-SUCCESSOR-SCAN.md)。
