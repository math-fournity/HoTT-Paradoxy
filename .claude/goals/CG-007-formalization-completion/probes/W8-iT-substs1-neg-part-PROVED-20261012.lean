import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

lemma substs_qqAlls : ∀ (k : ℕ) (X w : V), IsUFormula ℒₛₑₜ X →
    subst ℒₛₑₜ w (qqAlls X (k : V))
      = qqAlls (subst ℒₛₑₜ ((qVec ℒₛₑₜ)^[k] w) X) (k : V) := by
  intro k
  induction k with
  | zero => intro X w _; simp
  | succ j ih =>
    intro X w hX
    rw [show ((j + 1 : ℕ) : V) = (j : V) + 1 by push_cast; ring]
    rw [qqAlls_succ]
    have hu : IsUFormula ℒₛₑₜ (qqAlls X (j : V)) := isUFormula_qqAlls.mpr hX
    rw [Bootstrapping.substs_all (L := ℒₛₑₜ) hu]
    rw [ih X (qVec ℒₛₑₜ w) hX]
    rw [qqAlls_succ]
    congr 3

lemma qVec_two : (qVec ℒₛₑₜ)^[2] (?[^&0] : V) = (?[^#0, ^#1, ^&0] : V) := by
  rw [Function.iterate_succ_apply', Function.iterate_one]
  rw [show qVec ℒₛₑₜ (?[^&0] : V) = (?[^#0, ^&0] : V) from by
    rw [Bootstrapping.qVec, show len (?[^&0] : V) = (1:V) from by simp]
    rw [show (1:V) = 0 + 1 by norm_num,
      termBShiftVec_cons (IsUTerm.fvar (x := (0:V))) IsUTermVec.empty,
      termBShift_fvar, termBShiftVec_nil]]
  rw [Bootstrapping.qVec,
    show len (?[^#0, ^&0] : V) = (2:V) from by simp [len_adjoin, len_nil]; norm_num]
  rw [show (2:V) = 0 + 1 + 1 by norm_num,
    termBShiftVec_cons (IsUTerm.bvar (z := (0:V)))
      (IsUTermVec.adjoin IsUTermVec.empty (IsUTerm.fvar (x := (0:V)))),
    termBShift_bvar, show (0:V) + 1 = 1 by norm_num,
    termBShiftVec_cons₁ (IsUTerm.fvar (x := (0:V))), termBShift_fvar]

/-- `subst ?[^#0,^#1] (cRel R)` 的 `IsUFormula`（引号化句子）。 -/
lemma hC : IsUFormula ℒₛₑₜ (subst ℒₛₑₜ (?[^#0, ^#1] : V) (cRel (↑cEqN : V))) :=
  (IsSemiformula.subst (L := ℒₛₑₜ) (isSemiformula_cRel (↑cEqN : V))
    (IsSemitermVec.doubleton.mpr
      ⟨(IsSemiterm.bvar (L := ℒₛₑₜ) (V := V) (n := (2:V)) (z := (0:V))).mpr (by norm_num),
       (IsSemiterm.bvar (L := ℒₛₑₜ) (V := V) (n := (2:V)) (z := (1:V))).mpr (by norm_num)⟩)).isUFormula

/-- `A := conjunct 2 1 0 (iVE 1 ^#0) ⋏ (conjunct 2 1 1 (iVE 1 ^#0) ⋏ ⊤)` 的 `IsSemiformula 3`。 -/
lemma hA : IsSemiformula ℒₛₑₜ (3:V)
    (conjunct 2 1 0 (iVE (1:V) (^#0 : V)) ^⋏
      (conjunct 2 1 1 (iVE (1:V) (^#0 : V)) ^⋏ ^⊤)) :=
  IsSemiformula.and.mpr
    ⟨isSemiformula_conjunct (b := 2) (n := (1:V)) (i := (0:V))
      (isSemiformula_iVE (n := (1:V)) (^#0) (IsSemiterm.bvar.mpr (by norm_num)))
      (by norm_num),
     IsSemiformula.and.mpr
      ⟨isSemiformula_conjunct (b := 2) (n := (1:V)) (i := (1:V))
        (isSemiformula_iVE (n := (1:V)) (^#0) (IsSemiterm.bvar.mpr (by norm_num)))
        (by norm_num),
       IsSemiformula.verum⟩⟩

/-- **`neg` 分量**：`subst W (neg A) = neg (subst W A)`，再用 `conjunct_rename` 两次。 -/
lemma neg_part :
    subst ℒₛₑₜ (?[^#0, ^#1, ^&0] : V)
        (neg ℒₛₑₜ (conjunct 2 1 0 (iVE (1:V) (^#0 : V)) ^⋏
          (conjunct 2 1 1 (iVE (1:V) (^#0 : V)) ^⋏ ^⊤)))
      = neg ℒₛₑₜ (conjunct 2 0 0 (iVE (0:V) (^&0 : V)) ^⋏
          (conjunct 2 0 1 (iVE (0:V) (^&0 : V)) ^⋏ ^⊤)) := by
  have hlen : len (?[^#0, ^#1, ^&0] : V) = (3:V) := by
    rw [show (?[^#0, ^#1, ^&0] : V)
          = (^#0 : V) ∷ ((^#1 : V) ∷ ((^&0 : V) ∷ (0:V))) from rfl]
    simp only [len_adjoin, len_nil]
    norm_num
  have hW : IsSemitermVec ℒₛₑₜ (3:V) (2:V) (?[^#0, ^#1, ^&0] : V) :=
    IsSemitermVec.iff.mpr ⟨hlen,
      fun j hj ↦ by
        rw [show (?[^#0, ^#1, ^&0] : V)
              = (^#0 : V) ∷ ((^#1 : V) ∷ ((^&0 : V) ∷ (0:V))) from rfl]
        have hj3 : j < (3:V) := hj
        rcases zero_or_succ j with (rfl | ⟨l, rfl⟩)
        · simp only [nth_adjoin_zero]
          exact IsSemiterm.bvar.mpr (by norm_num)
        · rcases zero_or_succ l with (rfl | ⟨m, rfl⟩)
          · simp only [nth_adjoin_succ, nth_adjoin_zero]
            exact IsSemiterm.bvar.mpr (by norm_num)
          · have hm : m = 0 := by
              have h := hj3
              rw [show (3:V) = (1:V) + 1 + 1 from by norm_num] at h
              have h2 := (add_lt_add_iff_right (1:V)).mp ((add_lt_add_iff_right (1:V)).mp h)
              exact lt_one_iff_eq_zero.mp h2
            subst hm
            simp only [nth_adjoin_succ, nth_adjoin_zero]
            exact IsSemiterm.fvar (L := ℒₛₑₜ) (V := V) (n := (2:V)) 0⟩
  rw [Bootstrapping.substs_neg (L := ℒₛₑₜ) hA hW]
  congr 1
  -- `subst W (A0 ⋏ A1) = subst W A0 ⋏ subst W A1`
  have hA0s : IsSemiformula ℒₛₑₜ (3:V) (conjunct 2 1 0 (iVE (1:V) (^#0 : V))) :=
    isSemiformula_conjunct (b := 2) (n := (1:V)) (i := (0:V))
      (isSemiformula_iVE (n := (1:V)) (^#0) (IsSemiterm.bvar.mpr (by norm_num)))
      (by norm_num)
  have hA1s : IsSemiformula ℒₛₑₜ (3:V)
      (conjunct 2 1 1 (iVE (1:V) (^#0 : V)) ^⋏ ^⊤) :=
    IsSemiformula.and.mpr
      ⟨isSemiformula_conjunct (b := 2) (n := (1:V)) (i := (1:V))
        (isSemiformula_iVE (n := (1:V)) (^#0) (IsSemiterm.bvar.mpr (by norm_num)))
        (by norm_num), IsSemiformula.verum⟩
  rw [Bootstrapping.substs_and (L := ℒₛₑₜ) hA0s.isUFormula hA1s.isUFormula]
  congr 1
  · -- 第一分量：`conjunct_rename 0`
    exact conjunct_rename (i := (0:V)) (by norm_num)
  · -- 第二分量：`subst W (A1 ⋏ ⊤)`，先拆 `⋏`
    have hA1' : IsSemiformula ℒₛₑₜ (3:V) (conjunct 2 1 1 (iVE (1:V) (^#0 : V))) :=
      isSemiformula_conjunct (b := 2) (n := (1:V)) (i := (1:V))
        (isSemiformula_iVE (n := (1:V)) (^#0) (IsSemiterm.bvar.mpr (by norm_num)))
        (by norm_num)
    rw [Bootstrapping.substs_and (L := ℒₛₑₜ) hA1'.isUFormula IsUFormula.verum,
      Bootstrapping.substs_verum]
    exact congrArg (fun (x : V) => x ^⋏ (^⊤ : V)) (conjunct_rename (i := (1:V)) (by norm_num))

end GodelQ.ProbeFB
