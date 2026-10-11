import GodelQ.ZFC.CG008SetComplete

/-!
# CG-008 · 集合语言的全称与 Lévy 有界全称：内部引入

`ZFCSetInternal.lean` 给了 13 条集合语言内部演算引理，唯一还缺的是**全称引入**。
本文件补上它。

## 为什么集合语言的版本比算术版简单

算术版 `PeanoMinus.lean:235` 的 `ball_intro` 处理 `φ.ball (𝕹 n)`（「对所有 `i < n`」），
必须先把 `< n` 展开成 `substItrDisj`（有限析取）再用 `numeral_lt` 逐项验证——
因为算术的 `<` 在模型里等价于有限析取。

集合语言的 Lévy 有界全称 `∀¹[“#0 ∈ t”] φ` 是**真正的量词**（`∈` 是关系符号），
不需要展开。所以集合版直接用 `TProof.all!` 即可——
而 `TProof.all!`（`Typed.lean:489`）对任意 `InternalTheory V L` 通用，与 `L` 无关。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进入收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008SetAll

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.ZFCSetSigma1
  GodelQ.ZFCSetInternal GodelQ.CG008Reduce

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **内部全称引入**：若对自由变量 0 能证 `φ`，则能证 `∀¹ φ`。

`TProof.all!`（`Typed.lean:489`）对 `InternalTheory V L` 通用——与 `L` 无关，
所以集合语言直接可用。这是集合版与算术版 `ball_intro` 之间最大的差别。 -/
theorem set_all_intro (φ : Semiformula V ℒₛₑₜ 1)
    (h : 𝗭𝗙𝗖.internalize V ⊢ φ.free) :
    𝗭𝗙𝗖.internalize V ⊢ ∀¹ φ :=
  TProof.all! h

/-- **内部全称消去**（对偶）：`∀¹ φ` 例化到任意项。 -/
theorem set_all_elim (φ : Semiformula V ℒₛₑₜ 1) (t : Term V ℒₛₑₜ)
    (h : 𝗭𝗙𝗖.internalize V ⊢ ∀¹ φ) :
    𝗭𝗙𝗖.internalize V ⊢ φ.subst ![t] :=
  TProof.specialize! h t

/-- **Lévy 有界全称**（显式 typed 定义）：`∀¹ (#0 ∈ t 🡒 φ)`，
即「对每个 `x ∈ t`，`φ x`」。

**为什么不直接写 `∀¹[“#0 ∈ !!(Rew.bShift t)”] φ`**：那条记号宏展开成
**untyped** 的 `FirstOrder.Semiformula`，与 `Bootstrapping.Semiformula V ℒₛₑₜ` 接不上
（编译实证：`Application type mismatch … expected Bootstrapping.Semiformula V ℒₛₑₜ`）。
显式写 `∀¹ (… 🡒 φ)` 就落在 typed 层，正是 `SetTheory/Basic/Hierarchy.lean`
的 `hBall` 情形（`∀¹[“#0 ∈ !!(Rew.bShift t)”] φ`）在 `val` 层的同一形状。 -/
noncomputable abbrev setBall (t : Term V ℒₛₑₜ) (φ : Semiformula V ℒₛₑₜ 1) :
    Semiformula V ℒₛₑₜ 0 :=
  ∀¹ ((.rel Language.Mem.mem ![Semiterm.bvar 0, Semiterm.bShift t]) 🡒 φ)

/-- **Lévy 有界全称引入**：若对自由变量 0 能证 `#0 ∈ t 🡒 φ`，则能证 `setBall t φ`。
由 `set_all_intro` 一步给出。 -/
theorem set_ball_intro (t : Term V ℒₛₑₜ) (φ : Semiformula V ℒₛₑₜ 1)
    (h : 𝗭𝗙𝗖.internalize V ⊢
      ((.rel Language.Mem.mem ![Semiterm.bvar 0, Semiterm.bShift t]) 🡒 φ).free) :
    𝗭𝗙𝗖.internalize V ⊢ setBall t φ :=
  set_all_intro _ h

/-- **成员关系的等号替换（推论形式）**：`x ∈ t → t = u → x ∈ u`。
由 `set_subst_mem`（`ZFCSetInternal.lean`）加自反性得到；
这是集合版 `ball_replace` 的核心。 -/
theorem set_mem_of_eq (x t u : Term V ℒₛₑₜ) :
    𝗭𝗙𝗖.internalize V ⊢ (.rel Language.Mem.mem ![x, t]) 🡒 setEq t u 🡒
      (.rel Language.Mem.mem ![x, u]) := by
  have hmem := set_subst_mem x x t u
  have hrefl : 𝗭𝗙𝗖.internalize V ⊢ setEq x x := set_eq_refl x
  cl_prover [hmem, hrefl]

end GodelQ.CG008SetAll
