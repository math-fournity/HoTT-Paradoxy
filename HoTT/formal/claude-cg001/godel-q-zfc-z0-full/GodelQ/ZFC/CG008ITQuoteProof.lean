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

end GodelQ.CG008ITQuoteProof
