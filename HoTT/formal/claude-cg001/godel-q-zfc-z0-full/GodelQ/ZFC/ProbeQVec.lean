import GodelQ.ZFC.TranslateSeqShift

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

namespace GodelQ.ProbeQVec
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- (1) 关键：qVec 用 termBShift（bvar+1，fvar 不动）。
--     故两层 qVec 后，fvar ^&0 落在位置 2 仍是 ^&0（不是 ^&2）。
example : (qVec ℒₛₑₜ ((^&0 : V) ∷ 0)) = ((^#0 : V) ∷ (^&0 : V) ∷ 0) := by
  rw [qVec]
  simp [termBShiftVec_cons, termBShift_bvar, termBShift_fvar]

example : (qVec ℒₛₑₜ (qVec ℒₛₑₜ ((^&0 : V) ∷ 0)))
    = ((^#0 : V) ∷ (^#1 : V) ∷ (^&0 : V) ∷ 0) := by
  rw [show qVec ℒₛₑₜ ((^&0 : V) ∷ 0) = ((^#0 : V) ∷ (^&0 : V) ∷ 0) from by
    rw [qVec]; simp [termBShiftVec_cons, termBShift_bvar, termBShift_fvar]]
  rw [qVec]
  simp [termBShiftVec_cons, termBShift_bvar, termBShift_fvar]

-- (2) domZero 在 qVec w 下不动（subst_eq_self，层 1，条目 0 是 ^#0）
example {w : V} (hw : IsSemitermVec ℒₛₑₜ 1 0 w) (h0 : w.[0] = (^#0 : V)) :
    subst ℒₛₑₜ (qVec ℒₛₑₜ w) domZero = domZero := by
  have hlen : len (qVec ℒₛₑₜ w) = 1 := by
    rw [qVec]; simp [len_adjoin]
  rw [subst_eq_self (isSemiformula_domZero (n := 0))
    (by
      rw [IsSemitermVec.cons_iff]
      sorry)
    (by
      intro i hi
      rw [show i = 0 from by omega]
      rw [qVec]
      simp)]
  sorry

end GodelQ.ProbeQVec
