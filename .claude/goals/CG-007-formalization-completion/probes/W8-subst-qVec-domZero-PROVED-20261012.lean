import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeDF2
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **关键子步骤**：`subst (qVec ?[^&0]) domZero = domZero`。

`domZero = subst ?[^#0] cDomN`，`qVec ?[^&0] = ?[^#0, ^&0]`。
用 `substs_substs`：`termSubstVec 1 ?[^#0,^&0] ?[^#0] = ?[^#0]`。 -/
lemma subst_qVec_domZero : subst ℒₛₑₜ (qVec ℒₛₑₜ (?[^&0] : V)) (domZero (V := V))
    = domZero (V := V) := by
  -- `domZero = cDomN`（引号化句子，层数 1 且 bvar 全在引号内）
  rw [show qVec ℒₛₑₜ (?[^&0] : V) = (?[^#0, ^&0] : V) from by
    rw [Bootstrapping.qVec, show len (?[^&0] : V) = (1:V) from by simp]
    rw [show (1:V) = 0 + 1 by norm_num,
      termBShiftVec_cons (IsUTerm.fvar (x := (0:V))) IsUTermVec.empty,
      termBShift_fvar, termBShiftVec_nil]]
  rw [domZero_eq_cDomN (V := V)]
  -- 目标：`subst ?[^#0,^&0] cDomN = cDomN`；用 `subst_congr_prefix` 缩到 `?[^#0]`
  have hd : IsSemiformula ℒₛₑₜ (1:V) ((cDomN : ℕ) : V) := isSemiformula_cDomN (V := V)
  have hcp : subst ℒₛₑₜ (?[^#0, ^&0] : V) ((cDomN : ℕ) : V)
      = subst ℒₛₑₜ (?[^#0] : V) ((cDomN : ℕ) : V) :=
    subst_congr_prefix (V := V) (n := (1:V)) (m := (1:V) + 1) (k₁ := (1:V) + 1) (k₂ := (1:V))
      (w := (?[^#0, ^&0] : V)) (w' := (?[^#0] : V)) ((cDomN : ℕ) : V) hd
      (by norm_num) (by norm_num)
      (by
        refine IsSemitermVec.iff.mpr ⟨by simp [len_adjoin, len_nil], fun j hj ↦ ?_⟩
        have hj' : j < 1 + 1 := by norm_num at hj ⊢; exact hj
        rw [show (?[^#0, ^&0] : V) = (^#0 : V) ∷ ((^&0 : V) ∷ (0:V)) from rfl]
        rcases zero_or_succ j with (rfl | ⟨l, rfl⟩)
        · simpa only [nth_adjoin_zero] using
            (IsSemiterm.bvar (L := ℒₛₑₜ) (V := V) (n := (1:V) + 1) (z := (0:V))).mpr
              (by norm_num)
        · have hl : l = 0 := by
            have h := hj'
            rw [show 1 + 1 = (1:V) + 1 from rfl] at h
            exact lt_one_iff_eq_zero.mp ((add_lt_add_iff_right (1:V)).mp h)
          subst hl
          simp only [nth_adjoin_succ, nth_adjoin_zero]
          exact IsSemiterm.fvar (L := ℒₛₑₜ) (V := V) (n := (1:V) + 1) 0)
      (IsSemitermVec.singleton.mpr (IsSemiterm.bvar.mpr (by norm_num)))
      (fun j hj ↦ by
        rw [show j = 0 from lt_one_iff_eq_zero.mp hj]
        simp)
  rw [hcp]
  exact domZero_eq_cDomN (V := V) ▸ (subst_eq_self (L := ℒₛₑₜ) (n := (1:V))
    (w := (?[^#0] : V)) (p := ((cDomN : ℕ) : V)) hd
    (isSemitermVec_single_bvar (n := (1:V)) (by norm_num))
    (fun i hi ↦ by rw [show i = 0 from lt_one_iff_eq_zero.mp hi]; simp))

end GodelQ.ProbeDF2
