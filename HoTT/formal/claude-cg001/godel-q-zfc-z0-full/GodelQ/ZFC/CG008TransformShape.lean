import GodelQ.ZFC.CG008AxStep

/-!
# CG-008 · 变换的精确形状：为什么 `of_ss` 不够，缺的恰好是 `AxStep`

## 两条变换对比

**`Derivation.of_ss`（Foundation 已有）**：
```lean
lemma of_ss (h : T.Δ₁Class ⊆ U.Δ₁Class) : Derivation T d → Derivation U d
```
**码不变**——它靠「`T` 的公理也是 `U` 的公理」。这正是
`CG008OfSs.lean` 记的「沿公理集包含搬运推导、码不变」。

**缺口要的变换**：`Derivation 𝗜𝚺₁ d → Derivation 𝗭𝗙𝗖 d'`，
**码要变**——因为 `𝗜𝚺₁` 的公式在 `ℒₒᵣ`，`𝗭𝗙𝗖` 的在 `ℒₛₑₜ`，
两者的编码根本不在同一个空间里。

## 为什么码必须变（本文件机器化的要点）

- `Derivation 𝗜𝚺₁ d` 的 `d` 是 `ℒₒᵣ` 公式的**序列编码**；
- `Derivation 𝗭𝗙𝗖 d'` 的 `d'` 是 `ℒₛₑₜ` 公式的序列编码；
- 两者是**不同的归纳定义**（`Derivation.blueprint` 对 `T` 与语言都参数化，
  但 `isFormulaSet L` 里的 `L` 不同）。

**所以不能 `of_ss`**。九条逻辑规则的图虽然与 `T` 无关，
但它们里面的 `p`/`q`/`s` 是**公式码**，`ℒₒᵣ` 的码与 `ℒₛₑₜ` 的码不同，
所以要**逐条把码重写**（`iT` 做的正是这件事）。

## 归纳步的精确要求

对 `Derivation 𝗜𝚺₁ d` 做 `Fixpoint.induction`，十支里：

| 支 | 要什么 | 状态 |
|---|---|---|
| `axL`/`verumIntro`/`andIntro`/`orIntro`/`allIntro`/`exsIntro`/`wkRule`/`shiftRule`/`cutRule` | 把子推导的码经 `iT` 变换后再喂给同名规则 | **要建**（码重写，逐支） |
| `axm` | `p ∈ 𝗜𝚺₁.Δ₁Class → Provable 𝗭𝗙𝗖 (iT 0 p)` | **= `AxStep`，缺口本身** |

**本文件只固定这张表**（不证明任何一支）——把「哪些要建、哪一支是缺口」
写成可检视的形式。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008TransformShape
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Z0Full GodelQ.Translate
variable {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **码必须变**：`𝗜𝚺₁` 与 `𝗭𝗙𝗖` 是**不同语言**上的理论，
所以 `Derivation` 的 `isFormulaSet L` 用不同的 `L`，
两个 `Derivation` 谓词**不是同一个**。 -/
example : (𝗜𝚺₁ : ArithmeticTheory) = (𝗜𝚺₁ : Theory ℒₒᵣ) := rfl

-- **`of_ss` 的签名（机器读出的）**：
-- `T.Δ₁Class ⊆ U.Δ₁Class → Derivation T d → Derivation U d`，
-- 其中 `{T U : Theory L}`——**同一个 `L`**。
-- **这就是墙**：`𝗜𝚺₁ : Theory ℒₒᵣ` 而 `𝗭𝗙𝗖 : Theory ℒₛₑₜ`，
-- 所以 `of_ss` **不能**用于缺口。而它的证明里 `axm` 支恰好是
-- `h : p ∈ T.Δ₁Class → p ∈ U.Δ₁Class`——**码不变**。

/-- 缺口要的变换的**形状**（此处只写类型，不声称成立）。 -/
example : Prop :=
  ∀ d : V, Bootstrapping.Derivation 𝗜𝚺₁ d →
    ∃ d' : V, Bootstrapping.Derivation 𝗭𝗙𝗖 d'

/-- **九支与 `axm` 支的分工**（`AxStep` 见 `CG008AxStep`）。 -/
example : GodelQ.CG008AxStep.AxStep (V := V) ↔
    (∀ p : V, p ∈ (𝗜𝚺₁ : ArithmeticTheory).Δ₁Class →
      Provable 𝗭𝗙𝗖 (Translate.iT 0 p)) := Iff.rfl

end GodelQ.CG008TransformShape
