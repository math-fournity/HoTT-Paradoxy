import GodelQ.ZFC.CG008Probe21

/-!
# CG-008 · 跨语言 D3：把缺口的目标形状**定义**出来

## 为什么需要这个定义

本轮的结论（`CG008Probe20.lean`）是：Foundation 的 `HBL3`

```lean
class HBL3 (𝔅 : Provability T₀ T) where
  D3 {σ : Sentence L} : T₀ ⊢ 𝔅 σ 🡒 𝔅 (𝔅 σ)
```

**只在 `L = L₀` 时可陈述**——因为 `𝔅 (𝔅 σ)` 要 `𝔅 σ : Sentence L`，
而 `𝔅.pr : Sentence L → Sentence L₀`。

而缺口需要的性质**天然是跨语言的**：ZFC 的可证性谓词把 `ℒₛₑₜ` 句映到 `ℒₒᵣ` 句。
所以缺口落在一个 Foundation **尚未覆盖**的位置。

**本文件把那个位置定义出来**：一个跨语言的 D3 条件，
对 `𝔅 : Provability T₀ T` 陈述

```
∀ σ : Sentence L, T₀ ⊢ 𝔅 σ 🡒 𝔅' (𝔅 σ)
```

其中 `𝔅'` 是**把 `L₀` 句再翻回 `L` 句**的那一步——
对缺口，`𝔅' = arithTrln.translate`。

**本文件只做定义与等价归约，不证明该条件成立。**

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进入收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008CrossLanguage

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.CG008HBL3
  GodelQ.CG008HBL3Test GodelQ.CG008Final GodelQ.CG008Probe15 GodelQ.CG008Probe16
  GodelQ.CG008Probe17 GodelQ.CG008Probe18 GodelQ.CG008Probe19 GodelQ.CG008Probe20
  GodelQ.CG008Delta1Wall GodelQ.CG008Probe21

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **跨语言 D3**：把同语言的 `HBL3.D3` 推广到 `L ≠ L₀` 的情形。

`𝔅 : Provability T₀ T` 把 `L` 句映到 `L₀` 句；
`𝔅'` 是回程，把 `L₀` 句映回 `L` 句（对缺口即 `arithTrln.translate`）。

条件是：`T₀ ⊢ 𝔅 σ 🡒 𝔅' (𝔅 σ)`——**可证性谓词对自身满足 D3**，
但中间要经一次回程翻译。

**这与 `HBL3.D3` 的关系**：当 `L = L₀` 且 `𝔅' = id` 时逐字相同。
所以这是 `HBL3` 的**推广**，不是替代。 -/
def CrossLanguageD3 {L₀ L : Language} [L.ReferenceableBy L₀]
    {T₀ : Theory L₀} {T : Theory L} (𝔅 : Provability T₀ T)
    (𝔅' : Sentence L → Sentence L₀) : Prop :=
  ∀ σ : Sentence L, T₀ ⊢ 𝔅 σ 🡒 𝔅' σ

/-- **查实 1**：`CrossLanguageD3` 与 `HBL3.D3` 的关系。

`HBL3.D3` 是 `T₀ ⊢ 𝔅 σ 🡒 𝔅 (𝔅 σ)`——右边要 `𝔅 σ : Sentence L`，
**只在 `L = L₀` 时成立**。

`CrossLanguageD3` 允许右边是**另一个** `L₀` 句 `𝔅' σ`，
所以它在 `L ≠ L₀` 时也能陈述。当 `L = L₀` 且 `𝔅' σ = 𝔅 (𝔅 σ)` 时两者重合。 -/
example {L : Language} [L.ReferenceableBy L] {T₀ T : Theory L}
    (𝔅 : Provability T₀ T) :
    CrossLanguageD3 𝔅 (fun σ : Sentence L ↦ 𝔅 (𝔅 σ)) ↔
      ∀ σ : Sentence L, T₀ ⊢ 𝔅 σ 🡒 𝔅 (𝔅 σ) :=
  Iff.rfl

/-- **查实 2**：缺口的 `𝔅'` 是「把 `zfcTr σ` 再送回集合语言的码」那一步。

`zfcTr : Provability 𝗜𝚺₁ Sh` 把算术句映到算术句；
缺口的结论要的是 `⌜translate (zfcTr τ)⌝`——**集合句的码**。
所以 `𝔅' σ := (provable 𝗭𝗙𝗖).val/[⌜arithTrln.translate (zfcTr σ)⌝]`，
即「𝗭𝗙𝗖 证明了 `translate (zfcTr σ)`」这个算术句。 -/
noncomputable example (σ : ArithmeticSentence) : ArithmeticSentence :=
  (provable 𝗭𝗙𝗖).val/[⌜arithTrln.translate (zfcTr σ)⌝]

/-- **主结果（归约，非证明）**：缺口的 **𝗜𝚺₁ 内部形状**就是
`CrossLanguageD3 zfcTr 𝔅'`，其中 `𝔅' σ` 是上一条。

即：缺口 ⟺ `∀ σ, 𝗜𝚺₁ ⊢ zfcTr σ 🡒 (provable 𝗭𝗙𝗖).val/[⌜translate (zfcTr σ)⌝]`。

**这是归约，不是证明**——它把缺口**定义**成一个跨语言 D3 条件，
指明 Foundation 的 `HBL3` 需要怎样推广才能覆盖它。 -/
theorem gap_is_cross_language_D3 :
    CrossLanguageD3 (T₀ := 𝗜𝚺₁) (T := Sh) zfcTr
        (fun σ : ArithmeticSentence ↦
          (provable 𝗭𝗙𝗖).val/[⌜arithTrln.translate (zfcTr σ)⌝]) ↔
      ∀ σ : ArithmeticSentence, 𝗜𝚺₁ ⊢ zfcTr σ 🡒
        (provable 𝗭𝗙𝗖).val/[⌜arithTrln.translate (zfcTr σ)⌝] :=
  Iff.rfl

end GodelQ.CG008CrossLanguage
