import GodelQ.ZFC.CG008SetComplete

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008HEQ

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.ZFCSetInternal

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! # hEQ：等式自反性对**带自由变量的半项**

`setTheory_sigma₁_induction'` 的 `hEQ` 要求：
`∀ n t₁ t₂, 𝗭𝗙𝗖.internalize V ⊢ (.rel Language.Eq.eq ![t₁, t₂])`，
其中 `t₁ t₂ : Semiterm V ℒₛₑₜ n`（**n 个自由变量**）。

而 `ZFCSetInternal.lean:90 set_eq_refl` 只对`Term V ℒₛₑₜ = Semiterm V ℒₛₑₜ 0` 成立。
**这一跳是构造路线的第一个具体障碍。**

已查实的零件：

* `Semiterm V ℒₛₑₜ 0` 可强制换成 `Term V ℒₛₑₜ`——闭项就是 0 自由变量的半项；
* 内部推导 `⊢` 派生自 Foundation 的 `DerivationOf`，故 `allIntro`
  （`Proof/Basic.lean:715`）可用于把自由变量逐个泛化；
* 集合论的有界量词 `lévy_ball`/`lévy_bexs` 已有
  （`SetTheory/Definability/Hierarchy.lean:39,46`）。

**治理**：本文件只记查实，不含未证标记。 -/

/-- **查实 1**：闭项就是 0 个自由变量的半项。 -/
example (t : Semiterm V ℒₛₑₜ 0) : Term V ℒₛₑₜ := t

/-- **查实 2**：`set_eq_refl` 的形状（闭项版）。 -/
example (t : Term V ℒₛₑₜ) : 𝗭𝗙𝗖.internalize V ⊢ setEq t t := set_eq_refl t

end GodelQ.CG008HEQ
