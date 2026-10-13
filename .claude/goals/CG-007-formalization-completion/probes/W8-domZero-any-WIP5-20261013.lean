import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`subst (qVec w) domZero = domZero`**（只要求 `w` 是**项向量**，层数任意）。

`domZero` **层 1**，`subst` 只看向量**第 0 格**；
`(qVec w).[0] = ^#0`（`qVec` 的定义），**与 `w` 的层数无关**。
用 `subst_congr_prefix'` 把 `qVec w` 缩到 `?[^#0]`。 -/
lemma subst_qVec_domZero_any (w : V) (hw : IsUTermVec ℒₛₑₜ (len w) w) :
    subst ℒₛₑₜ (qVec ℒₛₑₜ w) (domZero (V := V)) = domZero (V := V) := by
  rw [domZero_eq_cDomN (V := V)]
  refine (subst_congr_prefix' (L := ℒₛₑₜ) (n := (1:V)) (m := (1:V))
    (k₁ := len (qVec ℒₛₑₜ w)) (k₂ := (1:V)) ((cDomN : ℕ) : V)
    (isSemiformula_cDomN (V := V))
    (by rw [len_qVec hw]; exact one_le_len_add_one w)
    (by norm_num)
    (by
      -- `qVec w` 的项向量性（层取 1）
      refine IsSemitermVec.iff (L := ℒₛₑₜ) (k := len (qVec ℒₛₑₜ w)) (n := (1:V))
        (v := qVec ℒₛₑₜ w) |>.mpr ⟨rfl, fun i hi ↦ ?_⟩
      rw [show (qVec ℒₛₑₜ w) = (^#0 : V) ∷ termBShiftVec ℒₛₑₜ (len w) w from rfl] at hi ⊢
      rcases zero_or_succ i with (rfl | ⟨j, rfl⟩)
      · rw [nth_adjoin_zero]
        exact (IsSemiterm.bvar (L := ℒₛₑₜ) (V := V) (n := (1:V)) (z := (0:V))).mpr (by norm_num)
      · rw [nth_adjoin_succ]
        have hj : j < len w := by
          have h := (add_lt_add_iff_right (1:V)).mp (by simpa using hi)
          rwa [len_termBShiftVec (V := V) (L := ℒₛₑₜ) hw] at h
        exact ⟨(hw.nth hj).isUTerm.termBShift, by
          have hb := (termBV_termBShift_le (L := ℒₛₑₜ) (hw.nth hj).isUTerm (len w)).mpr
            (hw.nth hj).bv
          simpa using hb⟩)
    (IsSemitermVec.singleton.mpr
      ((IsSemiterm.bvar (L := ℒₛₑₜ) (V := V) (n := (1:V)) (z := (0:V))).mpr (by norm_num)))
    (fun j hj ↦ by
      have hj0 : j = 0 := lt_one_iff_eq_zero.mp hj
      subst hj0
      rw [show (qVec ℒₛₑₜ w).[0] = (^#0 : V) from by
        rw [show (qVec ℒₛₑₜ w) = (^#0 : V) ∷ termBShiftVec ℒₛₑₜ (len w) w from rfl]
        rw [nth_adjoin_zero]]
      rw [show (?[^#0] : V).[0] = (^#0 : V) from by
        rw [show (?[^#0] : V) = ((^#0 : V) ∷ (0:V)) from rfl]
        rw [nth_adjoin_zero]])).trans ?_
  refine subst_eq_self (L := ℒₛₑₜ) (n := (1:V)) (w := (?[^#0] : V))
    (isSemiformula_cDomN (V := V))
    (IsSemitermVec.singleton.mpr
      ((IsSemiterm.bvar (L := ℒₛₑₜ) (V := V) (n := (1:V)) (z := (0:V))).mpr (by norm_num))) ?_
  intro i hi
  have hz : i = 0 := lt_one_iff_eq_zero.mp hi
  subst hz
  rw [show (?[^#0] : V).[0] = (^#0 : V) from by
    rw [show (?[^#0] : V) = ((^#0 : V) ∷ (0:V)) from rfl]
    rw [nth_adjoin_zero]]

end GodelQ.ProbeFL
