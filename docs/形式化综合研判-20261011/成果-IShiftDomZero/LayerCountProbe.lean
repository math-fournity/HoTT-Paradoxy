-- CG-009: settle the exact index count for the func branch, numerically.
import GodelQ.ZFC.SubstQqAlls

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate
open GodelQ.SubstQqAlls
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc2 GodelQ.IVEOpenFunc3 GodelQ.IVEOpenFunc4
open GodelQ.IVEOpenFunc5 GodelQ.IVEOpenFunc6 GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFunc9
open GodelQ.IVEOpenFunc10 GodelQ.IVEOpenFunc11 GodelQ.IVEOpenFunc12

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- Concrete count at `mm = 0` (no abstract-`V` arithmetic involved).

    * `ve2 1 2 f w`'s body conjunct is `conjunct 3 1 i _` (n = mm+1 = 1).
    * Its vector `^#i ∷ shiftVec 3 1` has entries at bvar-index 0 and 3.
    * Descent: `qVec² (QvecV 1) = QvecV 3`.  `QvecV 3` has length 4, identity
      on indices 0,1,2 — index 3 is `^&0`.
    * ⇒ the entry at index 3 is NOT fixed.  **Confirmed: one level short.**

    Where the extra level comes from:
    `subst` under `^∀ p` replaces `w` by `qVec w`, which PREPENDS `^#0` and
    SHIFTS all remaining indices up by one.  So after two descents the *body*
    sees its own bvar indices raised by 2: the conjunct's `shiftVec 3 1` entry
    `^#3` is still `^#3` (it is under the binders, so the substitution does not
    touch it directly) — but the SUBSTITUTION VECTOR it is tested against is
    `QvecV 3` whose slot 3 is `^&0`.

    Conclusion: `ve2`'s two `qqAlls` descents are NOT enough; the correct
    outer vector must be `QvecV 4` = `QvecV (mm + 4)` when `mm = 0`, i.e.
    **the descent must be applied to `QvecV (mm+2)`, not `QvecV (mm+1)`** —
    or, equivalently, `iVE_open`'s outer vector should be `QvecV (mm+2)`.

    This is the resolved open question from the handoff doc. -/
example : len (QvecV (V := V) (3 : V)) = 4 := by
  have h := isSemitermVec_QvecV (V := V) 3
  rw [show (3 : V) + 1 = 4 by norm_num] at h
  exact h.lh

example : (QvecV (V := V) (3 : V)).[3] = (^&0 : V) := nth_QvecV_last 3

example : (QvecV (V := V) (4 : V)).[3] = (^#3 : V) := nth_QvecV_lt 4 3 (by norm_num)

/-- **What the outer vector must be.**
    The conjunct inside `ve2 (mm+1) 2 f w` is `conjunct 3 (mm+1) i _`, so
    `subst_QvecV_conjunct` applies with `n := mm+1` and requires the outer
    vector `QvecV (mm+1+3) = QvecV (mm+4)`.
    Two `qqAlls` descents of `QvecV (mm+1)` give `QvecV (mm+3)` — one short.
    ⇒ `iVE_open`'s outer vector must be **`QvecV (mm+2)`**, not `QvecV (mm+1)`.
    Check at `mm = 0`: outer `QvecV 2`, descends twice to `QvecV 4`. ✓ -/
example : (2 : V) + 2 = 4 := by norm_num

/-- At `mm = 0` the required outer vector is `QvecV 2`. -/
example : (QvecV (V := V) (2 : V)).[2] = (^&0 : V) := nth_QvecV_last 2

-- Exact index range of the conjunct's own substitution vector at `n = mm+1`:
--   `^#i ∷ shiftVec 3 n` has entry 0 = `^#i`, entry `j+1` = `^#(3+j)` (`j < n`).
--   Largest bvar-index used = `3 + (n-1) = 3 + mm` when `n = mm+1`.
-- `QvecV (mm+3)` is the identity only on `0..mm+2`; index `mm+3` is `^&0`.
-- `termSubstVec k w v` reads `w` at the bvar-index baked into `v.[i]`
-- (see `Ve2BinderProbe`), so it DOES read `w.[mm+3]`.
-- ⇒ `QvecV (mm+3)` fails; `QvecV (mm+4)` is required, i.e. the outer vector in
--   `iVE_open` must be `QvecV (mm+2)` so the two descents land on `QvecV (mm+4)`.
