import GodelQ.ZFC.CG008ConRedo

/-!
# CG-008 · 为 `zfcTr` 补 `Mono` 与 `Ext`（重做 `con_unprovable` 的前置）

## 为什么需要

`CG008ConRedo.lean` 查实：`con_unprovable` 的证明链里，
**只有一步**用到 `D3`（在固定句 `𝐆` 上）。
要把它换成单句假设，其余步骤必须仍可用，其中：

```lean
h₂ : T₀ ⊢ 𝔅 𝐆 🡒 𝔅 (𝔅 𝐆 🡒 ⊥) := 𝔅.mono' <| by cl_prover [gödel_spec]
```

**`𝔅.mono'` 需要 `[𝔅.Mono]`**——而 `zfcTr` **没有** `Mono` 实例（本探针的前置查实）。

## 本文件要做的

补上 `zfcTr.Mono` 与 `zfcTr.Ext`。

**做法照 `zfcTr_HBL2` 的模式**（`Z0Full.lean:71-75`）：

```lean
instance zfcTr_HBL2 : zfcTr.HBL2 := ⟨fun {σ τ} ↦ complete 𝗜𝚺₁ _ fun (V : Type) _ _ ↦ by
  rw [..., models_zfcTr_iff, ..., LogicalConnective.HomClass.map_imply]
  exact modus_ponens_sentence (T := 𝗭𝗙𝗖)⟩
```

即：`complete 𝗜𝚺₁`（在 𝗜𝚺₁ 的每个模型里验证）+ `models_zfcTr_iff` 翻译 + 元层的 `𝗭𝗙𝗖` 事实。

**`Mono` 的内容**：`𝗭𝗙𝗖 ⊢ σ 🡒 τ → 𝗜𝚺₁ ⊢ zfcTr σ 🡒 zfcTr τ`。
在模型里：`zfcTr σ` 即「𝗭𝗙𝗖 证明 `translate σ`」，
而 𝗭𝗙𝗖 对蕴含封闭（`modus_ponens_sentence`）。

## 治理

- Foundation 只读；本文件纯下游。
- 若成功则无未证标记、可进收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008MonoExt

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.CG008HBL3
  GodelQ.CG008HBL3Test GodelQ.CG008Final GodelQ.CG008Probe15 GodelQ.CG008Probe16
  GodelQ.CG008Probe17 GodelQ.CG008Probe18 GodelQ.CG008Probe19 GodelQ.CG008Probe20
  GodelQ.CG008Delta1Wall GodelQ.CG008Probe21 GodelQ.CG008CrossLanguage
  GodelQ.CG008InterpretationWall GodelQ.CG008Probe22 GodelQ.CG008Probe23
  GodelQ.CG008CraigRoute GodelQ.CG008CraigBridge GodelQ.CG008PureArith
  GodelQ.CG008Probe24 GodelQ.CG008Probe25 GodelQ.CG008Correction
  GodelQ.CG008Rosser GodelQ.CG008InternalInduction GodelQ.CG008SingleD3
  GodelQ.CG008SingleD3Attack GodelQ.CG008BridgeAnatomy GodelQ.CG008SingleD3Theorem
  GodelQ.CG008ConRedo

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **主结果**：`zfcTr` 的 `Mono` 实例。

`Sh ⊢ σ 🡒 τ → 𝗜𝚺₁ ⊢ zfcTr σ 🡒 zfcTr τ`。

在模型里：`zfcTr σ` 即 `Provable 𝗭𝗙𝗖 ⌜translate σ⌝`（`V` 上的报价）。
`h : Sh ⊢ σ 🡒 τ` 经 `Sh_provable_iff` 给 `𝗭𝗙𝗖 ⊢ translate (σ 🡒 τ)`，
再由 `arithTrln` 的同态性拆成 `translate σ 🡒 translate τ`，
最后由 `internalize_provability`（D1，对任意 `T : Theory L` + `[T.Δ₁]`）
把它抬成 V 上的 `Provable`，再 `modus_ponens_sentence`。 -/
instance zfcTr_Mono : zfcTr.Mono := ⟨fun {σ τ} h ↦ complete 𝗜𝚺₁ _ fun (V : Type) _ _ ↦ by
  rw [Semantics.Imp.models_imply, models_zfcTr_iff, models_zfcTr_iff]
  have h' : 𝗭𝗙𝗖 ⊢ (arithTrln.translate (σ 🡒 τ) : SetTheorySentence) :=
    (Sh_provable_iff (σ 🡒 τ)).mp h
  rw [LogicalConnective.HomClass.map_imply] at h'
  have hV : Provable 𝗭𝗙𝗖 (⌜(arithTrln.translate σ 🡒 arithTrln.translate τ :
      SetTheorySentence)⌝ : V) := internalize_provability (V := V) h'
  intro hp
  exact modus_ponens_sentence (T := 𝗭𝗙𝗖) (L := ℒₛₑₜ) (V := V)
    (σ := arithTrln.translate σ) (τ := arithTrln.translate τ) hV hp⟩

end GodelQ.CG008MonoExt

-- 公理洁净检查（收据要求）
#print axioms GodelQ.CG008MonoExt.zfcTr_Mono
