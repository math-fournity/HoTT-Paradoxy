-- CG-009: 开口律的**正确**逐项核算（替换前几版不准确的记录）。
--
-- ## 定律（`ITSubstOpen.iT_subst_open`，m = 0 即 hAB 所需）
--
--     iT m (subst ℒₒᵣ (QvecVOr m) q) = subst ℒₛₑₜ (QvecV m) (iT (m+1) q)     (q : 层 m+1)
--
-- ## rel 支的核算（**两侧的向量长度确实不同，但这不构成矛盾**）
--
-- 记 `t := v.[j]`（层 m+1），`Y := iVE (m+1) t`（层 m+2）。
--
-- **LHS**：`iT m (^rel … (termSubstVec (QvecVOr m) v))` → `iTR m` 的 conjunct
-- 用向量 `L := ^#j ∷ shiftVec 2 m`（长度 m+1，层 m+2），作用于 `iVE m (termSubst (QvecVOr m) t)`。
--
-- **RHS**：`subst (QvecV m) (iTR (m+1) …)`。`iTR (m+1)` 有 `qqAlls … 2`，
-- `subst` 下降两层把 `QvecV m` 换成 `qVec²(QvecV m) = QvecV (m+2)`（长度 m+3）。
-- 体内的 conjunct 用向量 `R := ^#j ∷ shiftVec 2 (m+1)`（长度 m+2，层 m+3）。
-- 由 `substs_substs`（w = QvecV (m+2) 长度 m+3 = R 的层数 ✓）：
--     subst (QvecV (m+2)) (subst R Y) = subst (termSubstVec (m+2) (QvecV (m+2)) R) Y
-- 而 `termSubstVec (m+2) (QvecV (m+2)) R = [^#j, ^#2, …, ^#(m+1), ^&0]`（长度 m+2）。
--
-- ## 两侧的一致性（关键）
--
-- 需证（对层 m+1 的 t）：
--     subst L (iVE m (termSubst (QvecVOr m) t)) = subst R' (iVE (m+1) t)
-- 其中 `R' := [^#j, ^#2, …, ^#(m+1), ^&0]`。
--
-- 逐 bvar `z`（`z ≤ m`，因 t 在层 m+1）：
-- * `z < m`：LHS 走 `QvecVOr m` 第 z 项 `^#z` → `iVE m` 给 `eqAtom ^#(z+1)`
--   → subst 读索引 `z+1 ≤ m` → `^#(z+1)`；
--   RHS 走 `eqAtom ^#(z+1)` → subst 读索引 `z+1 ≤ m` → `^#(z+1)`。**一致**。
-- * `z = m`：LHS 走 `QvecVOr m` 第 m 项 `^&0` → `iVE m ^&0 = eqAtom ^&0`
--   → subst 不动 fvar → `eqAtom ^&0`；
--   RHS 走 `eqAtom ^#(m+1)` → subst 读索引 `m+1` = R' 的**末项** `^&0`
--   → `eqAtom ^&0`。**一致**。
--
-- ⟹ **定律为真**；R' 比 L 多出的末项 `^&0` 恰好承接 `z = m` 那一支。
import GodelQ.ZFC.OpenLawCheck2

open FFL FFL.FirstOrder FFL FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.OpenLawCheck5
variable {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat

-- 机器事实 1：下降两层 = QvecV (m+2)
example (m : V) : qVec ℒₛₑₜ (qVec ℒₛₑₜ (QvecV (V := V) m)) = QvecV (V := V) (m + 2) := by
  rw [← QvecV_succ, ← QvecV_succ]
  congr 1
  ring

-- 机器事实 2：`QvecV (m+2)` 的末项在索引 m+2 处
example (m : V) : (QvecV (V := V) (m + 2)).[m + 2] = (^&0 : V) := nth_QvecV_last (m + 2)

-- 机器事实 3：`QvecV (m+2)` 在索引 z+1 ≤ m+1 处是 `^#(z+1)`
example (m z : V) (hz : z < m + 1) : (QvecV (V := V) (m + 2)).[z + 1] = (^#(z + 1) : V) := by
  have h2 : z + 1 < m + 2 := by
    have h := add_lt_add_right hz 1
    rw [add_comm (1 : V) z, add_comm (1 : V) (m + 1),
      show (m + 1 : V) + 1 = m + 2 by ring] at h
    exact h
  exact nth_QvecV_lt (m + 2) (z + 1) h2

end GodelQ.OpenLawCheck5
