import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`subst_qVec_domZero'` 的层数放宽版**：只要求 `w` 的**首格是 `^#0`**。

`domZero` 层 1，故 `subst` 只看向量的**第 0 格**；
`(qVec w).[0] = ^#0`（定义即得），**与 `w` 的层数无关**。 -/
lemma subst_qVec_domZero'' {w : V} (hw : IsUTermVec ℒₛₑₜ (len w) w) :
    subst ℒₛₑₜ (qVec ℒₛₑₜ w) (domZero (V := V)) = domZero (V := V) := by
  rw [domZero_eq_cDomN (V := V)]
  -- 只层 1：用 `subst_congr_prefix'` 把 `qVec w` 缩到 `?[^#0]`
  refine (subst_congr_prefix' (L := ℒₛₑₜ) (n := (1:V)) (m := (1:V))
    (k₁ := len (qVec ℒₛₑₜ w)) (k₂ := (1:V)) ((cDomN : ℕ) : V)
    (isSemiformula_cDomN (V := V)) ?_ (by norm_num)
    ?_ (IsSemitermVec.singleton.mpr
      ((IsSemiterm.bvar (L := ℒₛₑₜ) (V := V) (n := (1:V)) (z := (0:V))).mpr (by norm_num)))
    ?_).trans ?_
  · rw [TranslateShiftCompat.len_qVec hw]
    have h1 : (1:V) ≤ len w + 1 := by
      have h0 : (0:V) < len w + 1 := lt_add_of_pos_right _ (by norm_num : (0:V) < 1)
      exact h0.le
    exact h1
  · -- `qVec w` 的项向量性（层任意，取 1）
    refine IsSemitermVec.iff.mpr ⟨rfl, fun i hi ↦ ?_⟩
    rw [show (qVec ℒₛₑₜ w) = (^#0 : V) ∷ termBShiftVec ℒₛₑₜ (len w) w from rfl] at hi ⊢
    rcases zero_or_succ i with (rfl | ⟨j, rfl⟩)
    · rw [nth_adjoin_zero]
      exact (IsSemiterm.bvar (L := ℒₛₑₜ) (V := V) (n := (1:V)) (z := (0:V))).mpr (by norm_num)
    · rw [nth_adjoin_succ]
      exact (IsSemitermVec.termBShiftVec (L := ℒₛₑₜ) (V := V)
        (hw.isSemitermVec)).nth (by
          rw [len_termBShiftVec (V := V) (L := ℒₛₑₜ) hw]
          exact (add_lt_add_iff_right (1:V)).mp (by simpa using hi))
  · intro j hj
    have hj0 : j = 0 := lt_one_iff_eq_zero.mp hj
    subst hj0
    rw [show (qVec ℒₛₑₜ w).[0] = (^#0 : V) from by
      rw [show (qVec ℒₛₑₜ w) = (^#0 : V) ∷ termBShiftVec ℒₛₑₜ (len w) w from rfl]
      rw [nth_adjoin_zero]]
    rw [show (?[^#0] : V).[0] = (^#0 : V) from by
      rw [show (?[^#0] : V) = ((^#0 : V) ∷ (0:V)) from rfl]
      rw [nth_adjoin_zero]]
  · -- 最后：`subst ?[^#0] cDomN = cDomN`（`#0 ↦ #0` 是恒等）
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
