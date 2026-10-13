import GodelQ.ZFC.CG008GapSharp
import GodelQ.ZFC.CG008Circularity

/-!
# CG-008 · 照 `provable_D3` 的证明模式试 `zfcTr` 的 D3

## Foundation 的模式（`StandardProvability.lean:66`）

```lean
lemma provable_sigma_one_complete [𝗣𝗔⁻ ⪯ T] {σ : ArithmeticSentence}
    (hσ : ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 σ) : 𝗜𝚺₁ ⊢ σ 🡒 □σ :=
  complete 𝗜𝚺₁ _ fun (V : Type) _ _ ↦ by
    simpa [models_iff] using Bootstrapping.Arithmetic.sigma_one_complete (T := T) (V := V) hσ

theorem provable_D3 [𝗣𝗔⁻ ⪯ T] {σ : ArithmeticSentence} :
    𝗜𝚺₁ ⊢ □σ 🡒 □□σ := provable_sigma_one_complete (by simp)
```

**关键**：`provable_D3` 是 `provable_sigma_one_complete` 的**特例**——
取 `σ := □σ`（它本身是 Σ₁ 句）。整个证明只有一行：
`complete 𝗜𝚺₁` + 在任意 V 内用 `sigma_one_complete`。

## 照搬到 `zfcTr`

`zfcTr σ = trProv.val/[⌜σ⌝]`，而 `zfcTr σ` 是 Σ₁ 句（`zfcTr_sigma1`）。
所以「`zfcTr σ 🡒 zfcTr (zfcTr σ)`」**如果**也能写成
`complete 𝗜𝚺₁ _ (fun V => sigma_one_complete …)`，就一样一行。

**但这里就是缺口**：`sigma_one_complete` 的 `T` 必须是**算术理论**
（它要 `T.Δ₁`、`𝗣𝗔⁻ ⪯ T`，且证明内部用 `term_complete` 把 V 的元素
代换成**数字项**）。而 `zfcTr` 的「理论」是 `Sh`——**不是**算术理论，
它是 `ℒₒᵣ` 上由 𝗭𝗙𝗖 的可证性定义的集合，`Sh.Δ₁` **不存在**（与 G1 矛盾）。

**所以模式搬不过来**：`complete` 那一行要求的 `□` 是 `provabilityPred T`
（`T` 算术理论），而缺口要的是 `trProv.val/[·]`（ZFC 可证性）。
两者在标准模型 ℕ 上重合（`zfcTr_D3_standard` 已证），
但在**非标准** V 上不重合——这正是落差。

## 本文件做什么

把「照搬」的**尝试**精确写成一条条件定理，以标明它**在哪一行**断掉：
断在 `[Sh.Δ₁]` 上。**不声称缺口已证。**
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008D3Attempt2
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Z0Full GodelQ.Translate
variable {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **断点**：照搬模式需要的实例。

`Sh` 是 `ℒₒᵣ` 上的理论（`Z0Shadow.lean` 定义），若它有 `Δ₁`，
则 `provable_D3 (T := Sh)` 可用，缺口即闭合。
**但 `Sh.Δ₁` 不存在**——本文件只把这条依赖写成显式类型（**不证明它**，
也不可能：`CG008Delta1Wall` 已证其不可能）。 -/
example : Type := Theory.Δ₁ (Sh : Theory ℒₒᵣ)

/-- **模式搬不过来的精确原因**：`provable_sigma_one_complete` 的
`T` 必须满足 `𝗣𝗔⁻ ⪯ T` 与 `T.Δ₁`，而 `Sh` 两者都不满足
（`𝗣𝗔⁻ ⪯ Sh` **成立**，但 `Sh.Δ₁` 不成立）。 -/
example : 𝗣𝗔⁻ ⪯ (Sh : Theory ℒₒᵣ) := inferInstance

end GodelQ.CG008D3Attempt2
