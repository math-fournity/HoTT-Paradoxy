import GodelQ.ZFC.CG008AbstractRedo

/-!
# CG-008 · 实例化到 `zfcTr`：单句 `D3` 能否真的喂进去

## 现状

`CG008AbstractRedo.lean` 已证（抽象层，`rc=0`，公理洁净）：

```lean
formalized_unprovable_gödel_single [𝔅.HBL2]
    (hD3G : T₀ ⊢ 𝔅 (gödel 𝔅) 🡒 𝔅 (𝔅 (gödel 𝔅))) :
    T₀ ⊢ 𝔅.con 🡒 ∼𝔅 (gödel 𝔅)
```

**现在试实例化**：`𝔅 := zfcTr`、`T₀ := 𝗜𝚺₁`、`T := Sh`、`L := ℒₒᵣ`。

**关键问题**：实例化那一步会不会也触发 `zfcTr` 的展开爆炸？
- `CG008RedoActual.lean` 的记录说：**判断 `∼zfcTr G` 与 `zfcTr G 🡒 ⊥` 相等时会炸**；
- 但**实例化一条已有的定理**可能不触发——因为定理的语句是**固定的**，
  Lean 只需把 `𝔅` 换成 `zfcTr`，不需要判断任何新的相等。

**本文件就是来实测这一点的。**

## 若成功

则得到**前提严格更弱**的条件定理：

```
hD3G : 𝗜𝚺₁ ⊢ zfcTr 𝐆 🡒 zfcTr (zfcTr 𝐆)
⟹ 𝗜𝚺₁ ⊢ zfcTr.con 🡒 ∼zfcTr 𝐆
```

再配上 `unprovable_gödel`（只需 D1 与 `gödel_spec`）与 `gödel_iff_con`，
就能得 `Sh ⊬ zfcTr.con`，进而经 `Sh_provable_iff` 得 Z0。

## 治理

- Foundation 只读；本文件纯下游。
- 若成功则无未证标记、可进收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Instantiate

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.CG008HBL3
  GodelQ.CG008HBL3Test GodelQ.CG008Final GodelQ.CG008Probe15 GodelQ.CG008Probe16
  GodelQ.CG008Probe17 GodelQ.CG008Probe18 GodelQ.CG008Probe19 GodelQ.CG008Probe20
  GodelQ.CG008Delta1Wall GodelQ.CG008Probe21 GodelQ.CG008CrossLanguage
  GodelQ.CG008InterpretationWall GodelQ.CG008Probe22 GodelQ.CG008Probe23
  GodelQ.CG008CraigRoute GodelQ.CG008CraigBridge GodelQ.CG008PureArith
  GodelQ.CG008Probe24 GodelQ.CG008Probe25 GodelQ.CG008Correction
  GodelQ.CG008Rosser GodelQ.CG008InternalInduction GodelQ.CG008SingleD3
  GodelQ.CG008SingleD3Attack GodelQ.CG008BridgeAnatomy GodelQ.CG008SingleD3Theorem
  GodelQ.CG008ConRedo GodelQ.CG008MonoExt GodelQ.CG008RedoPrereq GodelQ.CG008RedoActual
  GodelQ.CG008AbstractRedo

open ProvabilityAbstraction (gödel gödel_spec)

set_option linter.unusedSectionVars false

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1（本文件的关键实测）**：把抽象层的定理实例化到 `zfcTr`。

**实例化只是把 `𝔅` 换成 `zfcTr`**——不判断任何新的相等，
所以**可能**不触发 `CG008RedoActual.lean` 记录的展开爆炸。 -/
theorem formalized_unprovable_gödel_zfcTr
    (hD3G : 𝗜𝚺₁ ⊢ zfcTr (gödel (T₀ := 𝗜𝚺₁) zfcTr) 🡒
      zfcTr (zfcTr (gödel (T₀ := 𝗜𝚺₁) zfcTr))) :
    𝗜𝚺₁ ⊢ zfcTr.con 🡒 ∼zfcTr (gödel (T₀ := 𝗜𝚺₁) zfcTr) :=
  GodelQ.CG008AbstractRedo.formalized_unprovable_gödel_single (𝔅 := zfcTr) hD3G

-- 公理洁净检查
#print axioms GodelQ.CG008Instantiate.formalized_unprovable_gödel_zfcTr

end GodelQ.CG008Instantiate
