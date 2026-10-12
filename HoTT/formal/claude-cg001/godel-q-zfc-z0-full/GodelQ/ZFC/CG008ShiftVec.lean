import GodelQ.ZFC.CG008ShiftProof

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open GodelQ.Translate
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
namespace GodelQ.CG008ShiftVec
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

set_option maxHeartbeats 800000 in
theorem shiftVec_isUTermVec (b n : V) :
    Bootstrapping.IsUTermVec ℒₛₑₜ n (shiftVec b n) := by
  induction n using ISigma1.sigma1_succ_induction
  · definability
  case zero => simp
  case succ n ih =>
    have hihv : Bootstrapping.IsUTermVec ℒₛₑₜ n (shiftVec b n) := ih
    have hbshift : Bootstrapping.IsUTermVec ℒₛₑₜ n (termBShiftVec ℒₛₑₜ n (shiftVec b n)) :=
      Bootstrapping.IsUTermVec.termBShiftVec hihv
    have hadj : Bootstrapping.IsUTermVec ℒₛₑₜ (n + 1) (^#b ∷ termBShiftVec ℒₛₑₜ n (shiftVec b n)) :=
      hbshift.adjoin Bootstrapping.IsUTerm.bvar
    rw [GodelQ.Translate.shiftVec_succ]
    exact hadj

end GodelQ.CG008ShiftVec