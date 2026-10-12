-- CG-009: the `conjunct`/`cFunc` pieces of the func branch — substitution versions.
import GodelQ.ZFC.IVEOpenFunc6

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.IVEOpenFunc7
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc2 GodelQ.IVEOpenFunc3 GodelQ.IVEOpenFunc4
open GodelQ.IVEOpenFunc5 GodelQ.IVEOpenFunc6

/-- `subst ℒₛₑₜ (QvecV (mm+2))` fixes `subst ℒₛₑₜ ?[^#i] cDomN` for `i < mm+2`.

    NOT YET PROVED — see the handoff doc §3.2 for the exact remaining obligation.
    The blocker is the `substs_substs` instantiation: its `hw : IsSemitermVec L 1 (mm+3) ?[^#i]`
    argument needs `i < mm + 3`, and the composed vector `termSubstVec L 1 (QvecV (mm+2)) ?[^#i]`
    must be shown equal to `?[^#i]` (which holds because `QvecV (mm+2)`'s entry `i` is `^#i`
    for `i < mm+2`). -/
lemma subst_QvecV_cDomN_subst {mm i : V} (hi : i < mm + 2) :
    subst ℒₛₑₜ (QvecV (V := V) (mm + 2)) (subst ℒₛₑₜ (?[^#i] : V) ((cDomN : ℕ) : V)) =
      subst ℒₛₑₜ (?[^#i] : V) ((cDomN : ℕ) : V) := by
  sorry

end GodelQ.IVEOpenFunc7

#print axioms GodelQ.IVEOpenFunc7.subst_QvecV_cDomN_subst
