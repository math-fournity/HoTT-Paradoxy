import GodelQ.ZFC.CG008ITSet5

/-!
# CG-008 · `iTSet` 的 Σ₁ 实例（照 `disjSeqSubst` 的确切形状）

`disjSeqSubst`（`Iteration.lean:191`）的做法是**把递归位置做成显式参数**：

```lean
noncomputable def disjSeqSubst (w p k : V) : V := construction.result ![w, p] k
noncomputable def disjSeqSubstGraph : 𝚺ᴬ₁.Semisentence 4 :=
  blueprint.resultDef |>.rew (Rew.subst ![#0, #3, #1, #2])
```

——`resultDef` 是 `(z, u, param0, param1)`，`Rew.subst ![#0, #3, #1, #2]`
把它映到 `(y, k, w, p)`。**这样就不需要 `len` 的复合。**

`iTSet` 照抄：`iTSet n s k := construction.result ![n, s] k`，
用的时候取 `k := len s`。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008ITSet6
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Z0Full GodelQ.Translate
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`iTSet n s k`**：把 `iT n` 作用到 `s` 的前 `k` 位上。
（用的时候取 `k := len s`，即整个 `s`。） -/
noncomputable def iTSet (n s k : V) : V :=
  GodelQ.CG008ITSet4.iTSet.construction.result ![n, s] k

/-- **图**：照 `disjSeqSubstGraph`（`Iteration.lean:198`）。 -/
noncomputable def iTSetGraph : 𝚺ᴬ₁.Semisentence 4 :=
  GodelQ.CG008ITSet4.iTSet.blueprint.resultDef |>.rew (Rew.subst ![#0, #3, #1, #2])

-- **Σ₁ 实例**：目标形状（机器读出）是
--   `Eval (val v ∘ ![#0,#3,#1,#2]) Empty.elim resultDef ↔ v0 = iTSet (v1) (v2) (v3)`
-- 而 `result_defined_iff` 给的正是左半边（在 `Evalb ![v0,v3,v1,v2]` 记法下）。
-- 两者**定义上相同**（`Evalb b = Eval b Empty.elim`，`Fin.cons` 就是 `![]`），
-- 所以 `exact` 应当在把 `![]` 写成 `Fin.cons` 串后直接成立。
--
-- **收尾的精确位置**（本轮查实）：
--
-- 展开后左边是 `Eval (Semiterm.val v Empty.elim ∘ ![#0,#3,#1,#2]) Empty.elim resultDef`，
-- 而 `result_defined_iff` 给的是 `Evalb ![v0,v3,v1,v2] resultDef`。
-- **两者定义上相同**（`Evalb b = Eval b Empty.elim`；`Semiterm.val v Empty.elim ∘ ![…]`
-- 逐项就是 `![v 0, v 3, v 1, v 2]`），但 Lean 的 `isDefEq` 不直接穿
-- `Function.comp` + `Matrix.vecCons` 的这层。
--
-- **修法**（明确，纯机械）：用 `funext` 证两条向量的相等，
-- 再 `rw` 它，然后 `exact result_defined_iff …`。

/-- **两条向量的相等**（收尾要的桥）。 -/
theorem val_comp_vec (v : Fin (3 + 1) → V) :
    (Semiterm.val (L := ℒₒᵣ) v Empty.elim ∘ ![#0, #3, #1, #2]) = ![v 0, v 3, v 1, v 2] := by
  funext i
  fin_cases i <;> simp [Function.comp_apply, Matrix.cons_val, Semiterm.val_bvar]

/-- **`iTSet` 的 Σ₁ 实例**（用上面的桥）。 -/
instance iTSet.defined : 𝚺ᴬ₁-Function₃[V] iTSet via iTSetGraph :=
  .mk fun v ↦ by
    simp only [iTSetGraph, iTSet,
      Bounding.HierarchySymbol.Semiformula.val_rew, Semiformula.eval_substs,
      Function.comp_apply]
    rw [val_comp_vec]
    exact PR.Construction.result_defined_iff
      (c := GodelQ.CG008ITSet4.iTSet.construction)
      (p := GodelQ.CG008ITSet4.iTSet.blueprint) ![v 0, v 3, v 1, v 2]

instance iTSet.definable : 𝚺ᴬ₁-Function₃[V] iTSet := iTSet.defined.to_definable

instance iTSet.definable' (Γ k) : Γᴬ_[k + 1]-Function₃[V] iTSet :=
  iTSet.definable.of_sigmaOne

end GodelQ.CG008ITSet6

#print axioms GodelQ.CG008ITSet6.iTSet.defined
