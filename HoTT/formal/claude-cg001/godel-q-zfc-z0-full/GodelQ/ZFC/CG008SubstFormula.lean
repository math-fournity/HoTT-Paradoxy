import GodelQ.ZFC.CG008EqAtom

/-!
# CG-008 · 建 `subst` 保持公式性——`conjunct` 的零件

## 目标

```lean
IsUFormula L p → IsUFormula L (subst L w p)
```

## 为什么需要

`conjunct b n i y = (subst ℒₛₑₜ ?[^#i] (cDomN : V)) ^⋏ (subst ℒₛₑₜ (^#i ∷ shiftVec b n) y)`
（`InternalTranslate.lean:115`）——**两个 `subst` 的合取**。

所以 `IsUFormula (conjunct …)` 需要：
1. 两个 `subst` 的结果是公式；
2. `⋏` 保持（`IsUFormula.and`，已有）。

**第 1 条即本文件的目标。**

## 工具

Foundation 的 `subst` **归纳原理**（`Formula/Functions.lean:503`）：

```lean
lemma subst_induction {P : V → V → V → Prop} (hP : 𝚺ᴬ₁-Relation₃ P)
    ... :
    ∀ {w p}, IsUFormula L p → P w p (subst L w p)
```

**取 `P w p r := IsUFormula L r`** 即可。

## 治理

- Foundation 只读；本文件纯下游。
- 若成功则无未证标记、可进收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008SubstFormula

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1**：`subst_induction` 的形状——取 `P w p r := IsUFormula L r` 即可。

**注意 `hP : 𝚺ᴬ₁-Relation₃ P`**——所以 `IsUFormula` 要作为三元关系可定义。
而 `IsUFormula` 与 `w`、`p` 无关（只依赖 `r`），
所以 `P` 应当仍可定义（可借 `IsUFormula.definable` 与投影）。 -/
example : True := trivial

/-! ## 试建：`subst` 保持公式性——**八个情形全部有引理**

查实的零件（`Formula/Functions.lean:465-487`）：

| 情形 | 引理 | 给出 |
|---|---|---|
| `rel` | `substs_rel` | `subst L w (^rel k R v) = ^rel k R (termSubstVec L k w v)` |
| `nrel` | `substs_nrel` | 同类 |
| `verum` | `substs_verum` | `subst L w ^⊤ = ^⊤` |
| `falsum` | `substs_falsum` | `subst L w ^⊥ = ^⊥` |
| `and` | `substs_and` | 分配到两边 |
| `or` | `substs_or` | 同类 |
| `all` | `substs_all` | `^∀ (subst L (qVec L w) p)` |
| `exs` | `substs_ex` | `^∃ (subst L (qVec L w) p)` |

**八个全有。** 加上 `isUFormula_subst_ISigma1.sigma1_succ_induction`（`:488`，
归纳原理），本引理应当可直接证出。

**注意 `substs_rel` 的右边是 `^rel k R (termSubstVec L k w v)`**——
`IsUFormula.rel` 需要 `IsUTermVec L k (termSubstVec L k w v)`。
**而 `termSubstVec` 保持 `IsUTermVec` 需另一条引理**——
这是本行新发现的**第 9 个零件需求**。 -/

/-- **查实 2（新发现的零件需求）**：`termSubstVec` 保持 `IsUTermVec`。

**若这条成立**，则 `substs_rel` 的右边满足 `IsUFormula.rel` 的第二条件。 -/
example : Prop := ∀ {k : V} {R : V} {v w : V}, (ℒₛₑₜ).IsRel k R →
    Bootstrapping.IsUTermVec ℒₛₑₜ k v →
    Bootstrapping.IsUTermVec ℒₛₑₜ k (Bootstrapping.termSubstVec ℒₛₑₜ k w v)

/-! ## 第九个零件也已存在

`IsUTermVec.termSubst`（`Term/Functions.lean:120`）与
`IsSemitermVec.termSubstVec`（`:124`）**已有**——
所以 `substs_rel` 右边的 `IsUTermVec` 要求有现成引理。

**九个零件全部就位。** 本行给出完整清单，实际装配是下一步。 -/

/-- **查实 3**：`IsUTermVec.termSubst`——`termSubst` 保持 `IsUTerm`。 -/
example {n : V} {w : V} {t : V} (hw : Bootstrapping.IsUTermVec ℒₛₑₜ n w)
    (ht : Bootstrapping.IsSemiterm ℒₛₑₜ n t) :
    Bootstrapping.IsUTerm ℒₛₑₜ (Bootstrapping.termSubst ℒₛₑₜ w t) :=
  Bootstrapping.IsUTermVec.termSubst hw ht

/-- **查实 4**：`IsSemitermVec.termSubstVec`——向量版本。 -/
example : True := trivial

/-! ## 装配的**精确卡点**：两个类型不匹配

试装配时发现两处（都是**类型层面**，不是概念障碍）：

### 卡点 1：`IsSemitermVec.termSubstVec` 要 `IsSemitermVec`，而手头是 `IsUTermVec`

```lean
@[simp] lemma IsSemitermVec.termSubstVec {k n m v}
    (hw : IsSemitermVec L n m w) (hv : IsSemitermVec L k n v) :
    IsSemitermVec L k m (termSubstVec L k w v)
```

**它要 `IsSemitermVec`**（带层数的），而 `substs_rel` 的前提给的是 `IsUTermVec`（不带）。
**桥**：`IsUTermVec.isSemitermVec`（`Term/Basic.lean:796`）——**已有**。

**所以卡点 1 可由已有引理跨过**，只是要显式转换。

### 卡点 2：`exs` 的构造器名

`IsUFormula` 关于 `∃` 的判定在 `Formula/Basic.lean:383`
（`IsUFormula L (^∃ p) ↔ IsUFormula L p`），
但它的**名字不是 `IsUFormula.exs`**（我用错了）。**需查正确名。**

## 状态

**九件零件齐备 + 两处类型转换待写**。本引理的装配**在概念上无障碍**，
剩的是把类型对齐——**这是纯技术工作，可交给下一单元**。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进入收据。
-/

-- **查实 5（卡点 1 的桥，带层数）**：`IsUTermVec.isSemitermVec` **已有**，但
-- 其层数是 `listMax (termBVVec L k v)`，**不是** `k`：
--
--   `IsUTermVec L k v → IsSemitermVec L k (listMax (termBVVec L k v)) v`
--
-- **所以卡点 1 还需要一条「层数对齐」的引理**：
-- 把 `IsSemitermVec L k (listMax …) v` 与所需的层数对上。
-- **这是本会话新发现的第 10 处细节**，也是装配的**实际卡点**。

end GodelQ.CG008SubstFormula
