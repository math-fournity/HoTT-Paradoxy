import GodelQ.ZFC.SetNum

/-!
# 012-Opus · W8：𝗭𝗙𝗖 内部的数字算术（非标准数也可以）

加法、乘法、小于：对 V 中任意的 a、b，`Z ⊢` “若 x 是第 a 个数、y 是第 b 个数，则 x + y 是第 a + b 个数”，
等等。加法与乘法用的是翻译所用的 ω 上递归定义（`ArithInterp.funcDef`）。证明在 V 中归纳；
每一步用到的“一致的”集合论事实都是标准 𝗭𝗙𝗖 句，在模型里证明，再搬进 V。
-/

namespace GodelQ.SetNum

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment FFL.Entailment.FiniteContext
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCNum GodelQ.ZFCArith GodelQ.IntLogic

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

local prefix:max "#'" => Bootstrapping.Semiterm.bvar (V := V) (L := ℒₛₑₜ)
local prefix:max "&'" => Bootstrapping.Semiterm.fvar (V := V) (L := ℒₛₑₜ)

/-- 加法块 `z = x + y`（z = #0，x = #1，y = #2）。 -/
def addB : Semisentence ℒₛₑₜ 3 := funcDef Language.ORing.Func.add

/-- 乘法块 `z = x · y`（z = #0，x = #1，y = #2）。 -/
def mulB : Semisentence ℒₛₑₜ 3 := funcDef Language.ORing.Func.mul

noncomputable abbrev addF : Bootstrapping.Semiformula V ℒₛₑₜ 3 := ⌜addB⌝

noncomputable abbrev mulF : Bootstrapping.Semiformula V ℒₛₑₜ 3 := ⌜mulB⌝

section semantics

variable {M : Type*} [SetStructure M] [Nonempty M] [M↓[ℒₛₑₜ] ⊧* 𝗭]

@[simp] lemma eval_addB (z x y : M) : M ⊧/![z, x, y] addB ↔ z = add x y := eval_funcDef_add z x y

@[simp] lemma eval_mulB (z x y : M) : M ⊧/![z, x, y] mulB ↔ z = mul x y := eval_funcDef_mul z x y

lemma eval_num0 (z : M) : M ⊧/![z] (numeralF 0) ↔ z = ∅ := by
  rw [eval_numeralF_iff]; rfl

end semantics

/-! ## 加法 -/

lemma zfc_add_zero :
    𝗭𝗙𝗖 ⊢ (“∀ x y z, !(numeralF 0) y → !addB z x y → !eqB x z” : Sentence ℒₛₑₜ) := by
  apply SetTheory.complete.{0}
  intro M _ _ _
  simp only [models_iff]
  simp only [Semiformula.eval_all, LogicalConnective.HomClass.map_imply, Semiformula.eval_substs]
  intro x y z hy hz
  have hy' : y = ∅ := by simpa [eval_num0] using hy
  have hz' : z = add x y := by simpa using hz
  simp [hz', hy']

lemma zfc_add_succ :
    𝗭𝗙𝗖 ⊢ (“∀ x y v z, !GodelQ.ZFCArith.domainDef v → !numStep v y → !addB z x y →
      ∃ w, !addB w x v ∧ !numStep w z” : Sentence ℒₛₑₜ) := by
  apply SetTheory.complete.{0}
  intro M _ _ _
  simp only [models_iff]
  simp only [Semiformula.eval_all, LogicalConnective.HomClass.map_imply, Semiformula.eval_substs,
    Semiformula.eval_ex, LogicalConnective.HomClass.map_and]
  intro x y v z hv hy hz
  have hv' : v ∈ (ω : M) := by simpa using hv
  have hy' : y = SetTheory.succ v := by simpa using (eval_numStep v y).mp (by simpa using hy)
  have hz' : z = add x y := by simpa using hz
  refine ⟨add x v, by simp, ?_⟩
  simp [eval_numStep, hz', hy', add_succ x hv']

theorem numF_add (a b : V) :
    Z V ⊢ ∀¹ ∀¹ ∀¹ ((numF a).subst ![#'2] 🡒 (numF b).subst ![#'1] 🡒 addF.subst ![#'0, #'2, #'1] 🡒
      (numF (a + b)).subst ![#'0]) := by
  induction b using ISigma1.sigma1_succ_induction
  · simp only [tprovable_iff_provable]; definability
  case zero =>
    have hS : Z V ⊢ ∀¹ ∀¹ ∀¹ ((numF 0).subst ![#'1] 🡒 addF.subst ![#'0, #'2, #'1] 🡒
        eqF.subst ![#'2, #'0]) := by
      simpa [tq_vec_cons, fin1_fun_eq, numF_zero] using
        internal_provable_of_outer_provable (V := V) zfc_add_zero
    simp only [_root_.add_zero]
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
    have h1 : Z V ⊢ (numF 0).subst ![&'1] 🡒 addF.subst ![&'0, &'2, &'1] 🡒 eqF.subst ![&'2, &'0] := by
      simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₃! hS &'0 &'1 &'2
    have h2 : Z V ⊢ eqF.subst ![&'2, &'0] 🡒 (numF a).subst ![&'2] 🡒 (numF a).subst ![&'0] := by
      simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₂! (numF_congr a) &'0 &'2
    exact FiniteContext.of h2 ⨀ (FiniteContext.of h1 ⨀ FiniteContext.by_axm₁ ⨀ FiniteContext.by_axm₀) ⨀
      FiniteContext.by_axm₂
  case succ b ih =>
    have hS : Z V ⊢ ∀¹ ∀¹ ∀¹ ∀¹ (domF.subst ![#'1] 🡒 stepF.subst ![#'1, #'2] 🡒
        addF.subst ![#'0, #'3, #'2] 🡒 ∃¹ (addF.subst ![#'0, #'4, #'2] ⋏ stepF.subst ![#'0, #'1])) := by
      simpa [tq_vec_cons, fin1_fun_eq] using internal_provable_of_outer_provable (V := V) zfc_add_succ
    rw [← add_assoc, numF_succ (a + b), numF_succ b]
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
    apply exs_elim FiniteContext.by_axm₁
    simp [Bootstrapping.Semiformula.free, Bootstrapping.Semiformula.shift_substs,
      Bootstrapping.Semiformula.substs_substs]
    have hS' : Z V ⊢ domF.subst ![&'0] 🡒 stepF.subst ![&'0, &'2] 🡒 addF.subst ![&'1, &'3, &'2] 🡒
        ∃¹ (addF.subst ![#'0, &'3, &'0] ⋏ stepF.subst ![#'0, &'1]) := by
      simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₄! hS &'1 &'0 &'2 &'3
    have hD : Z V ⊢ (numF b).subst ![&'0] 🡒 domF.subst ![&'0] := by
      simpa using TProof.specialize! (numF_dom b) &'0
    apply exs_elim (FiniteContext.of hS' ⨀ (FiniteContext.of hD ⨀ K_left FiniteContext.by_axm₀) ⨀
      K_right FiniteContext.by_axm₀ ⨀ FiniteContext.by_axm₁)
    simp [Bootstrapping.Semiformula.free, Bootstrapping.Semiformula.shift_substs,
      Bootstrapping.Semiformula.substs_substs]
    apply exs_intro _ (&'0)
    simp [Bootstrapping.Semiformula.substs_substs]
    have ih' : Z V ⊢ (numF a).subst ![&'4] 🡒 (numF b).subst ![&'1] 🡒 addF.subst ![&'0, &'4, &'1] 🡒
        (numF (a + b)).subst ![&'0] := by
      simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₃! ih &'0 &'1 &'4
    exact K_intro (FiniteContext.of ih' ⨀ FiniteContext.nth_axm 4 ⨀ K_left FiniteContext.by_axm₁ ⨀
      K_left FiniteContext.by_axm₀) (K_right FiniteContext.by_axm₀)

/-! ## 乘法 -/

lemma zfc_mul_zero :
    𝗭𝗙𝗖 ⊢ (“∀ x y z, !(numeralF 0) y → !mulB z x y → !(numeralF 0) z” : Sentence ℒₛₑₜ) := by
  apply SetTheory.complete.{0}
  intro M _ _ _
  simp only [models_iff]
  simp only [Semiformula.eval_all, LogicalConnective.HomClass.map_imply, Semiformula.eval_substs]
  intro x y z hy hz
  have hy' : y = ∅ := by simpa [eval_num0] using hy
  have hz' : z = mul x y := by simpa using hz
  simp [eval_num0, hz', hy']

lemma zfc_mul_succ :
    𝗭𝗙𝗖 ⊢ (“∀ x y v z, !GodelQ.ZFCArith.domainDef v → !numStep v y → !mulB z x y →
      ∃ w, !mulB w x v ∧ !addB z w x” : Sentence ℒₛₑₜ) := by
  apply SetTheory.complete.{0}
  intro M _ _ _
  simp only [models_iff]
  simp only [Semiformula.eval_all, LogicalConnective.HomClass.map_imply, Semiformula.eval_substs,
    Semiformula.eval_ex, LogicalConnective.HomClass.map_and]
  intro x y v z hv hy hz
  have hv' : v ∈ (ω : M) := by simpa using hv
  have hy' : y = SetTheory.succ v := by simpa using (eval_numStep v y).mp (by simpa using hy)
  have hz' : z = mul x y := by simpa using hz
  refine ⟨mul x v, by simp, ?_⟩
  simp [hz', hy', mul_succ x hv']

theorem numF_mul (a b : V) :
    Z V ⊢ ∀¹ ∀¹ ∀¹ ((numF a).subst ![#'2] 🡒 (numF b).subst ![#'1] 🡒 mulF.subst ![#'0, #'2, #'1] 🡒
      (numF (a * b)).subst ![#'0]) := by
  induction b using ISigma1.sigma1_succ_induction
  · simp only [tprovable_iff_provable]; definability
  case zero =>
    have hS : Z V ⊢ ∀¹ ∀¹ ∀¹ ((numF 0).subst ![#'1] 🡒 mulF.subst ![#'0, #'2, #'1] 🡒
        (numF 0).subst ![#'0]) := by
      simpa [tq_vec_cons, fin1_fun_eq, numF_zero] using
        internal_provable_of_outer_provable (V := V) zfc_mul_zero
    simp only [MulZeroClass.mul_zero]
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
    have h1 : Z V ⊢ (numF 0).subst ![&'1] 🡒 mulF.subst ![&'0, &'2, &'1] 🡒 (numF 0).subst ![&'0] := by
      simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₃! hS &'0 &'1 &'2
    exact FiniteContext.of h1 ⨀ FiniteContext.by_axm₁ ⨀ FiniteContext.by_axm₀
  case succ b ih =>
    have hS : Z V ⊢ ∀¹ ∀¹ ∀¹ ∀¹ (domF.subst ![#'1] 🡒 stepF.subst ![#'1, #'2] 🡒
        mulF.subst ![#'0, #'3, #'2] 🡒 ∃¹ (mulF.subst ![#'0, #'4, #'2] ⋏ addF.subst ![#'1, #'0, #'4])) := by
      simpa [tq_vec_cons, fin1_fun_eq] using internal_provable_of_outer_provable (V := V) zfc_mul_succ
    rw [mul_add_one, numF_succ b]
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
    apply exs_elim FiniteContext.by_axm₁
    simp [Bootstrapping.Semiformula.free, Bootstrapping.Semiformula.shift_substs,
      Bootstrapping.Semiformula.substs_substs]
    have hS' : Z V ⊢ domF.subst ![&'0] 🡒 stepF.subst ![&'0, &'2] 🡒 mulF.subst ![&'1, &'3, &'2] 🡒
        ∃¹ (mulF.subst ![#'0, &'3, &'0] ⋏ addF.subst ![&'1, #'0, &'3]) := by
      simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₄! hS &'1 &'0 &'2 &'3
    have hD : Z V ⊢ (numF b).subst ![&'0] 🡒 domF.subst ![&'0] := by
      simpa using TProof.specialize! (numF_dom b) &'0
    apply exs_elim (FiniteContext.of hS' ⨀ (FiniteContext.of hD ⨀ K_left FiniteContext.by_axm₀) ⨀
      K_right FiniteContext.by_axm₀ ⨀ FiniteContext.by_axm₁)
    simp [Bootstrapping.Semiformula.free, Bootstrapping.Semiformula.shift_substs,
      Bootstrapping.Semiformula.substs_substs]
    have ih' : Z V ⊢ (numF a).subst ![&'4] 🡒 (numF b).subst ![&'1] 🡒 mulF.subst ![&'0, &'4, &'1] 🡒
        (numF (a * b)).subst ![&'0] := by
      simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₃! ih &'0 &'1 &'4
    have hA : Z V ⊢ (numF (a * b)).subst ![&'0] 🡒 (numF a).subst ![&'4] 🡒 addF.subst ![&'2, &'0, &'4] 🡒
        (numF (a * b + a)).subst ![&'2] := by
      simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₃! (numF_add (a * b) a) &'2 &'4 &'0
    exact FiniteContext.of hA ⨀
      (FiniteContext.of ih' ⨀ FiniteContext.nth_axm 4 ⨀ K_left FiniteContext.by_axm₁ ⨀
        K_left FiniteContext.by_axm₀) ⨀
      FiniteContext.nth_axm 4 ⨀ K_right FiniteContext.by_axm₀

/-! ## 小于 -/

lemma zfc_eq_step_mem :
    𝗭𝗙𝗖 ⊢ (“∀ x y v, !eqB x v → !numStep v y → !memB x y” : Sentence ℒₛₑₜ) := by
  apply SetTheory.complete.{0}
  intro M _ _ _
  simp only [models_iff]
  simp only [Semiformula.eval_all, LogicalConnective.HomClass.map_imply, Semiformula.eval_substs]
  intro x y v hxv hy
  have hxv' : x = v := by simpa using hxv
  have hy' : y = SetTheory.succ v := by simpa using (eval_numStep v y).mp (by simpa using hy)
  simp [hxv', hy', mem_succ_iff]

lemma zfc_mem_step_mem :
    𝗭𝗙𝗖 ⊢ (“∀ x y v, !memB x v → !numStep v y → !memB x y” : Sentence ℒₛₑₜ) := by
  apply SetTheory.complete.{0}
  intro M _ _ _
  simp only [models_iff]
  simp only [Semiformula.eval_all, LogicalConnective.HomClass.map_imply, Semiformula.eval_substs]
  intro x y v hxv hy
  have hxv' : x ∈ v := by simpa using hxv
  have hy' : y = SetTheory.succ v := by simpa using (eval_numStep v y).mp (by simpa using hy)
  simp [hxv', hy', mem_succ_iff]

/-- 第 a 个数属于第 a + d + 1 个数。 -/
theorem numF_lt (a d : V) :
    Z V ⊢ ∀¹ ∀¹ ((numF a).subst ![#'1] 🡒 (numF (a + d + 1)).subst ![#'0] 🡒 memF.subst ![#'1, #'0]) := by
  induction d using ISigma1.sigma1_succ_induction
  · simp only [tprovable_iff_provable]; definability
  case zero =>
    have hS : Z V ⊢ ∀¹ ∀¹ ∀¹ (eqF.subst ![#'2, #'0] 🡒 stepF.subst ![#'0, #'1] 🡒
        memF.subst ![#'2, #'1]) := by
      simpa [tq_vec_cons, fin1_fun_eq] using internal_provable_of_outer_provable (V := V) zfc_eq_step_mem
    rw [_root_.add_zero, numF_succ a]
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
    have hU : Z V ⊢ (numF a).subst ![&'2] 🡒 (numF a).subst ![&'0] 🡒 eqF.subst ![&'2, &'0] := by
      simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₂! (numF_uniq a) &'0 &'2
    have hS' : Z V ⊢ eqF.subst ![&'2, &'0] 🡒 stepF.subst ![&'0, &'1] 🡒 memF.subst ![&'2, &'1] := by
      simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₃! hS &'0 &'1 &'2
    exact FiniteContext.of hS' ⨀ (FiniteContext.of hU ⨀ FiniteContext.by_axm₂ ⨀ K_left FiniteContext.by_axm₀) ⨀
      K_right FiniteContext.by_axm₀
  case succ d ih =>
    have hS : Z V ⊢ ∀¹ ∀¹ ∀¹ (memF.subst ![#'2, #'0] 🡒 stepF.subst ![#'0, #'1] 🡒
        memF.subst ![#'2, #'1]) := by
      simpa [tq_vec_cons, fin1_fun_eq] using internal_provable_of_outer_provable (V := V) zfc_mem_step_mem
    rw [show a + (d + 1) + 1 = (a + d + 1) + 1 by ring, numF_succ (a + d + 1)]
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
    have ih' : Z V ⊢ (numF a).subst ![&'2] 🡒 (numF (a + d + 1)).subst ![&'0] 🡒 memF.subst ![&'2, &'0] := by
      simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₂! ih &'0 &'2
    have hS' : Z V ⊢ memF.subst ![&'2, &'0] 🡒 stepF.subst ![&'0, &'1] 🡒 memF.subst ![&'2, &'1] := by
      simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₃! hS &'0 &'1 &'2
    exact FiniteContext.of hS' ⨀ (FiniteContext.of ih' ⨀ FiniteContext.by_axm₂ ⨀ K_left FiniteContext.by_axm₀) ⨀
      K_right FiniteContext.by_axm₀

/-! ## 不小于、不等 -/

lemma zfc_eq_nmem : 𝗭𝗙𝗖 ⊢ (“∀ x y, !eqB x y → ¬!memB x y” : Sentence ℒₛₑₜ) := by
  apply SetTheory.complete.{0}
  intro M _ _ _
  simp only [models_iff]
  simp only [Semiformula.eval_all, LogicalConnective.HomClass.map_imply, Semiformula.eval_substs,
    LogicalConnective.HomClass.map_neg]
  intro x y hxy
  have e : x = y := by simpa using hxy
  subst e
  simp

lemma zfc_mem_nmem : 𝗭𝗙𝗖 ⊢ (“∀ x y, !memB y x → ¬!memB x y” : Sentence ℒₛₑₜ) := by
  apply SetTheory.complete.{0}
  intro M _ _ _
  simp only [models_iff]
  simp only [Semiformula.eval_all, LogicalConnective.HomClass.map_imply, Semiformula.eval_substs,
    LogicalConnective.HomClass.map_neg]
  intro x y hyx
  have h : y ∈ x := by simpa using hyx
  simpa using mem_asymm h

lemma zfc_mem_neq : 𝗭𝗙𝗖 ⊢ (“∀ x y, !memB x y → ¬!eqB x y” : Sentence ℒₛₑₜ) := by
  apply SetTheory.complete.{0}
  intro M _ _ _
  simp only [models_iff]
  simp only [Semiformula.eval_all, LogicalConnective.HomClass.map_imply, Semiformula.eval_substs,
    LogicalConnective.HomClass.map_neg]
  intro x y hxy hxy2
  have h : x ∈ y := by simpa using hxy
  have e : x = y := by simpa using hxy2
  subst e
  exact mem_irrefl _ h

lemma zfc_mem_neq' : 𝗭𝗙𝗖 ⊢ (“∀ x y, !memB y x → ¬!eqB x y” : Sentence ℒₛₑₜ) := by
  apply SetTheory.complete.{0}
  intro M _ _ _
  simp only [models_iff]
  simp only [Semiformula.eval_all, LogicalConnective.HomClass.map_imply, Semiformula.eval_substs,
    LogicalConnective.HomClass.map_neg]
  intro x y hyx hxy2
  have h : y ∈ x := by simpa using hyx
  have e : x = y := by simpa using hxy2
  subst e
  exact mem_irrefl _ h

/-- b ≤ a 时，第 a 个数不属于第 b 个数。 -/
theorem numF_nlt {a b : V} (h : b ≤ a) :
    Z V ⊢ ∀¹ ∀¹ ((numF a).subst ![#'1] 🡒 (numF b).subst ![#'0] 🡒 ∼memF.subst ![#'1, #'0]) := by
  rcases eq_or_lt_of_le h with (rfl | hlt)
  · have hS : Z V ⊢ ∀¹ ∀¹ (eqF.subst ![#'1, #'0] 🡒 ∼memF.subst ![#'1, #'0]) := by
      simpa [tq_vec_cons, fin1_fun_eq] using internal_provable_of_outer_provable (V := V) zfc_eq_nmem
    apply TProof.all!
    simp [Bootstrapping.Semiformula.free, Bootstrapping.Semiformula.shift_substs,
      Bootstrapping.Semiformula.substs_substs]
    apply TProof.all!
    simp [Bootstrapping.Semiformula.free, Bootstrapping.Semiformula.shift_substs,
      Bootstrapping.Semiformula.substs_substs]
    apply FiniteContext.deduct'
    apply FiniteContext.deduct
    have hU : Z V ⊢ (numF b).subst ![&'1] 🡒 (numF b).subst ![&'0] 🡒 eqF.subst ![&'1, &'0] := by
      simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₂! (numF_uniq b) &'0 &'1
    have hS' : Z V ⊢ eqF.subst ![&'1, &'0] 🡒 ∼memF.subst ![&'1, &'0] := by
      simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₂! hS &'0 &'1
    exact FiniteContext.of hS' ⨀ (FiniteContext.of hU ⨀ FiniteContext.by_axm₁ ⨀ FiniteContext.by_axm₀)
  · obtain ⟨d, rfl⟩ := le_iff_exists_add.mp (lt_iff_succ_le.mp hlt)
    have e : b + 1 + d = b + d + 1 := by ring
    rw [e]
    have hS : Z V ⊢ ∀¹ ∀¹ (memF.subst ![#'0, #'1] 🡒 ∼memF.subst ![#'1, #'0]) := by
      simpa [tq_vec_cons, fin1_fun_eq] using internal_provable_of_outer_provable (V := V) zfc_mem_nmem
    apply TProof.all!
    simp [Bootstrapping.Semiformula.free, Bootstrapping.Semiformula.shift_substs,
      Bootstrapping.Semiformula.substs_substs]
    apply TProof.all!
    simp [Bootstrapping.Semiformula.free, Bootstrapping.Semiformula.shift_substs,
      Bootstrapping.Semiformula.substs_substs]
    apply FiniteContext.deduct'
    apply FiniteContext.deduct
    have hL : Z V ⊢ (numF b).subst ![&'0] 🡒 (numF (b + d + 1)).subst ![&'1] 🡒 memF.subst ![&'0, &'1] := by
      simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₂! (numF_lt b d) &'1 &'0
    have hS' : Z V ⊢ memF.subst ![&'0, &'1] 🡒 ∼memF.subst ![&'1, &'0] := by
      simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₂! hS &'0 &'1
    exact FiniteContext.of hS' ⨀ (FiniteContext.of hL ⨀ FiniteContext.by_axm₀ ⨀ FiniteContext.by_axm₁)

/-- a ≠ b 时，第 a 个数与第 b 个数不等。 -/
theorem numF_neq {a b : V} (h : a ≠ b) :
    Z V ⊢ ∀¹ ∀¹ ((numF a).subst ![#'1] 🡒 (numF b).subst ![#'0] 🡒 ∼eqF.subst ![#'1, #'0]) := by
  rcases lt_or_gt_of_ne h with (hlt | hlt)
  · obtain ⟨d, rfl⟩ := le_iff_exists_add.mp (lt_iff_succ_le.mp hlt)
    have e : a + 1 + d = a + d + 1 := by ring
    rw [e]
    have hS : Z V ⊢ ∀¹ ∀¹ (memF.subst ![#'1, #'0] 🡒 ∼eqF.subst ![#'1, #'0]) := by
      simpa [tq_vec_cons, fin1_fun_eq] using internal_provable_of_outer_provable (V := V) zfc_mem_neq
    apply TProof.all!
    simp [Bootstrapping.Semiformula.free, Bootstrapping.Semiformula.shift_substs,
      Bootstrapping.Semiformula.substs_substs]
    apply TProof.all!
    simp [Bootstrapping.Semiformula.free, Bootstrapping.Semiformula.shift_substs,
      Bootstrapping.Semiformula.substs_substs]
    apply FiniteContext.deduct'
    apply FiniteContext.deduct
    have hL : Z V ⊢ (numF a).subst ![&'1] 🡒 (numF (a + d + 1)).subst ![&'0] 🡒 memF.subst ![&'1, &'0] := by
      simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₂! (numF_lt a d) &'0 &'1
    have hS' : Z V ⊢ memF.subst ![&'1, &'0] 🡒 ∼eqF.subst ![&'1, &'0] := by
      simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₂! hS &'0 &'1
    exact FiniteContext.of hS' ⨀ (FiniteContext.of hL ⨀ FiniteContext.by_axm₁ ⨀ FiniteContext.by_axm₀)
  · obtain ⟨d, rfl⟩ := le_iff_exists_add.mp (lt_iff_succ_le.mp hlt)
    have e : b + 1 + d = b + d + 1 := by ring
    rw [e]
    have hS : Z V ⊢ ∀¹ ∀¹ (memF.subst ![#'0, #'1] 🡒 ∼eqF.subst ![#'1, #'0]) := by
      simpa [tq_vec_cons, fin1_fun_eq] using internal_provable_of_outer_provable (V := V) zfc_mem_neq'
    apply TProof.all!
    simp [Bootstrapping.Semiformula.free, Bootstrapping.Semiformula.shift_substs,
      Bootstrapping.Semiformula.substs_substs]
    apply TProof.all!
    simp [Bootstrapping.Semiformula.free, Bootstrapping.Semiformula.shift_substs,
      Bootstrapping.Semiformula.substs_substs]
    apply FiniteContext.deduct'
    apply FiniteContext.deduct
    have hL : Z V ⊢ (numF b).subst ![&'0] 🡒 (numF (b + d + 1)).subst ![&'1] 🡒 memF.subst ![&'0, &'1] := by
      simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₂! (numF_lt b d) &'1 &'0
    have hS' : Z V ⊢ memF.subst ![&'0, &'1] 🡒 ∼eqF.subst ![&'1, &'0] := by
      simpa [Bootstrapping.Semiformula.substs_substs] using TProof.specialize₂! hS &'0 &'1
    exact FiniteContext.of hS' ⨀ (FiniteContext.of hL ⨀ FiniteContext.by_axm₀ ⨀ FiniteContext.by_axm₁)

end GodelQ.SetNum

#print axioms GodelQ.SetNum.numF_add
#print axioms GodelQ.SetNum.numF_mul
#print axioms GodelQ.SetNum.numF_lt
#print axioms GodelQ.SetNum.numF_nlt
#print axioms GodelQ.SetNum.numF_neq
