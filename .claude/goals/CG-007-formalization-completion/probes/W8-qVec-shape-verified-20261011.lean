import GodelQ.ZFC.ShCraigElimBranches
import GodelQ.ZFC.TranslateShiftCompat

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.TranslateShiftCompat

set_option maxHeartbeats 800000

namespace GodelQ.ProbeAH
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 检验：substs_all 的 qVec 形状是否让 iVE 与 subst 对齐
-- iVE n (^#z) = eqAtom ^#(z+1) = ^rel 2 cEqN (?[^#0, ^#(z+1)])
-- 若把 subst 的向量设成 qVec（首分量 ^#0），则 eqAtom 的 #0 不被改

-- 试：iVE 与 subst 在 **bvar** 上的对齐
-- subst (qVec ?[^&0]) (iVE 1 ^#0)
--   = subst (^#0 ∷ termBShiftVec 1 ?[^&0]) (eqAtom ^#1)
--   = subst (^#0 ∷ ^&0 ∷ 0) (eqAtom ^#1)      [termBShiftVec 1 ?[^&0] = ?[^&0]（fvar 不动）]
example : qVec ℒₛₑₜ (?[^&0] : V) = ((^#0 : V) ∷ (?[^&0] : V)) := by
  rw [qVec]
  congr 1
  -- termBShiftVec 1 ?[^&0] = ?[^&0]（fvar 不动）
  rw [show (len (?[^&0] : V)) = (1 : V) from by simp]
  rw [show (1 : V) = 0 + 1 by norm_num,
      termBShiftVec_cons (IsUTerm.fvar 0) IsUTermVec.empty,
      termBShift_fvar, termBShiftVec_nil]

end GodelQ.ProbeAH
