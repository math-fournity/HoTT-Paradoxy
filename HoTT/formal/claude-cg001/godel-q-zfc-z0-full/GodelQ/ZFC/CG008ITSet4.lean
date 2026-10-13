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

open Classical in
/-- **构造**：`zero := fun _ ↦ 0`，`succ` 用 Lean 的 `if`；
`succ_defined` 照 `insert_defined`（`Bit.lean:319-320`）用 `simp`。 -/
noncomputable def iTSet.construction : PR.Construction V iTSet.blueprint where
  zero := fun _ ↦ 0
  -- 照 `DisjSeqSubst.construction`（`Iteration.lean:181`）的约定：
  -- `succ param k ih`——`k` 是索引、`ih` 是前一值；
  -- 句子绑定 `“y ih k n s. …”` 即 `v 0 = y`、`v 1 = ih`、
  -- `v 2`/`v 3` = 两个 param、`v 4` = `k`。
  succ := fun param k ih ↦ if k ∈ param 1 then insert (Translate.iT (param 0) k) ih else ih
  zero_defined := .mk fun v ↦ by simp [iTSet.blueprint]
  succ_defined := .mk fun v ↦ by
    simp [iTSet.blueprint, GodelQ.CG008ITSet3.iTSetSuccDef,
      GodelQ.CG008ITSet3.iTSet_succ_graph]

/-- **`iTSet n s`**：从 `0` 扫到 `len s`，把 `iT n` 逐元素作用上去。

`iTSet n s = {iT n p | p ∈ s}`（位编码集合上的替换像）。 -/
noncomputable def iTSet (n s : V) : V :=
  iTSet.construction.result ![n, s] (Arithmetic.len s)

-- **`iTSet` 的 Σ₁ 性**（收尾的形状）：照 `disjSeqSubstGraph`
-- （`Iteration.lean:198-209`）——
-- ```lean
-- noncomputable def iTSetGraph : 𝚺ᴬ₁.Semisentence 4 :=
--   iTSet.blueprint.resultDef |>.rew (Rew.subst ![#0, #3, #1, #2])
-- instance iTSet.defined : 𝚺ᴬ₁-Function₃[V] iTSet via iTSetGraph :=
--   .mk fun v ↦ by simp [construction.result_defined_iff, iTSetGraph, iTSet]
-- ```
-- **但 `iTSet` 只吃两个参数**（`n`、`s`），而递归位置是 **`len s`**——
-- 一个 `s` 的**函数**，`rew`（只做变量重命名）表达不了。
-- 所以 `iTSet` 的图要么 (a) 写成 `Function₂` 加一层 `len` 的复合
-- （`DefinableFunction.comp`），要么 (b) 把递归位置也做成参数。
-- **本文件停在 `iTSet` 的定义**：`construction`（含 `succ_defined`）已过，
-- 图与实例属下一个工作单元。

end GodelQ.CG008ITSet4
