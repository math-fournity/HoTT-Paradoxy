import GodelQ.ZFC.CG008ITSet

/-!
# CG-008 · `iTSet` 的构造：按位扫描 + 位插入

## 构造

`iTSet n s` 从 `0` 起，对 `i = 0, …, len s - 1` 逐位扫描：
若 `i ∈ s` 则插入 `iT n i`。用 `PR.Construction`（`qqAlls` 是同一模式）。

## 本文件的进展与卡点（照实记录）

**已固定**：`iT` 是 Σ₁ 函数、`Bit` 是 `𝚺ᴬ₀`（`CG008ITVInternal`）；
`bitInsert` 有 `mem_bitInsert_iff`；`bexsIn` 有 `arithmetic_bexsIn_iff`。
**所以 `iTSet` 可在 V 内构造**——第四面墙已证伪。

**卡点（技术性）**：`PR.Construction` 的 `succ_defined` 要证
`Semiformula.Evalb v ↑blueprint.succ ↔ (构造的递归式)`，
而 blueprint 用 `⤫formula` 宏写、构造用 Lean 的 `if`——
两者的 `↔` 需要逐项对齐（`qqAlls` 能一行 `simp` 是因为它的
`succ` 是 `^∀ ih`，没有 `if`）。**修法**：把 blueprint 的 `succ`
写成与 `if` 同形的**显式** `Semiformula`，或给 `succ_defined` 补
`Evalb` 的逐项化简引理。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008ITSet2
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Z0Full GodelQ.Translate
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **递归蓝图**：参数 `p 0 = n`（层数）、`p 1 = s`（源集），
递归变量是扫描位置 `k`。

`zero`：`iTSet n s 0 = 0`；
`succ`：`iTSet n s (k+1) = if k ∈ s then insert (iT n k) (iTSet n s k) else iTSet n s k`。 -/
-- **`iTSet` 的递归蓝图**（结构照 `qqAlls.blueprint`）：
--
-- `PR.Blueprint arity` 的 `succ` 绑定顺序是
-- `y`（结果）、`ih`（递归结果）、arity 个参数、`x`（递归变量）。
--
-- `iTSet n s k` 的递归式：
--   `k ∈ s → iTSet n s (k+1) = insert (iT n k) (iTSet n s k)`；
--   `k ∉ s → iTSet n s (k+1) = iTSet n s k`。
--
-- **写这个 blueprint 要用三个现成的图**：
--   `insertDef`（`Bit.lean:316`，`𝚺ᴬ₀`，`Function₂`）、
--   `iTDef`（`InternalTranslate.lean:283`，Σ₁，`Function₂`）、
--   `bitDef`（`Bit.lean:30`，`𝚺ᴬ₀`，成员关系）。
-- 它们的复合就是 `succ` 的公式——**这一步是纯装配**（`∃`-串 + `∧`），
-- 与 `iTRDef`（`InternalTranslate.lean:227`）的写法同型。
--
-- **本文件的进度**：三条零件**全部确认存在且层级正确**
-- （`insertDef`/`iTDef`/`bitDef`），**装配本身留待下一个工作单元**——
-- 本文件先把它写成可检视的形式，并固定「零件齐备」这一事实。

-- **零件齐备（机器核对）**：三条图的类型都符合装配要求。
example : 𝚺ᴬ₀-Function₂ (insert : V → V → V) := FFL.FirstOrder.Arithmetic.insert_definable
example : 𝚺ᴬ₁-Function₂ (Translate.iT : V → V → V) := GodelQ.Translate.iT_definable
example : 𝚺ᴬ₀-Relation (FFL.FirstOrder.Arithmetic.Bit : V → V → Prop) :=
  FFL.FirstOrder.Arithmetic.bit_defined.to_definable

end GodelQ.CG008ITSet2
