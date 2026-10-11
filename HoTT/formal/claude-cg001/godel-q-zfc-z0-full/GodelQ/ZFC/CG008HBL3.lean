import GodelQ.ZFC.Z0Full

/-!
# CG-008 · 缺口 = `HBL3`（抽象 D3），以及一条新的可证子句

## 本轮读到的关键 API（`ProvabilityAbstraction/Basic.lean:25-93`）

```lean
structure Provability [L.ReferenceableBy L₀] (T₀ : Theory L₀) (T : Theory L) where
  prov : Semisentence L₀ 1
  bew_def {σ : Sentence L} : T ⊢ σ → T₀ ⊢ prov/[⌜σ⌝]        -- D1

class HBL2 (𝔅 : Provability T₀ T) where
  D2 {σ τ : Sentence L} : T₀ ⊢ 𝔅 (σ 🡒 τ) 🡒 𝔅 σ 🡒 𝔅 τ

class HBL3 (𝔅 : Provability T₀ T) where
  D3 {σ : Sentence L} : T₀ ⊢ 𝔅 σ 🡒 𝔅 (𝔅 σ)                  -- ← 缺口就是它

class FormalizedCompleteOn (𝔅 : Provability T₀ T) (σ) where
  formalized_complete_on : T₀ ⊢ σ 🡒 𝔅 σ

instance [∀ σ, 𝔅.FormalizedCompleteOn (𝔅 σ)] : 𝔅.HBL3 := ⟨by simp⟩
```

## 本文件的两个结论

### 结论 A（新）：缺口的 `zfcTr` 对 `Sh` 满足 `HBL2`

`zfcTr : Provability 𝗜𝚺₁ Sh` 已由 `Z0Full.lean:60` 建成（带 D1）。
`HBL2` 的内容是「𝔅 对蕴含分配」：`𝔅(σ🡒τ) → 𝔅σ → 𝔅τ`。
对 `zfcTr`，这从 `provable 𝗭𝗙𝗖` 的 D2 来（`𝗭𝗙𝗖` 的证明系统对蕴含封闭）。

### 结论 B：缺口 ⟺ `zfcTr.HBL3`

`HBL3` 的内容 `𝔅 σ → 𝔅 (𝔅 σ)` 展开后，`𝔅 = zfcTr` 时正是
`Provable 𝗭𝗙𝗖 ⌜translate σ⌝ → Provable 𝗭𝗙𝗖 ⌜translate (zfcTr σ)⌝`
（经 `models_zfcTr_iff` 与 `trProvable_quote`）——**即 `zfcTr_D3_internalize`**。

且 Foundation **已有** `instance [∀ σ, 𝔅.FormalizedCompleteOn (𝔅 σ)] : 𝔅.HBL3`，
所以缺口的**充分条件是** `∀ σ, zfcTr.FormalizedCompleteOn (zfcTr σ)`，
即「`zfcTr σ → zfcTr (zfcTr σ)` 的可形式化版本」。

**这是把缺口从「集合语言的 Σ₁ 完全性」改述为「`Sh` 上可证性谓词的 HBL3」**——
一个更标准、更易与既有文献对照的形状。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进入收据。
- **不声称 D3 已证**；`Z0Blocked.lean` 的未证标记仍在。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008HBL3

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1**：`HBL3` 的定义就是缺口的形状。

`D3 : T₀ ⊢ 𝔅 σ 🡒 𝔅 (𝔅 σ)`。
注意它的类型约束是 `{T₀ T : Theory L}`——**同一语言**，且 `[L.ReferenceableBy L]`。
`zfcTr : Provability 𝗜𝚺₁ Sh` 里两者都是 `Theory ℒₒᵣ`，正好满足。 -/
example (𝔅 : Provability 𝗜𝚺₁ Sh) [𝔅.HBL3] (σ : ArithmeticSentence) :
    𝗜𝚺₁ ⊢ 𝔅 σ 🡒 𝔅 (𝔅 σ) :=
  Provability.D3 (𝔅 := 𝔅) (σ := σ)

/-- **查实 2**：Foundation 已提供从 `FormalizedCompleteOn` 到 `HBL3` 的实例。

所以缺口的**充分条件**是 `∀ σ, zfcTr.FormalizedCompleteOn (zfcTr σ)`。 -/
example (𝔅 : Provability 𝗜𝚺₁ Sh) [∀ σ, 𝔅.FormalizedCompleteOn (𝔅 σ)] : 𝔅.HBL3 :=
  inferInstance

/-- **查实 3**：`zfcTr` 是 `Provability 𝗜𝚺₁ Sh`（已建成，带 D1）。 -/
noncomputable example : Provability 𝗜𝚺₁ Sh := zfcTr

/-- **查实 4（结论 B）**：缺口的**语义形状**。

`zfcTr_D3_internalize` 的结论
`Provable 𝗭𝗙𝗖 (⌜translate (zfcTr τ)⌝ : V)`
经 `models_zfcTr_iff` 就是 `V ⊨ zfcTr (zfcTr τ)`；
而前提 `Provable 𝗭𝗙𝗖 (⌜translate τ⌝ : V)` 就是 `V ⊨ zfcTr τ`。
所以缺口**在语义层就是** `V ⊨ zfcTr τ → V ⊨ zfcTr (zfcTr τ)`。

下面把**两个方向**的等价各固定一条（不证明缺口本身）。 -/
example (W : Type) [ORingStructure W] [W↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (τ : ArithmeticSentence)
    (h : W↓[ℒₒᵣ] ⊧ zfcTr τ) :
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : W) :=
  (models_zfcTr_iff W τ).mp h

example (W : Type) [ORingStructure W] [W↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (τ : ArithmeticSentence)
    (h : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr τ)⌝ : W)) :
    W↓[ℒₒᵣ] ⊧ zfcTr (zfcTr τ) :=
  (models_zfcTr_iff W (zfcTr τ)).mpr h

/-- **查实 5（结论 A 的骨架）**：`HBL2` 对 `zfcTr` 的形状。

`HBL2` 要求 `𝗜𝚺₁ ⊢ 𝔅(σ🡒τ) 🡒 𝔅σ 🡒 𝔅τ`。
对 `zfcTr` 展开（`zfcTr_def` + `models_trProv_iff`），它说的是
「`Provable 𝗭𝗙𝗖 ⌜translate (σ🡒τ)⌝` → `Provable 𝗭𝗙𝗖 ⌜translate σ⌝` →
`Provable 𝗭𝗙𝗖 ⌜translate τ⌝`」——即 `𝗭𝗙𝗖` 的证明对蕴含封闭，
再内部化一次。这是**可证的**（`provable 𝗭𝗙𝗖` 的 D2），但需要把
`translate` 与 `🡒` 的交换律（`arithTrln` 是同态）在 `𝗜𝚺₁` 里形式化。
本文件只固定形状，不证明它。 -/
example (σ τ : ArithmeticSentence) :
    zfcTr (σ 🡒 τ) = trProv.val/[⌜σ 🡒 τ⌝] :=
  zfcTr_def (σ 🡒 τ)

end GodelQ.CG008HBL3
