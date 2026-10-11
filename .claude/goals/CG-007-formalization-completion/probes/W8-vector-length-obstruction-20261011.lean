import GodelQ.ZFC.ShCraigElimBranches
import GodelQ.ZFC.TranslateShiftCompat

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate GodelQ.TranslateShiftCompat

set_option maxHeartbeats 800000

namespace GodelQ.ProbeAA
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 更正：substs_rel 用**整个** w 做 termSubstVec，所以两个分量拿到同一个向量。
-- 若 t = ^#1（bvar 1），subst (^#0 ∷ s ∷ 0) ^#1 = w.[1] = s —— 恰好对。
-- 若 t = ^#0，subst ... ^#0 = w.[0] = ^#0 —— 也对（保持 ^#0）。
-- 若 t 是 fvar，termSubst 不动。
-- 所以关键情形是 t 的**分量也是 bvar 或 fvar**。iVE 的输入项恰好如此！
--
-- 检验：t = ^#1 时两边相等
example (s : V) :
    subst ℒₛₑₜ ((^#0 : V) ∷ (s ∷ (0 : V))) (eqAtom (^#1 : V))
      = eqAtom (subst ℒₛₑₜ (?[s] : V) (^#1 : V)) := by
  show subst ℒₛₑₜ ((^#0 : V) ∷ (s ∷ (0 : V)))
      (^rel 2 (↑cEqN) ((^#0 : V) ∷ (^#1 : V) ∷ (0 : V)))
    = ^rel 2 (↑cEqN) ((^#0 : V) ∷ (subst ℒₛₑₜ (?[s] : V) (^#1 : V) ∷ (0 : V)))
  have hb : IsUTerm ℒₛₑₜ (^#0 : V) := IsUTerm.bvar (z := 0)
  have h1 : IsUTerm ℒₛₑₜ (^#1 : V) := IsUTerm.bvar (z := 1)
  have hv2 : IsUTermVec ℒₛₑₜ (2 : V) ((^#0 : V) ∷ (^#1 : V) ∷ (0 : V)) := by
    have ht1 : IsUTermVec ℒₛₑₜ (1 : V) ((^#1 : V) ∷ (0 : V)) := by
      simpa using IsUTermVec.adjoin IsUTermVec.empty h1
    simpa [show (2 : V) = 1 + 1 by norm_num] using IsUTermVec.adjoin ht1 hb
  rw [substs_rel (by rw [cEqN]; exact codeIn_rel_quote _) hv2]
  congr 1
  rw [show (2 : V) = 1 + 1 by norm_num,
      termSubstVec_cons hb (by simpa using IsUTermVec.adjoin IsUTermVec.empty h1),
      termSubst_bvar,
      show (1 : V) = 0 + 1 by norm_num,
      termSubstVec_cons h1 IsUTermVec.empty,
      termSubst_bvar, termSubstVec_nil]
  simp [termSubst_bvar, termSubstVec_cons, termSubstVec_nil]

end GodelQ.ProbeAA
