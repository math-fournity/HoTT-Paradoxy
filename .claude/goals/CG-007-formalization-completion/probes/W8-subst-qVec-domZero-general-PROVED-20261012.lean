import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFI
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`subst (qVec w) domZero = domZero`**（`w` 是层数 1 的项向量）。

`domZero = cDomN` 层数 1，`qVec w` 首分量恒为 `^#0`，
故 `subst_congr_prefix` 把它缩到 `?[^#0]`，再用 `subst_eq_self`。 -/
lemma subst_qVec_domZero' {w : V} (hw : IsSemitermVec ℒₛₑₜ (len w) (1:V) w) :
    subst ℒₛₑₜ (qVec ℒₛₑₜ w) (domZero (V := V)) = domZero (V := V) := by
  rw [domZero_eq_cDomN (V := V)]
  have hd : IsSemiformula ℒₛₑₜ (1:V) ((cDomN : ℕ) : V) := isSemiformula_cDomN (V := V)
  have hlen : (1:V) ≤ len (qVec ℒₛₑₜ w) := by
    rw [Bootstrapping.qVec]; simp [len_adjoin]
  -- `qVec w` 的项向量性（层数 2：`^#0` 与 `termBShift` 后的 bvar）
  have hW : IsSemitermVec ℒₛₑₜ (len (qVec ℒₛₑₜ w)) (2:V) (qVec ℒₛₑₜ w) := by
    refine IsSemitermVec.iff.mpr ⟨rfl, fun j hj ↦ ?_⟩
    have hj' : j < len (termBShiftVec ℒₛₑₜ (len w) w) + 1 := by
      rw [← len_adjoin, ← Bootstrapping.qVec]; exact hj
    rcases zero_or_succ j with (rfl | ⟨l, rfl⟩)
    · rw [show (qVec ℒₛₑₜ w).[0] = (^#0 : V) from by
        rw [Bootstrapping.qVec]; simp only [nth_adjoin_zero]]
      exact IsSemiterm.bvar.mpr (by norm_num)
    · have hl : l < len w := by
        have h := (add_lt_add_iff_right (1:V)).mp hj'
        rw [show len (termBShiftVec ℒₛₑₜ (len w) w) = len w from
          len_termBShiftVec (V := V) (L := ℒₛₑₜ) (k := len w) (ts := w) hw.isUTerm] at h
        exact h
      have hq1 : (qVec ℒₛₑₜ w).[l + 1] = (termBShiftVec ℒₛₑₜ (len w) w).[l] := by
        rw [Bootstrapping.qVec]
        exact nth_adjoin_succ _ _ _
      rw [hq1, nth_termBShiftVec (V := V) (L := ℒₛₑₜ) (k := len w) (ts := w) (i := l)
        hw.isUTerm hl]
      -- `w.[l]` 层数 1，`termBShift` 后 bv 加一 ⟹ 层数 ≤ 2
      have hbv : termBV ℒₛₑₜ (termBShift ℒₛₑₜ w.[l]) ≤ (1:V) + 1 :=
        (termBV_termBShift_le (L := ℒₛₑₜ) (hw.nth hl).isUTerm (1:V)).mpr (hw.nth hl).bv
      exact ⟨(hw.nth hl).isUTerm.termBShift, by norm_num at hbv ⊢; exact hbv⟩
  refine (subst_congr_prefix (V := V) (n := (1:V)) (m := (2:V))
    (k₁ := len (qVec ℒₛₑₜ w)) (k₂ := (1:V))
    (w := (qVec ℒₛₑₜ w)) (w' := (?[^#0] : V)) ((cDomN : ℕ) : V) hd
    hlen (by norm_num) hW
    (IsSemitermVec.singleton.mpr (IsSemiterm.bvar.mpr (by norm_num)))
    (fun j hj ↦ by
      have hj0 : j = 0 := lt_one_iff_eq_zero.mp hj
      subst hj0
      rw [show (qVec ℒₛₑₜ w).[0] = (^#0 : V) from by
        rw [Bootstrapping.qVec]; simp only [nth_adjoin_zero]]
      rw [show (?[^#0] : V).[0] = (^#0 : V) from by simp only [nth_adjoin_zero]])).trans ?_
  refine subst_eq_self (L := ℒₛₑₜ) (n := (1:V)) (w := (?[^#0] : V))
    (p := ((cDomN : ℕ) : V)) hd
    (isSemitermVec_single_bvar (n := (1:V)) (by norm_num)) ?_
  intro i hi
  have hz : i = 0 := lt_one_iff_eq_zero.mp hi
  subst hz
  simp

end GodelQ.ProbeFI
