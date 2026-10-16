/-!
`MP-ZFC-ACTUAL-POLICY-FRONTIER-001` machine-checks the status ledger for the
frozen M6 source denominator.  The ledger is intentionally finite:

* UOU supplies a source P card;
* UOU supplies only a source-level Q-gap candidate;
* SEP's foundation statement does not supply community adoption of P;
* UOU and HoTT evidence do not supply a PBacktrace;
* the user source supplies a normative A/B tension, not formal incompatibility.

This is a bounded evidence-frontier theorem, not a claim of global absence or a
theorem about actual ZFC.
-/

namespace ZfcActualPolicyEvidenceFrontier

inductive WitnessField where
  | sourcePCandidate
  | actualPolicyAdoption
  | actualQAbsence
  | pBacktrace
  | formalABIncompatibility
deriving DecidableEq, Repr

inductive EvidenceStatus where
  | mapped
  | sourceCandidateOnly
  | normativeOnly
  | notMapped
deriving DecidableEq, Repr

abbrev EvidenceLedger := WitnessField → EvidenceStatus

/-- The exact denominator frozen by H104--H110.  It is a transcription of
    scoped source verdicts, not a truth table for all mathematics. -/
def m6CurrentLedger : EvidenceLedger
  | .sourcePCandidate => .mapped
  | .actualPolicyAdoption => .notMapped
  | .actualQAbsence => .sourceCandidateOnly
  | .pBacktrace => .notMapped
  | .formalABIncompatibility => .normativeOnly

def WitnessComplete (ledger : EvidenceLedger) : Prop :=
  ∀ field, ledger field = .mapped

theorem m6_source_P_is_mapped :
    m6CurrentLedger .sourcePCandidate = .mapped := by
  rfl

theorem m6_policy_adoption_is_not_mapped :
    m6CurrentLedger .actualPolicyAdoption = .notMapped := by
  rfl

theorem m6_Q_is_only_source_candidate :
    m6CurrentLedger .actualQAbsence = .sourceCandidateOnly := by
  rfl

theorem m6_pbacktrace_is_not_mapped :
    m6CurrentLedger .pBacktrace = .notMapped := by
  rfl

theorem m6_AB_conflict_is_normative_only :
    m6CurrentLedger .formalABIncompatibility = .normativeOnly := by
  rfl

/-- Within this frozen denominator, a complete ActualPolicyWitness cannot be
    constructed because its adoption field is not source-mapped. -/
theorem m6_current_denominator_cannot_close_actual_witness :
    ¬ WitnessComplete m6CurrentLedger := by
  intro complete
  have adoption := complete .actualPolicyAdoption
  rw [m6_policy_adoption_is_not_mapped] at adoption
  cases adoption

/-- A formal contradiction is not licensed merely by a source P card and
    normative tension: the source denominator still lacks two required bridges. -/
theorem m6_current_denominator_cannot_supply_formal_reductio :
    ¬ (m6CurrentLedger .pBacktrace = .mapped ∧
      m6CurrentLedger .formalABIncompatibility = .mapped) := by
  intro h
  rw [m6_pbacktrace_is_not_mapped] at h
  cases h.1

#print axioms m6_source_P_is_mapped
#print axioms m6_policy_adoption_is_not_mapped
#print axioms m6_Q_is_only_source_candidate
#print axioms m6_pbacktrace_is_not_mapped
#print axioms m6_AB_conflict_is_normative_only
#print axioms m6_current_denominator_cannot_close_actual_witness
#print axioms m6_current_denominator_cannot_supply_formal_reductio

end ZfcActualPolicyEvidenceFrontier
