import GodelQ.ZFC.TransTerm

/-!
# 012-Opus · W8：有界 ∀ 的合并（V 中归纳）

若对每个 i < b（b ∈ V，可以非标准）都有 `Γ ⊢ ∀x(N_i(x) → Φ(x))`，则
`Γ ⊢ ∀z ∀x(N_b(z) → x ∈ z → Φ(x))`。证明对 c ≤ b 在 V 中归纳；归纳谓词“Z 证明某个码”是 Σ1 的。
每一步用两条标准句：空集没有元素；x ∈ v ∪ {v} 则 x ∈ v 或 v = x。
-/

namespace GodelQ.SetNum

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment FFL.Entailment.FiniteContext
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCNum GodelQ.ZFCArith GodelQ.IntLogic GodelQ.Translate

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

local prefix:max "#'" => Bootstrapping.Semiterm.bvar (V := V) (L := ℒₛₑₜ)
local prefix:max "&'" => Bootstrapping.Semiterm.fvar (V := V) (L := ℒₛₑₜ)

lemma zfc_num0_nmem : 𝗭𝗙𝗖 ⊢ (“∀ z x, !(numeralF 0) z → !memB x z → ⊥” : Sentence ℒₛₑₜ) := by
  apply SetTheory.complete.{0}
  intro M _ _ _
  simp only [models_iff]
  simp [Semiformula.eval_substs, eval_num0]
  intro z x hz
  subst hz
  simp

lemma zfc_mem_step_cases :
    𝗭𝗙𝗖 ⊢ (“∀ x z v, !numStep v z → !memB x z → !memB x v ∨ !eqB v x” : Sentence ℒₛₑₜ) := by
  apply SetTheory.complete.{0}
  intro M _ _ _
  simp only [models_iff]
  simp only [Semiformula.eval_all, LogicalConnective.HomClass.map_imply, Semiformula.eval_substs,
    LogicalConnective.HomClass.map_or]
  intro x z v hs hm
  have hz : z = SetTheory.succ v := by simpa using (eval_numStep v z).mp (by simpa using hs)
  have hx : x ∈ z := by simpa using hm
  rw [hz, mem_succ_iff] at hx
  rcases hx with (h | h)
  · right; simpa using h.symm
  · left; simpa using h

theorem ball_merge {Γ : List (Bootstrapping.Formula V ℒₛₑₜ)} (b : V) (Φ : Bootstrapping.Semiformula V ℒₛₑₜ 1)
    (h : ∀ i < b, Γ ⊢[Z V] ∀¹ (numF i 🡒 Φ)) :
    Γ ⊢[Z V] ∀¹ ∀¹ ((numF b).subst ![#'1] 🡒 memF.subst ![#'0, #'1] 🡒 Φ.subst ![#'0]) := by
  have key : ∀ c : V, c ≤ b → Z V ⊢ ⋀Γ 🡒 ∀¹ ∀¹ ((numF c).subst ![#'1] 🡒 memF.subst ![#'0, #'1] 🡒
      Φ.subst ![#'0]) := by
    intro c
    induction c using ISigma1.sigma1_succ_induction
    · simp only [tprovable_iff_provable]; definability
    case zero =>
      intro _
      have h0 : Z V ⊢ ∀¹ ∀¹ ((numF 0).subst ![#'1] 🡒 memF.subst ![#'0, #'1] 🡒 ⊥) := by
        simpa [tq_vec_cons, fin1_fun_eq, numF_zero] using
          internal_provable_of_outer_provable (V := V) zfc_num0_nmem
      apply FiniteContext.provable_iff.mp
      apply TProof.generalize!
      simp [Bootstrapping.Semiformula.free, Bootstrapping.Semiformula.shift_substs,
        Bootstrapping.Semiformula.substs_substs]
      apply TProof.generalize!
      simp [Bootstrapping.Semiformula.free, Bootstrapping.Semiformula.shift_substs,
        Bootstrapping.Semiformula.substs_substs]
      apply FiniteContext.deduct
      apply FiniteContext.deduct
      have h0' : Z V ⊢ (numF 0).subst ![&'1] 🡒 memF.subst ![&'0, &'1] 🡒 ⊥ := by
        simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₂! h0 &'0 &'1
      exact Entailment.of_O (FiniteContext.of h0' ⨀ FiniteContext.by_axm₁ ⨀ FiniteContext.by_axm₀)
    case succ c ih =>
      intro hcb
      have hc : c < b := lt_of_lt_of_le (lt_add_one c) hcb
      have ihc := FiniteContext.provable_iff.mpr (ih (le_of_lt hc))
      have hcΦ := h c hc
      have hS : Z V ⊢ ∀¹ ∀¹ ∀¹ (stepF.subst ![#'0, #'1] 🡒 memF.subst ![#'2, #'1] 🡒
          (memF.subst ![#'2, #'0] ⋎ eqF.subst ![#'0, #'2])) := by
        simpa [tq_vec_cons, fin1_fun_eq] using internal_provable_of_outer_provable (V := V) zfc_mem_step_cases
      apply FiniteContext.provable_iff.mp
      rw [numF_succ]
      apply TProof.generalize!
      simp [Bootstrapping.Semiformula.free, Bootstrapping.Semiformula.shift_substs,
        Bootstrapping.Semiformula.substs_substs]
      apply TProof.generalize!
      simp [Bootstrapping.Semiformula.free, Bootstrapping.Semiformula.shift_substs,
        Bootstrapping.Semiformula.substs_substs]
      apply FiniteContext.deduct
      apply FiniteContext.deduct
      apply exs_elim FiniteContext.by_axm₁
      simp [Bootstrapping.Semiformula.free, Bootstrapping.Semiformula.shift_substs,
        Bootstrapping.Semiformula.substs_substs]
      have ihc3 := ctx_lift (ctx_lift (ctx_lift ihc (Δ := List.map Bootstrapping.Semiformula.shift Γ) (by simp))
        (Δ := List.map (Bootstrapping.Semiformula.shift ∘ Bootstrapping.Semiformula.shift) Γ) (by simp))
        (Δ := List.map (Bootstrapping.Semiformula.shift ∘ Bootstrapping.Semiformula.shift ∘
          Bootstrapping.Semiformula.shift) Γ) (by simp)
      have hcΦ3 := ctx_lift (ctx_lift (ctx_lift hcΦ (Δ := List.map Bootstrapping.Semiformula.shift Γ) (by simp))
        (Δ := List.map (Bootstrapping.Semiformula.shift ∘ Bootstrapping.Semiformula.shift) Γ) (by simp))
        (Δ := List.map (Bootstrapping.Semiformula.shift ∘ Bootstrapping.Semiformula.shift ∘
          Bootstrapping.Semiformula.shift) Γ) (by simp)
      simp only [Bootstrapping.Semiformula.shift_all, Bootstrapping.Semiformula.shift_imp,
        Bootstrapping.Semiformula.shift_substs] at ihc3 hcΦ3
      have hM := specialize₂_ctx ihc3 (&'1) (&'0)
      have hE := TProof.specialize_with_ctx! hcΦ3 (&'1)
      simp [Bootstrapping.Semiformula.substs_substs] at hM hE
      have hS' : Z V ⊢ stepF.subst ![&'0, &'2] 🡒 memF.subst ![&'1, &'2] 🡒
          (memF.subst ![&'1, &'0] ⋎ eqF.subst ![&'0, &'1]) := by
        simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₃! hS &'0 &'2 &'1
      have hC : Z V ⊢ eqF.subst ![&'0, &'1] 🡒 (numF c).subst ![&'0] 🡒 (numF c).subst ![&'1] := by
        simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₂! (numF_congr c) &'1 &'0
      refine Entailment.of_C_of_C_of_A (FiniteContext.weakening ?_ hM ⨀ K_left FiniteContext.by_axm₀) ?_
        (FiniteContext.of hS' ⨀ K_right FiniteContext.by_axm₀ ⨀ FiniteContext.by_axm₁)
      · intro x hx; simp [hx]
      · apply FiniteContext.deduct
        refine FiniteContext.weakening ?_ hE ⨀
          (FiniteContext.of hC ⨀ FiniteContext.by_axm₀ ⨀ K_left FiniteContext.by_axm₁)
        intro x hx; simp [hx]
  exact FiniteContext.provable_iff.mpr (key b le_rfl)

end GodelQ.SetNum

#print axioms GodelQ.SetNum.ball_merge
