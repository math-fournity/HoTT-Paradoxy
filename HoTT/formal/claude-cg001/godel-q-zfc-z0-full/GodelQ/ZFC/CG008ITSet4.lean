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

-- **构造的收尾**：`zero := fun _ ↦ 0`，`succ` 用 Lean 的 `if`。
--
-- `succ_defined` 要证 `Evalb v ↑succ ↔ (if 式)`。**实质内容已证**：
-- `CG008ITSet3.iTSet_succ_graph` 正是这个 `↔` 的「`(if 式) ↔ (`∃`-串)」一半
-- （公理洁净）。**剩下的是 `Evalb` 的展开**——把
-- `(“#4 ∈ #3”) ⋏ (∃¹ …) ⋎ ∼(“#4 ∈ #3”) ⋏ (“#0 = #1”)`
-- 化简成 `iTSet_succ_graph` 左边的形状（`Evalb` 对
-- `⋏`/`⋎`/`∼`/`∈`/`∃¹` 的逐项引理，在 `Tarski.Structure` 侧）。
--
-- **本文件停在蓝图**：`iTSet.blueprint` 已装配（类型核对通过），
-- `iTSet.construction` 的两个 `_defined` 中 `zero_defined` 是 `simp`，
-- `succ_defined` 差 `Evalb` 展开这一层。

-- **`iTSet n s`** 将是 `iTSet.construction.result ![n, s] (len s)`——
-- 待 `succ_defined` 收尾后即可定义。

end GodelQ.CG008ITSet4
