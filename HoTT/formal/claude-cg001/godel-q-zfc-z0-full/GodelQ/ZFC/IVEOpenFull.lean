-- CG-009: **完整的 `iVE` 开口律** —— 三支合流。
--
-- `IVESubstOpen3.iVE_open` 的 func 支带 sorry（那里不能 import 本文件，
-- 会造成循环）。本文件在 func 支已证之后，重新陈述完整定理并给出干净证明。
import GodelQ.ZFC.IVEOpenFunc17

open FFL FFL.FirstOrder FFL FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.IVEOpenFull
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc2 GodelQ.IVEOpenFunc3 GodelQ.IVEOpenFunc4
open GodelQ.IVEOpenFunc5 GodelQ.IVEOpenFunc6 GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFunc9
open GodelQ.IVEOpenFunc10 GodelQ.IVEOpenFunc15 GodelQ.IVEOpenFunc16 GodelQ.IVEOpenFunc17

/-- **The full `iVE` opening law.** -/
theorem iVE_open : ∀ (mm : V) (t : V), IsSemiterm ℒₒᵣ (mm + 1) t →
    iVE (mm + 1) (termSubst ℒₒᵣ (QvecVOr (V := V) mm) t) =
      subst ℒₛₑₜ (QvecV (V := V) (mm + 1)) (iVE (mm + 1) t) := by
  intro mm t
  apply IsSemiterm.sigma1_induction (L := ℒₒᵣ) (n := mm + 1)
    (P := fun t ↦ iVE (mm + 1) (termSubst ℒₒᵣ (QvecVOr (V := V) mm) t) =
      subst ℒₛₑₜ (QvecV (V := V) (mm + 1)) (iVE (mm + 1) t))
  · definability
  · intro z hz; exact iVE_open_bvar hz
  · intro x; exact iVE_open_fvar mm x
  · intro k f v hkf hv ih
    exact iVE_open_func hkf hv ih

end GodelQ.IVEOpenFull

#print axioms GodelQ.IVEOpenFull.iVE_open
