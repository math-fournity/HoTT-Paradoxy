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
# CG-008 · 试修法 2 的实施：标 `irreducible` 后装配

## 做法

先标 `subst`/`IsUFormula` 相关的定义为 `irreducible`（仿 Foundation 的
`InternalTranslate.lean:210`），再试装配。

**注意**：`irreducible` 会让 `simp`/`rw` 也不能展开，
所以装配时要用**显式的等式引理**（`substs_*` 系列）而不是 `simp`。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008SubstIrred2

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## 实测结果：`irreducible` **使情况更糟**——栈溢出

标 `irreducible` 后，编译**栈溢出**（`rc=-6`，`Stack overflow detected`）。

**所以修法 2 不成立**（至少不是直接标 `subst`/`IsUFormula`）。
`irreducible` 阻止了展开，但类型检查器仍需比较两个**未展开**的 `Fixpoint` 项，
而那个比较本身递归到溢出。

**结论**：`subst`/`IsUFormula` 的超时**不是**「展开太多」，
而是**类型检查这两个 `Fixpoint` 项的比较成本**——
`irreducible` 治不了它。

## 剩下的修法

1. **提高 `maxHeartbeats` 到很高**（如 4000000）——**未测**；
2. **改写语句**：用等式引理把 `subst` 换成**不展开的形式**——
   但 `subst` 是 `Fixpoint`，等式引理本身也要展开它；
3. **改走 `Derivable` 层**（`CG008Raw` 的通道）——那一层没有 `IsUFormula`，
   只有编码，可能绕开整个问题。

**第 3 条值得认真考虑**：`rel` 情形的目的是证 `iTR` 的 `IsUFormula`，
而 `iT_isUFormula` 最终是为了 `iT_quote` 的内部化。
**若走 `Derivable` 层，可能完全不需要 `IsUFormula`。**

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进入收据。
- **记录的是实测结果与下一步，不是证明。**
-/

end GodelQ.CG008SubstIrred2
