-- CG-009: iT_shift — full version, all nine branches.
import GodelQ.ZFC.ITRShift

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.ITShiftFull
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

lemma shift_imp {p q : V} (hp : IsUFormula ℒₛₑₜ p) (hq : IsUFormula ℒₛₑₜ q) :
    shift (L := ℒₛₑₜ) (imp ℒₛₑₜ p q) =
      imp ℒₛₑₜ (shift (L := ℒₛₑₜ) p) (shift (L := ℒₛₑₜ) q) := by
  rw [imp, imp, shift_or hp.neg hq]
  congr 1
  exact shift_neg hp.isSemiformula

/-- **`iT_shift`** (full): `iT` and `shift` commute on any formula code. -/
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
  · -- rel: shift (^rel k R v) = ^rel k R (termShiftVec k v); iT_rel both sides
    intro n param k R v hR hv h
    rw [← h] at hv
    have hk2 : k = 2 := by
      rcases Arithmetic.isRel_iff_LOR.mp hR with h' | h' <;> exact h'.1
    subst hk2
    rw [shift_rel (L := ℒₒᵣ) hR hv.isUTermVec]
    show iT param (^rel 2 R (termShiftVec ℒₒᵣ 2 v)) =
      shift ℒₛₑₜ (iT.construction.rel param 2 R v)
    rw [iT_rel hR (hv.termShiftVec.isUTermVec)]
    change iTR param 2 R (termShiftVec ℒₒᵣ 2 v) =
      shift ℒₛₑₜ (iT.construction.rel param 2 R v)
    exact GodelQ.ITRShift.iTR_shift hR hv
  · -- nrel: shift (^nrel k R v) = ^nrel k R (termShiftVec k v); use iTR_shift + shift_neg
    intro n param k R v hR hv h
    rw [← h] at hv
    have hk2 : k = 2 := by
      rcases Arithmetic.isRel_iff_LOR.mp hR with h' | h' <;> exact h'.1
    subst hk2
    rw [shift_nrel (L := ℒₒᵣ) hR hv.isUTermVec]
    show iT param (^nrel 2 R (termShiftVec ℒₒᵣ 2 v)) =
      shift ℒₛₑₜ (iT.construction.nrel param 2 R v)
    rw [iT_nrel hR (hv.termShiftVec.isUTermVec)]
    change neg ℒₛₑₜ (iTR param 2 R (termShiftVec ℒₒᵣ 2 v)) =
      shift ℒₛₑₜ (iT.construction.nrel param 2 R v)
    show neg ℒₛₑₜ (iTR param 2 R (termShiftVec ℒₒᵣ 2 v)) =
      shift ℒₛₑₜ (neg ℒₛₑₜ (iTR param 2 R v))
    rw [shift_neg (L := ℒₛₑₜ) (n := param)
      (isSemiformula_iTR (n := param) hR (h ▸ hv))]
    rw [GodelQ.ITRShift.iTR_shift hR hv]
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

end GodelQ.ITShiftFull

#print axioms GodelQ.ITShiftFull.iT_shift
