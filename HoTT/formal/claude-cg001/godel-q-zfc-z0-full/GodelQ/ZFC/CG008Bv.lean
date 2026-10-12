import GodelQ.ZFC.CG008ShiftProof

/-!
# CG-008 · `bv (iVE n t) ≤ n + 1`——`iVE_isUFormula` 的最后一环
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Bv
open GodelQ.ZFCArith GodelQ.Translate
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- **`bv (iVE n t) ≤ n + 1` 未证**——这是 `iVE_isUFormula` 的**最后一环**。
--
-- 目标：`bv ℒₛₑₜ (iVE n v.[j]) ≤ 1 + n`（`CG008IVE.iVE_isUFormula` 里已精确定位）。
-- 需要的是一条 `bv (iVE n t) ≤ n + 1`（对 `t` 归纳，与 `iVE` 的构造同步）。
--
-- **本轮查清的材料**：
-- * `eqAtom t = ^rel 2 cEqN ?[^#0, t]`，其 `bv` 由 `bv_rel`（`Formula/Basic.lean:1286`）
--   给出为 `listMax (termBVVec 2 ?[^#0, t])`；
-- * `termBVVec_cons`（`Term/Basic.lean:723`）把它化成 `?[termBV ^#0, termBV t]`；
-- * `termBV_bvar` 给 `termBV ^#0 = 1`；
-- * 剩下 `listMax ?[1, termBV t] = termBV t + 1`——**这一步本轮未走通**，
--   是纯列表算术（`listMax` 的定义在 Foundation `HFS/Vec.lean`）。
--
-- 三个分支的 `bv` 各自要处理：
-- * `bvar`：`eqAtom (^#(z+1))`，`bv = (z + 1) + 1 ≤ n + 1` 需 `z ≤ n - 1`——**由 `IsUTerm` 给**；
-- * `fvar`：`eqAtom (^&x)`，自由变量不占 `bv`，`bv = 0 + 1 ≤ n + 1`；
-- * `func`：`ve0`/`ve2` 的 `bv` 由 `conjunct`/`subst` 的层数给出。

end GodelQ.CG008Bv
