import GodelQ.ZFC.CG008SubstMin

/-!
# CG-008 · `subst` 保持公式性——**Foundation 已有**，先前「卡在装配」的记录作废

## 本轮决定性的发现

`Formula/Functions.lean:561`：

```lean
@[simp] lemma IsSemiformula.subst {n p m w : V}
    (hp : IsSemiformula L n p) (hw : IsSemitermVec L n m w) :
    IsSemiformula L m (subst L w p)
```

**这正是我前两轮试图从零搭的引理**——`CG008SubstFormula.lean` 记的
「第 9 个零件需求：`termSubstVec` 保持 `IsUTermVec`、`rel` 情形需 `hlev`」
**全是多余的**：Foundation 用 `bounded_all_sigma1_order_induction₃` + `IsSemiformula.case_iff`
一次性做完九种情形，`rel` 情形的层数是 `hw : IsSemitermVec L n m w`
**直接给出的**（`hw.termSubstVec hv` 已含所需前提）。

**教训（本会话第四次同类）**：我在没有通读 `Syntax/Formula/Functions.lean` 的情况下
假设「引理不存在、要自己归纳」。**查「Foundation 有没有」必须查定义所在文件的全部 `lemma`，
不是只 grep 名字。**

## 从 `IsSemiformula` 降到 `IsUFormula`

`IsUFormula L p ↔ ∃ n, IsSemiformula L n p`（`IsSemiformula.iff_uFormula`）。
⇒ 要的结果是 `IsSemiformula L (m') (subst L w p)`，而 `IsSemiformula.subst` 给的是
`IsSemiformula L m (subst L w p)`，其中 `m` 来自 `hw : IsSemitermVec L n m w`。

**所以只需 `IsSemitermVec L n m w`**——即 `w` 是长度 `n` 的项向量，
且所有分量的约束变元 ≤ n。这正是上一轮 `termSubstVec_isUTermVec` 里
白手起家的那个前提，**现在由 `hw` 统一给出**。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008SubstNine

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
variable {L : Language} [L.Encodable] [L.LORDefinable]

/-- **查实 1**：`IsSemiformula.subst` 的类型——就是本文件要证的。 -/
example {n p m w : V} (hp : Bootstrapping.IsSemiformula L n p)
    (hw : Bootstrapping.IsSemitermVec L n m w) :
    Bootstrapping.IsSemiformula L m (Bootstrapping.subst L w p) :=
  Bootstrapping.IsSemiformula.subst hp hw

/-- **查实 2**：`IsUFormula ↔ IsSemiformula` 的桥（**不是** `∃` 形式，而是 `bv ≤ n`）。 -/
example {n p : V} :
    Bootstrapping.IsSemiformula L n p ↔ Bootstrapping.IsUFormula L p ∧ Bootstrapping.bv L p ≤ n :=
  Bootstrapping.isSemiformula_iff

/-- **主结果**：`subst` 保持 `IsUFormula`。

**取 `n := bv L p`**（`IsUFormula.isSemiformula` 给的最小层），
于是 `hw : IsSemitermVec L (bv L p) m w`——即 `w` 的分量的约束变元 ≤ `bv L p`。 -/
theorem subst_isUFormula {m w p : V}
    (hw : Bootstrapping.IsSemitermVec L (Bootstrapping.bv L p) m w) :
    Bootstrapping.IsUFormula L p →
    Bootstrapping.IsUFormula L (Bootstrapping.subst L w p) := by
  intro hp
  have hs := Bootstrapping.IsUFormula.isSemiformula (L := L) hp
  have hsub := Bootstrapping.IsSemiformula.subst (L := L) hs hw
  exact (Bootstrapping.isSemiformula_iff.mp hsub).1

end GodelQ.CG008SubstNine
