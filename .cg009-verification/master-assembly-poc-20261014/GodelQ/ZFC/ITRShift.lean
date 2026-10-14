-- CG-009: iTR_shift — the atomic piece for iT_shift's rel/nrel branches.
import GodelQ.ZFC.ITShift

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.ITRShift
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

lemma one_lt_two_add' (n : V) : (1 : V) < 1 + (1 + n) := by
  have h := lt_add_self_add_one (1 : V) n
  have e : n + 1 + 1 = 1 + (1 + n) := by ring
  rwa [e] at h

/-- `(^#0 ∷ ^#1 ∷ 0)` is a SemitermVec at layer `2 + n`. -/
lemma isSemitermVec_two_bvars (n : V) :
    IsSemitermVec ℒₛₑₜ 2 (2 + n) ((^#0 : V) ∷ (^#1 : V) ∷ (0 : V)) := by
  rw [show (2 : V) = 1 + 1 by norm_num, IsSemitermVec.cons_iff]
  refine ⟨IsSemiterm.bvar.mpr (by
      simpa [show (2 : V) = 1 + 1 by norm_num, add_assoc] using zero_lt_two_add n), ?_⟩
  rw [show (1 : V) = 0 + 1 by norm_num, IsSemitermVec.cons_iff]
  refine ⟨IsSemiterm.bvar.mpr (by
      simpa [show (2 : V) = 1 + (1 + 0) by ring, add_assoc] using one_lt_two_add' n), by simp⟩

/-- `termShiftVec` fixes the two-bvar vector. -/
lemma termShiftVec_two_bvars :
    termShiftVec ℒₛₑₜ 2 ((^#0 : V) ∷ (^#1 : V) ∷ (0 : V)) = (^#0 : V) ∷ (^#1 : V) ∷ (0 : V) := by
  rw [termShiftVec_cons₂ (IsUTerm.bvar (z := 0)) (IsUTerm.bvar (z := 1)),
    termShift_bvar, termShift_bvar]

/-- **`iTR_shift`**: `iTR` commutes with the argument shift (binary rel case). -/
lemma iTR_shift {n R v : V} (hR : (ℒₒᵣ).IsRel 2 R) (hv : IsSemitermVec ℒₒᵣ 2 n v) :
    iTR n 2 R (termShiftVec ℒₒᵣ 2 v) = shift (L := ℒₛₑₜ) (iTR n 2 R v) := by
  rw [iTR, iTR]
  have h0 : (termShiftVec ℒₒᵣ 2 v).[0] = termShift ℒₒᵣ v.[0] :=
    nth_termShiftVec hv.isUTermVec (by norm_num)
  have h1 : (termShiftVec ℒₒᵣ 2 v).[1] = termShift ℒₒᵣ v.[1] :=
    nth_termShiftVec hv.isUTermVec (by norm_num)
  rw [h0, h1]
  have hs0 : IsSemiformula ℒₛₑₜ (n + 1) (iVE n v.[0]) :=
    isSemiformula_iVE (n := n) v.[0] (hv.nth (i := 0) (by norm_num))
  have hs1 : IsSemiformula ℒₛₑₜ (n + 1) (iVE n v.[1]) :=
    isSemiformula_iVE (n := n) v.[1] (hv.nth (i := 1) (by norm_num))
  have e0 : conjunct 2 n 0 (iVE n (termShift ℒₒᵣ v.[0])) =
      shift ℒₛₑₜ (conjunct 2 n 0 (iVE n v.[0])) := by
    rw [GodelQ.TranslateShiftCompat.iVE_shift n v.[0] (hv.nth (i := 0) (by norm_num))]
    exact (GodelQ.TranslateShiftCompat.shift_conjunct (b := 2) (n := n) (i := 0)
      (y := iVE n v.[0]) hs0 (zero_lt_two_add n)).symm
  have e1 : conjunct 2 n 1 (iVE n (termShift ℒₒᵣ v.[1])) =
      shift ℒₛₑₜ (conjunct 2 n 1 (iVE n v.[1])) := by
    rw [GodelQ.TranslateShiftCompat.iVE_shift n v.[1] (hv.nth (i := 1) (by norm_num))]
    exact (GodelQ.TranslateShiftCompat.shift_conjunct (b := 2) (n := n) (i := 1)
      (y := iVE n v.[1]) hs1 (one_lt_two_add n)).symm
  rw [e0, e1]
  have hA0 : IsSemiformula ℒₛₑₜ (2 + n) (conjunct 2 n 0 (iVE n v.[0])) :=
    isSemiformula_conjunct (b := 2) (n := n) (i := 0) hs0 (zero_lt_two_add n)
  have hA1 : IsSemiformula ℒₛₑₜ (2 + n) (conjunct 2 n 1 (iVE n v.[1])) :=
    isSemiformula_conjunct (b := 2) (n := n) (i := 1) hs1 (one_lt_two_add n)
  have hA01 : IsSemiformula ℒₛₑₜ (2 + n) (conjunct 2 n 1 (iVE n v.[1]) ^⋏ ^⊤) :=
    IsSemiformula.and.mpr ⟨hA1, IsSemiformula.verum⟩
  have hA : IsSemiformula ℒₛₑₜ (2 + n)
      (conjunct 2 n 0 (iVE n v.[0]) ^⋏ (conjunct 2 n 1 (iVE n v.[1]) ^⋏ ^⊤)) :=
    IsSemiformula.and.mpr ⟨hA0, hA01⟩
  have hB : IsSemiformula ℒₛₑₜ (2 + n) (subst ℒₛₑₜ (?[^#0, ^#1] : V) (cRel R)) := by
    apply IsSemiformula.subst (L := ℒₛₑₜ) (n := 2) (m := 2 + n)
    · exact isSemiformula_cRel R
    · rw [show (?[^#0, ^#1] : V) = (^#0 : V) ∷ (^#1 : V) ∷ 0 from rfl]
      exact isSemitermVec_two_bvars n
  have hbody : IsUFormula ℒₛₑₜ
      (imp ℒₛₑₜ (conjunct 2 n 0 (iVE n v.[0]) ^⋏ (conjunct 2 n 1 (iVE n v.[1]) ^⋏ ^⊤))
        (subst ℒₛₑₜ (?[^#0, ^#1] : V) (cRel R))) :=
    (IsSemiformula.imp.mpr ⟨hA, hB⟩).isUFormula
  rw [GodelQ.TranslateShiftCompat.shift_qqAlls hbody]
  congr 1
  -- goal: imp (shA0 ⋏ (shA1 ⋏ ⊤)) B = shift (imp (A0 ⋏ (A1 ⋏ ⊤)) B)
  --       where shAj = shift (conjunct ...) etc.
  -- Unfold imp on the RHS, then push shift inside.
  -- Unfold imp on both sides, then push shift inside (mirrors 9276's shift_ve2).
  simp only [imp]
  rw [shift_or hA.isUFormula.neg hB.isUFormula,
    shift_neg (L := ℒₛₑₜ) (n := 2 + n) hA]
  congr 1
  · -- neg part: shift A0 ⋏ (shift A1 ⋏ ⊤) = shift (A0 ⋏ (A1 ⋏ ⊤))
    rw [shift_and hA0.isUFormula hA01.isUFormula,
      shift_and hA1.isUFormula IsUFormula.verum,
      shift_verum (L := ℒₛₑₜ)]
  · -- closed cRel substitution: shift B = B (all entries are bvars)
    rw [show (?[^#0, ^#1] : V) = (^#0 : V) ∷ (^#1 : V) ∷ 0 from rfl]
    rw [shift_substs (L := ℒₛₑₜ) (n := 2) (m := 2 + n) (p := cRel R)
      (isSemiformula_cRel R) (isSemitermVec_two_bvars n)]
    rw [termShiftVec_two_bvars, GodelQ.TranslateShiftCompat.shift_cRel R]

end GodelQ.ITRShift

#print axioms GodelQ.ITRShift.iTR_shift
