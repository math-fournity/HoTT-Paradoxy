import GodelQ.ZFC.SeqTranslateFormula

/-!
# CG-007 · W8 第二层（九）：一般（V 内任意公式码）的 `iT` 与 `neg` 相容律

`hAxL` / `hCut` / `hShift` 三支需要
`iT n (neg ℒₒᵣ p) = neg ℒₛₑₜ (iT n p)`（`p` 是 V 内任意公式码，可能非标准）。
`iT_quote_neg` 只对引号化（元层标准）公式给交换律，不能直接用在 `induction1` 的支里，
所以这里走 `semiformula_result_induction`（与 `isSemiformula_iT` 同形）在 V 内部证一般版本。

归纳谓词取 `P param n p q := iT param (neg p) = neg q`，其中 `q` 由原理固定为
`iT.construction.result ℒₒᵣ param p`。`iT` 改层（`all`/`exs` 支 `param' = n+1`），
故 `hall`/`hexs` 支的递归把 `param` 提升后仍需把 `q` 还原到 `iT n (...)` 的形状；
这里用 `iT_all`/`iT_exs` 的 `@[simp]` 形式加 `imp`/`congrArg` 衔接。
原子 `nrel` 支用 `IsUFormula.neg_neg` 在 `iTR` 上抵消一次 `neg`（`neg (neg x) = x`）。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

namespace GodelQ.ShCraigElimNegLaw

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- `iTR` 的产物是 `ℒₛₑₜ` 的公式（无层数约束），由 `IsUFormula` 的结构引理拼出。

`iTR n k R v = qqAlls (imp (conjunct 2 n 0 i₀ ^⋏ (conjunct 2 n 1 i₁ ^⋏ ⊤)) (subst ?[^#0,^#1] (cRel R))) 2`，
其中 `i₀ = iVE n v.[0]`、`i₁ = iVE n v.[1]`。逐段用 `IsUFormula.qqAlls` / `IsUFormula.imp` /
`IsUFormula.and` / `IsUFormula.verum` / `IsUFormula.subst` / `IsUFormula.rel`。
cRel 的两个候选都是 ℕ 层常量引号的 `rel`，故是 `IsUFormula`。 -/
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

/-- **一般版本的 `iT`/`neg` 相容律**：对 V 内任意公式码 `p`（层数 `n`）成立。 -/
theorem iT_neg {n : V} : ∀ p, IsSemiformula ℒₒᵣ n p →
    iT n (neg ℒₒᵣ p) = neg ℒₛₑₜ (iT n p) := by
  have key : ∀ {param n p : V}, IsSemiformula ℒₒᵣ n p →
      iT param (neg ℒₒᵣ p) = neg ℒₛₑₜ (iT.construction.result ℒₒᵣ param p) :=
    UformulaRec1.Construction.semiformula_result_induction
      (V := V) (c := iT.construction) (L := ℒₒᵣ)
      (P := fun param n p q => iT param (neg ℒₒᵣ p) = neg ℒₛₑₜ q)
      ?_ ?_ ?_ ?_ ?_ ?_ ?_ ?_ ?_
  · intro p hp
    simpa [iT] using (key hp)
  · definability
  · intro n param k R v hR hv
    show iT param (neg ℒₒᵣ (^rel k R v)) = neg ℒₛₑₜ (iT.construction.rel param k R v)
    rw [iT_rel hR hv, iT.construction.rel, iT_nrel hR hv, iT.construction.rel]; rfl
  · intro n param k R v hR hv
    show iT param (neg ℒₒᵣ (^nrel k R v)) = neg ℒₛₑₜ (iT.construction.nrel param k R v)
    rw [iT_nrel hR hv, iT.construction.nrel]
    rw [IsUFormula.neg_neg (isUFormula_iTR hR hv), iT_rel hR hv, iT.construction.rel]; rfl
  · intro n param
    show iT param (neg ℒₒᵣ (^⊤)) = neg ℒₛₑₜ (iT.construction.verum param)
    rw [iT_verum, iT.construction.verum]; rfl
  · intro n param
    show iT param (neg ℒₒᵣ (^⊥)) = neg ℒₛₑₜ (iT.construction.falsum param)
    rw [iT_falsum, iT.construction.falsum]; rfl
  · intro n param p q hp hq ihp ihq
    rw [iT_and hp.isUFormula hq.isUFormula, iT.construction.and,
      neg_and (L := ℒₛₑₜ) (isSemiformula_iT p hp).isUFormula
        (isSemiformula_iT q hq).isUFormula, ihp, ihq]
  · intro n param p q hp hq ihp ihq
    rw [iT_or hp.isUFormula hq.isUFormula, iT.construction.or,
      neg_or (L := ℒₛₑₜ) (isSemiformula_iT p hp).isUFormula
        (isSemiformula_iT q hq).isUFormula, ihp, ihq]
  · intro n param p hp ih
    rw [neg_all (L := ℒₒᵣ) hp.isUFormula, iT_exs (IsUFormula.neg hp.isUFormula), imp]
    rw [UformulaRec1.Construction.result_all (V := V) (c := iT.construction) (L := ℒₒᵣ)
      hp.isUFormula (rfl : iT.construction.allSize param (^∀ p) = 1)]
    rw [neg_all (L := ℒₛₑₜ) (IsUFormula.imp (isSemiformula_domZero (n := n + 1)).isUFormula
      (isSemiformula_iT p hp).isUFormula), imp, IsUFormula.neg_neg (isSemiformula_iT p hp).isUFormula]
    exact congrArg (fun x => (^∃ (domZero ^⋏ x : V))) (ih 0 (by simp) (by simp))
  · intro n param p hp ih
    rw [neg_ex (L := ℒₒᵣ) hp.isUFormula, iT_all (IsUFormula.neg hp.isUFormula), imp]
    rw [UformulaRec1.Construction.result_exs (V := V) (c := iT.construction) (L := ℒₒᵣ)
      hp.isUFormula (rfl : iT.construction.exsSize param (^∃ p) = 1)]
    rw [neg_ex (L := ℒₛₑₜ) (IsUFormula.imp (isSemiformula_domZero (n := n + 1)).isUFormula
      (isSemiformula_iT p hp).isUFormula), imp, IsUFormula.neg_neg (isSemiformula_iT p hp).isUFormula]
    exact congrArg (fun x => (^∀ (imp ℒₛₑₜ domZero x : V))) (ih 0 (by simp) (by simp))

end GodelQ.ShCraigElimNegLaw

#print axioms GodelQ.ShCraigElimNegLaw.iT_neg
