import GodelQ.ZFC.ShCraigElimBranches
import GodelQ.ZFC.TranslateShiftCompat

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup
open GodelQ.TranslateShiftCompat

set_option maxHeartbeats 800000

namespace GodelQ.ProbeO

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`translateSeq` 与 `setShift` 交换**（需要 `s` 是公式集，才拿到 `IsSemiformula`）。

逐元素用 `mem_translateSeq_iff` + `mem_setShift_iff`，公式性交给 `iT_shift`。 -/
lemma translateSeq_setShift {s : V} (hs : IsFormulaSet (L := ℒₒᵣ) s) :
    translateSeq (setShift (L := ℒₒᵣ) s) = setShift (L := ℒₛₑₜ) (translateSeq s) := by
  apply mem_ext; intro y
  simp only [mem_translateSeq_iff, mem_setShift_iff]
  constructor
  · rintro ⟨x, ⟨z, hz, rfl⟩, rfl⟩
    exact ⟨iT 0 z, ⟨z, hz, rfl⟩, iT_shift (n := 0) z (hs z hz)⟩
  · rintro ⟨w, ⟨z, hz, rfl⟩, rfl⟩
    exact ⟨shift ℒₒᵣ z, ⟨z, hz, rfl⟩, (iT_shift (n := 0) z (hs z hz)).symm⟩

/-- **`hShift` 支**：`s = setShift (fstIdx d)`，子推导在 `fstIdx d` 上。

`Derivable.shift` 直接给 `Derivable 𝗭𝗙𝗖 (setShift (translateSeq (fstIdx d)))`，
再用 `translateSeq_setShift` 换回 `translateSeq s`。 -/
lemma hShift {s d : V} (hs : IsFormulaSet (L := ℒₒᵣ) s)
    (h : s = setShift (L := ℒₒᵣ) (fstIdx d)) (ih : Q (V := V) d) :
    Q (V := V) (shiftRule s d) := by
  have hfs : IsFormulaSet (L := ℒₒᵣ) (fstIdx d) := by
    rw [h] at hs
    simpa using (IsFormulaSet.setShift_iff (L := ℒₒᵣ) (s := fstIdx d)).mp hs
  simp only [Q, fstIdx_shiftRule, h]
  rw [translateSeq_setShift hfs]
  exact Derivable.shift ih

end GodelQ.ProbeO
