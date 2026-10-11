import GodelQ.ZFC.SeqTranslateFormula

/-!
# CG-007 · W8 第二层（六）：`iT` 与 `neg` 的相容律（引号化版本）

`induction1` 的 `hAxL`、`hCut` 两支需要

```
iT 0 (neg p) = neg ℒₛₑₜ (iT 0 p)
```

其中 `p` 是 **V 内的任意公式码**。本文件给出**引号化版本**（`p = ⌜φ⌝`，
`φ` 是元层标准公式），并说明为什么一般版本需要新的工作。

## 引号化版本为什么不够

`induction1` 的支拿到的是 V 内的公式码，可能对应**非标准**公式；
`iT_quote` 只对 `⌜φ⌝`（φ 标准）给出 `iT` 与 `translate` 的一致性，
所以引号化版本不能直接用在支里。这与本 repo 反复出现的
"元层 vs V 内部"分界线是同一处。

## 一般版本的障碍（本机实测）

`iT` 是 `UformulaRec1` 的 `blueprint.result`，它的归纳原理
`semiformula_result_induction` 的谓词形如 `P param n p q`，其中 `q = iT param p`——
**它一次只跟踪一个递归结果**。而 `iT 0 (neg p)` 与 `iT 0 p` 是两个不同的递归调用，
需要归纳谓词同时提及两者，这超出了该原理直接提供的形状。

可行的方向：把谓词加强为同时携带 `p`、`iT param p`、`neg p`、`iT param (neg p)`
四元关系，或改用 `negGraph`（`Foundation` 提供，`{ Γ := 𝚺, rank := 1 }.Semisentence 2`）
把 `neg` 在码层面显式化。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

namespace GodelQ.ShCraigElimNeg

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **引号化版本的 `iT`/`neg` 相容律**：对元层标准公式 `φ` 成立。

`iT_quote` 把两边都送到 `arithTrln.translate` 的引号，
`LogicalConnective.Hom.map_neg'` 给出 `translate` 与 `neg` 的交换。 -/
lemma iT_quote_neg {n : ℕ} (φ : Semisentence ℒₒᵣ n) :
    iT (n : V) (⌜∼φ⌝ : V) = neg ℒₛₑₜ (iT (n : V) (⌜φ⌝ : V)) := by
  rw [iT_quote, iT_quote]
  rw [show neg ℒₛₑₜ (⌜arithTrln.translate φ⌝ : V) =
      (⌜∼(arithTrln.translate φ)⌝ : V) from (quote_neg' _).symm]
  congr 1
  exact LogicalConnective.Hom.map_neg' arithTrln.translate φ

end GodelQ.ShCraigElimNeg

#print axioms GodelQ.ShCraigElimNeg.iT_quote_neg
