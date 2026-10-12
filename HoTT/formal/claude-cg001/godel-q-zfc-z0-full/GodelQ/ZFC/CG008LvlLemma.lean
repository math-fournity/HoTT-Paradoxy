import GodelQ.ZFC.CG008LvlCheck

/-!
# CG-008 探针（非收据）：层数无关**引理**能否成立

## 目标

```
∀ p, IsUFormula ℒₒᵣ p → ∀ n : V, (IsUFormula ℒₛₑₜ (iT n p) ↔ IsUFormula ℒₛₑₜ (iT 0 p))
```

## 障碍

`iTR n _k R v` 的定义里 `n` **确实出现**：
`conjunct 2 n i (iVE n v_i)`——层数进了**原子翻译**。

**所以 `iT n p` 与 `iT 0 p` 是不同的码**，引理不能是等式。

**但 `IsUFormula` 是「是不是公式」的判定**——
层数只影响**自由变量的编号**，而「是不是公式」**不依赖编号**。
**所以引理可能仍成立**（只是要证 `iT n p` 与 `iT 0 p` 都是公式）。

## 本探针

固定这个观察，并试一条更弱但够用的形式。 -/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008LvlLemma

open GodelQ.Translate (iT iTR)

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1**：`iT` 的**原子情形**里层数确实出现（`iTR` 的 `conjunct 2 n i (iVE n v_i)`）。

**所以引理不能写成 `iT n p = iT 0 p`。** -/
noncomputable example (n k R v : V) : V := iTR n k R v

/-- **查实 2（够用的更弱形式）**：只需**单向**——
「`IsUFormula (iT 0 p)` ⟹ `IsUFormula (iT n p)`」，
因为归纳里是由**假设**（层 0 成立）推出**目标**（层 n+1 成立）。

**这个方向可能比双向容易**：它是「`iT` 保持公式性」的**单调**形式。 -/
example : Prop := ∀ (p : V), Bootstrapping.IsUFormula ℒₒᵣ p →
    ∀ n : V, (Bootstrapping.IsUFormula ℒₛₑₜ (iT 0 p) →
      Bootstrapping.IsUFormula ℒₛₑₜ (iT n p))

end GodelQ.CG008LvlLemma
