import Mathlib.Analysis.SpecificLimits.Normed

/-!
An exact real-analysis control for the A/P part of the user's proposal.

For the fixed geometric sequence `1 - (1/2)^n`, the formal limit outcome is
true while no finite natural-number stage is the endpoint.  Thus the specific
promotion “limit outcome implies a finite sequential endpoint” is refuted.

This is not a formalization of the Standard Solution's whole continuous-motion
model: that solution may instead use a closed real-time endpoint.  The positive
control below proves that such a model can have an endpoint arrival.
-/

open Filter Topology

namespace ZFCActualQPolicy

noncomputable section

def zenoPartialSum (n : ℕ) : ℝ := 1 - (1 / 2 : ℝ) ^ n

def FormalA : Prop := Tendsto zenoPartialSum atTop (𝓝 1)

def StrictSequentialDone : Prop := ∃ n : ℕ, zenoPartialSum n = 1

/-- A deliberately strict version of P, used as a control rather than attributed
    to the Standard Solution. -/
def LimitPromotesStrictSequentialDone : Prop := FormalA → StrictSequentialDone

theorem partial_sum_strictly_below_one (n : ℕ) : zenoPartialSum n < 1 := by
  unfold zenoPartialSum
  have hpos : 0 < (1 / 2 : ℝ) ^ n := by positivity
  linarith

theorem no_strict_sequential_done : ¬ StrictSequentialDone := by
  intro h
  rcases h with ⟨n, hn⟩
  exact (ne_of_lt (partial_sum_strictly_below_one n)) hn

theorem formal_A_holds : FormalA := by
  unfold FormalA zenoPartialSum
  have hpow : Tendsto (fun n : ℕ => (1 / 2 : ℝ) ^ n) atTop (𝓝 0) := by
    exact tendsto_pow_atTop_nhds_zero_of_norm_lt_one (by norm_num)
  simpa using (tendsto_const_nhds.sub hpow)

theorem strict_limit_promotion_is_refuted :
    ¬ LimitPromotesStrictSequentialDone := by
  intro p
  exact no_strict_sequential_done (p formal_A_holds)

/-- Positive control: continuous time may contain an actual endpoint. -/
abbrev ClosedTime := Set.Icc (0 : ℝ) 1

def continuousTrajectory (t : ClosedTime) : ℝ := t

def terminalTime : ClosedTime := ⟨1, by constructor <;> norm_num⟩

theorem closed_time_endpoint_arrival : continuousTrajectory terminalTime = 1 := by
  rfl

#print axioms partial_sum_strictly_below_one
#print axioms no_strict_sequential_done
#print axioms formal_A_holds
#print axioms strict_limit_promotion_is_refuted
#print axioms closed_time_endpoint_arrival

end

end ZFCActualQPolicy
