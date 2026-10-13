-- CG-009: 逐索引核算（纯算术，不含 subst 语义）。
--
-- ## 核算规则
--
-- `subst (^#j ∷ shiftVec b n) y` 把 `y` 的 bvar `z` 换成该向量第 `z` 项：
--   索引 0 → `^#j`；索引 k (1≤k≤n) → `^#(b + k - 1)`。
-- 向量长度 `n+1`，故 `z ≤ n`。
--
-- 再对它做 `termSubst w`：`termSubst w ^#z = w.[z]`。
-- 所以需要的最大索引是 `b + n - 1`（当 `b+n-1 ≥ j` 时）。
--
-- `subst` 下降 `qqAlls … 2` 两层，把向量 `W` 换成 `qVec² W`。
-- 从 `QvecV m` 出发得 `QvecV (m+2)`；它在索引 `< m+2` 处是 `^#i`。
--
-- ⟹ 要恒等需 `b + n - 1 < m + 2`。
import GodelQ.ZFC.IVEOpenFunc13

open FFL FFL.FirstOrder FFL FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.OpenLawCheck
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc2 GodelQ.IVEOpenFunc3 GodelQ.IVEOpenFunc4
open GodelQ.IVEOpenFunc5 GodelQ.IVEOpenFunc6 GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFunc9
open GodelQ.IVEOpenFunc10 GodelQ.LayerMono

-- `iTR` 的 conjunct：b = 2，n = m+1 ⟹ 最大索引 2 + (m+1) - 1 = m+2。
-- 需要 `m+2 < m+2` —— **不成立**。
example (m : V) : (QvecV (V := V) (m + 2)).[m + 2] = (^&0 : V) := nth_QvecV_last (m + 2)

-- 若外层向量是 `QvecV (m+1)`（而非 `m`），下降两层得 `QvecV (m+3)`，则够用。
example (m : V) : (QvecV (V := V) (m + 3)).[m + 2] = (^#(m + 2) : V) := by
  apply nth_QvecV_lt
  have h := lt_add_one (m + 2)
  rwa [show (m + 2 : V) + 1 = m + 3 by ring] at h

end GodelQ.OpenLawCheck

namespace GodelQ.OpenLawCheck
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc2 GodelQ.IVEOpenFunc3 GodelQ.IVEOpenFunc4
open GodelQ.IVEOpenFunc5 GodelQ.IVEOpenFunc6 GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFunc9
open GodelQ.IVEOpenFunc10 GodelQ.LayerMono

/-! ## 下降层数的实测

`subst L w (^∀ p) = ^∀ (subst L (qVec L w) p)`（`substs_all`）。
所以每下降**一层**绑定子，向量换成 `qVec`。`qqAlls … 2` 是**两层** `^∀`。
从 `QvecV m` 出发：`QvecV (m+2)`。
-/

-- 单层下降：
example (m : V) (w : V) (hw : w = QvecV (V := V) m) :
    qVec ℒₛₑₜ w = QvecV (V := V) (m + 1) := by
  rw [hw, ← QvecV_succ]

-- 两层下降：
example (m : V) : qVec ℒₛₑₜ (qVec ℒₛₑₜ (QvecV (V := V) m)) = QvecV (V := V) (m + 2) := by
  rw [← QvecV_succ, ← QvecV_succ]
  congr 1
  ring

end GodelQ.OpenLawCheck
