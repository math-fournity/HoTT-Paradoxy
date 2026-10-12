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

/-! ## 下一轮的两条路线（本轮都试过，未走通；结构已查清）

### 路线 A：一次归纳同时给「公式性 + `bv ≤ n + 1`」

`func` 分支要 `ve2_isUFormula`，其假设是 `IsSemiformula (1 + n)`；
分量 `iVE n v.[j]` 的层数由 `isSemiformula_iff` 配 `bv ≤ n + 1` 给出——
**正是第二个合取项**，所以两者必须同时归纳（分开证会成环）。

谓词 `P t := IsUFormula ℒₛₑₜ (iVE n t) ∧ bv ℒₛₑₜ (iVE n t) ≤ n + 1`。
`Σ₁` 闸门用 `Definable.and` 拼两块：第一块是 `IsUFormula ∘ iVE`（已过，见 `CG008IVE`）；
第二块是 `bv ∘ iVE ≤ n + 1`，用 `DefinableFunction.comp₂` 拼 `bv` 与常函数，再 `Definable.le`。
**本轮在这一步的 `comp₂` 参数形状上卡住**（`bv : V → V` 要写成
`fun v : Fin 1 → V ↦ bv (iVE n (v 0))` 的样子）。

### 路线 B：只证 `bv (eqAtom t) ≤ termBV t + 1`（`iVE` 归纳的基例）

`bv_rel` → `listMaxss_le_iff` 逐分量 → 两个分量分别是 `^#0`（`termBV = 1`）与 `t`。
**已推进到只剩两个分量的取值**：`nth_termBVVec` 给
`(termBVVec 2 ?[^#0,t]).[i] = termBV (?[^#0,t]).[i]`，
再用 `nth_zero`/`nth_succ` + `fstIdx_adjoin` 化简 `(?[^#0,t]).[i]`。
**卡点**：`nth_adjoin_zero` 等 `@[simp]` 引理在 `V` 上触发 `Zero ?m` 的合成歧义；
`nth_zero` 只给 `fstIdx` 形状，要再配 `termBV_bvar`。
**要点**：全程用 `≤` 不用 `=`（`V` 无 `OrderedRing`，`max_eq_left` 要的 `0 ≤ x` 没有现成引理）。

### 本轮实测可用的材料

- `listMaxss_le_iff`（`HFS/Vec.lean:740`）：`listMax v ≤ z ↔ ∀ i < len v, v.[i] ≤ z`
- `lt_succ_iff_le`（`FFL.FirstOrder.Arithmetic`）+ `le_iff_lt_or_eq`（**同 namespace，不加前缀**）
  ⇒ `i < 2` 拆成 `i = 0 ∨ i = 1`
- `len_termBVVec` / `nth_termBVVec`（`Term/Basic.lean:714/717`）
- `termBV_bvar : termBV ^#z = z + 1`、`termBV_fvar : termBV ^&x = 0`、`fstIdx_adjoin`
- `le_add_of_nonneg_right` / `add_le_add_right` / `positivity` 在 `V` 上可用
-/
