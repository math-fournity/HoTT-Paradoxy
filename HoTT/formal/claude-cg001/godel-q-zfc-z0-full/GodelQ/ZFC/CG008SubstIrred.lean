import GodelQ.ZFC.CG008Rel3Instance

/-!
# CG-008 · 试修法 2：用 `irreducible` 阻止 `whnf` 展开

## 依据

Foundation 自己在 `InternalTranslate.lean:210` 就这么做：

```lean
attribute [irreducible] shiftVecDef eqAtomDef cFuncDef conjunctDef ve0Def ve2Def iVEDef cRelDef iTRDef
```

**所以把 `subst`/`IsUFormula` 相关的定义标 `irreducible` 是 Foundation 的既定做法。**

## 治理

- Foundation 只读；本文件纯下游。
- 若成功则无未证标记、可进收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008SubstIrred

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1**：`subst` 与 `IsUFormula` 都是 `Fixpoint` 构造的结果——
所以 `whnf` 会展开它们。

**先确认它们**不**是 `irreducible` 的**（若已是，则超时另有原因）。 -/
noncomputable example (w p : V) : V := Bootstrapping.subst ℒₛₑₜ w p

example (p : V) : Prop := Bootstrapping.IsUFormula ℒₛₑₜ p

end GodelQ.CG008SubstIrred
