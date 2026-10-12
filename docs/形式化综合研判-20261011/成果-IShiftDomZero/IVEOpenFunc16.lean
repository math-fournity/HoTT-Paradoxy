-- CG-009: func 支的 k = 0 支（ve0）—— 与 domZero 同一机制。
--
-- `ve0 0 f = imp ⊤ (subst ?[^#0] (cFunc 0 f))`，其中内层 `subst ?[^#0] cFunc`
-- 是**引号化句子**（层 1），所以 `QvecV (mm+1)` 的第 0 项 `^#0` 把它吸收
-- （与 `SubstDomZero.subst_QvecV_domZero` 完全同构）。
import GodelQ.ZFC.IVEOpenFunc15

open FFL FFL.FirstOrder FFL FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.IVEOpenFunc16
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc2 GodelQ.IVEOpenFunc3 GodelQ.IVEOpenFunc4
open GodelQ.IVEOpenFunc5 GodelQ.IVEOpenFunc6 GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFunc9
open GodelQ.IVEOpenFunc10 GodelQ.IVEOpenFunc15

/-- `QvecV (mm+1)` 固定 `subst ?[^#0] (cFunc 0 f)`（层 1 的引号化句子）。 -/
lemma subst_QvecV_subst_cFunc0 {mm f : V} :
    subst ℒₛₑₜ (QvecV (V := V) (mm + 1)) (subst ℒₛₑₜ (?[^#0] : V) (cFunc 0 f)) =
      subst ℒₛₑₜ (?[^#0] : V) (cFunc 0 f) := by
  have hc : IsSemiformula ℒₛₑₜ 1 (cFunc 0 f) := isSemiformula_cFunc_arity0 f
  have hQ : IsSemitermVec ℒₛₑₜ (mm + 2) (mm + 2) (QvecV (V := V) (mm + 1)) := by
    have h := isSemitermVec_QvecV (V := V) (mm + 1)
    have e : (mm + 1 : V) + 1 = mm + 2 := by ring
    rwa [e] at h
  have hw : IsSemitermVec ℒₛₑₜ 1 (mm + 2) (?[^#0] : V) :=
    isSemitermVec_single_bvar (n := mm + 2) (by simp)
  rw [show subst ℒₛₑₜ (QvecV (V := V) (mm + 1))
        (subst ℒₛₑₜ (?[^#0] : V) (cFunc 0 f))
      = subst ℒₛₑₜ (termSubstVec ℒₛₑₜ 1 (QvecV (V := V) (mm + 1)) (?[^#0] : V))
        (cFunc 0 f) from
    Bootstrapping.substs_substs (L := ℒₛₑₜ) (l := 1) (n := mm + 2) (m := mm + 2)
      (p := cFunc 0 f) hc hQ hw]
  rw [show (?[^#0] : V) = (^#0 : V) ∷ (0 : V) from rfl,
    termSubstVec_cons₁ (IsUTerm.bvar (z := 0)), termSubst_bvar,
    GodelQ.ITRSubstOpen.nth_QvecV_lt (mm + 1) 0 (by simp)]

/-- **k = 0 支**：`subst (QvecV (mm+1)) (ve0 0 f) = ve0 0 f`。 -/
lemma subst_QvecV_ve0 {mm f : V} :
    subst ℒₛₑₜ (QvecV (V := V) (mm + 1)) (ve0 0 f) = ve0 0 f := by
  have hs : IsUFormula ℒₛₑₜ (subst ℒₛₑₜ (?[^#0] : V) (cFunc 0 f)) :=
    (IsSemiformula.subst (L := ℒₛₑₜ) (isSemiformula_cFunc_arity0 f)
      (isSemitermVec_single_bvar (n := 1) (by simp))).isUFormula
  rw [ve0]
  simp only [imp, Bootstrapping.neg_verum]
  rw [Bootstrapping.substs_or (L := ℒₛₑₜ) (IsSemiformula.falsum (n := 1)).isUFormula hs,
    Bootstrapping.substs_falsum (L := ℒₛₑₜ)]
  congr 1
  exact subst_QvecV_subst_cFunc0 (mm := mm) (f := f)

end GodelQ.IVEOpenFunc16

#print axioms GodelQ.IVEOpenFunc16.subst_QvecV_subst_cFunc0
#print axioms GodelQ.IVEOpenFunc16.subst_QvecV_ve0
