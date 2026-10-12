import GodelQ.ZFC.CG008LvlLemma

/-!
# CG-008 · **重大发现**：Foundation 有**层数感知**的公式归纳

## 读到的（`Formula/Basic.lean:1484`）

```lean
lemma IsSemiformula.sigma1_structural_induction {P : V → V → Prop} (hP : 𝚺ᴬ₁-Relation P)
    (hrel : ∀ n k r v, L.IsRel k r → IsSemitermVec L k n v → P n (^rel k r v))
    ...
    (hall : ∀ n p, IsSemiformula L (n + 1) p → P (n + 1) p → P n (^∀ p))
    (hexs : ∀ n p, IsSemiformula L (n + 1) p → P (n + 1) p → P n (^∃ p)) {n p} :
    IsSemiformula L n p → P n p
```

**关键**：谓词 `P : V → V → Prop` **吃层数**！
`hall` 的形式是 `P (n+1) p → P n (^∀ p)`——
**归纳假设在层 `n+1`，结论在层 `n`**。

**这正是 `iT_quote` 内部化所需的**：`iT_all` 给出 `iT (n+1) p`，
而这条归纳**允许**在层 `n+1` 上假设！

## 这解决了 `CG008ITQuoteProof` 的层数障碍

之前用的 `sigma1_succ_induction` 的 `P : V → Prop` **不吃层数**，
所以 `all` 情形的 `n+1` 无法覆盖。

**换成 `sigma1_structural_induction`**（`P : V → V → Prop`）即可。

**代价**：`hP : 𝚺ᴬ₁-Relation P`——**二元**关系的 Σ₁ 可定义性
（比一元谓词要求高，需重新查）。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进入收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008LvlInduction

open GodelQ.Translate (iT iTR)

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1（本轮要点）**：`sigma1_structural_induction` 是**层数感知**的——
`P : V → V → Prop`，且 `hall : ∀ n p, IsSemiformula L (n+1) p → P (n+1) p → P n (^∀ p)`。

**这就是解决 `iT_all` 层数问题所需的形状。** -/
example : True := trivial

/-- **查实 2（新的靶子）**：二元关系 `P n p := IsUFormula ℒₛₑₜ (iT n p)`
是否 Σ₁ 可定义——这是用 `sigma1_structural_induction` 的**新闸门**。

**注意**：`P` 现在吃 `n` 与 `p` 两个参数，所以要求 `𝚺ᴬ₁-Relation P`（二元）。
**这比一元的 `𝚺ᴬ₁-Predicate` 要求高**——但 `iT` 是二元 Σ₁ 函数（`iTDef` 是三元句，
吃 `n` 与 `p`），所以**可能仍然可定义**。 -/
example : 𝚺ᴬ₁-Relation (fun n p : V ↦ Bootstrapping.IsUFormula ℒₛₑₜ (iT n p)) := by
  definability

/-! ## 试证的结果：**两处新的技术障碍**

**试证 `∀ p, IsUFormula ℒₒᵣ p → ∀ n : V, IsUFormula ℒₛₑₜ (iT n p)`，
用 `sigma1_structural_induction`。实测两处障碍：**

### 障碍 1：归纳的**前提**用 `IsSemiformula`（带层数），不是 `IsUFormula`

`sigma1_structural_induction` 的结论是

```lean
{n p} : IsSemiformula L n p → P n p
```

**不是** `IsUFormula L p → P n p`。
**所以**：手头有 `IsUFormula ℒₒᵣ p`（不带层数），
而归纳要 `IsSemiformula ℒₒᵣ n p`（**带**层数）。

**这需要一条桥**：`IsUFormula p ↔ ∃ n, IsSemiformula n p`，
或 `IsUFormula p → IsSemiformula n p`（对某 `n`）。
**Foundation 是否提供这条桥，是新的待查项。**

### 障碍 2：`definability` 在 `intro` 后的位置失败

`(by definability)` 在 `intro p hp` 之后、作为**第八个参数**时失败
（`aesop` 穷尽搜索未果），而**独立一行** `example : 𝚺ᴬ₁-Relation ... := by definability`
**通过**（本文件查实 2）。

**说明**：`definability` 的成功与否**依赖目标的具体形状**，
在参数位置可能因元变量未解而失败。
**修法**：把它提为**独立的 `have`**，再传入。

## 结论

**层数感知归纳是对的**（形状匹配），
**但用它还需要一条 `IsUFormula → IsSemiformula` 的桥**——
这是**新的待查项**，也是下一步的具体靶子。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进入收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008LvlInduction

open GodelQ.Translate (iT iTR)

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1（本轮要点）**：`sigma1_structural_induction` 是**层数感知**的——
`P : V → V → Prop`，且 `hall : ∀ n p, IsSemiformula L (n+1) p → P (n+1) p → P n (^∀ p)`。

**形状与 `iT_all` 的层数问题匹配。** -/
example : True := trivial

/-- **查实 2（闸门已过）**：二元关系 `P n p := IsUFormula ℒₛₑₜ (iT n p)` **Σ₁ 可定义**。 -/
example : 𝚺ᴬ₁-Relation (fun n p : V ↦ Bootstrapping.IsUFormula ℒₛₑₜ (iT n p)) := by
  definability

/-- **查实 3（障碍 1）**：归纳的**前提**是 `IsSemiformula L n p`（**带层数**），
不是 `IsUFormula L p`（**不带**）。

**所以需要一条桥**：由 `IsUFormula p` 得 `IsSemiformula n p`（对某个 `n`）。

**本行把这条桥固定为下一步的靶子**（Foundation 是否已提供待查）。 -/
example : Prop := ∀ p : V, Bootstrapping.IsUFormula ℒₒᵣ p →
    ∃ n : V, Bootstrapping.IsSemiformula ℒₒᵣ n p

end GodelQ.CG008LvlInduction
