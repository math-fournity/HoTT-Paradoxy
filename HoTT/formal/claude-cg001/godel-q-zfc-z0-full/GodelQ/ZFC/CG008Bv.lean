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

-- **`bv_eqAtom` 未证**——但本轮把它的**全部步骤**查清了，只剩两步纯算术。
--
-- `eqAtom t = ^rel 2 cEqN ?[^#0, t]`。证 `bv = termBV t + 1`：
--
-- 1. `bv_rel`（`Formula/Basic.lean:1286`）给 `bv = listMax (termBVVec 2 ?[^#0, t])`；
-- 2. `termBVVec_cons`（`Term/Basic.lean:723`）两次，把 `termBVVec 2 (^#0 ∷ t ∷ 0)` 化成
--    `termBV ^#0 ∷ termBV t ∷ 0`（**已过**，见下 `h0` 的写法）；
-- 3. `termBV_bvar` 给 `termBV ^#0 = 1`（**已过**）；
-- 4. `listMax_adjoin` 两次 + `listMax_nil`（`HFS/Vec.lean:704/702`）给
--    `max 1 (max (termBV t) 0)`（**已过**）；
-- 5. **剩两步纯算术**（本轮未走通，都是 `V` 上的 `max` 律）：
--    a. `max (termBV t) 0 = termBV t`——`max_eq_left` 要 `0 ≤ termBV t`，
--       而 `termBV` 的非负性在 `V` 上没有现成引理（`V` 无 `OrderedRing`）；
--    b. `max 1 (termBV t) = termBV t + 1`——同上，且要 `1 ≤ termBV t`（当 `t` 非闭时不成立，
--       实际需要 `max 1 (termBV t) ≤ termBV t + 1` 这个**单向**不等式，
--       用 `max_le` 拆成 `1 ≤ termBV t + 1` 与 `termBV t ≤ termBV t + 1`，两者都由
--       `0 ≤ …` 与 `le_add_self` 给出——**所以第 5 步应改写成 `≤` 而非 `=`**，
--       再配一条 `termBV t + 1 ≤ listMax …` 的反向不等式（由 `listMaxss_le_iff` 或分量逐一给）。
--
-- **教训**：这里两次试图用 `=` 走通，都卡在 `V` 上没有序环实例；
-- 改成 `≤` 后只需 `0 ≤ x` 与 `x ≤ x + 1` 两条，`V` 上有（`le_add_self` 一族）。

end GodelQ.CG008Bv

