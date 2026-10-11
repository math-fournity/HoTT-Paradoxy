import GodelQ.ZFC.OmegaLaws
import GodelQ.ZFC.Soundness
import Foundation.FirstOrder.Arithmetic.Schemata

/-!
# CG-007 · W3（二）：每个 𝗭𝗙𝗖 模型的 ω 满足 𝗣𝗔；于是 `𝗭𝗙𝗖 ⊳ 𝗣𝗔`

翻译诱导的算术结构 `N M := arithTrln.Model M`（S3）带着翻译给出的 ℒₒᵣ 解释。为了用 Foundation 对
“标准 ℒₒᵣ 结构”的现成化简，另取类型同义词 `W M := N M`，在它上面放 `ORingStructure`
（0 = ∅，1 = succ ∅，加乘取 ω 上的递归，`<` 取 `∈`），从而得到 Foundation 的 `standardModel`。
恒等双射 `Θ : N M ≃ W M` 保持全部函数与关系，于是两者满足同样的公式（`eval_equiv_iff`，S4）。

* `models_PeanoMinus_W`：𝗣𝗔⁻ 的 17 条公理化成 ω 上的算术律，由 `OmegaLaws` 支付。
* `models_succInd_W`：任一算术公式（带参数）的归纳实例成立。φ 在 ω 上定义的子集由 φ 的翻译在 M 中定义，
  于是经 Foundation 的 `naturalNumber_induction`（ω 是最小的归纳集，归纳谓词经分离取成集合）得到。
* `models_PA`：`(N M) ⊧* 𝗣𝗔`；`paInterp : 𝗭𝗙𝗖 ⊳ 𝗣𝗔`。
-/

namespace GodelQ.ZFCArith

open FFL FFL.FirstOrder FFL.FirstOrder.SetTheory FFL.FirstOrder.Arithmetic

variable {M : Type*} [SetStructure M] [Nonempty M] [M↓[ℒₛₑₜ] ⊧* 𝗭𝗙𝗖]

/-- ω 的算术结构，取标准的 ℒₒᵣ 解释（类型同义词，与 `N M` 的翻译解释分开）。 -/
def W (M : Type*) [SetStructure M] := N M

noncomputable instance : ORingStructure (W M) where
  zero := (toN ∅ (by simp) : N M)
  one := (toN (SetTheory.succ ∅) (ω_succ_closed (by simp)) : N M)
  add a b := (toN (add (a : N M).val (b : N M).val)
    (add_mem_ω (val_mem_ω (a : N M)) (val_mem_ω (b : N M))) : N M)
  mul a b := (toN (mul (a : N M).val (b : N M).val)
    (mul_mem_ω (val_mem_ω (a : N M)) (val_mem_ω (b : N M))) : N M)
  lt a b := (a : N M).val ∈ (b : N M).val

/-- `W M` 中的元素回到 M。 -/
def wval (a : W M) : M := (a : N M).val

lemma wval_mem_ω (a : W M) : wval a ∈ (ω : M) := val_mem_ω (a : N M)

@[simp] lemma wval_zero : wval (0 : W M) = 0 := rfl
@[simp] lemma wval_one : wval (1 : W M) = SetTheory.succ 0 := rfl
@[simp] lemma wval_add (a b : W M) : wval (a + b) = add (wval a) (wval b) := rfl
@[simp] lemma wval_mul (a b : W M) : wval (a * b) = mul (wval a) (wval b) := rfl
lemma lt_iff_wval (a b : W M) : a < b ↔ wval a ∈ wval b := Iff.rfl

omit [Nonempty M] [M↓[ℒₛₑₜ] ⊧* 𝗭𝗙𝗖] in
lemma wext {a b : W M} (h : wval a = wval b) : a = b :=
  DirectTranslation.Model.ext (M := M) (π := arithTrln) h

lemma exists_W {x : M} (hx : x ∈ (ω : M)) : ∃ a : W M, wval a = x := ⟨(toN x hx : N M), rfl⟩

/-! ## 𝗣𝗔⁻ -/

set_option linter.flexible false in
instance models_PeanoMinus_W : (W M)↓[ℒₒᵣ] ⊧* 𝗣𝗔⁻ := ⟨by
  intro σ h
  rcases h <;> simp [models_iff, Semiformula.eval_bexsLTSucc, Tarski.Structure.le_iff_of_eq_of_lt]
  case equal h =>
    have : (W M)↓[ℒₒᵣ] ⊧* (𝗘𝗤 ℒₒᵣ : ArithmeticTheory) := inferInstance
    exact models_theory_iff.mp this _ h
  case addZero => intro a; exact wext (by simp)
  case addAssoc => intro a b c; exact wext (by simp [add_assoc' _ _ (wval_mem_ω c) (wval_mem_ω b)])
  case addComm => intro a b; exact wext (by simp [add_comm' (wval_mem_ω a) (wval_mem_ω b)])
  case addEqOfLt =>
    intro a b hab
    have hb := wval_mem_ω b
    have hsub : wval a ⊆ wval b := fun w hw => lt_trans' hb hw hab
    obtain ⟨z, hzω, hz⟩ := exists_add_of_subset (wval_mem_ω a) hb hsub
    obtain ⟨c, rfl⟩ := exists_W hzω
    refine ⟨c, ?_, wext (by simpa using hz)⟩
    rw [lt_iff_wval, wval_add, wval_one, add_succ _ zero_mem_ω, add_zero]
    have hle : wval c ⊆ wval b := hz ▸ le_add (wval_mem_ω a) hzω
    rcases (subset_iff_eq_or_mem hzω hb).mp hle with h | h
    · exact mem_succ_iff.mpr (Or.inl h)
    · exact mem_succ_iff.mpr (Or.inr h)
  case zeroLe =>
    intro a
    rcases zero_le' (wval_mem_ω a) with h | h
    · exact Or.inl (wext h)
    · exact Or.inr h
  case zeroLtOne => exact (lt_iff_wval _ _).mpr (by simp [zero_def])
  case oneLeOfZeroLt =>
    intro a ha
    rcases (subset_iff_eq_or_mem (ω_succ_closed zero_mem_ω) (wval_mem_ω a)).mp
      (succ_subset_of_mem (wval_mem_ω a) ha) with h | h
    · exact Or.inl (wext h)
    · exact Or.inr h
  case addLtAdd =>
    intro a b c hab
    rw [lt_iff_wval] at hab ⊢
    simp only [wval_add]
    exact add_mem_add (wval_mem_ω _) hab (wval_mem_ω c)
  case mulZero => intro a; exact wext (mul_zero' (wval a))
  case mulOne => intro a; exact wext (mul_one' (wval_mem_ω a))
  case mulAssoc =>
    intro a b c
    exact wext (by simp [mul_assoc' (wval_mem_ω a) (wval_mem_ω b) (wval_mem_ω c)])
  case mulComm => intro a b; exact wext (by simp [mul_comm' (wval_mem_ω a) (wval_mem_ω b)])
  case mulLtMul =>
    intro a b c hab hc
    rw [lt_iff_wval] at hab hc ⊢
    simp only [wval_mul]
    exact mul_mem_mul (wval_mem_ω _) hab (wval_mem_ω c) hc
  case distr =>
    intro a b c
    exact wext (by simp [mul_add' (wval_mem_ω a) (wval_mem_ω b) (wval_mem_ω c)])
  case ltIrrefl => intro a; exact mem_irrefl (wval a)
  case ltTrans => intro a b c hab hbc; exact lt_trans' (wval_mem_ω c) hab hbc
  case ltTri =>
    intro a b
    rcases lt_trichotomy' (wval_mem_ω a) (wval_mem_ω b) with h | h | h
    · exact Or.inl h
    · exact Or.inr (Or.inl (wext h))
    · exact Or.inr (Or.inr h)⟩

/-! ## `N M` 与 `W M` 满足同样的公式 -/

instance : Nonempty (W M) := inferInstanceAs (Nonempty (N M))

/-- 恒等双射：同一个 ω，两种写法的 ℒₒᵣ 解释。 -/
def theta : N M ≃ W M := Equiv.refl _

omit [Nonempty M] [M↓[ℒₛₑₜ] ⊧* 𝗭𝗙𝗖] in
lemma vec2_eta {α : Type*} (v : Fin 2 → α) : v = ![v 0, v 1] :=
  funext fun i ↦ match i with | 0 => rfl | 1 => rfl

omit [Nonempty M] [M↓[ℒₛₑₜ] ⊧* 𝗭𝗙𝗖] in
lemma comp_vec2 {α β : Type*} (g : α → β) (a b : α) : g ∘ ![a, b] = ![g a, g b] :=
  funext fun i ↦ match i with | 0 => rfl | 1 => rfl

lemma theta_func {k} (f : (ℒₒᵣ).Func k) (v : Fin k → N M) :
    theta (Tarski.Structure.func f v) = Tarski.Structure.func (M := W M) f (theta ∘ v) := by
  cases f with
  | zero => rw [func_zero]; rfl
  | one => rw [func_one]; rfl
  | add => rw [vec2_eta v, func_add]; rfl
  | mul => rw [vec2_eta v, func_mul]; rfl

lemma theta_rel {k} (r : (ℒₒᵣ).Rel k) (v : Fin k → W M) :
    Tarski.Structure.rel (M := W M) r v ↔ Tarski.Structure.rel r (theta.symm ∘ v) := by
  cases r with
  | eq =>
    rw [vec2_eta v, comp_vec2, DirectTranslation.Model.rel_iff]
    show (v 0 = v 1) ↔ _
    have hv : (fun i ↦ ((![theta.symm (v 0), theta.symm (v 1)] i : N M) : M)) =
        ![wval (v 0), wval (v 1)] := funext fun i ↦ match i with | 0 => rfl | 1 => rfl
    rw [hv]
    exact ⟨fun h ↦ (eval_relDef_eq (V := M) _ _).mpr (congrArg wval h),
      fun h ↦ wext ((eval_relDef_eq (V := M) _ _).mp h)⟩
  | lt =>
    rw [vec2_eta v, comp_vec2, rel_lt]
    exact Iff.rfl

/-- `W M`（标准解释）与 `N M`（翻译解释）满足同样的公式。 -/
lemma eval_W_iff {ξ : Type*} {n : ℕ} {b : Fin n → W M} {ε : ξ → W M} {φ : Semiformula ℒₒᵣ ξ n} :
    Semiformula.Eval b ε φ ↔ Semiformula.Eval (theta.symm ∘ b) (theta.symm ∘ ε) φ :=
  GodelQ.ZFCSound.eval_equiv_iff theta theta_func theta_rel

lemma models_N_iff (σ : ArithmeticSentence) : (N M)↓[ℒₒᵣ] ⊧ σ ↔ (W M)↓[ℒₒᵣ] ⊧ σ := by
  rw [models_iff, models_iff]
  have h := eval_W_iff (b := (![] : Fin 0 → W M)) (ε := (Empty.elim : Empty → W M)) (φ := σ)
  have hb : (theta.symm ∘ (![] : Fin 0 → W M)) = ![] := funext fun i ↦ i.elim0
  have hε : (theta.symm ∘ (Empty.elim : Empty → W M)) = Empty.elim := funext fun x ↦ x.elim
  rw [hb, hε] at h
  exact h.symm

/-! ## 归纳模式 -/

/-- 算术公式 φ（带参数 f）在 ω 上定义的谓词，用 φ 的翻译写成集合语言里的谓词。 -/
def indPred (φ : Semiformula ℒₒᵣ ℕ 1) (f : ℕ → W M) (y : M) : Prop :=
  y ∈ (ω : M) ∧ Semiformula.Eval ![y] (fun i ↦ wval (f i)) (arithTrln.translate φ)

lemma indPred_iff (φ : Semiformula ℒₒᵣ ℕ 1) (f : ℕ → W M) (a : W M) :
    indPred φ f (wval a) ↔ Semiformula.Eval ![a] f φ := by
  have h1 := DirectTranslation.Model.eval_translate_iff (π := arithTrln) (M := M) (φ := φ)
    (ε := fun i ↦ (f i : N M)) (e := ![(a : N M)])
  have e1 : (fun i : Fin 1 ↦ (((![(a : N M)] : Fin 1 → N M) i : N M) : M)) = ![wval a] :=
    funext fun i ↦ match i with | 0 => rfl
  rw [e1] at h1
  have h2 := eval_W_iff (b := ![a]) (ε := f) (φ := φ)
  have e2 : (theta.symm ∘ (![a] : Fin 1 → W M)) = ![(a : N M)] :=
    funext fun i ↦ match i with | 0 => rfl
  rw [e2] at h2
  constructor
  · rintro ⟨-, h⟩
    exact h2.mpr (h1.mp h)
  · intro h
    exact ⟨wval_mem_ω a, h1.mpr (h2.mp h)⟩

lemma indPred_definable (φ : Semiformula ℒₒᵣ ℕ 1) (f : ℕ → W M) :
    ℒₛₑₜ-predicate (indPred φ f) := by
  refine ⟨⟨domainDef.emb ⋏ (Rew.rewriteMap (fun i ↦ wval (f i)) ▹ arithTrln.translate φ),
    fun v ↦ ?_⟩⟩
  obtain ⟨y, rfl⟩ : ∃ y : M, v = ![y] := ⟨v 0, funext fun i ↦ match i with | 0 => rfl⟩
  simp [indPred, Semiformula.eval_rewriteMap]

/-- **ω 上的归纳**：任一算术公式（带参数）的归纳实例在 `W M` 中成立。 -/
theorem W_induction (φ : Semiformula ℒₒᵣ ℕ 1) (f : ℕ → W M)
    (h0 : Semiformula.Eval ![(0 : W M)] f φ)
    (hs : ∀ x : W M, Semiformula.Eval ![x] f φ → Semiformula.Eval ![x + 1] f φ) :
    ∀ x : W M, Semiformula.Eval ![x] f φ := by
  have key : ∀ y ∈ (ω : M), indPred φ f y := by
    intro y hy
    refine naturalNumber_induction (indPred φ f) ?_ ?_ ?_ y hy
    · exact indPred_definable φ f
    · exact (indPred_iff φ f 0).mpr h0
    · intro y hy ih
      obtain ⟨a, rfl⟩ := exists_W hy
      have h := (indPred_iff φ f (a + 1)).mpr (hs a ((indPred_iff φ f a).mp ih))
      have e : wval (a + 1) = SetTheory.succ (wval a) := by
        rw [wval_add, wval_one, add_succ _ zero_mem_ω, add_zero]
      rwa [e] at h
  intro x
  exact (indPred_iff φ f x).mp (key (wval x) (wval_mem_ω x))

theorem models_succInd_W (φ : Semiformula ℒₒᵣ ℕ 1) : (W M)↓[ℒₒᵣ] ⊧ (succInd φ).univCl := by
  suffices ∀ f : ℕ → W M, Semiformula.Eval ![(0 : W M)] f φ →
      (∀ x, Semiformula.Eval ![x] f φ → Semiformula.Eval ![x + 1] f φ) →
      ∀ x, Semiformula.Eval ![x] f φ by
    simpa [Semiformula.eval_univCl, succInd, models_iff, Matrix.constant_eq_singleton,
      Semiformula.eval_substs]
  intro f h0 hs
  exact W_induction φ f h0 hs

/-! ## 𝗣𝗔 与 `𝗭𝗙𝗖 ⊳ 𝗣𝗔` -/

instance models_PA_W : (W M)↓[ℒₒᵣ] ⊧* 𝗣𝗔 := by
  have : ∀ φ, (W M)↓[ℒₒᵣ] ⊧ (succInd φ).univCl := models_succInd_W
  simp only [Peano, Semantics.ModelsSet.union_iff, models_PeanoMinus_W, true_and, InductionScheme]
  exact Semantics.ModelsSet.setOf_iff.mpr (fun ψ ⟨φ, _, hψ⟩ ↦ hψ ▸ this φ)

/-- **每个 𝗭𝗙𝗖 模型的 ω（翻译解释）满足 𝗣𝗔。** -/
instance models_PA : (N M)↓[ℒₒᵣ] ⊧* 𝗣𝗔 :=
  ⟨fun σ h ↦ (models_N_iff σ).mpr (models_theory_iff.mp (models_PA_W (M := M)) σ h)⟩

end GodelQ.ZFCArith

namespace GodelQ.ZFCArith

open FFL FFL.FirstOrder FFL.FirstOrder.SetTheory FFL.FirstOrder.Arithmetic

set_option warn.classDefReducibility false in
/-- **直接解释：𝗭𝗙𝗖 解释 𝗣𝗔**（同一个翻译 `arithTrln`）。 -/
noncomputable def paInterp : 𝗭𝗙𝗖 ⊳ 𝗣𝗔 where
  trln := arithTrln
  interpret_theory φ hφ := by
    apply SetTheory.complete.{0}
    intro M _ _ _
    exact DirectTranslation.Model.translate_iff.mpr
      (models_theory_iff.mp (models_PA (M := M)) φ hφ)

end GodelQ.ZFCArith

#print axioms GodelQ.ZFCArith.models_PeanoMinus_W
#print axioms GodelQ.ZFCArith.W_induction
#print axioms GodelQ.ZFCArith.models_succInd_W
#print axioms GodelQ.ZFCArith.models_PA
#print axioms GodelQ.ZFCArith.paInterp
