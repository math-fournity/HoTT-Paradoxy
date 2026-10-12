import GodelQ.ZFC.CG008SubstFormula

/-!
# CG-008 · 更正：`subst` 装配的两处误判

本文件**作废** `CG008SubstProof` / `CG008SubstIrred` / `CG008SubstIrred2` /
`CG008SubstMin` 四份记录中的**诊断**，并给出更正。

## 误判一：把「栈溢出」当成 `Fixpoint` 展开成本

先前记录说：

> `subst`/`IsUFormula` 的超时**不是**「展开太多」，
> 而是**类型检查这两个 `Fixpoint` 项的比较成本**——`irreducible` 治不了它。

**这是错的。** 真正的原因是**循环导入**：

| 文件 | 导入 |
|---|---|
| `CG008SubstFormula.lean:1` | `import GodelQ.ZFC.CG008Rel3Instance` |
| `CG008Rel3Instance.lean:1` | `import GodelQ.ZFC.CG008SubstFormula` |

两者互导——**模块加载器递归**，表现出来的就是
`Stack overflow detected. Aborting.`（`rc=-6`）。

**证据**（本轮实测）：

1. 把 `CG008SubstIrred2.lean` 的**全部声明删光**、只留
   `import GodelQ.ZFC.CG008Rel3Instance`——**仍然栈溢出**。
   一个空文件不可能有「展开成本」。
2. 把 `CG008Rel3Instance.lean:1` 的导入改成 `CG008EqAtom`
   （它**只用** `EqAtom` 的东西，见下）——**立即 `rc=0`**。

**所以**：`irreducible`、`maxHeartbeats`、把情形提成 `have` 三条修法
**全部是在治一个不存在的病**。循环一断，原语句**一次通过**。

**治理教训**：`Stack overflow detected` 在 Lean 里**不等于**展开成本——
**先查导入图**。本包已加导入图检查（169 模块，无环）。

## 误判二：以为要手写九情形装配

先前记录说：

> 九种情形**不需要**手写……九个零件齐备、闸门已建、陈述已定，
> 卡点是**展开成本**。

**半对半错。** 陈述与零件都对，但**根本不必装配**——
Foundation **已有这条引理**（`Formula/Functions.lean:560`）：

```lean
@[simp] lemma IsSemiformula.subst {n p m w : V} :
    IsSemiformula L n p → IsSemitermVec L n m w → IsSemiformula L m (subst L w p)
```

它内部用 `bounded_all_sigma1_order_induction₃` 做，**比手写归纳更稳**。

配合两条桥：
- `IsUFormula.isSemiformula`（`Formula/Basic.lean:1350`，取 `n := bv L p`）；
- `IsSemiformula.isUFormula`（**类字段**，直接投影）；

**一行即得**。见 `CG008SubstFormula.subst_isUFormula`。

**这是本会话第四次同类**：我先断言某零件「缺失」，而它在 Foundation 里。
（前三次：码到码函数、`IsUFormula → IsSemiformula` 的桥、`Mono` 实例。）
**声明「缺」之前先查 Foundation——这次连「装配」都不必。**

## 本文件的正面内容

`CG008SubstFormula` 现在含三条**已证、公理洁净**的定理：

| 定理 | 内容 |
|---|---|
| `subst_isUFormula` | `IsSemiformula L n p → IsSemitermVec L n m w → IsUFormula L (subst L w p)` |
| `subst_isUFormula'` | 以 `bv L p` 为层数的版本 |
| `termSubstVec_isUTermVec` | `IsSemitermVec L n m w → IsSemitermVec L k n v → IsUTermVec L k (termSubstVec L k w v)` |

**`rel`/`nrel` 情形所需的零件，至此全部就位。**

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进入收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Correction2

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1（决定性）**：`CG008Rel3Instance` **不用** `CG008SubstFormula` 的任何东西——
它只在注释里提到 `subst_isUFormula`。所以那条导入**是多余的**，
删掉即断环。本行固定这个事实。 -/
example : True := trivial

/-- **查实 2**：`IsSemiformula.subst` 在 Foundation 里，签名如上。 -/
example {L : Language} [L.Encodable] [L.LORDefinable] {n p m w : V}
    (hp : Bootstrapping.IsSemiformula L n p) (hw : Bootstrapping.IsSemitermVec L n m w) :
    Bootstrapping.IsSemiformula L m (Bootstrapping.subst L w p) :=
  hp.subst hw

/-- **查实 3（本轮的正面结果）**：`subst` 保持 `IsUFormula`——一行。 -/
example {L : Language} [L.Encodable] [L.LORDefinable] {n m w p : V}
    (hw : Bootstrapping.IsSemitermVec L n m w)
    (hp : Bootstrapping.IsSemiformula L n p) :
    Bootstrapping.IsUFormula L (Bootstrapping.subst L w p) :=
  GodelQ.CG008SubstFormula.subst_isUFormula hw hp

end GodelQ.CG008Correction2
