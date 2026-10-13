-- CG-009: `iT_subst_open` 的 b = 2 向量恒等式。
--
-- `iTR` 用 `conjunct 2 n j (iVE n v.[j])`，其向量 `W := ^#i ∷ shiftVec 2 n`
-- 长度 `n+1`、层 `n+2`。代入 `n = m+1` 后长度 `m+2`、层 `m+3`。
import GodelQ.ZFC.IVEOpenFull
import GodelQ.ZFC.IVEOpenFunc8
import GodelQ.ZFC.LayerMono

open FFL FFL.FirstOrder FFL FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.ITSubstOpen2
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFull GodelQ.LayerMono

/-- `W := ^#i ∷ shiftVec 2 (m+1)` 的第 `j` 项（`j < m+2`）：`^#i`（`j=0`）或 `^#(j+1)`。 -/
lemma nth_cons_shiftVec2 {m i j : V} (hj : j < m + 2) :
    ((^#i : V) ∷ shiftVec 2 (m + 1)).[j] = if j = 0 then (^#i : V) else ^#(j + 1) := by
  rcases zero_or_succ j with rfl | ⟨j', rfl⟩
  · simp
  · rw [nth_adjoin_succ]
    have hj' : j' < m + 1 := by
      have h2 : j' + 1 < m + 1 + 1 := by
        have e : (m + 1 : V) + 1 = m + 2 := by ring
        rwa [e]
      exact add_lt_add_iff_right (1 : V) |>.mp h2
    rw [nth_shiftVec 2 (m + 1) j' hj', if_neg (by simp : ¬(j' + 1 = 0 : Prop))]
    congr 1
    ring

/-- `W` 是长度 `m+2`、层 `m+3` 的项向量（`i < m+2`）。 -/
lemma isSemitermVec_cons_shiftVec2 {m i : V} (hi : i < m + 2) :
    IsSemitermVec ℒₛₑₜ (m + 2) (m + 3) ((^#i : V) ∷ shiftVec 2 (m + 1)) := by
  have hb : (i : V) < 2 + (m + 1) := by
    have e : (2 : V) + (m + 1) = m + 3 := by ring
    rw [e]
    exact lt_trans hi (by
      have h := lt_add_one (m + 2)
      have e2 : (m + 2 : V) + 1 = m + 3 := by ring
      rwa [e2] at h)
  have h := isSemitermVec_shiftVec_cons (b := 2) (n := m + 1) (i := i) hb
  have e1 : ((m + 1) + 1 : V) = m + 2 := by ring
  rw [e1, show (2 : V) + (m + 1) = 3 + m by ring] at h
  exact LayerMono.IsSemitermVec.mono h (le_of_eq (by ring : (3 : V) + m = m + 3))

/-- `QvecV (m+1)` 是长度/层 `m+2` 的项向量。 -/
lemma isSemitermVec_QvecV_one' {m : V} :
    IsSemitermVec ℒₛₑₜ (m + 2) (m + 2) (QvecV (V := V) (m + 1)) := by
  have h := isSemitermVec_QvecV (V := V) (m + 1)
  rwa [show (m + 1 : V) + 1 = m + 2 by ring] at h

/-- **b = 2 的向量恒等式**：`QvecV (m+2)` 复合 `W` = `W` 复合 `QvecV (m+1)`。 -/
lemma termSubstVec_two_QvecV_eq {m i : V} (hi : i < m + 2) :
    termSubstVec ℒₛₑₜ (m + 2) (QvecV (V := V) (m + 2)) ((^#i : V) ∷ shiftVec 2 (m + 1))
      = termSubstVec ℒₛₑₜ (m + 2) ((^#i : V) ∷ shiftVec 2 (m + 1)) (QvecV (V := V) (m + 1)) := by
  have hW := isSemitermVec_cons_shiftVec2 (m := m) (i := i) hi
  have hQ1 := isSemitermVec_QvecV_one' (V := V) (m := m)
  apply nth_ext' (m + 2)
  · rw [len_termSubstVec hW.isUTerm]
  · rw [len_termSubstVec hQ1.isUTerm]
  · intro j hj
    rw [nth_termSubstVec hW.isUTerm hj, nth_termSubstVec hQ1.isUTerm hj,
      nth_cons_shiftVec2 (m := m) (i := i) hj]
    rcases zero_or_succ j with rfl | ⟨j', rfl⟩
    · -- j = 0：两侧都是 ^#i
      rw [if_pos rfl, termSubst_bvar, GodelQ.ITRSubstOpen.nth_QvecV_lt (m + 2) i hi]
      rw [GodelQ.ITRSubstOpen.nth_QvecV_lt (m + 1) 0 (by simp), termSubst_bvar,
        nth_adjoin_zero]
    · -- j = j'+1
      rw [if_neg (by simp : ¬(j' + 1 = 0 : Prop))]
      by_cases hlast : j' + 1 = m + 1
      · -- 末槽：左 = (QvecV (m+2)).[m+2] = ^&0；右 = termSubst W (^&0) = ^&0
        rw [show (j' + 1 + 1 : V) = m + 2 by rw [hlast]; ring]
        rw [termSubst_bvar, GodelQ.ITRSubstOpen.nth_QvecV_last (m + 2)]
        rw [show (j' + 1 : V) = m + 1 from hlast,
          GodelQ.ITRSubstOpen.nth_QvecV_last (m + 1), termSubst_fvar]
      · have hj'' : j' + 1 < m + 1 := by
          have h2 : j' + 1 < (m + 1) + 1 := by
            have e : (m + 1 : V) + 1 = m + 2 := by ring
            rwa [e]
          exact lt_of_le_of_ne (lt_succ_iff_le.mp h2) (fun h => hlast h)
        rw [termSubst_bvar, GodelQ.ITRSubstOpen.nth_QvecV_lt (m + 2) (j' + 1 + 1) (by
            have h : (1 : V) + (j' + 1) < 1 + (m + 1) := add_lt_add_right hj'' 1
            have e1 : (1 : V) + (j' + 1) = j' + 1 + 1 := by ring
            have e2 : (1 : V) + (m + 1) = m + 2 := by ring
            rw [e1, e2] at h
            exact h)]
        rw [GodelQ.ITRSubstOpen.nth_QvecV_lt (m + 1) (j' + 1) hj'']
        rw [show termSubst ℒₛₑₜ ((^#i : V) ∷ shiftVec 2 (m + 1)) (^#(j' + 1) : V)
            = ((^#i : V) ∷ shiftVec 2 (m + 1)).[j' + 1] from termSubst_bvar (j' + 1),
          nth_cons_shiftVec2 (m := m) (i := i) (j := j' + 1) (by
            have h := lt_succ_iff_le.mpr (le_of_lt hj'')
            have e : (m + 1 : V) + 1 = m + 2 := by ring
            rwa [e] at h),
          if_neg (by simp : ¬(j' + 1 = 0 : Prop))]

end GodelQ.ITSubstOpen2

#print axioms GodelQ.ITSubstOpen2.termSubstVec_two_QvecV_eq
