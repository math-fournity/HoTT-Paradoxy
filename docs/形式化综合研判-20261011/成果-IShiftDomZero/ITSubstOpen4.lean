-- CG-009: (★★) 的向量代数 —— qVec 的逐项展开 + VRel 的变换保持。
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

/-- 向量关系（(★★) 的前提）。`len Vw = m+1`、`len Ww = m+2`；
    前 `m+1` 项相等，且 `Ww` 的末项是 `^&0`。 -/
def VRel (m Vw Ww : V) : Prop :=
  (∀ k ≤ m, Vw.[k] = Ww.[k]) ∧ Ww.[m + 1] = ^&0

end GodelQ.ITSubstOpen4
