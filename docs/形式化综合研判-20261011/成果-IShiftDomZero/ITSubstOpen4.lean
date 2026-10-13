-- CG-009: (★★) 的向量代数 —— qVec 的逐项展开 + VRel 的变换保持。
--
-- ## VRel 的参数化
--
-- `VRel m Vw Ww`：`len Vw = m+1`、`len Ww = m+2`，且
--   (a) `∀ k ≤ m, Vw.[k] = Ww.[k]`
--   (b) `Ww.[m+1] = ^&0`
--
-- rel 支：`Vw = ^#j ∷ shiftVec 2 m`（长 m+1）、`Ww = [^#j, ^#2, …, ^#(m+1), ^&0]`（长 m+2）。
-- func 支：下降两层后 `Vw₁`、`Ww₁` 仍是同一形状（本文件的 `VRel_transform`）。
import GodelQ.ZFC.ITSubstOpen3

open FFL FFL.FirstOrder FFL FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.ITSubstOpen4
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFull GodelQ.LayerMono
open GodelQ.ITSubstOpen3

lemma nth_qVec_zero (X : V) : (qVec ℒₛₑₜ X).[0] = (^#0 : V) := by
  rw [qVec, nth_adjoin_zero]

lemma nth_qVec_succ {X k : V} (hX : IsUTermVec ℒₛₑₜ (len X) X) (hk : k < len X) :
    (qVec ℒₛₑₜ X).[k + 1] = termBShift ℒₛₑₜ X.[k] := by
  rw [qVec, nth_adjoin_succ, nth_termBShiftVec (L := ℒₛₑₜ) hX hk]

/-- `qVec²` 的逐项展开：源索引 `j` ↦ 结果索引 `j+2`。 -/
lemma nth_qVec_qVec {X j : V} (hX : IsUTermVec ℒₛₑₜ (len X) X) (hj : j < len X) :
    (qVec ℒₛₑₜ (qVec ℒₛₑₜ X)).[j + 2] = termBShift ℒₛₑₜ (termBShift ℒₛₑₜ X.[j]) := by
  have h1 : IsUTermVec ℒₛₑₜ (len (qVec ℒₛₑₜ X)) (qVec ℒₛₑₜ X) := by
    have h := (IsSemitermVec.qVec (hX.isSemitermVec)).isUTerm
    have e : (len X + 1 : V) = len (qVec ℒₛₑₜ X) := (len_qVec hX).symm
    rwa [e] at h
  have hj1 : (1 : V) + j < len (qVec ℒₛₑₜ X) := by
    have h : (1 : V) + j < len X + 1 := by
      rw [show (1 : V) + j = j + 1 by ring]
      exact add_lt_add_left hj 1
    rw [len_qVec hX]
    exact h
  have step : (qVec ℒₛₑₜ (qVec ℒₛₑₜ X)).[j + 2] = termBShift ℒₛₑₜ (qVec ℒₛₑₜ X).[1 + j] := by
    rw [show (j + 2 : V) = (1 + j) + 1 by ring]
    exact nth_qVec_succ h1 hj1
  rw [step]
  rw [show (1 + j : V) = j + 1 by ring]
  rw [nth_qVec_succ (X := X) hX hj]

/-- `(^#i ∷ shiftVec 3 n)` 的项（`j < n+1`）：`^#i`（`j=0`）或 `^#(j+2)`。 -/
lemma nth_cons_shiftVec3 {n i j : V} (hj : j < n + 1) :
    ((^#i : V) ∷ shiftVec 3 n).[j] = if j = 0 then (^#i : V) else ^#(j + 2) := by
  rcases zero_or_succ j with rfl | ⟨j', rfl⟩
  · simp
  · rw [nth_adjoin_succ]
    have hj' : j' < n := by
      have h2 : j' + 1 < n + 1 := by simpa using hj
      exact add_lt_add_iff_right (1 : V) |>.mp h2
    rw [nth_shiftVec 3 n j' hj', if_neg (by simp : ¬(j' + 1 = 0 : Prop))]
    congr 1
    ring

lemma nth_qVec_qVec_zero (X : V) : (qVec ℒₛₑₜ (qVec ℒₛₑₜ X)).[0] = (^#0 : V) :=
  nth_qVec_zero _

/-- `qVec (qVec X)` 在索引 1 处 = `^#1`（与 `X` 无关）。 -/
lemma nth_qVec_qVec_one {X : V} (hX : IsUTermVec ℒₛₑₜ (len X) X) :
    (qVec ℒₛₑₜ (qVec ℒₛₑₜ X)).[1] = (^#1 : V) := by
  have h1 : IsUTermVec ℒₛₑₜ (len (qVec ℒₛₑₜ X)) (qVec ℒₛₑₜ X) := by
    have h := (IsSemitermVec.qVec (hX.isSemitermVec)).isUTerm
    have e : (len X + 1 : V) = len (qVec ℒₛₑₜ X) := (len_qVec hX).symm
    rwa [e] at h
  have h0 : (0 : V) < len (qVec ℒₛₑₜ X) := by
    rw [len_qVec hX]
    exact lt_of_le_of_lt (zero_le) (lt_add_one (len X))
  rw [show (1 : V) = 0 + 1 by norm_num]
  rw [nth_qVec_succ (X := qVec ℒₛₑₜ X) (k := 0) h1 h0]
  rw [nth_qVec_zero, termBShift_bvar]

/-- `len (shiftVec 3 n) = n`。 -/
lemma len_shiftVec_three' (n : V) : len (shiftVec 3 n) = n :=
  (isSemitermVec_shiftVec_V 3 n).isUTerm.lh.symm

/-- 向量关系（(★★) 的前提）。`len Vw = m+1`、`len Ww = m+2`；
    前 `m+1` 项相等，且 `Ww` 的末项是 `^&0`。 -/
def VRel (m Vw Ww : V) : Prop :=
  (∀ k ≤ m, Vw.[k] = Ww.[k]) ∧ Ww.[m + 1] = ^&0

-- 说明：`VRel_transform` 的完整证明需要大量 V 层算术（长度、索引的逐项核算）。
-- 本文件先给出其**零件**（qVec 逐项 + 边界引理），完整证明见下一会话。
-- 关键事实（已由 OpenLawCheck5 机器核验）：
--   * qVec² 的索引 0/1 与 X 无关（^#0 / ^#1）
--   * qVec² 在索引 j+2 处 = termBShift²(X.[j])
--   * VRel m Vw Ww 的三条件在 qVec² + shiftVec 3 的复合下保持

/-- 单调界：`k ≤ m` ⟹ `k < m + 2`。 -/
lemma lt_add_two_of_le {k m : V} (hk : k ≤ m) : k < m + 2 :=
  calc k ≤ m := hk
    _ < m + 1 := lt_add_one m
    _ < m + 2 := by
        have h := lt_add_one (m + 1)
        rwa [show (m + 1 : V) + 1 = m + 2 by ring] at h

/-- 单调界：`k ≤ m + 1` ⟹ `k < m + 3`。 -/
lemma lt_add_three_of_le {k m : V} (hk : k ≤ m + 1) : k < m + 3 :=
  calc k ≤ m + 1 := hk
    _ < m + 2 := by
        have h := lt_add_one (m + 1)
        rwa [show (m + 1 : V) + 1 = m + 2 by ring] at h
    _ < m + 3 := by
        have h := lt_add_one (m + 2)
        rwa [show (m + 2 : V) + 1 = m + 3 by ring] at h


-- 关键发现（2026-10-12，机器核验）：V 层 `m + 1 + 1` **不是** definitionally `m + 2`
-- （V 是任意模型，`2` 是字面量而非 `1+1` 的缩写）。
-- 因此 W 侧的长度一律写成 `(m+1)+1` 形式，避免 `m+2` 的归一化摩擦。

/-- `qVec² X` 的长度（`X` 的项向量形式）。 -/
lemma len_qVec_qVec_eq {X : V} (hX : IsUTermVec ℒₛₑₜ (len X) X) :
    len (qVec ℒₛₑₜ (qVec ℒₛₑₜ X)) = len X + 2 := by
  rw [len_qVec (by
      have h := (IsSemitermVec.qVec (hX.isSemitermVec)).isUTerm
      have e : (len X + 1 : V) = len (qVec ℒₛₑₜ X) := (len_qVec hX).symm
      rwa [e] at h), len_qVec hX]
  ring

/-- `^#i ∷ shiftVec 3 n` 的长度 = `n + 1`。 -/
lemma len_cons_shiftVec3'' (n i : V) : len ((^#i : V) ∷ shiftVec 3 n) = n + 1 := by
  rw [len_adjoin, len_shiftVec_three']

/-- `(^#i ∷ shiftVec 3 n)` 的项（`j ≤ n`）：`^#i`（`j=0`）或 `^#(j+2)`。 -/
lemma nth_cons_shiftVec3_le {n i j : V} (hj : j ≤ n) :
    ((^#i : V) ∷ shiftVec 3 n).[j] = if j = 0 then (^#i : V) else ^#(j + 2) :=
  nth_cons_shiftVec3 (n := n) (i := i) (lt_succ_iff_le.mpr hj)

/-- `k ≤ m` ⟹ `k < m + 3`。 -/
lemma lt_add_three_of_le' {k m : V} (hk : k ≤ m) : k < m + 3 := by
  have h1 : k < m + 1 := lt_of_le_of_lt hk (lt_add_one m)
  have h2 : m + 1 < m + 3 := by
    have h := lt_add_one (m + 1)
    rw [show (m + 1 : V) + 1 = m + 2 by ring] at h
    have h2' := lt_add_one (m + 2)
    rw [show (m + 2 : V) + 1 = m + 3 by ring] at h2'
    exact lt_trans h h2'
  exact lt_trans h1 h2

/-- `k ≤ m` ⟹ `k < m + 4`。 -/
lemma lt_add_four_of_le {k m : V} (hk : k ≤ m) : k < m + 4 := by
  have h1 : k < m + 3 := lt_add_three_of_le' hk
  have h2 : m + 3 < m + 4 := by
    have h := lt_add_one (m + 3)
    rw [show (m + 3 : V) + 1 = m + 4 by ring] at h
    exact h
  exact lt_trans h1 h2

/-- **VRel 的变换保持**（func 支的关键）。
    W 侧长度写成 `(m+1)+1` 以匹配 V 层的实际归一化形式。 -/
lemma VRel_transform {m i Vw Ww : V}
    (hV : IsUTermVec ℒₛₑₜ (len Vw) Vw) (hW : IsUTermVec ℒₛₑₜ (len Ww) Ww)
    (hlV : len Vw = m + 1) (hlW : len Ww = m + 2)
    (hi : i ≤ 1) (h : VRel m Vw Ww) :
    VRel m
      (termSubstVec ℒₛₑₜ (m + 1) (qVec ℒₛₑₜ (qVec ℒₛₑₜ Vw)) ((^#i : V) ∷ shiftVec 3 m))
      (termSubstVec ℒₛₑₜ (m + 2) (qVec ℒₛₑₜ (qVec ℒₛₑₜ Ww)) ((^#i : V) ∷ shiftVec 3 (m + 1))) := by
  obtain ⟨hpre, hlast⟩ := h
  -- 代入向量与其长度
  have hlenV : len ((^#i : V) ∷ shiftVec 3 m) = m + 1 := len_cons_shiftVec3'' m i
  have hlenW : len ((^#i : V) ∷ shiftVec 3 (m + 1)) = m + 2 := by
    rw [len_cons_shiftVec3'']
    ring
  have huv : IsUTermVec ℒₛₑₜ (m + 1) ((^#i : V) ∷ shiftVec 3 m) :=
    ⟨hlenV.symm,
      fun j hj ↦ by
        rw [nth_cons_shiftVec3_le (n := m) (i := i) (lt_succ_iff_le.mp hj)]
        split
        · exact IsUTerm.bvar
        · exact IsUTerm.bvar⟩
  have huw : IsUTermVec ℒₛₑₜ (m + 2) ((^#i : V) ∷ shiftVec 3 (m + 1)) :=
    ⟨hlenW.symm,
      fun j hj ↦ by
        rw [nth_cons_shiftVec3_le (n := m + 1) (i := i) (by
          have h : j < (m + 1) + 1 := by rwa [show (m + 1 : V) + 1 = m + 2 by ring]
          exact lt_succ_iff_le.mp h)]
        split
        · exact IsUTerm.bvar
        · exact IsUTerm.bvar⟩
  -- qVec² 的长度
  have hlen2 : len (qVec ℒₛₑₜ (qVec ℒₛₑₜ Vw)) = m + 3 := by
    rw [len_qVec_qVec_eq hV, hlV]
    ring
  have hlen3 : len (qVec ℒₛₑₜ (qVec ℒₛₑₜ Ww)) = m + 4 := by
    rw [len_qVec_qVec_eq hW, hlW]
    ring
  constructor
  · -- (a) ∀ k ≤ m, Vw₁.[k] = Ww₁.[k]
    intro k hk
    have hkV : k < len (qVec ℒₛₑₜ (qVec ℒₛₑₜ Vw)) := by
      rw [hlen2]
      calc k ≤ m := hk
        _ < m + 1 := lt_add_one m
        _ < m + 3 := lt_trans (lt_add_one (m + 1)) (by
          rw [show (m + 1 : V) + 1 = m + 2 by ring]
          rw [show (m + 3 : V) = (m + 2) + 1 by ring]
          exact lt_add_one (m + 2))
    have hkW : k < len (qVec ℒₛₑₜ (qVec ℒₛₑₜ Ww)) := by
      rw [hlen3]; exact lt_add_four_of_le hk
    have hkV1 : k < m + 1 := lt_of_le_of_lt hk (lt_add_one m)
    have hkW2 : k < m + 2 := by
      rw [show (m + 2 : V) = (m + 1) + 1 by ring]
      exact lt_trans hkV1 (lt_add_one (m + 1))
    rw [nth_termSubstVec (L := ℒₛₑₜ) huv hkV1, nth_termSubstVec (L := ℒₛₑₜ) huw hkW2]
    rw [nth_cons_shiftVec3 (n := m) (i := i) hkV1,
      nth_cons_shiftVec3 (n := m + 1) (i := i) (by
        rw [show (m + 1 : V) + 1 = m + 2 by ring]; exact hkW2)]
    rcases eq_or_ne k 0 with rfl | hk0
    · -- k = 0：索引 i（i ≤ 1），两侧 qVec² 的索引 i 处相同
      rw [if_pos rfl]
      have hi01 : i = 0 ∨ i = 1 := by
        rcases lt_or_eq_of_le hi with h | h
        · left
          exact le_antisymm (lt_succ_iff_le.mp (by
            rwa [show (1 : V) = 0 + 1 by norm_num] at h)) (zero_le)
        · right; exact h
      rcases hi01 with rfl | rfl
      · -- i = 0：两侧都是 termSubst (qVec² X) ^#0 = (qVec² X).[0] = ^#0
        rw [termSubst_bvar, termSubst_bvar, nth_qVec_qVec_zero, nth_qVec_qVec_zero]
      · rw [termSubst_bvar, termSubst_bvar, nth_qVec_qVec_one hV, nth_qVec_qVec_one hW]
    · -- k ≥ 1：索引 k+2，两侧都是 termBShift²(X.[k])，由前缀相等
      rw [if_neg hk0, termSubst_bvar, termSubst_bvar]
      have hkV' : k < len Vw := by
        rw [hlV]; exact lt_of_le_of_lt hk (lt_add_one m)
      have hkW' : k < len Ww := by
        rw [hlW]
        have h1 : k < m + 1 := lt_of_le_of_lt hk (lt_add_one m)
        have h2 : m + 1 < m + 2 := by
          rw [show (m + 2 : V) = (m + 1) + 1 by ring]
          exact lt_add_one (m + 1)
        exact lt_trans h1 h2
      rw [nth_qVec_qVec hV hkV', nth_qVec_qVec hW hkW', hpre k hk]
  · -- (b) Ww₁.[m+1] = ^&0
    have h1 : m + 1 < m + 1 + 1 := lt_add_one (m + 1)
    have h1' : m + 1 < m + 2 := by
      rw [show (m + 2 : V) = (m + 1) + 1 by ring]; exact h1
    rw [nth_termSubstVec (L := ℒₛₑₜ) huw h1']
    rw [nth_cons_shiftVec3 (n := m + 1) (i := i) h1,
      if_neg (by
        intro h
        have := lt_add_one m
        rw [show (m + 1 : V) = 0 from h] at this
        exact absurd this (not_lt_of_ge (zero_le)))]
    have hkW' : m + 1 < len Ww := by rw [hlW]; exact h1'
    rw [termSubst_bvar, nth_qVec_qVec hW hkW', hlast, termBShift_fvar, termBShift_fvar]



#print axioms GodelQ.ITSubstOpen4.VRel_transform

end GodelQ.ITSubstOpen4
