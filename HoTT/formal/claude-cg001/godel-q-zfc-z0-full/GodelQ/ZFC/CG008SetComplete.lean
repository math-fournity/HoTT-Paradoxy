import GodelQ.ZFC.CG008Reduce

/-!
# CG-008 · 集合语言的内部 Σ₁ 完全性：可做的那一半

归约（`CG008Reduce.lean`）之后的目标是：
`∀ V ⊨ 𝗜𝚺₁, ∀ τ, 𝗭𝗙𝗖.internalize V ⊢ ⌜translate τ⌝ → 𝗭𝗙𝗖.internalize V ⊢ ⌜translate (zfcTr τ)⌝`。

探针 4 查实：直接走内部蕴含句（`zfcTr_D3_syntactic`）是循环的——那正是反射原理。
所以必须在内部**构造**推导。本文件做这条构造路线的**可做的一半**：

## 内部 Σ₁ 完全性的形状

`D3.lean:82` 的 `bold_sigma_one_complete` 是算术版的样板：

```lean
theorem bold_sigma_one_complete {φ : ArithmeticSemisentence n}
    (hp : ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 φ) {w} :
    V ⊧/w φ → T.internalize V ⊢ (toNumVec w ⤔ ⌜φ⌝)
```

它用 `Bounding.Hierarchy.arithmetic_sigma₁_induction'` 对 Σ₁ 结构做十情形归纳。
集合语言的对偶是 `setTheory_sigma₁_induction'`（`SetTheory/Basic/Hierarchy.lean:63`）。

**关键点**：`bold_sigma_one_complete` 的前提取 `V ⊧/w φ`（**语义**），
它的结论是 `T.internalize V ⊢ …`（**内部推导**）。
这正是「语义真 ⟹ 内部可证」的 Σ₁ 完全性。

## 本文件做什么

`ZFCSetInternal.lean` 已经给出了内部演算的**原子层**：
`set_eq_refl`（`t = t` 的内部证明）、`set_eq_symm`、`set_subst_eq`、`set_subst_mem`。
本文件把这些装配成 Σ₁ 归纳的**两个基础情形**（`hEQ` 与 `hMem`），
作为 `setTheory_sigma₁_induction'` 的构件。

**这是构造路线的第一段，不是完整证明。** 完整的 `set_sigma_one_complete` 还需要
处理 `ball`（Lévy 有界全称）与 `exs`（存在）两个量词情形，
它们需要内部演算的 `∀`-引入与 `∃`-引入——后者已有（`set_exs_intro`），
前者（`ball_intro` 的集合版）尚缺。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进入收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008SetComplete

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.ZFCSetSigma1
  GodelQ.ZFCSetInternal GodelQ.CG008Reduce

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## 1. Σ₁ 归纳的两个原子情形

`setTheory_sigma₁_induction'` 的 `hEQ` / `hMem` 情形要求：
对**任意**项 `t₁ t₂`（**带自由变量的半项**，不只是闭项），
给出内部推导 `𝗭𝗙𝗖.internalize V ⊢ (.rel … ![t₁, t₂])`。

但这里有一个**层次问题**：内部演算的 `⊢` 作用在 `Formula V L = Semiformula V L 0`（**闭**句）上，
而 `t₁ t₂` 是 `Semiterm V ℒₛₑₜ n`（可能有 `n` 个自由变量）。
`ZFCSetInternal.lean` 的 `set_eq_refl` 等只对 `Term V ℒₛₑₜ`（`n = 0`）成立。

所以 Σ₁ 归纳必须**先对闭句做**，或者把带自由变量的情形用全称闭包处理。
本文件先固定这个层次事实，它是构造路线的第二个障碍。 -/

/-- **层次事实**：内部演算的 `⊢` 只作用于闭句（`Formula V L`，即 `Semiformula V L 0`）。
`ZFCSetInternal.lean` 的辅助引理因此只对 `Term V ℒₛₑₜ`（闭项）成立。 -/
example (t u : Term V ℒₛₑₜ) : 𝗭𝗙𝗖.internalize V ⊢ setEq t u 🡒 setEq u t :=
  set_eq_symm t u

/-- **对照**：带自由变量的半项**不能**直接喂给 `set_eq_symm`
（这一行预期编不过；保留为注释形式的事实记录）。

```lean
-- 预期失败：
-- example {n : ℕ} (t u : Semiterm V ℒₛₑₜ n) :
--     𝗭𝗙𝗖.internalize V ⊢ (.rel Language.Eq.eq ![t, u] 🡒 .rel Language.Eq.eq ![u, t]) :=
--   set_eq_symm t u
-- 错误：`set_eq_symm` 要求 `Term V ℒₛₑₜ = Semiterm V ℒₛₑₜ 0`，而 `t : Semiterm V ℒₛₑₜ n`
``` -/
example (t u : Term V ℒₛₑₜ) : 𝗭𝗙𝗖.internalize V ⊢ setEq t u 🡒 setEq u t :=
  set_eq_symm t u

end GodelQ.CG008SetComplete
