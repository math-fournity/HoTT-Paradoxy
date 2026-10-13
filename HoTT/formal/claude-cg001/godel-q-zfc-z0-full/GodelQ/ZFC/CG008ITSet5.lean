import GodelQ.ZFC.CG008ITSet4

/-!
# CG-008 · `iTSet` 的 Σ₁ 性

`iTSet n s = construction.result ![n, s] (len s)`——递归位置是 **`len s`**，
`s` 的函数。`Rew.subst` 只做变量重命名，表达不了它，
所以照 `disjSeqSubstGraph`（`Iteration.lean:198`）的 `rew` 写法不够。

## 做法

把 `result` 的图（`Function₃`：`(z, u, param0, param1)` 式的 4 元）
与 `len` 复合：`iTSet` 的图是

```
∃ l, !lenDef l s ∧ !resultDef u l n s
```

——`lenDef` 给 `l = len s`，`resultDef` 用 `l` 作递归位置。
这样 `iTSet` 就是 `Function₂`（参数 `n`、`s`）。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008ITSet5
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Z0Full GodelQ.Translate
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`iTSet` 的图**：`∃ l, len s = l ∧ resultDef (y, l, n, s)`。

（`resultDef` 是 `(k + 2) = 4` 元的：`z`（结果）、`u`（递归位置）、
两个 param。这里 `z = y`、`u = l`、param0 = `n`、param1 = `s`。） -/
noncomputable def iTSetGraph : 𝚺ᴬ₁.Semisentence 3 := .mkSigma
  “y n s. ∃ l, !lenDef l s ∧ !(GodelQ.CG008ITSet4.iTSet.blueprint.resultDef) y l n s”

-- **`iTSet` 的 Σ₁ 实例**：形状照 `disjSeqSubst.defined`
-- （`Iteration.lean:205-209`）：
-- ```lean
-- instance iTSet.defined : 𝚺ᴬ₁-Function₂[V] iTSet via iTSetGraph :=
--   .mk fun v ↦ by simp [iTSetGraph, iTSet, PR.Construction.result_defined_iff]
-- instance iTSet.definable : 𝚺ᴬ₁-Function₂[V] iTSet := iTSet.defined.to_definable
-- instance iTSet.definable' (Γ k) : Γᴬ_[k + 1]-Function₂[V] iTSet :=
--   iTSet.definable.of_sigmaOne
-- ```
-- **卡点（技术性）**：`mkSigma` 的目标是 `Evalb v ↑iTSetGraph ↔ v 0 = iTSet …`，
-- 展开 `iTSetGraph` 后要 `Evalb ![v0, len (v1), v1, v2] resultDef ↔ …`——
-- 即 `result_defined_iff` 的实例，但**参数排列与 `resultDef` 的绑定序
-- 要逐位对齐**（`resultDef` 是 `(z, u, params…)`，我给的 `mkSigma` 是
-- `(y, n, s)` 加内部 `l`）。**逐位对齐是纯机械工作**，
-- 与 `disjSeqSubstGraph` 的 `Rew.subst ![#0, #3, #1, #2]` 同型。

end GodelQ.CG008ITSet5
