import GodelQ.ZFC.NegInvolution
import GodelQ.ZFC.ShCraigElimNegFilled

/-!
# CG-007 · W8 第二层（九）：一般（V 内任意公式码）的 `iT` 与 `neg` 相容律

`hAxL` / `hCut` / `hShift` 三支需要
`iT n (neg ℒₒᵣ p) = neg ℒₛₑₜ (iT n p)`（`p` 是 V 内任意公式码，可能非标准）。
`iT_quote_neg` 只对引号化（元层标准）公式给交换律，不能直接用在 `induction1` 的支里。

## 做法（与 Foundation 的 `substs_neg` 同形）

用 `IsSemiformula.pi1_structural_induction`，谓词取

```lean
P n p := iT n (neg ℒₒᵣ p) = neg ℒₛₑₜ (iT n p)
```

九个支：

* `rel` / `verum` / `falsum` / `and` / `or` 用 `ShCraigElimNegFilled` 里已证的
  `neg_rel_branch`、`neg_verum_branch`、`neg_falsum_branch`、`neg_and_branch`、`neg_or_branch`
  （后两支需要 `IsSemiformula ℒₛₑₜ n (iT n p)`，由 `isSemiformula_iT` 提供）。
* `nrel` 支需要码层面的对合律：`neg_nrel` 把左边化成 `iT n (^rel …)`，
  `iT_rel`/`iT_nrel` 把两边都化成 `iTR` 与 `neg (neg (iTR))`，
  再用 `NegInvolution.neg_neg_code` 的对合律（经 `IsUFormula.neg_neg`）。
* `all` / `exs` 支：`neg_all`/`neg_ex`（ℒₒᵣ 侧）把 `neg` 推进量词，
  `iT_all`/`iT_exs` 各把层数提升一（`n ↦ n+1`），这正是归纳假设的层数；
  ℒₛₑₜ 侧再用 `neg_all`/`neg_ex`，最后把 `neg (imp a b)` 展开成
  `neg (neg a) ⋏ neg b`（`imp` 的定义）并用 `IsUFormula.neg_neg` 消去双重否定。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate GodelQ.ShCraigElimNegFilled

namespace GodelQ.ShCraigElimNegLaw

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

set_option maxHeartbeats 800000 in
/-- **一般版本的 `iT`/`neg` 相容律**：对 V 内任意公式码 `p`（层数 `n`）成立。 -/
theorem iT_neg : ∀ {n p : V}, IsSemiformula ℒₒᵣ n p →
    iT n (neg ℒₒᵣ p) = neg ℒₛₑₜ (iT n p) := by
  refine IsSemiformula.pi1_structural_induction (V := V) (L := ℒₒᵣ)
    (P := fun n p => iT n (neg ℒₒᵣ p) = neg ℒₛₑₜ (iT n p))
    ?_ ?_ ?_ ?_ ?_ ?_ ?_ ?_ ?_
  · definability
  · intro n k R v hR hv
    exact neg_rel_branch n n k R v hR hv.isUTerm
  · intro n k R v hR hv
    rw [neg_nrel (L := ℒₒᵣ) hR hv.isUTerm, iT_rel hR hv.isUTerm, iT_nrel hR hv.isUTerm]
    exact (IsUFormula.neg_neg (isSemiformula_iTR hR hv).isUFormula).symm
  · intro n
    rw [iT_verum]
    exact neg_verum_branch n n
  · intro n
    rw [iT_falsum]
    exact neg_falsum_branch n n
  · intro n p q hp hq ihp ihq
    exact neg_and_branch n n p q hp hq ihp ihq
      (isSemiformula_iT p hp) (isSemiformula_iT q hq)
  · intro n p q hp hq ihp ihq
    exact neg_or_branch n n p q hp hq ihp ihq
      (isSemiformula_iT p hp) (isSemiformula_iT q hq)
  · intro n p hp ih
    rw [neg_all (L := ℒₒᵣ) hp.isUFormula, iT_exs (IsUFormula.neg hp.isUFormula),
      iT_all hp.isUFormula]
    rw [neg_all (L := ℒₛₑₜ) (IsUFormula.imp.mpr
      ⟨(isSemiformula_domZero (n := n)).isUFormula, (isSemiformula_iT p hp).isUFormula⟩)]
    have hneg : neg ℒₛₑₜ (imp ℒₛₑₜ domZero (iT (n+1) p)) =
        (neg ℒₛₑₜ (neg ℒₛₑₜ domZero) ^⋏ neg ℒₛₑₜ (iT (n+1) p) : V) :=
      neg_or (L := ℒₛₑₜ) (isSemiformula_domZero (n := n)).isUFormula.neg
        (isSemiformula_iT p hp).isUFormula
    rw [hneg, IsUFormula.neg_neg (isSemiformula_domZero (n := n)).isUFormula, ← ih]
  · intro n p hp ih
    rw [neg_ex (L := ℒₒᵣ) hp.isUFormula, iT_all (IsUFormula.neg hp.isUFormula),
      iT_exs hp.isUFormula]
    rw [neg_ex (L := ℒₛₑₜ) (IsUFormula.and.mpr
      ⟨(isSemiformula_domZero (n := n)).isUFormula, (isSemiformula_iT p hp).isUFormula⟩)]
    have hneg : neg ℒₛₑₜ (domZero ^⋏ iT (n+1) p) =
        (neg ℒₛₑₜ domZero ^⋎ neg ℒₛₑₜ (iT (n+1) p) : V) :=
      neg_and (L := ℒₛₑₜ) (isSemiformula_domZero (n := n)).isUFormula
        (isSemiformula_iT p hp).isUFormula
    rw [hneg, ← ih]
    rfl

end GodelQ.ShCraigElimNegLaw

#print axioms GodelQ.ShCraigElimNegLaw.iT_neg
