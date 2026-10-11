-- CG-009 round 31: ishift — the all-branch, as a named theorem.
--   Given the IH at layer n+1, iT/shift commute on (^∀ q).
-- Route: shift_all → iT_all (both sides) → shift_imp → shift_domZero → IH.
import GodelQ.ZFC.ShiftDomZeroProbe

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.IShiftAllBranch

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

lemma isSemiformula_mono_or {n m p : V} (h : IsSemiformula ℒₒᵣ n p) (hnm : n ≤ m) :
    IsSemiformula ℒₒᵣ m p := ⟨h.isUFormula, le_trans h.bv_le hnm⟩

/-- shift distributes over imp (ℒₛₑₜ level). -/
lemma shift_imp {p q : V} (hp : IsUFormula ℒₛₑₜ p) (hq : IsUFormula ℒₛₑₜ q) :
    shift (L := ℒₛₑₜ) (imp ℒₛₑₜ p q) =
      imp ℒₛₑₜ (shift (L := ℒₛₑₜ) p) (shift (L := ℒₛₑₜ) q) := by
  rw [imp, imp, shift_or hp.neg hq]
  congr 1
  exact shift_neg hp.isSemiformula

/-- **The `all` branch of `ishift`**: at layer `n`, assuming the IH at layer `n+1`. -/
theorem ishift_all {n q : V} (hq : IsSemiformula ℒₒᵣ (n + 1) q)
    (ih : iT (n + 1) (shift (L := ℒₒᵣ) q) = shift (L := ℒₛₑₜ) (iT (n + 1) q)) :
    iT n (shift (L := ℒₒᵣ) (^∀ q)) = shift (L := ℒₛₑₜ) (iT n (^∀ q)) := by
  rw [shift_all hq.isUFormula, iT_all hq.isUFormula]
  rw [iT_all (IsUFormula.shift (L := ℒₒᵣ) hq.isUFormula)]
  rw [shift_all]
  · congr 1
    rw [shift_imp]
    · rw [GodelQ.ShiftDomZeroProbe.shift_domZero (V := V)]
      exact congrArg (fun x => imp ℒₛₑₜ domZero x) ih
    · exact (isSemiformula_domZero (n := n)).isUFormula
    · exact (isSemiformula_iT (n := n + 1) q hq).isUFormula
  · exact (IsUFormula.imp).mpr ⟨(isSemiformula_domZero (n := n)).isUFormula,
      (isSemiformula_iT (n := n + 1) q hq).isUFormula⟩

end GodelQ.IShiftAllBranch

#print axioms GodelQ.IShiftAllBranch.ishift_all

namespace GodelQ.IShiftAllBranch

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **The `exs` branch of `ishift`** (dual of `ishift_all`). -/
theorem ishift_exs {n q : V} (hq : IsSemiformula ℒₒᵣ (n + 1) q)
    (ih : iT (n + 1) (shift (L := ℒₒᵣ) q) = shift (L := ℒₛₑₜ) (iT (n + 1) q)) :
    iT n (shift (L := ℒₒᵣ) (^∃ q)) = shift (L := ℒₛₑₜ) (iT n (^∃ q)) := by
  rw [shift_exs hq.isUFormula, iT_exs hq.isUFormula]
  rw [iT_exs (IsUFormula.shift (L := ℒₒᵣ) hq.isUFormula)]
  rw [shift_exs]
  · congr 1
    rw [shift_and]
    · rw [GodelQ.ShiftDomZeroProbe.shift_domZero (V := V)]
      exact congrArg (fun x => domZero ^⋏ x) ih
    · exact (isSemiformula_domZero (n := n)).isUFormula
    · exact (isSemiformula_iT (n := n + 1) q hq).isUFormula
  · exact (IsUFormula.and).mpr ⟨(isSemiformula_domZero (n := n)).isUFormula,
      (isSemiformula_iT (n := n + 1) q hq).isUFormula⟩

end GodelQ.IShiftAllBranch

#print axioms GodelQ.IShiftAllBranch.ishift_exs
