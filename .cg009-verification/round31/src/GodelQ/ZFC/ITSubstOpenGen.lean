-- CG-009: **一般开口律 `iT_subst_open`（∀m，含 0）** —— statement 与承重支。
--
--      iT m (subst ℒₒᵣ (QvecVOr m) q) = subst ℒₛₑₜ (QvecV m) (iT (m+1) q)      (q : 层 m+1)
--
-- ## 分工（2026-10-13 Master 派工）
--   * rel 支：001-Flash 装配（零件 ITSubstOpen2-7 已齐，见其树）
--   * **本文件：谓词 + all/exs 支**（承重点：用归纳假设的 m+1 实例）
--
-- ## 为什么 all/exs 是承重的
-- m=0 的 all 支：`iT 0 (subst ?[^&0] (^∀ q'))` 下降一层后子目标 =
--   `iT 1 (subst (QvecVOr 1) q') = subst (QvecV 1) (iT 2 q')`
-- 即一般律在 m=1、q'（层 2）的实例（因 `qVec (QvecVOr m) = QvecVOr (m+1)`，
-- 递归在 QvecVOr 族下闭合）。公式深度无界，故连 m=0 都依赖一般律。
import GodelQ.ZFC.ITSubstOpen7
import GodelQ.ZFC.IVEOpenFull
open FFL FFL.FirstOrder FFL FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.ITSubstOpen3 GodelQ.ITSubstOpen4 GodelQ.ITSubstOpen5 GodelQ.ITSubstOpen6
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFull GodelQ.LayerMono

namespace GodelQ.ITSubstOpenGen

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **一般开口律**（statement，含 m = 0）。

证明用 `semiformula_result_induction`（Σ1 谓词，带 `param = m+1` 护罩），
照 `ITSubsts1.iT_substs1` 的模板：谓词把**层数**放在 `param` 里走，
`iT` 的量词支把 `param ↦ param+1`，而 `subst` 推过 `qqAlls` 时向量变成
`qVec (QvecVOr m) = QvecVOr (m+1)` —— **两者同步**，这就是定律为真的机制。 -/
theorem iT_subst_open (m : V) :
    ∀ (q : V), IsSemiformula ℒₒᵣ (m + 1) q →
      iT m (subst ℒₒᵣ (QvecVOr (V := V) m) q) = subst ℒₛₑₜ (QvecV (V := V) m) (iT (m + 1) q) := by
  intro q hq
  have key : ∀ {param n q : V}, IsSemiformula ℒₒᵣ n q → param = n → param = (m + 1) →
      iT m (subst ℒₒᵣ (QvecVOr (V := V) m) q)
        = subst ℒₛₑₜ (QvecV (V := V) m)
            (UformulaRec1.Construction.result ℒₒᵣ iT.construction param q) :=
    UformulaRec1.Construction.semiformula_result_induction
      (V := V) (c := iT.construction) (L := ℒₒᵣ)
      (P := fun param n q r => param = n → param = (m + 1) →
        iT m (subst ℒₒᵣ (QvecVOr (V := V) m) q)
          = subst ℒₛₑₜ (QvecV (V := V) m) r)
      ?_ ?_ ?_ ?_ ?_ ?_ ?_ ?_ ?_
  · have hh := key hq (rfl : m + 1 = m + 1) (rfl : m + 1 = m + 1)
    simpa only [iT] using hh
  · definability
  · -- rel（由 001-Flash 装配，此处略）
    all_goals sorry
  · -- nrel
    all_goals sorry
  · -- verum
    intro n param h h1
    -- 两侧都化到 `^⊤`：`iT` 的定义把 `iT p ^⊤` 算成 `verum p`
    rw [show iT.construction.verum param = iT param ^⊤ from (iT_verum param).symm]
    rw [Bootstrapping.substs_verum (L := ℒₒᵣ), iT_verum, iT_verum,
      Bootstrapping.substs_verum (L := ℒₛₑₜ)]
  · -- falsum
    intro n param h h1
    rw [show iT.construction.falsum param = iT param ^⊥ from (iT_falsum param).symm]
    rw [Bootstrapping.substs_falsum (L := ℒₒᵣ), iT_falsum, iT_falsum,
      Bootstrapping.substs_falsum (L := ℒₛₑₜ)]
  · -- and
    intro n param p q hp hq ihp ihq h h1
    have hp' := ihp h h1
    have hq' := ihq h h1
    have hn : n = m + 1 := h.symm.trans h1
    subst hn
    -- LHS：subst 先推过 ^⋏，再展 iT
    rw [Bootstrapping.substs_and (L := ℒₒᵣ) hp.isUFormula hq.isUFormula,
      iT_and (IsSemiformula.subst (L := ℒₒᵣ) hp (isSemitermVec_QvecVOr m)).isUFormula
             (IsSemiformula.subst (L := ℒₒᵣ) hq (isSemitermVec_QvecVOr m)).isUFormula]
    -- RHS：result 形 → iT 形 → ^⋏ 形 → subst 推过
    rw [show UformulaRec1.Construction.result ℒₒᵣ iT.construction param (p ^⋏ q)
          = iT param (p ^⋏ q) from rfl,
      iT_and hp.isUFormula hq.isUFormula,
      Bootstrapping.substs_and (L := ℒₛₑₜ)
        (isSemiformula_iT p hp).isUFormula (isSemiformula_iT q hq).isUFormula]
    rw [hp', hq']
  · -- or
    intro n param p q hp hq ihp ihq h h1
    have hp' := ihp h h1
    have hq' := ihq h h1
    have hn : n = m + 1 := h.symm.trans h1
    subst hn
    rw [Bootstrapping.substs_or (L := ℒₒᵣ) hp.isUFormula hq.isUFormula,
      iT_or (IsSemiformula.subst (L := ℒₒᵣ) hp (isSemitermVec_QvecVOr m)).isUFormula
            (IsSemiformula.subst (L := ℒₒᵣ) hq (isSemitermVec_QvecVOr m)).isUFormula]
    rw [← iT.construction.result_or hp.isUFormula hq.isUFormula,
      show UformulaRec1.Construction.result ℒₒᵣ iT.construction param (p ^⋎ q)
          = iT param (p ^⋎ q) from rfl,
      iT_or hp.isUFormula hq.isUFormula]
    rw [Bootstrapping.substs_or (L := ℒₛₑₜ)
      (isSemiformula_iT p hp).isUFormula (isSemiformula_iT q hq).isUFormula]
    rw [hp', hq']
  · -- all
    all_goals sorry
  · -- exs
    all_goals sorry

end GodelQ.ITSubstOpenGen

#print axioms GodelQ.ITSubstOpenGen.iT_subst_open
