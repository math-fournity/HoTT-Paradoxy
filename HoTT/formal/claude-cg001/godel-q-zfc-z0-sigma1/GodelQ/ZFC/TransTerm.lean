import GodelQ.ZFC.TransTyped

/-!
# 012-Opus · W8：项引理的准备——上下文工具、参数假设与标准句

D3 的主归纳把参数（σ 中的约束变量）换成自由变量 e i，并在上下文 Γ 中假设“e i 是第 w i 个数”
（`NumHyp`）。本文件给出：上下文的自由变量平移（`ctx_shift`、`ctx_lift`）；参数假设在弱化、平移、
进量词时的保持；项引理要用的几条标准 𝗭𝗙𝗖 句；加法、乘法在数字上的反向计算律。
-/

namespace GodelQ.SetNum

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment FFL.Entailment.FiniteContext
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCNum GodelQ.ZFCArith GodelQ.IntLogic GodelQ.Translate

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

local prefix:max "#'" => Bootstrapping.Semiterm.bvar (V := V) (L := ℒₛₑₜ)
local prefix:max "&'" => Bootstrapping.Semiterm.fvar (V := V) (L := ℒₛₑₜ)

section ctx
variable {L : Language} [L.Encodable] [L.LORDefinable] {T : InternalTheory V L}

lemma ctx_shift {Γ : List (Bootstrapping.Formula V L)} {φ : Bootstrapping.Formula V L}
    (h : Γ ⊢[T] φ) : Γ.map Bootstrapping.Semiformula.shift ⊢[T] φ.shift := by
  have h' : T ⊢ ⋀Γ 🡒 φ := FiniteContext.provable_iff.mp h
  apply FiniteContext.provable_iff.mpr
  have := TProof.shift! h'
  simpa [TProof.conj_shift] using this

lemma ctx_lift {Γ Δ : List (Bootstrapping.Formula V L)} {φ : Bootstrapping.Formula V L}
    (h : Γ ⊢[T] φ) (hΔ : Γ.map Bootstrapping.Semiformula.shift ⊆ Δ) : Δ ⊢[T] φ.shift :=
  FiniteContext.weakening hΔ (ctx_shift h)

end ctx

@[simp] lemma arithTrln_func {k : ℕ} (f : (ℒₒᵣ).Func k) : arithTrln.func f = funcDef f := rfl
@[simp] lemma arithTrln_rel {k : ℕ} (R : (ℒₒᵣ).Rel k) : arithTrln.rel R = relDef R := rfl
@[simp] lemma arithTrln_domain : arithTrln.domain = GodelQ.ZFCArith.domainDef := rfl

/-- 参数假设：上下文 Γ 证明每个 e i 是第 w i 个数。 -/
def NumHyp {n : ℕ} (Γ : List (Bootstrapping.Formula V ℒₛₑₜ)) (w : Fin n → V)
    (e : Fin n → Bootstrapping.Term V ℒₛₑₜ) : Prop :=
  ∀ i, Γ ⊢[Z V] (numF (w i)).subst ![e i]

lemma NumHyp.weak {n : ℕ} {Γ Δ : List (Bootstrapping.Formula V ℒₛₑₜ)} {w : Fin n → V}
    {e : Fin n → Bootstrapping.Term V ℒₛₑₜ} (h : NumHyp Γ w e) (hΔ : Γ ⊆ Δ) : NumHyp Δ w e :=
  fun i ↦ FiniteContext.weakening hΔ (h i)

lemma NumHyp.lift {n : ℕ} {Γ Δ : List (Bootstrapping.Formula V ℒₛₑₜ)} {w : Fin n → V}
    {e : Fin n → Bootstrapping.Term V ℒₛₑₜ} (h : NumHyp Γ w e)
    (hΔ : Γ.map Bootstrapping.Semiformula.shift ⊆ Δ) : NumHyp Δ w (fun i ↦ (e i).shift) := by
  intro i
  have := ctx_lift (h i) hΔ
  simpa [Bootstrapping.Semiformula.shift_substs] using this

lemma NumHyp.cons {n : ℕ} {Γ : List (Bootstrapping.Formula V ℒₛₑₜ)} {w : Fin n → V}
    {e : Fin n → Bootstrapping.Term V ℒₛₑₜ} (h : NumHyp Γ w e) (a : V) :
    NumHyp ((numF a).free :: Γ.map Bootstrapping.Semiformula.shift) (a :> w)
      (&'0 :> fun i ↦ (e i).shift) := by
  intro i
  cases i using Fin.cases
  · simpa [Bootstrapping.Semiformula.free] using
      (FiniteContext.by_axm₀ : ((numF a).free :: Γ.map Bootstrapping.Semiformula.shift) ⊢[Z V] (numF a).free)
  · simpa using h.lift (Δ := (numF a).free :: Γ.map Bootstrapping.Semiformula.shift) (by simp) _

/-! ## 项引理要用的标准句 -/

lemma zfc_eq_refl : 𝗭𝗙𝗖 ⊢ (“∀ x, !eqB x x” : Sentence ℒₛₑₜ) := by
  apply SetTheory.complete.{0}
  intro M _ _ _
  simp only [models_iff]
  simp [Semiformula.eval_substs]

lemma zfc_eq_symm : 𝗭𝗙𝗖 ⊢ (“∀ x y, !eqB x y → !eqB y x” : Sentence ℒₛₑₜ) := by
  apply SetTheory.complete.{0}
  intro M _ _ _
  simp only [models_iff]
  simp only [Semiformula.eval_all, LogicalConnective.HomClass.map_imply, Semiformula.eval_substs]
  intro x y h
  have e : x = y := by simpa using h
  subst e
  simp

lemma zfc_add_total :
    𝗭𝗙𝗖 ⊢ (“∀ x y, !GodelQ.ZFCArith.domainDef x → !GodelQ.ZFCArith.domainDef y → ∃ z, !addB z x y” :
      Sentence ℒₛₑₜ) := by
  apply SetTheory.complete.{0}
  intro M _ _ _
  simp only [models_iff]
  simp only [Semiformula.eval_all, LogicalConnective.HomClass.map_imply, Semiformula.eval_substs,
    Semiformula.eval_ex]
  intro x y _ _
  exact ⟨add x y, by simp⟩

lemma zfc_mul_total :
    𝗭𝗙𝗖 ⊢ (“∀ x y, !GodelQ.ZFCArith.domainDef x → !GodelQ.ZFCArith.domainDef y → ∃ z, !mulB z x y” :
      Sentence ℒₛₑₜ) := by
  apply SetTheory.complete.{0}
  intro M _ _ _
  simp only [models_iff]
  simp only [Semiformula.eval_all, LogicalConnective.HomClass.map_imply, Semiformula.eval_substs,
    Semiformula.eval_ex]
  intro x y _ _
  exact ⟨mul x y, by simp⟩

lemma zfc_add_congr : 𝗭𝗙𝗖 ⊢ (“∀ z w x y, !eqB w z → !addB w x y → !addB z x y” : Sentence ℒₛₑₜ) := by
  apply SetTheory.complete.{0}
  intro M _ _ _
  simp only [models_iff]
  simp only [Semiformula.eval_all, LogicalConnective.HomClass.map_imply, Semiformula.eval_substs]
  intro z w x y h hw
  have e : w = z := by simpa using h
  subst e
  simpa using hw

lemma zfc_mul_congr : 𝗭𝗙𝗖 ⊢ (“∀ z w x y, !eqB w z → !mulB w x y → !mulB z x y” : Sentence ℒₛₑₜ) := by
  apply SetTheory.complete.{0}
  intro M _ _ _
  simp only [models_iff]
  simp only [Semiformula.eval_all, LogicalConnective.HomClass.map_imply, Semiformula.eval_substs]
  intro z w x y h hw
  have e : w = z := by simpa using h
  subst e
  simpa using hw

/-- 加法的反向：x 是第 a 个、y 是第 b 个、z 是第 a + b 个数，则 z = x + y。 -/
theorem numF_add_rev (a b : V) :
    Z V ⊢ ∀¹ ∀¹ ∀¹ ((numF a).subst ![#'2] 🡒 (numF b).subst ![#'1] 🡒 (numF (a + b)).subst ![#'0] 🡒
      addF.subst ![#'0, #'2, #'1]) := by
  have hT : Z V ⊢ ∀¹ ∀¹ (domF.subst ![#'1] 🡒 domF.subst ![#'0] 🡒 ∃¹ (addF.subst ![#'0, #'2, #'1])) := by
    simpa [tq_vec_cons, fin1_fun_eq] using internal_provable_of_outer_provable (V := V) zfc_add_total
  have hC : Z V ⊢ ∀¹ ∀¹ ∀¹ ∀¹ (eqF.subst ![#'2, #'3] 🡒 addF.subst ![#'2, #'1, #'0] 🡒
      addF.subst ![#'3, #'1, #'0]) := by
    simpa [tq_vec_cons, fin1_fun_eq] using internal_provable_of_outer_provable (V := V) zfc_add_congr
  apply TProof.all!
  simp [Bootstrapping.Semiformula.free, Bootstrapping.Semiformula.shift_substs,
    Bootstrapping.Semiformula.substs_substs]
  apply TProof.all!
  simp [Bootstrapping.Semiformula.free, Bootstrapping.Semiformula.shift_substs,
    Bootstrapping.Semiformula.substs_substs]
  apply TProof.all!
  simp [Bootstrapping.Semiformula.free, Bootstrapping.Semiformula.shift_substs,
    Bootstrapping.Semiformula.substs_substs]
  apply FiniteContext.deduct'
  apply FiniteContext.deduct
  apply FiniteContext.deduct
  have hDa : Z V ⊢ (numF a).subst ![&'2] 🡒 domF.subst ![&'2] := by
    simpa using TProof.specialize! (numF_dom a) &'2
  have hDb : Z V ⊢ (numF b).subst ![&'1] 🡒 domF.subst ![&'1] := by
    simpa using TProof.specialize! (numF_dom b) &'1
  have hT' : Z V ⊢ domF.subst ![&'2] 🡒 domF.subst ![&'1] 🡒 ∃¹ (addF.subst ![#'0, &'2, &'1]) := by
    simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₂! hT &'1 &'2
  apply exs_elim (FiniteContext.of hT' ⨀ (FiniteContext.of hDa ⨀ FiniteContext.by_axm₂) ⨀
    (FiniteContext.of hDb ⨀ FiniteContext.by_axm₁))
  simp [Bootstrapping.Semiformula.free, Bootstrapping.Semiformula.shift_substs,
    Bootstrapping.Semiformula.substs_substs]
  have hA : Z V ⊢ (numF a).subst ![&'3] 🡒 (numF b).subst ![&'2] 🡒 addF.subst ![&'0, &'3, &'2] 🡒
      (numF (a + b)).subst ![&'0] := by
    simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₃! (numF_add a b) &'0 &'2 &'3
  have hU : Z V ⊢ (numF (a + b)).subst ![&'0] 🡒 (numF (a + b)).subst ![&'1] 🡒 eqF.subst ![&'0, &'1] := by
    simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₂! (numF_uniq (a + b)) &'1 &'0
  have hC' : Z V ⊢ eqF.subst ![&'0, &'1] 🡒 addF.subst ![&'0, &'3, &'2] 🡒 addF.subst ![&'1, &'3, &'2] := by
    simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₄! hC &'2 &'3 &'0 &'1
  exact FiniteContext.of hC' ⨀ (FiniteContext.of hU ⨀ (FiniteContext.of hA ⨀ FiniteContext.nth_axm 3 ⨀
    FiniteContext.by_axm₂ ⨀ FiniteContext.by_axm₀) ⨀ FiniteContext.by_axm₁) ⨀ FiniteContext.by_axm₀

/-- 乘法的反向。 -/
theorem numF_mul_rev (a b : V) :
    Z V ⊢ ∀¹ ∀¹ ∀¹ ((numF a).subst ![#'2] 🡒 (numF b).subst ![#'1] 🡒 (numF (a * b)).subst ![#'0] 🡒
      mulF.subst ![#'0, #'2, #'1]) := by
  have hT : Z V ⊢ ∀¹ ∀¹ (domF.subst ![#'1] 🡒 domF.subst ![#'0] 🡒 ∃¹ (mulF.subst ![#'0, #'2, #'1])) := by
    simpa [tq_vec_cons, fin1_fun_eq] using internal_provable_of_outer_provable (V := V) zfc_mul_total
  have hC : Z V ⊢ ∀¹ ∀¹ ∀¹ ∀¹ (eqF.subst ![#'2, #'3] 🡒 mulF.subst ![#'2, #'1, #'0] 🡒
      mulF.subst ![#'3, #'1, #'0]) := by
    simpa [tq_vec_cons, fin1_fun_eq] using internal_provable_of_outer_provable (V := V) zfc_mul_congr
  apply TProof.all!
  simp [Bootstrapping.Semiformula.free, Bootstrapping.Semiformula.shift_substs,
    Bootstrapping.Semiformula.substs_substs]
  apply TProof.all!
  simp [Bootstrapping.Semiformula.free, Bootstrapping.Semiformula.shift_substs,
    Bootstrapping.Semiformula.substs_substs]
  apply TProof.all!
  simp [Bootstrapping.Semiformula.free, Bootstrapping.Semiformula.shift_substs,
    Bootstrapping.Semiformula.substs_substs]
  apply FiniteContext.deduct'
  apply FiniteContext.deduct
  apply FiniteContext.deduct
  have hDa : Z V ⊢ (numF a).subst ![&'2] 🡒 domF.subst ![&'2] := by
    simpa using TProof.specialize! (numF_dom a) &'2
  have hDb : Z V ⊢ (numF b).subst ![&'1] 🡒 domF.subst ![&'1] := by
    simpa using TProof.specialize! (numF_dom b) &'1
  have hT' : Z V ⊢ domF.subst ![&'2] 🡒 domF.subst ![&'1] 🡒 ∃¹ (mulF.subst ![#'0, &'2, &'1]) := by
    simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₂! hT &'1 &'2
  apply exs_elim (FiniteContext.of hT' ⨀ (FiniteContext.of hDa ⨀ FiniteContext.by_axm₂) ⨀
    (FiniteContext.of hDb ⨀ FiniteContext.by_axm₁))
  simp [Bootstrapping.Semiformula.free, Bootstrapping.Semiformula.shift_substs,
    Bootstrapping.Semiformula.substs_substs]
  have hA : Z V ⊢ (numF a).subst ![&'3] 🡒 (numF b).subst ![&'2] 🡒 mulF.subst ![&'0, &'3, &'2] 🡒
      (numF (a * b)).subst ![&'0] := by
    simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₃! (numF_mul a b) &'0 &'2 &'3
  have hU : Z V ⊢ (numF (a * b)).subst ![&'0] 🡒 (numF (a * b)).subst ![&'1] 🡒 eqF.subst ![&'0, &'1] := by
    simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₂! (numF_uniq (a * b)) &'1 &'0
  have hC' : Z V ⊢ eqF.subst ![&'0, &'1] 🡒 mulF.subst ![&'0, &'3, &'2] 🡒 mulF.subst ![&'1, &'3, &'2] := by
    simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₄! hC &'2 &'3 &'0 &'1
  exact FiniteContext.of hC' ⨀ (FiniteContext.of hU ⨀ (FiniteContext.of hA ⨀ FiniteContext.nth_axm 3 ⨀
    FiniteContext.by_axm₂ ⨀ FiniteContext.by_axm₀) ⨀ FiniteContext.by_axm₁) ⨀ FiniteContext.by_axm₀

/-! ## 项引理 -/

@[simp] lemma subst_eq_self₂ {L : Language} [L.Encodable] [L.LORDefinable]
    (φ : Bootstrapping.Semiformula V L 2) :
    φ.subst ![Bootstrapping.Semiterm.bvar 0, Bootstrapping.Semiterm.bvar 1] = φ :=
  Bootstrapping.Semiformula.subst_eq_self _ _ (by intro i; fin_cases i <;> rfl)

lemma zfc_zero_ex :
    𝗭𝗙𝗖 ⊢ (“∃ z, !GodelQ.ZFCArith.domainDef z ∧ (⊤ → !(funcDef Language.ORing.Func.zero) z)” :
      Sentence ℒₛₑₜ) := by
  apply SetTheory.complete.{0}
  intro M _ _ _
  simp only [models_iff]
  simp [Semiformula.eval_substs]

lemma zfc_zero_ch :
    𝗭𝗙𝗖 ⊢ (“∀ z, (⊤ → !(funcDef Language.ORing.Func.zero) z) → !(numeralF 0) z” : Sentence ℒₛₑₜ) := by
  apply SetTheory.complete.{0}
  intro M _ _ _
  simp only [models_iff]
  simp [Semiformula.eval_substs, eval_num0]

lemma zfc_one_ex :
    𝗭𝗙𝗖 ⊢ (“∃ z, !GodelQ.ZFCArith.domainDef z ∧ (⊤ → !(funcDef Language.ORing.Func.one) z)” :
      Sentence ℒₛₑₜ) := by
  apply SetTheory.complete.{0}
  intro M _ _ _
  simp only [models_iff]
  simp

lemma zfc_one_ch :
    𝗭𝗙𝗖 ⊢ (“∀ z, (⊤ → !(funcDef Language.ORing.Func.one) z) → ∃ y, !(numeralF 0) y ∧ !numStep y z” :
      Sentence ℒₛₑₜ) := by
  apply SetTheory.complete.{0}
  intro M _ _ _
  simp only [models_iff]
  simp [Semiformula.eval_substs, eval_num0, eval_numStep]


section ctxtools
variable {L : Language} [L.Encodable] [L.LORDefinable] {T : InternalTheory V L}

/-- 0 层项提升到 m+1 层：等于提升到 m 层再 bShift。 -/
@[simp] lemma subst_vec0_succ {m : ℕ} (t : Bootstrapping.Term V L) (w : SemitermVec V L 0 (m + 1)) :
    t.subst w = (t.subst (![] : SemitermVec V L 0 m)).bShift := by
  rw [← Bootstrapping.Semiterm.bShift_substs_q, Bootstrapping.Semiterm.bShift_substs_succ]
  congr 1
  funext i; exact i.elim0

lemma of_eq_ctx {Γ : List (Bootstrapping.Formula V L)} {φ ψ : Bootstrapping.Formula V L}
    (h : Γ ⊢[T] φ) (e : φ = ψ) : Γ ⊢[T] ψ := e ▸ h

lemma specialize₂_ctx {Γ : List (Bootstrapping.Formula V L)} {B : Bootstrapping.Semiformula V L 2}
    (h : Γ ⊢[T] ∀¹ ∀¹ B) (s t : Bootstrapping.Term V L) : Γ ⊢[T] B.subst ![s, t] := by
  have h1 := TProof.specialize_with_ctx! h t
  simp only [Bootstrapping.Semiformula.substs_all] at h1
  have h2 := TProof.specialize_with_ctx! h1 s
  simpa [Bootstrapping.Semiformula.substs_substs] using h2

end ctxtools

/-- 二元函数项的刻画（ch）：由子项的存在与刻画，加上数字层的正向计算律。 -/
lemma ch_func2 {n : ℕ} (f : (ℒₒᵣ).Func 2) (v : Fin 2 → ClosedSemiterm ℒₒᵣ n) (w : Fin n → V) (a0 a1 a : V)
    (hfwd : Z V ⊢ ∀¹ ∀¹ ∀¹ ((numF a0).subst ![#'2] 🡒 (numF a1).subst ![#'1] 🡒
      (⌜(arithTrln.func f : Semisentence ℒₛₑₜ 3)⌝ : Bootstrapping.Semiformula V ℒₛₑₜ 3).subst ![#'0, #'2, #'1] 🡒
      (numF a).subst ![#'0]))
    (ex0 : ∀ (Γ : List (Bootstrapping.Formula V ℒₛₑₜ)) (e : Fin n → Bootstrapping.Term V ℒₛₑₜ), NumHyp Γ w e →
      Γ ⊢[Z V] ∃¹ (domF ⋏ veF (v 0) #'0 (fun i ↦ (e i).bShift)))
    (ex1 : ∀ (Γ : List (Bootstrapping.Formula V ℒₛₑₜ)) (e : Fin n → Bootstrapping.Term V ℒₛₑₜ), NumHyp Γ w e →
      Γ ⊢[Z V] ∃¹ (domF ⋏ veF (v 1) #'0 (fun i ↦ (e i).bShift)))
    (ch0 : ∀ (Γ : List (Bootstrapping.Formula V ℒₛₑₜ)) (e : Fin n → Bootstrapping.Term V ℒₛₑₜ)
      (z : Bootstrapping.Term V ℒₛₑₜ), NumHyp Γ w e → Γ ⊢[Z V] veF (v 0) z e 🡒 (numF a0).subst ![z])
    (ch1 : ∀ (Γ : List (Bootstrapping.Formula V ℒₛₑₜ)) (e : Fin n → Bootstrapping.Term V ℒₛₑₜ)
      (z : Bootstrapping.Term V ℒₛₑₜ), NumHyp Γ w e → Γ ⊢[Z V] veF (v 1) z e 🡒 (numF a1).subst ![z])
    (Γ : List (Bootstrapping.Formula V ℒₛₑₜ)) (e : Fin n → Bootstrapping.Term V ℒₛₑₜ)
    (z : Bootstrapping.Term V ℒₛₑₜ) (h : NumHyp Γ w e) :
    Γ ⊢[Z V] veF (Semiterm.func f v) z e 🡒 (numF a).subst ![z] := by
  rw [veF_func2]
  apply FiniteContext.deduct
  apply exs_elim (ex0 _ e (h.weak (by simp)))
  simp [Bootstrapping.Semiformula.free, veF_shift, veF_subst, Bootstrapping.Semiformula.shift_substs,
    ← Bootstrapping.Semiterm.bShift_shift_comm]
  have h1 : NumHyp (List.map Bootstrapping.Semiformula.shift Γ) w (fun i ↦ (e i).shift) := h.lift (by simp)
  apply exs_elim (ex1 _ _ (h1.weak (by simp)))
  simp [Bootstrapping.Semiformula.free, veF_shift, veF_subst, Bootstrapping.Semiformula.shift_substs,
    ← Bootstrapping.Semiterm.bShift_shift_comm]
  have h2 : NumHyp (List.map (Bootstrapping.Semiformula.shift ∘ Bootstrapping.Semiformula.shift) Γ) w
      (fun i ↦ (e i).shift.shift) := by
    simpa using h1.lift (Δ := List.map (Bootstrapping.Semiformula.shift ∘ Bootstrapping.Semiformula.shift) Γ)
      (by simp)
  have hF : Z V ⊢ (numF a0).subst ![&'1] 🡒 (numF a1).subst ![&'0] 🡒
      (⌜(arithTrln.func f : Semisentence ℒₛₑₜ 3)⌝ : Bootstrapping.Semiformula V ℒₛₑₜ 3).subst
        ![z.shift.shift, &'1, &'0] 🡒 (numF a).subst ![z.shift.shift] := by
    simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₃! hfwd z.shift.shift &'0 &'1
  simp only [arithTrln_func] at hF
  refine FiniteContext.of hF ⨀ (ch0 _ _ (&'1) (h2.weak ?_) ⨀ K_right FiniteContext.by_axm₁) ⨀
    (ch1 _ _ (&'0) (h2.weak ?_) ⨀ K_right FiniteContext.by_axm₀) ⨀
    (of_eq_ctx (specialize₂_ctx FiniteContext.by_axm₂ (&'1) (&'0)) ?_ ⨀
      K_intro FiniteContext.by_axm₁ (K_intro FiniteContext.by_axm₀ Entailment.verum))
  · intro x hx; simp [hx]
  · intro x hx; simp [hx]
  · simp [veF_subst, Bootstrapping.Semiformula.substs_substs, Bootstrapping.Semiterm.bShift_substs_succ]

/-- 二元函数项的存在（ex）：取第 a 个数作值，用子项的刻画与数字层的反向计算律。 -/
lemma ex_func2 {n : ℕ} (f : (ℒₒᵣ).Func 2) (v : Fin 2 → ClosedSemiterm ℒₒᵣ n) (w : Fin n → V) (a0 a1 a : V)
    (hrev : Z V ⊢ ∀¹ ∀¹ ∀¹ ((numF a0).subst ![#'2] 🡒 (numF a1).subst ![#'1] 🡒 (numF a).subst ![#'0] 🡒
      (⌜(arithTrln.func f : Semisentence ℒₛₑₜ 3)⌝ : Bootstrapping.Semiformula V ℒₛₑₜ 3).subst ![#'0, #'2, #'1]))
    (ch0 : ∀ (Γ : List (Bootstrapping.Formula V ℒₛₑₜ)) (e : Fin n → Bootstrapping.Term V ℒₛₑₜ)
      (z : Bootstrapping.Term V ℒₛₑₜ), NumHyp Γ w e → Γ ⊢[Z V] veF (v 0) z e 🡒 (numF a0).subst ![z])
    (ch1 : ∀ (Γ : List (Bootstrapping.Formula V ℒₛₑₜ)) (e : Fin n → Bootstrapping.Term V ℒₛₑₜ)
      (z : Bootstrapping.Term V ℒₛₑₜ), NumHyp Γ w e → Γ ⊢[Z V] veF (v 1) z e 🡒 (numF a1).subst ![z])
    (Γ : List (Bootstrapping.Formula V ℒₛₑₜ)) (e : Fin n → Bootstrapping.Term V ℒₛₑₜ) (h : NumHyp Γ w e) :
    Γ ⊢[Z V] ∃¹ (domF ⋏ veF (Semiterm.func f v) #'0 (fun i ↦ (e i).bShift)) := by
  rw [veF_func2]
  apply exs_elim (FiniteContext.of (numF_exists a))
  simp [Bootstrapping.Semiformula.free, veF_shift, veF_subst, Bootstrapping.Semiformula.shift_substs,
    ← Bootstrapping.Semiterm.bShift_shift_comm]
  apply exs_intro _ (&'0)
  simp [veF_shift, veF_subst, Bootstrapping.Semiformula.shift_substs, Bootstrapping.Semiformula.substs_substs,
    ← Bootstrapping.Semiterm.bShift_shift_comm, Bootstrapping.Semiterm.bShift_substs_succ]
  have hD : Z V ⊢ (numF a).subst ![&'0] 🡒 domF.subst ![&'0] := by
    simpa using TProof.specialize! (numF_dom a) &'0
  refine K_intro (FiniteContext.of hD ⨀ FiniteContext.by_axm₀) ?_
  apply TProof.generalize!
  simp [Bootstrapping.Semiformula.free, veF_shift, veF_subst, Bootstrapping.Semiformula.shift_substs,
    Bootstrapping.Semiformula.substs_substs, ← Bootstrapping.Semiterm.bShift_shift_comm,
    Bootstrapping.Semiterm.bShift_substs_succ]
  apply TProof.generalize!
  simp [Bootstrapping.Semiformula.free, veF_shift, veF_subst, Bootstrapping.Semiformula.shift_substs,
    Bootstrapping.Semiformula.substs_substs, ← Bootstrapping.Semiterm.bShift_shift_comm,
    Bootstrapping.Semiterm.bShift_substs_succ]
  apply FiniteContext.deduct
  have h3 : NumHyp (List.map (Bootstrapping.Semiformula.shift ∘ Bootstrapping.Semiformula.shift ∘
      Bootstrapping.Semiformula.shift) Γ) w (fun i ↦ (e i).shift.shift.shift) := by
    have h1 := h.lift (Δ := List.map Bootstrapping.Semiformula.shift Γ) (by simp)
    have h2 := h1.lift (Δ := List.map (Bootstrapping.Semiformula.shift ∘ Bootstrapping.Semiformula.shift) Γ)
      (by simp)
    simpa using h2.lift (Δ := List.map (Bootstrapping.Semiformula.shift ∘ Bootstrapping.Semiformula.shift ∘
      Bootstrapping.Semiformula.shift) Γ) (by simp)
  have hR : Z V ⊢ (numF a0).subst ![&'0] 🡒 (numF a1).subst ![&'1] 🡒 (numF a).subst ![&'2] 🡒
      (⌜(arithTrln.func f : Semisentence ℒₛₑₜ 3)⌝ : Bootstrapping.Semiformula V ℒₛₑₜ 3).subst
        ![&'2, &'0, &'1] := by
    simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₃! hrev &'2 &'1 &'0
  simp only [arithTrln_func] at hR
  refine FiniteContext.of hR ⨀ (ch0 _ _ (&'0) (h3.weak ?_) ⨀ K_right (K_left FiniteContext.by_axm₀)) ⨀
    (ch1 _ _ (&'1) (h3.weak ?_) ⨀ K_right (K_left (K_right FiniteContext.by_axm₀))) ⨀ FiniteContext.by_axm₁
  · intro x hx; simp [hx]
  · intro x hx; simp [hx]

/-- **项引理**：t 的翻译值存在且属于 ω（ex）；任一满足变量等式的值都是第 t(w) 个数（ch）。 -/
theorem term_ve {n : ℕ} : ∀ (t : ClosedSemiterm ℒₒᵣ n) (w : Fin n → V),
    (∀ (Γ : List (Bootstrapping.Formula V ℒₛₑₜ)) (e : Fin n → Bootstrapping.Term V ℒₛₑₜ), NumHyp Γ w e →
      Γ ⊢[Z V] ∃¹ (domF ⋏ veF t #'0 (fun i ↦ (e i).bShift))) ∧
    (∀ (Γ : List (Bootstrapping.Formula V ℒₛₑₜ)) (e : Fin n → Bootstrapping.Term V ℒₛₑₜ)
      (z : Bootstrapping.Term V ℒₛₑₜ), NumHyp Γ w e →
      Γ ⊢[Z V] veF t z e 🡒 (numF (t.valb w)).subst ![z])
  | #i, w => by
    refine ⟨fun Γ e h ↦ ?_, fun Γ e z h ↦ ?_⟩
    · rw [veF_bvar]
      apply exs_intro _ (e i)
      simp [Bootstrapping.Semiformula.substs_substs]
      have hR : Z V ⊢ ∀¹ (eqF.subst ![#'0, #'0]) := by
        simpa [tq_vec_cons, fin1_fun_eq] using internal_provable_of_outer_provable (V := V) zfc_eq_refl
      have hD : Z V ⊢ (numF (w i)).subst ![e i] 🡒 domF.subst ![e i] := by
        simpa using TProof.specialize! (numF_dom (w i)) (e i)
      have hR' : Z V ⊢ eqF.subst ![e i, e i] := by
        simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize! hR (e i)
      exact K_intro (FiniteContext.of hD ⨀ h i) (FiniteContext.of hR')
    · rw [veF_bvar]
      have hv : (#i : ClosedSemiterm ℒₒᵣ n).valb w = w i := by simp
      rw [hv]
      have hSym : Z V ⊢ ∀¹ ∀¹ (eqF.subst ![#'1, #'0] 🡒 eqF.subst ![#'0, #'1]) := by
        simpa [tq_vec_cons, fin1_fun_eq] using internal_provable_of_outer_provable (V := V) zfc_eq_symm
      have h1 : Z V ⊢ eqF.subst ![z, e i] 🡒 eqF.subst ![e i, z] := by
        simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₂! hSym (e i) z
      have h2 : Z V ⊢ eqF.subst ![e i, z] 🡒 (numF (w i)).subst ![e i] 🡒 (numF (w i)).subst ![z] := by
        simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₂! (numF_congr (w i)) z (e i)
      apply FiniteContext.deduct
      exact FiniteContext.of h2 ⨀ (FiniteContext.of h1 ⨀ FiniteContext.by_axm₀) ⨀
        FiniteContext.weakening (by simp) (h i)
  | &x, _ => Empty.elim x
  | .func Language.Zero.zero v, w => by
    refine ⟨fun Γ e h ↦ ?_, fun Γ e z h ↦ ?_⟩
    · rw [veF_func0]
      have := internal_provable_of_outer_provable (V := V) zfc_zero_ex
      simp at this ⊢
      exact FiniteContext.of this
    · rw [veF_func0]
      have := internal_provable_of_outer_provable (V := V) zfc_zero_ch
      simp at this
      have h' := TProof.specialize! this z
      simp [Semiterm.val_func, numF_zero] at h' ⊢
      exact FiniteContext.of h'
  | .func Language.One.one v, w => by
    refine ⟨fun Γ e h ↦ ?_, fun Γ e z h ↦ ?_⟩
    · rw [veF_func0]
      have := internal_provable_of_outer_provable (V := V) zfc_one_ex
      simp at this ⊢
      exact FiniteContext.of this
    · rw [veF_func0]
      have := internal_provable_of_outer_provable (V := V) zfc_one_ch
      simp [tq_vec_cons, fin1_fun_eq] at this
      have h' := TProof.specialize! this z
      have e1 : numF (1 : V) = ∃¹ ((numF 0).subst ![#'0] ⋏ ⌜numStep⌝) := by simpa using numF_succ (0 : V)
      simp [Semiterm.val_func, e1, numF_zero, Bootstrapping.Semiformula.substs_substs] at h' ⊢
      exact FiniteContext.of h'
  | .func Language.Add.add v, w => by
    have ih0 := term_ve (v 0) w
    have ih1 := term_ve (v 1) w
    have hv : (Semiterm.func Language.Add.add v : ClosedSemiterm ℒₒᵣ n).valb w =
        (v 0).valb w + (v 1).valb w := by
      simp [Semiterm.val_func]
    rw [hv]
    exact ⟨fun Γ e h ↦ ex_func2 Language.Add.add v w _ _ _ (numF_add_rev _ _) ih0.2 ih1.2 Γ e h,
      fun Γ e z h ↦ ch_func2 Language.Add.add v w _ _ _ (numF_add _ _) ih0.1 ih1.1 ih0.2 ih1.2 Γ e z h⟩
  | .func Language.Mul.mul v, w => by
    have ih0 := term_ve (v 0) w
    have ih1 := term_ve (v 1) w
    have hv : (Semiterm.func Language.Mul.mul v : ClosedSemiterm ℒₒᵣ n).valb w =
        (v 0).valb w * (v 1).valb w := by
      simp [Semiterm.val_func]
    rw [hv]
    exact ⟨fun Γ e h ↦ ex_func2 Language.Mul.mul v w _ _ _ (numF_mul_rev _ _) ih0.2 ih1.2 Γ e h,
      fun Γ e z h ↦ ch_func2 Language.Mul.mul v w _ _ _ (numF_mul _ _) ih0.1 ih1.1 ih0.2 ih1.2 Γ e z h⟩

end GodelQ.SetNum

#print axioms GodelQ.SetNum.numF_add_rev
#print axioms GodelQ.SetNum.numF_mul_rev
#print axioms GodelQ.SetNum.term_ve
