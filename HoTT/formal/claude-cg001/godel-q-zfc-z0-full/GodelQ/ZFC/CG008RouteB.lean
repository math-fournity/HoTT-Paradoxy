import GodelQ.ZFC.CG008Typeclass

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008RouteB

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.ZFCSetInternal

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! # 路 B 的第一步：半项的等式自反性

**目标**：`∀ n (t : Semiterm V ℒₛₑₜ n), 𝗭𝗙𝗖.internalize V ⊢ setEq t t`。

**为什么这不可能直接写**：`⊢` 的实例只到 `n = 0`（`CG008Typeclass` 已机器核实）。

**路 B 的做法**（照 `ZFCSetInternal` 的范例）：

1. 先用 `SetTheory.complete` 证**元层闭句** `∀ x, x = x`；
2. `internal_provable_of_outer_provable` 把它搬进 V；
3. 用 `TProof.all!` / `TProof.specialize!` **实例化**到 `t`。

第 3 步给出的是 `Semiformula V ℒₛₑₜ 0`（闭句），
因为 `specialize!` 把 `∀¹ φ` 特化成 `φ/[t]`，**减少了自由变量数**。

**所以 `∀¹` 的情形会被降到 0，但 `n = 1` 的 `setEq (Semiterm.bvar 0) t` 仍留 1 个变量**。
这正是需要「把标签往外提」的地方。

**本文件先查：`TProof.all!` 与 `specialize!` 的确切能力边界。**

**治理**：本文件只记查实，不含未证标记。 -/

/-- **查实 1**：`∀¹ (∀¹ φ)` 可逐层特化（`ZFCSetInternal` 的 `set_subst_eq` 就是这么做的）。

看 `ZFCSetInternal.lean:144` 的 `set_subst_eq`：它造的是
`∀¹ (∀¹ (∀¹ (∀¹ (setEq … : Semiformula V ℒₛₑₜ 4) )))`，
再 `TProof.specialize₄!` **四次**代入，得到 0 层。

**所以模式是：先在最高层把全称闭包做完，再逐次特化到底。** -/
noncomputable example : True := trivial

/-- **查实 2**：`set_eq_refl` 的构造（闭项版），完整读法。 -/
noncomputable example (t : Term V ℒₛₑₜ) : 𝗭𝗙𝗖.internalize V ⊢ setEq t t :=
  set_eq_refl t

end GodelQ.CG008RouteB
