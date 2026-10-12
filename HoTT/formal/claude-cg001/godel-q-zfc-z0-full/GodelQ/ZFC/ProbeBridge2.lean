import GodelQ.ZFC.TranslateSeqShift

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

set_option maxHeartbeats 8000000

namespace GodelQ.ProbeBridge2
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 最简实例：q := ^rel 2 R ?[^#1, ^#1]（层 1，#0 在 rel 内出现两次）
-- 看桥的两边在 simp 归约后剩下的目标是什么。
example {R : V} (hR : (ℒₒᵣ).IsRel 2 R) :
    subst ℒₛₑₜ (?[^&0] : V) (iT (1 : V) (^rel 2 R ?[^#1, ^#1]))
      = iT (0 : V) (subst ℒₒᵣ (?[^&0] : V) (^rel 2 R ?[^#1, ^#1])) := by
  rw [iT_rel hR (by
        -- 向量 ?[^#1,^#1] 是 IsUTermVec
        rw [show (?[^#1, ^#1] : V) = (^#1 : V) ∷ (^#1 : V) ∷ 0 from rfl]
        rw [show (2 : V) = 1 + 1 by norm_num, IsUTermVec.cons_iff]
        exact ⟨IsUTerm.bvar, IsUTermVec.adjoin (IsUTermVec.empty) (IsUTerm.bvar), by simp⟩)]
  rw [iT_rel hR (by
        rw [show (subst ℒₒᵣ (?[^&0] : V) (^rel 2 R ?[^#1, ^#1]) : V) = _ from rfl]
        rw [substs_rel hR (by
          rw [show (?[^#1, ^#1] : V) = (^#1 : V) ∷ (^#1 : V) ∷ 0 from rfl]
          rw [show (2 : V) = 1 + 1 by norm_num, IsUTermVec.cons_iff]
          exact ⟨IsUTerm.bvar, IsUTermVec.adjoin (IsUTermVec.empty) (IsUTerm.bvar), by simp⟩)]
        rw [show (termSubstVec ℒₒᵣ 2 (?[^&0] : V) (?[^#1, ^#1] : V))
              = ((^&1 : V) ∷ (^&1 : V) ∷ 0) from by
          rw [show (?[^#1, ^#1] : V) = (^#1 : V) ∷ (^#1 : V) ∷ 0 from rfl]
          rw [show (2 : V) = 1 + 1 by norm_num, termSubstVec_cons, termSubstVec_cons,
            termSubstVec_nil, termSubst_bvar, termSubst_bvar]
          rw [show (?[^&0] : V) = (^&0 : V) ∷ 0 from rfl]
          simp]
        rw [show ((^&1 : V) ∷ (^&1 : V) ∷ 0) = (^&1 : V) ∷ (^&1 : V) ∷ 0 from rfl]
        rw [show (2 : V) = 1 + 1 by norm_num, IsUTermVec.cons_iff]
        exact ⟨IsUTerm.fvar, IsUTermVec.adjoin (IsUTermVec.empty) (IsUTerm.fvar), by simp⟩)]
  trace_state
  sorry

end GodelQ.ProbeBridge2
