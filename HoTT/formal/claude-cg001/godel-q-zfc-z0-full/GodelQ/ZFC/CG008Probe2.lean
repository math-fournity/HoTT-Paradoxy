import GodelQ.ZFC.Z0Full
import GodelQ.ZFC.ZFCSetSigma1

/-!
# CG-008 探针 2（非收据）：判定 §4 路线可行性

**核心发现**：`EquationalTheory.lean` 的 `eq_refl`/`eq_symm` 套路**对语言 L 通用**：
`TProof.specialize!`、`internal_provable_of_outer_provable`、`K_intro`、`A_intro_left`、`TProof.exs!`
都只要求 `T : Theory L` + `[T.Δ₁]`。唯一 ℒₒᵣ 专属的是 `≐` 记号（`Semiterm.equals` 硬接线 `ℒₒᵣ`）
与 `complete` 的来源（算术版 vs `SetTheory.complete`）。

本探针用编译逐条验证这个判断。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Probe2

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.ZFCSetSigma1

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- 集合语言的等式原子（`≐` 的 ℒₛₑₜ 版）。 -/
noncomputable abbrev setEq {n : ℕ} (t u : Semiterm V ℒₛₑₜ n) : Semiformula V ℒₛₑₜ n :=
  .rel Language.Eq.eq ![t, u]

/-- 探针 A：集合语言的 `eq_refl`（`SetTheory.complete` 路径）。**已通过编译。** -/
theorem probe_eq_refl (t : Term V ℒₛₑₜ) : 𝗭𝗙𝗖.internalize V ⊢ setEq t t := by
  have h₁ : 𝗭𝗙𝗖 ⊢ (∀¹ (setEq (Semiterm.bvar 0) (Semiterm.bvar 0) :
      Semiformula V ℒₛₑₜ 1) : SetTheorySentence) :=
    SetTheory.complete 𝗭𝗙𝗖 _ fun M _ _ _ ↦ by simp [setEq, models_iff]
  have h₂ : 𝗭𝗙𝗖.internalize V ⊢ (∀¹ (setEq (Semiterm.bvar 0) (Semiterm.bvar 0) :
      Semiformula V ℒₛₑₜ 1)) := by
    simpa using! internal_provable_of_outer_provable (T := 𝗭𝗙𝗖) (V := V) h₁
  simpa using TProof.specialize! h₂ t

/-- 探针 C：集合语言的合取引入（`K_intro` 对 `InternalTheory V L` 通用）。 -/
theorem probe_K_intro (φ ψ : Formula V ℒₛₑₜ)
    (hφ : 𝗭𝗙𝗖.internalize V ⊢ φ) (hψ : 𝗭𝗙𝗖.internalize V ⊢ ψ) :
    𝗭𝗙𝗖.internalize V ⊢ φ ⋏ ψ :=
  K_intro hφ hψ

/-- 探针 D：集合语言的析取引入。 -/
theorem probe_A_intro_left (φ ψ : Formula V ℒₛₑₜ) (hφ : 𝗭𝗙𝗖.internalize V ⊢ φ) :
    𝗭𝗙𝗖.internalize V ⊢ φ ⋎ ψ :=
  A_intro_left hφ

/-- 探针 E：集合语言的 ∃-引入（`TProof.exs!`）。 -/
theorem probe_exs (φ : Semiformula V ℒₛₑₜ 1) (t : Term V ℒₛₑₜ)
    (h : 𝗭𝗙𝗖.internalize V ⊢ φ.subst ![t]) :
    𝗭𝗙𝗖.internalize V ⊢ ∃¹ φ :=
  TProof.exs! t h

/-- 探针 F：`SetTheory.complete` 对 `𝗭𝗙𝗖` 可用。 -/
theorem probe_complete (φ : SetTheorySentence)
    (H : ∀ (M : Type) [SetStructure M] [Nonempty M] [M↓[ℒₛₑₜ] ⊧* 𝗭𝗙𝗖], M↓[ℒₛₑₜ] ⊧ φ) :
    𝗭𝗙𝗖 ⊢ φ := SetTheory.complete 𝗭𝗙𝗖 φ H

end GodelQ.CG008Probe2
