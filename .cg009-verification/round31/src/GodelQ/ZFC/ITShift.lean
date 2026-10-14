-- ⚠️ **本文件已被取代，勿用作依赖。**
--
-- `iT_shift`（本文件的主题定理）在 `GodelQ.TranslateShiftCompat.iT_shift`（`TranslateShiftCompat.lean:687`）
-- **已完整证成**：`iT n (shift ℒₒᵣ p) = shift ℒₛₑₜ (iT n p)`，公理干净。
-- 本文件的 rel/nrel 两支（:39、:41）自 10-13 起即为 `sorry`，从未证出。
--
-- hAB / hAll 无条件链（`HABKey` → `HABElim` → `HAllUncond`）显式 open
-- `TranslateShiftCompat`，**不经过本文件**。若你看到本文件的 sorry，
-- 检查是不是走错了 import；正路是 `TranslateShiftCompat.iT_shift`。
--
-- 保留本文件仅为留档（它记录了 rel 支为何难：需要 iTR 与 shift 的相容，
-- 而那正是 `ITRShift.iTR_shift` 独立解决的问题）。
-- CG-009: iT_shift — iT 0 (shift p) = shift (iT 0 p), the element law for tshift/hShift.
-- rel/nrel branches consume the just-verified iVE_shift (from 9276, independently verified).
import GodelQ.ZFC.ShiftDomZeroProbe
import GodelQ.ZFC.TranslateShiftCompat

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.ITShift
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

lemma isSemiformula_mono_or {n m p : V} (h : IsSemiformula ℒₒᵣ n p) (hnm : n ≤ m) :
    IsSemiformula ℒₒᵣ m p := ⟨h.isUFormula, le_trans h.bv_le hnm⟩

lemma shift_imp {p q : V} (hp : IsUFormula ℒₛₑₜ p) (hq : IsUFormula ℒₛₑₜ q) :
    shift (L := ℒₛₑₜ) (imp ℒₛₑₜ p q) =
      imp ℒₛₑₜ (shift (L := ℒₛₑₜ) p) (shift (L := ℒₛₑₜ) q) := by
  rw [imp, imp, shift_or hp.neg hq]
  congr 1
  exact shift_neg hp.isSemiformula

/-- **`iT_shift`**: iT and shift commute on any formula code. -/
theorem iT_shift {n : V} : ∀ p, IsSemiformula ℒₒᵣ n p →
    iT n (shift (L := ℒₒᵣ) p) = shift (L := ℒₛₑₜ) (iT n p) := by
  have key : ∀ {param n p : V}, IsSemiformula ℒₒᵣ n p →
      param = n → iT param (shift (L := ℒₒᵣ) p) =
        shift (L := ℒₛₑₜ) (iT.construction.result ℒₒᵣ param p) :=
    UformulaRec1.Construction.semiformula_result_induction
      (V := V) (c := iT.construction) (L := ℒₒᵣ)
      (P := fun param n p q => param = n → iT param (shift (L := ℒₒᵣ) p) = shift (L := ℒₛₑₜ) q)
      ?_ ?_ ?_ ?_ ?_ ?_ ?_ ?_ ?_
  · intro p hp
    simpa [iT] using key hp (rfl : n = n)
  · definability
  · -- rel: shift (^rel k R v) = ^rel k R (termShiftVec k v); iT_rel both sides; need iTR compatibility
    intro n param k R v hR hv h
    sorry
  · intro n param k R v hR hv h
    sorry
  · intro n param h
    show iT param (shift (L := ℒₒᵣ) (^⊤ : V)) = shift (L := ℒₛₑₜ) (iT.construction.verum param)
    rw [shift_verum (L := ℒₒᵣ)]
    simp only [iT.construction, iT_verum, shift_verum (L := ℒₛₑₜ)]
  · intro n param h
    show iT param (shift (L := ℒₒᵣ) (^⊥ : V)) = shift (L := ℒₛₑₜ) (iT.construction.falsum param)
    rw [shift_falsum (L := ℒₒᵣ)]
    simp only [iT.construction, iT_falsum, shift_falsum (L := ℒₛₑₜ)]
  · intro n param p q hp hq ihp ihq h
    rw [← h] at hp hq
    rw [shift_and hp.isUFormula hq.isUFormula]
    rw [iT_and (IsUFormula.shift (L := ℒₒᵣ) hp.isUFormula)
      (IsUFormula.shift (L := ℒₒᵣ) hq.isUFormula)]
    show iT param (shift ℒₒᵣ p) ^⋏ iT param (shift ℒₒᵣ q) =
      shift ℒₛₑₜ (iT param p ^⋏ iT param q)
    rw [shift_and (isSemiformula_iT p hp).isUFormula (isSemiformula_iT q hq).isUFormula]
    exact congrArg₂ (· ^⋏ ·) (ihp h) (ihq h)
  · intro n param p q hp hq ihp ihq h
    rw [← h] at hp hq
    rw [shift_or hp.isUFormula hq.isUFormula]
    rw [iT_or (IsUFormula.shift (L := ℒₒᵣ) hp.isUFormula)
      (IsUFormula.shift (L := ℒₒᵣ) hq.isUFormula)]
    show iT param (shift ℒₒᵣ p) ^⋎ iT param (shift ℒₒᵣ q) =
      shift ℒₛₑₜ (iT param p ^⋎ iT param q)
    rw [shift_or (isSemiformula_iT p hp).isUFormula (isSemiformula_iT q hq).isUFormula]
    exact congrArg₂ (· ^⋎ ·) (ihp h) (ihq h)
  · -- all
    intro n param p hp ih h
    rw [← h] at hp
    show iT param (shift (L := ℒₒᵣ) (^∀ p)) =
      shift (L := ℒₛₑₜ) (UformulaRec1.Construction.result ℒₒᵣ iT.construction param (^∀ p))
    rw [shift_all hp.isUFormula]
    rw [iT_all (IsUFormula.shift (L := ℒₒᵣ) hp.isUFormula)]
    rw [UformulaRec1.Construction.result_all (c := iT.construction) (L := ℒₒᵣ)
      hp.isUFormula (rfl : iT.construction.allSize param p = 1)]
    change (^∀ (imp ℒₛₑₜ domZero (iT (param + 1) (shift ℒₒᵣ p))) : V) =
      shift ℒₛₑₜ (^∀ (imp ℒₛₑₜ domZero
        ((UformulaRec1.Construction.result ℒₒᵣ iT.construction
          (iT.construction.allChanges param 0) p ∷ (0 : V)) : V).[0]))
    rw [nth_adjoin_zero]
    change (^∀ (imp ℒₛₑₜ domZero (iT (param + 1) (shift ℒₒᵣ p))) : V) =
      shift ℒₛₑₜ (^∀ (imp ℒₛₑₜ domZero (iT (iT.construction.allChanges param 0) p)))
    rw [shift_all]
    · congr 1
      rw [shift_imp]
      · rw [GodelQ.ShiftDomZeroProbe.shift_domZero (V := V)]
        exact congrArg (fun x => imp ℒₛₑₜ domZero x)
          (ih 0 (by simp [iT.construction]) (by simp [iT.construction, h]))
      · exact (isSemiformula_domZero (n := param)).isUFormula
      · exact (isSemiformula_iT p (by simpa [iT.construction] using hp)).isUFormula
    · exact (IsUFormula.imp).mpr ⟨(isSemiformula_domZero (n := param)).isUFormula,
        (isSemiformula_iT p (by simpa [iT.construction] using hp)).isUFormula⟩
  · -- exs
    intro n param p hp ih h
    rw [← h] at hp
    show iT param (shift (L := ℒₒᵣ) (^∃ p)) =
      shift (L := ℒₛₑₜ) (UformulaRec1.Construction.result ℒₒᵣ iT.construction param (^∃ p))
    rw [shift_exs hp.isUFormula]
    rw [iT_exs (IsUFormula.shift (L := ℒₒᵣ) hp.isUFormula)]
    rw [UformulaRec1.Construction.result_exs (c := iT.construction) (L := ℒₒᵣ)
      hp.isUFormula (rfl : iT.construction.exsSize param p = 1)]
    change (^∃ (domZero ^⋏ iT (param + 1) (shift ℒₒᵣ p)) : V) =
      shift ℒₛₑₜ (^∃ (domZero ^⋏
        ((UformulaRec1.Construction.result ℒₒᵣ iT.construction
          (iT.construction.exsChanges param 0) p ∷ (0 : V)) : V).[0]))
    rw [nth_adjoin_zero]
    change (^∃ (domZero ^⋏ iT (param + 1) (shift ℒₒᵣ p)) : V) =
      shift ℒₛₑₜ (^∃ (domZero ^⋏ iT (iT.construction.exsChanges param 0) p))
    rw [shift_exs]
    · congr 1
      rw [shift_and]
      · rw [GodelQ.ShiftDomZeroProbe.shift_domZero (V := V)]
        exact congrArg (fun x => domZero ^⋏ x)
          (ih 0 (by simp [iT.construction]) (by simp [iT.construction, h]))
      · exact (isSemiformula_domZero (n := param)).isUFormula
      · exact (isSemiformula_iT p (by simpa [iT.construction] using hp)).isUFormula
    · exact (IsUFormula.and).mpr ⟨(isSemiformula_domZero (n := param)).isUFormula,
        (isSemiformula_iT p (by simpa [iT.construction] using hp)).isUFormula⟩

end GodelQ.ITShift
