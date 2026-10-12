import GodelQ.ZFC.CG008RedoActual

/-!
# CG-008 · 抽象层重做：把 `D3` 换成单句假设（`𝔅` 保持为变量）

## 为什么走这条

`CG008RedoActual.lean` 实测：把 `𝔅` 具体化成 `zfcTr` 后，
Lean 在 `zfcTr` 的定义上展开爆炸（`rc=-9`）。
**Foundation 自己的写法能编译**，因为那里 `𝔅` 是**变量**，不展开。

**所以本文件在抽象层重做**——对任意 `𝔅 : Provability T₀ T` + `[𝔅.HBL2]` 等，
把 `formalized_unprovable_gödel` 里唯一用 `D3` 的那一步换成单句假设。
最后再实例化到 `zfcTr`（实例化那一步不展开 `𝔅`，所以安全）。

## 要证的（抽象版）

```
hD3G : T₀ ⊢ 𝔅 𝐆 🡒 𝔅 (𝔅 𝐆)          𝐆 := gödel 𝔅
⟹ T₀ ⊢ 𝔅.con 🡒 ∼𝔅 𝐆
```

**这与 Foundation 的 `formalized_unprovable_gödel` 只差 `h₁` 的来源**：
原文用 `D3`（需 `[𝔅.HBL3]`），本文件用 `hD3G`（只需单句）。

## 治理

- Foundation 只读；本文件纯下游。
- 若成功则无未证标记、可进收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008AbstractRedo

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

open ProvabilityAbstraction (gödel gödel_spec)

set_option linter.unusedSectionVars false

variable {L : Language} [L.ReferenceableBy L]
  {T₀ T : Theory L} [Diagonalization T₀] [T₀ ⪯ T]
  {𝔅 : Provability T₀ T}

/-- **主结果（抽象层重做）**：把 `formalized_unprovable_gödel` 里唯一用 `D3` 的那一步
换成**单句假设** `hD3G`。

**注意**：这里 `𝔅` 是**变量**——正是 Foundation 的写法，也是能编译的原因。
`[𝔅.HBL2]` 提供 `D2` 与 `Mono`（`Basic.lean:134` 的实例）。 -/
theorem formalized_unprovable_gödel_single [𝔅.HBL2]
    (hD3G : T₀ ⊢ 𝔅 (gödel 𝔅) 🡒 𝔅 (𝔅 (gödel 𝔅))) :
    T₀ ⊢ 𝔅.con 🡒 ∼𝔅 (gödel 𝔅) := by
  suffices T₀ ⊢ ∼𝔅 ⊥ 🡒 ∼𝔅 (gödel 𝔅) from this
  have h₁ : T₀ ⊢ 𝔅 (gödel 𝔅) 🡒 𝔅 (𝔅 (gödel 𝔅)) := hD3G
  have h₂ : T₀ ⊢ 𝔅 (gödel 𝔅) 🡒 𝔅 (𝔅 (gödel 𝔅) 🡒 ⊥) :=
    𝔅.mono' <| by cl_prover [gödel_spec (𝔅 := 𝔅)]
  have h₃ : T₀ ⊢ 𝔅 (𝔅 (gödel 𝔅) 🡒 ⊥) 🡒 𝔅 (𝔅 (gödel 𝔅)) 🡒 𝔅 ⊥ :=
    Provability.D2 (𝔅 := 𝔅)
  cl_prover [h₁, h₂, h₃]

end GodelQ.CG008AbstractRedo

-- 公理洁净检查
#print axioms GodelQ.CG008AbstractRedo.formalized_unprovable_gödel_single
