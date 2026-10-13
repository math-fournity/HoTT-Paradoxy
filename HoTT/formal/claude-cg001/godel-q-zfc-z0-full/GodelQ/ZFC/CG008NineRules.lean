import GodelQ.ZFC.CG008ITSet6

/-!
# CG-008 · 九支搬运：把 `Derivable 𝗜𝚺₁` 变成 `Derivable 𝗭𝗙𝗖`

## 工具

`Derivation.induction1`（`Proof/Basic.lean:642`）——十支归纳：

| 支 | 要建什么 |
|---|---|
| `axL`/`verumIntro`/`andIntro`/`orIntro`/`allIntro`/`exsIntro`/`wkRule`/`shiftRule`/`cutRule` | **九支**：把子推导的码经 `iTSet` 变换后喂给同名规则 |
| `axm` | **缺口本身**（`CG008AxStep.AxStep`） |

## 本轮的定位

九支的**零件全部齐备**（本会话建成的）：
- `iTSet`（`CG008ITSet6`）——公式集的像，V 内的 Σ₁ 函数；
- `iT` 与 `⋏`/`⋎`/`∀`/`∃` 的交换律（`CG008ITCommute`）；
- 规则函数（`axL`/`verumIntro`/…/`cutRule`）都是 V 内的 Σ₀ 函数（`Basic.lean:155-222`）。

**但九支的搬运要证的是**：`Derivation 𝗜𝚺₁ d → Derivation 𝗭𝗙𝗖 d'`，
其中 `d'` 由 `iT`/`iTSet` 重写 `d` 得到。**这不是一条归纳**——
`Derivation 𝗭𝗙𝗖` 的十支与 `Derivation 𝗜𝚺₁` 的十支**要对上**，
而 `iT` 把 `ℒₒᵣ` 的公式码映到 `ℒₛₑₜ` 的公式码，
所以**每一支的 `IsFormulaSet`/`DerivationOf` 前提都要重证**。

**本文件把这张对照表写出来**（不声称九支已证）。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008NineRules
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Z0Full GodelQ.Translate
variable {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **变换的目标**（缺口的最具体形式）：

存在一个 V 内的码变换，把 `𝗜𝚺₁` 的推导码变成 `𝗭𝗙𝗖` 的推导码。 -/
def DerivationTransform : Prop :=
  ∀ d : V, Bootstrapping.Derivation (𝗜𝚺₁ : ArithmeticTheory) d →
    ∃ d' : V, Bootstrapping.Derivation (𝗭𝗙𝗖 : SetTheory) d'

-- **`DerivationTransform` 与缺口的关系**（本轮查实）：
--
-- `Derivation.induction1`（`Proof/Basic.lean:642`）的十支里，
-- **`axm` 支的前提是 `p ∈ T.Δ₁Class`**——`T` 从 `𝗜𝚺₁` 变成 `𝗭𝗙𝗖` 时，
-- 这一支**不能搬运**（`ℒₒᵣ` 的公理码不是 `ℒₛₑₜ` 的公理码）。
-- 其余九支的前提（`IsFormulaSet`/`DerivationOf`）**都是结构的**，
-- 经 `iT`/`iTSet` 重写后可以重建。
--
-- **所以 `DerivationTransform` 就是缺口的最具体形式**，
-- 而它的唯一障碍是 `axm` 支——即 `CG008AxStep.AxStep`。
--
-- **本文件只固定这个形状**（不声称任一侧已证）。

end GodelQ.CG008NineRules
