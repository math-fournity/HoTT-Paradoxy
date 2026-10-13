import GodelQ.ZFC.CG008SetC
import GodelQ.ZFC.ZFCDelta1

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008WhichT

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! # 哪一条 Foundation 引理**几乎**够用，差在哪里

## `provable_internalize`（`D3.lean:175`）

    theorem provable_internalize {sigma : ArithmeticSentence} :
        Provable T (⌜sigma⌝ : V) → Provable T (⌜provabilityPred T sigma⌝ : V)

上下文 `variable (T : ArithmeticTheory) [Theory.Δ₁ T] [𝗣𝗔⁻ ⪯ T]`。
`ArithmeticTheory := Theory ℒₒᵣ`（`Arithmetic/Basic/Misc.lean:42`）——**T 必须是 ℒₒᵣ 上的理论**。

## 三个候选 T

| T | `[T.Δ₁]` | `provable T x` 的含义 | 与 `zfcTr` 的关系 |
|---|---|---|---|
| `𝗜𝚺₁` | 有 | 有 𝗜𝚺₁ 推导，结论 x | **谓词不同**（𝗜𝚺₁ 推导 ≠ 𝗭𝗙𝗖 推导） |
| `Sh` | **无（且不可能）** | 有 Sh 推导，结论 x | 语义等价，但内部等价即缺口 |
| `Sh.craig` | **有** | 有 Sh.craig 推导，结论 x | 同上；桥 = 推导翻译 |

**`𝗭𝗙𝗖` 本身有 `Theory.Δ₁`**（本包 `ZFCDelta1.lean:43`），
但它是 `SetTheory = Theory 𝗭𝗙𝗖 上的型别`，**不是 `ArithmeticTheory`**，
所以 `provable_internalize` 的 `T` 槽放不进去。

## 结论：差的是**推导种类的翻译**

`zfcTr x` 量词范围是 **𝗭𝗙𝗖 推导**（`provable 𝗭𝗙𝗖`），
而 `provabilityPred Sh.craig sigma` 量词范围是 **Sh.craig 推导**。
两者要相等，须把「Sh.craig 推导」逐条规则换成「𝗭𝗙𝗖 推导」——
即 `CG008DerivationTransform` 记的**公理步那一处**（九种规则与理论无关，
`of_ss` 原码搬运；只有 `axm` 要换 `T.Δ₁Class`）。

**这正是缺口，且它是数学的：那把换名要 Σ₁ 完全性。**

**治理**：本文件只记查实，不含未证标记。 -/

/-- **查实 1**：`Sh.craig` 的 Δ₁ 实例存在（`CraigTrick.lean:311`）。 -/
noncomputable example : Theory.Δ₁ Sh.craig := inferInstance

/-- **查实 2**：`𝗭𝗙𝗖` 的 Δ₁ 实例存在（本包 `ZFCDelta1.lean:43`）。 -/
noncomputable example : Theory.Δ₁ (𝗭𝗙𝗖 : SetTheory) := inferInstance

end GodelQ.CG008WhichT
