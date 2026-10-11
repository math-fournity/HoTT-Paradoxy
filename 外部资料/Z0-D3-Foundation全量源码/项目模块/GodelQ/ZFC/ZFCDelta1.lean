import GodelQ.ZFC.ReplacementDelta1
import Foundation.FirstOrder.SetTheory.ZF.Basic

/-!
# CG-006 · S2b（三）：`𝗭𝗙𝗖` 是 Δ1 的（有效公理化）

`𝗭𝗙𝗖 = ((𝗕𝗦𝗧 ∪ 𝗦𝗘𝗣) ∪ 𝗥𝗘𝗣𝗟) ∪ 𝗔𝗖`。
* `𝗕𝗦𝗧`：等词公理 `𝗘𝗤 ℒₛₑₜ`（ℒₛₑₜ 有限，故有限）加七条单句，有限；
* `𝗦𝗘𝗣`、`𝗥𝗘𝗣𝗟`：见 `SchemaDelta1.lean`、`ReplacementDelta1.lean`；
* `𝗔𝗖`：单句。
并集用 Foundation 的 `Theory.Δ₁` 并集实例。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping SetTheory
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.ZFCDelta1

/-- `𝗕𝗦𝗧` 的七条单句公理（逐字取自 Foundation `BST/Basic.lean`）。 -/
def bstAxioms : Set (Sentence ℒₛₑₜ) :=
  { “∃ e, !isEmpty e”,
    “∀ x y, x = y ↔ ∀ z, z ∈ x ↔ z ∈ y”,
    “∀ x y, ∃ z, ∀ w, w ∈ z ↔ w = x ∨ w = y”,
    “∀ x, ∃ y, ∀ z, z ∈ y ↔ ∃ w ∈ x, z ∈ w”,
    “∀ x, ∃ y, ∀ z, z ∈ y ↔ z ⊆ x”,
    “∃ I, (∀ e, !isEmpty e → e ∈ I) ∧ (∀ x ∈ I, ∀ x', !isSucc x' x → x' ∈ I)”,
    “∀ x, !isNonempty x → ∃ y ∈ x, ∀ z ∈ x, z ∉ y” }

lemma bst_subset : (𝗕𝗦𝗧 : SetTheory) ⊆ 𝗘𝗤 ℒₛₑₜ ∪ bstAxioms := by
  intro σ h
  cases h with
  | equality φ hφ => exact Or.inl hφ
  | _ => right; simp [bstAxioms]

lemma bst_finite : Set.Finite (𝗕𝗦𝗧 : SetTheory) :=
  (Theory.EqAxiom.finite.union (by simp [bstAxioms])).subset bst_subset

noncomputable instance BST.delta1 : (𝗕𝗦𝗧 : SetTheory).Δ₁ := Theory.Δ₁.ofFinite _ bst_finite

noncomputable instance AC.delta1 : (𝗔𝗖 : SetTheory).Δ₁ := Theory.Δ₁.singleton Axiom.choice

/-- **𝗭𝗙𝗖 有 Δ1 的公理表示**（Foundation 意义下的 `Theory.Δ₁`）。 -/
noncomputable instance ZFC.delta1 : (𝗭𝗙𝗖 : SetTheory).Δ₁ := inferInstance

#print axioms ZFC.delta1

end GodelQ.ZFCDelta1
