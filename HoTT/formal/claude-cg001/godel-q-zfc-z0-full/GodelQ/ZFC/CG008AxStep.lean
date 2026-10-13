import GodelQ.ZFC.CG008FixpointProbe

/-!
# CG-008 · 缺口核心步：`axm` 步在 V 内

`Fixpoint.induction` 可用（见 `CG008FixpointProbe`），归纳步要处理
`Derivation.blueprint` 的十种规则。**九种与 `T` 无关**（纯逻辑，图不含 `T`），
唯一依赖 `T` 的是 `axm` 步：

```
axLGraph d s p ∧ p ∈ s ∧ ¬p ∈ s   （`Basic.lean:415`）
```

其 V 内前提是 `p ∈ 𝗜𝚺₁.Δ₁Class`。**归纳步要证的**：
`translate p` 在 𝗭𝗙𝗖 中可证（V 内），即 `Provable 𝗭𝗙𝗖 ⌜translate p⌝`。

## 本文件做什么

把这一步**精确写成一条显式命题**，并标明它**就是**缺口——
不是证明。这样后继工作单元有一个单一、可独立攻的目标。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008AxStep
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Z0Full GodelQ.Translate
variable {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **缺口核心步（`axm` 步）**：`𝗜𝚺₁` 的每条公理的**翻译**在 𝗭𝗙𝗖 中可证，
且这一事实**在 V 内**有证明码。

**这就是缺口**：它说的是「V 能把 `p ∈ 𝗜𝚺₁.Δ₁Class` 变成
`Provable 𝗭𝗙𝗖 ⌜translate p⌝`」。`paInterp.interpret_theory` 只在**元层**
对**标准** `p` 给这件事；V 可以是**非标准**的。 -/
def AxStep : Prop :=
  ∀ p : V, p ∈ (𝗜𝚺₁ : ArithmeticTheory).Δ₁Class →
    Provable 𝗭𝗙𝗖 (Translate.iT 0 p)

/-- **九种逻辑规则与 `T` 无关**：`Derivation.blueprint` 的十个分支里，
只有 `axLGraph` 那支提到 `T` 的谓词（经 `p ∈ T.Δ₁Class`）。
其余九支（`verumIntro`/`andIntro`/`orIntro`/`allIntro`/`exsIntro`/`wkRule`/
`shiftRule`/`cutRule`/`axR`）的图是**纯语法**的，与 `T` 无关。

**这不是新定理**——`CG008DerivationTransform` 已机器化同一事实。
此处只把它接到 `Fixpoint.induction` 的归纳步形状上。 -/
theorem axStep_is_the_gap :
    AxStep (V := V) ↔
      (∀ p : V, p ∈ (𝗜𝚺₁ : ArithmeticTheory).Δ₁Class →
        Provable 𝗭𝗙𝗖 (Translate.iT 0 p)) :=
  Iff.rfl

/-- **对标准公理，`axStep` 是定理**：若 `p = ⌜σ⌝` 且 `σ ∈ 𝗜𝚺₁`，
则 `iT 0 p = ⌜translate σ⌝`（`iT_quote`），而 `translate σ` 在 𝗭𝗙𝗖 中可证
（`paInterp.interpret_theory`，元层）。**V 内的编码由 `internalize_provability` 给。** -/
theorem axStep_standard (σ : Sentence ℒₒᵣ) (hσ : σ ∈ (𝗜𝚺₁ : ArithmeticTheory)) :
    Provable 𝗭𝗙𝗖 (Translate.iT 0 (⌜σ⌝ : V)) := by
  have hq := GodelQ.Translate.iT_quote (V := V) σ
  simp only [Nat.cast_zero] at hq
  rw [hq]
  have hPA : 𝗣𝗔 ⊢ σ := Entailment.weakerThan_iff.mp (inferInstance : 𝗜𝚺₁ ⪯ 𝗣𝗔)
    (Entailment.by_axm hσ)
  exact internalize_provability (V := V) (GodelQ.ZFCZ0.zfc_proves_PA_theorems hPA)

end GodelQ.CG008AxStep

#print axioms GodelQ.CG008AxStep.axStep_standard
