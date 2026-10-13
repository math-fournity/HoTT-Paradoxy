import GodelQ.ZFC.CG008ITSet5

/-!
# CG-008 · `iTSet` 的 Σ₁ 实例（收尾）

`CG008ITSet5` 写出 `iTSetGraph`：
`∃ l, lenDef l s ∧ resultDef y l n s`——`len` 的复合，`Rew.subst` 表达不了。

本文件记录收尾的**精确形状**与卡点。

## 卡点（技术性，与 `disjSeqSubstGraph` 同型）

`disjSeqSubstGraph`（`Iteration.lean:198`）是
```lean
blueprint.resultDef |>.rew (Rew.subst ![#0, #3, #1, #2])
```
——因为它的递归位置是**参数**，`rew` 的变量重命名够用。

`iTSet` 的递归位置是 `len s`（`s` 的**函数**），所以图要写成
`∃ l, lenDef l s ∧ resultDef …`（`iTSetGraph` 已写出这个形状），
实例的证明要把 `Evalb v ↑iTSetGraph` 化到
`result_defined_iff` 的实例上——**参数排列要逐位对齐**：

- `resultDef` 是 `“z u. …”`，即 `v 0 = z`（结果）、`v 1 = u`（递归位置）、
  `v 2..` = 参数；
- 我的 `mkSigma` 是 `“y n s. ∃ l, …”`，展开后
  `Evalb ![v 0, len (v 1), v 0, v 1] resultDef`——
  **`v 2` 位置要放 `n = v 0`、`v 3` 位置要放 `s = v 1`**。

对齐后 `constructor` + `result_defined_iff` 即可（`CG008ITSet6` 的
先前版本已把这两支写对，只差 `change`/`simp only` 的展开层次）。

**本文件停在「形状已固定」**：`iTSet` 的**构造**（`CG008ITSet4`，
含 `succ_defined`）**已建成**；Σ₁ 实例差这一层对齐。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008ITSet6
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Z0Full GodelQ.Translate
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- **零件核对**：`iTSet` 的构造与蓝图都在，图已写出。
noncomputable example : PR.Blueprint 2 := GodelQ.CG008ITSet4.iTSet.blueprint
noncomputable example : PR.Construction V GodelQ.CG008ITSet4.iTSet.blueprint :=
  GodelQ.CG008ITSet4.iTSet.construction
noncomputable example : 𝚺ᴬ₁.Semisentence 3 := GodelQ.CG008ITSet5.iTSetGraph

end GodelQ.CG008ITSet6
