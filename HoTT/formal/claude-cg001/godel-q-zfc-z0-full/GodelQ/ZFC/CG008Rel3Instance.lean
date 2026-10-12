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

**修法 2 也不通**：`uformula_result_induction`（`Formula/Basic.lean:1161`）
**同样**要 `hP : 𝚺ᴬ₁-Relation₃ P`：

```lean
lemma uformula_result_induction {P : V → V → V → Prop} (hP : 𝚺ᴬ₁-Relation₃ P) ...
```

**所以两条路都卡在同一个闸门**：`𝚺ᴬ₁-Relation₃ (fun _ _ r ↦ IsUFormula L r)`
的构造。

**这不是「换归纳原理」能绕开的**——是**必须**建这个实例。

**本行记录这个决定性的判断**：
`subst_isUFormula` 的装配**唯一**的实际障碍是
「把一元 `IsUFormula.definable` 变成三元投影版本」，
而那是纯 API 工作（读 `Definable` 系列的复合工具）。 -/

/-! ## 建实例：用 `DefinablePred.comp`

`Tarski/Definability.lean:388`：

```lean
lemma DefinablePred.comp {P : M → Prop} {k} {f : (Fin k → M) → M}
    [hP : L.DefinablePred P] (hf : L.DefinableFunction f) : L.DefinablePred (P ∘ f)
```

**取 `P := IsUFormula`、`f := fun v : Fin 3 → V ↦ v 2`（投影）**，
则 `P ∘ f = fun v ↦ IsUFormula (v 2)`——**正是三元形状**。 -/

-- **查实 3**：投影 `fun v : Fin 3 → V ↦ v 2` 是可定义函数。
-- `var`（`Tarski/HierarchicalDefinability/Basic.lean:688`）：
--   `@[simp] lemma var [L.Eq] [Tarski.Structure.Eq L V] {k} (i : Fin k) : …`

/-- **主结果**：三元实例——`IsUFormula` 复合投影。

**这是两条路线共同的闸门**，建成即解锁 `subst_isUFormula` 的装配。 -/
theorem isUFormula_relation3 :
    𝚺ᴬ₁-Relation₃ (fun _ _ r : V ↦ Bootstrapping.IsUFormula ℒₛₑₜ r) := by
  -- `(fun _ _ r ↦ IsUFormula r)` 与 `(fun v : Fin 3 → V ↦ IsUFormula (v 2))` 等价
  have hP : 𝚺ᴬ₁-Predicate (fun r : V ↦ Bootstrapping.IsUFormula ℒₛₑₜ r) := inferInstance
  have hf : 𝚺ᴬ₁.DefinableFunction (fun v : Fin 3 → V ↦ v 2) :=
    Bounding.HierarchySymbol.DefinableFunction.var 2
  have hcomp := Bounding.HierarchySymbol.DefinablePred.comp hP hf
  apply Bounding.HierarchySymbol.Definable.of_iff hcomp
  intro v
  simp

-- 公理洁净检查
#print axioms GodelQ.CG008Rel3Instance.isUFormula_relation3

end GodelQ.CG008Rel3Instance
