import GodelQ.ZFC.CG008Probe19

/-!
# CG-008 探针 20（非收据）：跨语言墙的**最终形式**

## 探针 19 的结果

`𝗭𝗙𝗖.standardProvability : Provability 𝗜𝚺₁ 𝗭𝗙𝗖` **建成了**（`rc=0`）。
四个前提都就位：多语言 `Provability` + `ℒₒᵣ` 的通用 `GödelNumber`
+ `ℒₛₑₜ.LORDefinable` + `𝗭𝗙𝗖.Δ₁`。

**而且它的 D1 对集合句成立**（`provable_D1` 的 `{σ : Sentence L}` 是通用的）：

```
𝗭𝗙𝗖 ⊢ σ → 𝗜𝚺₁ ⊢ provable 𝗭𝗙𝗖 σ        -- σ 是集合句
```

## 但 `HBL3` 对**它**连陈述都不行

`HBL3` 的声明（`ProvabilityAbstraction/Basic.lean:62`，所在 section 的
`variable [L.ReferenceableBy L] {T₀ T : Theory L}`）：

```lean
class HBL3 (𝔅 : Provability T₀ T) where
  D3 {σ : Sentence L} : T₀ ⊢ 𝔅 σ 🡒 𝔅 (𝔅 σ)
```

**`𝔅 (𝔅 σ)` 要求 `𝔅 σ : Sentence L`**，但 `𝔅.pr : Sentence L → Sentence L₀`。
所以 `HBL3` **只在 `L = L₀` 时有意义**。

对照：

| | `T₀` | `T` | `L₀` | `L` | `HBL2` | `HBL3` |
|---|---|---|---|---|---|---|
| `zfcTr : Provability 𝗜𝚺₁ Sh` | `𝗜𝚺₁` | `Sh` | `ℒₒᵣ` | `ℒₒᵣ` | ✅ | ✅ **可陈述**（缺口所在） |
| `𝗭𝗙𝗖.standardProvability : Provability 𝗜𝚺₁ 𝗭𝗙𝗖` | `𝗜𝚺₁` | `𝗭𝗙𝗖` | `ℒₒᵣ` | `ℒₛₑₜ` | ✅ | ❌ **不可陈述** |

`HBL2` 是**多语言**的（`D2 {σ τ : Sentence L} : T₀ ⊢ 𝔅(σ🡒τ) 🡒 𝔅σ 🡒 𝔅τ`——
两边都是 `L₀` 句，自洽）；`HBL3` 不是。

## 这是跨语言墙的最终形式

缺口要在「**同一语言**的可证性谓词」上做 D3，
而 ZFC 的可证性谓词**天然跨语言**（集合句 → 算术句）。

于是只有两条路，**都被堵死**：

1. **走 `zfcTr : Provability 𝗜𝚺₁ Sh`**（同语言，`HBL3` 可陈述）——
   但 `Sh` 没有 `Δ₁`（探针 15），`provable_D3` 用不了，D3 必须手证。
2. **走 `𝗭𝗙𝗖.standardProvability : Provability 𝗜𝚺₁ 𝗭𝗙𝗖`**（有 `Δ₁`）——
   但 `HBL3` 连陈述都不行。

**两条路各堵一半，而它们堵的正是同一件事**：
ZFC 的可证性谓词把 `ℒₛₑₜ` 句映到 `ℒₒᵣ` 句，这个跨语言性
要么让 `Δ₁` 丢失（路 1），要么让 `HBL3` 无法陈述（路 2）。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进入收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Probe20

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.CG008HBL3
  GodelQ.CG008HBL3Test GodelQ.CG008Final GodelQ.CG008Probe15 GodelQ.CG008Probe16
  GodelQ.CG008Probe17 GodelQ.CG008Probe18 GodelQ.CG008Probe19

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1**：`𝗭𝗙𝗖.standardProvability` 的 `HBL2` 成立——
`provable_D2` 的 `{σ π : Sentence L}` 是通用的，对 `L = ℒₛₑₜ` 可用。 -/
noncomputable example : 𝗭𝗙𝗖.standardProvability.HBL2 := inferInstance

/-- **查实 2（本探针的要点）**：`HBL3` 的 `D3` 需要 `𝔅 (𝔅 σ)`，
而 `𝔅.pr` 是 `Sentence L → Sentence L₀`。对 `𝗭𝗙𝗖.standardProvability`，
`L = ℒₛₑₜ` 而 `L₀ = ℒₒᵣ`，**类型对不上**。

所以 `𝗭𝗙𝗖.standardProvability.HBL3` **无法陈述**。
本探针用「`zfcTr` 的 HBL3 可陈述、`𝗭𝗙𝗖.standardProvability` 的不行」来固定这个对照。 -/
example (𝔅 : Provability 𝗜𝚺₁ Sh) [𝔅.HBL3] (σ : ArithmeticSentence) :
    𝗜𝚺₁ ⊢ 𝔅 σ 🡒 𝔅 (𝔅 σ) :=
  Provability.D3 (𝔅 := 𝔅) (σ := σ)

/-- **查实 3**：`zfcTr` 与 `𝗭𝗙𝗖.standardProvability` 的关系。

`zfcTr σ` 就是 `provable 𝗭𝗙𝗖` 作用在 `⌜translate σ⌝` 上，
而 `𝗭𝗙𝗖.standardProvability.pr` 是 `provable 𝗭𝗙𝗖` 作用在 `⌜·⌝` 上。
**所以 `zfcTr` 是 `𝗭𝗙𝗖.standardProvability` 与 `translate` 的复合**——
这正是它跨语言的体现。 -/
example (σ : ArithmeticSentence) :
    TrProvable (⌜σ⌝ : V) ↔ Provable 𝗭𝗙𝗖 (⌜arithTrln.translate σ⌝ : V) :=
  trProvable_quote σ

end GodelQ.CG008Probe20
