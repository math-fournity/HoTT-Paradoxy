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

/-- `iTR` 的产物是 `ℒₛₑₜ` 的公式（无层数约束），由 `IsUFormula` 的结构引理拼出。 -/
lemma isUFormula_iTR {n k R v : V} (hR : (ℒₒᵣ).IsRel k R) (hv : IsUTermVec ℒₒᵣ k v) :
    IsUFormula ℒₛₑₜ (iTR n k R v) := by
  rw [iTR]
  apply IsUFormula.qqAlls
  apply IsUFormula.imp
  · rw [IsUFormula.and]
    refine ⟨?_, ?_⟩
    · rw [conjunct]; apply IsUFormula.and
      refine ⟨IsUFormula.subst (isSemiformula_cDomN.isUFormula)
        (IsSemitermVec.singleton.mpr ?_), ?_⟩
      · rw [IsSemiterm.bvar]; simp
      · rw [conjunct]; apply IsUFormula.and
        refine ⟨IsUFormula.subst (isSemiformula_iVE (hv.nth (i := 0) (by simp))).isUFormula
          (IsSemitermVec.cons_iff.mpr
            ⟨IsSemiterm.bvar.mpr (by simp), isSemitermVec_shiftVec 2 2⟩), ?_⟩
        · exact IsUFormula.verum
    · rw [conjunct]; apply IsUFormula.and
      refine ⟨IsUFormula.subst (isSemiformula_cDomN.isUFormula)
        (IsSemitermVec.singleton.mpr ?_), ?_⟩
      · rw [IsSemiterm.bvar]; simp
      · rw [conjunct]; apply IsUFormula.and
        refine ⟨IsUFormula.subst (isSemiformula_iVE (hv.nth (i := 1) (by simp))).isUFormula
          (IsSemitermVec.cons_iff.mpr
            ⟨IsSemiterm.bvar.mpr (by simp), isSemitermVec_shiftVec 2 2⟩), ?_⟩
        · exact IsUFormula.verum
  · apply IsUFormula.subst (IsUFormula.rel.mpr ⟨?_, ?_⟩)
    · simp [cRel]
      split <;> rw [IsUFormula.rel]; use isSemiformula_cRel.isUFormula.1
    · rw [IsSemitermVec.cons_iff]
      refine ⟨IsSemiterm.bvar.mpr (by simp), ?_⟩
      rw [IsSemitermVec.cons_iff]
      refine ⟨IsSemiterm.bvar.mpr (by simp), by simp⟩

/-- 对 `imp ℒₛₑₜ domZero x` 取 `neg` 的展开：`neg (imp domZero x) = domZero ^⋏ neg x`。 -/
lemma neg_imp_domZero {x : V} (hx : IsUFormula ℒₛₑₜ x) :
    neg ℒₛₑₜ (imp ℒₛₑₜ domZero x) = domZero ^⋏ neg ℒₛₑₜ x := by
  rw [imp, neg_or, neg_falsum (L := ℒₛₑₜ), IsUFormula.neg_neg hx]; simp

/-- **一般版本的 `iT`/`neg` 相容律**：对 V 内任意公式码 `p`（层数 `n`）成立。 -/

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
    rw [neg_or (L := ℒₛₑₜ) (isSemiformula_iT p hp).isUFormula
      (isSemiformula_iT q hq).isUFormula, ihp (by simp) h, ihq (by simp) h]
  · intro n param p q hp hq ihp ihq h
    rw [← h] at hp hq
    rw [neg_or (L := ℒₒᵣ) hp.isUFormula hq.isUFormula, iT_and (IsUFormula.neg hp.isUFormula)
      (IsUFormula.neg hq.isUFormula)]
    rw [neg_and (L := ℒₛₑₜ) (isSemiformula_iT p hp).isUFormula
      (isSemiformula_iT q hq).isUFormula, ihp (by simp) h, ihq (by simp) h]
  · intro n param p hp ih h
    rw [← h] at hp
    have hdom : IsUFormula ℒₛₑₜ domZero := (isSemiformula_domZero (n := param)).isUFormula
    have hres : IsUFormula ℒₛₑₜ (iT.construction.result ℒₒᵣ (param + 1) p) :=
      (isSemiformula_iT (param + 1) p hp).isUFormula
    rw [neg_all (L := ℒₒᵣ) hp.isUFormula, iT_exs (IsUFormula.neg hp.isUFormula)]
    rw [UformulaRec1.Construction.result_all (V := V) (c := iT.construction) (L := ℒₒᵣ)
      hp.isUFormula (rfl : iT.construction.allSize param (^∀ p) = 1)]
    rw [neg_all (L := ℒₛₑₜ) hres, neg_imp_domZero hres, IsUFormula.neg_neg hres]
    exact congrArg (fun x => (^∃ (domZero ^⋏ x : V)))
      (ih 0 (by simp [iT.construction]) (by simp [iT.construction, h]))
  · intro n param p hp ih h
    rw [← h] at hp
    have hdom : IsUFormula ℒₛₑₜ domZero := (isSemiformula_domZero (n := param)).isUFormula
    have hres : IsUFormula ℒₛₑₜ (iT.construction.result ℒₒᵣ (param + 1) p) :=
      (isSemiformula_iT (param + 1) p hp).isUFormula
    have hQ : IsUFormula ℒₛₑₜ (^∃ (domZero ^⋏ iT.construction.result ℒₒᵣ (param + 1) p)) :=
      IsUFormula.and.mpr ⟨hdom, hres⟩
    rw [neg_ex (L := ℒₒᵣ) hp.isUFormula, iT_all (IsUFormula.neg hp.isUFormula)]
    rw [UformulaRec1.Construction.result_exs (V := V) (c := iT.construction) (L := ℒₒᵣ)
      hp.isUFormula (rfl : iT.construction.exsSize param (^∃ p) = 1)]
    rw [neg_ex (L := ℒₛₑₜ) hQ, IsUFormula.neg hQ,
      neg_and (L := ℒₛₑₜ) hdom hres, IsUFormula.neg_neg hres]
    exact congrArg (fun x => (^∀ (imp ℒₛₑₜ domZero x : V)))
      (ih 0 (by simp [iT.construction]) (by simp [iT.construction, h]))

end GodelQ.ShCraigElimNegLaw

#print axioms GodelQ.ShCraigElimNegLaw.iT_neg
