/-!
`MP-ZFC-NORMATIVE-PROCESS-AUDIT-001` formalizes an explicit *normative*
completion-audit interface suggested by the user's MetaTheory → SubTheory
requirement.  It is intentionally not an object-language formalization of
ZFC, nor a claim that current mathematical practice already uses this audit.

The interface takes a proved formal completion and classifies the source-side
relationship to the original process task into exactly three possibilities:

* a paid bridge, which permits `originalResolved`;
* an explicit task switch, which permits only `revisedResolved`;
* no payment, which returns `bridgeRequired`.

The Norton-style contract, a paid positive control, and an unpaid negative
control make the rule's intended boundary kernel-checkable.
-/

namespace ZFCNormativeProcessAudit

/-- What a source/application contract supplies for a formal completion. -/
inductive BridgeStatus (formalDone originDone : Prop) where
  | paid (certificate : formalDone → originDone)
  | explicitTaskSwitch
  | missing

/-- An audit outcome preserves the distinction between original resolution,
revised-task resolution, and an unclosed bridge obligation. -/
inductive AuditVerdict where
  | originalResolved
  | revisedResolved
  | bridgeRequired
deriving DecidableEq, Repr

/-- A source or application contract keeps the model-side and origin-side
completion predicates separate until a `BridgeStatus` says how they relate. -/
structure CompletionContract where
  formalDone : Prop
  originDone : Prop
  bridge : BridgeStatus formalDone originDone

/-- `audit` is called only after the model-side `formalDone` evidence has been
supplied.  It never turns that evidence alone into `originalResolved`. -/
def audit (contract : CompletionContract) (_formal : contract.formalDone) : AuditVerdict :=
  match contract.bridge with
  | .paid _ => .originalResolved
  | .explicitTaskSwitch => .revisedResolved
  | .missing => .bridgeRequired

/-- Soundness of the normative interface: an original-resolution verdict carries
a source-supplied bridge certificate and therefore entails origin completion. -/
theorem audit_original_resolved_is_sound
    (contract : CompletionContract) (formal : contract.formalDone)
    (h : audit contract formal = .originalResolved) :
    contract.originDone := by
  rcases contract with ⟨formalDone, originDone, bridge⟩
  cases bridge with
  | paid certificate =>
      exact certificate formal
  | explicitTaskSwitch =>
      cases h
  | missing =>
      cases h

/-- A visible task switch is not silently re-labelled as original resolution. -/
theorem audit_explicit_switch_is_revised
    (contract : CompletionContract) (formal : contract.formalDone)
    (h : contract.bridge = .explicitTaskSwitch) :
    audit contract formal = .revisedResolved := by
  rcases contract with ⟨formalDone, originDone, bridge⟩
  cases bridge with
  | paid certificate =>
      cases h
  | explicitTaskSwitch =>
      rfl
  | missing =>
      cases h

/-- An explicit switch cannot be silently reported as resolution of the
original task. -/
theorem audit_explicit_switch_is_not_original
    (contract : CompletionContract) (formal : contract.formalDone)
    (h : contract.bridge = .explicitTaskSwitch) :
    audit contract formal ≠ .originalResolved := by
  rw [audit_explicit_switch_is_revised contract formal h]
  decide

/-- An unpaid bridge remains an obligation rather than a completion verdict. -/
theorem audit_missing_bridge_requires_payment
    (contract : CompletionContract) (formal : contract.formalDone)
    (h : contract.bridge = .missing) :
    audit contract formal = .bridgeRequired := by
  rcases contract with ⟨formalDone, originDone, bridge⟩
  cases bridge with
  | paid certificate =>
      cases h
  | explicitTaskSwitch =>
      cases h
  | missing =>
      rfl

/-- A missing bridge cannot be silently reported as resolution of the original
task. -/
theorem audit_missing_bridge_is_not_original
    (contract : CompletionContract) (formal : contract.formalDone)
    (h : contract.bridge = .missing) :
    audit contract formal ≠ .originalResolved := by
  rw [audit_missing_bridge_requires_payment contract formal h]
  decide

/-- The strict Norton control requires a greatest natural-number-indexed action. -/
def StrictLastActionCompletion : Prop :=
  ∃ last : Nat, ∀ action : Nat, action ≤ last

/-- The revised Norton control accepts every natural-number-indexed action
without adding a non-existent last member. -/
def RevisedAllActionsCompletion : Prop :=
  ∀ _action : Nat, True

theorem revised_all_actions_complete : RevisedAllActionsCompletion := by
  intro _action
  trivial

theorem strict_last_action_completion_impossible :
    ¬ StrictLastActionCompletion := by
  intro h
  rcases h with ⟨last, hlast⟩
  exact Nat.not_succ_le_self last (hlast (Nat.succ last))

/-- The source-bound Norton input has revised formal completion and an explicit
task switch; it deliberately carries no bridge to strict origin completion. -/
def nortonContract : CompletionContract where
  formalDone := RevisedAllActionsCompletion
  originDone := StrictLastActionCompletion
  bridge := .explicitTaskSwitch

theorem audit_norton_contract_reports_task_switch :
    audit nortonContract revised_all_actions_complete = .revisedResolved := by
  rfl

theorem audit_norton_contract_is_not_original_resolution :
    audit nortonContract revised_all_actions_complete ≠ .originalResolved := by
  decide

/-- Positive control: a source that supplies a bridge can earn original resolution. -/
def paidBridgeControl : CompletionContract where
  formalDone := True
  originDone := True
  bridge := .paid (fun _ => True.intro)

theorem audit_paid_bridge_control_resolves_original :
    audit paidBridgeControl True.intro = .originalResolved := by
  rfl

theorem paid_bridge_control_origin_done :
    paidBridgeControl.originDone := by
  exact audit_original_resolved_is_sound paidBridgeControl True.intro rfl

/-- Negative control: formal completion without payment is never promoted to
original completion by this normative interface. -/
def missingBridgeControl : CompletionContract where
  formalDone := True
  originDone := False
  bridge := .missing

theorem audit_missing_bridge_control_requires_payment :
    audit missingBridgeControl True.intro = .bridgeRequired := by
  rfl

theorem audit_missing_bridge_control_does_not_resolve_original :
    audit missingBridgeControl True.intro ≠ .originalResolved := by
  decide

#print axioms audit_original_resolved_is_sound
#print axioms audit_explicit_switch_is_revised
#print axioms audit_explicit_switch_is_not_original
#print axioms audit_missing_bridge_requires_payment
#print axioms audit_missing_bridge_is_not_original
#print axioms strict_last_action_completion_impossible
#print axioms audit_norton_contract_reports_task_switch
#print axioms audit_norton_contract_is_not_original_resolution
#print axioms audit_paid_bridge_control_resolves_original
#print axioms paid_bridge_control_origin_done
#print axioms audit_missing_bridge_control_requires_payment
#print axioms audit_missing_bridge_control_does_not_resolve_original

end ZFCNormativeProcessAudit
