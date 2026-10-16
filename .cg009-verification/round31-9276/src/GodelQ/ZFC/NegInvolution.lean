import GodelQ.ZFC.NegInvolutionBranches

/-!
# CG-007 · W8 第二层（十）：码层面 `neg` 的对合律

`iT`/`neg` 相容律的 `nrel` 支需要码层面的对合律 `neg (neg x) = x`。
Foundation 只有元层的 `Semiformula.neg_neg`；本文件给出**码层面**的版本。

## 证明

`neg` 是 `Negation.construction.result L 0 p`——一个 `UformulaRec1` 构造，
与 `iT` 用同一套机制。所以对合律用同一个归纳原理
`UformulaRec1.Construction.semiformula_result_induction`，谓词取

```lean
P _param _n p q := neg ℒₒᵣ q = p
```

（`q` 由原理固定为 `result L c param p`，故 `P _param _n p (result …)` 展开
正是 `neg (neg p) = p`。）

## 关键技术点

* `Negation.construction` 的八个支定义都**不使用 `param`**（`rel`/`nrel` 直接给出
  原子码，`verum`/`falsum` 是常量，`and`/`or` 组合两个子结果，`all`/`exs` 取
  `ys.[0]`）。因此 `result param p` 与 `result 0 p` 恒等。
* 支里的 `Negation.construction.<field>` 用 `NegInvolutionBranches` 的
  `negConstruction_*` 引理（全部 `rfl`）化成码层面形状，
  再用 Foundation 的 `@[simp]` `neg_*` 引理把外层 `neg` 抵消。
* `all`/`exs` 支用 `result_all`/`result_exs` 的 `@[simp]` 形式展开
  `result param (^∀ p)`，落到 `Negation.construction.all param p ?[…]`，
  再用 `nth_adjoin_zero` 把 `ys.[0]` 取出，最后 `congrArg` 搬进量词下。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

namespace GodelQ.NegInvolution

set_option maxHeartbeats 2000000

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- `neg` 保持公式性（码层面）：由 `IsSemiformula.neg` 给出。 -/
lemma isSemiformula_neg {n p : V} (hp : IsSemiformula ℒₒᵣ n p) :
    IsSemiformula ℒₒᵣ n (neg ℒₒᵣ p) :=
  IsSemiformula.neg hp

/-- `IsUFormula` 版的推论（`n` 任取 0 即可，公式性只要求某个层数）。 -/
lemma isUFormula_neg {p : V} (hp : IsUFormula ℒₒᵣ p) : IsUFormula ℒₒᵣ (neg ℒₒᵣ p) :=
  hp.neg

/-- **码层面的 `neg` 对合律**：`neg (neg p) = p`，对 V 内任意公式码成立。 -/
theorem neg_neg_code : ∀ {n p : V}, IsSemiformula ℒₒᵣ n p → neg ℒₒᵣ (neg ℒₒᵣ p) = p := by
  intro n p hp
  have key : ∀ {param n p : V}, IsSemiformula ℒₒᵣ n p →
      neg ℒₒᵣ (Negation.construction.result ℒₒᵣ param p) = p :=
    UformulaRec1.Construction.semiformula_result_induction
      (V := V) (c := Negation.construction) (L := ℒₒᵣ)
      (P := fun _param _n p q => neg ℒₒᵣ q = p)
      (by definability)
      (by
        intro n param k R v hR hv
        rw [NegInvolutionBranches.negConstruction_rel]
        exact NegInvolutionBranches.neg_invol_rel hR hv.isUTerm)
      (by
        intro n param k R v hR hv
        rw [NegInvolutionBranches.negConstruction_nrel]
        exact NegInvolutionBranches.neg_invol_nrel hR hv.isUTerm)
      (by
        intro n param
        rw [NegInvolutionBranches.negConstruction_verum]
        exact NegInvolutionBranches.neg_invol_verum)
      (by
        intro n param
        rw [NegInvolutionBranches.negConstruction_falsum]
        exact NegInvolutionBranches.neg_invol_falsum)
      (by
        intro n param p q hp hq ihp ihq
        have hu₁ : IsUFormula ℒₒᵣ (UformulaRec1.Construction.result ℒₒᵣ
            Negation.construction param p) :=
          UformulaRec1.Construction.graph_dom_uformula (c := Negation.construction)
            (L := ℒₒᵣ) (param := param) (p := p)
            (UformulaRec1.Construction.result_prop (c := Negation.construction)
              (L := ℒₒᵣ) (param := param) (p := p) hp.isUFormula)
        have hu₂ : IsUFormula ℒₒᵣ (UformulaRec1.Construction.result ℒₒᵣ
            Negation.construction param q) :=
          UformulaRec1.Construction.graph_dom_uformula (c := Negation.construction)
            (L := ℒₒᵣ) (param := param) (p := q)
            (UformulaRec1.Construction.result_prop (c := Negation.construction)
              (L := ℒₒᵣ) (param := param) (p := q) hq.isUFormula)
        rw [NegInvolutionBranches.negConstruction_and]
        exact NegInvolutionBranches.neg_invol_and ihp ihq hu₁ hu₂)
      (by
        intro n param p q hp hq ihp ihq
        have hu₁ : IsUFormula ℒₒᵣ (UformulaRec1.Construction.result ℒₒᵣ
            Negation.construction param p) :=
          UformulaRec1.Construction.graph_dom_uformula (c := Negation.construction)
            (L := ℒₒᵣ) (param := param) (p := p)
            (UformulaRec1.Construction.result_prop (c := Negation.construction)
              (L := ℒₒᵣ) (param := param) (p := p) hp.isUFormula)
        have hu₂ : IsUFormula ℒₒᵣ (UformulaRec1.Construction.result ℒₒᵣ
            Negation.construction param q) :=
          UformulaRec1.Construction.graph_dom_uformula (c := Negation.construction)
            (L := ℒₒᵣ) (param := param) (p := q)
            (UformulaRec1.Construction.result_prop (c := Negation.construction)
              (L := ℒₒᵣ) (param := param) (p := q) hq.isUFormula)
        rw [NegInvolutionBranches.negConstruction_or]
        exact NegInvolutionBranches.neg_invol_or ihp ihq hu₁ hu₂)
      (by
        intro n param p hp ih
        have hu : IsUFormula ℒₒᵣ (UformulaRec1.Construction.result ℒₒᵣ
            Negation.construction (Negation.construction.allChanges param 0) p) :=
          UformulaRec1.Construction.graph_dom_uformula (c := Negation.construction)
            (L := ℒₒᵣ)
            (UformulaRec1.Construction.result_prop (c := Negation.construction)
              (L := ℒₒᵣ) (param := Negation.construction.allChanges param 0) hp.isUFormula)
        rw [UformulaRec1.Construction.result_all (c := Negation.construction) (L := ℒₒᵣ)
              hp.isUFormula (rfl : Negation.construction.allSize param p = 1)]
        show neg ℒₒᵣ (^∃ ((?[UformulaRec1.Construction.result ℒₒᵣ Negation.construction
          (Negation.construction.allChanges param 0) p] : V).[0])) = (^∀ p : V)
        rw [nth_adjoin_zero]
        exact NegInvolutionBranches.neg_invol_all (ih 0 (by simp)) hu)
      (by
        intro n param p hp ih
        have hu : IsUFormula ℒₒᵣ (UformulaRec1.Construction.result ℒₒᵣ
            Negation.construction (Negation.construction.exsChanges param 0) p) :=
          UformulaRec1.Construction.graph_dom_uformula (c := Negation.construction)
            (L := ℒₒᵣ)
            (UformulaRec1.Construction.result_prop (c := Negation.construction)
              (L := ℒₒᵣ) (param := Negation.construction.exsChanges param 0) hp.isUFormula)
        rw [UformulaRec1.Construction.result_exs (c := Negation.construction) (L := ℒₒᵣ)
              hp.isUFormula (rfl : Negation.construction.exsSize param p = 1)]
        show neg ℒₒᵣ (^∀ ((?[UformulaRec1.Construction.result ℒₒᵣ Negation.construction
          (Negation.construction.exsChanges param 0) p] : V).[0])) = (^∃ p : V)
        rw [nth_adjoin_zero]
        exact NegInvolutionBranches.neg_invol_exs (ih 0 (by simp)) hu)
  · show neg ℒₒᵣ (neg ℒₒᵣ p) = p
    exact key hp

end GodelQ.NegInvolution

#print axioms GodelQ.NegInvolution.neg_neg_code
