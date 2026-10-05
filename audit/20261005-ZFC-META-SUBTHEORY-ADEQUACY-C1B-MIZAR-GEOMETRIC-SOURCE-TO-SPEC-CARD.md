# C1B：Mizar 几何级数到芝诺标准解法的受限 source-to-spec 卡

> **身份：** `CORE_ADEQUACY_TASK_CARD / C1_C4_COMPONENT_MAPPING / SOURCE_REPORTED_FORMAL_THEOREM_UNREPLAYED / NOT_A_CORE_VERDICT`。
>
> **父方案：** `ZFC-META-SUBTHEORY-ADEQUACY-SOP`；前序：[C1A](20261005-ZFC-META-SUBTHEORY-ADEQUACY-C1A-FOUNDATION-THEOREM-CARD.md)、[C1A-2](20261005-ZFC-META-SUBTHEORY-ADEQUACY-C1A2-ISAR-ZF-REAL-CARD.md)。

## 1. 真实来源怎样在这里会合

IEP 的 Standard Solution 明说：Achilles 的非重叠子路径构成 actual infinity，但**geometric series converges**，其和是 runner 能在 constant speed 下完成的 finite distance；它还明确说明级数 (1/2+1/4+1/8+cdots) 通过 partial sums 逼近有限值来计算。IEP 同时把其所用 standard real analysis 放在 ZF-with-Choice foundation 语境中。

Mizar 的 `SERIES_1` 在其 FOTG foundation context 中给出了这条数学组件的精确定理：

```text
Th22: a ≠ 1 → Partial_Sums(a GeoSeq).n = (1 - a^(n+1))/(1-a)
Th24: |a| < 1 → a GeoSeq is summable ∧ Sum(a GeoSeq) = 1/(1-a)
```

取 (a=rac12)，再按 source 中的 scalar-partial-sum rule 缩放首项 (rac12)，得到 IEP 所举半、四分之一、八分之一……的**几何级数数学组件**。这不是新发明的数学命题；它只是把 IEP 的具体级数叙述与一个版本固定的 Mizar theorem 对齐。

## 2. source-to-spec fidelity table

| 一手来源字段 | C1B 形式／规格字段 | 已支付内容 | 仍未支付 |
|---|---|---|---|
| Mizar FOTG foundation | `M = FOTG` | 明确的 ZFC extension foundation context。 | bare ZFC exact proof replay。 |
| `SERIES_1:Th22/Th24` | `SeriesFormalDoneComponent` | 几何 partial sums 与 finite total 的 exact theorem identity。 | runner path 的连续运动语义。 |
| IEP 的 ½+¼+⅛+…／Achilles passage | `Q_component = actual-infinite subpaths, finite summed distance` | 来源确实把 geometric-series finiteness放在 Achilles Standard Solution 中。 | Q 的全部输入、trajectory、speed、time、observation 与 original Done。 |
| IEP “finite distance that Achilles can readily complete” | `P_component` | 来源有从 geometric sum 到 finite-distance runner wording 的 promotion component。 | 这一个 component 单独不等于 `FormalDone → OriginDone` bridge。 |
| Norton strict/revised completion | `BridgeStrict` | 已有来源卡表明 final-action strict bridge 未支付／task contract 被改写。 | 完整 Alternate OriginDone contract 的所有哲学解释。 |
| `ZenoLimitControl.lean` / C-361 | independent `ℝ` translation control | 本轮重放 PASS：(s_n=1-2^{-n}) 趋于 1，但不存在有限自然数 stage 已等于 1；closed real-time endpoint 有正控制。 | Lean/Mathlib 不是 Mizar/FOTG/ZFC implementation，不能替代 Mizar or IEP source payment。 |

## 3. 这张卡实际推进到哪里

```text
C1:  FOTG → MML series theorem             = source-fixed component paid
C2:  IEP Q 与上述 component 的对应          = partial, not full task fidelity
C3:  IEP P has geometric-series promotion   = source component present
C4:  Strict/OriginDone bridge                = source-unpaid / explicit task-switch control
C5:  foundation adequacy responsibility      = unsourced
C6:  core theorem                             = not released
```

因此 C1B 不是“极限理论已被重新证明正确”，也不是“ZFC 的问题已经被证明”。它把两个此前分离的事实放进同一张可审计表：**标准解法确实使用几何级数的有限和做 promotion；一个明确集合论基础上的形式化库确实有相应 theorem；但这一数学组件还没有支付原过程的 completion bridge。**

## 4. 最强反证与 controls

- **Bridge-paid control：** 若存在一份来源或形式规范逐字段证明 runner 的 actual process Done 与 formal series Done 等价，则本卡的 bridge-gap 方向必须收回。
- **Different-task control：** Norton 的 revised completion 即使数学上相容，也不自动成为 strict process completion。
- **Translation control：** C-361 的 Lean run 将“极限到达”与“某个自然数阶段到达”区分开，并给 closed-time endpoint 正例；它防止将本卡写成对连续端点的错误否定。
- **Foundation-variant control：** IsarMathLib/Isabelle-ZF real model 与 Mizar/FOTG theorem 都是真实来源，但它们不能不经说明相互替换，也不能替代 IEP 的 P。

## 5. successor scan

下一项是 `C2A-FOTG-GEOMETRIC-TASK-FIDELITY`：固定 IEP runner Q 的输入、path、speed、time、observation 与 Done，逐项问 Mizar `Th22/Th24` 所支付的 series component 覆盖何处、遗漏何处；随后只在同一合同下审计 P 和 Bridge。若 Q 不能完整映射，登记 component mismatch 并转其他候选，而不把 C1B 的系列定理外推为 core verdict。
