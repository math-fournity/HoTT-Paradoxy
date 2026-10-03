import Mathlib.Analysis.SpecificLimits.Normed

/-!
Concrete real-analysis companion to MP-ZFC-OBSERVATION-BOUNDARY-001.

The source proves that a fixed geometric partial-sum sequence stays strictly
below 1 at every finite natural-number stage while tending to 1 in the usual
real topology.  It deliberately does not define a process-level Done predicate:
the separation between the two is the research question rather than a theorem
that real analysis itself promises to settle.
-/

open Filter Topology

namespace ZfcObservationBoundary

noncomputable section

def zenoPartialSum (n : ℕ) : ℝ := 1 - (1 / 2 : ℝ) ^ n

/-- The analysis-side statement: the finite-stage values tend to the endpoint. -/
def hasLimitOutcome : Prop :=
  Tendsto zenoPartialSum atTop (𝓝 1)

/-- The finite-stage statement: some natural-number stage is exactly the endpoint. -/
def hasFiniteStageEndpoint : Prop :=
  ∃ n : ℕ, zenoPartialSum n = 1

theorem zenoPartialSum_strictly_below_one (n : ℕ) :
    zenoPartialSum n < 1 := by
  unfold zenoPartialSum
  have hpos : 0 < (1 / 2 : ℝ) ^ n := by positivity
  linarith

theorem zenoPartialSum_never_reaches_one (n : ℕ) :
    zenoPartialSum n ≠ 1 :=
  ne_of_lt (zenoPartialSum_strictly_below_one n)

theorem zenoPartialSum_tendsto_one :
    Tendsto zenoPartialSum atTop (𝓝 1) := by
  unfold zenoPartialSum
  have hpow : Tendsto (fun n : ℕ => (1 / 2 : ℝ) ^ n) atTop (𝓝 0) := by
    exact tendsto_pow_atTop_nhds_zero_of_norm_lt_one (by norm_num)
  simpa using (tendsto_const_nhds.sub hpow)

theorem zeno_has_limit_outcome : hasLimitOutcome :=
  zenoPartialSum_tendsto_one

theorem zeno_has_no_finite_stage_endpoint : ¬ hasFiniteStageEndpoint := by
  intro h
  rcases h with ⟨n, hn⟩
  exact zenoPartialSum_never_reaches_one n hn

/-- The precise coexistence needed for the inquiry: a limit outcome is true
    while finite-stage endpoint arrival is false.  This theorem does not assign
    either proposition the unrestricted ordinary-language word "completed". -/
theorem zeno_limit_outcome_without_finite_stage_endpoint :
    hasLimitOutcome ∧ ¬ hasFiniteStageEndpoint :=
  ⟨zeno_has_limit_outcome, zeno_has_no_finite_stage_endpoint⟩

/-- In this concrete real-analysis model, the limit outcome alone does not
    entail finite-stage endpoint arrival. -/
theorem zeno_limit_outcome_does_not_imply_finite_stage_endpoint :
    ¬ (hasLimitOutcome → hasFiniteStageEndpoint) := by
  intro h
  exact zeno_has_no_finite_stage_endpoint (h zeno_has_limit_outcome)

#print axioms zenoPartialSum_strictly_below_one
#print axioms zenoPartialSum_never_reaches_one
#print axioms zenoPartialSum_tendsto_one
#print axioms zeno_limit_outcome_without_finite_stage_endpoint
#print axioms zeno_limit_outcome_does_not_imply_finite_stage_endpoint

end

end ZfcObservationBoundary
