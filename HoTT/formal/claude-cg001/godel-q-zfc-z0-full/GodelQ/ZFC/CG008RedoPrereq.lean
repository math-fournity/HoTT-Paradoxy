import GodelQ.ZFC.CG008MonoExt

/-!
# CG-008 · 重做 `con_unprovable` 的**真实**前置清单（用合成而非 grep）

## 教训的应用

上一个单元我因为只 grep 本包而误判 `zfcTr.Mono` 缺失。
本文件用**合成试探**（`inferInstance`）把重做所需的**全部**类型类逐条查实。

## `formalized_unprovable_gödel` 的依赖（`Basic.lean:245-252`）

```lean
theorem formalized_unprovable_gödel : T₀ ⊢ 𝔅.con 🡒 ∼𝔅 𝐆 := by
  have h₁ : T₀ ⊢ 𝔅 𝐆 🡒 𝔅 (𝔅 𝐆) := D3                     -- ← 唯一用 D3
  have h₂ : T₀ ⊢ 𝔅 𝐆 🡒 𝔅 (𝔅 𝐆 🡒 ⊥) := 𝔅.mono' <| ...    -- 需 [𝔅.Mono]
  have h₃ : T₀ ⊢ 𝔅 (𝔅 𝐆 🡒 ⊥) 🡒 𝔅 (𝔅 𝐆) 🡒 𝔅 ⊥ := D2       -- 需 [𝔅.HBL2]
  cl_prover [h₁, h₂, h₃]
```

**`gödel_iff_con`** 还用到 `formalized_consistent_of_existance_unprovable`（需 `HBL2`、`D1`）
与 `gödel_spec`（需 `Diagonalization`）。

**`con_unprovable`** 还用到 `unprovable_gödel`（需 `D1`、`gödel_spec`）。

## 本文件查实

对 `𝔅 := zfcTr`、`T₀ := 𝗜𝚺₁`、`T := Sh`、`L := ℒₒᵣ`，
上述每一个类型类是否**可合成**。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008RedoPrereq

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.CG008HBL3
  GodelQ.CG008HBL3Test GodelQ.CG008Final GodelQ.CG008Probe15 GodelQ.CG008Probe16
  GodelQ.CG008Probe17 GodelQ.CG008Probe18 GodelQ.CG008Probe19 GodelQ.CG008Probe20
  GodelQ.CG008Delta1Wall GodelQ.CG008Probe21 GodelQ.CG008CrossLanguage
  GodelQ.CG008InterpretationWall GodelQ.CG008Probe22 GodelQ.CG008Probe23
  GodelQ.CG008CraigRoute GodelQ.CG008CraigBridge GodelQ.CG008PureArith
  GodelQ.CG008Probe24 GodelQ.CG008Probe25 GodelQ.CG008Correction
  GodelQ.CG008Rosser GodelQ.CG008InternalInduction GodelQ.CG008SingleD3
  GodelQ.CG008SingleD3Attack GodelQ.CG008BridgeAnatomy GodelQ.CG008SingleD3Theorem
  GodelQ.CG008ConRedo GodelQ.CG008MonoExt

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1**：`zfcTr.HBL2` 可合成——`D2` 与 `bew_distribute_imply` 的基础。 -/
noncomputable example : zfcTr.HBL2 := inferInstance

/-- **查实 2**：`zfcTr.Mono` 可合成（由 `HBL2` 自动给出）。 -/
noncomputable example : zfcTr.Mono := inferInstance

/-- **查实 3**：`Diagonalization 𝗜𝚺₁` 可合成——`𝐆 := gödel zfcTr` 的基础。 -/
noncomputable example : Diagonalization 𝗜𝚺₁ := inferInstance

/-- **查实 4**：`𝐆` 可构造。 -/
noncomputable example : Sentence ℒₒᵣ := gödel (T₀ := 𝗜𝚺₁) zfcTr

/-- **查实 5**：`gödel_spec` 对 `zfcTr` 可用——`𝗜𝚺₁ ⊢ 𝐆 🡘 ∼zfcTr 𝐆`。 -/
example : 𝗜𝚺₁ ⊢ (gödel (T₀ := 𝗜𝚺₁) zfcTr) 🡘 ∼zfcTr (gödel (T₀ := 𝗜𝚺₁) zfcTr) :=
  gödel_spec (𝔅 := zfcTr)

/-- **查实 6（本文件的结论）**：重做所需的前置**全部可合成**——
`HBL2`、`Mono`、`Diagonalization`、`gödel_spec`。
**唯一缺的仍是 `D3`**，而它正是要替换成单句假设的那一步。

**所以重做在类型层没有障碍**；剩下的工作是把 `formalized_unprovable_gödel`、
`gödel_iff_con`、`con_unprovable`、`unprovable_gödel` 四条在本包内重写。 -/
example : True := trivial

end GodelQ.CG008RedoPrereq
