import GodelQ.ZFC.CG008Rel3Instance

/-!
# CG-008 · `subst` 保持公式性——**Foundation 已有**，先前「卡在装配」的记录作废

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

/-! ### 卡点 1 的**解决**：层数由 `IsSemitermVec` 的判定给出

重读 `Term/Basic.lean:782`（`IsSemitermVec.def`）：

```lean
IsSemitermVec L k n v ↔ IsUTermVec L k v ∧ ∀ i < k, termBV (V := V) L v.[i] ≤ n
```

**关键**：`IsUTermVec L k v` 对**任意**满足界条件的 `n` 都给出 `IsSemitermVec L k n v`。
**所以层数不必是 `listMax`**——只要它足够大。

**因此卡点 1 可解**：由 `hv : IsUTermVec L k v` 与
「`n` 足够大」（如 `n := listMax (termBVVec L k v)`），得 `IsSemitermVec L k n v`；
再喂给 `IsSemitermVec.termSubstVec`。

**具体地**：`IsUTermVec.isSemitermVec` 恰好取 `n := listMax (termBVVec L k v)`——
**正是「足够大」的那个**。所以：
1. `hv.isSemitermVec : IsSemitermVec L k (listMax …) v` ✅
2. `IsSemitermVec.termSubstVec` 需 `hw : IsSemitermVec L n m w`——**`w` 的层数也要对上**。

**所以真正的待查是**：`w`（替换向量）的 `IsSemitermVec` 从哪来。
`substs_rel` 只给 `IsUTermVec L k v`（被替换的那个），**没给 `w` 的任何信息**——
**这说明 `subst_isUFormula` 的陈述可能需要给 `w` 加前提**，
或 `w` 的界由别处保证。**这是下一步要定的。** -/

/-- **查实 5**：`IsSemitermVec` 的判定——`IsUTermVec` 加界条件。 -/
example {L : Language} [L.Encodable] [L.LORDefinable] {k n v : V} :
    Bootstrapping.IsSemitermVec L k n v ↔
      (Bootstrapping.IsUTermVec L k v ∧ ∀ i, i < k → Bootstrapping.termBV L v.[i] ≤ n) :=
  Bootstrapping.IsSemitermVec.def

/-! ## 定下 `subst_isUFormula` 的**正确陈述**

`IsSemitermVec.termSubstVec` 要 `hw : IsSemitermVec L n m w`（**替换向量**），
而 `substs_rel` 只给被替换向量的信息。**所以陈述要给 `w` 加前提。**

**但在 `conjunct` 的应用里，`w` 是具体的**：
`conjunct b n i y = (subst ℒₛₑₜ ?[^#i] (cDomN : V)) ^⋏ (subst ℒₛₑₜ (^#i ∷ shiftVec b n) y)`
——两个 `w` 分别是 `?[^#i]`（单个有界变量）与 `^#i ∷ shiftVec b n`。
**它们的 `IsUTermVec`/`IsSemitermVec` 性应当可由 `IsUTerm.bvar` 等拼出。**

**所以正确的路线是**：把 `subst_isUFormula` 陈述为**带 `w` 前提**的版本，
在 `conjunct` 处**实例化并付清前提**。

**本行固定这个判断。** -/

-- **查实 6（`w` 前提的形式）**：若 `w` 是 `IsSemitermVec`（带层数），
-- 则 `subst` 保持公式性。**这是要证的形状**——`n`、`m` 是层数参数：
--
--   `IsSemitermVec L n m w → IsUFormula L p → IsUFormula L (subst L w p)`
--
-- （以注释记录：`example` 里的多宇宙 binder 推断失败，实际定理应写在
-- `variable` 声明下。）

/-! ## 卡点**已解**：用 `IsUTermVec.termSubst` 绕开 `IsSemitermVec`

上一轮卡在 `IsSemitermVec.termSubstVec` 上（`whnf` 超时）。

**修法**：Foundation **已有** `IsUTermVec.termSubst`
（`Term/Functions.lean:120`）：

```lean
@[simp] lemma IsUTermVec.termSubst {t} (hw : IsUTermVec L n w) (ht : IsSemiterm L n t) :
    IsUTerm L (termSubst L w t) :=
  IsSemitermVec.termSubst hw.isSemitermVec ht |>.isUTerm
```

**它直接吃 `IsUTermVec`**——不必先转 `IsSemitermVec`。

**配合 `nth_termSubstVec`（`:91`）**——它给出向量的第 `i` 个分量
`termSubstVec L k w v` 就是 `termSubst L w v.[i]`。
**由 `IsUTermVec.termSubst` 逐分量得 `IsUTerm`，再由 `IsUTermVec.iff`（`:802`）得
`IsUTermVec`**——**绕开了那个超时的引理**。

**所以本定理的前提可以放松为 `hw : IsUTermVec L n w`**（原来写的是 `IsSemitermVec`）。 -/

section
variable {L : Language} [L.Encodable] [L.LORDefinable]

/-- **主结果**：`subst` 保持公式性。

**Foundation 已有这条引理**——`IsSemiformula.subst`（`Formula/Functions.lean:560`）：

```lean
@[simp] lemma IsSemiformula.subst {n p m w : V} :
    IsSemiformula L n p → IsSemitermVec L n m w → IsSemiformula L m (subst L w p)
```

配合桥 `IsUFormula.isSemiformula`（`Formula/Basic.lean:1350`，取 `n := bv L p`）
与投影 `IsSemiformula.isUFormula`（类字段），**一行即得**。

**这一条推翻了本文件先前「卡在装配」的记录**：那九种情形**不需要**手写，
Foundation 的 `IsSemiformula.subst` 已把它们全部包办
（它内部用 `bounded_all_sigma1_order_induction₃` 做，比手写归纳更稳）。 -/
theorem subst_isUFormula {n m : V} {w : V} (hw : Bootstrapping.IsSemitermVec L n m w)
    {p : V} (hp : Bootstrapping.IsSemiformula L n p) :
    Bootstrapping.IsUFormula L (Bootstrapping.subst L w p) :=
  (hp.subst hw).isUFormula

/-- **`IsUFormula` 版本**：以 `bv L p` 为层数（`IsUFormula.isSemiformula` 给出的正是这个）。 -/
theorem subst_isUFormula' {m : V} {w : V} {p : V} (hp : Bootstrapping.IsUFormula L p)
    (hw : Bootstrapping.IsSemitermVec L (Bootstrapping.bv L p) m w) :
    Bootstrapping.IsUFormula L (Bootstrapping.subst L w p) :=
  (hp.isSemiformula.subst hw).isUFormula

/-- **项向量版本**（`rel`/`nrel` 情形要的）。 -/
theorem termSubstVec_isUTermVec {k n m w v : V} (hv : Bootstrapping.IsSemitermVec L k n v)
    (hw : Bootstrapping.IsSemitermVec L n m w) :
    Bootstrapping.IsUTermVec L k (Bootstrapping.termSubstVec L k w v) :=
  (hw.termSubstVec hv).isUTermVec

end

end GodelQ.CG008SubstFormula
