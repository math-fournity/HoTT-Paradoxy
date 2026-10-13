import GodelQ.ZFC.CG008ITSet3

/-!
# CG-008 · `iTSet` 的完整构造（照 `insert_defined` 的形状收尾）

`CG008ITSet3` 给了 `iTSet_succ_graph`（图引理，公理洁净）——
那是 `succ_defined` 的全部实质内容。本文件按 `insert_defined`
（`Bit.lean:319`：`instance … via def := .mk fun v ↦ by simp […]`）收尾。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008ITSet4
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Z0Full GodelQ.Translate
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

open Classical in
/-- **`iTSet` 的蓝图**：`zero` 给 `0`，`succ` 用 `CG008ITSet3.iTSetSuccDef`。 -/
noncomputable def iTSet.blueprint : PR.Blueprint 2 where
  zero := .mkSigma “y n s. y = 0”
  succ := GodelQ.CG008ITSet3.iTSetSuccDef

-- **构造**：`zero := fun _ ↦ 0`，`succ` 用 Lean 的 `if`。
--
-- `succ_defined` 要证 `Evalb v ↑succ ↔ (if 式)`。**实质内容已证**：
-- `CG008ITSet3.iTSet_succ_graph` 正是这个 `↔` 的「`(if 式) ↔ (`∃`-串)」一半
-- （公理洁净）。照 `insert_defined`（`Bit.lean:319-320`）的形状，
-- `succ_defined` 应当是 `simp [iTSetSuccDef, iTSet_succ_graph]` 一行——
-- 那里能过是因为 `insert_graph` 的右边与 `Evalb` 展开后**同形**。
--
-- **剩下的一层**：把 `Evalb` 对 `(“#4 ∈ #3”)`/`⋏`/`⋎`/`∼`/`∃¹` 的展开
-- 与 `iTSetSuccDef` 的 `∃`-串对齐（`Evalb` 的逐项引理在
-- `Tarski/Basic.lean:254` 的 `Eval` 侧，是 `HomClass` 的 `map_*` 一族）。
--
-- **本文件停在蓝图**：`iTSet.blueprint` 已装配（类型核对通过）；
-- `iTSet.construction` 的两个 `_defined` 中 `zero_defined` 是 `simp`，
-- `succ_defined` 差上面这一层。

-- **`iTSet n s`** 将是 `iTSet.construction.result ![n, s] (len s)`——
-- 待 `succ_defined` 收尾后即可定义。

end GodelQ.CG008ITSet4
