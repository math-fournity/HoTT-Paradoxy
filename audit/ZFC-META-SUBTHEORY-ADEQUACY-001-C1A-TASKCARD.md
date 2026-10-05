# CoreAdequacyTaskCard — C1A：Mizar 的基础到几何级数链

> **状态：** `LOCAL_LEAF_CLOSED / SOURCE_ADMISSION_ONLY / NOT_A_CORE_VERDICT`。
>
> **父合同：** [`ZFC-META-SUBTHEORY-ADEQUACY-SOP`](../dev-docs/ZFC元理论子理论充分性最终闭环SOP.md) 的 `C1`；候选宇宙为 [`C0 manifest`](ZFC-META-SUBTHEORY-ADEQUACY-001-C0-CANDIDATE-MANIFEST.md) 的 `F-A × F-B`。
>
> **开卡时间：** 2026-10-05。此前的网页检索只用于定位这个候选；本卡冻结后，才允许它影响 C1 的结论。

## 1. 要检验的最小问题

标准芝诺来源已经给出一个 application-level 链：IEP 把带 Choice 的 ZF、标准实分析和 Standard Solution 放在一起；Norton 同时表明该解法改变了完成合同。C1A 不重复这一点，也不把 Mizar 的 proof checker 当作完成判词。它只问：

```text
是否存在一个版本固定的集合论基础 M，实际承载一个可定位的
几何级数／部分和 S 定理，足以作为 IEP 所说标准实分析的
可核 formalization 候选？
```

## 2. 预先冻结的候选、反证者与边界

| 字段 | C1A 的冻结值 |
|---|---|
| `M` 候选 | Mizar 8.1.15 / MML 5.94.1493（官方页面标示日期 2025-05-30）中的 Tarski–Grothendieck（TG）共同公理层。它不是 bare ZFC；本卡要求另核其是否是**来源已支付的 ZFC-founded extension**。 |
| `S` 候选 | 当前 MML 的 `SERIES_1`：`Partial_Sums`、`summable`、`Sum`，及局部名 `Th22`、`Th24` 的几何级数部分。 |
| `FormalDone` 候选 | 对 `|a| < 1`，`a GeoSeq` 可求和，且 `Sum(a GeoSeq)=1/(1-a)`；在 `a=1/2` 和常数缩放下，这是 dichotomy 的几何级数模型所需的数学结果。 |
| `Q` / `OriginDone` | 只引用既有 IEP/Norton 卡中的 Dichotomy 完成合同；本卡不自行选择 strict 或 revised `OriginDone`。 |
| `P` | IEP 的 Standard Solution／“间接解答”文字。它没有引用或消费 Mizar。 |
| `Bridge` | 预期未付：Mizar 的几何级数 theorem 不能仅凭存在就把 `FormalDone` 变成 IEP/Norton 的 `OriginDone`。 |
| `Adequacy` | 未冻结；Mizar library 的基础关系本身不等于 bare ZFC 的基础责任。 |

**最强反证者。** 若一手资料不能支付 TG 与 ZFC（含 Choice）之间的精确基础关系，C1A 只能保留为邻近控制；若它能支付这条关系，则 C1A 必须把 M 升格为一个允许的 `ZFC-founded` context，但仍要分别检验：(ii) `SERIES_1` 的此项 theorem 是否被实际用作 IEP 标准解法的来源；(iii) 该来源是否支付同一任务 bridge。后两项任一失败都不能进入 C2–C5。

**局部停止条件。** 找到或排除一个版本固定的 `M → S` 关系后关闭 C1A；不论结果怎样，都必须扫描剩余 F-A/F-B/F-C，而不能宣布整个核心目标完成。

## 3. 证据输入与禁止外推

| 输入 | 作用 | 禁止外推 |
|---|---|---|
| Mizar 官方 MML 页面、`TARSKI_0.miz`、`TARSKI_A.miz` | 固定 TG 公理层和 MML 的共同基础。 | 不将 TG 自动等同 bare ZFC 或 IEP 的 ZFC-with-Choice。 |
| `SERIES_1.miz` | 固定 S 的具体定义与 theorem identity。 | 不将外部 Mizar checker 声称升级为本机 kernel replay。 |
| IEP/Norton 已有 A2 卡 | 固定应用侧 P 和 task-switch control。 | 不将 IEP 说成引用了 Mizar，或说 Mizar 证明了运动完成。 |

本卡不创建数学命题、proof package 或 `CORE-*` claim。它是 C1 的来源准入卡。

**实际结论。** 所有字段的来源核验见 [C1A result](ZFC-META-SUBTHEORY-ADEQUACY-001-C1A-MIZAR-FOUNDATION-TO-SUBTHEORY.md)。它支付一个允许的 `ZFC-founded M → S` 片段，未支付 application promotion、Bridge 或 adequacy；后继由 [C1A successor scan](ZFC-META-SUBTHEORY-ADEQUACY-001-C1A-SUCCESSOR-SCAN.md) 固定。
