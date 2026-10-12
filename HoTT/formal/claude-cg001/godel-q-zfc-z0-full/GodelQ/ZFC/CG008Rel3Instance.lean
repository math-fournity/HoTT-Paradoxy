import GodelQ.ZFC.CG008SubstFormula

/-!
# CG-008 · 试建 `𝚺ᴬ₁-Relation₃ (fun _ _ r ↦ IsUFormula L r)`（修法 1）

## 为什么不用 `definability`

`definability` 在这个形状上 `whnf` 超时——它似乎去展开 `IsUFormula` 的 `Fixpoint` 定义。

**修法 1**：**显式构造**——`(fun _ _ r ↦ IsUFormula L r)` 是
「`IsUFormula` 复合一个投影」，而 Foundation 有：
- `IsUFormula.definable`（`Formula/Basic.lean` 的实例）；
- 复合的工具（`Bounding.HierarchySymbol.DefinablePred.comp` 等）。

## 治理

- Foundation 只读；本文件纯下游。
- 若成功则无未证标记、可进收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Rel3Instance

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1**：`IsUFormula.definable` 已有——一元版本。 -/
example : 𝚺ᴬ₁-Predicate (fun r : V ↦ Bootstrapping.IsUFormula ℒₛₑₜ r) :=
  inferInstance

/- **查实 2（试建，未成）**：三元版本的**显式构造**。

试借 `DefinablePred.comp` 与投影函数，**两处受阻**：
1. `Function₃` 的记法吃 `Fin 3 → V` 的向量而非三个独立参数——
   投影要写成 `fun v : Fin 3 → V ↦ v 2`，而 `definability` 在该形状上仍失败；
2. `DefinablePred.comp` 的参数顺序与预期不同。

**所以修法 1 需要更仔细地读 `Definable` 系列的 API**——
不是「写一行就成」，但也不是概念障碍。

**修法 2（更可能成功）**：**避开 `sigma1_succ_induction`**，
改用 `subst` 的 `uformula_result_induction`（`Formula/Basic.lean:1161`），
它按 `subst` 的**递归结构**归纳，可能不需要 `𝚺ᴬ₁-Relation₃` 那一层。

**本行记录两条修法的实测状态。** -/

end GodelQ.CG008Rel3Instance
