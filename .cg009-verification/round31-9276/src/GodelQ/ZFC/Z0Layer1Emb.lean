import GodelQ.ZFC.Z0Layer1

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.Z0Full
open LogicalConnective

/-!
# CG-007 · W8 第 1 层剩余：语句模式转移 `emb`（CG001-C-389，**部分已证**）

本文件带未证标记，因此**4e0d是**任何运行收据的编译源。
已证：`emb_term`（项层）、`emb_vec`（向量层）、`emb_id` 的 8 个构造子中 6 个。
未证：`emb_id` 的 `all`/`exs` 两案（下面有诊断），以及由它们组成的 `emb_commute`。
-/

namespace GodelQ.Z0Layer1Emb

variable {n : ℕ} {k : ℕ}

/-- 项层：`emb` 在 `Empty` 上下文的项上是身份（结构归纳）。 -/
theorem emb_term (t : Semiterm ℒₒᵣ Empty n) : Rew.emb t = t := by
  induction t using FirstOrder.Semiterm.rec with
  | bvar x => simp [Rew.emb, Rew.map_bvar]
  | fvar x => exact isEmptyElim x
  | func a v ih =>
      have h : ⇑Rew.id ∘ v = v := by funext i; simp
      simp [Rew.func, h]

/-- 向量层。 -/
theorem emb_vec (v : Fin k → Semiterm ℒₒᵣ Empty n) : ⇑Rew.id ∘ v = v := by
  funext i; simp

/-- **部分已证**：语句层的 `emb` 恒等。`all`/`exs` 两案例未证。 -/
theorem emb_id (φ : Semiformula ℒₒᵣ Empty n) : Semiformula.rew Rew.emb φ = φ := by
  induction φ using FirstOrder.Semiformula.rec' with
  | hverum => rfl
  | hfalsum => rfl
  | hrel r v =>
      show Semiformula.rew Rew.emb (FirstOrder.Semiformula.rel r v) = FirstOrder.Semiformula.rel r v
      rw [show Semiformula.rew Rew.emb (FirstOrder.Semiformula.rel r v)
            = FirstOrder.Semiformula.rel r (Rew.emb ∘ v) from rfl]
      congr 1
      funext i
      exact emb_term (v i)
  | hnrel r v =>
      show Semiformula.rew Rew.emb (FirstOrder.Semiformula.nrel r v) = FirstOrder.Semiformula.nrel r v
      rw [show Semiformula.rew Rew.emb (FirstOrder.Semiformula.nrel r v)
            = FirstOrder.Semiformula.nrel r (Rew.emb ∘ v) from rfl]
      congr 1
      funext i
      exact emb_term (v i)
  | hand φ ψ ihφ ihψ =>
      obtain ⟨hφ, hψ⟩ : (Semiformula.rew Rew.emb φ = φ) ∧ (Semiformula.rew Rew.emb ψ = ψ) := ⟨ihφ, ihψ⟩
      rw [Rew.emb_eq_id] at hφ hψ
      simpa using ⟨hφ, hψ⟩
  | hor φ ψ ihφ ihψ =>
      obtain ⟨hφ, hψ⟩ : (Semiformula.rew Rew.emb φ = φ) ∧ (Semiformula.rew Rew.emb ψ = ψ) := ⟨ihφ, ihψ⟩
      rw [Rew.emb_eq_id] at hφ hψ
      simpa using ⟨hφ, hψ⟩
  | hall φ ih => sorry
  | hexs φ ih => sorry

end GodelQ.Z0Layer1Emb
