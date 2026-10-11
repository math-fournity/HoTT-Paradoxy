import GodelQ.ZFC.ShCraigElimBranches
import GodelQ.ZFC.TranslateShiftCompat

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate GodelQ.TranslateShiftCompat

set_option maxHeartbeats 800000

namespace GodelQ.ProbeY
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 检验：iVE 与 termSubst 的「朴素」相容律（用同一个向量）
example : iVE 0 (termSubst ℒₒᵣ (?[^&0] : V) (^#0 : V)) = iVE 0 ((?[^&0] : V).[0]) := by
  rw [termSubst_bvar]

-- 手算结论：LHS = iVE 0 (^&0) = eqAtom (^&0) = ^rel 2 cEqN (^#0 ∷ ^&0 ∷ 0)
example : iVE 0 (^&0 : V) = (^rel 2 (↑cEqN) ((^#0 : V) ∷ (^&0 : V) ∷ (0 : V)) : V) := by
  rw [iVE_fvar, eqAtom]
  rfl

-- 而 RHS（朴素版）= subst ?[^&0] (iVE 1 (^#0)) = subst ?[^&0] (eqAtom (^#1))
--   termSubstVec 2 ?[^&0] ?[^#0,^#1] = ^&0 ∷ 0 ∷ 0  （越界取 0）
--   → ^rel 2 cEqN (^&0 ∷ 0 ∷ 0)  ≠ LHS
example : (termSubstVec ℒₛₑₜ 2 (?[^&0] : V) ((^#0 : V) ∷ (^#1 : V) ∷ (0 : V))) =
    ((^&0 : V) ∷ (0 : V) ∷ (0 : V)) := by
  rw [show (2 : V) = 1 + 1 by norm_num,
      termSubstVec_cons (IsUTerm.bvar (z := 0))
        (by simpa using IsUTermVec.adjoin IsUTermVec.empty (IsUTerm.bvar (z := 1))),
      termSubst_bvar,
      show (1 : V) = 0 + 1 by norm_num,
      termSubstVec_cons (IsUTerm.bvar (z := 1)) IsUTermVec.empty,
      termSubst_bvar, termSubstVec_nil]
  simp

-- 正确版：用 qVec 移位后的向量（^#0 ∷ termBShiftVec w）
example : (termSubstVec ℒₛₑₜ 2 ((^#0 : V) ∷ (^&0 : V) ∷ (0 : V))
      ((^#0 : V) ∷ (^#1 : V) ∷ (0 : V))) =
    ((^#0 : V) ∷ (^&0 : V) ∷ (0 : V)) := by
  rw [show (2 : V) = 1 + 1 by norm_num,
      termSubstVec_cons (IsUTerm.bvar (z := 0))
        (by simpa using IsUTermVec.adjoin IsUTermVec.empty (IsUTerm.bvar (z := 1))),
      termSubst_bvar,
      show (1 : V) = 0 + 1 by norm_num,
      termSubstVec_cons (IsUTerm.bvar (z := 1)) IsUTermVec.empty,
      termSubst_bvar, termSubstVec_nil]
  simp

end GodelQ.ProbeY
