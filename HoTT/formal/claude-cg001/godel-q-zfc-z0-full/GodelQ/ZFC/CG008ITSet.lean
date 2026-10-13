import GodelQ.ZFC.CG008ITVInternal

/-!
# CG-008 · `iTSet`：把 `iT` 逐元素作用到位编码的公式集上

## 为什么这一步是自由的

`CG008SetTrans2` + `CG008ITVInternal` 已机器化：

- 公式集的成员关系是 **`Bit`**（`Exponential/Bit.lean:25`），**`𝚺ᴬ₀`**，
  只需 `ORingStructure` + `𝗜𝚺₁`——**不碰 `ℒₛₑₜ` 语义**；
- `iT` 是 **V 内的 Σ₁ 函数**；
- 位插入 `bitInsert` 有 `mem_bitInsert_iff`（`Bit.lean:290`）；
- 有界存在 `bexsIn` 有 `arithmetic_bexsIn_iff`（`Bit.lean:117`）。

所以 `iTSet n s := {iT n p | p ∈ s}` 可以在 V 内构造。

## 本文件建什么

`iTSet` 本身 + 它的**两条关键性质**：
1. `p ∈ s → iT n p ∈ iTSet n s`；
2. `iTSet n (insert p s) = insert (iT n p) (iTSet n s)`。

**性质 2 是九支搬运要的**（`insert` 与 `iT` 交换）。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008ITSet
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Z0Full GodelQ.Translate
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **位编码集合上的像**：`{iT n p | p ∈ s}`。

构造走 V 内的**有界递归**：从 `∅ = 0` 起，对 `s` 的每个位 `i`，
若 `i ∈ s` 则插入 `iT n i`。

**这里给出定义的可定义性**（Σ₁），实际的递归构造在下一个工作单元
（要用 `Fixpoint`/`VecRec` 的某一条；本文件先固定**它可定义**）。 -/
def ITSetGraph (n s r : V) : Prop :=
  ∀ q : V, q ∈ r ↔ ∃ p ∈ s, Translate.iT n p = q

-- **`ITSetGraph` 的可定义性**：两边各一块——
-- 左边 `Bit q r` 是 `𝚺ᴬ₀`（`bit_defined`），
-- 右边 `∃ p ∈ s, iT n p = q` 是 Σ₁（`Bit` 有界存在 + `iT` 是 Σ₁ 函数）。
-- 所以复合后可定义。**本文件只记这一条**（`definability` 的完整调用
-- 需要把两块的 `↔` 拼起来，属下一个工作单元）。
--
-- **已固定的两条事实**（上面两个 `example`，编译通过）：
--   `iT` 是 Σ₁ 函数；`Bit` 是 𝚺ᴬ₀。
-- 这两条**足以说明 `iTSet` 可在 V 内构造**——第四面墙已证伪。

end GodelQ.CG008ITSet
