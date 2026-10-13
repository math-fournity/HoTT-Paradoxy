import GodelQ.ZFC.OpenLawCheck2
import GodelQ.ZFC.IVEOpenFunc15
import GodelQ.ZFC.IVEOpenFull
open FFL FFL.FirstOrder FFL FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat

namespace GodelQ.ITSubstOpenGen

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## 两层下降律（一般 m）

`IVEOpenFunc15.subst_QvecV_qqAlls_two` 只覆盖 `QvecV (mm+1)`。
这里给任意 `m` 的版本：下降两层把向量从 `QvecV m` 换成 `qVec²(QvecV m) = QvecV (m+2)`。 -/
lemma subst_QvecV_qqAlls_two_gen {m B : V} (hB : IsUFormula ℒₛₑₜ B) :
    subst ℒₛₑₜ (QvecV (V := V) m) (qqAlls B 2)
      = qqAlls (subst ℒₛₑₜ (QvecV (V := V) (m + 2)) B) 2 := by
  have hvec : qVec ℒₛₑₜ (qVec ℒₛₑₜ (QvecV (V := V) m)) = QvecV (V := V) (m + 2) := by
    rw [← QvecV_succ, ← QvecV_succ]
    congr 1
    ring
  have h23 : (2 : V) = (0 + 1) + 1 := by norm_num
  -- expand both sides into the ^∀(^∀ B) form, then push substs_all twice
  rw [h23, qqAlls_succ, qqAlls_succ, qqAlls_zero] at *
  rw [h23, qqAlls_succ, qqAlls_succ, qqAlls_zero]
  rw [Bootstrapping.substs_all (IsUFormula.all.mpr hB)]
  rw [Bootstrapping.substs_all hB, hvec]

/-! ## rel 支：`iT m (subst (QvecVOr m) (^rel k R v)) = subst (QvecV m) (iT (m+1) (^rel k R v))`

两侧向量长度确实不同，但由 `substs_substs` 桥接：
* LHS：`termSubst (QvecVOr m)` 先把 `v` 换成 `termSubstVec (QvecVOr m) v`，
  `iT m` 给 `iTR m k R`，其 conjunct 用向量 `L := ^#j ∷ shiftVec 2 m`（长度 m+1）；
* RHS：`iT (m+1)` 给 `iTR (m+1) k R`，conjunct 用向量 `R := ^#j ∷ shiftVec 2 (m+1)`（长度 m+2），
  再被 `subst (QvecV m)` 下降两层 ⇒ 体内向量 `qVec²(QvecV m) = QvecV (m+2)`。

关键：`L` 作用在 `iVE m (termSubst (QvecVOr m) t)`，`R` 作用在 `iTR` 体的 fvar 侧
`subst ?[^#0,^#1] (cRel R)`；两侧一致性靠 `iVE_open`（已证）逐 bvar z ∈ {z<m, z=m} 收口。 -/

/-- rel 支（statement）。 -/
lemma rel_branch (m : V) :
    ∀ (k R v : V), (ℒₒᵣ).IsRel k R → IsUTermVec ℒₒᵣ k v →
      iT m (subst ℒₒᵣ (QvecVOr (V := V) m) (^rel k R v))
        = subst ℒₛₑₜ (QvecV (V := V) m) (iT (m + 1) (^rel k R v)) := by
  intro k R v hR hv
  -- LHS: subst pushes into the relation's term vector
  rw [substs_rel hR hv]
  -- RHS: iT computes first
  rw [iT_rel hR hv]
  -- LHS: now apply iT_rel to the substituted term vector
  have hvT : IsSemitermVec ℒₒᵣ k (m + 1) (termSubstVec ℒₒᵣ k (QvecVOr (V := V) m) v) :=
    IsSemitermVec.termSubstVec (isSemitermVec_QvecVOr m) hv
  rw [iT_rel hR hvT.isUTerm]
  -- unfold both iTR's
  show iTR m k R (termSubstVec ℒₒᵣ k (QvecVOr m) v)
     = subst ℒₛₑₜ (QvecV m) (iTR (m + 1) k R v)
  rw [iTR, iTR]
  -- RHS: the two-binder descent  subst (QvecV m) (qqAlls B 2) = qqAlls (subst (QvecV (m+2)) B) 2
  rw [subst_QvecV_qqAlls_two_gen]
  trace_state
  sorry

end GodelQ.ITSubstOpenGen

#print axioms GodelQ.ITSubstOpenGen.rel_branch
