import GodelQ.ZFC.CG008Probe10

/-!
# CG-008 探针 11（非收据）：`SoundOnHierarchy` 是不是那道墙

读 `Arithmetic/Definability/Absoluteness.lean:121-152` 发现两条关键引理：

```lean
variable {T : ArithmeticTheory} [𝗣𝗔⁻ ⪯ T] [T.SoundOnHierarchy 𝚺 1]

lemma models_iff_provable_of_Sigma0_param [V↓[ℒₒᵣ] ⊧* T] {σ : ArithmeticSemisentence n}
    (hσ : ℬ[<, ℒₒᵣ].Hierarchy 𝚺 0 σ) {e : Fin n → ℕ} :
    V ⊧/(Nat.cast ∘ e) σ ↔ T ⊢ (σ ⇜ fun x ↦ numeral (e x))

lemma models_iff_provable_of_Delta1_param [V↓[ℒₒᵣ] ⊧* T] {σ : 𝚫ᴬ₁.Semisentence n}
    (hσ : σ.ProperOn ℕ) (hσV : σ.ProperOn V) {e : Fin n → ℕ} :
    V ⊧/(Nat.cast ∘ e) σ.val ↔ T ⊢ (σ.val ⇜ fun x ↦ numeral (e x))
```

**注意前提 `[T.SoundOnHierarchy 𝚺 1]`**：这条说「T 在 Σ₁ 层级上**可靠**」——
即 `T ⊢ σ → ℕ ⊨ σ` 对 Σ₁ 句成立。

这是**反方向**的：它从「V 中真」推出「T 可证」，靠的是 T 的**可靠性**
（把非标准模型里的证明降到标准模型里核对）。

本探针查实：
1. `SoundOnHierarchy` 对 `𝗭𝗙𝗖` 是否成立（`𝗭𝗙𝗖` 是 `SetTheory` 不是 `ArithmeticTheory`）；
2. 这条引理能否用于缺口。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Probe11

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.ZFCSetSigma1
  GodelQ.ZFCSetInternal GodelQ.CG008Reduce GodelQ.CG008SetAll GodelQ.CG008Raw
  GodelQ.CG008RawSigma1 GodelQ.CG008SetSigma1Complete

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1**：`SoundOnHierarchy` 的定义（`Basic/Hierarchy.lean:182`）是
`T.SoundOn (Hierarchy 𝚺 1)`——一个 `abbrev`，不是 `iff`。 -/
example (T : ArithmeticTheory) :
    T.SoundOnHierarchy 𝚺 1 = T.SoundOn (ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1) := rfl

/-- **查实 2（关键）**：`SoundOnHierarchy 𝚺 1` 说的是
「T 证明的 Σ₁ 句**在标准模型 ℕ 中为真**」。

对缺口的用途：若能用它，就能从 `T ⊢ σ` 回到 `ℕ ⊨ σ`，
进而（经 Σ₁ 完全性的另一方向）回到 V 中的真。

**但对 `𝗭𝗙𝗖` 不直接可用**：`SoundOnHierarchy` 定义在 `ArithmeticTheory` 上，
而 `𝗭𝗙𝗖 : Theory ℒₛₑₜ`。 -/
example (T : ArithmeticTheory) [T.SoundOnHierarchy 𝚺 1]
    {σ : ArithmeticSentence} (hσ : ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 σ) (h : T ⊢ σ) :
    ℕ↓[ℒₒᵣ] ⊧ σ :=
  T.soundOnHierarchy 𝚺 1 h hσ

/-- **查实 3**：`Sh`（𝗭𝗙𝗖 的算术影子）是 `ArithmeticTheory`，
所以 `Sh.SoundOnHierarchy 𝚺 1` **可以陈述**（类型检查通过）。 -/
example : Sh.SoundOnHierarchy 𝚺 1 = Sh.SoundOn (ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1) := rfl

end GodelQ.CG008Probe11
