import GodelQ.ZFC.ShCraigElimBranches
import GodelQ.ZFC.TranslateShiftCompat

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.TranslateShiftCompat

set_option maxHeartbeats 800000

namespace GodelQ.ProbeR

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 先看清 subst 对 eqAtom 的作用（eqAtom t = ^rel 2 cEqN ?[#0, t]）
-- subst ?[^&0] (eqAtom t)：把 fvar 0 塞进去
-- 但 ?[^&0] 的长度是 1，subst 对 ^rel 2 ... 的向量只有 2 个分量
-- 向量里是 bvar #0 和 t。subst 会把 #0 换成 ^&0（w.[0]），把 t 递归处理。

-- 试直接证 iVE_subst 的 fvar 情形（最简单）
-- iVE n (termSubst ℒₒᵣ ?[^&0] t) = ?
-- termSubst 对 fvar 不动，对 bvar 换成 w.[z]

-- 先看 eqAtom 与 subst 的交换
example (t : V) :
    subst ℒₛₑₜ ?[^&0] (eqAtom t) = eqAtom (subst ℒₛₑₜ ?[^#0] t) := by
  sorry

end GodelQ.ProbeR
