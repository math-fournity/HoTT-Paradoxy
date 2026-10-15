import GodelQ.ZFC.ConPABoundary

/-!
# 命题对照：CG001-C-429（𝗭𝗙𝗖 证 Con(𝗣𝗔) 落在哪条义务上）

* (1) 𝗭𝗙𝗖 证明 Con(𝗣𝗔) 的翻译，当且仅当 𝗭𝗙𝗖 每个模型的 ω 都满足 Con(𝗣𝗔)；
* (2) 𝗭𝗙𝗖 每个模型的 ω 都是 𝗣𝗔 的模型（C-109）；
* (3) 标准模型 `Universe` 满足 Con(𝗣𝗔) 的翻译；(4) 𝗭𝗙𝗖 驳不倒它；
* (5) 并非每个 𝗣𝗔 的模型都满足 Con(𝗣𝗔)，所以 (2) 不足以给出 (1) 的右边。
-/

namespace GodelQ.ConPA

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory
open scoped FFL.FirstOrder.Arithmetic
open GodelQ.ZFCNum GodelQ.ZFCArith GodelQ.ZFCSound

/-- CG001-C-429：𝗭𝗙𝗖 证 Con(𝗣𝗔) 归结为一条义务，那条义务不能只靠“ω 是 𝗣𝗔 的模型”来付。 -/
theorem qual_C429 :
    (𝗭𝗙𝗖 ⊢ arithTrln.translate conPA ↔
      ∀ (M : Type) [SetStructure M] [Nonempty M] [M↓[ℒₛₑₜ] ⊧* 𝗭𝗙𝗖], (W M)↓[ℒₒᵣ] ⊧ conPA) ∧
    (∀ (M : Type) [SetStructure M] [Nonempty M] [M↓[ℒₛₑₜ] ⊧* 𝗭𝗙𝗖], (W M)↓[ℒₒᵣ] ⊧* 𝗣𝗔) ∧
    Universe.{0}↓[ℒₛₑₜ] ⊧ arithTrln.translate conPA ∧
    𝗭𝗙𝗖 ⊬ ∼ arithTrln.translate conPA ∧
    ¬ ∀ (V : Type) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗣𝗔], V↓[ℒₒᵣ] ⊧ conPA :=
  ⟨zfc_conPA_iff, fun _ _ _ _ => inferInstance, universe_conPA, zfc_not_refute_conPA,
    pa_model_refutes_conPA⟩

end GodelQ.ConPA

#print axioms GodelQ.ConPA.qual_C429
#print axioms GodelQ.ConPA.zfc_conPA_iff
#print axioms GodelQ.ConPA.universe_conPA
#print axioms GodelQ.ConPA.zfc_not_refute_conPA
#print axioms GodelQ.ConPA.pa_model_refutes_conPA
