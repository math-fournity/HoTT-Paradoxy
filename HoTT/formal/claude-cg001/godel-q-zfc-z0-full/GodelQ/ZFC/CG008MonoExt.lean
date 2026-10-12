import GodelQ.ZFC.CG008ConRedo

/-!
# CG-008 · 更正：`zfcTr.Mono` **不需要**新建——Foundation 已从 `HBL2` 推出

## 本文件原本想做的事，以及为什么它多余

我原本以为 `zfcTr` 缺 `Mono` 实例（`CG008ConRedo.lean` 的前置查实里 grep 了
本包目录，没找到）。**那个 grep 是错的**——它只查了本包，
而 `Mono` 实例在 **Foundation 里**（`ProvabilityAbstraction/Basic.lean:134`）：

```lean
instance [𝔅.HBL2] : 𝔅.Mono := ⟨fun h => bew_distribute_imply <| D1 h⟩
instance [𝔅.HBL2] : 𝔅.Ext  := ⟨fun h => E_intro (mono (K_left h)) (mono (K_right h))⟩
```

而 `zfcTr.HBL2` **已建成**（`Z0Full.lean:72`）。
**所以 `zfcTr.Mono` 与 `zfcTr.Ext` 一直是可推导的**——
`CG008MonoCheck.lean` 用一行 `inferInstance` 机器确认了这一点。

**本文件下面的实例是冗余的**，但保留它作为**一次自我更正的可查记录**：
它证明了我原来的 grep 方法（只查本包）会漏掉 Foundation 侧的实例。

## 教训

**查「某实例是否存在」时，不能只 grep 本包**——必须 `inferInstance` 或
`#synth` 让 Lean 实际去合成，或 grep Foundation 源码。
本会话在探针 15（`Sh.Δ₁`）与探针 23（`Sh.craig.Δ₁`）上用的是**正确**方法
（编译试探），唯独 `Mono` 这一步退回了 grep。

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

/-- **查实 1（决定性）**：`zfcTr.Mono` **可从已有的 `HBL2` 推出**——
Foundation 的实例（`Basic.lean:134`）加上 `zfcTr_HBL2`（`Z0Full.lean:72`）。 -/
example : zfcTr.Mono := inferInstance

/-- **查实 2**：`zfcTr.Ext` 同样可得。 -/
example : zfcTr.Ext := inferInstance

/-- **（冗余，保留作更正记录）**：手写的 `zfcTr.Mono`。

本实例**非必需**——上一行 `inferInstance` 已能合成。
保留它作为「我原来的 grep 方法漏了 Foundation 侧实例」的可查证据。 -/
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
