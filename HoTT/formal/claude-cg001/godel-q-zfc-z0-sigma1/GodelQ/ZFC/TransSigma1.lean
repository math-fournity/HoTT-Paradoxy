import GodelQ.ZFC.TransBall

/-!
# 012-Opus · W8：经翻译的形式化 Σ1 完全性

对每个 V ⊧ 𝗜𝚺₁ 与每个 Σ1 算术公式 σ（参数 w : Fin n → V，可以非标准）：若 V ⊧ σ[w]，则在
“e i 是第 w i 个数”的上下文中，𝗭𝗙𝗖（在 V 中内化）证明 σ 的翻译。仿 Foundation `D3.lean` 的
`bold_sigma_one_complete`，对标准公式 σ 作元层归纳（`arithmetic_sigma₁_induction'`）：
- 原子情形用项引理（`term_ve`）与数字算术（`numF_uniq`、`numF_lt`、`numF_neq`、`numF_nlt`）；
- ∃ 情形取第 a 个数作见证（`numF_exists`）；
- 有界 ∀ 情形把对每个 i < b 的证明在 V 中归纳合并（`ball_merge`）。
-/

namespace GodelQ.SetNum

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment FFL.Entailment.FiniteContext
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCNum GodelQ.ZFCArith GodelQ.IntLogic GodelQ.Translate

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

local prefix:max "#'" => Bootstrapping.Semiterm.bvar (V := V) (L := ℒₛₑₜ)
local prefix:max "&'" => Bootstrapping.Semiterm.fvar (V := V) (L := ℒₛₑₜ)

@[simp] lemma relDef_eq' : relDef (Language.Eq.eq : (ℒₒᵣ).Rel 2) = eqB := rfl
@[simp] lemma relDef_lt' : relDef (Language.LT.lt : (ℒₒᵣ).Rel 2) = memB := rfl

variable (V) in
/-- 主归纳的断言：σ 在 V 中（参数 w）成立，则在“e i 是第 w i 个数”的上下文中，𝗭𝗙𝗖 证明 σ 的翻译。 -/
def TrComplete {n : ℕ} (φ : ArithmeticSemisentence n) : Prop :=
  ∀ (w : Fin n → V), V ⊧/w φ → ∀ (Γ : List (Bootstrapping.Formula V ℒₛₑₜ))
    (e : Fin n → Bootstrapping.Term V ℒₛₑₜ), NumHyp Γ w e →
    Γ ⊢[Z V] (⌜(arithTrln.translate φ : Semisentence ℒₛₑₜ n)⌝ : Bootstrapping.Semiformula V ℒₛₑₜ n).subst e

lemma trc_eq {n : ℕ} (t₁ t₂ : ClosedSemiterm ℒₒᵣ n) : TrComplete V (.rel Language.Eq.eq ![t₁, t₂]) := by
  intro w h Γ e hΓ
  have ha : t₁.valb w = t₂.valb w := by simpa using h
  rw [DirectTranslation.translate_rel, trRel2]
  apply TProof.generalize!
  simp [Bootstrapping.Semiformula.free, veF_shift, veF_subst, Bootstrapping.Semiformula.shift_substs,
    Bootstrapping.Semiformula.substs_substs, ← Bootstrapping.Semiterm.bShift_shift_comm,
    Bootstrapping.Semiterm.bShift_substs_succ]
  apply TProof.generalize!
  simp [Bootstrapping.Semiformula.free, veF_shift, veF_subst, Bootstrapping.Semiformula.shift_substs,
    Bootstrapping.Semiformula.substs_substs, ← Bootstrapping.Semiterm.bShift_shift_comm,
    Bootstrapping.Semiterm.bShift_substs_succ]
  apply FiniteContext.deduct
  have h2 : NumHyp (List.map (Bootstrapping.Semiformula.shift ∘ Bootstrapping.Semiformula.shift) Γ) w
      (fun i ↦ (e i).shift.shift) := by
    have h1 := hΓ.lift (Δ := List.map Bootstrapping.Semiformula.shift Γ) (by simp)
    simpa using h1.lift (Δ := List.map (Bootstrapping.Semiformula.shift ∘ Bootstrapping.Semiformula.shift) Γ)
      (by simp)
  have hU : Z V ⊢ (numF (t₂.valb w)).subst ![&'0] 🡒 (numF (t₂.valb w)).subst ![&'1] 🡒
      eqF.subst ![&'0, &'1] := by
    simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₂! (numF_uniq (t₂.valb w)) &'1 &'0
  have c1 := (term_ve t₁ w).2
  have c2 := (term_ve t₂ w).2
  rw [ha] at c1
  refine FiniteContext.of hU ⨀ (c1 _ _ (&'0) (h2.weak ?_) ⨀ K_right (K_left FiniteContext.by_axm₀)) ⨀
    (c2 _ _ (&'1) (h2.weak ?_) ⨀ K_right (K_left (K_right FiniteContext.by_axm₀)))
  · intro x hx; simp [hx]
  · intro x hx; simp [hx]

lemma trc_lt {n : ℕ} (t₁ t₂ : ClosedSemiterm ℒₒᵣ n) : TrComplete V (.rel Language.LT.lt ![t₁, t₂]) := by
  intro w h Γ e hΓ
  have ha : t₁.valb w < t₂.valb w := by simpa using h
  obtain ⟨d, hd⟩ := le_iff_exists_add.mp (lt_iff_succ_le.mp ha)
  have hd' : t₂.valb w = t₁.valb w + d + 1 := by rw [hd]; ring
  rw [DirectTranslation.translate_rel, trRel2]
  apply TProof.generalize!
  simp [Bootstrapping.Semiformula.free, veF_shift, veF_subst, Bootstrapping.Semiformula.shift_substs,
    Bootstrapping.Semiformula.substs_substs, ← Bootstrapping.Semiterm.bShift_shift_comm,
    Bootstrapping.Semiterm.bShift_substs_succ]
  apply TProof.generalize!
  simp [Bootstrapping.Semiformula.free, veF_shift, veF_subst, Bootstrapping.Semiformula.shift_substs,
    Bootstrapping.Semiformula.substs_substs, ← Bootstrapping.Semiterm.bShift_shift_comm,
    Bootstrapping.Semiterm.bShift_substs_succ]
  apply FiniteContext.deduct
  have h2 : NumHyp (List.map (Bootstrapping.Semiformula.shift ∘ Bootstrapping.Semiformula.shift) Γ) w
      (fun i ↦ (e i).shift.shift) := by
    have h1 := hΓ.lift (Δ := List.map Bootstrapping.Semiformula.shift Γ) (by simp)
    simpa using h1.lift (Δ := List.map (Bootstrapping.Semiformula.shift ∘ Bootstrapping.Semiformula.shift) Γ)
      (by simp)
  have hL : Z V ⊢ (numF (t₁.valb w)).subst ![&'0] 🡒 (numF (t₁.valb w + d + 1)).subst ![&'1] 🡒
      memF.subst ![&'0, &'1] := by
    simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₂! (numF_lt (t₁.valb w) d) &'1 &'0
  have c1 := (term_ve t₁ w).2
  have c2 := (term_ve t₂ w).2
  rw [hd'] at c2
  refine FiniteContext.of hL ⨀ (c1 _ _ (&'0) (h2.weak ?_) ⨀ K_right (K_left FiniteContext.by_axm₀)) ⨀
    (c2 _ _ (&'1) (h2.weak ?_) ⨀ K_right (K_left (K_right FiniteContext.by_axm₀)))
  · intro x hx; simp [hx]
  · intro x hx; simp [hx]

lemma trc_neq {n : ℕ} (t₁ t₂ : ClosedSemiterm ℒₒᵣ n) : TrComplete V (.nrel Language.Eq.eq ![t₁, t₂]) := by
  intro w h Γ e hΓ
  have ha : t₁.valb w ≠ t₂.valb w := by simpa using h
  rw [DirectTranslation.translate_nrel]
  have hq : (⌜(∼arithTrln.translateRel Language.Eq.eq ![t₁, t₂] : Semisentence ℒₛₑₜ n)⌝ :
      Bootstrapping.Semiformula V ℒₛₑₜ n).subst e =
      ∼((⌜(arithTrln.translateRel Language.Eq.eq ![t₁, t₂] : Semisentence ℒₛₑₜ n)⌝ :
        Bootstrapping.Semiformula V ℒₛₑₜ n).subst e) := by simp
  rw [hq, trRel2]
  simp only [Bootstrapping.Semiformula.neg_all, Bootstrapping.Semiformula.imp_def]
  simp
  have h1 : NumHyp (List.map Bootstrapping.Semiformula.shift Γ) w (fun i ↦ (e i).shift) := hΓ.lift (by simp)
  apply exs_elim ((term_ve t₁ w).1 Γ e hΓ)
  simp [Bootstrapping.Semiformula.free, veF_shift, veF_subst, Bootstrapping.Semiformula.shift_substs,
    Bootstrapping.Semiformula.substs_substs, ← Bootstrapping.Semiterm.bShift_shift_comm,
    Bootstrapping.Semiterm.bShift_substs_succ]
  apply exs_elim ((term_ve t₂ w).1 _ _ (h1.weak (by simp)))
  simp [Bootstrapping.Semiformula.free, veF_shift, veF_subst, Bootstrapping.Semiformula.shift_substs,
    Bootstrapping.Semiformula.substs_substs, ← Bootstrapping.Semiterm.bShift_shift_comm,
    Bootstrapping.Semiterm.bShift_substs_succ]
  apply exs_intro _ (&'0)
  simp [Bootstrapping.Semiformula.free, veF_shift, veF_subst, Bootstrapping.Semiformula.shift_substs,
    Bootstrapping.Semiformula.substs_substs, ← Bootstrapping.Semiterm.bShift_shift_comm,
    Bootstrapping.Semiterm.bShift_substs_succ]
  apply exs_intro _ (&'1)
  simp [Bootstrapping.Semiformula.free, veF_shift, veF_subst, Bootstrapping.Semiformula.shift_substs,
    Bootstrapping.Semiformula.substs_substs, ← Bootstrapping.Semiterm.bShift_shift_comm,
    Bootstrapping.Semiterm.bShift_substs_succ]
  have h2 : NumHyp (List.map (Bootstrapping.Semiformula.shift ∘ Bootstrapping.Semiformula.shift) Γ) w
      (fun i ↦ (e i).shift.shift) := by
    simpa using h1.lift (Δ := List.map (Bootstrapping.Semiformula.shift ∘ Bootstrapping.Semiformula.shift) Γ)
      (by simp)
  have hN : Z V ⊢ (numF (t₁.valb w)).subst ![&'1] 🡒 (numF (t₂.valb w)).subst ![&'0] 🡒
      ∼eqF.subst ![&'1, &'0] := by
    simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₂! (numF_neq ha) &'0 &'1
  refine K_intro (K_intro FiniteContext.by_axm₁ (K_intro FiniteContext.by_axm₀ Entailment.verum))
    (FiniteContext.of hN ⨀ ((term_ve t₁ w).2 _ _ (&'1) (h2.weak ?_) ⨀ K_right FiniteContext.by_axm₁) ⨀
      ((term_ve t₂ w).2 _ _ (&'0) (h2.weak ?_) ⨀ K_right FiniteContext.by_axm₀))
  · intro x hx; simp [hx]
  · intro x hx; simp [hx]


lemma trc_nlt {n : ℕ} (t₁ t₂ : ClosedSemiterm ℒₒᵣ n) : TrComplete V (.nrel Language.LT.lt ![t₁, t₂]) := by
  intro w h Γ e hΓ
  have ha : t₂.valb w ≤ t₁.valb w := by simpa using h
  rw [DirectTranslation.translate_nrel]
  have hq : (⌜(∼arithTrln.translateRel Language.LT.lt ![t₁, t₂] : Semisentence ℒₛₑₜ n)⌝ :
      Bootstrapping.Semiformula V ℒₛₑₜ n).subst e =
      ∼((⌜(arithTrln.translateRel Language.LT.lt ![t₁, t₂] : Semisentence ℒₛₑₜ n)⌝ :
        Bootstrapping.Semiformula V ℒₛₑₜ n).subst e) := by simp
  rw [hq, trRel2]
  simp only [Bootstrapping.Semiformula.neg_all, Bootstrapping.Semiformula.imp_def]
  simp
  have h1 : NumHyp (List.map Bootstrapping.Semiformula.shift Γ) w (fun i ↦ (e i).shift) := hΓ.lift (by simp)
  apply exs_elim ((term_ve t₁ w).1 Γ e hΓ)
  simp [Bootstrapping.Semiformula.free, veF_shift, veF_subst, Bootstrapping.Semiformula.shift_substs,
    Bootstrapping.Semiformula.substs_substs, ← Bootstrapping.Semiterm.bShift_shift_comm,
    Bootstrapping.Semiterm.bShift_substs_succ]
  apply exs_elim ((term_ve t₂ w).1 _ _ (h1.weak (by simp)))
  simp [Bootstrapping.Semiformula.free, veF_shift, veF_subst, Bootstrapping.Semiformula.shift_substs,
    Bootstrapping.Semiformula.substs_substs, ← Bootstrapping.Semiterm.bShift_shift_comm,
    Bootstrapping.Semiterm.bShift_substs_succ]
  apply exs_intro _ (&'0)
  simp [Bootstrapping.Semiformula.free, veF_shift, veF_subst, Bootstrapping.Semiformula.shift_substs,
    Bootstrapping.Semiformula.substs_substs, ← Bootstrapping.Semiterm.bShift_shift_comm,
    Bootstrapping.Semiterm.bShift_substs_succ]
  apply exs_intro _ (&'1)
  simp [Bootstrapping.Semiformula.free, veF_shift, veF_subst, Bootstrapping.Semiformula.shift_substs,
    Bootstrapping.Semiformula.substs_substs, ← Bootstrapping.Semiterm.bShift_shift_comm,
    Bootstrapping.Semiterm.bShift_substs_succ]
  have h2 : NumHyp (List.map (Bootstrapping.Semiformula.shift ∘ Bootstrapping.Semiformula.shift) Γ) w
      (fun i ↦ (e i).shift.shift) := by
    simpa using h1.lift (Δ := List.map (Bootstrapping.Semiformula.shift ∘ Bootstrapping.Semiformula.shift) Γ)
      (by simp)
  have hN : Z V ⊢ (numF (t₁.valb w)).subst ![&'1] 🡒 (numF (t₂.valb w)).subst ![&'0] 🡒
      ∼memF.subst ![&'1, &'0] := by
    simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₂! (numF_nlt ha) &'0 &'1
  refine K_intro (K_intro FiniteContext.by_axm₁ (K_intro FiniteContext.by_axm₀ Entailment.verum))
    (FiniteContext.of hN ⨀ ((term_ve t₁ w).2 _ _ (&'1) (h2.weak ?_) ⨀ K_right FiniteContext.by_axm₁) ⨀
      ((term_ve t₂ w).2 _ _ (&'0) (h2.weak ?_) ⨀ K_right FiniteContext.by_axm₀))
  · intro x hx; simp [hx]
  · intro x hx; simp [hx]


/-- q-代换后的句子引号，平移再实例化：变成直接代换。 -/
lemma tq_subst_q_shift_inst {n : ℕ} (σ : Semisentence ℒₛₑₜ (n + 1)) (e : Fin n → Bootstrapping.Term V ℒₛₑₜ)
    (t : Bootstrapping.Term V ℒₛₑₜ) :
    (((⌜σ⌝ : Bootstrapping.Semiformula V ℒₛₑₜ (n + 1)).subst (SemitermVec.q e)).shift).subst ![t] =
      (⌜σ⌝ : Bootstrapping.Semiformula V ℒₛₑₜ (n + 1)).subst (t :> fun i ↦ (e i).shift) := by
  rw [Bootstrapping.Semiformula.shift_substs, tq_shift_sentence, Bootstrapping.Semiformula.substs_substs]
  congr 1
  funext i
  cases i using Fin.cases <;> simp [← Bootstrapping.Semiterm.bShift_shift_comm]

lemma tq_subst_q_free {n : ℕ} (σ : Semisentence ℒₛₑₜ (n + 1)) (e : Fin n → Bootstrapping.Term V ℒₛₑₜ) :
    ((⌜σ⌝ : Bootstrapping.Semiformula V ℒₛₑₜ (n + 1)).subst (SemitermVec.q e)).free =
      (⌜σ⌝ : Bootstrapping.Semiformula V ℒₛₑₜ (n + 1)).subst (&'0 :> fun i ↦ (e i).shift) :=
  tq_subst_q_shift_inst σ e &'0

lemma trc_verum {n : ℕ} : TrComplete V (⊤ : ArithmeticSemisentence n) := by
  intro w _ Γ e _
  simpa using (Entailment.verum : Γ ⊢[Z V] ⊤)

lemma trc_falsum {n : ℕ} : TrComplete V (⊥ : ArithmeticSemisentence n) := by
  intro w h
  simp at h

lemma trc_and {n : ℕ} (φ ψ : ArithmeticSemisentence n) (ihφ : TrComplete V φ) (ihψ : TrComplete V ψ) :
    TrComplete V (φ ⋏ ψ) := by
  intro w h Γ e hΓ
  have H : V ⊧/w φ ∧ V ⊧/w ψ := by simpa using h
  simpa using K_intro (ihφ w H.1 Γ e hΓ) (ihψ w H.2 Γ e hΓ)

lemma trc_or {n : ℕ} (φ ψ : ArithmeticSemisentence n) (ihφ : TrComplete V φ) (ihψ : TrComplete V ψ) :
    TrComplete V (φ ⋎ ψ) := by
  intro w h Γ e hΓ
  have H : V ⊧/w φ ∨ V ⊧/w ψ := by simpa using h
  rcases H with (H | H)
  · simpa using A_intro_left (ψ := (⌜(arithTrln.translate ψ : Semisentence ℒₛₑₜ n)⌝ :
      Bootstrapping.Semiformula V ℒₛₑₜ n).subst e) (ihφ w H Γ e hΓ)
  · simpa using A_intro_right (φ := (⌜(arithTrln.translate φ : Semisentence ℒₛₑₜ n)⌝ :
      Bootstrapping.Semiformula V ℒₛₑₜ n).subst e) (ihψ w H Γ e hΓ)

lemma trc_exs {n : ℕ} (φ : ArithmeticSemisentence (n + 1)) (ih : TrComplete V φ) : TrComplete V (∃¹ φ) := by
  intro w h Γ e hΓ
  obtain ⟨a, ha⟩ : ∃ a, V ⊧/(a :> w) φ := by simpa using h
  rw [DirectTranslation.translate_ex]
  simp [DirectTranslation.exs, FirstOrder.bexs, Bootstrapping.Semiformula.substs_substs, fin1_fun_eq]
  apply exs_elim (FiniteContext.of (numF_exists a))
  have hD : Z V ⊢ (numF a).subst ![&'0] 🡒 domF.subst ![&'0] := by
    simpa using TProof.specialize! (numF_dom a) &'0
  have hdom : ((numF a).free :: Γ.map Bootstrapping.Semiformula.shift) ⊢[Z V] domF.subst ![&'0] :=
    FiniteContext.of hD ⨀ of_eq_ctx FiniteContext.by_axm₀ (by simp [Bootstrapping.Semiformula.free])
  have hih := ih (a :> w) ha _ _ (hΓ.cons a)
  refine of_eq_ctx (exs_intro ((domF ⋏ (⌜(arithTrln.translate φ : Semisentence ℒₛₑₜ (n + 1))⌝ :
      Bootstrapping.Semiformula V ℒₛₑₜ (n + 1)).subst (SemitermVec.q e)).shift) (&'0)
    (of_eq_ctx (K_intro hdom hih) ?_)) ?_
  · simp [tq_subst_q_shift_inst]
  · simp

lemma bS2_q {n : ℕ} (e : Fin n → Bootstrapping.Term V ℒₛₑₜ) :
    bS2 (SemitermVec.q e) =
      (#'2 : Bootstrapping.Semiterm V ℒₛₑₜ 3) :> fun j ↦ (e j).bShift.bShift.bShift := by
  funext j; cases j using Fin.cases <;> simp [bS2]

lemma trc_ball {n : ℕ} (t : ClosedSemiterm ℒₒᵣ n) (φ : ArithmeticSemisentence (n + 1)) (ih : TrComplete V φ) :
    TrComplete V (∀¹[“#0 < !!(Rew.bShift t)”] φ) := by
  intro w h Γ e hΓ
  have hb : ∀ i < t.valb w, V ⊧/(i :> w) φ := by simpa using h
  simp only [FirstOrder.ball, LogicalConnective.HomClass.map_imply, DirectTranslation.translate_all,
    Semiformula.Operator.lt_def]
  simp [DirectTranslation.fal, FirstOrder.ball, Bootstrapping.Semiformula.substs_substs, fin1_fun_eq]
  rw [trRel2]
  simp only [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons, veF_bvar, bS2_q, veF_bShift]
  set Φ := (⌜(arithTrln.translate φ : Semisentence ℒₛₑₜ (n + 1))⌝ :
    Bootstrapping.Semiformula V ℒₛₑₜ (n + 1)).subst (SemitermVec.q e) with hΦ
  have hmerge : Γ ⊢[Z V] ∀¹ ∀¹ ((numF (t.valb w)).subst ![#'1] 🡒 memF.subst ![#'0, #'1] 🡒
      Φ.subst ![#'0]) := by
    apply ball_merge
    intro i hi
    apply TProof.generalize!
    refine of_eq_ctx (FiniteContext.deduct (of_eq_ctx (ψ := Φ.free) (ih (i :> w) (hb i hi) _ _ (hΓ.cons i)) ?_)) ?_
    · rw [hΦ, tq_subst_q_free]
    · simp [Bootstrapping.Semiformula.free]
  apply TProof.generalize!
  simp [Bootstrapping.Semiformula.free, veF_shift, veF_subst, Bootstrapping.Semiformula.shift_substs,
    Bootstrapping.Semiformula.substs_substs, ← Bootstrapping.Semiterm.bShift_shift_comm,
    Bootstrapping.Semiterm.bShift_substs_succ]
  apply FiniteContext.deduct
  apply FiniteContext.deduct
  have h1 : NumHyp (List.map Bootstrapping.Semiformula.shift Γ) w (fun i ↦ (e i).shift) := hΓ.lift (by simp)
  apply exs_elim ((term_ve t w).1 _ _ (h1.weak (by intro x hx; simp [hx])))
  simp [Bootstrapping.Semiformula.free, veF_shift, veF_subst, Bootstrapping.Semiformula.shift_substs,
    Bootstrapping.Semiformula.substs_substs, ← Bootstrapping.Semiterm.bShift_shift_comm,
    Bootstrapping.Semiterm.bShift_substs_succ]
  have h2 : NumHyp (List.map (Bootstrapping.Semiformula.shift ∘ Bootstrapping.Semiformula.shift) Γ) w
      (fun i ↦ (e i).shift.shift) := by
    simpa using h1.lift (Δ := List.map (Bootstrapping.Semiformula.shift ∘ Bootstrapping.Semiformula.shift) Γ)
      (by simp)
  have hR : Z V ⊢ ∀¹ (eqF.subst ![#'0, #'0]) := by
    simpa [tq_vec_cons, fin1_fun_eq] using internal_provable_of_outer_provable (V := V) zfc_eq_refl
  have hR1 : Z V ⊢ eqF.subst ![&'1, &'1] := by
    simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize! hR &'1
  have hm2 := ctx_lift (ctx_lift hmerge (Δ := List.map Bootstrapping.Semiformula.shift Γ) (by simp))
    (Δ := List.map (Bootstrapping.Semiformula.shift ∘ Bootstrapping.Semiformula.shift) Γ) (by simp)
  simp only [Bootstrapping.Semiformula.shift_all, Bootstrapping.Semiformula.shift_imp,
    Bootstrapping.Semiformula.shift_substs] at hm2
  have hm3 := specialize₂_ctx hm2 (&'1) (&'0)
  simp [Bootstrapping.Semiformula.substs_substs] at hm3
  refine FiniteContext.weakening ?_ hm3 ⨀ ((term_ve t w).2 _ _ (&'0) (h2.weak ?_) ⨀ K_right FiniteContext.by_axm₀) ⨀
    (of_eq_ctx (specialize₂_ctx FiniteContext.by_axm₁ (&'1) (&'0)) ?_ ⨀
      K_intro (K_intro FiniteContext.by_axm₂ (FiniteContext.of hR1)) (K_intro FiniteContext.by_axm₀ Entailment.verum))
  · intro x hx; simp [hx]
  · intro x hx; simp [hx]
  · simp [Bootstrapping.Semiformula.substs_substs, veF_subst, Bootstrapping.Semiterm.bShift_substs_succ]


/-- **经翻译的形式化 Σ1 完全性**：σ 是 Σ1 的、在 V 中（参数 w）成立，则 𝗭𝗙𝗖（在 V 中内化）证明它的翻译。 -/
theorem tr_sigma1_complete {n : ℕ} {φ : ArithmeticSemisentence n} (hp : ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 φ) :
    TrComplete V φ := by
  apply Bounding.Hierarchy.arithmetic_sigma₁_induction' (P := fun _ φ ↦ TrComplete V φ) hp
  · intro n; exact trc_verum
  · intro n; exact trc_falsum
  · intro n t₁ t₂; exact trc_eq t₁ t₂
  · intro n t₁ t₂; exact trc_neq t₁ t₂
  · intro n t₁ t₂; exact trc_lt t₁ t₂
  · intro n t₁ t₂; exact trc_nlt t₁ t₂
  · intro n φ ψ _ _ ihφ ihψ; exact trc_and φ ψ ihφ ihψ
  · intro n φ ψ _ _ ihφ ihψ; exact trc_or φ ψ ihφ ihψ
  · intro n t φ _ ih; exact trc_ball t φ ih
  · intro n φ _ ih; exact trc_exs φ ih

/-- 句子形式。 -/
theorem tr_sigma1_provable {σ : ArithmeticSentence} (hσ : ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 σ)
    (h : V↓[ℒₒᵣ] ⊧ σ) :
    Z V ⊢ (⌜(arithTrln.translate σ : Sentence ℒₛₑₜ)⌝ : Bootstrapping.Formula V ℒₛₑₜ) := by
  have h0 : V ⊧/![] σ := by simpa [models_iff] using h
  have := tr_sigma1_complete hσ ![] h0 [] ![] (fun i ↦ i.elim0)
  simpa using FiniteContext.emptyPrf this


end GodelQ.SetNum

#print axioms GodelQ.SetNum.trc_eq
#print axioms GodelQ.SetNum.trc_neq
#print axioms GodelQ.SetNum.trc_lt
#print axioms GodelQ.SetNum.trc_nlt
#print axioms GodelQ.SetNum.trc_exs
#print axioms GodelQ.SetNum.trc_ball
#print axioms GodelQ.SetNum.tr_sigma1_complete
#print axioms GodelQ.SetNum.tr_sigma1_provable
