import GodelQ.ZFC.IntLogic

/-!
# 012-Opus · W8：𝗭𝗙𝗖 内部的数字公式（非标准数也可以）

集合语言没有函数符号，一个数 a ∈ V 在 𝗭𝗙𝗖 里只能用公式指称：Rayo 式数字公式
`N_0(z) = ∀u(u ∉ z)`，`N_{a+1}(z) = ∃y(N_a(y) ∧ Succ(z, y))`（`NumeralCode.lean` 的 `numCode`）。
本文件把它做成 V 中的有型公式 `numF a`（a 可以是非标准数），并在 𝗭𝗙𝗖 的内部证明它的基本事实。
-/

namespace GodelQ.SetNum

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment FFL.Entailment.FiniteContext
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCNum GodelQ.ZFCArith GodelQ.IntLogic

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- 𝗭𝗙𝗖 的内部化。 -/
noncomputable abbrev Z (V : Type*) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] : InternalTheory V ℒₛₑₜ :=
  𝗭𝗙𝗖.internalize V

local prefix:max "#'" => Bootstrapping.Semiterm.bvar (V := V) (L := ℒₛₑₜ)
local prefix:max "&'" => Bootstrapping.Semiterm.fvar (V := V) (L := ℒₛₑₜ)

/-! ## 有型的数字公式 -/

/-- 等号块 `x = y`（x = #0，y = #1）。 -/
def eqB : Semisentence ℒₛₑₜ 2 := “x y. x = y”

/-- 属于块 `x ∈ y`（x = #0，y = #1）。 -/
def memB : Semisentence ℒₛₑₜ 2 := “x y. x ∈ y”

noncomputable abbrev eqF : Bootstrapping.Semiformula V ℒₛₑₜ 2 := ⌜eqB⌝

noncomputable abbrev memF : Bootstrapping.Semiformula V ℒₛₑₜ 2 := ⌜memB⌝

section semanticsB

variable {M : Type*} [SetStructure M]

@[simp] lemma eval_eqB (x y : M) : M ⊧/![x, y] eqB ↔ x = y := by simp [eqB]

@[simp] lemma eval_memB (x y : M) : M ⊧/![x, y] memB ↔ x ∈ y := by simp [memB]

end semanticsB

/-- 后继块：`numStep y z`（y = #0，z = #1）说 z = y ∪ {y}。 -/
noncomputable abbrev stepF : Bootstrapping.Semiformula V ℒₛₑₜ 2 := ⌜numStep⌝

lemma stepCode_eq : ((stepCode : ℕ) : V) = (⌜numStep⌝ : V) := Sentence.coe_quote_eq_quote _

lemma num0Code_eq : ((num0Code : ℕ) : V) = (⌜numeralF 0⌝ : V) := Sentence.coe_quote_eq_quote _

/-- 层数 1 的公式码在 `#0 ↦ #0` 的代换下不变（V 层；Foundation 的同名 `subst_eq_self₁` 会解析到 ℕ 层）。 -/
lemma subst_bvar0_self {p : V} (hp : IsSemiformula ℒₛₑₜ 1 p) : subst ℒₛₑₜ (^#0 ∷ 0) p = p :=
  FFL.FirstOrder.Arithmetic.Bootstrapping.subst_eq_self hp (by simp) (by simp)

lemma isSemiformula_numCode (a : V) : IsSemiformula ℒₛₑₜ 1 (numCode a) := by
  induction a using ISigma1.sigma1_succ_induction
  · definability
  case zero => simp [num0Code_eq]
  case succ a ih =>
    have h2 : IsSemiformula ℒₛₑₜ 2 (numCode a) := by
      have := (Bootstrapping.Semiformula.subst ![#'0]
        (⟨numCode a, by simpa using ih⟩ : Bootstrapping.Semiformula V ℒₛₑₜ 1) :
          Bootstrapping.Semiformula V ℒₛₑₜ 2).isSemiformula
      simpa [subst_bvar0_self ih] using this
    rw [numCode_succ, stepCode_eq]
    simp only [IsSemiformula.exs, IsSemiformula.and, one_add_one_eq_two]
    exact ⟨h2, by simpa using Sentence.quote_isSemiformula (V := V) numStep⟩

/-- 数字公式 `N_a(#0)`。 -/
noncomputable def numF (a : V) : Bootstrapping.Semiformula V ℒₛₑₜ 1 :=
  ⟨numCode a, by simpa using isSemiformula_numCode a⟩

@[simp] lemma numF_val (a : V) : (numF a).val = numCode a := rfl

lemma numF_zero : numF (0 : V) = ⌜numeralF 0⌝ := by
  ext; simp [numF, num0Code_eq, Sentence.quote_eq]

lemma numF_succ (a : V) :
    numF (a + 1) = ∃¹ ((numF a).subst ![#'0] ⋏ ⌜numStep⌝) := by
  ext
  simp [numF, numCode_succ, stepCode_eq, subst_bvar0_self (isSemiformula_numCode a), Sentence.quote_eq]

lemma numCode_shift (a : V) : Bootstrapping.shift ℒₛₑₜ (numCode a) = numCode a := by
  induction a using ISigma1.sigma1_succ_induction
  · definability
  case zero =>
    rw [numCode_zero, num0Code_eq, Sentence.quote_eq]
    exact congrArg Bootstrapping.Semiformula.val (tq_shift_sentence (V := V) (numeralF 0))
  case succ a ih =>
    have ihT : (numF a).shift = numF a := by ext; simpa using ih
    have h : (numF (a + 1)).shift = numF (a + 1) := by
      rw [numF_succ]
      simp [Bootstrapping.Semiformula.shift_substs, ihT]
    simpa using congrArg Bootstrapping.Semiformula.val h

@[simp] lemma numF_shift (a : V) : (numF a).shift = numF a := by
  ext; simpa using numCode_shift a

/-! ## 标准句的引号与它的“块”形式 -/

section semantics

variable {M : Type*} [SetStructure M] [Nonempty M] [M↓[ℒₛₑₜ] ⊧* 𝗭]

/-- `numStep y z` 在 𝗭 的模型里说的是 z = y ∪ {y}。 -/
lemma eval_numStep (y z : M) : M ⊧/![y, z] numStep ↔ z = SetTheory.succ y := by
  simp only [numStep]
  simp [Matrix.constant_eq_singleton]
  rw [mem_ext_iff (x := z)]
  simp only [mem_succ_iff]
  exact forall_congr' fun w ↦ by rw [or_comm]

end semantics

/-- 后继存在：`∀y ∃x Succ(x, y)`（`numStep y x`：x = y ∪ {y}）。 -/
lemma zfc_succ_exists : 𝗭𝗙𝗖 ⊢ (“∀ y, ∃ x, !numStep y x” : Sentence ℒₛₑₜ) := by
  apply SetTheory.complete.{0}
  intro M _ _ _
  simp only [models_iff]
  simp [Semiformula.eval_substs, Matrix.comp_vecCons', eval_numStep]

/-- 空集存在：`∃z N_0(z)`。 -/
lemma zfc_num0_exists : 𝗭𝗙𝗖 ⊢ (“∃ z, !(numeralF 0) z” : Sentence ℒₛₑₜ) := by
  apply SetTheory.complete.{0}
  intro M _ _ _
  simp only [models_iff]
  simp [eval_numeralF_iff]

/-! ## 存在：`Z ⊢ ∃x N_a(x)` -/

theorem numF_exists (a : V) : Z V ⊢ ∃¹ numF a := by
  induction a using ISigma1.sigma1_succ_induction
  · simp only [tprovable_iff_provable]; definability
  case zero =>
    rw [numF_zero]
    simpa using internal_provable_of_outer_provable (V := V) zfc_num0_exists
  case succ a ih =>
    rw [numF_succ]
    have hS : Z V ⊢ ∀¹ ∃¹ (stepF.subst ![#'1, #'0]) := by
      simpa [tq_vec_cons, fin1_fun_eq] using internal_provable_of_outer_provable (V := V) zfc_succ_exists
    apply FiniteContext.emptyPrf
    apply exs_elim (FiniteContext.of ih)
    simp only [List.map_nil, Bootstrapping.Semiformula.free, numF_shift]
    have hS' : [(numF a).subst ![&'0]] ⊢[Z V] ∃¹ (stepF.subst ![&'0, #'0]) := by
      have := TProof.specialize! hS &'0
      exact FiniteContext.of (by simpa [Bootstrapping.Semiformula.substs_substs] using this)
    apply exs_elim hS'
    simp [Bootstrapping.Semiformula.free, Bootstrapping.Semiformula.shift_substs,
      Bootstrapping.Semiformula.substs_substs]
    apply exs_intro _ (&'0)
    simp only [Bootstrapping.Semiformula.substs_ex, Bootstrapping.Semiformula.substs_and,
      Bootstrapping.Semiformula.substs_substs]
    simp
    apply exs_intro _ (&'1)
    simp [Bootstrapping.Semiformula.substs_substs]
    exact K_intro FiniteContext.by_axm₁ FiniteContext.by_axm₀

/-! ## 属于 ω：`Z ⊢ ∀x(N_a(x) → x ∈ ω)` -/

/-- 定义域块 `x ∈ ω`。 -/
noncomputable abbrev domF : Bootstrapping.Semiformula V ℒₛₑₜ 1 := ⌜GodelQ.ZFCArith.domainDef⌝

lemma zfc_num0_dom : 𝗭𝗙𝗖 ⊢ (“∀ x, !(numeralF 0) x → !GodelQ.ZFCArith.domainDef x” : Sentence ℒₛₑₜ) := by
  apply SetTheory.complete.{0}
  intro M _ _ _
  simp only [models_iff]
  simp [Semiformula.eval_substs, eval_numeralF_iff, ofNat_mem_ω']

lemma zfc_succ_dom :
    𝗭𝗙𝗖 ⊢ (“∀ x y, !numStep y x → !GodelQ.ZFCArith.domainDef y → !GodelQ.ZFCArith.domainDef x” :
      Sentence ℒₛₑₜ) := by
  apply SetTheory.complete.{0}
  intro M _ _ _
  simp only [models_iff]
  simp only [Semiformula.eval_all, LogicalConnective.HomClass.map_imply, Semiformula.eval_substs]
  intro x y h hy
  have hx : x = SetTheory.succ y := by simpa using (eval_numStep y x).mp (by simpa using h)
  have hy' : y ∈ (ω : M) := by simpa using hy
  simpa [hx] using ω_succ_closed hy'

theorem numF_dom (a : V) : Z V ⊢ ∀¹ (numF a 🡒 domF) := by
  induction a using ISigma1.sigma1_succ_induction
  · simp only [tprovable_iff_provable]; definability
  case zero =>
    rw [numF_zero]
    simpa using internal_provable_of_outer_provable (V := V) zfc_num0_dom
  case succ a ih =>
    have hS : Z V ⊢ ∀¹ ∀¹ (stepF.subst ![#'0, #'1] 🡒 domF.subst ![#'0] 🡒 domF.subst ![#'1]) := by
      simpa [tq_vec_cons, fin1_fun_eq] using internal_provable_of_outer_provable (V := V) zfc_succ_dom
    rw [numF_succ]
    apply TProof.all!
    simp [Bootstrapping.Semiformula.free, Bootstrapping.Semiformula.shift_substs,
      Bootstrapping.Semiformula.substs_substs]
    apply FiniteContext.deduct'
    apply exs_elim FiniteContext.id
    simp [Bootstrapping.Semiformula.free, Bootstrapping.Semiformula.shift_substs,
      Bootstrapping.Semiformula.substs_substs]
    have hy : Z V ⊢ (numF a).subst ![&'0] 🡒 domF.subst ![&'0] := by
      simpa using TProof.specialize! ih &'0
    have hS' : Z V ⊢ stepF.subst ![&'0, &'1] 🡒 domF.subst ![&'0] 🡒 domF.subst ![&'1] := by
      simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₂! hS &'0 &'1
    exact FiniteContext.of hS' ⨀ K_right FiniteContext.by_axm₀ ⨀
      (FiniteContext.of hy ⨀ K_left FiniteContext.by_axm₀)

/-! ## 唯一：`Z ⊢ ∀x y(N_a(x) → N_a(y) → x = y)` -/

lemma zfc_num0_uniq :
    𝗭𝗙𝗖 ⊢ (“∀ x y, !(numeralF 0) x → !(numeralF 0) y → !eqB x y” : Sentence ℒₛₑₜ) := by
  apply SetTheory.complete.{0}
  intro M _ _ _
  simp only [models_iff]
  simp [Semiformula.eval_substs, eval_numeralF_iff]

lemma zfc_succ_uniq :
    𝗭𝗙𝗖 ⊢ (“∀ x y u v, !eqB u v → !numStep u x → !numStep v y → !eqB x y” : Sentence ℒₛₑₜ) := by
  apply SetTheory.complete.{0}
  intro M _ _ _
  simp only [models_iff]
  simp only [Semiformula.eval_all, LogicalConnective.HomClass.map_imply, Semiformula.eval_substs]
  intro x y u v huv hx hy
  have huv' : u = v := by simpa using huv
  have hx' : x = SetTheory.succ u := by simpa using (eval_numStep u x).mp (by simpa using hx)
  have hy' : y = SetTheory.succ v := by simpa using (eval_numStep v y).mp (by simpa using hy)
  simp [hx', hy', huv']

theorem numF_uniq (a : V) :
    Z V ⊢ ∀¹ ∀¹ ((numF a).subst ![#'1] 🡒 (numF a).subst ![#'0] 🡒 eqF.subst ![#'1, #'0]) := by
  induction a using ISigma1.sigma1_succ_induction
  · simp only [tprovable_iff_provable]; definability
  case zero =>
    rw [numF_zero]
    simpa [tq_vec_cons, fin1_fun_eq] using internal_provable_of_outer_provable (V := V) zfc_num0_uniq
  case succ a ih =>
    have hS : Z V ⊢ ∀¹ ∀¹ ∀¹ ∀¹ (eqF.subst ![#'1, #'0] 🡒 stepF.subst ![#'1, #'3] 🡒
        stepF.subst ![#'0, #'2] 🡒 eqF.subst ![#'3, #'2]) := by
      simpa [tq_vec_cons, fin1_fun_eq] using internal_provable_of_outer_provable (V := V) zfc_succ_uniq
    rw [numF_succ]
    apply TProof.all!
    simp [Bootstrapping.Semiformula.free, Bootstrapping.Semiformula.shift_substs,
      Bootstrapping.Semiformula.substs_substs]
    apply TProof.all!
    simp [Bootstrapping.Semiformula.free, Bootstrapping.Semiformula.shift_substs,
      Bootstrapping.Semiformula.substs_substs]
    apply FiniteContext.deduct'
    apply FiniteContext.deduct
    apply exs_elim FiniteContext.by_axm₀
    simp [Bootstrapping.Semiformula.free, Bootstrapping.Semiformula.shift_substs,
      Bootstrapping.Semiformula.substs_substs]
    apply exs_elim FiniteContext.by_axm₂
    simp [Bootstrapping.Semiformula.free, Bootstrapping.Semiformula.shift_substs,
      Bootstrapping.Semiformula.substs_substs]
    have ih' : Z V ⊢ (numF a).subst ![&'0] 🡒 (numF a).subst ![&'1] 🡒 eqF.subst ![&'0, &'1] := by
      simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₂! ih &'1 &'0
    have hS' : Z V ⊢ eqF.subst ![&'0, &'1] 🡒 stepF.subst ![&'0, &'3] 🡒 stepF.subst ![&'1, &'2] 🡒
        eqF.subst ![&'3, &'2] := by
      simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₄! hS &'1 &'0 &'2 &'3
    exact FiniteContext.of hS' ⨀
      (FiniteContext.of ih' ⨀ K_left FiniteContext.by_axm₀ ⨀ K_left FiniteContext.by_axm₁) ⨀
      K_right FiniteContext.by_axm₀ ⨀ K_right FiniteContext.by_axm₁

/-! ## 相合：`Z ⊢ ∀x y(x = y → N_a(x) → N_a(y))`（不归纳，只分 a = 0 与 a = c + 1） -/

lemma zfc_num0_congr :
    𝗭𝗙𝗖 ⊢ (“∀ x y, !eqB x y → !(numeralF 0) x → !(numeralF 0) y” : Sentence ℒₛₑₜ) := by
  apply SetTheory.complete.{0}
  intro M _ _ _
  simp only [models_iff]
  simp only [Semiformula.eval_all, LogicalConnective.HomClass.map_imply, Semiformula.eval_substs]
  intro x y hxy hx
  have e : x = y := by simpa using hxy
  subst e
  simpa using hx

lemma zfc_step_congr :
    𝗭𝗙𝗖 ⊢ (“∀ x y u, !eqB x y → !numStep u x → !numStep u y” : Sentence ℒₛₑₜ) := by
  apply SetTheory.complete.{0}
  intro M _ _ _
  simp only [models_iff]
  simp only [Semiformula.eval_all, LogicalConnective.HomClass.map_imply, Semiformula.eval_substs]
  intro x y u hxy hx
  have e : x = y := by simpa using hxy
  subst e
  simpa using hx

theorem numF_congr (a : V) :
    Z V ⊢ ∀¹ ∀¹ (eqF.subst ![#'1, #'0] 🡒 (numF a).subst ![#'1] 🡒 (numF a).subst ![#'0]) := by
  rcases zero_or_succ a with (rfl | ⟨c, rfl⟩)
  · rw [numF_zero]
    simpa [tq_vec_cons, fin1_fun_eq] using internal_provable_of_outer_provable (V := V) zfc_num0_congr
  · have hS : Z V ⊢ ∀¹ ∀¹ ∀¹ (eqF.subst ![#'2, #'1] 🡒 stepF.subst ![#'0, #'2] 🡒
        stepF.subst ![#'0, #'1]) := by
      simpa [tq_vec_cons, fin1_fun_eq] using internal_provable_of_outer_provable (V := V) zfc_step_congr
    rw [numF_succ]
    apply TProof.all!
    simp [Bootstrapping.Semiformula.free, Bootstrapping.Semiformula.shift_substs,
      Bootstrapping.Semiformula.substs_substs]
    apply TProof.all!
    simp [Bootstrapping.Semiformula.free, Bootstrapping.Semiformula.shift_substs,
      Bootstrapping.Semiformula.substs_substs]
    apply FiniteContext.deduct'
    apply FiniteContext.deduct
    apply exs_elim FiniteContext.by_axm₀
    simp [Bootstrapping.Semiformula.free, Bootstrapping.Semiformula.shift_substs,
      Bootstrapping.Semiformula.substs_substs]
    apply exs_intro _ (&'0)
    simp [Bootstrapping.Semiformula.substs_substs]
    have hS' : Z V ⊢ eqF.subst ![&'2, &'1] 🡒 stepF.subst ![&'0, &'2] 🡒 stepF.subst ![&'0, &'1] := by
      simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₃! hS &'0 &'1 &'2
    exact K_intro (K_left FiniteContext.by_axm₀)
      (FiniteContext.of hS' ⨀ FiniteContext.by_axm₂ ⨀ K_right FiniteContext.by_axm₀)

end GodelQ.SetNum

#print axioms GodelQ.SetNum.numF_succ
#print axioms GodelQ.SetNum.numF_exists
#print axioms GodelQ.SetNum.numF_dom
#print axioms GodelQ.SetNum.numF_uniq
#print axioms GodelQ.SetNum.numF_congr
