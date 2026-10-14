import GodelQ.ZFC.NegInvolution

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

/-- **`nrel` 支**：`neg (nrel …) = rel …`，而 `iT` 把 `nrel` 送到 `neg iTR`、
`rel` 送到 `iTR`；再用码层面对合律 `neg (neg x) = x` 抵消。

对合律取自 `NegInvolution.neg_neg_code`（其底层是 Foundation 的 `IsUFormula.neg_neg`）。

`iTR param k R v` 的公式性以显式假设传入（与 `neg_and_branch` 的 `hsp`/`hsq` 同法）：
它由 `isSemiformula_iTR` 提供，但那条引理要 `IsSemitermVec ℒₒᵣ k param v`，
而归纳给的 `hv` 只是 `IsUTermVec`；把 `IsUFormula` 显式传入可避免层数对齐与
`listMax` 项带来的 `whnf` 开销。 -/
lemma neg_nrel_branch (n param k R v : V)
    (hR : (ℒₒᵣ).IsRel k R) (hv : IsUTermVec ℒₒᵣ k v)
    (hsi : IsUFormula ℒₛₑₜ (iTR param k R v)) :
    iT param (neg ℒₒᵣ (^nrel k R v)) = neg ℒₛₑₜ (iT param (^nrel k R v)) := by
  rw [neg_nrel (L := ℒₒᵣ) hR hv, iT_rel hR hv, iT_nrel hR hv]
  exact (IsUFormula.neg_neg hsi).symm

/-- `neg (imp domZero x) = domZero ^⋏ neg x`（`imp p q := neg p ⋎ q`，配 De Morgan）。

`x` 的公式性以 `IsUFormula` 给出；`domZero` 是 ℒₛₑₜ 的公式（`isSemiformula_domZero`）。 -/
lemma neg_imp_domZero {x : V} (hx : IsUFormula ℒₛₑₜ x)
    (hd : IsUFormula (V := V) ℒₛₑₜ domZero) :
    neg ℒₛₑₜ (imp ℒₛₑₜ domZero x) = domZero ^⋏ neg ℒₛₑₜ x := by
  have h1 : neg ℒₛₑₜ (neg ℒₛₑₜ domZero ^⋎ x) = neg ℒₛₑₜ (neg ℒₛₑₜ domZero) ^⋏ neg ℒₛₑₜ x :=
    neg_or (L := ℒₛₑₜ) hd.neg hx
  have h2 : neg ℒₛₑₜ (neg ℒₛₑₜ domZero) = domZero := IsUFormula.neg_neg hd
  show neg ℒₛₑₜ (neg ℒₛₑₜ domZero ^⋎ x) = domZero ^⋏ neg ℒₛₑₜ x
  rw [h1, h2]

/-- 对偶方向：`neg (domZero ^⋏ x) = imp domZero (neg x)`。

即 `neg_imp_domZero` 的对称形，`exs` 支的收尾要用它把 `^∀ neg (domZero ⋏ ·)`
换成 `^∀ imp domZero (neg ·)`。 -/
lemma neg_and_domZero {x : V} (hx : IsUFormula ℒₛₑₜ x)
    (hd : IsUFormula (V := V) ℒₛₑₜ domZero) :
    neg ℒₛₑₜ (domZero ^⋏ x) = imp ℒₛₑₜ domZero (neg ℒₛₑₜ x) := by
  show neg ℒₛₑₜ (domZero ^⋏ x) = neg ℒₛₑₜ domZero ^⋎ neg ℒₛₑₜ x
  exact neg_and (L := ℒₛₑₜ) hd hx

/-- **`all` 支**：`neg (∀¹p) = ∃¹ neg p`，`iT` 把 `∀` 送到 `∀(imp domZero ·)`、
`∃` 送到 `∃(domZero ⋏ ·)`；收尾用 `neg_imp_domZero` 把两边对上。

带 `param = n` 护罩（与 `isSemiformula_iT` 同形）：`hp` 给的是层数 `n + 1`，
而 `iT` 的递归在层数 `param + 1` 上；护罩把它们对齐。 -/
lemma neg_all_branch (n param p : V) (h : param = n)
    (hp : IsSemiformula ℒₒᵣ (n + 1) p)
    (ih : iT (param + 1) (neg ℒₒᵣ p) = neg ℒₛₑₜ (iT (param + 1) p)) :
    iT param (neg ℒₒᵣ (^∀ p)) = neg ℒₛₑₜ (iT param (^∀ p)) := by
  have hup : IsUFormula ℒₒᵣ p := hp.isUFormula
  have hp' : IsSemiformula ℒₒᵣ (param + 1) p := by rw [h]; exact hp
  have hsp : IsUFormula ℒₛₑₜ (iT (param + 1) p) :=
    (isSemiformula_iT (n := param + 1) p hp').isUFormula
  have hdz : IsUFormula ℒₛₑₜ domZero := (isSemiformula_domZero (n := param + 1)).isUFormula
  have hsi : IsUFormula ℒₛₑₜ (imp ℒₛₑₜ domZero (iT (param + 1) p)) :=
    IsUFormula.imp.mpr ⟨hdz, hsp⟩
  rw [neg_all (L := ℒₒᵣ) hup, iT_exs hup.neg, iT_all hup]
  show (^∃ (domZero ^⋏ iT (param + 1) (neg ℒₒᵣ p)) : V) =
    neg ℒₛₑₜ (^∀ (imp ℒₛₑₜ domZero (iT (param + 1) p)))
  rw [neg_all (L := ℒₛₑₜ) hsi, neg_imp_domZero hsp hdz]
  exact congrArg (fun x => (^∃ (domZero ^⋏ x) : V)) ih

/-- **`exs` 支**：`neg (∃¹p) = ∀¹ neg p`，对偶。 -/
lemma neg_exs_branch (n param p : V) (h : param = n)
    (hp : IsSemiformula ℒₒᵣ (n + 1) p)
    (ih : iT (param + 1) (neg ℒₒᵣ p) = neg ℒₛₑₜ (iT (param + 1) p)) :
    iT param (neg ℒₒᵣ (^∃ p)) = neg ℒₛₑₜ (iT param (^∃ p)) := by
  have hup : IsUFormula ℒₒᵣ p := hp.isUFormula
  have hp' : IsSemiformula ℒₒᵣ (param + 1) p := by rw [h]; exact hp
  have hsp : IsUFormula ℒₛₑₜ (iT (param + 1) p) :=
    (isSemiformula_iT (n := param + 1) p hp').isUFormula
  have hdz : IsUFormula ℒₛₑₜ domZero := (isSemiformula_domZero (n := param + 1)).isUFormula
  have hsa : IsUFormula ℒₛₑₜ (domZero ^⋏ iT (param + 1) p) :=
    IsUFormula.and.mpr ⟨hdz, hsp⟩
  rw [neg_ex (L := ℒₒᵣ) hup, iT_all hup.neg, iT_exs hup]
  show (^∀ (imp ℒₛₑₜ domZero (iT (param + 1) (neg ℒₒᵣ p))) : V) =
    neg ℒₛₑₜ (^∃ (domZero ^⋏ iT (param + 1) p))
  rw [neg_ex (L := ℒₛₑₜ) hsa]
  show (^∀ (imp ℒₛₑₜ domZero (iT (param + 1) (neg ℒₒᵣ p))) : V) =
    ^∀ (neg ℒₛₑₜ (domZero ^⋏ iT (param + 1) p))
  rw [show (^∀ (neg ℒₛₑₜ (domZero ^⋏ iT (param + 1) p)) : V) =
      ^∀ (imp ℒₛₑₜ domZero (neg ℒₛₑₜ (iT (param + 1) p))) from
    congrArg (fun y => (^∀ y : V)) (neg_and_domZero hsp hdz)]
  exact congrArg (fun y => (^∀ (imp ℒₛₑₜ domZero y) : V)) ih

end GodelQ.ShCraigElimNegFilled

#print axioms GodelQ.ShCraigElimNegFilled.neg_verum_branch
#print axioms GodelQ.ShCraigElimNegFilled.neg_falsum_branch
#print axioms GodelQ.ShCraigElimNegFilled.neg_rel_branch
#print axioms GodelQ.ShCraigElimNegFilled.neg_and_branch
#print axioms GodelQ.ShCraigElimNegFilled.neg_or_branch
#print axioms GodelQ.ShCraigElimNegFilled.neg_nrel_branch
#print axioms GodelQ.ShCraigElimNegFilled.neg_all_branch
#print axioms GodelQ.ShCraigElimNegFilled.neg_exs_branch
