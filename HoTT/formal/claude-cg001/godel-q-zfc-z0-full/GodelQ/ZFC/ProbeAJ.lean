import GodelQ.ZFC.ShCraigElimBranches
import GodelQ.ZFC.TranslateShiftCompat

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.TranslateShiftCompat

set_option maxHeartbeats 800000

namespace GodelQ.ProbeAJ
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 先证一个有用的：subst 作用在 eqAtom 上（用 qVec 向量）
lemma subst_eqAtom_qVec (s t : V) (ht : IsUTerm ℒₛₑₜ t) :
    subst ℒₛₑₜ ((^#0 : V) ∷ (s ∷ (0 : V))) (eqAtom t)
      = eqAtom (subst ℒₛₑₜ (?[s] : V) t) := by
  have hb : IsUTerm ℒₛₑₜ (^#0 : V) := IsUTerm.bvar (z := 0)
  have h1 : IsUTermVec ℒₛₑₜ (1 : V) (t ∷ (0 : V)) := by
    simpa using IsUTermVec.adjoin IsUTermVec.empty ht
  have hv2 : IsUTermVec ℒₛₑₜ (2 : V) ((^#0 : V) ∷ (t ∷ (0 : V))) := by
    simpa [show (2 : V) = 1 + 1 by norm_num] using IsUTermVec.adjoin h1 hb
  show subst ℒₛₑₜ ((^#0 : V) ∷ (s ∷ (0 : V)))
      (^rel 2 (↑cEqN) ((^#0 : V) ∷ (t ∷ (0 : V))))
    = ^rel 2 (↑cEqN) ((^#0 : V) ∷ (subst ℒₛₑₜ (?[s] : V) t ∷ (0 : V)))
  rw [substs_rel (by rw [cEqN]; exact codeIn_rel_quote _) hv2]
  congr 1
  -- termSubstVec 2 (^#0 ∷ s ∷ 0) (^#0 ∷ t ∷ 0)
  rw [show (2 : V) = 1 + 1 by norm_num,
      termSubstVec_cons hb (by simpa using IsUTermVec.adjoin IsUTermVec.empty ht),
      termSubst_bvar,
      show (1 : V) = 0 + 1 by norm_num,
      termSubstVec_cons ht IsUTermVec.empty,
      termSubst_bvar, termSubstVec_nil]
  simp

-- 现在 bvar 支
lemma iVE_subst_bvar (z : V) :
    iVE 0 (subst ℒₒᵣ (?[^&0] : V) (^#z : V))
      = subst ℒₛₑₜ (qVec ℒₛₑₜ (?[^&0] : V)) (iVE 1 (^#z : V)) := by
  rw [substs_bvar]
  rw [iVE_bvar, iVE_bvar]
  rw [show (qVec ℒₛₑₜ (?[^&0] : V)) = ((^#0 : V) ∷ (?[^&0] : V)) from by
    rw [qVec, show (len (?[^&0] : V)) = (1 : V) from by simp,
      show (1 : V) = 0 + 1 by norm_num,
      termBShiftVec_cons (IsUTerm.fvar 0) IsUTermVec.empty,
      termBShift_fvar, termBShiftVec_nil]]
  -- 剩下 (?[^&0]).[z] 的处理
  by_cases hz : z = 0
  · subst hz
    rw [nth_adjoin_zero]
    rw [eqAtom, eqAtom]
    exact subst_eqAtom_qVec (^&0) (^#1) (IsUTerm.bvar (z := 1))
  · have : (?[^&0] : V).[z] = 0 := by
      rw [nth_lt_len]
      rw [show (len (?[^&0] : V)) = (1 : V) from by simp]
      -- z ≠ 0 → 1 ≤ z
      exact le_of_lt (lt_of_le_of_ne (zero_le z) (Ne.symm hz))
    rw [this]

end GodelQ.ProbeAJ
