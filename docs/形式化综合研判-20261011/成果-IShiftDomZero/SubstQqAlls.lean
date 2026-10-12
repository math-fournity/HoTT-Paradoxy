-- CG-009: the descent vector for `ve2`'s `qqAlls … 2`, and the WIP notes for
-- the two-step `subst`/`qqAlls` descent.
--
-- ## What is proved here
--
-- `qVec2_QvecV` : `qVec² (QvecV (mm+1)) = QvecV (mm+3)`.
-- This is the exact vector that `subst (QvecV (mm+1))` sees inside `ve2`'s
-- two `qqAlls` binders — the number the func branch of `iVE_open` hinges on.
--
-- ## What is NOT proved (recorded so the next session doesn't redo it)
--
-- `subst_qqAlls_two`: `subst w (qqAlls p 2) = qqAlls (subst (qVec² w) p) 2`.
-- `trace_state` confirmed the two sides are literally the same term after the
-- standard rewrite chain
--     qqAlls_succ, substs_all, qqAlls_succ, substs_all, qqAlls_zero
-- applied to LHS, and
--     qqAlls_succ, qqAlls_succ, qqAlls_zero
-- applied to RHS.
-- The only obstacle is Lean-side index shape: `qqAlls ?p (?k + 1)` does not
-- match a bare numeral `1`, so the inner `qqAlls p 1` needs to be seen as
-- `qqAlls p (0 + 1)` first (e.g. via `norm_num` / an explicit
-- `show (1 : V) = 0 + 1`).  No mathematics is missing.
import GodelQ.ZFC.Ve2BinderProbe

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.SubstQqAlls
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc2 GodelQ.IVEOpenFunc3 GodelQ.IVEOpenFunc4
open GodelQ.IVEOpenFunc5 GodelQ.IVEOpenFunc6 GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFunc9
open GodelQ.IVEOpenFunc10 GodelQ.IVEOpenFunc11 GodelQ.IVEOpenFunc12
open GodelQ.QVec2Probe GodelQ.QVec2Probe2 GodelQ.Ve2BinderProbe

/-- **`qVec² (QvecV (mm+1)) = QvecV (mm+3)`** — the descent vector for `ve2`. -/
lemma qVec2_QvecV (mm : V) :
    qVec ℒₛₑₜ (qVec ℒₛₑₜ (QvecV (V := V) (mm + 1))) = QvecV (V := V) (mm + 3) := by
  rw [qVec_QvecV, qVec_QvecV]
  congr 1
  ring

/-- `QvecV (mm+3)` has length `mm+4` — so `subst_QvecV_conjunct`'s hypothesis
    `i < mm+3` is exactly compatible with the conjunct's needs. -/
example (mm : V) : len (QvecV (V := V) (mm + 3)) = mm + 4 := by
  have h := isSemitermVec_QvecV (V := V) (mm + 3)
  rw [show (mm + 3 : V) + 1 = mm + 4 by ring] at h
  exact h.lh

end GodelQ.SubstQqAlls
