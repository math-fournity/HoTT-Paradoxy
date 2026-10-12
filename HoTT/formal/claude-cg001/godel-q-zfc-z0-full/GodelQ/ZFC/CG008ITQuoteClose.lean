import GodelQ.ZFC.CG008ITParts

/-!
# CG-008 · `iT_quote` 条件内部化——**三个子目标全部由 `iT_isUFormula` 支付**

`CG008ITQuoteProof.lean` 把「`iT_quote` 的条件内部化」列成三个子目标
（`hrel`、`hnrel`、`hall`/`hexs`），并判定 `hall`/`hexs` 是**实质障碍**
（`iT (n+1) p` 的层数与归纳假设 `iT 0 p` 对不上）。

**本轮结论**：那不是障碍，是**归纳原理选错了**。
`IsSemiformula.sigma1_structural_induction` 的谓词吃层数，
其 `hall` 的归纳假设就在层 `n + 1`——正是所需。
所以 `iT_isUFormula`（`CG008ITParts.lean`）**一次性付清三个子目标**，
本文件把这件事固定成可检视的形式。

## 目标陈述

条件内部化：**任意** `x : V`（含非标准码），若 `x` 是**层 `n`** 的算术公式码，
则 `iT n x` 是集合语言公式。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008ITQuoteClose
open GodelQ.ZFCArith GodelQ.Translate
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **条件内部化（层数版）**：就是 `iT_isUFormula`。 -/
theorem iT_quote_internalized {n x : V} (hx : Bootstrapping.IsSemiformula ℒₒᵣ n x) :
    Bootstrapping.IsUFormula ℒₛₑₜ (iT n x) :=
  GodelQ.CG008ITParts.iT_isUFormula n x hx

/-- **条件内部化（层 0 版）**：`CG008ITQuoteProof` 里那个谓词
`P x := IsUFormula ℒₛₑₜ (iT 0 x)` 的完整形式——
**注意假设是 `IsSemiformula ℒₒᵣ 0`**（不是 `IsUFormula ℒₒᵣ`，
理由见 `CG008ITParts.lean` 头部）。 -/
theorem iT_zero_isUFormula {x : V} (hx : Bootstrapping.IsSemiformula ℒₒᵣ 0 x) :
    Bootstrapping.IsUFormula ℒₛₑₜ (iT 0 x) :=
  GodelQ.CG008ITParts.iT_isUFormula 0 x hx

/-- **闭句版**：`Sentence ℒₒᵣ` 的码。 -/
theorem iT_quote_closed (φ : Sentence ℒₒᵣ) :
    Bootstrapping.IsUFormula ℒₛₑₜ (iT 0 (⌜φ⌝ : V)) :=
  iT_zero_isUFormula (FFL.FirstOrder.Sentence.quote_isSemiformula (V := V) (L := ℒₒᵣ) (n := 0) φ)

end GodelQ.CG008ITQuoteClose

#print axioms GodelQ.CG008ITQuoteClose.iT_quote_internalized
#print axioms GodelQ.CG008ITQuoteClose.iT_zero_isUFormula
#print axioms GodelQ.CG008ITQuoteClose.iT_quote_closed
