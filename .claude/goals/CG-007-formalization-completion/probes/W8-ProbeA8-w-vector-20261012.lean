import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000
namespace GodelQ.ProbeA8
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- `subst` 推过 `qqAlls`（Nat 归纳）。 -/
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

/-- `qVec² ?[^&0] = ?[^#0, ^#1, ^&0]`。 -/
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

/-- `?[^#0,^#1,^&0]` 的分量（`i < 2` 时是 `^#i`）。 -/
lemma lt_two_cases {i : V} (hi : i < 2) : i = 0 ∨ i = 1 := by
  have h : i < 1 + 1 := by norm_num at hi ⊢; exact hi
  rcases lt_succ_iff_eq_or_succ.mp h with h1 | h1
  · exact Or.inr h1
  · exact Or.inl (lt_one_iff_eq_zero.mp h1)

/-- `iVE` 与 `termSubst` 的相容律（**`iT_free` 的项层地基**）。

`iVE k (termSubst ?[^&0] t) = subst (qVec^k ?[^&0]) (iVE k t)`。

`k` 与向量长度同步：`termSubst` 不动 bvar，`subst` 在 `iVE` 的 `eqAtom` 层下
保护 `#0`（`qVec` 首分量）。 -/
lemma iVE_subst : ∀ (k : ℕ) (t : V), IsSemiterm ℒₒᵣ (k : V) t →
    iVE (k : V) (termSubst ℒₒᵣ (?[^&0] : V) t)
      = subst ℒₛₑₜ ((qVec ℒₛₑₜ)^[k] (?[^&0] : V)) (iVE (k : V) t) := by
  intro k
  induction k with
  | zero =>
    intro t ht
    rw [Function.iterate_zero_apply]
    -- 层数 0 时 t 无 bvar，故 `termSubst` 不动
    have h : termSubst ℒₒᵣ (?[^&0] : V) t = t := by
      apply termSubst_eq_self (n := (0:V)) ht
      intro i hi
      exact absurd hi (by norm_num at hi ⊢; exact hi)
    rw [h]
    -- `iVE 0 t` 层数 1，向量 `?[^&0]` 长度 1：`subst` 不动它
    -- （`subst_congr_prefix` 把它化到 `?[^#0]`，再用 `subst_eq_self₁`）
    have hiv : IsSemiformula ℒₛₑₜ (1:V) (iVE (V := V) (0:V) t) := by
      have hh := isSemiformula_iVE (V := V) (n := (0:V)) t ht
      norm_num at hh ⊢
      exact hh
    have hcp : subst ℒₛₑₜ (?[^&0] : V) (iVE (V := V) (0:V) t)
        = subst ℒₛₑₜ (?[^#0] : V) (iVE (V := V) (0:V) t) :=
      subst_congr_prefix (V := V) (n := (1:V)) (m := (1:V)) (k₁ := (1:V)) (k₂ := (1:V))
        (w := (?[^&0] : V)) (w' := (?[^#0] : V)) (iVE (V := V) (0:V) t) hiv
        (by norm_num) (by norm_num)
        (IsSemitermVec.singleton.mpr (IsSemiterm.fvar (L := ℒₛₑₜ) (V := V) (n := (1:V)) 0))
        (IsSemitermVec.singleton.mpr (IsSemiterm.bvar.mpr (by norm_num)))
        (by intro j hj; rw [show j = 0 from lt_one_iff_eq_zero.mp hj]; rfl)
    rw [← hcp]
    exact (subst_eq_self₁ (L := ℒₛₑₜ) hiv).symm
  | succ j ih =>
    intro t ht
    sorry

end GodelQ.ProbeA8
