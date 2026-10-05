/-!
MP-T-PRECISION-TDIAG-001 formalizes the smallest conditional logical core of
the T-DIAG route.

It does not encode syntax, build a Gödel numbering, prove an arithmetic
incompleteness theorem, or identify an actual ZFC-facing completion interface.
It records the exact consequence of three explicit conditions at one code:

* a self-code `d` fixed by `step`;
* a diagonal completion contract `originDone (step d) ↔ ¬ accept d`;
* a bridge from acceptance to that original completion predicate.

Under those conditions the interface cannot accept `d`.  A concrete
counter-control shows that diagonalContract plus self-coding alone is
consistent with acceptance when the bridge is absent.
-/

namespace TPrecisionDiagonal

/-- The explicitly supplied data for a self-coded acceptance question. -/
structure DiagonalContext (Code : Type) where
  step : Code → Code
  selfCode : Code
  accept : Code → Prop
  originDone : Code → Prop
  fixed : step selfCode = selfCode
  diagonalContract : originDone (step selfCode) ↔ ¬ accept selfCode

/-- The bridge that a completion interface would have to pay in order to
    upgrade its acceptance of the self-code to the original task's completion. -/
def Bridge {Code : Type} (context : DiagonalContext Code) : Prop :=
  context.accept context.selfCode → context.originDone (context.step context.selfCode)

/-- The fixed-point component is present as explicit data rather than being
    inferred from natural-language self-reference. -/
theorem fixed_point_is_available
    {Code : Type}
    (context : DiagonalContext Code) :
    context.step context.selfCode = context.selfCode :=
  context.fixed

/-- A paid completion bridge and the diagonal completion contract force
    rejection of the self-coded instance. -/
theorem self_code_cannot_be_accepted_when_bridge_paid
    {Code : Type}
    (context : DiagonalContext Code)
    (bridge : Bridge context) :
    ¬ context.accept context.selfCode := by
  intro accepted
  have original_done : context.originDone (context.step context.selfCode) :=
    bridge accepted
  exact (context.diagonalContract.mp original_done) accepted

/-- A one-element concrete code domain for the two controls below. -/
inductive OneCode where
  | only
deriving DecidableEq, Repr

/-- A self-coded context in which the interface accepts the code but the
    original task is not done.  Its diagonal contract holds; its bridge does
    not. -/
def bridgeMissingControl : DiagonalContext OneCode where
  step := fun _ => .only
  selfCode := .only
  accept := fun _ => True
  originDone := fun _ => False
  fixed := rfl
  diagonalContract := by
    constructor
    · intro impossible
      exact False.elim impossible
    · intro not_true
      exact not_true True.intro

theorem bridge_missing_control_accepts :
    bridgeMissingControl.accept bridgeMissingControl.selfCode := by
  trivial

theorem bridge_missing_control_not_origin_done :
    ¬ bridgeMissingControl.originDone
      (bridgeMissingControl.step bridgeMissingControl.selfCode) := by
  intro impossible
  exact impossible

/-- Self-coding and the diagonal contract alone do not manufacture a bridge. -/
theorem bridge_missing_control_has_no_bridge :
    ¬ Bridge bridgeMissingControl := by
  intro bridge
  have impossible := bridge bridge_missing_control_accepts
  exact impossible

/-- A positive control: when acceptance is false, the diagonal contract and a
    bridge can coexist, and the conclusion is the expected rejection. -/
def bridgePaidControl : DiagonalContext OneCode where
  step := fun _ => .only
  selfCode := .only
  accept := fun _ => False
  originDone := fun _ => True
  fixed := rfl
  diagonalContract := by
    constructor
    · intro _
      intro impossible
      exact impossible
    · intro _
      trivial

theorem bridge_paid_control_has_bridge : Bridge bridgePaidControl := by
  intro impossible
  exact False.elim impossible

theorem bridge_paid_control_rejects_self_code :
    ¬ bridgePaidControl.accept bridgePaidControl.selfCode :=
  self_code_cannot_be_accepted_when_bridge_paid bridgePaidControl
    bridge_paid_control_has_bridge

/-- The two controls separate the bridge condition from self-reference and
    from the diagonal completion contract. -/
theorem controls_separate_bridge_from_self_coding :
    (bridgeMissingControl.accept bridgeMissingControl.selfCode ∧
      ¬ Bridge bridgeMissingControl) ∧
    (Bridge bridgePaidControl ∧
      ¬ bridgePaidControl.accept bridgePaidControl.selfCode) := by
  exact ⟨⟨bridge_missing_control_accepts,
      bridge_missing_control_has_no_bridge⟩,
    ⟨bridge_paid_control_has_bridge,
      bridge_paid_control_rejects_self_code⟩⟩

#print axioms fixed_point_is_available
#print axioms self_code_cannot_be_accepted_when_bridge_paid
#print axioms bridge_missing_control_has_no_bridge
#print axioms bridge_paid_control_rejects_self_code
#print axioms controls_separate_bridge_from_self_coding

end TPrecisionDiagonal
