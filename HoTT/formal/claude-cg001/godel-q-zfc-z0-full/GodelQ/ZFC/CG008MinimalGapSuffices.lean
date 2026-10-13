import GodelQ.ZFC.CG008FleetGap
import GodelQ.ZFC.Z0Full

/-!
# CG-008 · `MinimalGap`（= 舰队对表项 C）**对 `hD3G` 是充分的**

002-Step 提出：C 是**必要不充分**，完整 `hD3G` 还需 `ring_step3`
（V 内 → 元层 `𝗭𝗙𝗖 ⊢ …`），理由是「`zfcTr.D1` 要元层 `Sh ⊢ (zfcTr σ)`」。

**本文件机器化地回答：那条额外的步，只有在他那条路线上才需要。**

## 两条路线的差别

| 路线 | 做法 | 是否需要 V→元层 |
|---|---|---|
| **元层环**（002-Step） | 从 `V ⊧ zfcTr σ` 一路推到元层 `Sh ⊢ (zfcTr σ)`，再喂 `zfcTr.D1` | **需要**（`ring_step3`） |
| **模型论直证**（本文件） | `HBL3` 是 **𝗜𝚺₁ 内**的命题 `∀σ, 𝗜𝚺₁ ⊢ zfcTr σ 🡒 zfcTr (zfcTr σ)`；用 `complete 𝗜𝚺₁`（语义完备性）在每个模型 V 里验证它即可 | **不需要** |

`models_zfcTr_iff`（`Z0Full.lean:67`）是 **↔**，两端都是 V 内部的
`Provable 𝗭𝗙𝗖 (⌜·⌝ : V)`。所以在每个模型内，C 直接把
「`Provable 𝗭𝗙𝗖 ⌜translate σ⌝`」变成「`Provable 𝗭𝗙𝗖 ⌜translate (zfcTr σ)⌝`」，
再经同一个 ↔ 回到 `V ⊧ zfcTr (zfcTr σ)`。**全程不出 V，不需要 `ring_step3`。**

## 结论

- `hbl3_of_minimalGap`：`MinimalGap ⟹ zfcTr.HBL3`（整族 D3）；
- `hD3G_of_minimalGap`：`MinimalGap ⟹ hD3G`（单句实例，就是 Z0 链条要的那一条）。

**所以 C 对 `hD3G` 充分**（经模型论路线）。002-Step 的 `ring_step3` 是他那条
**元层环**路线的额外负担，不是 C 本身的缺口。

这不是争论——`hbl3_of_minimalGap` 与 `hD3G_of_minimalGap` 都是编译通过的真实定理。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含未证标记，可进入收据。
- **不声称 C 已证**；`Z0Blocked.lean:65` 的未证标记仍在。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008MinimalGapSuffices

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Z0Full GodelQ.Translate
open ProvabilityAbstraction (gödel)

variable {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`MinimalGap` ⟹ `zfcTr.HBL3`（整族 D3）**。

照 `Z0Full.zfc_z0_full_of_D3_internalize`（`Z0Full.lean:117`）证明内部的同一构造：
`HBL3` 是 𝗜𝚺₁ 内的命题，用 `complete 𝗜𝚺₁` 在每个模型 V 里验证；
模型内的两步都是 `models_zfcTr_iff`（↔）的改写，**不出 V**。 -/
theorem hbl3_of_minimalGap (h : GodelQ.CG008FleetGap.MinimalGap) : zfcTr.HBL3 := by
  refine ⟨fun {σ} ↦ ?_⟩
  apply complete 𝗜𝚺₁ _
  intro V hV1 hV2
  apply Semantics.Imp.models_imply.mpr
  intro hp
  have hout : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr σ)⌝ : V) :=
    @h V _ _ σ ((models_zfcTr_iff V σ).mp hp)
  exact (models_zfcTr_iff V (zfcTr σ)).mpr hout

/-- **`MinimalGap` ⟹ `hD3G`**（单句实例，Z0 链条要的那一条）。

`hD3G` 的形状是 `𝗜𝚺₁ ⊢ zfcTr 𝐆 🡒 zfcTr (zfcTr 𝐆)`，`𝐆 := gödel zfcTr`。
它是 `HBL3.D3` 在 `σ := 𝐆` 的实例——**所以 C 直接给出它，无需 `ring_step3`**。 -/
theorem hD3G_of_minimalGap (h : GodelQ.CG008FleetGap.MinimalGap) :
    𝗜𝚺₁ ⊢ zfcTr (gödel (T₀ := 𝗜𝚺₁) zfcTr) 🡒
      zfcTr (zfcTr (gödel (T₀ := 𝗜𝚺₁) zfcTr)) := by
  letI : zfcTr.HBL3 := hbl3_of_minimalGap h
  exact Provability.D3 (𝔅 := zfcTr) (σ := gödel (T₀ := 𝗜𝚺₁) zfcTr)

/-- **一致性核对**：`MinimalGap ⟹ Z0` 与 `z0_of_minimalGap` 是同一条
（本行只是把已有的那条再引一次，确认两者不冲突）。 -/
theorem z0_again (h : GodelQ.CG008FleetGap.MinimalGap) :
    𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent : ArithmeticSentence) :=
  GodelQ.CG008FleetGap.z0_of_minimalGap h

end GodelQ.CG008MinimalGapSuffices

#print axioms GodelQ.CG008MinimalGapSuffices.hbl3_of_minimalGap
#print axioms GodelQ.CG008MinimalGapSuffices.hD3G_of_minimalGap
#print axioms GodelQ.CG008MinimalGapSuffices.z0_again
