-- CG-009: **the two-step `subst` / `qqAlls` descent — PROVED**.
--
-- `subst w (qqAlls p 2) = qqAlls (subst (qVec² w) p) 2`.
-- This is the descent law `ve2`'s `qqAlls … 2` needs: it says substituting under
-- two nested universal quantifiers transforms the vector by two `qVec` steps.
-- With `QVec2Probe.qVec_QvecV` this becomes
--     subst (QvecV k) (qqAlls p 2) = qqAlls (subst (QvecV (k+2)) p) 2.
-- Combined with `IVEOpenFunc12.subst_QvecV_conjunct` this closes the func
-- branch of `iVE_open`.
import GodelQ.ZFC.SubstQqAlls

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate
open GodelQ.SubstQqAlls

namespace GodelQ.SubstQqAllsTwo

/-- **The two-step `subst` / `qqAlls` descent.**
    Substituting under two nested universal quantifiers transforms the vector by
    two `qVec` steps: `subst w (qqAlls p 2) = qqAlls (subst (qVec² w) p) 2`. -/
lemma subst_qqAlls_two {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] {w p n : V}
    (_hp : IsSemiformula ℒₛₑₜ n p) :
    subst ℒₛₑₜ w (qqAlls p (2 : V))
      = qqAlls (subst ℒₛₑₜ (qVec ℒₛₑₜ (qVec ℒₛₑₜ w)) p) (2 : V) := by
  have h0 : IsUFormula ℒₛₑₜ p := _hp.isUFormula
  have hall : IsUFormula ℒₛₑₜ (^∀ p) := IsUFormula.all.mpr h0
  have hidx : ∀ q : V, (qqAlls q (2 : V) : V) = ^∀ (^∀ q) := by
    intro q
    have e23 : (2 : V) = (0 + 1) + 1 := by norm_num
    rw [e23, qqAlls_succ, qqAlls_succ, qqAlls_zero]
  rw [hidx, Bootstrapping.substs_all hall, Bootstrapping.substs_all h0]
  rw [show (qqAlls (subst ℒₛₑₜ (qVec ℒₛₑₜ (qVec ℒₛₑₜ w)) p) (2 : V) : V)
        = ^∀ (^∀ (subst ℒₛₑₜ (qVec ℒₛₑₜ (qVec ℒₛₑₜ w)) p)) from by
    rw [hidx]]

end GodelQ.SubstQqAllsTwo
