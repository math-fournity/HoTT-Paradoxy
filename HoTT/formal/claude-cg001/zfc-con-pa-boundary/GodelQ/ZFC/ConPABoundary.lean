import GodelQ.ZFC.PAModel
import Foundation.FirstOrder.Incompleteness.Second

/-!
# CG-010 R8：𝗭𝗙𝗖 证 Con(𝗣𝗔)——落在哪条义务上（CG001-C-429）

CN-079 §6 第 2 条：把“A 把不停机往上搬”的第一级——𝗭𝗙𝗖 证明 𝗣𝗔 一致——落到 Foundation 的 𝗭𝗙𝗖 上。
这是经典定理（𝗭𝗙𝗖 里 ω 是 𝗣𝗔 的模型，再加 ω 上的真值定义与可靠性）；本文件没有证出它，而是用机器
把它归结为一条精确的义务，并证明那条义务不能只靠“ω 是 𝗣𝗔 的模型”（C-109）来付：

* (1) `zfc_conPA_iff`：𝗭𝗙𝗖 证明 Con(𝗣𝗔) 的翻译，当且仅当 𝗭𝗙𝗖 每个模型的 ω 都满足 Con(𝗣𝗔)。
* (2) `universe_conPA`：标准模型 `Universe` 的 ω 满足它；于是 𝗭𝗙𝗖 驳不倒它（`zfc_not_refute_conPA`）。
* (3) `pa_model_refutes_conPA`：并非每个 𝗣𝗔 的模型都满足 Con(𝗣𝗔)（由 𝗣𝗔 的第二不完备与完备性）。

所以剩下的义务是：在 𝗭𝗙𝗖 的任意模型 M 里，用 M 的集合给 ω^M 上的算术公式定义满足关系，证明 𝗣𝗔 的全部
（内部编码的、可以是非标准的）公理都满足，且 Foundation 的内部推导保持满足。见 `CLAIM.md` §4。
-/

namespace GodelQ.ConPA

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory
open scoped FFL.FirstOrder.Arithmetic
open GodelQ.ZFCNum GodelQ.ZFCArith GodelQ.ZFCSound

/-- 𝗣𝗔 的一致性句（Foundation 的 Π1 算术句“𝗣𝗔 证不出 ⊥”）。 -/
noncomputable abbrev conPA : ArithmeticSentence := (Theory.consistent 𝗣𝗔 : ArithmeticSentence)

/-- **(1) 𝗭𝗙𝗖 证明 Con(𝗣𝗔) 的翻译，当且仅当 𝗭𝗙𝗖 每个模型的 ω 都满足 Con(𝗣𝗔)。** -/
theorem zfc_conPA_iff :
    𝗭𝗙𝗖 ⊢ arithTrln.translate conPA ↔
      ∀ (M : Type) [SetStructure M] [Nonempty M] [M↓[ℒₛₑₜ] ⊧* 𝗭𝗙𝗖], (W M)↓[ℒₒᵣ] ⊧ conPA := by
  constructor
  · intro h M _ _ _
    have hM : M↓[ℒₛₑₜ] ⊧ arithTrln.translate conPA := models_of_provable inferInstance h
    exact (models_N_iff conPA).mp (DirectTranslation.Model.translate_iff.mp hM)
  · intro H
    apply SetTheory.complete.{0}
    intro M _ _ _
    apply DirectTranslation.Model.translate_iff.mpr
    exact (models_N_iff (M := M) conPA).mpr (H M)

/-- `Universe` 的 ω 与 ℕ 满足同样的算术句。 -/
theorem N_universe_iff_nat (σ : ArithmeticSentence) :
    (N Universe.{0})↓[ℒₒᵣ] ⊧ σ ↔ ℕ↓[ℒₒᵣ] ⊧ σ := by
  rw [models_iff, models_iff]
  have h := eval_equiv_iff natEquivN natEquivN_func natEquivN_rel
    (b := (![] : Fin 0 → N Universe.{0})) (ε := (Empty.elim : Empty → N Universe.{0})) (φ := σ)
  have hb : (natEquivN.symm ∘ (![] : Fin 0 → N Universe.{0})) = ![] := funext fun i ↦ i.elim0
  have hε : (natEquivN.symm ∘ (Empty.elim : Empty → N Universe.{0})) = Empty.elim :=
    funext fun x ↦ x.elim
  rw [hb, hε] at h
  exact h

/-- ℕ 满足 Con(𝗣𝗔)：𝗣𝗔 一致（ℕ 是它的模型）。 -/
theorem nat_conPA : ℕ↓[ℒₒᵣ] ⊧ conPA := by
  simp only [conPA, models_iff]
  exact (Bootstrapping.consistent.defined (T := 𝗣𝗔) (V := ℕ)).mpr
    ((Bootstrapping.standard_consistent 𝗣𝗔).mpr inferInstance)

/-- **(2) 标准模型 `Universe` 满足 Con(𝗣𝗔) 的翻译。** -/
theorem universe_conPA : Universe.{0}↓[ℒₛₑₜ] ⊧ arithTrln.translate conPA :=
  DirectTranslation.Model.translate_iff.mpr ((N_universe_iff_nat conPA).mpr nat_conPA)

/-- 𝗭𝗙𝗖 驳不倒 Con(𝗣𝗔)（由 (2) 与 `Universe` 是 𝗭𝗙𝗖 的模型）。 -/
theorem zfc_not_refute_conPA : 𝗭𝗙𝗖 ⊬ ∼ arithTrln.translate conPA := by
  intro h
  have hU : Universe.{0}↓[ℒₛₑₜ] ⊧ ∼ arithTrln.translate conPA := models_of_provable inferInstance h
  exact (Semantics.Not.models_not.mp hU) universe_conPA

/-- **(3) 并非每个 𝗣𝗔 的模型都满足 Con(𝗣𝗔)**（𝗣𝗔 证不出自己一致，再用完备性）。 -/
theorem pa_model_refutes_conPA :
    ¬ ∀ (V : Type) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗣𝗔], V↓[ℒₒᵣ] ⊧ conPA := fun H =>
  consistent_unprovable 𝗣𝗔 (Arithmetic.complete 𝗣𝗔 conPA H)

end GodelQ.ConPA
