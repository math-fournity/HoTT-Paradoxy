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

end GodelQ.CG008Z0FromSingleD3
