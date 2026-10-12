-- CG-009: the iTR subst law (hAB's breakthrough via qVec).
import GodelQ.ZFC.HAllProof

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.ITRSubst
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- The exact statement needed. iTR has the shape:
--   qqAlls (imp (A0 ⋏ (A1 ⋏ ⊤)) (subst [#0,#1] (cRel R))) 2
-- where Aj = conjunct 2 n j (iVE n v.[j]).
-- Substituting ?[^&0] at depth 2 via qVec → the vector for the inner subst becomes
-- [#0, #1] bumped appropriately, and the cRel part is closed.

-- KEY SUB-LEMMA: subst ?[^&0] of the cRel substitution part, under 2 binders.
lemma subst_cRel_under_binders (R : V) :
    subst ℒₛₑₜ (?[^&0] : V)
      (qqAlls (subst ℒₛₑₜ ((^#0 : V) ∷ (^#1 : V) ∷ (0 : V)) (cRel R)) 2) =
    qqAlls (subst ℒₛₑₜ (qVec ℒₛₑₜ (?[^&0] : V))
      (subst ℒₛₑₜ ((^#0 : V) ∷ (^#1 : V) ∷ (0 : V)) (cRel R))) 2 := by
  -- qqAlls p 2 is the iterated universal quantifier; its subst rule is substs_all twice.
  -- Need: qqAlls p k = ...  First establish the qqAlls-subst bridge.
  sorry

end GodelQ.ITRSubst
