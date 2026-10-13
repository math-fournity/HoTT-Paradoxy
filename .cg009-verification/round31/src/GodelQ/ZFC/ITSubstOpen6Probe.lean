import GodelQ.ZFC.ITSubstOpen5

open FFL FFL.FirstOrder FFL FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.ITSubstOpen6Probe
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFull GodelQ.LayerMono
open GodelQ.ITSubstOpen3 GodelQ.ITSubstOpen4 GodelQ.ITSubstOpen5

/-- (★★) 的归纳谓词（层自由，向量以 IsUTermVec 约束）。 -/
def QPred (m : V) (t : V) : Prop :=
  ∀ Vw Ww : V, IsUTermVec ℒₛₑₜ (m + 1) Vw → IsUTermVec ℒₛₑₜ (m + 2) Ww →
    VRel m Vw Ww →
    subst ℒₛₑₜ Vw (iVE m (termSubst ℒₒᵣ (QvecVOr (V := V) m) t))
      = subst ℒₛₑₜ Ww (iVE (m + 1) t)

example (m : V) : 𝚷ᴬ₁-Predicate (QPred (V := V) m) := by
  unfold QPred
  definability

end GodelQ.ITSubstOpen6Probe
