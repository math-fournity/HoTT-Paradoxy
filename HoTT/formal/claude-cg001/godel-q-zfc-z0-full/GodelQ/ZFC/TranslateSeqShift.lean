import GodelQ.ZFC.ITShift
import GodelQ.ZFC.SeqTranslate

/-!
# CG-007 · W8 第二层（十六）：`translateSeq` 与 `setShift` 的相容律

`ShCraigElim` 的 `shiftRule` 支需要：推导的结论 sequent 在 `setShift` 下
翻译仍可证。逐元素看（`mem_translateSeq_iff` + `mem_setShift_iff`），
两边都是 `∃ x ∈ s, y = shift (iT 0 x)`，中间用 `ITShift.iT_shift`
（`iT n (shift p) = shift (iT n p)`，2026-10-11 证出）换名。
-/

set_option maxHeartbeats 2000000

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

namespace GodelQ.TranslateSeqShift

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`translateSeq` 与 `setShift` 相容**：逐元素换名。

`y ∈ translateSeq (setShift s)` ⟺ `∃ x ∈ setShift s, y = iT 0 x`
⟺ `∃ x' ∈ s, y = iT 0 (shift x')` ⟺（`iT_shift`）`∃ x' ∈ s, y = shift (iT 0 x')`
⟺ `y ∈ setShift (translateSeq s)`。 -/
lemma translateSeq_setShift {s : V} (hs : IsFormulaSet (L := ℒₒᵣ) s) :
    translateSeq (V := V) (setShift ℒₒᵣ s) =
      setShift ℒₛₑₜ (translateSeq (V := V) s) := by
  apply Arithmetic.mem_ext; intro y
  simp only [mem_translateSeq_iff, mem_setShift_iff]
  constructor
  · rintro ⟨x, ⟨x', hx', rfl⟩, rfl⟩
    exact ⟨iT (0 : V) x', ⟨x', hx', rfl⟩, GodelQ.ITShift.iT_shift (n := 0) x' (hs x' hx')⟩
  · rintro ⟨z, ⟨x', hx', rfl⟩, rfl⟩
    exact ⟨shift ℒₒᵣ x', ⟨x', hx', rfl⟩,
      (GodelQ.ITShift.iT_shift (n := 0) x' (hs x' hx')).symm⟩

end GodelQ.TranslateSeqShift

#print axioms GodelQ.TranslateSeqShift.translateSeq_setShift
