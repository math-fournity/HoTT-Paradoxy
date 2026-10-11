import GodelQ.ZFC.ShCraigElimBranches
import GodelQ.ZFC.TranslateShiftCompat

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate GodelQ.TranslateShiftCompat

set_option maxHeartbeats 800000

namespace GodelQ.ProbeZ
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 反例检验：iVE 1 ^#0 = eqAtom ^#1，其中 eqAtom ^#1 含它自己的 ^#0 绑定。
-- subst ?[^&0] (eqAtom ^#1) 会把那个 ^#0 也换掉 —— 与 eqAtom ^&0 不同。
example : iVE 1 (^#0 : V) = (^rel 2 (↑cEqN) ((^#0 : V) ∷ (^#1 : V) ∷ (0 : V)) : V) := by
  rw [iVE_bvar, eqAtom]; rfl

example : subst ℒₛₑₜ (?[^&0] : V) (iVE 1 (^#0 : V))
    = (^rel 2 (↑cEqN) ((^&0 : V) ∷ (^#1 : V) ∷ (0 : V)) : V) := by
  rw [iVE_bvar, eqAtom]
  rw [show (?[^#0, ^#1] : V) = (^#0 : V) ∷ (^#1 : V) ∷ (0 : V) from rfl]
  rw [substs_rel (by rw [cEqN]; exact codeIn_rel_quote _) (by
    rw [show (2 : V) = 1 + 1 by norm_num, IsUTermVec.cons_iff]
    refine ⟨IsUTerm.bvar (z := 0), ?_⟩
    rw [show (1 : V) = 0 + 1 by norm_num, IsUTermVec.cons_iff]
    exact ⟨IsUTerm.bvar (z := 1), by simp⟩)]
  congr 1
  rw [show (2 : V) = 1 + 1 by norm_num,
      termSubstVec_cons (IsUTerm.bvar (z := 0))
        (by simpa using IsUTermVec.adjoin IsUTermVec.empty (IsUTerm.bvar (z := 1))),
      termSubst_bvar,
      show (1 : V) = 0 + 1 by norm_num,
      termSubstVec_cons (IsUTerm.bvar (z := 1)) IsUTermVec.empty,
      termSubst_bvar, termSubstVec_nil]
  simp

-- 而 iVE 0 ^&0 = eqAtom ^&0 = ^rel 2 cEqN (^#0 ∷ ^&0 ∷ 0)
example : iVE 0 (^&0 : V) = (^rel 2 (↑cEqN) ((^#0 : V) ∷ (^&0 : V) ∷ (0 : V)) : V) := by
  rw [iVE_fvar, eqAtom]; rfl

-- 两者不同：^&0 ∷ ^#1 ∷ 0 ≠ ^#0 ∷ ^&0 ∷ 0
example : ((^&0 : V) ∷ (^#1 : V) ∷ (0 : V)) ≠ ((^#0 : V) ∷ (^&0 : V) ∷ (0 : V)) := by
  intro h
  have h0 : (^&0 : V) = (^#0 : V) := by
    have := congrArg (fun v => v.[0]) h
    simpa using this
  -- ^&0 与 ^#0 是不同构造子
  exact absurd h0 (by decide)

end GodelQ.ProbeZ
