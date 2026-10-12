import GodelQ.ZFC.CG008Rel3Instance

/-!
# CG-008 · 最小化试：`termSubstVec` 保持 `IsUTermVec`

## 层数要点（本轮查实，纠正了先前的误解）

`Term/Basic.lean` 的定义是：

```lean
abbrev IsTermVec (k v : V) : Prop := IsSemitermVec L k 0 v

lemma IsSemitermVec.def {v : V} :
    IsSemitermVec L k n v ↔ IsUTermVec L k v ∧ ∀ i < k, termBV L v.[i] ≤ n
```

**所以 `n` 不是「层数」，只是「约束变元上界」。**
`IsUTermVec L k v` 只要求「长度是 `k`、每个分量是项」。

`Term/Functions.lean:124`：

```lean
@[simp] lemma IsSemitermVec.termSubstVec {k n m v}
    (hw : IsSemitermVec L n m w) (hv : IsSemitermVec L k n v) :
    IsSemitermVec L k m (termSubstVec L k w v)
```

**`n` 身兼二职**：既是 `w` 的**长度**，又是 `v` 的**约束变元上界**。
这正是代换的语义——`termSubstVec L k w v` 把 `v` 的第 `i` 个约束变元换成
`w.[i]`，所以 `w` 必须**足够长**（长度 ≥ `v` 的最大约束变元）。

⇒ 定理的形式必须带一条「`w` 够长」的前提：
`listMax (termBVVec L k v) ≤ n`。

（先前版本把 `n₀` 与 `n` 写成互相独立的两个变量，
于是 `termSubstVec` 报类型不匹配——**那不是工程问题，是这个引理的固有形状**。）
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008SubstMin

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

section
variable {L : Language} [L.Encodable] [L.LORDefinable]

/-- **查实 1**：`IsSemitermVec.def`——`n` 只是约束变元上界。 -/
example {k n v : V} :
    Bootstrapping.IsSemitermVec L k n v ↔
      Bootstrapping.IsUTermVec L k v ∧ ∀ i < k, Bootstrapping.termBV L v.[i] ≤ n :=
  Bootstrapping.IsSemitermVec.def

set_option maxHeartbeats 800000 in
/-- **主结果**：`termSubstVec` 保持 `IsUTermVec`。

**前提 `hlev` 是必需的、且形状正确**：`w` 的长度必须覆盖 `v` 的约束变元。 -/
theorem termSubstVec_isUTermVec {n k w v : V}
    (hw : Bootstrapping.IsUTermVec L n w) (hv : Bootstrapping.IsUTermVec L k v)
    (hlev : listMax (Bootstrapping.termBVVec L k v) ≤ n) :
    Bootstrapping.IsUTermVec L k (Bootstrapping.termSubstVec L k w v) := by
  have hwS : Bootstrapping.IsSemitermVec L n (listMax (Bootstrapping.termBVVec L n w)) w :=
    hw.isSemitermVec
  have hvS : Bootstrapping.IsSemitermVec L k n v := by
    refine Bootstrapping.IsSemitermVec.def.mpr ⟨hv, fun i hi ↦ ?_⟩
    have hth := Bootstrapping.nth_termBVVec hv hi
    rw [hth.symm]
    exact le_trans (nth_le_listMax (i := i) (v := Bootstrapping.termBVVec L k v)
      (by rw [Bootstrapping.len_termBVVec hv]; exact hi)) hlev
  exact (Bootstrapping.IsSemitermVec.termSubstVec hwS hvS).isUTerm

end

end GodelQ.CG008SubstMin
