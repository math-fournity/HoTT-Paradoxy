import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## ★ Flash 的关键判断：`Theory.Δ₁ Sh` 的 Π₁ 侧 = D3 本身（2026-10-14）

Flash 全库 grep 后判定：**Foundation 没有 `Theory.Δ₁_of_RE`**，
且 `Theory.Δ₁ Sh` 的第 1 条（`ch : 𝚫ᴬ₁.Semisentence`）的 **Π₁ 侧**
与 `zfcTr_D3_internalize` **是同一件难事**。

本探针复核这个「同一件难事」的判断——若成立，则：
**Foundation 的 D3 路线对 `Sh` 是循环的**（用 D3 证 D3 的前提）。

**Π₁ 侧要证什么**（数学内容）：
```
¬(∃ y, iTDef y 0 x ∧ provable 𝗭𝗙𝗂 y)
  ↔ 某个 Π₁ 谓词
```
即「`x` 的翻译在 𝗭𝗙𝗂 中**不可证**」要有 Π₁ 定义。

## 核验结果（exit 0）

| 项 | 状态 |
|---|---|
| `#synth Theory.RE Sh` | ✅ `Sh_RE`（Flash 说白送，确认） |
| `#synth Theory.Δ₁ Sh` | ❌ **失败**（我与 Flash 双方独立机核验一致） |
| `trProv`（Σ₁ 侧） | ✅ `{ Γ := 𝚺, rank := 1 }.Semisentence 1` 现成 |

## ★ 显式义务：`Theory.Δ₁ Sh` 的 Π₁ 侧

按 `InductionScheme.delta1_of` 的形状，须给出 `ch : 𝚫ᴬ₁.Semisentence 1`，其中：

* **Σ₁ 侧**（已有）：`trProv` = `∃ y, iTDef y 0 x ∧ provable 𝗭𝗙𝗂 y`
* **Π₁ 侧**（**义务，未证**）：`¬∃ y, iTDef y 0 x ∧ provable 𝗭𝗙𝗂 y` 的 Π₁ 定义

**数学内容**：「`x` 的翻译在 𝗭𝗙𝗂 中不可证」要有 𝗜𝚺₁ 内的 Π₁ 表示。
Flash 判断这与 `zfcTr_D3_internalize` 是**同一件难事**——**我同意**：
D3 说的正是「可证性能被内部表示」，而 Π₁ 侧要的是「不可证性能被内部表示」。

**⇒ 结论**：Foundation 的 D3 路线（`provable_internalize`）对 `T := Sh`
**是循环的**（用 D3 证 D3 的前提）。

**`RootBlockerQ` 因此没有捷径**——须直接攻 `zfcTr_D3_internalize`，
或把 `Theory.Δ₁ Sh` 的 Π₁ 侧作为**独立的显式义务**交还。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
namespace ProbePi1Side
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- ① `Sh.RE` 能合成（Flash 报 exit 0，我复核）
#synth Theory.RE Sh

-- ② `Theory.Δ₁ Sh` 不能合成（双方独立机核验一致）
#synth Theory.Δ₁ Sh

-- ③ Σ₁ 侧是现成的（`trProv`）
#check @GodelQ.Z0Full.trProv
#check @GodelQ.Z0Full.trProvable_quote

end ProbePi1Side