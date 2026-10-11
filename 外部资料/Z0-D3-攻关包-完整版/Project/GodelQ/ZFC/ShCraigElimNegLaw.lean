import GodelQ.ZFC.SeqTranslateFormula

/-!
# CG-007 · W8 第二层（九）：一般（V 内任意公式码）的 `iT` 与 `neg` 相容律

`hAxL` / `hCut` / `hShift` 三支需要
`iT n (neg ℒₒᵣ p) = neg ℒₛₑₜ (iT n p)`（`p` 是 V 内任意公式码，可能非标准）。
`iT_quote_neg` 只对引号化（元层标准）公式给交换律，不能直接用在 `induction1` 的支里，
所以这里走 `semiformula_result_induction`（与 `isSemiformula_iT` 同形）在 V 内部证一般版本。

谓词 `P param n p q := iT param (neg ℒₒᵣ p) = neg ℒₛₑₜ q` 被原理接受：原理把 `q` 固定成
`iT.construction.result ℒₒᵣ param p`，于是 `P param n p (result param p)` 正是所要等式。

`nrel` / `all` / `exs` 支用到码层面的 `neg` 对合 `neg (neg x) = x`：Foundation 没有单独的码层面引理，
但 `neg` 本身是 `UformulaRec1` 构造，对任何 `IsUFormula x` 有 `IsUFormula.neg_neg : neg (neg x) = x`
（本项目 `Foundation` 的 `Formula/Functions.lean:127`），而 `iTR` / `iT (...) ` 都是 `IsUFormula`。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

namespace GodelQ.ShCraigElimNegLaw

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **一般版本的 `iT`/`neg` 相容律**：对 V 内任意公式码 `p`（层数 `n`）成立。 -/
theorem iT_neg {n : V} : ∀ p, IsSemiformula ℒₒᵣ n p →
    iT n (neg ℒₒᵣ p) = neg ℒₛₑₜ (iT n p) := by
  have key : ∀ {param n p : V}, IsSemiformula ℒₒᵣ n p →
      iT param (neg ℒₒᵣ p) = neg ℒₛₑₜ (iT.construction.result ℒₒᵣ param p) :=
    UformulaRec1.Construction.semiformula_result_induction
      (V := V) (c := iT.construction) (L := ℒₒᵣ)
      (P := fun param _n p q => iT param (neg ℒₒᵣ p) = neg ℒₛₑₜ q)
      (by definability)
      (by intro n param k R v hR hv
        simp [iT.construction]
        rw [neg_rel (L := ℒₒᵣ) hR hv, iT_nrel hR hv, iT_rel hR hv])
      (by intro n param k R v hR hv
        simp [iT.construction]
        rw [neg_nrel (L := ℒₒᵣ) hR hv, iT_rel hR hv,
          IsUFormula.neg_neg (isSemiformula_iTR hR hv).isUFormula,
          iT_nrel hR hv])
      (by intro n param
        simp [iT.construction]
        rw [neg_verum (L := ℒₒᵣ), iT_falsum, neg_verum (L := ℒₛₑₜ)]
        rfl)
      (by intro n param
        simp [iT.construction]
        rw [neg_falsum (L := ℒₒᵣ), iT_verum, neg_falsum (L := ℒₛₑₜ)]
        rfl)
      (by intro n param p q hp hq ihp ihq
        have hsp := (isSemiformula_iT p hp).isUFormula
        have hsq := (isSemiformula_iT q hq).isUFormula
        simp [iT.construction]
        rw [neg_and (L := ℒₒᵣ) hp.isUFormula hq.isUFormula,
          iT_or hp.isUFormula.neg hq.isUFormula.neg, ← ihp, ← ihq,
          neg_and (L := ℒₛₑₜ) hsp hsq, iT_and hp.isUFormula hq.isUFormula])
      (by intro n param p q hp hq ihp ihq
        have hsp := (isSemiformula_iT p hp).isUFormula
        have hsq := (isSemiformula_iT q hq).isUFormula
        simp [iT.construction]
        rw [neg_or (L := ℒₒᵣ) hp.isUFormula hq.isUFormula,
          iT_and hp.isUFormula.neg hq.isUFormula.neg, ← ihp, ← ihq,
          neg_or (L := ℒₛₑₜ) hsp hsq, iT_or hp.isUFormula hq.isUFormula])
      (by intro n param p hp ih
        have hsp := (isSemiformula_iT p hp).isUFormula
        simp [iT.construction]
        rw [neg_all (L := ℒₒᵣ) hp.isUFormula, iT_exs hp.isUFormula.neg,
          ← ih 0 (by simp : 0 < iT.construction.allSize param (^∀ p)),
          neg_ex (L := ℒₛₑₜ) (IsUFormula.imp
            (isSemiformula_domZero (n := n + 1)).isUFormula hsp),
          imp, neg_or (L := ℒₛₑₜ),
          IsUFormula.neg_neg (isSemiformula_domZero (n := n + 1)).isUFormula,
          iT_all hp.isUFormula])
      (by intro n param p hp ih
        have hsp := (isSemiformula_iT p hp).isUFormula
        simp [iT.construction]
        rw [neg_ex (L := ℒₒᵣ) hp.isUFormula, iT_all hp.isUFormula.neg,
          ← ih 0 (by simp : 0 < iT.construction.exsSize param (^∃ p)),
          neg_all (L := ℒₛₑₜ) (IsUFormula.imp
            (isSemiformula_domZero (n := n + 1)).isUFormula hsp),
          imp, neg_or (L := ℒₛₑₜ),
          IsUFormula.neg_neg (isSemiformula_domZero (n := n + 1)).isUFormula,
          iT_exs hp.isUFormula])
  · intro p hp
    simpa [iT] using key hp

end GodelQ.ShCraigElimNegLaw

#print axioms GodelQ.ShCraigElimNegLaw.iT_neg
