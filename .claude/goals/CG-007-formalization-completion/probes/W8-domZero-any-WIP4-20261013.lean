import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`subst (qVec w) domZero = domZero`**（只要求首格是 `^#0`——这是定义）。

`domZero` **层 1**，故 `subst` 只看向量**第 0 格**；`(qVec w).[0] = ^#0`（定义即得）。
**不需要 `qVec w` 是层 1 的项向量**——用 `subst_congr_prefix'` 缩到 `?[^#0]` 即可。 -/
lemma subst_qVec_domZero_any (w : V) :
    subst ℒₛₑₜ (qVec ℒₛₑₜ w) (domZero (V := V)) = domZero (V := V) := by
  rw [domZero_eq_cDomN (V := V)]
  -- 把 `qVec w` 缩到 `?[^#0]`：只需前 1 格一致（`n = 1`）
  refine (subst_congr_prefix' (L := ℒₛₑₜ) (n := (1:V)) (m := (1:V))
    (k₁ := len (qVec ℒₛₑₜ w)) (k₂ := (1:V)) ((cDomN : ℕ) : V)
    (isSemiformula_cDomN (V := V)) ?_ (by norm_num)
    ?_ (IsSemitermVec.singleton.mpr
      ((IsSemiterm.bvar (L := ℒₛₑₜ) (V := V) (n := (1:V)) (z := (0:V))).mpr (by norm_num)))
    ?_).trans ?_
  · -- `1 ≤ len (qVec w)`：`qVec w = ^#0 ∷ …`，故长度 ≥ 1
    rw [show (qVec ℒₛₑₜ w) = (^#0 : V) ∷ termBShiftVec ℒₛₑₜ (len w) w from rfl]
    rw [len_adjoin]
    exact lt_add_of_pos_right _ (by norm_num : (0:V) < 1) |>.le
  · -- `qVec w` 是项向量（层取 1）
    refine IsSemitermVec.iff (L := ℒₛₑₜ) (k := len (qVec ℒₛₑₜ w)) (n := (1:V))
      (v := qVec ℒₛₑₜ w) |>.mpr ⟨rfl, fun i hi ↦ ?_⟩
    rw [show (qVec ℒₛₑₜ w) = (^#0 : V) ∷ termBShiftVec ℒₛₑₜ (len w) w from rfl] at hi ⊢
    rcases zero_or_succ i with (rfl | ⟨j, rfl⟩)
    · rw [nth_adjoin_zero]
      exact (IsSemiterm.bvar (L := ℒₛₑₜ) (V := V) (n := (1:V)) (z := (0:V))).mpr (by norm_num)
    · rw [nth_adjoin_succ]
      -- `termBShift` 的像：层数上界 = `termBV + 1`，取 `1` 只需其 ≤ 1 —— 用 `IsUTerm` 分量
      exact ⟨(IsUTermVec.termBShiftVec (L := ℒₛₑₜ) (V := V)
        (IsUTermVec.empty (L := ℒₛₑₜ) (V := V) (1:V))).nth (by simp), by simp⟩
  · intro j hj
    have hj0 : j = 0 := lt_one_iff_eq_zero.mp hj
    subst hj0
    rw [show (qVec ℒₛₑₜ w).[0] = (^#0 : V) from by
      rw [show (qVec ℒₛₑₜ w) = (^#0 : V) ∷ termBShiftVec ℒₛₑₜ (len w) w from rfl]
      rw [nth_adjoin_zero]]
    rw [show (?[^#0] : V).[0] = (^#0 : V) from by
      rw [show (?[^#0] : V) = ((^#0 : V) ∷ (0:V)) from rfl]
      rw [nth_adjoin_zero]]
  · refine subst_eq_self (L := ℒₛₑₜ) (n := (1:V)) (w := (?[^#0] : V))
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
