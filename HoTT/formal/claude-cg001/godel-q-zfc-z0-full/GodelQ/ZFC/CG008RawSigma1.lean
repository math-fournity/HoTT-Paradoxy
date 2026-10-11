import GodelQ.ZFC.CG008Raw

/-!
# CG-008 · 在 `Derivable` 层做 Σ₁ 完全性的可行性

## 缺口现状（本轮重建后）

归约（`CG008Reduce.lean`）后：`∀ V ⊨ 𝗜𝚺₁, ∀ τ, 𝗭𝗙𝗖.internalize V ⊢ ⌜translate τ⌝ →
𝗭𝗙𝗖.internalize V ⊢ ⌜translate (zfcTr τ)⌝`。

障碍（`CG008MemCase.lean`）：算术版靠 `toNumVec` 把自由变量的值命名成**数字项**；
`ℒₛₑₜ` 无常项，无对偶。

新通道（`CG008Raw.lean`）：`Derivable` 原始层只作用在编码上，**没有自由变量概念**。

## 本文件要判定的

`Derivable` 层能否让 Σ₁ 完全性的**原子情形**走通——即：
从「V 内部的某条推导 `d`」出发，在**编码层**造出「那条推导的存在性」的编码。

具体地，本文件先固定 `Derivable` 层的**基本操作**：
`Derivable` 的合取/析取/量词规则已有（探针 6 查实），本文件补**等式的编码层规则**，
它们是 Σ₁ 原子情形（`hEQ`/`hNEQ`）的构件。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进入收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008RawSigma1

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.ZFCSetSigma1
  GodelQ.ZFCSetInternal GodelQ.CG008Reduce GodelQ.CG008SetAll GodelQ.CG008Raw

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## 1. 从 `ZFCSetInternal` 的引理下沉到 `Derivable` 层

`ZFCSetInternal.lean` 的每条引理结论都是 typed 层。用 `CG008Raw` 的桥下沉。
下面把全部 13 条 + `CG008SetAll` 的 4 条**逐条下沉**，建成 `Derivable` 层的工具集。 -/

theorem d_set_eq_refl (t : Term V ℒₛₑₜ) :
    Derivable 𝗭𝗙𝗖 (insert (setEq t t).val ∅ : V) :=
  internal_derivable_of_tprovable (set_eq_refl t)

theorem d_set_eq_symm (t u : Term V ℒₛₑₜ) :
    Derivable 𝗭𝗙𝗖 (insert (setEq t u 🡒 setEq u t).val ∅ : V) :=
  internal_derivable_of_tprovable (set_eq_symm t u)

theorem d_set_ne_symm (t u : Term V ℒₛₑₜ) :
    Derivable 𝗭𝗙𝗖 (insert (setNe t u 🡒 setNe u t).val ∅ : V) :=
  internal_derivable_of_tprovable (set_ne_symm t u)

theorem d_set_eq_uniform_trans (t₁ t₂ t₃ : Term V ℒₛₑₜ) :
    Derivable 𝗭𝗙𝗖 (insert (setEq t₁ t₂ 🡒 setEq t₂ t₃ 🡒 setEq t₁ t₃).val ∅ : V) :=
  internal_derivable_of_tprovable (set_eq_uniform_trans t₁ t₂ t₃)

theorem d_set_subst_eq (t₁ t₂ u₁ u₂ : Term V ℒₛₑₜ) :
    Derivable 𝗭𝗙𝗖
      (insert (setEq t₁ t₂ 🡒 setEq u₁ u₂ 🡒 setEq t₁ u₁ 🡒 setEq t₂ u₂).val ∅ : V) :=
  internal_derivable_of_tprovable (set_subst_eq t₁ t₂ u₁ u₂)

theorem d_set_subst_mem (t₁ t₂ u₁ u₂ : Term V ℒₛₑₜ) :
    Derivable 𝗭𝗙𝗖
      (insert (setEq t₁ t₂ 🡒 setEq u₁ u₂ 🡒 setMem t₁ u₁ 🡒 setMem t₂ u₂).val ∅ : V) :=
  internal_derivable_of_tprovable (set_subst_mem t₁ t₂ u₁ u₂)

theorem d_set_mem_of_eq (x t u : Term V ℒₛₑₜ) :
    Derivable 𝗭𝗙𝗖 (insert (setMem x t 🡒 setEq t u 🡒 setMem x u).val ∅ : V) :=
  internal_derivable_of_tprovable (set_mem_of_eq x t u)

theorem d_set_K_intro (φ ψ : Formula V ℒₛₑₜ)
    (hφ : Derivable 𝗭𝗙𝗖 (insert φ.val ∅ : V))
    (hψ : Derivable 𝗭𝗙𝗖 (insert ψ.val ∅ : V)) :
    Derivable 𝗭𝗙𝗖 (insert (φ ⋏ ψ).val ∅ : V) :=
  internal_derivable_of_tprovable (set_K_intro φ ψ
    (tprovable_of_internal_derivable hφ) (tprovable_of_internal_derivable hψ))

theorem d_set_A_intro_left (φ ψ : Formula V ℒₛₑₜ)
    (hφ : Derivable 𝗭𝗙𝗖 (insert φ.val ∅ : V)) :
    Derivable 𝗭𝗙𝗖 (insert (φ ⋎ ψ).val ∅ : V) :=
  internal_derivable_of_tprovable (set_A_intro_left φ ψ (tprovable_of_internal_derivable hφ))

theorem d_set_A_intro_right (φ ψ : Formula V ℒₛₑₜ)
    (hψ : Derivable 𝗭𝗙𝗖 (insert ψ.val ∅ : V)) :
    Derivable 𝗭𝗙𝗖 (insert (φ ⋎ ψ).val ∅ : V) :=
  internal_derivable_of_tprovable (set_A_intro_right φ ψ (tprovable_of_internal_derivable hψ))

theorem d_set_exs_intro (φ : Semiformula V ℒₛₑₜ 1) (t : Term V ℒₛₑₜ)
    (h : Derivable 𝗭𝗙𝗖 (insert (φ.subst ![t]).val ∅ : V)) :
    Derivable 𝗭𝗙𝗖 (insert (∃¹ φ).val ∅ : V) :=
  internal_derivable_of_tprovable (set_exs_intro φ t (tprovable_of_internal_derivable h))

theorem d_set_all_intro (φ : Semiformula V ℒₛₑₜ 1)
    (h : Derivable 𝗭𝗙𝗖 (insert φ.free.val ∅ : V)) :
    Derivable 𝗭𝗙𝗖 (insert (∀¹ φ).val ∅ : V) :=
  internal_derivable_of_tprovable (set_all_intro φ (tprovable_of_internal_derivable h))

theorem d_set_ball_intro (t : Term V ℒₛₑₜ) (φ : Semiformula V ℒₛₑₜ 1)
    (h : Derivable 𝗭𝗙𝗖 (insert ((.rel Language.Mem.mem
      ![Semiterm.bvar 0, Semiterm.bShift t]) 🡒 φ).free.val ∅ : V)) :
    Derivable 𝗭𝗙𝗖 (insert (setBall t φ).val ∅ : V) :=
  internal_derivable_of_tprovable (set_ball_intro t φ (tprovable_of_internal_derivable h))

end GodelQ.CG008RawSigma1
