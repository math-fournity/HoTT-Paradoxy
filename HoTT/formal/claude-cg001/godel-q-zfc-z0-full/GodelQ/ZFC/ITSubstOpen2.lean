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

namespace GodelQ.ITSubstOpen2
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFull GodelQ.LayerMono

/-- `QvecV (m+1)` 是长度 `m+2`、**层 `m+1`** 的项向量（层是上界，可压低）。
    其项为 `^#0, …, ^#m, ^&0`，最大 bvar 索引 `m`。 -/
lemma isSemitermVec_QvecV_one_low {m : V} :
    IsSemitermVec ℒₛₑₜ (m + 2) (m + 1) (QvecV (V := V) (m + 1)) := by
  refine IsSemitermVec.iff.mpr ⟨(len_QvecV (m + 1)).trans (by ring), ?_⟩
  intro i hi
  -- `hi : i < m + 2`；`nth_QvecV (m+1)` 要求 `i ≤ m + 1`。
  -- `m + 2` 与 `(m + 1) + 1` 不是定义相等，需先 ring 改写再用 `lt_succ_iff_le.mp`。
  have hi' : i < (m + 1) + 1 := by
    have e : (m : V) + 2 = (m + 1) + 1 := by ring
    rwa [e] at hi
  have hle : i ≤ m + 1 := lt_succ_iff_le.mp hi'
  rw [show (QvecV (V := V) (m + 1)).[i]
      = if i = m + 1 then (^&0 : V) else ^#i from
    GodelQ.IVEOpenFunc.nth_QvecV (m + 1) i hle]
  split
  · exact IsSemiterm.fvar (m + 1) 0
  · rename_i hne
    exact IsSemiterm.bvar.mpr (lt_of_le_of_ne hle hne)

-- 〔2026-10-13 删除〕原本此处有一条 `composite_eq`（两个复合向量相等）。
-- 它有两个问题：(1) 缺少 `j` 的上界参数，`j` 无约束时 `j < 2 + m` 不可证；
-- (2) 使用了 `▸` 于不等式（非法）。已确认 **0 处下游引用**（全 worktree grep），
-- 且 `ITSubstOpen6.subst_iVE_open` 不依赖它。留着只会让下一个会话误判进度，
-- 故删除。等价功能由 `ITSubstOpen7.termSubstVec_two_QvecV_doubleton` 覆盖。
--
-- 原命题（若日后需要，须补 `hj : j < m + 2` 参数）：
--   termSubstVec ℒₛₑₜ (m + 2) ((^#j : V) ∷ shiftVec 2 m) (QvecV (m + 1))
--     = termSubstVec ℒₛₑₜ (m + 2) ((^#j : V) ∷ shiftVec 2 (m + 1)) (QvecV (m + 1))

end GodelQ.ITSubstOpen2
