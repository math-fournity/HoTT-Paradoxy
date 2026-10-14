import GodelQ.ZFC.Z0Full

/-!
# 012-Opus · W8：内部推理的小工具

Foundation 的有型内部证明系统（`TProof`、`FiniteContext`）对任意语言都可用。本文件补几条
D3 施工反复要用、Foundation 没有现成给出的推理规则：上下文中的 ∃ 引入与 ∃ 消去，以及把
“标准句的有型引号”化成“块的代换”这一标准形的 simp 引理。
-/

namespace GodelQ.IntLogic

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment FFL.Entailment.FiniteContext
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

variable {L : Language} [L.Encodable] [L.LORDefinable]

/-! ## 自由变量编号的数字规范化（`shift` 产生 `1 + 1` 之类） -/

@[simp] lemma one_add_one_V : (1 : V) + 1 = 2 := one_add_one_eq_two

@[simp] lemma two_add_one_V : (2 : V) + 1 = 3 := two_add_one_eq_three

@[simp] lemma three_add_one_V : (3 : V) + 1 = 4 := by norm_num

@[simp] lemma four_add_one_V : (4 : V) + 1 = 5 := by norm_num

@[simp] lemma five_add_one_V : (5 : V) + 1 = 6 := by norm_num

/-! ## 标准句的有型引号：块的代换 -/

/-- 闭项代换与有型引号交换：`⌜σ ⇜ w⌝ = ⌜σ⌝.subst ⌜w⌝`。 -/
@[simp] lemma tq_substs {k m : ℕ} (σ : Semisentence L k) (w : Fin k → ClosedSemiterm L m) :
    (⌜(σ ⇜ w : Semisentence L m)⌝ : Bootstrapping.Semiformula V L m) =
      (⌜σ⌝ : Bootstrapping.Semiformula V L k).subst (fun i ↦ ⌜w i⌝) := by
  rw [Sentence.typed_quote_def, Rewriting.emb_subst_eq_subst_emb, Semiformula.typed_quote_substs,
    Sentence.typed_quote_def]
  rfl

/-- 句子（无自由变量）的有型引号在 `shift` 下不变。 -/
@[simp] lemma tq_shift_sentence {n : ℕ} (σ : Semisentence L n) :
    (⌜σ⌝ : Bootstrapping.Semiformula V L n).shift = ⌜σ⌝ := by
  ext
  simp only [Bootstrapping.Semiformula.val_shift]
  rw [← Sentence.quote_eq, Sentence.quote_def, ← Semiformula.quote_shift]
  congr 1
  unfold Rewriting.emb Rewriting.shift
  rw [← TransitiveRewriting.comp_app]
  congr 2
  ext x
  · simp
  · exact x.elim

/-- 有型引号穿过向量的 cons。 -/
lemma tq_vec_cons {k m : ℕ} (t : ClosedSemiterm L m) (v : Fin k → ClosedSemiterm L m) :
    (fun i ↦ (⌜(t :> v) i⌝ : Bootstrapping.Semiterm V L m)) = ⌜t⌝ :> fun i ↦ ⌜v i⌝ := by
  funext i; cases i using Fin.cases <;> simp

/-- Fin 1 上的常函数就是单元素向量。 -/
lemma fin1_fun_eq {α : Type*} (b : α) : (fun _ : Fin 1 ↦ b) = ![b] := by
  funext i; fin_cases i; rfl

@[simp] lemma q_one {k : ℕ} (w : SemitermVec V L 1 k) : w.q 1 = (w 0).bShift :=
  SemitermVec.q_succ w 0

@[simp] lemma q_two_one {k : ℕ} (w : SemitermVec V L 2 k) : w.q 1 = (w 0).bShift :=
  SemitermVec.q_succ w 0

@[simp] lemma q_two_two {k : ℕ} (w : SemitermVec V L 2 k) : w.q 2 = (w 1).bShift :=
  SemitermVec.q_succ w 1

@[simp] lemma q_three_one {k : ℕ} (w : SemitermVec V L 3 k) : w.q 1 = (w 0).bShift :=
  SemitermVec.q_succ w 0

@[simp] lemma q_three_two {k : ℕ} (w : SemitermVec V L 3 k) : w.q 2 = (w 1).bShift :=
  SemitermVec.q_succ w 1

@[simp] lemma q_three_three {k : ℕ} (w : SemitermVec V L 3 k) : w.q 3 = (w 2).bShift :=
  SemitermVec.q_succ w 2

@[simp] lemma q_four_one {k : ℕ} (w : SemitermVec V L 4 k) : w.q 1 = (w 0).bShift :=
  SemitermVec.q_succ w 0

@[simp] lemma q_four_two {k : ℕ} (w : SemitermVec V L 4 k) : w.q 2 = (w 1).bShift :=
  SemitermVec.q_succ w 1

@[simp] lemma q_four_three {k : ℕ} (w : SemitermVec V L 4 k) : w.q 3 = (w 2).bShift :=
  SemitermVec.q_succ w 2

@[simp] lemma q_four_four {k : ℕ} (w : SemitermVec V L 4 k) : w.q 4 = (w 3).bShift :=
  SemitermVec.q_succ w 3

@[simp] lemma q_five_one {k : ℕ} (w : SemitermVec V L 5 k) : w.q 1 = (w 0).bShift :=
  SemitermVec.q_succ w 0

@[simp] lemma q_five_two {k : ℕ} (w : SemitermVec V L 5 k) : w.q 2 = (w 1).bShift :=
  SemitermVec.q_succ w 1

@[simp] lemma q_five_three {k : ℕ} (w : SemitermVec V L 5 k) : w.q 3 = (w 2).bShift :=
  SemitermVec.q_succ w 2

@[simp] lemma q_five_four {k : ℕ} (w : SemitermVec V L 5 k) : w.q 4 = (w 3).bShift :=
  SemitermVec.q_succ w 3

@[simp] lemma q_five_five {k : ℕ} (w : SemitermVec V L 5 k) : w.q 5 = (w 4).bShift :=
  SemitermVec.q_succ w 4

@[simp] lemma q_six_one {k : ℕ} (w : SemitermVec V L 6 k) : w.q 1 = (w 0).bShift :=
  SemitermVec.q_succ w 0

@[simp] lemma q_six_two {k : ℕ} (w : SemitermVec V L 6 k) : w.q 2 = (w 1).bShift :=
  SemitermVec.q_succ w 1

@[simp] lemma q_six_three {k : ℕ} (w : SemitermVec V L 6 k) : w.q 3 = (w 2).bShift :=
  SemitermVec.q_succ w 2

@[simp] lemma q_six_four {k : ℕ} (w : SemitermVec V L 6 k) : w.q 4 = (w 3).bShift :=
  SemitermVec.q_succ w 3

@[simp] lemma q_six_five {k : ℕ} (w : SemitermVec V L 6 k) : w.q 5 = (w 4).bShift :=
  SemitermVec.q_succ w 4

@[simp] lemma q_six_six {k : ℕ} (w : SemitermVec V L 6 k) : w.q 6 = (w 5).bShift :=
  SemitermVec.q_succ w 5

@[simp] lemma q_single {k : ℕ} (t : Bootstrapping.Semiterm V L k) :
    (SemitermVec.q ![t] : SemitermVec V L 2 (k + 1)) = ![Bootstrapping.Semiterm.bvar 0, t.bShift] := by
  funext i; fin_cases i <;> rfl

/-! ## 空量词：把 0 层公式提升到 1 层（不含 #0） -/

/-- `χ` 提升到 1 层，不出现 #0。 -/
noncomputable abbrev lift (χ : Bootstrapping.Formula V L) : Bootstrapping.Semiformula V L 1 :=
  χ.subst ![]

lemma vec_nil_eq {n : ℕ} (w : Fin 0 → Bootstrapping.Semiterm V L n) : w = ![] := by
  funext i; exact i.elim0

lemma lift_free (χ : Bootstrapping.Formula V L) : (lift χ).free = χ.shift := by
  simp only [lift, Bootstrapping.Semiformula.free, Bootstrapping.Semiformula.shift_substs,
    Bootstrapping.Semiformula.substs_substs]
  exact Bootstrapping.Semiformula.subst_nil_eq_self _ _

/-! ## 上下文中的 ∃ 引入与 ∃ 消去 -/

variable {T : InternalTheory V L}

/-- `φ(t) 🡒 ∃x φ(x)`。 -/
lemma exs_of_inst (φ : Bootstrapping.Semiformula V L 1) (t : Bootstrapping.Term V L) :
    T ⊢ φ.subst ![t] 🡒 ∃¹ φ := by
  refine ⟨?_⟩
  show T ⊢!ᵈᵉʳ insert (φ.subst ![t] 🡒 ∃¹ φ) ∅
  rw [Bootstrapping.Semiformula.imp_def]
  apply TDerivation.or
  apply TDerivation.rotate₁
  apply TDerivation.exs t
  exact TDerivation.em (φ.subst ![t])

open Classical in
/-- 上下文中的 ∃ 引入。 -/
lemma exs_intro {Γ : List (Bootstrapping.Formula V L)} (φ : Bootstrapping.Semiformula V L 1)
    (t : Bootstrapping.Term V L) (h : Γ ⊢[T] φ.subst ![t]) : Γ ⊢[T] ∃¹ φ :=
  FiniteContext.of (exs_of_inst φ t) ⨀ h

open Classical in
/-- 上下文中的 ∃ 消去：由 `Γ ⊢ ∃x φ(x)` 与 `φ(&0), Γ↑ ⊢ χ↑` 得 `Γ ⊢ χ`。 -/
lemma exs_elim {Γ : List (Bootstrapping.Formula V L)} {φ : Bootstrapping.Semiformula V L 1}
    {χ : Bootstrapping.Formula V L} (h₁ : Γ ⊢[T] ∃¹ φ)
    (h₂ : (φ.free :: Γ.map Bootstrapping.Semiformula.shift) ⊢[T] χ.shift) : Γ ⊢[T] χ := by
  have hA : Γ ⊢[T] ∀¹ (∼lift χ) 🡒 ∀¹ (∼φ) := by
    apply TProof.all_imp_all!
    have : Γ.map Bootstrapping.Semiformula.shift ⊢[T] φ.free 🡒 χ.shift := deduct h₂
    have e1 : (∼lift χ).free = ∼χ.shift := by
      rw [← lift_free]; simp [Bootstrapping.Semiformula.free]
    have e2 : (∼φ).free = ∼φ.free := by simp [Bootstrapping.Semiformula.free]
    rw [e1, e2]
    exact Entailment.contra this
  have hB : Γ ⊢[T] ∼χ 🡒 ∀¹ (∼lift χ) := by
    apply deduct
    apply TProof.generalize!
    have e1 : (∼lift χ).free = ∼χ.shift := by
      rw [← lift_free]; simp [Bootstrapping.Semiformula.free]
    rw [e1]
    simpa using (FiniteContext.by_axm (by simp) :
      ((∼χ).shift :: Γ.map Bootstrapping.Semiformula.shift) ⊢[T] (∼χ).shift)
  have hC : Γ ⊢[T] ∼χ 🡒 ∼(∃¹ φ) := by
    have : Γ ⊢[T] ∼χ 🡒 ∀¹ (∼φ) := Entailment.C_trans hB hA
    simpa using this
  exact Entailment.of_NN (Entailment.contra hC ⨀ (Entailment.dni' h₁))

end GodelQ.IntLogic

#print axioms GodelQ.IntLogic.exs_intro
#print axioms GodelQ.IntLogic.exs_elim
