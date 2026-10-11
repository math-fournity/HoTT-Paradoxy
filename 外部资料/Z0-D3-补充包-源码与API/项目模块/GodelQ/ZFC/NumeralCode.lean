import GodelQ.ZFC.ZFCDelta1

/-!
# CG-006 · S2c：Rayo 式数字公式及其编码的原始递归

`Num_0(z) := ∀w (w ∉ z)`，`Num_{n+1}(z) := ∃y (Num_n(y) ∧ ∀w (w ∈ z ↔ w ∈ y ∨ w = y))`。
在 ∃y 之下 `Num_n(y)` 只是把 `Num_n` 的唯一约束变量放到更深一层（`castLE`），编码不变，所以
`⌜Num_{n+1}⌝ = ^∃ (⌜Num_n⌝ ^⋏ ⌜step⌝)`：编码是一个简单的原始递归，在 𝗜𝚺₁ 的任意模型中
由 `PR.Blueprint` 定义为 Σ1 函数 `numCode`。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping SetTheory
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.ZFCNum

/-- 后继步 `∀w (w ∈ z ↔ w ∈ y ∨ w = y)`，y = #0，z = #1。 -/
def numStep : SetTheorySemisentence 2 := “y z. ∀ w, w ∈ z ↔ w ∈ y ∨ w = y”

/-- Rayo 式冯·诺依曼数公式 `Num_n(z)`（z = #0）。 -/
def numeralF : ℕ → SetTheorySemisentence 1
  | 0 => “z. ∀ w, w ∉ z”
  | n + 1 => ∃¹ ((Rew.castLE (by omega : 1 ≤ 2) ▹ numeralF n : SetTheorySemisentence 2) ⋏ numStep)

lemma emb_castLE {n n' : ℕ} (h : n ≤ n') (σ : SetTheorySemisentence n) :
    (Rewriting.emb (Rew.castLE h ▹ σ : SetTheorySemisentence n') : SetTheorySemiproposition n')
      = Rew.castLE h ▹ (Rewriting.emb σ : SetTheorySemiproposition n) := by
  show Rew.emb ▹ (Rew.castLE h ▹ σ) = Rew.castLE h ▹ (Rew.emb ▹ σ)
  rw [← TransitiveRewriting.comp_app, ← TransitiveRewriting.comp_app]
  apply Semiformula.rew_eq_of_funEqOn
  · intro x; simp [Rew.comp_app]
  · intro x _; exact x.elim

lemma quote_castLE_sentence {n n' : ℕ} (h : n ≤ n') (σ : SetTheorySemisentence n) :
    (⌜(Rew.castLE h ▹ σ : SetTheorySemisentence n')⌝ : ℕ) = ⌜σ⌝ := by
  rw [Sentence.quote_def, Sentence.quote_def, emb_castLE, Semiformula.quote_castLE]

noncomputable def num0Code : ℕ := ⌜numeralF 0⌝
noncomputable def stepCode : ℕ := ⌜numStep⌝

lemma quote_numeralF_succ (n : ℕ) :
    (⌜numeralF (n + 1)⌝ : ℕ) = ^∃ ((⌜numeralF n⌝ : ℕ) ^⋏ stepCode) := by
  have e : (⌜numeralF (n + 1)⌝ : ℕ) =
      ^∃ ((⌜(Rew.castLE (by omega : 1 ≤ 2) ▹ numeralF n : SetTheorySemisentence 2)⌝ : ℕ)
        ^⋏ ⌜numStep⌝) := by
    simp [numeralF, Sentence.quote_def]
  rw [e, quote_castLE_sentence]
  rfl

section

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

noncomputable def numCode.blueprint : PR.Blueprint 0 where
  zero := .mkSigma “y. y = ↑num0Code”
  succ := .mkSigma “y ih n. ∃ a, !qqAndDef a ih ↑stepCode ∧ !qqExsDef y a”

noncomputable def numCode.construction : PR.Construction V numCode.blueprint where
  zero := fun _ ↦ ↑num0Code
  succ := fun _ _ ih ↦ ^∃ (ih ^⋏ ↑stepCode)
  zero_defined := .mk fun v ↦ by simp [numCode.blueprint, numeral_eq_natCast]
  succ_defined := .mk fun v ↦ by simp [numCode.blueprint, numeral_eq_natCast]

/-- `numCode n = ⌜Num_n⌝`（内部原始递归）。 -/
noncomputable def numCode (n : V) : V := numCode.construction.result ![] n

@[simp] lemma numCode_zero : numCode (0 : V) = ↑num0Code := by
  simp [numCode, numCode.construction]

@[simp] lemma numCode_succ (n : V) : numCode (n + 1) = ^∃ (numCode n ^⋏ ↑stepCode) := by
  simp [numCode, numCode.construction]

noncomputable def numCodeDef : 𝚺ᴬ₁.Semisentence 2 := numCode.blueprint.resultDef

instance numCode.defined : 𝚺ᴬ₁-Function₁ (numCode : V → V) via numCodeDef := .mk
  fun v ↦ by simp [numCode.construction.result_defined_iff, numCodeDef]; rfl

instance numCode.definable : 𝚺ᴬ₁-Function₁ (numCode : V → V) := numCode.defined.to_definable

end

lemma numCode_quote (n : ℕ) : numCode (n : ℕ) = (⌜numeralF n⌝ : ℕ) := by
  induction n with
  | zero => simp [num0Code]
  | succ n ih => rw [numCode_succ, ih, quote_numeralF_succ, natCast_nat]

#print axioms numCode_quote
#print axioms numCode.defined

end GodelQ.ZFCNum
