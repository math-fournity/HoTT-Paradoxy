import GodelQ.ZFC.SetNumArith

/-!
# 012-Opus · W8：翻译后的原子公式与变量等式的有型形状

把 Foundation 的 `arithTrln.varEqual t` 与 `arithTrln.translateRel R v` 的有型引号，在任意参数向量的
代换下写成“块”的组合：定义域块 `domF`、等号块 `eqF`、函数块 `⌜func f⌝`、关系块 `⌜rel R⌝` 与更小的
变量等式。这是项引理与原子情形的唯一入口。
-/

namespace GodelQ.SetNum

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment FFL.Entailment.FiniteContext
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCNum GodelQ.ZFCArith GodelQ.IntLogic GodelQ.Translate

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

local prefix:max "#'" => Bootstrapping.Semiterm.bvar (V := V) (L := ℒₛₑₜ)
local prefix:max "&'" => Bootstrapping.Semiterm.fvar (V := V) (L := ℒₛₑₜ)

/-- 参数在两个约束变量之下的提升。 -/
noncomputable abbrev bS2 {n m : ℕ} (e : Fin n → Bootstrapping.Semiterm V ℒₛₑₜ m) :
    Fin n → Bootstrapping.Semiterm V ℒₛₑₜ (m + 2) := fun j ↦ (e j).bShift.bShift

/-- 翻译的变量等式 `VE[t](z; e)`：z 等于项 t 的值，t 的变量取 e。 -/
noncomputable def veF {n m : ℕ} (t : ClosedSemiterm ℒₒᵣ n) (z : Bootstrapping.Semiterm V ℒₛₑₜ m)
    (e : Fin n → Bootstrapping.Semiterm V ℒₛₑₜ m) : Bootstrapping.Semiformula V ℒₛₑₜ m :=
  (⌜(arithTrln.varEqual t : Semisentence ℒₛₑₜ (n + 1))⌝ :
    Bootstrapping.Semiformula V ℒₛₑₜ (n + 1)).subst (z :> e)

section
variable {L : Language} [L.Encodable] [L.LORDefinable]

omit [L.Encodable] [L.LORDefinable] in
lemma app_subst_eq {k m : ℕ} (σ : Semisentence L k) (w : Fin k → ClosedSemiterm L m) :
    Rewriting.app (Rew.subst w) σ = σ ⇜ w := rfl

lemma tq_conj2 {n : ℕ} (A : Fin 2 → Semisentence L n) :
    (⌜Matrix.conj A⌝ : Bootstrapping.Semiformula V L n) = ⌜A 0⌝ ⋏ (⌜A 1⌝ ⋏ ⊤) := by
  rw [matrix_conj_two]; simp

lemma qq_addNat {k m : ℕ} (w : SemitermVec V L k m) (j : Fin k) :
    w.q.q (j.addNat 2) = (w j).bShift.bShift := by
  have : (j.addNat 2 : Fin (k + 2)) = j.succ.succ := Fin.ext (by simp)
  rw [this, SemitermVec.q_succ, SemitermVec.q_succ]

lemma qq_addCast0 {k m : ℕ} (w : SemitermVec V L k m) :
    w.q.q ((0 : Fin 2).addCast k) = Bootstrapping.Semiterm.bvar 0 := by
  have : ((0 : Fin 2).addCast k : Fin (k + 2)) = 0 := Fin.ext (by simp)
  rw [this]; rfl

lemma qq_addCast1 {k m : ℕ} (w : SemitermVec V L k m) :
    w.q.q ((1 : Fin 2).addCast k) = Bootstrapping.Semiterm.bvar 1 := by
  have : ((1 : Fin 2).addCast k : Fin (k + 2)) = (0 : Fin (k + 1)).succ := Fin.ext (by simp)
  rw [this, SemitermVec.q_succ]
  simp

lemma tq_conj0 {n : ℕ} (A : Fin 0 → Semisentence L n) :
    (⌜Matrix.conj A⌝ : Bootstrapping.Semiformula V L n) = ⊤ := by
  rw [matrix_conj_zero]; simp
end

lemma veF_bvar {n m : ℕ} (i : Fin n) (z : Bootstrapping.Semiterm V ℒₛₑₜ m)
    (e : Fin n → Bootstrapping.Semiterm V ℒₛₑₜ m) :
    veF (#i : ClosedSemiterm ℒₒᵣ n) z e = eqF.subst ![z, e i] := by
  have h : (“#0 = #i.succ” : Semisentence ℒₛₑₜ (n + 1)) = eqB ⇜ ![#0, #i.succ] := by
    simp [eqB]
  simp only [veF, DirectTranslation.varEqual]
  rw [h, tq_substs, Bootstrapping.Semiformula.substs_substs]
  congr 1
  funext j; fin_cases j <;> simp

lemma veF_func2 {n m : ℕ} (f : (ℒₒᵣ).Func 2) (v : Fin 2 → ClosedSemiterm ℒₒᵣ n)
    (z : Bootstrapping.Semiterm V ℒₛₑₜ m) (e : Fin n → Bootstrapping.Semiterm V ℒₛₑₜ m) :
    veF (Semiterm.func f v) z e =
      ∀¹ ∀¹ (((domF.subst ![#'0] ⋏ veF (v 0) #'0 (bS2 e)) ⋏ ((domF.subst ![#'1] ⋏ veF (v 1) #'1 (bS2 e)) ⋏ ⊤)) 🡒
        (⌜(arithTrln.func f : Semisentence ℒₛₑₜ 3)⌝ : Bootstrapping.Semiformula V ℒₛₑₜ 3).subst
          ![z.bShift.bShift, #'0, #'1]) := by
  simp only [veF, DirectTranslation.varEqual]
  simp [embSubsts_app, allItr_succ, app_subst_eq, tq_conj2, Bootstrapping.Semiformula.substs_substs,
    tq_vec_cons, qq_addNat, qq_addCast0, qq_addCast1]
  refine ⟨⟨⟨rfl, ?_⟩, rfl, ?_⟩, ?_⟩
  · congr 1; funext i; cases i using Fin.cases <;> simp [qq_addNat, bS2]
  · congr 1; funext i; cases i using Fin.cases <;> simp [qq_addNat, bS2]
  · congr 1; funext i; fin_cases i <;> simp [Matrix.vecHead, Matrix.vecTail, qq_addCast0, qq_addCast1]

lemma veF_func0 {n m : ℕ} (f : (ℒₒᵣ).Func 0) (v : Fin 0 → ClosedSemiterm ℒₒᵣ n)
    (z : Bootstrapping.Semiterm V ℒₛₑₜ m) (e : Fin n → Bootstrapping.Semiterm V ℒₛₑₜ m) :
    veF (Semiterm.func f v) z e =
      (⊤ 🡒 (⌜(arithTrln.func f : Semisentence ℒₛₑₜ 1)⌝ : Bootstrapping.Semiformula V ℒₛₑₜ 1).subst ![z]) := by
  simp only [veF, DirectTranslation.varEqual]
  simp [embSubsts_app, app_subst_eq, Bootstrapping.Semiformula.substs_substs]

/-- 原子公式 `R(v₀, v₁)` 的翻译在代换 e 下的形状。 -/
lemma trRel2 {n m : ℕ} (R : (ℒₒᵣ).Rel 2) (v : Fin 2 → ClosedSemiterm ℒₒᵣ n)
    (e : Fin n → Bootstrapping.Semiterm V ℒₛₑₜ m) :
    (⌜(arithTrln.translateRel R v : Semisentence ℒₛₑₜ n)⌝ : Bootstrapping.Semiformula V ℒₛₑₜ n).subst e =
      ∀¹ ∀¹ (((domF.subst ![#'0] ⋏ veF (v 0) #'0 (bS2 e)) ⋏ ((domF.subst ![#'1] ⋏ veF (v 1) #'1 (bS2 e)) ⋏ ⊤)) 🡒
        (⌜(arithTrln.rel R : Semisentence ℒₛₑₜ 2)⌝ : Bootstrapping.Semiformula V ℒₛₑₜ 2).subst ![#'0, #'1]) := by
  simp only [DirectTranslation.translateRel]
  simp [embSubsts_app, allItr_succ, app_subst_eq, tq_conj2, Bootstrapping.Semiformula.substs_substs,
    tq_vec_cons, qq_addCast0, qq_addCast1]
  refine ⟨⟨⟨rfl, ?_⟩, rfl, ?_⟩, ?_⟩
  · simp only [veF]; congr 1; funext i; cases i using Fin.cases <;> simp [qq_addNat, bS2]
  · simp only [veF]; congr 1; funext i; cases i using Fin.cases <;> simp [qq_addNat, bS2]
  · congr 1; funext i; fin_cases i <;> simp [Matrix.vecHead, Matrix.vecTail, qq_addCast0, qq_addCast1]

/-- 项的 bShift：多出的第 0 个变量不出现在变量等式里。 -/
lemma veF_bShift {n m : ℕ} : ∀ (t : ClosedSemiterm ℒₒᵣ n) (z : Bootstrapping.Semiterm V ℒₛₑₜ m)
    (x : Bootstrapping.Semiterm V ℒₛₑₜ m) (e : Fin n → Bootstrapping.Semiterm V ℒₛₑₜ m),
    veF (Rew.bShift t) z (x :> e) = veF t z e
  | #i, z, x, e => by simp [veF_bvar]
  | &x, _, _, _ => Empty.elim x
  | .func Language.Zero.zero v, z, x, e => by
      rw [Rew.func, veF_func0, veF_func0]
  | .func Language.One.one v, z, x, e => by
      rw [Rew.func, veF_func0, veF_func0]
  | .func Language.Add.add v, z, x, e => by
      rw [Rew.func, veF_func2, veF_func2]
      have h0 := veF_bShift (v 0) (#'0) x.bShift.bShift (bS2 e)
      have h1 := veF_bShift (v 1) (#'1) x.bShift.bShift (bS2 e)
      have hb : bS2 (x :> e) = x.bShift.bShift :> bS2 e := by
        funext j; cases j using Fin.cases <;> simp [bS2]
      simp only [hb, Function.comp_apply, h0, h1]
  | .func Language.Mul.mul v, z, x, e => by
      rw [Rew.func, veF_func2, veF_func2]
      have h0 := veF_bShift (v 0) (#'0) x.bShift.bShift (bS2 e)
      have h1 := veF_bShift (v 1) (#'1) x.bShift.bShift (bS2 e)
      have hb : bS2 (x :> e) = x.bShift.bShift :> bS2 e := by
        funext j; cases j using Fin.cases <;> simp [bS2]
      simp only [hb, Function.comp_apply, h0, h1]

/-- 代换穿过 `veF`。 -/
lemma veF_subst {n m l : ℕ} (t : ClosedSemiterm ℒₒᵣ n) (z : Bootstrapping.Semiterm V ℒₛₑₜ m)
    (e : Fin n → Bootstrapping.Semiterm V ℒₛₑₜ m) (w : SemitermVec V ℒₛₑₜ m l) :
    (veF t z e).subst w = veF t (z.subst w) (fun i ↦ (e i).subst w) := by
  simp only [veF, Bootstrapping.Semiformula.substs_substs]
  congr 1; funext j; cases j using Fin.cases <;> simp

/-- 自由变量平移穿过 `veF`。 -/
lemma veF_shift {n m : ℕ} (t : ClosedSemiterm ℒₒᵣ n) (z : Bootstrapping.Semiterm V ℒₛₑₜ m)
    (e : Fin n → Bootstrapping.Semiterm V ℒₛₑₜ m) :
    (veF t z e).shift = veF t z.shift (fun i ↦ (e i).shift) := by
  simp only [veF, Bootstrapping.Semiformula.shift_substs, tq_shift_sentence]
  congr 1; funext j; cases j using Fin.cases <;> simp

end GodelQ.SetNum
