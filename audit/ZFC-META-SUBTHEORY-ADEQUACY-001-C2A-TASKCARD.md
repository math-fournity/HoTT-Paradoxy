# CoreAdequacyTaskCard — C2A：IEP 几何级数与 Mizar `SERIES_1` 的 Q／FormalDone 对齐

> **状态：** `LOCAL_LEAF_CLOSED / SOURCE_TO_SPEC_FIDELITY / NOT_A_CORE_VERDICT`。
>
> **父合同：** [`ZFC-META-SUBTHEORY-ADEQUACY-SOP`](../dev-docs/ZFC元理论子理论充分性最终闭环SOP.md) 的 `C2`；前叶为 [C1A](ZFC-META-SUBTHEORY-ADEQUACY-001-C1A-MIZAR-FOUNDATION-TO-SUBTHEORY.md)。

## 1. 精确问题

IEP 现行条目把无限级数 `1/2 + 1/4 + 1/8 + …` 的 partial sums 越来越接近有限值作为 Standard Solution 的一部分；MML `SERIES_1` 对部分和、收敛和几何级数给出 formal theorem。C2A 只问这两者在哪些字段上忠实对应：

```text
Q_math      = IEP 对几何级数／partial-sum 的数学子任务；
FormalDone  = MML 中部分和收敛并给出和式的 theorem；
Q_motion    = IEP 的连续物理 runner/path/time 模型；
OriginDone  = Q_motion 的原过程完成（仍未由本卡固定）。
```

它不能预设 `Q_math = Q_motion`，更不能预设 `FormalDone → OriginDone`。

## 2. 预先冻结的字段

| 字段 | 冻结值 |
|---|---|
| `M` | C1A 固定的 Mizar TG / MML 5.94.1493 ZFC-founded extension。 |
| `S` | `SERIES_1.miz` 的 `Partial_Sums`、`summable`、`Sum`、Th10、Th22、Th24。 |
| source `Q_math` | IEP *Zeno’s Paradoxes* §2，尤其第 100–104 行关于几何级数、partial sums 逼近有限值、limits／motion definitions 的说明。 |
| candidate `FormalDone` | `0 < r` / limit formulation under MML’s sequence definitions；在 ratio `1/2` 的 geometric-series specialization中给出有限和。 |
| `DifferentTaskControl` | IEP 的 physical-continuum runner path/speed/time（第 68–88 行）和 Norton strict/revised completion card；它们必须保持为 distinct fields。 |
| `P` / `Bridge` / `Adequacy` | 本 leaf 明确不填写；C3/C4/C5 才允许。 |

## 3. 候选主张、最强反证者与本叶完成条件

**候选主张。** IEP 的级数语言和 MML 的 partial-sum/limit definitions 支持一个受限的 `Q_math ↔ FormalDone` source-to-spec mapping；它不支持整个物理 `Q_motion` 或 `OriginDone` mapping。

**最强反证者。** 若 IEP 使用的 series semantics、起点、收敛／sum 条件，或其计算对象与 `SERIES_1` 定义不相容，则这一 Mizar route 是 `MODEL_MISMATCH`，不能再进入 C3。若它们相容但只覆盖数学子任务，则必须把对应范围写清，禁止把它悄悄改名为完整 Q。

**局部停止条件。** 给出逐字段 fidelity table、至少一个 `DifferentTaskControl`、和明确的 `Q_math` / `Q_motion` 分层结论后关闭 C2A；随即做 successor scan。没有 source-to-spec mapping 的 machine proof 一律不启动。

**实际结论。** [C2A result](ZFC-META-SUBTHEORY-ADEQUACY-001-C2A-IEP-MIZAR-QCONTRACT.md) 已支付 `Q_math / FormalDone` 的有限 fidelity，并明确保留 full physical Q、P、Bridge、Adequacy 的未付状态；当前自动后继见 [C2A successor scan](ZFC-META-SUBTHEORY-ADEQUACY-001-C2A-SUCCESSOR-SCAN.md)。
