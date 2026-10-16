import GodelQ.ZFC.SeqTranslateFormula

/-!
# CG-007 · W8 第二层（八）：`iT`/`neg` 相容律——五支已填

`hAxL`、`hCut`、`hShift` 三支需要 `iT n (neg p) = neg ℒₛₑₜ (iT n p)`
（`p` 是 V 内任意公式码）。本文件填掉 `semiformula_result_induction` 九支中的五支。

## 已填（无未证标记）

| 支 | 用到的引理 |
|---|---|
| `verum` | `neg_verum` + `iT_falsum` + `iT_verum` |
| `falsum` | `neg_falsum` + `iT_verum` + `iT_falsum` |
| `rel` | `neg_rel` + `iT_nrel` + `iT_rel` |
| `and` | `neg_and` + `iT_or` + `iT_and` + 归纳假设 |
| `or` | `neg_or` + `iT_and` + `iT_or` + 归纳假设 |

## 未填（两支 + 一支）

| 支 | 障碍 |
|---|---|
| `nrel` | 需要**码层面的 `neg` 对合律** `neg (neg x) = x`。Foundation 只有元层 `Semiformula.neg_neg`；`iTR param k R v` 是 `qqAlls` 复合、不是 `^rel` 形式，`neg_rel` 不能直接套。**该对合律本身也可用同一个 `semiformula_result_induction` 证**（`neg` 也是 `UformulaRec1` 的构造），是下一步的自然目标 |
| `all` / `exs` | `result_all`/`result_exs` 的展开涉及 `allSize`/`allChanges` 与 `∷ 0` 的向量索引，需要额外的算术引理；归纳假设给的是 `iT (allChanges param i) (neg p)`，与目标里的层数要对齐 |

## 一个技术要点

`neg_and`/`neg_or`（ℒₛₑₜ 侧）需要 `IsUFormula` 而不是 `IsSemiformula`，
而目标里的 `iT param p` 的 `IsUFormula` 要由 `isSemiformula_iT` 提供
（`IsSemiformula ℒₛₑₜ param (iT param p)` 的 `.isUFormula`）。
把这些作为显式假设传入可以避免 `isDefEq` 超时（本机实测需要
`set_option maxHeartbeats 800000`）。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

namespace GodelQ.ShCraigElimNegFilled

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`verum` 支**：`neg ⊤ = ⊥`，`iT` 不动真假。 -/
lemma neg_verum_branch (n param : V) :
    iT param (neg ℒₒᵣ (^⊤ : V)) = neg ℒₛₑₜ (iT.construction.verum param) := by
  rw [neg_verum (L := ℒₒᵣ), iT_falsum]
  show (^⊥ : V) = neg ℒₛₑₜ (^⊤ : V)
  exact (neg_verum (L := ℒₛₑₜ)).symm

/-- **`falsum` 支**：对偶。 -/
lemma neg_falsum_branch (n param : V) :
    iT param (neg ℒₒᵣ (^⊥ : V)) = neg ℒₛₑₜ (iT.construction.falsum param) := by
  rw [neg_falsum (L := ℒₒᵣ), iT_verum]
  show (^⊤ : V) = neg ℒₛₑₜ (^⊥ : V)
  exact (neg_falsum (L := ℒₛₑₜ)).symm

/-- **`rel` 支**：`neg (rel …) = nrel …`，而 `iT` 把 `rel` 送到 `iTR`、`nrel` 送到 `neg iTR`。 -/
lemma neg_rel_branch (n param k R v : V)
    (hR : (ℒₒᵣ).IsRel k R) (hv : IsUTermVec ℒₒᵣ k v) :
    iT param (neg ℒₒᵣ (^rel k R v)) = neg ℒₛₑₜ (iT param (^rel k R v)) := by
  rw [neg_rel (L := ℒₒᵣ) hR hv, iT_nrel hR hv, iT_rel hR hv]

/-- **`and` 支**：`neg (p ⋏ q) = neg p ⋎ neg q`，配 De Morgan 与归纳假设。 -/
lemma neg_and_branch (n param p q : V)
    (hp : IsSemiformula ℒₒᵣ n p) (hq : IsSemiformula ℒₒᵣ n q)
    (ihp : iT param (neg ℒₒᵣ p) = neg ℒₛₑₜ (iT param p))
    (ihq : iT param (neg ℒₒᵣ q) = neg ℒₛₑₜ (iT param q))
    (hsp : IsSemiformula ℒₛₑₜ param (iT param p))
    (hsq : IsSemiformula ℒₛₑₜ param (iT param q)) :
    iT param (neg ℒₒᵣ (p ^⋏ q)) = neg ℒₛₑₜ (iT param (p ^⋏ q)) := by
  have hup : IsUFormula ℒₒᵣ p := hp.isUFormula
  have huq : IsUFormula ℒₒᵣ q := hq.isUFormula
  rw [neg_and (L := ℒₒᵣ) hup huq]
  rw [iT_or hup.neg huq.neg]
  rw [iT_and hup huq]
  rw [neg_and (L := ℒₛₑₜ) hsp.isUFormula hsq.isUFormula]
  rw [← ihp, ← ihq]

/-- **`or` 支**：对偶。 -/
lemma neg_or_branch (n param p q : V)
    (hp : IsSemiformula ℒₒᵣ n p) (hq : IsSemiformula ℒₒᵣ n q)
    (ihp : iT param (neg ℒₒᵣ p) = neg ℒₛₑₜ (iT param p))
    (ihq : iT param (neg ℒₒᵣ q) = neg ℒₛₑₜ (iT param q))
    (hsp : IsSemiformula ℒₛₑₜ param (iT param p))
    (hsq : IsSemiformula ℒₛₑₜ param (iT param q)) :
    iT param (neg ℒₒᵣ (p ^⋎ q)) = neg ℒₛₑₜ (iT param (p ^⋎ q)) := by
  have hup : IsUFormula ℒₒᵣ p := hp.isUFormula
  have huq : IsUFormula ℒₒᵣ q := hq.isUFormula
  rw [neg_or (L := ℒₒᵣ) hup huq]
  rw [iT_and hup.neg huq.neg]
  rw [iT_or hup huq]
  rw [neg_or (L := ℒₛₑₜ) hsp.isUFormula hsq.isUFormula]
  rw [← ihp, ← ihq]

end GodelQ.ShCraigElimNegFilled

#print axioms GodelQ.ShCraigElimNegFilled.neg_verum_branch
#print axioms GodelQ.ShCraigElimNegFilled.neg_falsum_branch
#print axioms GodelQ.ShCraigElimNegFilled.neg_rel_branch
#print axioms GodelQ.ShCraigElimNegFilled.neg_and_branch
#print axioms GodelQ.ShCraigElimNegFilled.neg_or_branch
