-- CG-009: `subst (QvecV (m+1)) domZero = domZero` —— 直接路线。
--
-- `domZero = subst ?[^#0] cDomN`，且 `QvecV (m+1)` 的第 0 项就是 `^#0`。
-- 于是 `substs_substs` 把两层复合起来，内层 `?[^#0]` 被外层 `QvecV` 的第 0 项吸收：
--     subst (QvecV (m+1)) (subst ?[^#0] cDomN)
--       = subst (termSubstVec 1 (QvecV (m+1)) ?[^#0]) cDomN
--       = subst ?[^#0] cDomN                      （termSubstVec_cons₁ + nth_QvecV_lt）
--       = domZero
import GodelQ.ZFC.IVESubstOpen

open FFL FFL.FirstOrder FFL FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.SubstDomZero
variable {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.IVESubstOpen GodelQ.ITRSubstOpen

/-- **The pivot**: `QvecV (m+1)` fixes `domZero`. -/
lemma subst_QvecV_domZero (m : V) :
    subst ℒₛₑₜ (QvecV (V := V) (m + 1)) (domZero (V := V)) = domZero (V := V) := by
  rw [domZero]
  have hQ : IsSemitermVec ℒₛₑₜ (m + 1 + 1) (m + 1 + 1) (QvecV (V := V) (m + 1)) :=
    isSemitermVec_QvecV (m + 1)
  have hw : IsSemitermVec ℒₛₑₜ 1 (m + 1 + 1) (?[^#0] : V) :=
    isSemitermVec_single_bvar (n := m + 1 + 1) (by simp)
  rw [Bootstrapping.substs_substs (L := ℒₛₑₜ) (l := 1) isSemiformula_cDomN hQ hw]
  -- termSubstVec 1 (QvecV (m+1)) ?[^#0] = ?[^#0]
  rw [show (?[^#0] : V) = (^#0 : V) ∷ (0 : V) from rfl,
    termSubstVec_cons₁ (IsUTerm.bvar (z := 0)), termSubst_bvar]
  rw [show ((QvecV (V := V) (m + 1)).[0]) = ^#0 from
    GodelQ.ITRSubstOpen.nth_QvecV_lt (m + 1) 0 (by simp)]

end GodelQ.SubstDomZero

#print axioms GodelQ.SubstDomZero.subst_QvecV_domZero
