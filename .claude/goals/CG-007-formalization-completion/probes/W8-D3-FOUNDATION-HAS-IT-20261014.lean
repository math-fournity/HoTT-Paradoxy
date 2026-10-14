import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## ★★ D3 **已在 Foundation 被证明**：`provable_internalize`（2026-10-14）

`DerivabilityCondition/D3.lean:175`：

```
theorem provable_internalize {σ : ArithmeticSentence} :
    Provable T (⌜σ⌝ : V) → Provable T (⌜provabilityPred T σ⌝ : V)
```

**这与 `Z0Blocked.zfcTr_D3_internalize` 是同一形状**（`zfcTr := 𝔅`），
且**已在 Foundation 证完**，前提只是 `[Theory.Δ₁ T] [𝗣𝗔⁻ ⪯ T]`。

**对 D3 的意义**：`RootBlockerQ` 的第四步可能**不需要自己证**，
只要把 `𝗭𝗙𝗖`（或 `Sh`）装进 `[Theory.Δ₁ T] [𝗣𝗔⁻ ⪯ T]` 的框架即可。

⚠ 上一轮我报「`Theory.Δ₁ Sh` 失败」是本轮的**关键闸门**——
这条工具需要 Δ₁，而 `Sh` 的 Δ₁ 未建。

## 核验结果（**exit 0**）

| 项 | 状态 |
|---|---|
| `provable_internalize` 的形状 | ✅ `Provable T ⌜σ⌝ → Provable T ⌜provabilityPred T σ⌝` |
| `#synth 𝗣𝗔⁻ ⪯ 𝗜𝚺₁` | ✅ `instWeakerThan…IBroadSigmaOfNatNat 𝗜𝚺₁` |
| `#synth Theory.Δ₁ 𝗜𝚺₁` | ✅ `Theory.Δ₁.instUnion` |
| **`provable_internalize 𝗜𝚺₁` 实例化** | ✅ **exit 0，真的能用** |

## ★★ 结论：D3 的**数学内容**已在 Foundation 证完

`provable_internalize` 就是 D3（`Provable T ⌜σ⌝ → Provable T ⌜□σ⌝`），
和 `Z0Blocked.zfcTr_D3_internalize` **同一形状**。

**对本项目的意义**：`RootBlockerQ`（D3）的核心**不需自己证**。
剩下的工作是**工程化**：
1. `zfcTr` 是我们包的 `Provability 𝗜𝚺₁ Sh`（不是 Foundation 的 `provabilityPred`）；
2. 需证 `zfcTr σ = provabilityPred T σ`（或 `σ ∈ Sh ↔ …` 一类桥）；
3. 而 `Sh` 的 `[Theory.Δ₁ Sh]` **未建**（上一轮的闸门）。

**故 `RootBlockerQ` 归约到**：
`Theory.Δ₁ Sh` + `zfcTr` 与 Foundation `provabilityPred` 的对应。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
namespace ProbeD3Found
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- ① 工具的精确形状
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.Arithmetic.provable_internalize

-- ② 前提：`[Theory.Δ₁ T] [𝗣𝗔⁻ ⪯ T]` 对哪些 T 成立？
#synth 𝗣𝗔⁻ ⪯ 𝗜𝚺₁
#synth Theory.Δ₁ 𝗜𝚺₁

-- ③ `provabilityPred` 是什么（与 zfcTr 对照）
#check @provabilityPred

-- ④ ★ 关键试验：T := 𝗜𝚺₁ 时 `provable_internalize` 可用吗？
--    （若可用，D3 的数学内容已在 Foundation 证完，只剩工程化）
#synth 𝗣𝗔⁻ ⪯ 𝗜𝚺₁
#synth Theory.Δ₁ 𝗜𝚺₁

/-- ★ 关键形态试验：`T := 𝗜𝚺₁` 的 D3。
（注意：这是 **Foundation 层**的 D3，不是我们包内的 `zfcTr` 版本。） -/
example {σ : ArithmeticSentence} (h : Provable (V := V) 𝗜𝚺₁ (⌜σ⌝ : V)) :
    Provable (V := V) 𝗜𝚺₁ (⌜provabilityPred 𝗜𝚺₁ σ⌝ : V) :=
  FFL.FirstOrder.Arithmetic.Bootstrapping.Arithmetic.provable_internalize 𝗜𝚺₁ h

-- ⑤ zfcTr 与 provabilityPred 的关系（D3 归约的关键）
#check @GodelQ.Z0Full.zfcTr

end ProbeD3Found