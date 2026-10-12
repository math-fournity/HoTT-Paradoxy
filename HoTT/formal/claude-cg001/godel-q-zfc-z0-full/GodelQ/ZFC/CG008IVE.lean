import GodelQ.ZFC.CG008BvMain

/-!
# CG-008 · `iVE_isUFormula`——由层数版直接得出

## 本轮的结构性更正（重要）

本文件原先用 `IsUTerm.induction` 证 `IsUFormula (iVE n t)`，**假设取错了**。

`iVE n t` 的层数**确实依赖 `n`**：`func` 分支走 `ve2 (p 0) k f w`，而
`ve2` 内的 `conjunct 3 n i w.[i]` 要求 `w.[i]` 在层 `1 + n` 是公式——
这只有知道 `v.[i]` 在层 `n` 时才成立。`IsUTerm t` **不给** `v.[i]` 的层，
所以那条路上「`bv ≤ 1 + n`」这一步是**证不出来**的（先前记作最后一环的 sorry）。

**正确的假设是 `IsSemiterm ℒₒᵣ n t`**（层 `n`），结论是层 `n + 1`。
这正是 `CG008BvMain.isSemiformula_iVE` 所证的，且**严格更强**
（`IsSemiformula` 直接给 `IsUFormula` 投影）。

本文件因此缩成一条推论。原证明的三分支（`bvar`/`fvar`/`func`）与
`CG008BvMain.isSemiformula_iVE` 的三个分支逐字对应，但那里每支都
**同时**给出 `IsUFormula` 与层数——**这正是先前缺的那一半**。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008IVE
open GodelQ.ZFCArith GodelQ.Translate
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`iVE n t` 是公式**（`t` 是层 `n` 的算术项）。

**注意假设是 `IsSemiterm ℒₒᵣ n t`，不是 `IsUTerm ℒₒᵣ t`**——
见文件头部的结构性更正。 -/
theorem iVE_isUFormula {n t : V} (ht : Bootstrapping.IsSemiterm ℒₒᵣ n t) :
    Bootstrapping.IsUFormula ℒₛₑₜ (Translate.iVE n t) :=
  (GodelQ.CG008BvMain.isSemiformula_iVE ht).isUFormula

/-- **`IsUTerm` 的版本**：取 `n := termBV ℒₒᵣ t`（`IsUTerm.isSemiterm` 给的层）。 -/
theorem iVE_isUFormula_of_isUTerm {t : V} (ht : Bootstrapping.IsUTerm ℒₒᵣ t) :
    Bootstrapping.IsUFormula ℒₛₑₜ (Translate.iVE (Bootstrapping.termBV ℒₒᵣ t) t) :=
  iVE_isUFormula ht.isSemiterm

end GodelQ.CG008IVE

#print axioms GodelQ.CG008IVE.iVE_isUFormula
#print axioms GodelQ.CG008IVE.iVE_isUFormula_of_isUTerm
