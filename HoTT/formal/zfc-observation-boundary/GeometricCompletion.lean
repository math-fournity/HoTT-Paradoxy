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

/-- Names used only for the source-aligned task-switch control below.  They
    describe the two fixed formal predicates, not an unrestricted account of
    physical completion. -/
abbrev limitOutcomeDone : Prop := hasLimitOutcome
abbrev finalStageDone : Prop := hasFiniteStageEndpoint

/-- A separate positive-control time domain: the closed real interval contains
    an actual terminal parameter.  It is deliberately distinct from the
    natural-number stage index of `zenoPartialSum`. -/
abbrev ClosedTime := Set.Icc (0 : ℝ) 1

def continuousTrajectory (t : ClosedTime) : ℝ := t

def terminalTime : ClosedTime := ⟨1, by constructor <;> norm_num⟩

def continuousEndpointArrival : Prop :=
  continuousTrajectory terminalTime = 1

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

/-- The two explicitly named completion predicates are not equivalent on this
    geometric-sequence model.  This is a source-aligned control for any claim
    that replaces a final-stage condition by a limit-outcome condition. -/
theorem zeno_limit_outcome_done_not_equiv_final_stage_done :
    ¬ (limitOutcomeDone ↔ finalStageDone) := by
  intro h
  exact zeno_has_no_finite_stage_endpoint (h.mp zeno_has_limit_outcome)

/-- Positive control: a model whose time domain is a *closed* real interval
    can contain a terminal parameter at which its trajectory is at the goal.
    This theorem does not identify that model-side arrival with any physical or
    independently specified process-completion condition. -/
theorem closed_continuous_time_has_endpoint_arrival :
    continuousEndpointArrival := by
  rfl

theorem closed_continuous_time_has_terminal_witness :
    ∃ t : ClosedTime, continuousTrajectory t = 1 :=
  ⟨terminalTime, rfl⟩

#print axioms zenoPartialSum_strictly_below_one
#print axioms zenoPartialSum_never_reaches_one
#print axioms zenoPartialSum_tendsto_one
#print axioms zeno_limit_outcome_without_finite_stage_endpoint
#print axioms zeno_limit_outcome_does_not_imply_finite_stage_endpoint
#print axioms zeno_limit_outcome_done_not_equiv_final_stage_done
#print axioms closed_continuous_time_has_endpoint_arrival
#print axioms closed_continuous_time_has_terminal_witness

end

end ZfcObservationBoundary
