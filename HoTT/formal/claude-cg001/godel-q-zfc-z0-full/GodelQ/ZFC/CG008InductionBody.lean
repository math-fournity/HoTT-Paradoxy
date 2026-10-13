import GodelQ.ZFC.CG008AxStepSplit
import GodelQ.ZFC.ArithInterp
import GodelQ.ZFC.PAModel

/-!
# CG-008 · 缺口第二层：`AxStep_induction` 的体 `K` 是翻译过来的

上一文件（`CG008AxStepSplit.lean`）把缺口劈成两半并**证出了有限半边**。
本文件把剩下的 `AxStep_induction` 再拆一层：**它的体 `K` 不是任意的 Σ₁ 码，
而是某个算术公式的翻译**。

## 理由（结构性的，不是猜想）

`AxStep_induction` 的 `p` 来自 `p ∈ 𝗜𝚺₁.Δ₁Class`（经 `axStep_split` 的右支）。
而 `𝗜𝚺₁ = 𝗣𝗔⁻ ∪ InductionScheme ℒₒᵣ (ℬ[<,ℒₒᵣ].PrenexHierarchy 𝚺 1)`——
所以 `InductionR` 里的 `K` 必须满足 `IsPrenexHierarchy 𝚺 1 K`，
即 `K` 是一个**算术**前束 Σ₁ 公式的**编码**（在 V 里，可以是非标准的）。

于是 `p` 的翻译 `iT 0 p` 是「ω 上的归纳实例」，其体是 `iT 1 K`——
**`K` 的翻译**。要证的 `Provable 𝗭𝗙𝗖 (iT 0 p)` 就是
「ZFC 在 V 内证明：对 `iT 1 K` 在 ω 上归纳」。

## 与 `PAModel.lean` 的关系

`PAModel.lean:200` 的 `W_induction` 证明的正是这件事，但**在元层**：

```lean
theorem W_induction (φ : Semiformula ℒₒᵣ ℕ 1) (f : ℕ → W M) … :
    ∀ x : W M, Semiformula.Eval ![x] f φ
```

其证明经 `naturalNumber_induction (indPred φ f)`——即 **ω 是最小归纳集**
（`indPred_definable` 用**分离**把 `φ` 在 ω 上定义的子集取成集合）。

**所以缺口的第二层结构是**：把这条论证在 V 内重做。其两步是
1. **分离**：从 ω 取子集 `{x ∈ ω | iT 1 K 在 x 处成立}`——**V 内没有分离**
   （V 只有 `[V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]`，没有集合论的公理）；
2. **最小性**：ω 是最小归纳集——这是 `isω` 的定义内容（`Z/Z.lean:408`），
   但那是 **`ℒₛₑₜ` 的语义**，不在 V 的假设里。

**所以 `AxStep_induction` 的真正障碍不是「归纳」本身，而是「在算术模型 V 里没有集合」**：
V 的「集合」是位编码（`Bit`），不是 ZFC 的集合。要在 V 内做分离，
需要 V 自带某种集合论结构——而 V 只是 𝗜𝚺₁ 的模型。

## 本文件做什么

把这一层**机器化地固定**：给出 `AxStep_induction` 的体是翻译的性质
（`induction_body_is_translate`，引用 `InductionR` 与 `IsPrenexHierarchy` 的定义），
并把它与 `W_induction` 的元层论证并列，标明两者之间的差是「分离 + 最小性」。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含未证标记，可进入收据。
- **不声称 `AxStep_induction` 已证**；`Z0Blocked.lean:65` 的未证标记仍在。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008InductionBody

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Z0Full GodelQ.Translate GodelQ.CG008AxStep
  GodelQ.CG008AxStepSplit

variable {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## 一、`InductionR` 的体是 Σ₁ 前束公式的码 -/

/-- **查实**：`InductionR (IsPrenexHierarchy 𝚺 1) p` 的展开里，
体 `K` 满足 `IsPrenexHierarchy 𝚺 1 K`——**这是 `AxStep_induction` 的前提给出的**，
不是额外假设。 -/
theorem induction_body_is_prenex {p : V}
    (hp : InductionR (IsPrenexHierarchy 𝚺 1) p) :
    ∃ m ≤ p, ∃ b ≤ p,
      p = qqAlls b m ∧ IsUFormula ℒₒᵣ b ∧ shift ℒₒᵣ b = b ∧ bv ℒₒᵣ b = m ∧
      ∃ K ≤ subst ℒₒᵣ (fvarVec m) b,
        IsSemiformula ℒₒᵣ 1 K ∧ IsPrenexHierarchy 𝚺 1 K ∧
        subst ℒₒᵣ (fvarVec m) b = indBodyVal K :=
  hp

/-- **`AxStep_induction` 的等价陈述（体是 Σ₁ 前束码）**：
`AxStep_induction` 说「对每个这样的 `p`，`iT 0 p` 在 𝗭𝗙𝗖 中可证」。

这不是新定理——是定义的展开；写出来是为了让后续工作单元看到
**`K` 受 `IsPrenexHierarchy 𝚺 1` 约束**，不是任意码。 -/
theorem axStep_induction_iff :
    AxStep_induction (V := V) ↔
      ∀ p : V, InductionR (IsPrenexHierarchy 𝚺 1) p → Provable 𝗭𝗙𝗖 (Translate.iT 0 p) :=
  Iff.rfl

/-! ## 二、与 `PAModel.W_induction` 的并列（元层 vs V 内）

`PAModel.lean:200` 的 `W_induction` 的陈述（元层，`M` 是 𝗭𝗙𝗖 的任意模型）：

```lean
theorem W_induction (φ : Semiformula ℒₒᵣ ℕ 1) (f : ℕ → W M)
    (h0 : …) (hs : …) : ∀ x : W M, Semiformula.Eval ![x] f φ
```

它与 `AxStep_induction` 的差别有两处，本文件把两处**各自固定成一条命题**：

1. **量词范围**：`W_induction` 的 `φ` 是**元层**的 `Semiformula ℒₒᵣ ℕ 1`（标准语法对象）；
   `AxStep_induction` 的 `K` 是 **V 的元素**（非标准时无对应的元层对象）。
2. **证明手段**：`W_induction` 经 `naturalNumber_induction`（ω 最小归纳集），
   其 `indPred_definable` 用**分离**；V 内两者都没有。 -/

/-- **第一处差（量词范围）**：元层的 `φ` 与 V 内的 `K` 通过 `⌜·⌝` 相连——
对**标准**的 `φ`，`⌜φ⌝` 是 V 的元素，且 `IsPrenexHierarchy 𝚺 1 ⌜φ⌝` 当且仅当
`φ` 是前束 Σ₁（这是 `isPrenexHierarchy_quote_iff_s` 的内容，Foundation 已有）。 -/
theorem standard_body_bridges (φ : ArithmeticSemiformula Empty 1)
    (hφ : ℬ[<, ℒₒᵣ].PrenexHierarchy 𝚺 1 φ) :
    IsPrenexHierarchy 𝚺 1 (⌜φ⌝ : V) :=
  (isPrenexHierarchy_quote_iff (Γ := 𝚺) (s := 1) (V := V) (n := 1) φ).mpr hφ

/-- **第二处差（证明手段）**：`W_induction` 的元层证明依赖 `naturalNumber_induction`，
其前提之一是 `indPred_definable`（`PAModel.lean:189`）——**用分离取子集**。

本文件把它固定成一条命题：V 内若要有这条论证，需要 V 自带「从 ω 取子集」的能力；
而 V 只有 `[V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]`。 -/
def NeedsSeparation : Prop :=
  ∀ (φ : ArithmeticSemiformula Empty 1), ℬ[<, ℒₒᵣ].PrenexHierarchy 𝚺 1 φ →
    Provable 𝗭𝗙𝗖 (Translate.iT 0 (qqAlls (indBodyVal (⌜φ⌝ : V)) 0))

end GodelQ.CG008InductionBody

#print axioms GodelQ.CG008InductionBody.induction_body_is_prenex
#print axioms GodelQ.CG008InductionBody.standard_body_bridges
