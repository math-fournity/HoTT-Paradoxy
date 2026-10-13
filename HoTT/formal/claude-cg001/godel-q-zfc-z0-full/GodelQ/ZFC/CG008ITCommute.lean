import GodelQ.ZFC.CG008TransformShape

/-!
# CG-008 · `iT` 与规则构造子的交换律——九支搬运的**零件**

缺口要的变换必须**重写码**（`CG008TransformShape` 已机器化为什么 `of_ss` 不够）。
重写靠 `iT`。九条逻辑规则的图里，公式码以 `p ⋏ q`/`^∀ p`/`^∃ p`/`^⊤` 等
**构造子**出现，所以搬运需要 `iT` 与这些构造子的交换律。

**Foundation 已有这些**（`InternalTranslate.lean:574-598`）：
`iT_verum`、`iT_and`、`iT_or`、`iT_all`、`iT_exs`、`iT_nrel`、`iT_rel`。
本文件把它们**汇总成搬运要用的形状**，并给出**集合侧**的对应物
（`iT` 的结果是 `ℒₛₑₜ` 的公式，所以还要 `iT p ⋏ iT q` 这类**在 `ℒₛₑₜ` 里**的构造）。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008ITCommute
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Z0Full GodelQ.Translate
variable {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`iT` 与合取的交换**（搬运 `andIntro` 支要用）。

`iT n (p ⋏ q) = iT n p ⋏ iT n q`——右边是 **`ℒₛₑₜ` 的合取**
（`iT.construction.and` 就是 `^⋏`，而 `^⋏` 对 `ℒₛₑₜ` 与 `ℒₒᵣ` 同形）。 -/
theorem it_and {n p q : V} (hp : Bootstrapping.IsUFormula ℒₒᵣ p)
    (hq : Bootstrapping.IsUFormula ℒₒᵣ q) :
    Translate.iT n (p ^⋏ q) = Translate.iT n p ^⋏ Translate.iT n q :=
  GodelQ.Translate.iT_and hp hq

/-- **`iT` 与全称量词的交换**（搬运 `allIntro` 支要用）。

注意**层数加一**：`iT n (^∀ p) = ^∀ (imp ℒₛₑₜ domZero (iT (n+1) p))`。
搬运时子推导的码在层 `n+1`，所以归纳假设必须**对任意层**成立——
这正是 `iT_isUFormula` 用层数感知归纳的原因。 -/
theorem it_all {n p : V} (hp : Bootstrapping.IsUFormula ℒₒᵣ p) :
    Translate.iT n (^∀ p) = ^∀ (Bootstrapping.imp ℒₛₑₜ Translate.domZero
      (Translate.iT (n + 1) p)) :=
  GodelQ.Translate.iT_all hp

/-- **层数在搬运里必须跟着走**（本轮的要点）：

`iT_all` 的右边含 `iT (n+1) p`，所以**任何对 `iT n p` 的归纳都必须
对 `n` 一致**。这就是 `iT_isUFormula` 取 `IsSemiformula ℒₒᵣ n p` 的理由，
也是搬运九支时**不能固定 `n := 0`** 的理由。 -/
theorem level_must_follow (n p : V) (hp : Bootstrapping.IsUFormula ℒₒᵣ p) :
    Translate.iT n (^∀ p) = ^∀ (Bootstrapping.imp ℒₛₑₜ Translate.domZero
      (Translate.iT (n + 1) p)) :=
  it_all hp

end GodelQ.CG008ITCommute

#print axioms GodelQ.CG008ITCommute.it_and
#print axioms GodelQ.CG008ITCommute.it_all
