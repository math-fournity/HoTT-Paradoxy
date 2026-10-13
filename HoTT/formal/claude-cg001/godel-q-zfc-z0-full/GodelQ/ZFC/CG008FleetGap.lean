import GodelQ.ZFC.CG008AxStep
import GodelQ.ZFC.CG008GapSharp
import GodelQ.ZFC.Z0Full
import GodelQ.ZFC.ZFCDelta1

/-!
# CG-008 · 舰队对表：缺口的最小技术命题

本文件为跨会话对表（001-Master 2026-10-13 派工）而写：把 CG-008 的缺口写成**最小技术命题**，
并把「Foundation 缺什么 API」钉在可编译的例子上。**不声称缺口已证**；
`Z0Blocked.lean` 的未证标记仍在。

## 最小技术命题（`MinimalGap`）

```
∀ (V : Type) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (σ : ArithmeticSentence),
    Provable 𝗭𝗙𝗖 (⌜translate σ⌝ : V) → Provable 𝗭𝗙𝗖 (⌜translate (zfcTr σ)⌝ : V)
```

它一旦成立，Z0 完整形式立即成立（`z0_of_minimalGap`，经已证的
`Z0Full.zfc_z0_full_of_D3_internalize`）。

## 对一条舰队情报的机器化核对（重要更正）

情报称「**精确缺口 = ℕ→任意 V 的搬运**」。本文件把它拆成两半，各用一个可编译的例子核对：

| 方向 | 状态 | 证据 |
|---|---|---|
| ℕ → V：`Provable T (⌜σ⌝ : ℕ) → Provable T (⌜σ⌝ : V)` | **存在**（一行） | `n_to_v_transfer`：`Provable.sound`（`provable_iff_provable`）给元层 `T ⊢ σ`，再 `internalize_provability` 给任意 V 的内部编码 |
| V → ℕ：`Provable T (⌜σ⌝ : V) → T ⊢ σ` | **不存在**（非标准 V 上为假） | `Provable.sound` / `provable_iff_provable` 的载体**硬接线 `ℕ`**（`Coding.lean:424`、`D1.lean:40`）；这正是 `Z0Probe6/7` 的载体墙 |

**所以缺口不在「ℕ→V 的搬运」**——那个搬运是现成的。缺口的实质是：
`MinimalGap` 的**前提是 V 内部的**（V 内有一个编码为 V 元素的 𝗭𝗙𝗖 推导 `d`，非标准 V 时
`d` 可以是**非标准**推导），而结论要求 V 内部**造出**另一条推导 `d'`。
从 `d` 到 `d'` 的构造**只能在 V 内做**（不能经 ℕ，因为 V→ℕ 不存在）。

## 缺口的三个等价形状（本包已机器化）

| # | 形状 | 文件 |
|---|---|---|
| 1 | `MinimalGap`（上） | 本文件 |
| 2 | `zfcTr.HBL3`：`∀σ, 𝗜𝚺₁ ⊢ zfcTr σ 🡒 zfcTr (zfcTr σ)` | `CG008HBL3` |
| 3 | `AxStep`：`∀ p ∈ 𝗜𝚺₁.Δ₁Class, Provable 𝗭𝗙𝗖 (iT 0 p)` | `CG008AxStep` |

形状 3 是**归纳步**：`Derivation.induction1`（`Proof/Basic.lean:642`）的十支里九支是纯语法的
（经 `iT`/`iTSet` 重写可重建），唯一依赖 `T` 的是 `axm` 支——它的 V 内前提正是
`p ∈ 𝗜𝚺₁.Δ₁Class`。

## `AxStep` 的两个半边（已机器化的分界）

- **标准半边已证**（`axStep_standard`）：`p = ⌜σ⌝`、`σ ∈ 𝗜𝚺₁` 时，
  `iT 0 ⌜σ⌝ = ⌜translate σ⌝`（`iT_quote`），而 `translate σ` 在 𝗭𝗙𝗖 中可证
  （`paInterp.interpret_theory`，元层），其 V 内编码由 `internalize_provability` 给。
- **非标准半边是缺口**：非标准的 `p ∈ 𝗜𝚺₁.Δ₁Class` 必是**归纳模式的非标准实例**
  （`𝗣𝗔⁻` 有限，非标准码只能来自 `InductionScheme`）。
  其翻译是「ω 上的归纳实例」，公式为 `translate φ`（`φ` 非标准）。
  V 内要证的：**ZFC 对任意 V 内公式证明 ω 归纳**——即把 `PAModel.lean` 的
  「ω 是最小归纳集」论证（`W_induction`/`naturalNumber_induction`，目前是**元层**）
  在 **V 内**形式化。

## Foundation 缺什么 API（精确）

1. **无 V 内版的「解释保可证性」**：`DirectInterpretation.of_provability`
   （`LK/Interpretation.lean:443`）走 `complete_on_eq_models`（完备性），
   是**元层语义论证**，不产生 V 内的证明编码。
2. **无 V 内版的「ω 最小归纳」**：`PAModel.lean` 的 `models_succInd_W` /
   `naturalNumber_induction` 量化的是**元层** `φ : Semiformula ℒₒᵣ ℕ 1`，
   不覆盖 V 的非标准码。
3. **`Provable.sound` 的载体硬接线**：`provable_iff_provable` 只对 `: ℕ` 成立
   （`D1.lean:40`），所以 `MinimalGap` 的前提**不能**降到元层去用
   `interpret_theory` + `internalize_provability` 的组合。

第 3 条是本包 `CG008InterpretationWall`、`CG008Circularity` 与
`CG008Probe15/17-21` 反复确认的同一堵墙的第四种说法。

## 本文件已机器化的事实（可进收据，无未证标记）

- `z0_of_minimalGap`：`MinimalGap ⟹ Z0` 完整形式；
- `n_to_v_transfer`：ℕ→V 搬运**存在**（对情报的更正）；
- `n_instance_proved`：`MinimalGap` 的 ℕ-实例已证（`zfcTr_D3_standard`）；
- `standard_half_proved`：`AxStep` 的标准半边已证（`axStep_standard`）；
- `gap_sharpening`：`MinimalGap` 的前提**已经**给出一个 𝗜𝚺₁ 内部证明编码
  （`d3_hypothesis_gives_ISigma1_proof`）。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008FleetGap

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Z0Full GodelQ.Translate GodelQ.CG008AxStep

variable {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **最小技术命题**（`Z0Blocked.lean:61-65` 的 `Type` 层形状，与
`zfc_z0_full_of_D3_internalize` 的前提逐字相同）。 -/
def MinimalGap : Prop :=
  ∀ (V : Type) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (σ : ArithmeticSentence),
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate σ⌝ : V) →
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr σ)⌝ : V)

/-- **`MinimalGap ⟹ Z0` 完整形式**（引用已证的条件定理；本行无未证标记）。 -/
theorem z0_of_minimalGap (h : MinimalGap) :
    𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent : ArithmeticSentence) :=
  zfc_z0_full_of_D3_internalize h

/-- **ℕ→V 搬运存在**（对「缺口 = ℕ→V 搬运」这条情报的机器化更正）：
`Provable T (⌜σ⌝ : ℕ)` 先经 `provable_iff_provable` 降为元层 `T ⊢ σ`，
再经 `internalize_provability` 升为任意 V 的内部编码。
**所以「宇宙不匹配」不在这一侧。** -/
theorem n_to_v_transfer (σ : SetTheorySentence) (h : Provable 𝗭𝗙𝗖 (⌜σ⌝ : ℕ)) :
    Provable 𝗭𝗙𝗖 (⌜σ⌝ : V) :=
  internalize_provability (V := V) (provable_iff_provable.mp h)

/-- **V→ℕ 搬运不存在**（本节要点的另一面）：`provable_iff_provable` 的载体
硬接线 `ℕ`，所以 `MinimalGap` 的前提**不能**降为元层 `𝗭𝗙𝗖 ⊢ ·`。
本行只把该引理的**精确载体**钉住（不声称任何否命题是定理——那需要反例模型）。 -/
example (σ : SetTheorySentence) : (Provable 𝗭𝗙𝗖 (⌜σ⌝ : ℕ) ↔ 𝗭𝗙𝗖 ⊢ σ) :=
  provable_iff_provable

/-- **ℕ-实例已证**：`MinimalGap` 在 `V := ℕ` 上的对应语义形状
（`zfcTr_D3_standard`，正对照）。 -/
theorem n_instance_proved (σ : ArithmeticSentence) :
    ℕ↓[ℒₒᵣ] ⊧ (zfcTr σ 🡒 zfcTr (zfcTr σ)) :=
  zfcTr_D3_standard σ

/-- **`AxStep` 的标准半边已证**：`p = ⌜σ⌝`、`σ ∈ 𝗜𝚺₁` 时 `iT 0 p` 在 𝗭𝗙𝗖 中可证。 -/
theorem standard_half_proved (σ : Sentence ℒₒᵣ) (hσ : σ ∈ (𝗜𝚺₁ : ArithmeticTheory)) :
    Provable 𝗭𝗙𝗖 (Translate.iT 0 (⌜σ⌝ : V)) :=
  axStep_standard (V := V) σ hσ

/-- **锐化（前提已给出 𝗜𝚺₁ 内部编码）**：`MinimalGap` 的前提
（`Provable 𝗭𝗙𝗖 ⌜translate τ⌝`）经 `models_zfcTr_iff` + `zfcTr_sigma1`
**已经**给出一个 V 内部的 **𝗜𝚺₁** 证明编码——这个编码在原前提里从未被提到。
这是缺口可以改写成「**V 内的跨系统推导搬运**」的原因。 -/
theorem gap_sharpening (τ : ArithmeticSentence)
    (h : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V)) :
    Provable 𝗜𝚺₁ (⌜zfcTr τ⌝ : V) :=
  GodelQ.CG008GapSharp.d3_hypothesis_gives_ISigma1_proof (V := V) τ h

/-- **`AxStep` 的九支形状**（`CG008NineRules.DerivationTransform` 的
`Type` 层陈述）：V 内的码变换，把 `𝗜𝚺₁` 的推导码变成 `𝗭𝗙𝗖` 的推导码。 -/
def DerivationTransform : Prop :=
  ∀ (V : Type) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (d : V),
    Bootstrapping.Derivation (𝗜𝚺₁ : ArithmeticTheory) d →
    ∃ d' : V, Bootstrapping.Derivation (𝗭𝗙𝗖 : SetTheory) d'

end GodelQ.CG008FleetGap

#print axioms GodelQ.CG008FleetGap.z0_of_minimalGap
#print axioms GodelQ.CG008FleetGap.n_to_v_transfer
#print axioms GodelQ.CG008FleetGap.n_instance_proved
#print axioms GodelQ.CG008FleetGap.standard_half_proved
#print axioms GodelQ.CG008FleetGap.gap_sharpening
