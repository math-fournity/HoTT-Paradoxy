import GodelQ.ZFC.CG008Vhelp

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open GodelQ.Translate GodelQ.CG008Vhelp
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008BvT
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

set_option maxHeartbeats 800000 in
theorem nth_shiftVec (b n i : V) (hi : i < n) :
    (shiftVec b n).[i] = ^#(b + i) := by
  induction n using ISigma1.sigma1_succ_induction generalizing i
  · definability
  case zero => simp at hi
  case succ n ih =>
    rw [GodelQ.Translate.shiftVec_succ]
    by_cases h0 : i = 0
    · subst h0; simp
    · obtain ⟨j, hj⟩ : ∃ j, i = j + 1 := by
        rcases zero_or_succ i with (h | ⟨j, hj⟩)
        · exact absurd h h0
        · exact ⟨j, hj⟩
      have Hj : j < n := by
        have h3 : (j + 1) + 1 ≤ n + 1 := by
          have h4 : i + 1 ≤ n + 1 := succ_le_iff_lt.mpr hi
          rwa [hj] at h4
        exact succ_le_iff_lt.mp (le_of_succ_le_succ (j + 1) n h3)
      have hin : (shiftVec b n).[j] = ^#(b + j) := ih j Hj
      rw [hj, FFL.FirstOrder.Arithmetic.nth_adjoin_succ]
      rw [Bootstrapping.nth_termBShiftVec (GodelQ.CG008ShiftVec.shiftVec_isUTermVec b n) Hj]
      rw [hin, Bootstrapping.termBShift_bvar]
      congr 1
      rw [add_assoc]

set_option maxHeartbeats 800000 in
theorem shiftVec_bv (b n : V) :
    ∀ i < n, Bootstrapping.termBV ℒₛₑₜ (shiftVec b n).[i] ≤ b + n := by
  intro i hi
  rw [nth_shiftVec b n i hi]
  rw [Bootstrapping.termBV_bvar]
  exact add_assoc b i 1 ▸ add_le_add_right (succ_le_iff_lt.mpr hi) b

#print axioms GodelQ.CG008BvT.nth_shiftVec
#print axioms GodelQ.CG008BvT.shiftVec_bv
