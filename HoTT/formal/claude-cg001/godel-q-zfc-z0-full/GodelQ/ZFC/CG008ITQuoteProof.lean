import GodelQ.ZFC.CG008ITQuote

/-!
# CG-008 · 试证条件形式的内部 `iT_quote`

## 目标

```
∀ x : V, IsUFormula ℒₒᵣ x → IsUFormula ℒₛₑₜ (iT 0 x)
```

**工具**：`ISigma1.sigma1_succ_induction`（`Syntax/Formula/Basic.lean:443`）。

## 要给的八种情形

| 情形 | 目标 |
|---|---|
| `hrel` | `IsUFormula ℒₛₑₜ (iT 0 (^rel k r v))` |
| `hnrel` | 同类 |
| `hverum` | `IsUFormula ℒₛₑₜ (iT 0 ^⊤)` |
| `hfalsum` | 同类 |
| `hand` | `IsUFormula ℒₛₑₜ (iT 0 (p ^⋏ q))` |
| `hor` | 同类 |
| `hall` | `IsUFormula ℒₛₑₜ (iT 0 (^∀ p))` |
| `hexs` | 同类 |

## 前置障碍

`hP : 𝚺ᴬ₁-Predicate P`——**谓词必须是 Σ₁ 可定义的**。
而 `P x := IsUFormula ℒₛₑₜ (iT 0 x)` 是否 Σ₁，取决于 `iT` 与 `IsUFormula` 的层级。

**`iT` 是 `UformulaRec1.Construction.result`**——它由 `prConstruction` 给出，
是**原始递归**的，所以应当 Δ₁。`IsUFormula` 也是 Δ₁。
**所以 `P` 应当 Σ₁**——本探针先查这一点。

## 治理

- Foundation 只读；本文件纯下游。
- 若成功则无未证标记、可进收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008ITQuoteProof

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
  GodelQ.CG008OfSs GodelQ.CG008FinalAnalysis GodelQ.CG008ITQuote

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1**：`iT` 由 `iT.blueprint` 的 `result` 给出——**Σ₁ 函数**（`iTDef`）。 -/
noncomputable example : 𝚺ᴬ₁.Semisentence 3 := iTDef

/-- **查实 2**：`IsUFormula` 是可定义谓词——`iT_quote` 的各条引理都在用它。 -/
example (x : V) : Prop := Bootstrapping.IsUFormula ℒₛₑₜ x

/-- **查实 3（本轮要点）**：目标谓词 `P x := IsUFormula ℒₛₑₜ (iT 0 x)`
**是否 Σ₁ 可定义**——这是能否用 `sigma1_succ_induction` 的关键。

**待查**：需要把 `IsUFormula` 与 `iT` 的 `Definable` 实例复合起来。
本行只固定目标形状，不声称已证。 -/
example : Prop := ∀ x : V, Bootstrapping.IsUFormula ℒₒᵣ x →
    Bootstrapping.IsUFormula ℒₛₑₜ (iT 0 x)

/-! ## 试证：给 `sigma1_succ_induction` 的八种情形

**第一步：先把谓词写出来，并查它能否合成 `𝚺ᴬ₁-Predicate`。**

`P x := IsUFormula ℒₛₑₜ (iT 0 x)`——**若这行能过**，
则 `sigma1_succ_induction` 的 `hP` 前提就位。 -/

/-- **查实 4（决定性）**：目标谓词能否合成 `𝚺ᴬ₁-Predicate`。

**这是整条路的闸门**：`sigma1_succ_induction` 要 `hP : 𝚺ᴬ₁-Predicate P`。
`iT` 是 Σ₁ 函数（`iTDef`），`IsUFormula` 是可定义谓词，
**两者的复合应当是 Σ₁ 可定义**——本行让 Lean 实际去合成。 -/
example : 𝚺ᴬ₁-Predicate (fun x : V ↦ Bootstrapping.IsUFormula ℒₛₑₜ (iT 0 x)) := by
  definability

/-! ## 试证的结果：**归纳已接通，三个子目标待补**

**已接通**（这是实质进展）：
- 目标谓词 `P x := IsUFormula ℒₛₑₜ (iT 0 x)` **合成 `𝚺ᴬ₁-Predicate`**（`definability`，`rc=0`）；
- `Bootstrapping.IsUFormula.ISigma1.sigma1_succ_induction` **可用**，
  八种情形被正确展开为八个子目标。

**三个子目标待补**（都是具体的技术步骤，不是概念障碍）：

| 子目标 | 需要什么 |
|---|---|
| `hrel` | `IsUFormula ℒₛₑₜ (iTR 0 k r v)`——即 `iTR` 把**算术原子**映成**集合语言原子**。需 `iTR` 的 `IsUFormula` 引理（对应 `iT_quote_rel`） |
| `hnrel` | `IsUFormula ℒₛₑₜ (neg ℒₛₑₜ (iTR 0 k r v))`——`neg` 保持 `IsUFormula`（`IsUFormula.neg`，`Formula/Functions.lean:102`） |
| `hall`/`hexs` | `IsUFormula ℒₛₑₜ (imp ℒₛₑₜ domZero (iT (0+1) p))`——**注意 `iT (0+1)` 不是 `iT 0`**！归纳假设给的是 `iT 0 p`，而 `all` 情形要 `iT (0+1) p`。**这就是 `allChanges`/`exsChanges` 的作用**（层数加一），需要一条**层数无关**的辅助引理 |

**第三条是本轮的新发现**：`iT` 的 `all`/`exs` 情形**增加层数**（`iT.blueprint` 的
`allChanges n _ := n + 1`），所以归纳假设 `P p := IsUFormula ℒₛₑₜ (iT 0 p)`
**不直接适用**——需要一个「层数无关」的版本，
或把 `P` 改成 `∀ n, IsUFormula ℒₛₑₜ (iT n p)`。

**后者更可能成功**：`P p := ∀ n : V, IsUFormula ℒₛₑₜ (iT n p)`——
它对 `n` 全称，所以 `all` 情形的 `n + 1` 自动覆盖。
但 `∀ n` 是**内部**量词，`P` 是否仍 Σ₁ 可定义**要重新查**。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进入收据。
- **记录的是进展与待补子目标，不是证明。**
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008ITQuoteProof

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
  GodelQ.CG008OfSs GodelQ.CG008FinalAnalysis GodelQ.CG008ITQuote

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1**：`iT` 由 `iT.blueprint` 的 `result` 给出——**Σ₁ 函数**（`iTDef`）。 -/
noncomputable example : 𝚺ᴬ₁.Semisentence 3 := iTDef

/-- **查实 2（决定性，已过）**：目标谓词合成 `𝚺ᴬ₁-Predicate`——整条路的闸门。 -/
example : 𝚺ᴬ₁-Predicate (fun x : V ↦ Bootstrapping.IsUFormula ℒₛₑₜ (iT 0 x)) := by
  definability

/-- **查实 3**：`all`/`exs` 情形**增加层数**——`iT.blueprint` 的 `allChanges n _ := n + 1`。

**所以归纳假设 `IsUFormula ℒₛₑₜ (iT 0 p)` 不直接适用于 `all`**——
需要层数无关的版本。 -/
noncomputable example (n p : V) : V := iT (n + 1) p

/-- **查实 4（下一步的形状）**：把 `P` 改成**层数无关**的版本。

`P p := ∀ n : V, IsUFormula ℒₛₑₜ (iT n p)`——`all` 情形的 `n + 1` 自动覆盖。

**待查**：`∀ n` 是内部量词，`P` 是否仍 Σ₁ 可定义。
（若不可，需改用别的形状——那是下一步的具体工作。） -/
example : Prop := ∀ p : V, Bootstrapping.IsUFormula ℒₒᵣ p →
    ∀ n : V, Bootstrapping.IsUFormula ℒₛₑₜ (iT n p)

end GodelQ.CG008ITQuoteProof
