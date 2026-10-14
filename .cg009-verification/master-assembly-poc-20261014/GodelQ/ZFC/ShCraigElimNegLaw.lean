import GodelQ.ZFC.ShCraigElimNegFilled

/-!
# CG-007 · W8 第二层（九）：一般（V 内任意公式码）的 `iT` 与 `neg` 相容律

`hAxL` / `hCut` / `hShift` 三支需要
`iT n (neg ℒₒᵣ p) = neg ℒₛₑₜ (iT n p)`（`p` 是 V 内任意公式码，可能非标准）。
`iT_quote_neg` 只对引号化（元层标准）公式给交换律，不能直接用在 `induction1` 的支里，
所以这里走 `semiformula_result_induction`（与 `isSemiformula_iT` 同形）在 V 内部证一般版本。

## 本文件只做组装

八个支已在 `ShCraigElimNegFilled` 里逐条机器证（`neg_verum_branch` … `neg_exs_branch`，
各自的 `#print axioms` 都只有三条标准公理）。本文件把归纳原理
`UformulaRec1.Construction.semiformula_result_induction` 的九处填上。

## 归纳谓词带 `param = n` 护罩

原理把输出层 `param` 与输入层 `n` 独立量化，而 `iT` 改层（`all`/`exs` 支
`param' = param + 1`）。与 `isSemiformula_iT` 同法，谓词取

```lean
P param n p q := param = n → iT param (neg ℒₒᵣ p) = neg ℒₛₑₜ q
```

护罩 `param = n` 把两层对齐；`all`/`exs` 支里先 `subst` 再调分支引理。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate
open GodelQ.ShCraigElimNegFilled

namespace GodelQ.ShCraigElimNegLaw

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **一般版本的 `iT`/`neg` 相容律**：对 V 内任意公式码 `p`（层数 `n`）成立。

八支全部来自 `ShCraigElimNegFilled`；本定理只做归纳原理的填装。 -/
theorem iT_neg {n : V} : ∀ p, IsSemiformula ℒₒᵣ n p →
    iT n (neg ℒₒᵣ p) = neg ℒₛₑₜ (iT n p) := by
  have key : ∀ {param n p : V}, IsSemiformula ℒₒᵣ n p → param = n →
      iT param (neg ℒₒᵣ p) = neg ℒₛₑₜ (iT.construction.result ℒₒᵣ param p) :=
    UformulaRec1.Construction.semiformula_result_induction
      (V := V) (c := iT.construction) (L := ℒₒᵣ)
      (P := fun param n p q => param = n → iT param (neg ℒₒᵣ p) = neg ℒₛₑₜ q)
      (by definability)
      -- rel
      (by
        intro n param k R v hR hv h
        subst h
        rw [show iT.construction.rel param k R v = iT param (^rel k R v) from
          (UformulaRec1.Construction.result_rel (c := iT.construction) (L := ℒₒᵣ)
            hR hv.isUTerm).symm]
        exact neg_rel_branch param param k R v hR hv.isUTerm)
      -- nrel
      (by
        intro n param k R v hR hv h
        subst h
        rw [show iT.construction.nrel param k R v = iT param (^nrel k R v) from
          (UformulaRec1.Construction.result_nrel (c := iT.construction) (L := ℒₒᵣ)
            hR hv.isUTerm).symm]
        exact neg_nrel_branch param param k R v hR hv.isUTerm
          (isSemiformula_iTR (n := param) hR hv).isUFormula)
      -- verum
      (by
        intro n param h
        subst h
        exact neg_verum_branch param param)
      -- falsum
      (by
        intro n param h
        subst h
        exact neg_falsum_branch param param)
      -- and
      (by
        intro n param p q hp hq ihp ihq h
        subst h
        rw [show iT.construction.and param p q
              (UformulaRec1.Construction.result ℒₒᵣ iT.construction param p)
              (UformulaRec1.Construction.result ℒₒᵣ iT.construction param q)
              = iT param (p ^⋏ q) from
          (UformulaRec1.Construction.result_and (c := iT.construction) (L := ℒₒᵣ)
            hp.isUFormula hq.isUFormula).symm]
        exact neg_and_branch param param p q hp hq (ihp rfl) (ihq rfl)
          (isSemiformula_iT (n := param) p hp)
          (isSemiformula_iT (n := param) q hq))
      -- or
      (by
        intro n param p q hp hq ihp ihq h
        subst h
        rw [show iT.construction.or param p q
              (UformulaRec1.Construction.result ℒₒᵣ iT.construction param p)
              (UformulaRec1.Construction.result ℒₒᵣ iT.construction param q)
              = iT param (p ^⋎ q) from
          (UformulaRec1.Construction.result_or (c := iT.construction) (L := ℒₒᵣ)
            hp.isUFormula hq.isUFormula).symm]
        exact neg_or_branch param param p q hp hq (ihp rfl) (ihq rfl)
          (isSemiformula_iT (n := param) p hp)
          (isSemiformula_iT (n := param) q hq))
      -- all
      (by
        intro n param p hp ih h
        exact neg_all_branch n param p h hp
          (ih 0 (by simp [iT.construction]) (by simp [iT.construction, h])))
      -- exs
      (by
        intro n param p hp ih h
        exact neg_exs_branch n param p h hp
          (ih 0 (by simp [iT.construction]) (by simp [iT.construction, h])))
  · intro p hp
    have h := key hp (rfl : n = n)
    simpa [iT] using h

end GodelQ.ShCraigElimNegLaw

#print axioms GodelQ.ShCraigElimNegLaw.iT_neg
