import GodelQ.ZFC.OmegaArith
import Foundation.FirstOrder.LK.Interpretation
import Foundation.FirstOrder.SetTheory.ZF.Model

/-!
# CG-006 · S3b：把算术语言翻译进 𝗭𝗙𝗖

`arithTrln : DirectTranslation 𝗭𝗙𝗖 ℒₒᵣ`：定义域 ω；`0 ↦ ∅`，`1 ↦ succ ∅`；加法、乘法取 ω 上递归的
定义公式；`= ↦ =`，`< ↦ ∈`。三条证明义务（定义域非空、函数在 ω 上存在唯一、等号保持）由
`SetTheory.complete` 化成“在 𝗭𝗙𝗖 的每个模型里成立”，用 `OmegaArith` 的模型事实证明。
-/

namespace GodelQ.ZFCArith

open FFL FFL.FirstOrder FFL.FirstOrder.SetTheory

def domainDef : SetTheorySemisentence 1 := “x. ∃ w, !isω w ∧ x ∈ w”

def relDef : {k : ℕ} → (ℒₒᵣ).Rel k → SetTheorySemisentence k
  | _, Language.ORing.Rel.eq => “x y. x = y”
  | _, Language.ORing.Rel.lt => “x y. x ∈ y”

def funcDef : {k : ℕ} → (ℒₒᵣ).Func k → SetTheorySemisentence (k + 1)
  | _, Language.ORing.Func.zero => “z. !isEmpty z”
  | _, Language.ORing.Func.one => “z. ∃ e, !isEmpty e ∧ !succ.dfn z e”
  | _, Language.ORing.Func.add => “z x y. !addBlueprint.resultDef z y x”
  | _, Language.ORing.Func.mul => “z x y. !mulBlueprint.resultDef z y x”

section semantics

variable {V : Type*} [SetStructure V] [Nonempty V] [V↓[ℒₛₑₜ] ⊧* 𝗭]

omit [Nonempty V] [V↓[ℒₛₑₜ] ⊧* 𝗭] in
@[simp] lemma eval_relDef_eq' (x y : V) :
    Semiformula.Eval ![x, y] Empty.elim (relDef Language.ORing.Rel.eq) ↔ x = y := by
  simp [relDef]

@[simp] lemma eval_domainDef (x : V) : V ⊧/![x] domainDef ↔ x ∈ (ω : V) := by
  simp [domainDef]

@[simp] lemma eval_funcDef_zero (z : V) :
    Semiformula.Eval ![z] Empty.elim (funcDef Language.ORing.Func.zero) ↔ z = ∅ := by
  simp [funcDef, isEmpty_iff_eq_empty]

@[simp] lemma eval_funcDef_one (z : V) :
    Semiformula.Eval ![z] Empty.elim (funcDef Language.ORing.Func.one) ↔ z = SetTheory.succ ∅ := by
  simp [funcDef, isEmpty_iff_eq_empty, succ.defined.iff]

@[simp] lemma eval_funcDef_add (z x y : V) :
    Semiformula.Eval ![z, x, y] Empty.elim (funcDef Language.ORing.Func.add) ↔ z = add x y := by
  simp [funcDef, add, addC.result_defined.iff, Matrix.vec_single_eq_const]

@[simp] lemma eval_funcDef_mul (z x y : V) :
    Semiformula.Eval ![z, x, y] Empty.elim (funcDef Language.ORing.Func.mul) ↔ z = mul x y := by
  simp [funcDef, mul, mulC.result_defined.iff, Matrix.vec_single_eq_const]

@[simp] lemma eval_relDef_eq (x y : V) :
    Semiformula.Eval ![x, y] Empty.elim (relDef Language.ORing.Rel.eq) ↔ x = y := by
  simp [relDef]

@[simp] lemma eval_relDef_lt (x y : V) :
    Semiformula.Eval ![x, y] Empty.elim (relDef Language.ORing.Rel.lt) ↔ x ∈ y := by
  simp [relDef]

end semantics

/-- 从算术语言到 𝗭𝗙𝗖 的直接翻译。 -/
noncomputable def arithTrln : DirectTranslation 𝗭𝗙𝗖 ℒₒᵣ where
  domain := domainDef
  rel := relDef
  func := funcDef
  domain_nonempty := by
    apply SetTheory.complete.{0}
    intro M _ _ _
    simp [models_iff]
    exact ⟨∅, by simp⟩
  func_defined {k} f := by
    apply SetTheory.complete.{0}
    intro M _ _ _
    cases f with
    | zero =>
      simp [models_iff]
      exact ⟨∅, ⟨by simp, rfl⟩, fun y hy => hy.2⟩
    | one =>
      simp [models_iff]
      refine ⟨SetTheory.succ ∅, ⟨ω_succ_closed (by simp), rfl⟩, fun y hy => hy.2⟩
    | add =>
      simp [models_iff]
      intro e h0 h1
      obtain ⟨a, b, rfl⟩ : ∃ a b : M, e = ![a, b] :=
        Exists.intro (e 0) (Exists.intro (e 1) (funext fun i => match i with | 0 => rfl | 1 => rfl))
      refine ⟨add a b, ⟨add_mem_ω h0 h1, by simp⟩, fun y hy => ?_⟩
      simpa using hy.2
    | mul =>
      simp [models_iff]
      intro e h0 h1
      obtain ⟨a, b, rfl⟩ : ∃ a b : M, e = ![a, b] :=
        Exists.intro (e 0) (Exists.intro (e 1) (funext fun i => match i with | 0 => rfl | 1 => rfl))
      refine ⟨mul a b, ⟨mul_mem_ω h0 h1, by simp⟩, fun y hy => ?_⟩
      simpa using hy.2
  preserve_eq := by
    apply SetTheory.complete.{0}
    intro M _ _ _
    simp [models_iff]
    intro x y _ _
    exact eval_relDef_eq x y

end GodelQ.ZFCArith

#print axioms GodelQ.ZFCArith.eval_domainDef
#print axioms GodelQ.ZFCArith.arithTrln
