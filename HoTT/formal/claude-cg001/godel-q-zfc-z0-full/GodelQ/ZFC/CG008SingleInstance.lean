import GodelQ.ZFC.CG008FleetGap

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

set_option linter.unusedSectionVars false

namespace GodelQ.CG008SingleInstance

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Z0Full GodelQ.Translate

/-!
# CG-008 · 单实例收窄：Z0 只需要**一条** D3 实例（在 Gödel 句上）

## 本轮机器化的收窄

舰队对表把缺口统一为命题 C（`∀σ` 的 D3 形状，`CG008FleetGap.MinimalGap`）。
本文件把 Z0 对 D3 的**实际需求**收窄到一个句子：

> **Z0 只需要 `𝗜𝚺₁ ⊢ zfcTr 𝐆 🡒 zfcTr (zfcTr 𝐆)` 这一条实例**，
> 其中 `𝐆 := gödel zfcTr` 是 `zfcTr` 的 Gödel 不动点句。

依据是 Foundation 第二定理证明的结构（`ProvabilityAbstraction/Basic.lean:224-262`）：
`con_unprovable` 经 `gödel_iff_con`，而 `gödel_iff_con` 里 `D3` **只用在一个句子**
（`formalized_unprovable_gödel` 的 `h₁ : T₀ ⊢ 𝔅 𝐆 🡒 𝔅 (𝔅 𝐆)`）。
本文件把这条依赖显式化：把 `[𝔅.HBL3]` 换成假设 `hD3`，其余证明逐行照抄。

## 两条等价的改写（都机器化在本文件里）

* `𝔅𝐆 → 𝔅(𝔅𝐆)` ⟺ `𝔅𝐆 → 𝔅⊥`（在 D1+D2 下）——
  所以单实例也可以读作「若 V 认为 𝗭𝗙𝗖 证明了 `translate 𝐆`，则 V 认为 𝗭𝗙𝗖 不一致」；
* 因此收窄后的目标可以写成**一条蕴含**，而不是整族 `∀σ`。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件的定理都是真证明（`rc=0`、无未证标记），可进收据。
- **不声称 C 已证**；`Z0Blocked.lean` 的未证标记仍在。本文件只**收窄目标**。 -/

section Abstract

variable {L : Language} [L.Encodable] [L.LORDefinable] [L.ReferenceableBy L]
  {T₀ T : Theory L} [Diagonalization T₀] {𝔅 : Provability T₀ T}

local notation "𝐆" => gödel 𝔅

/-- **单实例版 `formalized_consistent_of_existance_unprovable`**：只用 D1+D2
（Foundation 的版本在 `[𝔅.HBL]` 段内，本行显式降为 `[𝔅.HBL2]`，证明逐字相同）。 -/
theorem formalized_consistent_of_existance_unprovable_single [L.DecidableEq] [𝔅.HBL2]
    {σ : Sentence L} : T₀ ⊢ ∼𝔅 σ 🡒 𝔅.con := contra <| mdp Provability.D2 <| Provability.D1 efq

/-- **单实例版 `formalized_unprovable_gödel`**：把 `D3` 换成假设 `hD3`，其余逐行相同。

Foundation 原文（`ProvabilityAbstraction/Basic.lean:236`）的 `h₁` 是 `D3`；
这里它是假设。**这是本文件的核心：`D3` 只在这一个句子上被用到。** -/
theorem formalized_unprovable_gödel_single [L.DecidableEq] [T₀ ⪯ T] [𝔅.HBL2]
    (hD3 : T₀ ⊢ 𝔅 𝐆 🡒 𝔅 (𝔅 𝐆)) : T₀ ⊢ 𝔅.con 🡒 ∼𝔅 𝐆 := by
  suffices T₀ ⊢ ∼𝔅 ⊥ 🡒 ∼𝔅 𝐆 from this
  have h₁ : T₀ ⊢ 𝔅 𝐆 🡒 𝔅 (𝔅 𝐆) := hD3
  have h₂ : T₀ ⊢ 𝔅 𝐆 🡒 𝔅 (𝔅 𝐆 🡒 ⊥) := 𝔅.mono' <| by cl_prover [gödel_spec (T₀ := T₀)]
  have h₃ : T₀ ⊢ 𝔅 (𝔅 𝐆 🡒 ⊥) 🡒 𝔅 (𝔅 𝐆) 🡒 𝔅 ⊥ := Provability.D2
  cl_prover [h₁, h₂, h₃]

/-- **单实例版 `gödel_iff_con`**。 -/
theorem gödel_iff_con_single [L.DecidableEq] [T₀ ⪯ T] [𝔅.HBL2]
    (hD3 : T₀ ⊢ 𝔅 𝐆 🡒 𝔅 (𝔅 𝐆)) : T₀ ⊢ 𝐆 🡘 𝔅.con := by
  have h₁ : T₀ ⊢ ∼𝔅 𝐆 🡒 𝔅.con := formalized_consistent_of_existance_unprovable_single
  have h₂ : T₀ ⊢ 𝔅.con 🡒 ∼𝔅 𝐆 := formalized_unprovable_gödel_single hD3
  have h₃ : T₀ ⊢ 𝐆 🡘 ∼𝔅 𝐆 := gödel_spec
  cl_prover [h₁, h₂, h₃]

/-- **单实例版 `con_unprovable`**：第二定理只需要 Gödel 句上的那一条 D3 实例。 -/
theorem con_unprovable_single [L.DecidableEq] [T₀ ⪯ T] [Consistent T] [𝔅.HBL2]
    (hD3 : T₀ ⊢ 𝔅 𝐆 🡒 𝔅 (𝔅 𝐆)) : T ⊬ 𝔅.con := by
  intro h
  have : T₀ ⊢ 𝐆 🡘 𝔅.con := gödel_iff_con_single hD3
  have : T ⊢ 𝐆 := by cl_prover [h, this]
  exact unprovable_gödel this

/-- **等价改写之一**：单实例 `𝔅𝐆 → 𝔅(𝔅𝐆)` 与 `𝔅𝐆 → 𝔅⊥` 互相可导（在 D1+D2 下）。

所以单实例也可以读作「若 V 认为 𝗭𝗙𝗖 证明了 `translate 𝐆`，则 V 认为 𝗭𝗙𝗖 不一致」。 -/
theorem bew_gödel_iff_bew_bot [L.DecidableEq] [T₀ ⪯ T] [𝔅.HBL2]
    (hD3 : T₀ ⊢ 𝔅 𝐆 🡒 𝔅 (𝔅 𝐆)) : T₀ ⊢ 𝔅 𝐆 🡘 𝔅 ⊥ := by
  have h₂ : T₀ ⊢ 𝔅 𝐆 🡒 𝔅 (𝔅 𝐆 🡒 ⊥) := 𝔅.mono' <| by cl_prover [gödel_spec (T₀ := T₀)]
  have h₃ : T₀ ⊢ 𝔅 (𝔅 𝐆 🡒 ⊥) 🡒 𝔅 (𝔅 𝐆) 🡒 𝔅 ⊥ := Provability.D2
  have hf : T₀ ⊢ 𝔅 𝐆 🡒 𝔅 ⊥ := by cl_prover [hD3, h₂, h₃]
  have hb : T₀ ⊢ 𝔅 ⊥ 🡒 𝔅 𝐆 := 𝔅.mono' <| by cl_prover
  cl_prover [hf, hb]

/-- **等价改写之二（反向）**：`𝔅𝐆 → 𝔅⊥` 也足够给出单实例。 -/
theorem d3G_of_bew_gödel_imp_bew_bot [T₀ ⪯ T] [𝔅.HBL2]
    (h : T₀ ⊢ 𝔅 𝐆 🡒 𝔅 ⊥) : T₀ ⊢ 𝔅 𝐆 🡒 𝔅 (𝔅 𝐆) := by
  have : T₀ ⊢ 𝔅 ⊥ 🡒 𝔅 (𝔅 𝐆) := 𝔅.mono' <| by cl_prover
  cl_prover [h, this]

end Abstract

section ZFC

/-- **单实例版的 `sh_z0_full`**：`Sh ⊬ Con(𝗭𝗙𝗖)` 只需要 Gödel 句上的那一条 D3 实例。 -/
theorem sh_z0_full_of_single
    (hD3G : 𝗜𝚺₁ ⊢ zfcTr (gödel zfcTr) 🡒 zfcTr (zfcTr (gödel zfcTr))) :
    Sh ⊬ (𝗭𝗙𝗖.consistent : ArithmeticSentence) := by
  intro h
  have e : Sh ⊢ zfcTr.con 🡘 (𝗭𝗙𝗖.consistent : ArithmeticSentence) :=
    WeakerThan.pbl zfcTr_con_iff
  have hc : Sh ⊢ zfcTr.con := by cl_prover [e, h]
  exact con_unprovable_single (𝔅 := zfcTr) hD3G hc

/-- **单实例版的 `zfc_z0_full`**：Z0 完整形式只需要 Gödel 句上的那一条 D3 实例。 -/
theorem zfc_z0_full_of_single
    (hD3G : 𝗜𝚺₁ ⊢ zfcTr (gödel zfcTr) 🡒 zfcTr (zfcTr (gödel zfcTr))) :
    𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent : ArithmeticSentence) :=
  fun h ↦ sh_z0_full_of_single hD3G ((Sh_provable_iff _).mpr h)

/-- **单实例的 C 形状 ⟹ 语法形状**（经 `complete`）：把收窄目标写成与 `MinimalGap`
同款的语义蕴含（只是 `σ` 固定为 `gödel zfcTr`）。 -/
theorem single_syntactic_of_single_semantic
    (h : ∀ (V : Type) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁],
      Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (gödel zfcTr)⌝ : V) →
      Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr (gödel zfcTr))⌝ : V)) :
    𝗜𝚺₁ ⊢ zfcTr (gödel zfcTr) 🡒 zfcTr (zfcTr (gödel zfcTr)) := by
  apply complete 𝗜𝚺₁ _
  intro V hV1 hV2
  apply Semantics.Imp.models_imply.mpr
  intro hp
  exact (models_zfcTr_iff V (zfcTr (gödel zfcTr))).mpr
    (h V ((models_zfcTr_iff V (gödel zfcTr)).mp hp))

/-- **`MinimalGap`（= 舰队命题 C）⟹ 单实例目标**：C 蕴含收窄后的目标（显然，
但把两条线的接口钉住）。 -/
theorem single_of_minimalGap (h : GodelQ.CG008FleetGap.MinimalGap) :
    𝗜𝚺₁ ⊢ zfcTr (gödel zfcTr) 🡒 zfcTr (zfcTr (gödel zfcTr)) :=
  single_syntactic_of_single_semantic fun V _ _ ↦ h V (gödel zfcTr)

end ZFC

end GodelQ.CG008SingleInstance

#print axioms GodelQ.CG008SingleInstance.con_unprovable_single
#print axioms GodelQ.CG008SingleInstance.zfc_z0_full_of_single
#print axioms GodelQ.CG008SingleInstance.single_of_minimalGap
