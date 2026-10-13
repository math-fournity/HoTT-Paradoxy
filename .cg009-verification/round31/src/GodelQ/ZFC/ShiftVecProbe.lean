-- CG-009: termShiftVec fixes shiftVec (all-bvar vector).
import GodelQ.ZFC.TranslateShiftCompat
import GodelQ.ZFC.ShiftQuote

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

namespace GodelQ.ShiftVecProbe
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

lemma isUTermVec_shiftVec (b : V) (n : ℕ) :
    IsUTermVec ℒₛₑₜ (n : V) (shiftVec (V := V) b (n : V)) :=
  (isSemitermVec_shiftVec (V := V) b n).isUTermVec

/-- `termBShiftVec` bumps every entry: `(termBShiftVec L k ts).[i] = ^#(z+1)` if `ts.[i] = ^#z`.
    In particular on `shiftVec` it gives `shiftVec (b+1) n`. -/
lemma termBShiftVec_shiftVec (b : V) : ∀ (n : ℕ),
    termBShiftVec ℒₛₑₜ (n : V) (shiftVec (V := V) b (n : V)) = shiftVec (V := V) (b + 1) (n : V)
  | 0 => by simp
  | n + 1 => by
    push_cast
    rw [shiftVec_succ, termBShiftVec_cons (IsUTerm.bvar (z := b))
      (isUTermVec_shiftVec b n)]
    rw [termBShift_bvar, termBShiftVec_shiftVec b n]
    rw [show (b + 1 : V) = b + 1 from rfl, shiftVec_succ]

end GodelQ.ShiftVecProbe
