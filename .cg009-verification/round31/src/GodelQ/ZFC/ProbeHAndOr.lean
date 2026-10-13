import GodelQ.ZFC.ShCraigElimNegLaw
import GodelQ.ZFC.ShCraigElimBranches

/-!
# DEVELOPMENT_PROBE / NOT_A_RECEIPT / NOT_A_CLAIM

身份：开发探针。测 `hAnd`/`hOr` 两支能否用已有零件接上。
- `andIntro`：`p ⋏ q ∈ s`，子推导结论 `insert p s` 与 `insert q s`。
- `orIntro`：`p ⋎ q ∈ s`，子推导结论 `insert p (insert q s)`。
关键零件是 `translateSeq_insert`（`[simp]`，把 `insert` 推进翻译）。
**不是**收据源，**不是**数学主张。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

namespace GodelQ.ProbeHAndOr

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`hAnd` 支**：`p ⋏ q ∈ s`，两条子推导分别给出 `insert p s` 与 `insert q s` 的结论。 -/
lemma hAnd {s p q dp dq : V} (h : p ^⋏ q ∈ s)
    (ihp : GodelQ.ShCraigElimSetup.Q (V := V) dp) (ihq : GodelQ.ShCraigElimSetup.Q (V := V) dq)
    (hdp : fstIdx dp = insert p s) (hdq : fstIdx dq = insert q s) :
    GodelQ.ShCraigElimSetup.Q (V := V) (andIntro s p q dp dq) := by
  simp only [GodelQ.ShCraigElimSetup.Q, fstIdx_andIntro]
  simp only [GodelQ.ShCraigElimSetup.Q] at ihp ihq
  rw [hdp] at ihp
  rw [hdq] at ihq
  simp only [translateSeq_insert] at ihp ihq
  exact Derivable.and_m h ihp ihq

/-- **`hOr` 支**：`p ⋎ q ∈ s`，子推导给出 `insert p (insert q s)` 的结论。 -/
lemma hOr {s p q dpq : V} (h : p ^⋎ q ∈ s)
    (ih : GodelQ.ShCraigElimSetup.Q (V := V) dpq) (hd : fstIdx dpq = insert p (insert q s)) :
    GodelQ.ShCraigElimSetup.Q (V := V) (orIntro s p q dpq) := by
  simp only [GodelQ.ShCraigElimSetup.Q, fstIdx_orIntro]
  simp only [GodelQ.ShCraigElimSetup.Q] at ih
  rw [hd] at ih
  simp only [translateSeq_insert] at ih
  exact Derivable.or_m h ih

end GodelQ.ProbeHAndOr

#print axioms GodelQ.ProbeHAndOr.hAnd
#print axioms GodelQ.ProbeHAndOr.hOr
