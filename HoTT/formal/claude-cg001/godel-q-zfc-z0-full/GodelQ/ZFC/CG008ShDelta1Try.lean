import GodelQ.ZFC.CG008GapSharp
import GodelQ.ZFC.Z0Shadow

/-!
# CG-008 · 能不能给 `Sh` 造一个 `Δ₁` 实例？——**不能**，且这是 G1 的必然

## 试什么

`provable_D3` 需要 `[T.Δ₁]`。若 `Sh` 有 `Δ₁`，则
`provable_D3 (T := Sh)` 直接给出缺口。本文件核对 `Sh` 的形状。

`Sh := {σ | 𝗭𝗙𝗖 ⊢ arithTrln.translate σ}`（`Z0Shadow.lean`）。

## 为什么不可能（`CG008Delta1Wall` 已证，此处只复述类型）

`Theory.Δ₁ T` 的 `mem_iff` 要求**精确刻画** `T` 的公理集：
一个 Δ₁ 公式 `φ` 使 `x ∈ T ↔ φ(x)`。而 `Sh` 的成员判定是
「𝗭𝗙𝗖 证明 translate σ」——**Σ₁ 而非 Δ₁**：其否定是「不存在证明」，
Π₁。若 `Sh.Δ₁` 成立，则 `Sh` 的成员判定递归，即 **𝗭𝗙𝗖 的定理集递归**，
与哥德尔第一不完备矛盾（在 𝗭𝗙𝗖 一致的前提下）。

**所以 `Sh.Δ₁` 不可能**，缺口不能经 `provable_D3` 闭合。

## 那 `Sh.craig` 呢？（`CG008CraigRoute` 已查）

Craig 技巧给出 `Sh.craig`，它**有** `Δ₁`（`CraigTrick.lean:311`），
所以 `provable_D3 (T := Sh.craig)` **可用**。但它的可证性谓词是
`provable Sh.craig`，与 `zfcTr`（= `provable 𝗭𝗙𝗖` ∘ translate）的桥
**等价于缺口本身**——换名不归约。

## 结论

缺口不能通过「给 `Sh` 补 `Δ₁`」闭合。这与 `CG008Delta1Wall`、
`CG008CraigRoute` 的结论一致，本文件只是把它们与 `provable_D3` 的
类型要求**接在一起**。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008ShDelta1Try
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Z0Full GodelQ.Translate

/-- `Sh` 是 `ArithmeticTheory`（`ArithmeticTheory` 就是 `Theory ℒₒᵣ` 的缩写，
所以这不是新事实——写出来是为了标明 `provable_D3` 只差 `[T.Δ₁]` 这一个实例）。 -/
example : ArithmeticTheory := (Sh : Theory ℒₒᵣ)

/-- **断点**：`provable_D3` 对 `Sh` 需要的实例（**不可能**，见文件头）。 -/
example : Type := Theory.Δ₁ (Sh : Theory ℒₒᵣ)

end GodelQ.CG008ShDelta1Try
