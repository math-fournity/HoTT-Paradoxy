import GodelQ.ZFC.SeqTranslateFormula

/-!
# CG-007 · W8 第二层（九）：一般（V 内任意公式码）的 `iT` 与 `neg` 相容律

`hAxL` / `hCut` / `hShift` 三支需要
`iT n (neg ℒₒᵣ p) = neg ℒₛₑₜ (iT n p)`（`p` 是 V 内任意公式码，可能非标准）。
`iT_quote_neg` 只对引号化（元层标准）公式给交换律，不能直接用在 `induction1` 的支里，
所以这里走 `semiformula_result_induction`（与 `isSemiformula_iT` 同形）在 V 内部证一般版本。

归纳谓词取 `P param n p q := param = n → iT param (neg ℒₒᵣ p) = neg ℒₛₑₜ (iT param p)`，
结论用 `iT param p`（非原始 `iT.construction.result`），使 `iT_all`/`iT_exs` 能直接匹配两侧。
原子 `nrel` 支用 `IsUFormula.neg_neg` 在 `iTR` 上抵消一次 `neg`。
`iT.construction` 的字段（`rel`/`nrel`/`verum`/`falsum`/`and`/`or`）按
`InternalTranslate.lean:231-253` 的逐字段定义直接内联展开。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

namespace GodelQ.ShCraigElimNegLaw

set_option maxHeartbeats 2000000

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

open FFL.FirstOrder.Arithmetic.Bootstrapping.Syntax.Formula

/-- `neg (imp ℒₛₑₜ domZero x) = domZero ^⋏ neg x`。 -/
@[simp] lemma neg_imp_domZero {x : V} (hx : IsUFormula ℒₛₑₜ x) :
    neg ℒₛₑₜ (imp ℒₛₑₜ domZero x) = domZero ^⋏ neg ℒₛₑₜ x := by
  rw [imp, neg_and (L := ℒₛₑₜ), neg_falsum (L := ℒₛₑₜ), IsUFormula.neg_neg hx]; simp

/-- `iTR` 的产物是 `ℒₛₑₜ` 的公式（无层数约束），由 `isSemiformula_iTR` 直接给出 `IsUFormula`。 -/
lemma isUFormula_iTR {n k R v : V} (hR : (ℒₒᵣ).IsRel k R) (hv : IsUTermVec ℒₒᵣ k v) :
    IsUFormula ℒₛₑₜ (iTR n k R v) :=
  (isSemiformula_iTR hR hv).isUFormula

/-- `neg (imp L domZero x) = domZero ^⋏ neg x`。 -/
lemma neg_imp_domZero {x : V} (hx : IsUFormula Ls x) :
    neg Ls (imp Ls domZero x) = domZero ^⋏ neg Ls x := by
  rw [imp, neg_and (L := Ls), neg_falsum (L := Ls), IsUFormula.neg_neg hx]; simp

/-! **一般版本的 `iT`/`neg` 相容律**：对 V 内任意公式码 `p`（层数 `n`）成立。
`iT` 改层（`all`/`exs` 支引入 `param+1`），故归纳谓词带 `param = n` 护罩，否则递归层数与
`isSemiformula_iT` 不一致，证不出来。all/exs 支使用 `iT (param+1) (neg p)` 的字段展开 +
归纳假设 `ih h`（字段形式），不用 `iT_all`/`iT_exs`（后者只改写 `^∀ p`/`^∃ p`，不处理外面的 `neg`）。 -/
theorem iT_neg {n : V} : ∀ p, IsSemiformula ℒₒᵣ n p →
    iT n (neg ℒₒᵣ p) = neg ℒₛₑₜ (iT n p) := by
  have key : ∀ {param n p : V}, IsSemiformula ℒₒᵣ n p →
      param = n → iT param (neg ℒₒᵣ p) = neg ℒₛₑₜ (iT.construction.result ℒₒᵣ param p) :=
    UformulaRec1.Construction.semiformula_result_induction
      (V := V) (c := iT.construction) (L := ℒₒᵣ)
      (P := fun param n p q => param = n → iT param (neg ℒₒᵣ p) = neg ℒₛₑₜ q)
      ?_ ?_ ?_ ?_ ?_ ?_ ?_ ?_ ?_
  · intro p hp
    simpa [iT] using key hp rfl
  · definability
  · intro n param k R v hR hv h
    rw [← h] at hv
    show iT param (neg ℒₒᵣ (^rel k R v)) = neg ℒₛₑₜ (iTR param k R v)
    rw [neg_rel (L := ℒₒᵣ) hR hv.isUTerm, iT_nrel hR hv.isUTerm]; rfl
  · intro n param k R v hR hv h
    rw [← h] at hv
    show iT param (neg ℒₒᵣ (^nrel k R v)) = neg ℒₛₑₜ (neg ℒₛₑₜ (iTR param k R v))
    rw [neg_nrel (L := ℒₒᵣ) hR hv.isUTerm, iT_rel hR hv.isUTerm]
    exact IsUFormula.neg_neg (isUFormula_iTR hR hv.isUTerm)
  · intro n param h
    show iT param (neg ℒₒᵣ (^⊤)) = neg ℒₛₑₜ (^⊥)
    rw [neg_verum (L := ℒₒᵣ), iT_falsum]; rfl
  · intro n param h
    show iT param (neg ℒₒᵣ (^⊥)) = neg ℒₛₑₜ (^⊤)
    rw [neg_falsum (L := ℒₒᵣ), iT_verum]; rfl
  · intro n param p q hp hq ihp ihq h
    rw [← h] at hp hq
    rw [neg_and (L := ℒₒᵣ) hp.isUFormula hq.isUFormula, iT_or (IsUFormula.neg hp.isUFormula)
      (IsUFormula.neg hq.isUFormula)]
    rw [neg_or (L := ℒₛₑₜ) (isSemiformula_iT p hp).isUFormula (isSemiformula_iT q hq).isUFormula]
    exact congrArg₂ (· ^⋎ ·) (ihp h) (ihq h)
  · intro n param p q hp hq ihp ihq h
    rw [← h] at hp hq
    rw [neg_or (L := ℒₒᵣ) hp.isUFormula hq.isUFormula, iT_and (IsUFormula.neg hp.isUFormula)
      (IsUFormula.neg hq.isUFormula)]
    rw [neg_and (L := ℒₛₑₜ) (isSemiformula_iT p hp).isUFormula (isSemiformula_iT q hq).isUFormula]
    exact congrArg₂ (· ^⋏ ·) (ihp h) (ihq h)
  · intro n param p hp ih h
    rw [← h] at hp
    rw [neg_all (L := ℒₒᵣ) hp.isUFormula, iT_exs (IsUFormula.neg hp.isUFormula)]
    rw [show iT (param + 1) (neg ℒₒᵣ p) = iT (iT.construction.exsChanges param 0) (neg ℒₒᵣ p) by simp [iT.construction]]
    rw [← ih 0 (by simp [iT.construction]) (by simp [iT.construction, h])]
    simpa [iT.construction, neg, imp, domZero]
  · intro n param p hp ih h
    rw [← h] at hp
    rw [neg_ex (L := ℒₒᵣ) hp.isUFormula, iT_all (IsUFormula.neg hp.isUFormula)]
    rw [show iT (param + 1) (neg ℒₒᵣ p) = iT (iT.construction.exsChanges param 0) (neg ℒₒᵣ p) by simp [iT.construction]]
    rw [← ih 0 (by simp [iT.construction]) (by simp [iT.construction, h])]
    simpa [iT.construction, neg, imp, domZero]