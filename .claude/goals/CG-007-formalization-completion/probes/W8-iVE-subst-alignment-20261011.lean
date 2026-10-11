import GodelQ.ZFC.ShCraigElimBranches
import GodelQ.ZFC.TranslateShiftCompat

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.TranslateShiftCompat

set_option maxHeartbeats 800000

namespace GodelQ.ProbeAI
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 关键对齐检验：用 qVec 向量时，subst 与 iVE 在 bvar 上是否一致？
-- iVE 0 (^#0) = eqAtom (^#1) = ^rel 2 cEqN (?[^#0, ^#1])
-- subst (qVec ?[^&0]) (iVE 1 ^#0) = subst (^#0 ∷ ^&0 ∷ 0) (eqAtom ^#1)
--   = ^rel 2 cEqN (?[^#0, ^&0])        ← eqAtom 的 #0 保留、#1 被换成 ^&0
-- 而 iVE 0 (subst ?[^&0] ^#0) = iVE 0 (^&0) = eqAtom (^&0) = ^rel 2 cEqN (?[^#0, ^&0])  ✓ 一致！

lemma iVE_subst_bvar (z : V) :
    iVE 0 (subst ℒₒᵣ (?[^&0] : V) (^#z : V)) = subst ℒₛₑₜ (qVec ℒₛₑₜ (?[^&0] : V)) (iVE 1 (^#z : V)) := by
  show iVE 0 (subst ℒₒᵣ (?[^&0] : V) (^#z : V))
      = subst ℒₛₑₜ (qVec ℒₛₑₜ (?[^&0] : V)) (iVE 1 (^#z : V))
  rw [substs_bvar]
  -- 左边：iVE 0 ((?[^&0]).[z])
  -- z = 0 时是 iVE 0 ^&0 = eqAtom ^&0；z ≠ 0 时 (?[^&0]).[z] = 0（越界）
  sorry

end GodelQ.ProbeAI
