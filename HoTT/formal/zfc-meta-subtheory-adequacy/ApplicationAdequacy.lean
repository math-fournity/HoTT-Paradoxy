/-!
`MP-ZFC-META-SUBTHEORY-ADEQUACY-001` is the Lean-core consequence of one
source-bounded application-adequacy contract.

It deliberately distinguishes:

* a mathematical model's internal completion;
* an application claim about a physical target;
* a paid model-to-target completion bridge; and
* an explicit switch to a revised task.

The source audit, not Lean, classifies the IEP Standard Solution, Mizar/TG
formal proxy, and Norton task-revision material.  This file proves only what
follows after those fields have been fixed.  It contains no ZFC syntax, no
model of a material runner, no claim that ZFC is inconsistent, and no HoTT
same-Q premise.
-/

namespace ZFCMetaSubtheoryAdequacy

/-- A finite, source-facing classification of one mathematical-model
    application.  Each field is deliberately explicit: source silence cannot
    be converted into any field by the kernel. -/
structure ApplicationCase where
  applicationClaim : Prop
  claimsOriginalResolution : Prop
  requiresBridge : Prop
  bridgePaid : Prop
  explicitTaskSwitch : Prop

/-- The failure predicate is defined at the application-policy layer.  It is
    not a proposition in the language of ZFC. -/
def ApplicationAdequacyFailure (case_ : ApplicationCase) : Prop :=
  case_.applicationClaim ∧
  case_.claimsOriginalResolution ∧
  case_.requiresBridge ∧
  ¬ case_.bridgePaid ∧
  ¬ case_.explicitTaskSwitch

/-- If an application policy claims original target resolution, requires a
    bridge, and supplies neither a bridge nor an explicit task switch, the
    policy violates the fixed ApplicationAdequacy contract. -/
theorem failure_of_unpaid_application
    (case_ : ApplicationCase)
    (application : case_.applicationClaim)
    (original : case_.claimsOriginalResolution)
    (requires : case_.requiresBridge)
    (unpaid : ¬ case_.bridgePaid)
    (no_switch : ¬ case_.explicitTaskSwitch) :
    ApplicationAdequacyFailure case_ :=
  ⟨application, original, requires, unpaid, no_switch⟩

/-- A paid bridge is a positive control: it blocks the failure predicate. -/
theorem paid_bridge_blocks_failure
    (case_ : ApplicationCase)
    (paid : case_.bridgePaid) :
    ¬ ApplicationAdequacyFailure case_ := by
  intro failure
  exact failure.2.2.2.1 paid

/-- An explicit task switch is also a positive control for this contract.
    It does not establish the original completion predicate. -/
theorem explicit_task_switch_blocks_failure
    (case_ : ApplicationCase)
    (switched : case_.explicitTaskSwitch) :
    ¬ ApplicationAdequacyFailure case_ := by
  intro failure
  exact failure.2.2.2.2 switched

/-- A purely mathematical endpoint claim does not activate the application
    contract without an application claim about an external target. -/
theorem model_only_blocks_failure
    (case_ : ApplicationCase)
    (no_application : ¬ case_.applicationClaim) :
    ¬ ApplicationAdequacyFailure case_ := by
  intro failure
  exact no_application failure.1

/-- The source-certified branch that represents the current IEP application
    audit: a physical application claim and an original-resolution claim are
    recorded, the fixed criterion requires a bridge, and the current source
    denominator contains neither its source-to-spec payment nor an explicit
    switch for that exact claim.  This is source input, not a theorem about a
    webpage or ZFC. -/
def applicationUnpaid : ApplicationCase where
  applicationClaim := True
  claimsOriginalResolution := True
  requiresBridge := True
  bridgePaid := False
  explicitTaskSwitch := False

theorem application_unpaid_is_failure :
    ApplicationAdequacyFailure applicationUnpaid := by
  apply failure_of_unpaid_application
  · trivial
  · trivial
  · trivial
  · intro impossible
    exact impossible
  · intro impossible
    exact impossible

/-- Positive control: a case with a completion-preserving bridge is not a
    failure, even when it makes an application/original-resolution claim. -/
def bridgePaidControl : ApplicationCase where
  applicationClaim := True
  claimsOriginalResolution := True
  requiresBridge := True
  bridgePaid := True
  explicitTaskSwitch := False

theorem bridge_paid_control_is_not_failure :
    ¬ ApplicationAdequacyFailure bridgePaidControl := by
  exact paid_bridge_blocks_failure bridgePaidControl trivial

/-- Positive control: an explicitly revised task is not classified as an
    unannounced failure of the original-task bridge. -/
def taskSwitchControl : ApplicationCase where
  applicationClaim := True
  claimsOriginalResolution := False
  requiresBridge := True
  bridgePaid := False
  explicitTaskSwitch := True

theorem task_switch_control_is_not_failure :
    ¬ ApplicationAdequacyFailure taskSwitchControl := by
  exact explicit_task_switch_blocks_failure taskSwitchControl trivial

/-- Positive control: a model-internal endpoint theorem alone is not a
    physical application claim. -/
def modelOnlyControl : ApplicationCase where
  applicationClaim := False
  claimsOriginalResolution := False
  requiresBridge := False
  bridgePaid := True
  explicitTaskSwitch := False

theorem model_only_control_is_not_failure :
    ¬ ApplicationAdequacyFailure modelOnlyControl := by
  exact model_only_blocks_failure modelOnlyControl (by intro h; exact h)

/-- HoTT may contribute to a later consequence only after SameQ is separately
    supplied.  This control prevents the current theorem from silently taking
    that premise. -/
structure H0Admission where
  sameQ : Prop

def H0Eligible (admission : H0Admission) : Prop := admission.sameQ

def h0MissingSameQ : H0Admission where
  sameQ := False

theorem h0_missing_same_q_is_ineligible :
    ¬ H0Eligible h0MissingSameQ := by
  intro h
  exact h

#print axioms failure_of_unpaid_application
#print axioms paid_bridge_blocks_failure
#print axioms explicit_task_switch_blocks_failure
#print axioms model_only_blocks_failure
#print axioms application_unpaid_is_failure
#print axioms bridge_paid_control_is_not_failure
#print axioms task_switch_control_is_not_failure
#print axioms model_only_control_is_not_failure
#print axioms h0_missing_same_q_is_ineligible

end ZFCMetaSubtheoryAdequacy
