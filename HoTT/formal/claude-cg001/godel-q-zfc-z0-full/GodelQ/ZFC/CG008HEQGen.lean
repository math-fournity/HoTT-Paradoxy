import GodelQ.ZFC.CG008HEQ

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008HEQGen

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.ZFCSetInternal

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! # 查实：`⊢` 只对**闭句**有定义——`hEQ` 的自由变量障碍的确切来源

`Syntax/Classical/Formula.lean:38`：
    abbrev Formula (L : Language) (xi : Type*) := Semiformula L xi 0

`Syntax/Proof/Typed.lean:140`：
    instance : Entailment (InternalTheory V L) (Formula V L)

**所以 `T.internalize V ⊢` 只接受 `Semiformula V L 0`**，
对 `Semiformula V L n`（n > 0）连**类型类实例都没有**。

这意味着 `setTheory_sigma₁_induction'` 的 `hEQ`（要对 `Semiterm V ℒₛₑₜ n` 给推导）
**不能直接喂给 `⊢`**——必须先把带自由变量的公式**全称闭包**成闭句，
或用 Foundation 的 `DerivationOf`/`TDerivation` 层（那层的 `Sequent V L` 带公式集，
可以承载带自由变量的上下文）。

**治理**：本文件只记查实，不含未证标记。 -/

/-- **查实 1**：`Formula L xi` 就是 `Semiformula L xi 0`。 -/
example : Formula ℒₛₑₜ V = Semiformula ℒₛₑₜ V 0 := rfl

/-- **查实 2**：闭项版的自反性成立（`ZFCSetInternal.lean:90`）。 -/
example (t : Term V ℒₛₑₜ) : 𝗭𝗙𝗖.internalize V ⊢ setEq t t := set_eq_refl t

/-- **查实 3**：而 `n > 0` 时 `⊢` 不适用。

下面这行**预期编不过**（保留为注释形式的事实记录）：

```lean
-- example {n : ℕ} (t : Semiterm V ℒₛₑₜ n) (hn : n ≠ 0) :
--     𝗭𝗙𝗖.internalize V ⊢ setEq t t := set_eq_refl t
-- 错误：failed to synthesize instance of type class
--   Entailment (InternalTheory V ℒₛₑₜ) (Bootstrapping.Semiformula V ℒₛₑₜ n)
``` -/
example : True := trivial

end GodelQ.CG008HEQGen
