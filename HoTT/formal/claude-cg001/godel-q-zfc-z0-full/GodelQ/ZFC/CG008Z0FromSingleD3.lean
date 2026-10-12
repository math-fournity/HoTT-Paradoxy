import GodelQ.ZFC.CG008Instantiate

/-!
# CG-008 · 从**单句 `D3`** 到 **Z0**：完整链条

## 目标

```
hD3G : 𝗜𝚺₁ ⊢ zfcTr 𝐆 🡒 zfcTr (zfcTr 𝐆)          𝐆 := gödel (T₀ := 𝗜𝚺₁) zfcTr
⟹ 𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent)
```

## 链条（照 Foundation 的 `con_unprovable` 链，只换 `D3` 那一步）

| 步 | Foundation 原文 | 本文件 |
|---|---|---|
| 1 | `formalized_unprovable_gödel`（用 `D3 @ 𝐆`） | ✅ `CG008Instantiate` 已给（用 `hD3G`） |
| 2 | `formalized_consistent_of_existance_unprovable`（只用 D2、D1） | 需实例化 |
| 3 | `gödel_iff_con` | 需实例化 |
| 4 | `unprovable_gödel`（只用 D1、`gödel_spec`） | 需实例化 |
| 5 | `con_unprovable [Consistent T]` | 需重做 |
| 6 | 经 `Sh_provable_iff` 到 Z0 完整形式 | 需重做 |

**第 2、4 步的抽象版本不依赖 `D3`**，所以可以**直接用 Foundation 的定理**（它们取 `[𝔅.HBL]`，而
`[𝔅.HBL] = HBL2 + HBL3`——**这一步要小心**：Foundation 的版本取 `HBL`，
而我们只有 `HBL2`。所以第 2、4 步也要在抽象层重做，去掉 `HBL3` 的依赖）。

**本文件先做第 2 步**（最小、只依赖 D2/D1），确认抽象层重做 + 实例化的方法可行。

## 治理

- Foundation 只读；本文件纯下游。
- 若成功则无未证标记、可进收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Z0FromSingleD3

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
  GodelQ.CG008AbstractRedo GodelQ.CG008Instantiate

open ProvabilityAbstraction (gödel gödel_spec)

set_option linter.unusedSectionVars false
set_option maxHeartbeats 800000

variable {L : Language} [L.DecidableEq] [L.ReferenceableBy L]
  {T₀ T : Theory L} [Diagonalization T₀] [T₀ ⪯ T]
  {𝔅 : Provability T₀ T}

/-- **第 2 步（抽象层重做）**：`formalized_consistent_of_existance_unprovable`。

Foundation 原文（`Basic.lean:237`）：

```lean
omit [Diagonalization T₀] in
lemma formalized_consistent_of_existance_unprovable [L.DecidableEq] {σ : Sentence L} :
    T₀ ⊢ ∼𝔅 σ 🡒 𝔅.con := contra <| mdp D2 <| D1 efq
```

**它只用 `D2` 与 `D1`——不需要 `D3`**，所以理论上可直接用。
但 Foundation 的版本在 `[𝔅.HBL]` 的 section 里，故本文件在 `[𝔅.HBL2]` 下重做。 -/
theorem formalized_consistent_of_existance_unprovable' [𝔅.HBL2] {σ : Sentence L} :
    T₀ ⊢ ∼𝔅 σ 🡒 𝔅.con :=
  contra <| mdp (Provability.D2 (𝔅 := 𝔅)) <| Provability.D1 (𝔅 := 𝔅) efq

/-- **第 3 步（抽象层重做）**：`gödel_iff_con`。

Foundation 原文（`Basic.lean:254-260`）：

```lean
theorem gödel_iff_con : T₀ ⊢ 𝐆 🡘 𝔅.con := by
  have h₁ : T₀ ⊢ ∼𝔅 𝐆 🡒 𝔅.con := formalized_consistent_of_existance_unprovable
  have h₂ : T₀ ⊢ 𝔅.con 🡒 ∼𝔅 𝐆 := formalized_unprovable_gödel
  have h₃ : T₀ ⊢ 𝐆 🡘 ∼𝔅 𝐆 := gödel_spec
  cl_prover [h₁, h₂, h₃];
```

**`h₂` 是唯一用到 `D3` 的地方**（经 `formalized_unprovable_gödel`）。
本行把它换成 `hD3G` 的产物（`CG008AbstractRedo` 的定理）。 -/
theorem gödel_iff_con' [𝔅.HBL2]
    (hD3G : T₀ ⊢ 𝔅 (gödel 𝔅) 🡒 𝔅 (𝔅 (gödel 𝔅))) :
    T₀ ⊢ gödel 𝔅 🡘 𝔅.con := by
  have h₁ : T₀ ⊢ ∼𝔅 (gödel 𝔅) 🡒 𝔅.con :=
    formalized_consistent_of_existance_unprovable' (𝔅 := 𝔅)
  have h₂ : T₀ ⊢ 𝔅.con 🡒 ∼𝔅 (gödel 𝔅) :=
    GodelQ.CG008AbstractRedo.formalized_unprovable_gödel_single (𝔅 := 𝔅) hD3G
  have h₃ : T₀ ⊢ gödel 𝔅 🡘 ∼𝔅 (gödel 𝔅) := gödel_spec (𝔅 := 𝔅)
  cl_prover [h₁, h₂, h₃]

/-- **第 4 步（抽象层重做）**：`unprovable_gödel`。

Foundation 原文（`Basic.lean:202-210`）：

```lean
theorem unprovable_gödel : T ⊬ (gödel 𝔅) := by
  intro h
  have h₁ : T ⊢ 𝔅 (gödel 𝔅) := WeakerThan.pbl <| D1 h
  have h₂ : T ⊢ (gödel 𝔅) 🡘 ∼𝔅 (gödel 𝔅) := WeakerThan.pbl <| gödel_spec
  have : T ⊢ ⊥ := by cl_prover [h₁, h₂, h]
  ...
```

**只用 `D1` 与 `gödel_spec`——不需要 `D3`**。
Foundation 的版本在 `[Consistent T]` 的 section 里，本行原样重做（只需 `D1`）。 -/
theorem unprovable_gödel' [Consistent T] : T ⊬ (gödel 𝔅) := by
  intro h
  have h₁ : T ⊢ 𝔅 (gödel 𝔅) := WeakerThan.pbl <| Provability.D1 (𝔅 := 𝔅) h
  have h₂ : T ⊢ (gödel 𝔅) 🡘 ∼𝔅 (gödel 𝔅) := WeakerThan.pbl <| gödel_spec (𝔅 := 𝔅)
  have : T ⊢ ⊥ := by cl_prover [h₁, h₂, h]
  have : ¬Consistent T :=
    not_consistent_iff_inconsistent.mpr <| inconsistent_iff_provable_bot.mpr this
  contradiction

/-- **第 5 步（抽象层重做）**：`con_unprovable`。

Foundation 原文（`Basic.lean:259-264`）：

```lean
theorem con_unprovable [Consistent T] : T ⊬ 𝔅.con := by
  intro h
  have : T₀ ⊢ 𝐆 🡘 𝔅.con := gödel_iff_con
  have : T ⊢ 𝐆 := by cl_prover [h, this]
  exact unprovable_gödel this
```

**只经 `gödel_iff_con` 用到 `D3`**——本行用第 3 步的版本。 -/
theorem con_unprovable' [𝔅.HBL2] [Consistent T]
    (hD3G : T₀ ⊢ 𝔅 (gödel 𝔅) 🡒 𝔅 (𝔅 (gödel 𝔅))) :
    T ⊬ 𝔅.con := by
  intro h
  have : T₀ ⊢ gödel 𝔅 🡘 𝔅.con := gödel_iff_con' (𝔅 := 𝔅) hD3G
  have : T ⊢ gödel 𝔅 := by cl_prover [h, this]
  exact unprovable_gödel' (𝔅 := 𝔅) this

/-! ## 第 6 步：实例化到 `zfcTr`，得 Z0 -/

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **第 6 步（本文件的主结果）**：从**单句 `D3`** 得 `Sh ⊬ zfcTr.con`。

这是 `CG008AbstractRedo` + `CG008Instantiate` 的收获：
抽象层重做（`𝔅` 保持变量，不展开）**加上**实例化（只替换，不判断新的相等）
——两半合起来把 `D3` 的**模式**需求降到**一条实例**。 -/
theorem sh_con_unprovable_of_single_D3
    (hD3G : 𝗜𝚺₁ ⊢ zfcTr (gödel (T₀ := 𝗜𝚺₁) zfcTr) 🡒
      zfcTr (zfcTr (gödel (T₀ := 𝗜𝚺₁) zfcTr)))
    [Consistent Sh] :
    Sh ⊬ zfcTr.con :=
  con_unprovable' (𝔅 := zfcTr) hD3G

/-- **第 6 步的完整形式（Z0）**：从**单句 `D3`** 得 Z0 的完整形式。

**对照** `Z0Full.sh_z0_full`：它取 `[zfcTr.HBL3]`（**模式**），
本定理取一条 `hD3G`（**实例**）——前提严格更弱。

结构照抄 `Z0Full.sh_z0_full` 与 `zfc_z0_full`，只把 `con_unprovable` 换成
`con_unprovable'`（第 5 步的重做版）。 -/
theorem zfc_z0_of_single_D3
    (hD3G : 𝗜𝚺₁ ⊢ zfcTr (gödel (T₀ := 𝗜𝚺₁) zfcTr) 🡒
      zfcTr (zfcTr (gödel (T₀ := 𝗜𝚺₁) zfcTr)))
    [Consistent Sh] :
    𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent : ArithmeticSentence) := by
  intro h
  -- `h : 𝗭𝗙𝗖 ⊢ translate consistent`，经 `Sh_provable_iff` 得 `Sh ⊢ consistent`
  have hSh : Sh ⊢ (𝗭𝗙𝗖.consistent : ArithmeticSentence) :=
    (Sh_provable_iff _).mpr h
  -- 与 `Z0Full.sh_z0_full` 同构：`Sh ⊢ zfcTr.con`，再由 `con_unprovable'` 得矛盾
  have e : Sh ⊢ zfcTr.con 🡘 (𝗭𝗙𝗖.consistent : ArithmeticSentence) :=
    WeakerThan.pbl zfcTr_con_iff
  have hc : Sh ⊢ zfcTr.con := by cl_prover [e, hSh]
  exact con_unprovable' (𝔅 := zfcTr) hD3G hc

-- 公理洁净检查
#print axioms GodelQ.CG008Z0FromSingleD3.zfc_z0_of_single_D3

end GodelQ.CG008Z0FromSingleD3
