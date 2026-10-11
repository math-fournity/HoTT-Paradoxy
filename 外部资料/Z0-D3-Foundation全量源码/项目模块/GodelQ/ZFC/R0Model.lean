import GodelQ.ZFC.ArithInterp
import Foundation.FirstOrder.Arithmetic.R0.Basic

/-!
# CG-006 · S3c：𝗥₀ 在每个 ZFC 模型的 ω 上成立，`𝗭𝗙𝗖 ⊳ 𝗥₀`

对 `M ⊧ 𝗭𝗙𝗖`，翻译诱导的算术结构 `N M := arithTrln.Model M`（ω 上的加乘）满足 𝗥₀；由
`SetTheory.complete` 与 `translate_iff` 得到直接解释 `arithInterp : 𝗭𝗙𝗖 ⊳ 𝗥₀`。
-/

namespace GodelQ.ZFCArith

open FFL FFL.FirstOrder FFL.FirstOrder.SetTheory

variable {M : Type*} [SetStructure M] [Nonempty M] [M↓[ℒₛₑₜ] ⊧* 𝗭𝗙𝗖]

/-- 翻译诱导的算术结构（ω 上的加乘）。 -/
abbrev N (M : Type*) [SetStructure M] := arithTrln.Model M

lemma dom_iff_mem_ω (x : M) : arithTrln.Dom x ↔ x ∈ (ω : M) := eval_domainDef x

/-- ω 中的元素作为解释结构的元素。 -/
def toN (x : M) (hx : x ∈ (ω : M)) : N M := ⟨x, (dom_iff_mem_ω x).mpr hx⟩

lemma val_mem_ω (a : N M) : a.val ∈ (ω : M) := (dom_iff_mem_ω _).mp a.dom

@[simp] lemma toN_val (x : M) (hx : x ∈ (ω : M)) : (toN x hx).val = x := rfl

omit [Nonempty M] [M↓[ℒₛₑₜ] ⊧* 𝗭𝗙𝗖] in
lemma vec2_eq (y : M) (a b : N M) :
    (y :> fun i => ((![a, b] i : N M) : M)) = ![y, a.val, b.val] :=
  funext fun i => match i with | 0 => rfl | 1 => rfl | 2 => rfl

lemma func_zero (v : Fin 0 → N M) :
    Tarski.Structure.func (L := ℒₒᵣ) Language.ORing.Func.zero v = toN ∅ (by simp) := by
  symm
  apply (DirectTranslation.Model.func_iff).mpr
  have hv : ((toN (∅ : M) (by simp)).val :> fun i => ((v i : N M) : M)) = ![(∅ : M)] :=
    funext fun i => by obtain rfl : i = 0 := Subsingleton.elim i 0; rfl
  rw [hv]
  exact (eval_funcDef_zero (V := M) ∅).mpr rfl

lemma func_one (v : Fin 0 → N M) :
    Tarski.Structure.func (L := ℒₒᵣ) Language.ORing.Func.one v =
      toN (SetTheory.succ ∅) (ω_succ_closed (by simp)) := by
  symm
  apply (DirectTranslation.Model.func_iff).mpr
  have hv : ((toN (SetTheory.succ (∅ : M)) (ω_succ_closed (by simp))).val :>
      fun i => ((v i : N M) : M)) = ![SetTheory.succ (∅ : M)] :=
    funext fun i => by obtain rfl : i = 0 := Subsingleton.elim i 0; rfl
  rw [hv]
  exact (eval_funcDef_one (V := M) _).mpr rfl

lemma func_add (a b : N M) :
    Tarski.Structure.func (L := ℒₒᵣ) Language.ORing.Func.add ![a, b] =
      toN (add a.val b.val) (add_mem_ω (val_mem_ω a) (val_mem_ω b)) := by
  symm
  apply (DirectTranslation.Model.func_iff).mpr
  rw [toN_val, vec2_eq]
  exact (eval_funcDef_add (V := M) _ _ _).mpr rfl

lemma func_mul (a b : N M) :
    Tarski.Structure.func (L := ℒₒᵣ) Language.ORing.Func.mul ![a, b] =
      toN (mul a.val b.val) (mul_mem_ω (val_mem_ω a) (val_mem_ω b)) := by
  symm
  apply (DirectTranslation.Model.func_iff).mpr
  rw [toN_val, vec2_eq]
  exact (eval_funcDef_mul (V := M) _ _ _).mpr rfl

lemma rel_lt (a b : N M) :
    Tarski.Structure.rel (L := ℒₒᵣ) Language.ORing.Rel.lt ![a, b] ↔ a.val ∈ b.val := by
  rw [DirectTranslation.Model.rel_iff]
  have hv : (fun i => ((![a, b] i : N M) : M)) = ![a.val, b.val] :=
    funext fun i => match i with | 0 => rfl | 1 => rfl
  rw [hv]
  exact eval_relDef_lt (V := M) _ _

/-! ## 运算子与数字项的值 -/

lemma bvar_vec2 (a b : N M) :
    (Semiterm.val (L := ℒₒᵣ) (ξ := Empty) ![a, b] Empty.elim ∘ Semiterm.bvar) = ![a, b] :=
  funext fun i => match i with | 0 => rfl | 1 => rfl

lemma opval_zero : Semiterm.Operator.val (M := N M) ![]
    (Semiterm.Operator.Zero.zero : Semiterm.Const ℒₒᵣ) = toN ∅ (by simp) := by
  simp only [Semiterm.Operator.val, Semiterm.Operator.Zero.term_eq, Semiterm.val_func]
  exact func_zero _

lemma opval_one : Semiterm.Operator.val (M := N M) ![]
    (Semiterm.Operator.One.one : Semiterm.Const ℒₒᵣ) =
      toN (SetTheory.succ ∅) (ω_succ_closed (by simp)) := by
  simp only [Semiterm.Operator.val, Semiterm.Operator.One.term_eq, Semiterm.val_func]
  exact func_one _

lemma opval_add (a b : N M) : Semiterm.Operator.val ![a, b]
    (Semiterm.Operator.Add.add : Semiterm.Operator ℒₒᵣ 2) =
      toN (add a.val b.val) (add_mem_ω (val_mem_ω a) (val_mem_ω b)) := by
  simp only [Semiterm.Operator.val, Semiterm.Operator.Add.term_eq, Semiterm.val_func]
  rw [bvar_vec2]
  exact func_add a b

lemma opval_mul (a b : N M) : Semiterm.Operator.val ![a, b]
    (Semiterm.Operator.Mul.mul : Semiterm.Operator ℒₒᵣ 2) =
      toN (mul a.val b.val) (mul_mem_ω (val_mem_ω a) (val_mem_ω b)) := by
  simp only [Semiterm.Operator.val, Semiterm.Operator.Mul.term_eq, Semiterm.val_func]
  rw [bvar_vec2]
  exact func_mul a b

lemma opval_lt (a b : N M) : Semiformula.Operator.val ![a, b]
    (Semiformula.Operator.LT.lt : Semiformula.Operator ℒₒᵣ 2) ↔ a.val ∈ b.val := by
  simp only [Semiformula.Operator.val, Semiformula.Operator.LT.sentence_eq, Semiformula.eval_rel]
  rw [bvar_vec2]
  exact rel_lt a b

lemma val_numeral (n : ℕ) : Semiterm.Operator.val (M := N M) ![]
    (Semiterm.Operator.numeral ℒₒᵣ n) = toN (ofNat n) (ofNat_mem_ω' n) := by
  match n with
  | 0 => rw [Semiterm.Operator.numeral_zero, opval_zero]; rfl
  | 1 => rw [Semiterm.Operator.numeral_one, opval_one]; rfl
  | k + 2 =>
    rw [Semiterm.Operator.numeral_add_two, Semiterm.Operator.val_comp]
    have h1 : (Semiterm.Operator.val (M := N M) ![] ∘
        ![Semiterm.Operator.numeral ℒₒᵣ (k + 1), (Semiterm.Operator.One.one : Semiterm.Const ℒₒᵣ)])
        = ![Semiterm.Operator.val ![] (Semiterm.Operator.numeral ℒₒᵣ (k + 1)),
            Semiterm.Operator.val ![] (Semiterm.Operator.One.one : Semiterm.Const ℒₒᵣ)] :=
      funext fun i => match i with | 0 => rfl | 1 => rfl
    rw [h1, val_numeral (k + 1), opval_one, opval_add]
    apply DirectTranslation.Model.ext
    show add (ofNat (k + 1) : M) (SetTheory.succ ∅) = ofNat (k + 2)
    exact add_ofNat (k + 1) 1

/-! ## 𝗥₀ 在解释结构上成立 -/

lemma models_Ω₁ (n m : ℕ) : (N M)↓[ℒₒᵣ] ⊧ (“↑n + ↑m = ↑(n + m)” : ArithmeticSentence) := by
  simp only [models_iff, Semiformula.eval_operator, Semiterm.val_operator, Function.comp_def]
  simp [val_numeral, opval_add]
  apply DirectTranslation.Model.ext
  exact add_ofNat n m

lemma models_Ω₂ (n m : ℕ) : (N M)↓[ℒₒᵣ] ⊧ (“↑n * ↑m = ↑(n * m)” : ArithmeticSentence) := by
  simp only [models_iff, Semiformula.eval_operator, Semiterm.val_operator, Function.comp_def]
  simp [val_numeral, opval_mul]
  apply DirectTranslation.Model.ext
  exact mul_ofNat n m

lemma models_Ω₃ (n : ℕ) :
    (N M)↓[ℒₒᵣ] ⊧ (“∀ x, x < ↑n ↔ ⋁ i < n, x = ↑i” : ArithmeticSentence) := by
  simp [models_iff]
  intro x
  rw [val_numeral, opval_lt]
  simp only [val_numeral, toN_val]
  rw [mem_ofNat_iff]
  constructor
  · rintro ⟨i, hi, h⟩; exact ⟨i, hi, DirectTranslation.Model.ext h⟩
  · rintro ⟨i, hi, rfl⟩; exact ⟨i, hi, rfl⟩

instance models_R0 : (N M)↓[ℒₒᵣ] ⊧* 𝗥₀ := ⟨by
  intro σ h
  rcases h with ⟨φ, hφ⟩ | ⟨n, m⟩ | ⟨n, m⟩ | n
  · have : (N M)↓[ℒₒᵣ] ⊧* (𝗘𝗤 ℒₒᵣ : ArithmeticTheory) := inferInstance
    exact models_theory_iff.mp this _ hφ
  · exact models_Ω₁ n m
  · exact models_Ω₂ n m
  · exact models_Ω₃ n⟩

end GodelQ.ZFCArith

namespace GodelQ.ZFCArith

open FFL FFL.FirstOrder FFL.FirstOrder.SetTheory

/-- 直接解释：𝗭𝗙𝗖 解释 𝗥₀。 -/
noncomputable def arithInterp : 𝗭𝗙𝗖 ⊳ 𝗥₀ where
  trln := arithTrln
  interpret_theory φ hφ := by
    apply SetTheory.complete.{0}
    intro M _ _ _
    exact DirectTranslation.Model.translate_iff.mpr
      (models_theory_iff.mp (models_R0 (M := M)) φ hφ)

end GodelQ.ZFCArith

#print axioms GodelQ.ZFCArith.func_add
#print axioms GodelQ.ZFCArith.rel_lt
#print axioms GodelQ.ZFCArith.val_numeral
#print axioms GodelQ.ZFCArith.opval_lt
#print axioms GodelQ.ZFCArith.models_R0
#print axioms GodelQ.ZFCArith.arithInterp
