import GodelQ.ZFC.CG008FinalAnalysis

/-!
# CG-008 · 内部化 `iT_quote` 的可行性核对

## 目标

`iT_quote`（`InternalTranslate.lean:611`）是**逐 φ 的元层定理**：

```lean
theorem iT_quote : ∀ {n : ℕ} (φ : Semisentence ℒₒᵣ n),
    iT (n : V) ⌜φ⌝ = ⌜(arithTrln.translate φ : Semisentence ℒₛₑₜ n)⌝
```

**它是元层归纳**（对 `φ` 的语法结构）。

缺口要的是 **V 内部**的版本：**对任意 `x : V`**（一个码），
`iT 0 x` 与「`x` 若是一个算术句的码，则 `iT 0 x` 是它的翻译的码」的关系。

## 关键观察：`iT` 是 **Σ₁ 函数**

`iT.blueprint : UformulaRec1.Blueprint`（`InternalTranslate.lean:217`）——
它是**不动点定义**的**递归函数**，吃 `V` 吐 `V`。

**所以 `iT` 本身在 V 内是函数**——不需要「内部化」它。
**要内部化的是 `iT_quote` 这个定理**：即 V 内证明
「`iT` 在**句子码**上与 `translate` 一致」。

## 本探针要查实

1. `iT` 在 V 内是（Σ₁ 可定义）函数；
2. `iT_quote` 的**元层**版本可用于**标准** `φ`；
3. V 内版本要处理**非标准** `x`——**这正是落差**。

**第 3 条是本轮要点**：`iT_quote` 的前提是**元层的** `φ : Semisentence ℒₒᵣ n`；
V 内的 `x` 可以是**非标准码**（不对应任何元层 φ）。
**所以 `iT_quote` 的内部化不是「把定理搬进去」，而是「对非标准码也成立」**——
而后者**可能为假**（非标准码可能不对应任何公式）。

## 因此

**`iT_quote` 的内部化方向要选对**：
不是「`iT 0 x` = 翻译」，而是
「**若** `x` 是一个算术句的码，**则** `iT 0 x` 是它翻译的码」——
条件形式，前提用 V 内可表达的「`x` 是句子码」（`IsUFormula`/`IsSemiformula`）。

**而 Foundation 有** `IsUFormula`、`IsSemiformula`（V 内谓词）——
所以这个条件形式**可陈述**。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进入收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008ITQuote

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.CG008HBL3
  GodelQ.CG008HBL3Test GodelQ.CG008Final GodelQ.CG008Probe15 GodelQ.CG008Probe16
  GodelQ.CG008Probe17 GodelQ.CG008Probe18 GodelQ.CG008Probe19 GodelQ.CG008Probe20
  GodelQ.CG008Delta1Wall GodelQ.CG008Probe21 GodelQ.CG008CrossLanguage
  GodelQ.CG008InterpretationWall GodelQ.CG008Probe22 GodelQ.CG008Probe23
  GodelQ.CG008CraigRoute GodelQ.CG008CraigBridge GodelQ.CG008PureArith
  GodelQ.CG008Probe24 GodelQ.CG008Probe25 GodelQ.CG008Correction
  GodelQ.CG008Rosser GodelQ.CG008InternalInduction GodelQ.CG008SingleD3
  GodelQ.CG008SingleD3Attack GodelQ.CG008BridgeAnatomy GodelQ.CG008SingleD3Theorem
  GodelQ.CG008ConRedo GodelQ.CG008MonoExt GodelQ.CG008RedoPrereq GodelQ.CG008RedoActual
  GodelQ.CG008AbstractRedo GodelQ.CG008Instantiate GodelQ.CG008Z0FromSingleD3
  GodelQ.CG008D3AtG GodelQ.CG008CodeFunctions GodelQ.CG008DerivationTransform
  GodelQ.CG008OfSs GodelQ.CG008FinalAnalysis

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1**：`iT` 在 V 内是函数（吃 `V` 吐 `V`）——**不需要内部化**。 -/
noncomputable example (n x : V) : V := iT n x

/-- **查实 2**：`iT_quote` 的元层版本——对**标准**的 `φ` 成立。 -/
example {n : ℕ} (φ : Semisentence ℒₒᵣ n) :
    iT (n : V) ⌜φ⌝ = ⌜(arithTrln.translate φ : Semisentence ℒₛₑₜ n)⌝ :=
  iT_quote (V := V) φ

/-- **查实 3（本轮要点）**：V 内要的是**条件形式**——
「**若** `x` 是算术句的码，**则** `iT 0 x` 是它翻译的码」。

**前提用 V 内可表达的 `IsUFormula`**（Foundation 有）。
**这个条件形式可陈述**——本行把它固定下来。

**注意 `iT_quote` 的直接内部化不成立**：V 内的 `x` 可以是**非标准码**，
不对应任何元层 `φ`。 -/
example : Prop :=
  ∀ x : V, Bootstrapping.IsUFormula ℒₒᵣ x → Bootstrapping.IsUFormula ℒₛₑₜ (iT 0 x)

/-! ## 关键工具：`ISigma1.sigma1_succ_induction` 是 **V 内部**的公式归纳

读到的（`Syntax/Formula/Basic.lean:443`）：

```lean
lemma ISigma1.sigma1_succ_induction {P : V → Prop} (hP : 𝚺ᴬ₁-Predicate P)
    (hrel : ∀ k r v, L.IsRel k r → IsUTermVec L k v → P (^rel k r v))
    ... (hall : ∀ p, IsUFormula L p → P p → P (^∀ p)) ... :
    ∀ p, IsUFormula L p → P p
```

**注意结论**：`∀ p, IsUFormula L p → P p`——**`p` 是 `V` 的元素**，
**前提用 V 内的 `IsUFormula`**。**这正是「条件形式」所需的归纳原理。**

**所以 `iT_quote` 的条件内部化是可行的**：
取 `P p := iT 0 p = ⌜translate⌝` 之类，由 `sigma1_succ_induction` 逐结构验证。
**但 `P` 要满足 `𝚺ᴬ₁-Predicate`**——这是本探针的待查项。 -/

/-- **查实 4（关键工具）**：`sigma1_succ_induction` 是 **V 内部**的公式归纳，
其结论是 `∀ p, IsUFormula L p → P p`（`p : V`，前提用 V 内的 `IsUFormula`）。

**这正是「条件形式」所需的归纳原理。**
（本行只以注释记录其类型；实例化需要逐条给出八个情形，
那是本文件之后的实际工作。） -/
example : True := trivial

end GodelQ.CG008ITQuote
