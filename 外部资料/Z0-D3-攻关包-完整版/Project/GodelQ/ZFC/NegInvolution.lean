import GodelQ.ZFC.SeqTranslateFormula

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

* `Negation.construction` 的八个支定义都**不使用 `param`**：
  `rel`/`nrel` 直接给出原子码，`verum`/`falsum` 是常量，
  `and`/`or` 组合两个子结果，`all`/`exs` 取 `ys.[0]`。因此 `result param p`
  与 `result 0 p` 恒等，归纳里的 `result param p` 可以直接展开成
  `neg (...)` 的码层面形状，无需单独的 `param_irrel` 引理。
* 原子支用 `simp only [Negation.construction.rel, …]` 把构造子投影化归成
  原子码（`construction` 不能省略命名空间前缀，否则会被 Generic 的
  `UformulaRec1.Construction` 遮蔽）；随后 Foundation 的 `@[simp]` `neg_*` 引理
  （`neg_nrel`/`neg_rel`/`neg_falsum`/`neg_verum`）把外层 `neg` 抵消。
* `all`/`exs` 支用 `UformulaRec1.Construction.result_all`/`result_exs` 展开
  谓词的归纳假设（作用于 `result param p`），再用 `nth_adjoin_zero` 把
  `ys.[0]` 落到被否定的子公式，最后 `congrArg` 把归纳假设搬进量词下。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate
open FFL.FirstOrder.Arithmetic.Bootstrapping.Syntax.Formula.Functions

namespace GodelQ.NegInvolution

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
      (by intro n param k R v hR hv
        show neg ℒₒᵣ (Negation.construction.rel param k R v) = (^rel k R v : V)
        rw [← neg_nrel (L := ℒₒᵣ) hR (IsSemitermVec.isUTermVec n)]
        congr 1
        rfl)
      (by intro n param k R v hR hv
        show neg ℒₒᵣ (Negation.construction.nrel param k R v) = (^nrel k R v : V)
        rw [← neg_rel (L := ℒₒᵣ) hR (IsSemitermVec.isUTermVec n)]
        congr 1
        rfl)
      (by intro n param
        show neg ℒₒᵣ (Negation.construction.verum param) = (^⊤ : V)
        rw [← neg_falsum (L := ℒₒᵣ)]
        congr 1
        rfl)
      (by intro n param
        show neg ℒₒᵣ (Negation.construction.falsum param) = (^⊥ : V)
        rw [← neg_verum (L := ℒₒᵣ)]
        congr 1
        rfl)
      (by intro n param p q hp hq ihp ihq
        show neg ℒₒᵣ (Negation.construction.result ℒₒᵣ param p ^⋎
          Negation.construction.result ℒₒᵣ param q) = (p ^⋏ q : V)
        rw [neg_or (L := ℒₒᵣ) (isSemiformula_neg hp).isUFormula
          (isSemiformula_neg hq).isUFormula, ihp, ihq])
      (by intro n param p q hp hq ihp ihq
        show neg ℒₒᵣ (Negation.construction.result ℒₒᵣ param p ^⋏
          Negation.construction.result ℒₒᵣ param q) = (p ^⋎ q : V)
        rw [neg_and (L := ℒₒᵣ) (isSemiformula_neg hp).isUFormula
          (isSemiformula_neg hq).isUFormula, ihp, ihq])
      (by intro n param p hp ih
        show neg ℒₒᵣ (^∃ (Negation.construction.result ℒₒᵣ param p)) = (^∀ p : V)
        rw [neg_ex (L := ℒₒᵣ) (isSemiformula_neg hp).isUFormula]
        exact congrArg (fun x => (^∀ x : V)) (ih 0 (by simp)))
      (by intro n param p hp ih
        show neg ℒₒᵣ (^∀ (Negation.construction.result ℒₒᵣ param p)) = (^∃ p : V)
        rw [neg_all (L := ℒₒᵣ) (isSemiformula_neg hp).isUFormula]
        exact congrArg (fun x => (^∃ x : V)) (ih 0 (by simp)))
  · show neg ℒₒᵣ (neg ℒₒᵣ p) = p
    exact key hp

end GodelQ.NegInvolution

#print axioms GodelQ.NegInvolution.neg_neg_code
