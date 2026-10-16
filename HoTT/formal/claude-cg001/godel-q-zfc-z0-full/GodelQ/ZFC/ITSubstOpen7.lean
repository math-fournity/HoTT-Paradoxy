-- CG-009: `iT_subst_open` 的 rel 支 —— `iTR` 与开口代入交换。
--
-- 目标（`q` 层 `m+1`）：
--     iT m (subst ℒₒᵣ (QvecVOr m) q) = subst ℒₛₑₜ (QvecV m) (iT (m+1) q)
--
-- rel 支（`q = ^rel 2 R v`）：
--   LHS = iTR m 2 R (termSubstVec 2 (QvecVOr m) v)
--   RHS = subst (QvecV m) (iTR (m+1) 2 R v)
-- 两侧展开成 `qqAlls _ 2`，体内向量的关系由 `subst_iVE_open`（(★★)）在
--   Vw = ^#j ∷ shiftVec 2 m、Ww = termSubstVec (m+2) (QvecV (m+2)) (^#j ∷ shiftVec 2 (m+1))
-- 处给出（VRel 由 `VRel_rel` 核验）。
import GodelQ.ZFC.ITSubstOpen6

open FFL FFL.FirstOrder FFL FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.ITSubstOpen7
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFull GodelQ.LayerMono
open GodelQ.ITSubstOpen2 GodelQ.ITSubstOpen3 GodelQ.ITSubstOpen4
open GodelQ.ITSubstOpen5 GodelQ.ITSubstOpen6

/-! ## 零件 J：`QvecV (m+2)` 固定 `subst ?[^#0,^#1] (cRel R)` -/

/-- `2 ≤ m + 2`。 -/
lemma two_le_m_add_two (m : V) : (2 : V) ≤ m + 2 := by
  have h : (2 : V) + 0 ≤ (2 : V) + m :=
    add_le_add_right (show (0 : V) ≤ m from zero_le) 2
  calc (2 : V) = (2 : V) + 0 := by ring
    _ ≤ (2 : V) + m := h
    _ = m + 2 := by ring

/-- `termSubstVec 2 (QvecV (m+2)) ?[^#i, ^#j] = ?[^#i, ^#j]`（`i, j < m+2`）。 -/
lemma termSubstVec_two_QvecV_doubleton {m i j : V} (hi : i < m + 2) (hj : j < m + 2) :
    termSubstVec ℒₛₑₜ 2 (QvecV (V := V) (m + 2)) (?[^#i, ^#j] : V) = (?[^#i, ^#j] : V) := by
  rw [termSubstVec_cons₂ (IsUTerm.bvar (z := i)) (IsUTerm.bvar (z := j))]
  congr 1
  · rw [termSubst_bvar, GodelQ.ITRSubstOpen.nth_QvecV_lt (m + 2) i hi]
  · rw [termSubst_bvar, GodelQ.ITRSubstOpen.nth_QvecV_lt (m + 2) j hj]

/-- `subst (QvecV (m+2)) (subst ?[^#0,^#1] (cRel R)) = subst ?[^#0,^#1] (cRel R)`。 -/
lemma subst_QvecV_cRel {m R : V} :
    subst ℒₛₑₜ (QvecV (V := V) (m + 2)) (subst ℒₛₑₜ (?[^#0, ^#1] : V) (cRel R)) =
      subst ℒₛₑₜ (?[^#0, ^#1] : V) (cRel R) := by
  have hc : IsSemiformula ℒₛₑₜ 2 (cRel R) := isSemiformula_cRel R
  have hQ : IsSemitermVec ℒₛₑₜ (m + 3) (m + 3) (QvecV (V := V) (m + 2)) := by
    have h := isSemitermVec_QvecV (V := V) (m + 2)
    have e : (m + 2 : V) + 1 = m + 3 := by ring
    rwa [e] at h
  have hw : IsSemitermVec ℒₛₑₜ 2 (m + 3) (?[^#0, ^#1] : V) := by
    rw [IsSemitermVec.doubleton]
    exact ⟨IsSemiterm.bvar.mpr (by
      have h := zero_lt_three_add m
      have e : (3 : V) + m = m + 3 := by ring
      rwa [e] at h), IsSemiterm.bvar.mpr (by
      have h := one_lt_three_add m
      have e : (3 : V) + m = m + 3 := by ring
      rwa [e] at h)⟩
  rw [show subst ℒₛₑₜ (QvecV (V := V) (m + 2)) (subst ℒₛₑₜ (?[^#0, ^#1] : V) (cRel R))
      = subst ℒₛₑₜ (termSubstVec ℒₛₑₜ 2 (QvecV (V := V) (m + 2)) (?[^#0, ^#1] : V)) (cRel R) from
    Bootstrapping.substs_substs (L := ℒₛₑₜ) (l := 2) (n := m + 3) (m := m + 3)
      (p := cRel R) hc hQ hw]
  rw [show (?[^#0, ^#1] : V) = ?[^#0, ^#1] from rfl,
    termSubstVec_two_QvecV_doubleton
      (lt_of_lt_of_le (by norm_num : (0 : V) < 2) (two_le_m_add_two m))
      (lt_of_lt_of_le (by norm_num : (1 : V) < 2) (two_le_m_add_two m))]


#print axioms GodelQ.ITSubstOpen7.subst_QvecV_cRel

/-! ## 零件 K：`^#i ∷ shiftVec 2 n` 的逐项展开（长度 `n+1` 版） -/

/-- `((^#i : V) ∷ shiftVec 2 n).[k]`（`k < n+1`）：`^#i`（k=0）或 `^#(k+1)`。 -/
lemma nth_cons_shiftVec2_len {n i k : V} (hk : k < n + 1) :
    ((^#i : V) ∷ shiftVec 2 n).[k] = if k = 0 then (^#i : V) else ^#(k + 1) := by
  rcases zero_or_succ k with rfl | ⟨k', rfl⟩
  · simp
  · rw [nth_adjoin_succ]
    have hk' : k' < n := by
      have h2 : k' + 1 < n + 1 := by simpa using hk
      exact add_lt_add_iff_right (a := (1 : V)) (b := k') (c := n) |>.mp h2
    rw [nth_shiftVec 2 n k' hk', if_neg (by simp : ¬(k' + 1 = 0 : Prop))]
    congr 1
    ring

/-! ## 零件 L：rel 支的 `VRel` 实例 -/

/-- **rel 支的向量关系**。

`Vw := ^#j ∷ shiftVec 2 m`（长 `m+1`）与
`Ww := termSubstVec (m+2) (QvecV (m+2)) (^#j ∷ shiftVec 2 (m+1))`（长 `m+2`）满足：
(a) `∀ k ≤ m, Vw.[k] = Ww.[k]`；(b) `Ww.[m+1] = ^&0`。

这正是 `subst_iVE_open`（(★★)）在 rel 支所需的前提。 -/
lemma VRel_rel (m j : V) (hj : j < m + 2) :
    (∀ k ≤ m, ((^#j : V) ∷ shiftVec 2 m).[k] =
      (termSubstVec ℒₛₑₜ (m + 2) (QvecV (V := V) (m + 2))
        ((^#j : V) ∷ shiftVec 2 (m + 1))).[k]) ∧
    (termSubstVec ℒₛₑₜ (m + 2) (QvecV (V := V) (m + 2))
        ((^#j : V) ∷ shiftVec 2 (m + 1))).[m + 1] = ^&0 := by
  constructor
  · intro k hk
    have hk1 : k < m + 1 := lt_of_le_of_lt hk (lt_add_one m)
    have hk2 : k < m + 2 := lt_trans hk1 (by
      have h := lt_add_one (m + 1)
      rw [show ((m + 1) + 1 : V) = m + 2 by ring] at h
      exact h)
    rw [nth_termSubstVec (isSemitermVec_cons_shiftVec2 (m := m) (i := j) hj).isUTerm hk2]
    rw [nth_cons_shiftVec2_len (n := m) (i := j) hk1]
    rw [nth_cons_shiftVec2 (m := m) (i := j) (j := k) hk2]
    rcases zero_or_succ k with rfl | ⟨k', rfl⟩
    · simp [termSubst_bvar, GodelQ.ITRSubstOpen.nth_QvecV_lt (m + 2) j hj]
    · simp [termSubst_bvar]
      have hk2b : k' + 1 + 1 < m + 2 := by
        have h2 := add_lt_add_right (by simpa using hk1 : k' + 1 < m + 1) 1
        rw [show (1 : V) + (k' + 1) = k' + 1 + 1 by ring,
          show (1 : V) + (m + 1) = m + 2 by ring] at h2
        exact h2
      exact (GodelQ.ITRSubstOpen.nth_QvecV_lt (m + 2) (k' + 1 + 1) hk2b).symm
  · have hm1 : m + 1 < m + 2 := by
      have h := lt_add_one (m + 1)
      rw [show ((m + 1) + 1 : V) = m + 2 by ring] at h
      exact h
    rw [nth_termSubstVec (isSemitermVec_cons_shiftVec2 (m := m) (i := j) hj).isUTerm hm1]
    rw [nth_cons_shiftVec2 (m := m) (i := j) (j := m + 1) hm1]
    rw [if_neg (by
      intro h
      have hpos : (0 : V) < m + 1 := lt_of_le_of_lt zero_le (lt_add_one m)
      rw [h] at hpos
      exact absurd hpos (not_lt_of_ge (le_refl 0))),
      termSubst_bvar]
    rw [show ((m + 1 + 1 : V)) = m + 2 by ring,
      GodelQ.ITRSubstOpen.nth_QvecV_last (m + 2)]

end GodelQ.ITSubstOpen7

#print axioms GodelQ.ITSubstOpen7.two_le_m_add_two
#print axioms GodelQ.ITSubstOpen7.termSubstVec_two_QvecV_doubleton
#print axioms GodelQ.ITSubstOpen7.subst_QvecV_cRel
#print axioms GodelQ.ITSubstOpen7.nth_cons_shiftVec2_len
#print axioms GodelQ.ITSubstOpen7.VRel_rel