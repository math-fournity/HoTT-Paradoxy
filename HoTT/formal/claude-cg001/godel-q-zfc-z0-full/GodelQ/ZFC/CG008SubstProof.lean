import GodelQ.ZFC.CG008Rel3Instance

/-!
> **【本文件已作废 — 2026-10-12】**
> 其中的**诊断**（「卡在 Fixpoint 展开成本」）是**错的**。
> 真因是**循环导入**（`CG008SubstFormula` ↔ `CG008Rel3Instance`），
> 且 Foundation **已有** `IsSemiformula.subst`，**根本不必装配**。
> 更正见 `CG008Correction2.lean` 与 `CG008SubstFormula.lean`。
> 本文件仅作历史保留，**不作为结论**。
-/


/-!
# CG-008 · 装配 `subst_isUFormula`（闸门已开）

## 目标

```
IsSemitermVec L n m w → IsUFormula L p → IsUFormula L (subst L w p)
```

## 工具

- `isUFormula_subst_ISigma1.sigma1_succ_induction`（`Formula/Functions.lean:488`）；
- `hP` 由 `isUFormula_relation3`（本包，已证）给出；
- 八情形各有 `substs_*` 引理；
- `rel`/`nrel` 用 `IsSemitermVec.termSubstVec`（`:124`）。

## 治理

- Foundation 只读；本文件纯下游。
- 若成功则无未证标记、可进收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008SubstProof

open GodelQ.CG008Rel3Instance

/-! ## 装配实测：**定理语句本身**就 `whnf` 超时

闸门（`isUFormula_relation3`）**已开**，但装配仍在**第 37 行——定理的语句**上超时：

```
theorem subst_isUFormula_set {n m : V} {w : V}
    (hw : IsSemitermVec ℒₛₑₜ n m w) {p : V} (hp : IsUFormula ℒₛₑₜ p) :
    IsUFormula ℒₛₑₜ (subst ℒₛₑₜ w p) := by ...
```

**报错位置是语句行**，不是证明体。`maxHeartbeats` 提到 800000 仍超时。

**根因**：`subst` 与 `IsUFormula` 都是 `Fixpoint` 定义，
Lean 在**类型检查语句**时就要 `whnf` 展开两者以对齐类型。

**这与 `CG008RedoActual` 的 `zfcTr` 爆炸、以及本文件先前
`definability` 超时是同一族现象**——**Fixpoint 定义的类型检查成本**。

## 三条可能的修法（下一步）

1. **加 `set_option maxHeartbeats` 到更高**（如 4000000）——
   若只是慢而非发散，这就能过；
2. **把 `subst`/`IsUFormula` 标为 `irreducible`**，阻止 `whnf` 展开
   （Foundation 对 `shiftVecDef` 等正是这么做的：`attribute [irreducible] …`）；
3. **先证一条 `subst` 的等式引理**（如 `subst_eq_self`，`Functions.lean:747`），
   用它把语句**改写成不展开的形式**再证。

**第 2 条最可能成功**——Foundation 自己在 `InternalTranslate.lean:210` 就用
`attribute [irreducible] shiftVecDef eqAtomDef …` 处理同类问题。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进入收据。
- **记录的是卡点与修法，不是证明。**
-/

end GodelQ.CG008SubstProof
