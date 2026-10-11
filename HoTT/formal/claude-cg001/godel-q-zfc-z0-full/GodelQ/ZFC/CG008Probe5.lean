import GodelQ.ZFC.CG008SetAll

/-!
# CG-008 探针 5（非收据）：`setTheory_sigma₁_induction'` 与内部演算的层次不匹配

归约后的目标（`CG008Reduce.lean`）在**内部演算**层：
`𝗭𝗙𝗖.internalize V ⊢ ⌜σ⌝`，其中 `⌜σ⌝ : Bootstrapping.Semiformula V ℒₛₑₜ 0`（**typed**）。

而 Σ₁ 归纳的对偶 `setTheory_sigma₁_induction'`（`SetTheory/Basic/Hierarchy.lean:63`）
的 `P` 取 `(n : ℕ) → SetTheorySemiformula ξ n → Prop`，其中
`SetTheorySemiformula ξ n = Semiformula ℒₛₑₜ ξ n`（**untyped**，`Misc.lean:86`）。

本探针查实这两个层次能否直接对接。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Probe5

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.ZFCSetSigma1
  GodelQ.ZFCSetInternal GodelQ.CG008Reduce GodelQ.CG008SetAll

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1**：`SetTheorySemiformula` 是 untyped 的 `Semiformula ℒₛₑₜ`。 -/
example : SetTheorySemiformula Empty 0 = Semiformula ℒₛₑₜ Empty 0 := rfl

/-- **查实 2**：内部演算的 `⊢` 只作用于 **typed** `Bootstrapping.Semiformula V ℒₛₑₜ n`。
两者是**不同的类型**，不能直接互相喂。
（这一行预期编不过，保留为事实记录。）

```lean
-- 预期失败：untyped 的 `SetTheorySemiformula Empty 0` 不是 `Bootstrapping.Semiformula V ℒₛₑₜ 0`
-- example (φ : SetTheorySemiformula Empty 0) : 𝗭𝗙𝗖.internalize V ⊢ φ := …
```

不过 `⌜·⌝`（typed quote）**可以**把 untyped 的句搬到 typed 层——这正是
`tprovable_tquote_iff_provable_quote` 用的通道。 -/
example (σ : SetTheorySentence) :
    (⌜σ⌝ : Bootstrapping.Semiformula V ℒₛₑₜ 0) = ⌜(Rewriting.emb σ : Semiproposition ℒₛₑₜ 0)⌝ :=
  Sentence.typed_quote_def σ

/-- **查实 3**：Σ₁ 归纳的 `P` 若取内部演算形状，必须先把 untyped 的
`SetTheorySemiformula ξ n` quote 到 typed 层，再要求内部推导。
这样 `P` 的 `n` 参数（自由变量数）与内部演算对**闭句**的要求之间的落差就显式化了。

对 `n = 0`（闭句）这条路是通的：`typed_quote_def` 直接给出等式。 -/
example (σ : SetTheorySentence) :
    (⌜σ⌝ : Bootstrapping.Semiformula V ℒₛₑₜ 0) =
      ⌜(Rewriting.emb σ : Semiproposition ℒₛₑₜ 0)⌝ :=
  Sentence.typed_quote_def σ

end GodelQ.CG008Probe5
