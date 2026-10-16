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
  `and`/`or` 组合两个子结果，`all`/`exs` 取 `ys.[0]`。因此归纳里的
  `result param p` 可以直接展开成 `neg (...)` 的码层面形状。
* 归纳原理在 `all`/`exs` 支把层数**升一**（前提是 `IsSemiformula L (n+1) p`），
  而 `Negation.construction.allChanges` 取默认（`param' = param`）。
* 原子支把构造子投影化归成原子码（`construction` 不能省略命名空间前缀，
  否则会被 Generic 的 `UformulaRec1.Construction` 遮蔽）；随后 Foundation 的
  `neg_rel`/`neg_nrel`/`neg_verum`/`neg_falsum` 把外层 `neg` 抵消。
* `and`/`or`/`all`/`exs` 支用 `neg_and`/`neg_or`/`neg_all`/`neg_ex`；它们要求
  被否定的是 `IsUFormula`，这个事实由 `result_prop` 与 `graph_dom_uformula` 给出
  （`isUFormula_result`）。
* `all`/`exs` 支先用 `UformulaRec1.Construction.result_all`/`result_exs` 展开
  构造子产出（`^∃ ys.[0]`），再用 `nth_adjoin_zero` 把 `ys.[0]` 落到被否定的
  子公式，最后用 `congrArg` 把归纳假设搬进量词下。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

namespace GodelQ.NegInvolution

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- `neg` 保持公式性（码层面）：由 `IsSemiformula.neg` 给出。 -/
lemma isSemiformula_neg {n p : V} (hp : IsSemiformula ℒₒᵣ n p) :
    IsSemiformula ℒₒᵣ n (neg ℒₒᵣ p) :=
  IsSemiformula.neg hp

/-- `IsUFormula` 版的推论。 -/
lemma isUFormula_neg {p : V} (hp : IsUFormula ℒₒᵣ p) : IsUFormula ℒₒᵣ (neg ℒₒᵣ p) :=
  hp.neg

/-- **码层面的 `neg` 对合律**：`neg (neg p) = p`，对 V 内任意公式码成立。 -/
theorem neg_neg_code : ∀ {n p : V}, IsSemiformula ℒₒᵣ n p → neg ℒₒᵣ (neg ℒₒᵣ p) = p := by
  intro n p hp
  have key : ∀ {param n p : V}, IsSemiformula ℒₒᵣ n p →
      IsUFormula ℒₒᵣ (Negation.construction.result ℒₒᵣ param p) ∧
        neg ℒₒᵣ (Negation.construction.result ℒₒᵣ param p) = p :=
    UformulaRec1.Construction.semiformula_result_induction
      (V := V) (c := Negation.construction) (L := ℒₒᵣ)
      (P := fun _param _n p q => IsUFormula ℒₒᵣ q ∧ neg ℒₒᵣ q = p)
      (by definability)
      (by
        intro n param k R v hR hv
        show IsUFormula ℒₒᵣ (Negation.construction.rel param k R v) ∧
          neg ℒₒᵣ (Negation.construction.rel param k R v) = (^rel k R v : V)
        rw [show Negation.construction.rel param k R v = (^nrel k R v : V) from rfl]
        exact ⟨IsUFormula.nrel.mpr ⟨hR, hv.isUTermVec⟩, neg_nrel (L := ℒₒᵣ) hR hv.isUTermVec⟩)
      (by
        intro n param k R v hR hv
        show IsUFormula ℒₒᵣ (Negation.construction.nrel param k R v) ∧
          neg ℒₒᵣ (Negation.construction.nrel param k R v) = (^nrel k R v : V)
        rw [show Negation.construction.nrel param k R v = (^rel k R v : V) from rfl]
        exact ⟨IsUFormula.rel.mpr ⟨hR, hv.isUTermVec⟩, neg_rel (L := ℒₒᵣ) hR hv.isUTermVec⟩)
      (by
        intro n param
        show IsUFormula ℒₒᵣ (Negation.construction.verum param) ∧
          neg ℒₒᵣ (Negation.construction.verum param) = (^⊤ : V)
        rw [show Negation.construction.verum param = (^⊥ : V) from rfl]
        exact ⟨IsUFormula.falsum, neg_falsum (L := ℒₒᵣ)⟩)
      (by
        intro n param
        show IsUFormula ℒₒᵣ (Negation.construction.falsum param) ∧
          neg ℒₒᵣ (Negation.construction.falsum param) = (^⊥ : V)
        rw [show Negation.construction.falsum param = (^⊤ : V) from rfl]
        exact ⟨IsUFormula.verum, neg_verum (L := ℒₒᵣ)⟩)
      (by
        intro n param p q hp hq ihp ihq
        show IsUFormula ℒₒᵣ (Negation.construction.and param p q
            (Negation.construction.result ℒₒᵣ param p)
            (Negation.construction.result ℒₒᵣ param q)) ∧
          neg ℒₒᵣ (Negation.construction.and param p q
            (Negation.construction.result ℒₒᵣ param p)
            (Negation.construction.result ℒₒᵣ param q)) = (p ^⋏ q : V)
        rw [show Negation.construction.and param p q
            (Negation.construction.result ℒₒᵣ param p)
            (Negation.construction.result ℒₒᵣ param q) =
            (Negation.construction.result ℒₒᵣ param p ^⋎
              Negation.construction.result ℒₒᵣ param q : V) from rfl]
        exact ⟨IsUFormula.or.mpr ⟨ihp.1, ihq.1⟩, by
          rw [neg_or (L := ℒₒᵣ) ihp.1 ihq.1, ihp.2, ihq.2]⟩)
      (by
        intro n param p q hp hq ihp ihq
        show IsUFormula ℒₒᵣ (Negation.construction.or param p q
            (Negation.construction.result ℒₒᵣ param p)
            (Negation.construction.result ℒₒᵣ param q)) ∧
          neg ℒₒᵣ (Negation.construction.or param p q
            (Negation.construction.result ℒₒᵣ param p)
            (Negation.construction.result ℒₒᵣ param q)) = (p ^⋎ q : V)
        rw [show Negation.construction.or param p q
            (Negation.construction.result ℒₒᵣ param p)
            (Negation.construction.result ℒₒᵣ param q) =
            (Negation.construction.result ℒₒᵣ param p ^⋏
              Negation.construction.result ℒₒᵣ param q : V) from rfl]
        exact ⟨IsUFormula.and.mpr ⟨ihp.1, ihq.1⟩, by
          rw [neg_and (L := ℒₒᵣ) ihp.1 ihq.1, ihp.2, ihq.2]⟩)
      (by
        intro n param p hp ih
        rw [UformulaRec1.Construction.result_all (V := V) (c := Negation.construction) (L := ℒₒᵣ)
          hp.isUFormula (rfl : Negation.construction.allSize param (^∀ p) = 1)]
        change IsUFormula ℒₒᵣ
            (^∃ ((Negation.construction.result ℒₒᵣ (Negation.construction.allChanges param 0) p ∷
              (0 : V) : V).[0])) ∧
          neg ℒₒᵣ
            (^∃ ((Negation.construction.result ℒₒᵣ (Negation.construction.allChanges param 0) p ∷
              (0 : V) : V).[0])) = (^∀ p : V)
        rw [nth_adjoin_zero]
        refine ⟨IsUFormula.ex.mpr (ih 0 (by simp [Negation.construction])).1, ?_⟩
        rw [neg_ex (L := ℒₒᵣ) (ih 0 (by simp [Negation.construction])).1]
        exact congrArg (fun x => (^∀ x : V)) (ih 0 (by simp [Negation.construction])).2)
      (by
        intro n param p hp ih
        rw [UformulaRec1.Construction.result_exs (V := V) (c := Negation.construction) (L := ℒₒᵣ)
          hp.isUFormula (rfl : Negation.construction.exsSize param (^∃ p) = 1)]
        change IsUFormula ℒₒᵣ
            (^∀ ((Negation.construction.result ℒₒᵣ (Negation.construction.exsChanges param 0) p ∷
              (0 : V) : V).[0])) ∧
          neg ℒₒᵣ
            (^∀ ((Negation.construction.result ℒₒᵣ (Negation.construction.exsChanges param 0) p ∷
              (0 : V) : V).[0])) = (^∃ p : V)
        rw [nth_adjoin_zero]
        refine ⟨IsUFormula.all.mpr (ih 0 (by simp [Negation.construction])).1, ?_⟩
        rw [neg_all (L := ℒₒᵣ) (ih 0 (by simp [Negation.construction])).1]
        exact congrArg (fun x => (^∃ x : V)) (ih 0 (by simp [Negation.construction])).2)
  · show neg ℒₒᵣ (neg ℒₒᵣ p) = p
    exact (key hp).2

end GodelQ.NegInvolution

#print axioms GodelQ.NegInvolution.neg_neg_code
