import GodelQ.ZFC.CG008Probe16

/-!
# CG-008 探针 17（非收据）：能否把缺口改述为「`𝗭𝗙𝗖` 是 `Provability` 的 `T`」

## 探针 16 的发现

`Provability T₀ T` 要求 `[L.ReferenceableBy L₀]` 且 `T₀ T : Theory L`（**同语言**）。
`zfcTr : Provability 𝗜𝚺₁ Sh` 里两者都是 `Theory ℒₒᵣ`——所以它满足形状。
但缺口的**内容**谈的是 `𝗭𝗙𝗖`（`trProvable_quote`），
`Sh` 只是为了让类型成立而引入的影子。

**问题**：能不能反过来——让 `𝗭𝗙𝗖` 当 `T`？

## 障碍

`Provability T₀ T` 要求 `T₀ T : Theory L` 同语言。而

- `𝗜𝚺₁ : Theory ℒₒᵣ`（算术语言）；
- `𝗭𝗙𝗖 : Theory ℒₛₑₜ`（集合语言）。

**语言不同**，所以 `Provability 𝗜𝚺₁ 𝗭𝗙𝗖` 直接写不出来。
但 `Provability` 是**多语言**的：`Provability (T₀ : Theory L₀) (T : Theory L)`——
`L₀` 与 `L` 可以不同！只有 `[L.ReferenceableBy L₀]`（`GödelNumber L₀ (Sentence L)`）
是要求。

所以真正的问题是：**`ℒₒᵣ.ReferenceableBy ℒₛₑₜ` 是否成立**？
即「能否把集合句 Gödel 编码成算术数」。

**这可能正是缺失的那块拼图**：若能，缺口就能改述为
`Provability 𝗜𝚺₁ 𝗭𝗙𝗖`，而 `𝗭𝗙𝗖` 有 `Δ₁`（探针 16），
`provable_D3` 也许就适用了。

## 本探针查实
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Probe17

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.CG008HBL3
  GodelQ.CG008HBL3Test GodelQ.CG008Final GodelQ.CG008Probe15 GodelQ.CG008Probe16

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1**：`Provability` 是**多语言**的——`T₀` 与 `T` 的语言可以不同。 -/
example (L₀ L : Language) [L.ReferenceableBy L₀] (T₀ : Theory L₀) (T : Theory L) :
    Type _ := Provability T₀ T

/-- **查实 2（关键问题）**：`ℒₒᵣ.ReferenceableBy ℒₛₑₜ` 成立吗？

即 `GödelNumber ℒₛₑₜ (Sentence ℒₒᵣ)`——把**算术句**编码成**集合语言**的项。
反过来（把集合句编码成算术数）才是我想要的：
`Semiterm.Operator.GödelNumber ℒₒᵣ (Sentence ℒₛₑₜ)`。

Foundation 的 `ℒₒᵣ` 有 `GödelNumber ℒₒᵣ α` 对**任意** `[Encodable α]`
（`Arithmetic/Basic/Misc.lean:114`：`instance : Semiterm.Operator.GödelNumber ℒₒᵣ α`）。
所以若 `Sentence ℒₛₑₜ` 有 `Encodable`，这条就成立。 -/
example : Semiterm.Operator.GödelNumber ℒₒᵣ (Sentence ℒₛₑₜ) := inferInstance

/-- **查实 3**：于是 `Provability 𝗜𝚺₁ 𝗭𝗙𝗖` **可以陈述**！

这打开了探针 16 提出的出路：以 `𝗭𝗙𝗖` 为被谈论理论的 `Provability` 结构。
注意 `prov` 的类型是 `Semisentence ℒₒᵣ 1`（算术句），而 `bew_def` 要
`𝗭𝗙𝗖 ⊢ σ → 𝗜𝚺₁ ⊢ prov/[⌜σ⌝]`——**这正是缺口的形状**，
且 `⌜σ⌝` 现在是 `Semiterm ℒₒᵣ Empty 1`（算术项，承载集合句的码）。 -/
example : Type _ := Provability 𝗜𝚺₁ 𝗭𝗙𝗖

/-- **查实 4**：`zfcTr` 与这条形状的关系——`zfcTr.prov` 就是 `trProv.val`，
它量化的正是 `provable 𝗭𝗙𝗖`。所以 `zfcTr` **其实**已经是
`Provability 𝗜𝚺₁ 𝗭𝗙𝗖` 的候选，只是被声明成了 `Provability 𝗜𝚺₁ Sh`。 -/
noncomputable example : zfcTr.prov = trProv.val := rfl

end GodelQ.CG008Probe17
