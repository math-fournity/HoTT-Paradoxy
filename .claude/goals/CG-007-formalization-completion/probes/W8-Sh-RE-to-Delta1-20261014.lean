import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## `Theory.Δ₁ Sh` 的前提链：`Sh.RE` 是必需的吗？（2026-10-14）

Foundation 的 D3（`provable_internalize`）需要 `[Theory.Δ₁ T]`。
`#synth Theory.Δ₁ Sh` 已机核验失败。本探针查它的构造路径。

`Theory.Δ₁` 的内容（`Syntax/Theory.lean:16`）：
```
class Δ₁ (T : Theory L) where
  ch : 𝚫ᴬ₁.Semisentence 1
  mem_iff : ∀ φ : Proposition L, ℕ ⊧/![⌜φ⌝] ch.val ↔ ∃ σ ∈ T, φ = σ
  isDelta1 : ch.ProvablyProperOn 𝗜𝚺₁
```

**关键**：`ch : 𝚫ᴬ₁.Semisentence 1` —— 需要**既是 Σ₁ 又是 Π₁**。
对 `Sh`：Σ₁ 方向由 `trProv` 给（`Provable` 是 Σ₁）；
Π₁ 方向 = 「不可证」——需要 **𝗭𝗙𝗖 的完全性**，一般没有。

本探针核验：Foundation 里有没有从 RE 造 Δ₁ 的路径。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
namespace ProbeShRE
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- ① `𝚫ᴬ₁.Semisentence`（Δ₁ 句子的类型）
#check @𝚫ᴬ₁.Semisentence

-- ② 现成的 Δ₁ 构造路径：只有并集（各因子须已是 Δ₁）
#check @Theory.Δ₁.instUnion

-- ③ 结论：**没有**「RE ⟹ Δ₁」或「Σ₁ ⟹ Δ₁」的通用路径
#check @arithTrln
#check @GodelQ.ZFCZ0.Sh

/-- **结构性结论（本探针的发现）**：

`Theory.Δ₁ Sh` 的 `ch` 须是 `𝚫ᴬ₁.Semisentence`，即**Σ₁ 且 Π₁**。

* **Σ₁ 方向**：有——`trProv prov`（`Provable` 是 Σ₁，`Z0Full.lean:39-43`）。
* **Π₁ 方向**：即「φ 的翻译**不可证**」的 Π₁ 定义——
  这等价于 𝗭𝗙𝗖 的**完全性**（或至少 φ 层的完全性），**一般没有**。

故 **`Theory.Δ₁ Sh` ⟸ 𝗭𝗙𝗂 的 Σ₁-完全性**——
而那正是本项目要证的 `𝗭𝗙𝗂 ⊬ 𝗭𝗙𝗂.consistent` 所依赖的东西。

**⚠ 但注意**：Σ₁-完全性对 `Arithmetic` 是**可为真的**
（Σ₁ 句真 ⟹ 可证，这是 Σ₁-完备性，比一致性弱）。
Foundation 有 `bold_sigma_one_complete`（不需 SoundOnHierarchy）。

**故 `Theory.Δ₁ Sh` 的可行路径可能是**：
Σ₁ 方向用 `trProv prov`，Π₁ 方向用 Σ₁-完备性的某个内部化版本。
难度待估，且**与 `Sh.RE` 义务不同源**（`Sh.RE` 是纯可计算性）。 -/
theorem sh_delta1_structure : True := trivial

end ProbeShRE