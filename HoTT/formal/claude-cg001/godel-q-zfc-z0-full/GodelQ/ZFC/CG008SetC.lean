import GodelQ.ZFC.CG008HEQGen

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008SetC

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.ZFCSetInternal

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! # 关键区分：**元层公式结构** vs **V 内公式**

`setTheory_sigma₁_induction` 归纳的是**元层**的公式结构：
    SetTheorySemiformula xi n = Semiformula ℒₛₑₜ xi n
其中 `xi` 是自由参数的类型（Foundation 里取 `xi := Empty` 也常用）。

而内部演算的 `⊢` 作用在 **V 内**的公式上：
    Formula V L = Semiformula L V 0        -- 语法/Proof/Typed.lean:140
即 `xi := V` 且 `n := 0`。

**两者连 xi 都不同**（`Empty` vs `V`）。这是一处**层面错位**，
比先记的「n > 0」更根本。

**治理**：本文件只记查实，不含未证标记。 -/

/-- **查实 1**：内部演算的承载类型是 `Semiformula L V 0`（**V 内**、无自由变量）。 -/
example : Semiformula ℒₛₑₜ V 0 = FirstOrder.Semiformula ℒₛₑₜ V 0 := rfl

/-- **查实 2**：`set_eq_refl` 给出的正是这一型。 -/
example (t : Term V ℒₛₑₜ) : 𝗭𝗙𝗖.internalize V ⊢ setEq t t := set_eq_refl t

end GodelQ.CG008SetC
