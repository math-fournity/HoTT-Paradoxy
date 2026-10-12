-- CG-009: route (a) — the `b = 2` conjunct pieces.
import GodelQ.ZFC.IVEOpenFunc13

open FFL FFL.FirstOrder FFL FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.IVEOpenFunc14
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc2 GodelQ.IVEOpenFunc3 GodelQ.IVEOpenFunc4
open GodelQ.IVEOpenFunc5 GodelQ.IVEOpenFunc6 GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFunc9
open GodelQ.IVEOpenFunc10 GodelQ.LayerMono

/-- **Component ①, `b = 2`**: `QvecV (m+3)` fixes `?[^#i]` for `i < m+2`. -/
lemma termSubstVec_one_QvecV_three {m i : V} (hi : i < m + 2) :
    termSubstVec ℒₛₑₜ 1 (QvecV (V := V) (m + 3)) (?[^#i] : V) = (?[^#i] : V) := by
  rw [show (?[^#i] : V) = (^#i : V) ∷ (0 : V) from rfl,
    termSubstVec_cons₁ (IsUTerm.bvar (z := i)), termSubst_bvar]
  congr 1
  exact nth_QvecV_lt (m + 3) i (lt_trans hi (by
    have h := lt_add_one (m + 2)
    rwa [show (m + 2 : V) + 1 = m + 3 by ring] at h))

end GodelQ.IVEOpenFunc14

#print axioms GodelQ.IVEOpenFunc14.termSubstVec_one_QvecV_three
