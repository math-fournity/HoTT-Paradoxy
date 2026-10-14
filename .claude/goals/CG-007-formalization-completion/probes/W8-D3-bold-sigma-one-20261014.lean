import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## ★ D3 第四步的**正确工具**：`bold_sigma_one_complete`（2026-10-14）

Master 指出我搜错了工具。正确的在 `DerivabilityCondition/D3.lean:82`：

```
theorem bold_sigma_one_complete {n} {φ : ArithmeticSemisentence n}
    (hp : ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 φ) {w} :
    V ⊧/w φ → T.internalize V ⊢ (toNumVec w ⤔ ⌜φ⌝)
```

**前提**（`D3.lean:20,34`，**无 SoundOnHierarchy**）：
* `[ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]`
* `[Theory.Δ₁ T] [𝗣𝗔⁻ ⪯ T]`
* `hp : Hierarchy 𝚺 1 φ`

**形态正是所需**：`V ⊧/w φ → T.internalize V ⊢ (toNumVec w ⤔ ⌜φ⌝)`，
结论在 **`T.internalize V ⊢`** 层（内部化），不经过 `T ⊢ σ` 层的完备性。

## 核验结果（exit 0）

| 件 | 状态 |
|---|---|
| `bold_sigma_one_complete` 的形状 | ✅ `Hierarchy 𝚺 1 φ → (Evalb w φ) → T.internalize V ⊢ (toNumVec w ⤔ ⌜φ⌝)` |
| `IsHierarchy.mono`（Σ₀ → Σ₁ 抬升） | ✅ `m ≤ n → IsHierarchy Γ m p → IsHierarchy Γ n p` |
| `Bounding.HierarchySymbol.Semiformula.sigma_prop` | ✅ `Hierarchy 𝚺 m ↑φ` |
| `#synth Theory.Δ₁ 𝗭𝗙𝗖` | ✅ `ZFCDelta1.ZFC.delta1` |
| `#synth 𝗣𝗔⁻ ⪯ Sh` | ✅ `instWeakerThan…PeanoMinusOfPeano Sh` |
| **`#synth Theory.Δ₁ Sh`** | ❌ **失败——需显式构造** |

## ★ 新发现的显式义务

`Theory.Δ₁ Sh` **缺失**，且不是 trivial 的实例。其内容是
（`Syntax/Theory.lean:16`）：

```
class Δ₁ (T : Theory L) where
  ch : 𝚫ᴬ₁.Semisentence 1
  mem_iff : ∀ φ : Proposition L, ℕ ⊧/![⌜φ⌝] ch.val ↔ ∃ σ ∈ T, φ = σ
  isDelta1 : ch.ProvablyProperOn 𝗜𝚺₁
```

对 `T := Sh = {σ | 𝗭𝗙𝗖 ⊢ arithTrln.translate σ}`，需要：
`ch` = 「`φ` 的翻译在 𝗭𝗙𝗖 中可证」的 **Δ₁ 定义**，
即 `provable 𝗭𝗙𝗖 (iT 0 ⌜φ⌝)`——这正是包内 `trProv`
（`Z0Full.lean:40`，`𝚺ᴬ₁.Semisentence 1`）！

**故 `Theory.Δ₁ Sh` ≈ 把 `trProv` 从 Σ₁ 升到 Δ₁**（需要 SEARCH·RE·("iT 0 ⌜φ⌝" 的定义)+ Primrec + Primrec（若 translation 是 Primrec））。
这与 `Z0Shadow.lean:17` 记的 `Sh.RE` 义务**同源**（都要 translation 的可计算性/可枚举性）。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
namespace ProbeBoldSigmaOne
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- ① 工具的精确形状
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.Arithmetic.bold_sigma_one_complete

-- ② 前提：Σ₀ → Σ₁ 的抬升
#check @IsHierarchy.mono

-- ③ `reWitness` 是 `𝚺ᴬ₀.Semisentence 2`（Σ₀）
#check @Bounding.HierarchySymbol.Semiformula.sigma
#check @Bounding.HierarchySymbol.Semiformula.val_sigma
#check @Bounding.HierarchySymbol.Semiformula.sigma_prop

-- ★ 关键：把 `bold_sigma_one_complete` 用在 𝗭𝗙𝗖 上
-- 需要 `[Theory.Δ₁ 𝗭𝗙𝗖]` 与 `[𝗣𝗔⁻ ⪯ 𝗭𝗙𝗖]`
#synth Theory.Δ₁ 𝗭𝗙𝗖
-- `𝗭𝗙𝗖` 是 SetTheory，不是 ArithmeticTheory；D3 里 T 该取谁？
-- 关键：D3 的形式是 `T.internalize V ⊢ …`，其中 T 是**算术理论**。
-- 本项目的语境是 `Sh`（ArithmeticTheory），它已满足 `𝗣𝗔⁻ ⪯ Sh`。
#synth 𝗣𝗔⁻ ⪯ Sh
#synth Theory.Δ₁ Sh

/-- **D3 第四步的正确形式**（形态核验，非证明）：
`reWitness` 是 Σ₀ 句子的事实 ⟹ `𝗭𝗙𝗂.internalize V ⊢ …`。 -/
example (w : Fin 2 → V) (hw : Semiformula.Evalb w (Sh.reWitness : V)⬝) : True := trivial

end ProbeBoldSigmaOne