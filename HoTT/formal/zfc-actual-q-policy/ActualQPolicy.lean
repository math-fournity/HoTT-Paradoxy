/-!
`MP-ZFC-ACTUAL-Q-POLICY-002` is the strengthened logical core of the user's
ZFC-1 proposal.

It separates three layers that an earlier draft accidentally allowed to blur:

* a semantic task equivalence, preserving state, input, step, observation, and
  both completion predicates;
* source evidence about O1--O5 and bridge payment; and
* an explicit completion-promotion policy P.

The theorem is conditional.  It does not formalize ZFC syntax, IEP, a
mathematical-community consensus, physical motion, or the actual source bridge
between the fixed Cubical Agda HoTT Q and a Zeno process.
-/

namespace ZFCActualQPolicyV2

inductive Site where
  | zeno
  | hott
deriving DecidableEq, Repr

/-- Evidence absence is not evidence of negation. -/
inductive EvidenceStatus where
  | established
  | refuted
  | unobserved
  | inapplicable
  | conflicted
deriving DecidableEq, Repr

inductive CompletionJudgment where
  | originalResolved
  | revisedResolved
  | bridgeRequired
  | noPolicyClaim
deriving DecidableEq, Repr

/-- The process-facing task contract.  `observe` is deliberately explicit:
    model completion must not silently replace the observation of the original
    process. -/
structure TaskSignature where
  State : Type
  input : State
  step : State → State
  observe : State → Nat
  formalDone : State → Prop
  originDone : State → Prop

/-- Q is the ability of the supplied observation to classify the designated
    original completion predicate.  This is a precise, relative observation
    capacity; it is not a claim that bare ZFC has been modeled. -/
def CompletionObservable (task : TaskSignature) : Prop :=
  ∃ classify : Nat → Prop,
    ∀ state, classify (task.observe state) ↔ task.originDone state

def QMissing (task : TaskSignature) : Prop :=
  ¬ CompletionObservable task

/-- A collision in the supplied observation between opposite origin-completion
    states witnesses the corresponding Q gap. -/
theorem observation_collision_implies_QMissing
    {task : TaskSignature}
    (completed uncompleted : task.State)
    (sameObservation : task.observe completed = task.observe uncompleted)
    (completedDone : task.originDone completed)
    (uncompletedNotDone : ¬ task.originDone uncompleted) :
    QMissing task := by
  intro h
  rcases h with ⟨classify, hclassify⟩
  have atCompleted : classify (task.observe completed) :=
    (hclassify completed).mpr completedDone
  have atUncompleted : classify (task.observe uncompleted) := by
    simpa [sameObservation] using atCompleted
  exact uncompletedNotDone ((hclassify uncompleted).mp atUncompleted)

/-- A same-actual-Q witness is a task equivalence, not equality of source
    metadata.  It preserves the input, the allowed step, the observation, and
    both named completion predicates. -/
structure TaskEquiv (left right : TaskSignature) where
  to : left.State → right.State
  inverse : right.State → left.State
  leftInv : (x : left.State) → inverse (to x) = x
  rightInv : (y : right.State) → to (inverse y) = y
  inputPreserved : to left.input = right.input
  stepPreserved : (x : left.State) → to (left.step x) = right.step (to x)
  observationPreserved : (x : left.State) → left.observe x = right.observe (to x)
  formalDonePreserved : (x : left.State) → left.formalDone x ↔ right.formalDone (to x)
  originDonePreserved : (x : left.State) → left.originDone x ↔ right.originDone (to x)

/-- Identity is a valid semantic task equivalence.  This small constructor is
    used only for controls; actual Zeno--HoTT equivalence still needs its own
    evidence. -/
def TaskEquiv.refl (task : TaskSignature) : TaskEquiv task task where
  to := id
  inverse := id
  leftInv := fun _ => rfl
  rightInv := fun _ => rfl
  inputPreserved := rfl
  stepPreserved := fun _ => rfl
  observationPreserved := fun _ => rfl
  formalDonePreserved := fun _ => Iff.rfl
  originDonePreserved := fun _ => Iff.rfl

/-- These are source-facing audit fields.  Their equality alone does not
    establish `TaskEquiv`; source status and task semantics remain separate. -/
structure QEvidence where
  o1Represented : EvidenceStatus
  o2FormalCompletion : EvidenceStatus
  o3DistinguishesCompletion : EvidenceStatus
  o4BridgeVerified : EvidenceStatus
  o5MetaAuditPerformed : EvidenceStatus
  requiresBridge : EvidenceStatus
  bridgePaid : EvidenceStatus
  originalTaskPreserved : EvidenceStatus
deriving DecidableEq, Repr

structure CompletionCase where
  task : TaskSignature
  evidence : QEvidence
  judgment : CompletionJudgment

def SameActualQ (cases : Site → CompletionCase) : Prop :=
  Nonempty (TaskEquiv (cases .zeno).task (cases .hott).task)

def SourceEvidenceAgrees (cases : Site → CompletionCase) : Prop :=
  (cases .zeno).evidence = (cases .hott).evidence

/-- Semantic task equivalence transports a Q gap.  It is intentionally
    independent of equality of the evidence labels. -/
theorem task_equiv_transports_QMissing
    {left right : TaskSignature}
    (equiv : TaskEquiv left right) :
    QMissing left → QMissing right := by
  intro leftMissing rightObservable
  rcases rightObservable with ⟨classify, rightClassifies⟩
  apply leftMissing
  refine ⟨classify, ?_⟩
  intro state
  have observation : left.observe state = right.observe (equiv.to state) :=
    equiv.observationPreserved state
  constructor
  · intro atLeft
    have atRight : classify (right.observe (equiv.to state)) := by
      simpa only [observation] using atLeft
    have rightDone := (rightClassifies (equiv.to state)).mp atRight
    exact (equiv.originDonePreserved state).mpr rightDone
  · intro leftDone
    have rightDone := (equiv.originDonePreserved state).mp leftDone
    have atRight := (rightClassifies (equiv.to state)).mpr rightDone
    simpa only [observation] using atRight

theorem same_actual_Q_transports_QMissing
    {cases : Site → CompletionCase}
    (sameQ : SameActualQ cases) :
    QMissing (cases .zeno).task → QMissing (cases .hott).task := by
  rcases sameQ with ⟨equiv⟩
  exact task_equiv_transports_QMissing equiv

/-- A is the selected Zeno-side formal completion proposition. -/
def A (cases : Site → CompletionCase) : Prop :=
  ∃ state : (cases .zeno).task.State, (cases .zeno).task.formalDone state

/-- B is the HoTT-side counterexample shape: a formal completion occurs while
    the designated original completion does not. -/
def B (cases : Site → CompletionCase) : Prop :=
  ∃ state : (cases .hott).task.State,
    (cases .hott).task.formalDone state ∧ ¬ (cases .hott).task.originDone state

/-- P is a completion-promotion policy.  Its task-respect clause is a real
    hypothesis: P transfers only when an explicit semantic `SameActualQ`
    witness has been supplied. -/
structure MathematicalIllusionP (cases : Site → CompletionCase) where
  applies : Site → Prop
  respectsSameActualQ : SameActualQ cases → applies .zeno → applies .hott
  promote : (site : Site) →
    applies site →
    (state : (cases site).task.State) →
    (cases site).task.formalDone state →
    (cases site).task.originDone state

/-- A policy-scope witness is weaker than an isomorphism of task state spaces.
    It records the precise bridge that an actual comparison must justify: why
    does a policy admitted on the Zeno-side task also claim jurisdiction over
    the HoTT-side task?  This structure records no bibliographic provenance;
    a source card must separately justify interpreting it as source-owned.
    An exact `TaskEquiv` is one sufficient witness; it is deliberately not
    the only syntactic route. -/
structure PolicyScopeWitness
    {cases : Site → CompletionCase}
    (policy : MathematicalIllusionP cases) where
  transportsAdmissibility : policy.applies .zeno → policy.applies .hott

/-- The strict task-equivalence route gives a policy-scope witness whenever
    the policy itself declares invariance under that exact equivalence. -/
theorem policyScopeOfSameActualQ
    {cases : Site → CompletionCase}
    (policy : MathematicalIllusionP cases)
    (sameQ : SameActualQ cases) : PolicyScopeWitness policy where
  transportsAdmissibility := fun zenoApplies =>
    policy.respectsSameActualQ sameQ zenoApplies

/-- `ZFC-1` is a use-model: a base proposition together with a witnessed
    observation gap and a source-auditable policy P.  It is not object-language
    ZFC syntax or a consistency model of ZFC. -/
structure ZFCOneUse (ZFCBase : Prop) (cases : Site → CompletionCase) where
  baseAccepted : ZFCBase
  qMissing : QMissing (cases .zeno).task
  policy : MathematicalIllusionP cases
  gapAdmitsZenoP : QMissing (cases .zeno).task → policy.applies .zeno

def ZFCWith (ZFCBase extra : Prop) : Prop := ZFCBase ∧ extra

/-- The expression `ZFC + A = ZFC + P` requires a supplied equivalence; it is
    not licensed merely by a narrative connection between A and P. -/
theorem zfc_plus_A_iff_zfc_plus_P
    (ZFCBase AProp PProp : Prop) (A_iff_P : AProp ↔ PProp) :
    ZFCWith ZFCBase AProp ↔ ZFCWith ZFCBase PProp := by
  constructor
  · intro h
    exact ⟨h.1, A_iff_P.mp h.2⟩
  · intro h
    exact ⟨h.1, A_iff_P.mpr h.2⟩

theorem revised_is_not_original :
    CompletionJudgment.revisedResolved ≠ .originalResolved := by
  decide

theorem unobserved_is_not_refuted :
    EvidenceStatus.unobserved ≠ .refuted := by
  decide

/-- Missing Q does not, by pure logic, create P.  The policy admission is a
    separate source/model premise in `ZFCOneUse`. -/
theorem q_gap_does_not_logically_force_P :
    ¬ (∀ (qGap PProp : Prop), qGap → PProp) := by
  intro h
  exact h True False True.intro

/-- A `SameActualQ` witness contains an actual task equivalence.  Agreement of
    O1--O5 evidence labels is deliberately absent from this theorem. -/
theorem same_actual_Q_has_task_equivalence
    {cases : Site → CompletionCase}
    (sameQ : SameActualQ cases) :
    Nonempty (TaskEquiv (cases .zeno).task (cases .hott).task) :=
  sameQ

/-- Within the use-model, A is promoted on the Zeno side. -/
theorem zfc1_promotes_A
    {ZFCBase : Prop} {cases : Site → CompletionCase}
    (model : ZFCOneUse ZFCBase cases)
    (a : A cases) :
    ∃ state : (cases .zeno).task.State, (cases .zeno).task.originDone state := by
  rcases a with ⟨state, formal⟩
  exact ⟨state,
    model.policy.promote .zeno
      (model.gapAdmitsZenoP model.qMissing) state formal⟩

/-- A policy admitted on Zeno transfers to HoTT only through an explicit
    semantic task equivalence. -/
theorem same_actual_Q_transports_P_to_HoTT
    {ZFCBase : Prop} {cases : Site → CompletionCase}
    (model : ZFCOneUse ZFCBase cases)
    (sameQ : SameActualQ cases) :
    model.policy.applies .hott :=
  model.policy.respectsSameActualQ sameQ
    (model.gapAdmitsZenoP model.qMissing)

/-- This is the policy-level consequence needed by an actual source card.
    It does not demand a state-space bijection: an actual source card must
    instead justify a reviewable scope witness explaining why P applies to
    both tasks. -/
theorem source_scoped_P_with_B_is_inconsistent
    {ZFCBase : Prop} {cases : Site → CompletionCase}
    (model : ZFCOneUse ZFCBase cases)
    (scope : PolicyScopeWitness model.policy)
    (b : B cases) :
    False := by
  rcases b with ⟨state, formalHott, notOriginHott⟩
  exact notOriginHott
    (model.policy.promote .hott
      (scope.transportsAdmissibility
        (model.gapAdmitsZenoP model.qMissing))
      state formalHott)

/-- This is the formal A/B consequence requested by the user.  It is a
    contradiction in the explicitly assumed ZFC-1 use-model, conditional on
    the actual-Q task equivalence and the policy's invariance under it. -/
theorem zfc1_same_actual_Q_P_with_B_is_inconsistent
    {ZFCBase : Prop} {cases : Site → CompletionCase}
    (model : ZFCOneUse ZFCBase cases)
    (sameQ : SameActualQ cases)
    (b : B cases) :
    False := by
  exact source_scoped_P_with_B_is_inconsistent model
    (policyScopeOfSameActualQ model.policy sameQ) b

/-- The combined A/B statement exposes both outcomes: A is promoted on the
    Zeno side while B makes the transported policy contradictory on HoTT. -/
theorem zfc1_yields_A_and_conflicts_with_B
    {ZFCBase : Prop} {cases : Site → CompletionCase}
    (model : ZFCOneUse ZFCBase cases)
    (sameQ : SameActualQ cases)
    (a : A cases)
    (b : B cases) :
    (∃ state : (cases .zeno).task.State, (cases .zeno).task.originDone state) ∧ False :=
  ⟨zfc1_promotes_A model a,
   zfc1_same_actual_Q_P_with_B_is_inconsistent model sameQ b⟩

/-- The exact proposition which this file calls the admitted Zeno-side part of
    `P`.  This keeps the informal notation `ZFC-1 = ZFC + P` from hiding the
    fact that an admitted policy is an additional proposition. -/
def AdmittedZenoP
    {cases : Site → CompletionCase}
    (policy : MathematicalIllusionP cases) : Prop :=
  policy.applies .zeno

/-- The formal surrogate for the user's `ZFC-1`.  It is a use-level extension:
    accepted base theory plus an explicitly admitted completion-promotion
    policy.  It is deliberately not a syntactic extension of the ZFC axiom
    scheme. -/
def ZFCMinusOne
    (ZFCBase : Prop) {cases : Site → CompletionCase}
    (policy : MathematicalIllusionP cases) : Prop :=
  ZFCWith ZFCBase (AdmittedZenoP policy)

/-- Every `ZFCOneUse` contains the extra admitted policy proposition.  The
    theorem does not turn an absence of Q into P by logic; that is precisely
    the separately named `gapAdmitsZenoP` premise in the use-model. -/
theorem zfcOneUse_is_ZFCMinusOne
    {ZFCBase : Prop} {cases : Site → CompletionCase}
    (model : ZFCOneUse ZFCBase cases) :
    ZFCMinusOne ZFCBase model.policy :=
  ⟨model.baseAccepted, model.gapAdmitsZenoP model.qMissing⟩

/-- If a source-certified acceptance contract really equates the selected
    Zeno-side A with admitted P, the user's shorthand `ZFC + A = ZFC + P`
    becomes a theorem.  The equivalence remains an explicit premise, because
    neither a limit theorem nor a source label supplies it automatically. -/
theorem zfc_plus_A_iff_ZFCMinusOne
    {ZFCBase : Prop} {cases : Site → CompletionCase}
    (policy : MathematicalIllusionP cases)
    (A_iff_admittedP : A cases ↔ AdmittedZenoP policy) :
    ZFCWith ZFCBase (A cases) ↔ ZFCMinusOne ZFCBase policy :=
  zfc_plus_A_iff_zfc_plus_P ZFCBase (A cases) (AdmittedZenoP policy)
    A_iff_admittedP

/-- A weak resolution label is intentionally weaker than `MathematicalIllusionP`.
    It may call a formal state "resolved", but it does not assert that the
    original process has completed.  Separating it from P prevents a source's
    use of the word "resolved" from silently becoming a bridge theorem. -/
structure WeakResolutionLabel (task : TaskSignature) where
  label : (state : task.State) → task.formalDone state → CompletionJudgment

/-- A small, fully explicit process model.  `stage n` represents a finite
    indexed stage; `limit` represents the model's completed limit state; and
    `endpoint` represents the designated original-endpoint state.  Both latter
    states receive the same observation, so the selected observation cannot
    decide whether original completion has occurred.  This is a controlled
    surrogate, not a formal model of the real line, Achilles, or the user's
    full circle construction. -/
inductive ZenoToyState where
  | stage : Nat → ZenoToyState
  | limit : ZenoToyState
  | endpoint : ZenoToyState
deriving DecidableEq, Repr

/-- The two predicates are inductive rather than Boolean case splits so that
    the controlled model itself stays inside Lean's axiom-free kernel fragment. -/
inductive ZenoToyFormalDone : ZenoToyState → Prop where
  | atLimit : ZenoToyFormalDone .limit

inductive ZenoToyOriginDone : ZenoToyState → Prop where
  | atEndpoint : ZenoToyOriginDone .endpoint

def zenoToyTask : TaskSignature where
  State := ZenoToyState
  input := .stage 0
  step := fun state =>
    match state with
    | .stage n => .stage (Nat.succ n)
    | .limit => .limit
    | .endpoint => .endpoint
  observe := fun state =>
    match state with
    | .stage _ => 0
    | .limit => 1
    | .endpoint => 1
  formalDone := ZenoToyFormalDone
  originDone := ZenoToyOriginDone

/-- The actual finite-stage run of the controlled surrogate. -/
def zenoToyRun : Nat → ZenoToyState
  | 0 => .stage 0
  | Nat.succ n => zenoToyTask.step (zenoToyRun n)

theorem zenoToyRun_is_stage (n : Nat) :
    zenoToyRun n = .stage n := by
  induction n with
  | zero => rfl
  | succ n ih =>
      change zenoToyTask.step (zenoToyRun n) = .stage (Nat.succ n)
      rw [ih]
      rfl

/-- No natural-number-indexed finite stage of the surrogate is its designated
    original endpoint.  This statement is about the explicit `Nat` process;
    it does not deny that a separate continuous-time model can have an endpoint. -/
theorem zenoToy_no_finite_stage_is_origin_done (n : Nat) :
    ¬ zenoToyTask.originDone (zenoToyRun n) := by
  rw [zenoToyRun_is_stage n]
  exact fun h => nomatch h

/-- The model does contain a formal limit-completion witness A. -/
theorem zenoToy_has_formal_completion :
    ∃ state : zenoToyTask.State, zenoToyTask.formalDone state :=
  ⟨.limit, .atLimit⟩

/-- The `limit` and `endpoint` states are observationally merged even though
    they differ on original completion.  Hence this particular observation
    lacks the formal surrogate of Q. -/
theorem zenoToy_QMissing : QMissing zenoToyTask := by
  apply observation_collision_implies_QMissing
    ZenoToyState.endpoint ZenoToyState.limit
  · rfl
  · exact .atEndpoint
  · exact fun h => nomatch h

/-- A weak label can call the model-limit state "resolved" without proving a
    bridge to original completion.  This models the logical form of a
    convenience label only; it is not yet the stronger P used in the conflict
    theorem. -/
def zenoToyWeakResolution : WeakResolutionLabel zenoToyTask where
  label := fun _ _ => .revisedResolved

theorem zenoToy_weak_label_is_revised :
    zenoToyWeakResolution.label .limit .atLimit = .revisedResolved :=
  rfl

/-- The strong promotion required for `MathematicalIllusionP` fails in the
    controlled model at the formal limit state. -/
theorem zenoToy_no_unconditional_completion_bridge :
    ¬ ((state : zenoToyTask.State) →
      zenoToyTask.formalDone state → zenoToyTask.originDone state) := by
  intro bridge
  exact nomatch bridge .limit .atLimit

/-- A non-vacuously admitted strong policy P is impossible for the controlled
    model.  This is the formal distinction between calling the state
    `revisedResolved` and asserting the original-completion promotion. -/
def zenoToyEvidence : QEvidence where
  o1Represented := .established
  o2FormalCompletion := .established
  o3DistinguishesCompletion := .refuted
  o4BridgeVerified := .refuted
  o5MetaAuditPerformed := .unobserved
  requiresBridge := .established
  bridgePaid := .refuted
  originalTaskPreserved := .unobserved

def zenoToyCase : CompletionCase where
  task := zenoToyTask
  evidence := zenoToyEvidence
  judgment := .revisedResolved

def zenoToyCases : Site → CompletionCase
  | .zeno => zenoToyCase
  | .hott => zenoToyCase

/-- A control for the earlier metadata-equality mistake.  These predicates have
    no constructors; they let the example focus only on the mismatch between
    source labels and the underlying state spaces. -/
inductive BoolMetadataFormalDone : Bool → Prop
inductive BoolMetadataOriginDone : Bool → Prop
inductive UnitMetadataFormalDone : Unit → Prop
inductive UnitMetadataOriginDone : Unit → Prop

def boolMetadataTask : TaskSignature where
  State := Bool
  input := false
  step := fun state => state
  observe := fun _ => 0
  formalDone := BoolMetadataFormalDone
  originDone := BoolMetadataOriginDone

def unitMetadataTask : TaskSignature where
  State := Unit
  input := Unit.unit
  step := fun state => state
  observe := fun _ => 0
  formalDone := UnitMetadataFormalDone
  originDone := UnitMetadataOriginDone

def boolMetadataCase : CompletionCase where
  task := boolMetadataTask
  evidence := zenoToyEvidence
  judgment := .noPolicyClaim

def unitMetadataCase : CompletionCase where
  task := unitMetadataTask
  evidence := zenoToyEvidence
  judgment := .noPolicyClaim

def metadataOnlyCases : Site → CompletionCase
  | .zeno => boolMetadataCase
  | .hott => unitMetadataCase

/-- Equal O1--O5 labels alone can be manufactured for tasks whose states are
    not even bijective.  They therefore cannot serve as an actual-Q theorem. -/
theorem metadataOnlyCases_evidence_agrees :
    SourceEvidenceAgrees metadataOnlyCases :=
  rfl

theorem bool_unit_have_no_task_equiv :
    ¬ Nonempty (TaskEquiv boolMetadataTask unitMetadataTask) := by
  intro h
  rcases h with ⟨equiv⟩
  have sameTo : equiv.to false = equiv.to true := by
    cases equiv.to false
    cases equiv.to true
    rfl
  have falseEqTrue : false = true := by
    exact Eq.trans (equiv.leftInv false).symm
      (Eq.trans (congrArg equiv.inverse sameTo) (equiv.leftInv true))
  exact Bool.noConfusion falseEqTrue

theorem sourceEvidenceAgrees_does_not_prove_sameActualQ :
    SourceEvidenceAgrees metadataOnlyCases ∧ ¬ SameActualQ metadataOnlyCases :=
  ⟨metadataOnlyCases_evidence_agrees, bool_unit_have_no_task_equiv⟩

/-- A second control: even a genuine Q gap plus an admitted strong policy does
    not manufacture the HoTT-side B counterexample by logic.  B has to be
    supplied by a real target theorem and a task mapping; it cannot be smuggled
    into the conclusion merely because the use-model has admitted P. -/
inductive VacantFormalDone : Bool → Prop
inductive VacantOriginDone : Bool → Prop where
  | atTrue : VacantOriginDone true

def vacantFormalTask : TaskSignature where
  State := Bool
  input := false
  step := fun state => state
  observe := fun _ => 0
  formalDone := VacantFormalDone
  originDone := VacantOriginDone

def vacantFormalCase : CompletionCase where
  task := vacantFormalTask
  evidence := zenoToyEvidence
  judgment := .noPolicyClaim

def vacantFormalCases : Site → CompletionCase
  | .zeno => vacantFormalCase
  | .hott => vacantFormalCase

theorem vacantFormal_QMissing : QMissing vacantFormalTask := by
  apply observation_collision_implies_QMissing true false
  · rfl
  · exact .atTrue
  · exact fun h => nomatch h

def vacantFormalPolicy : MathematicalIllusionP vacantFormalCases where
  applies := fun _ => True
  respectsSameActualQ := fun _ _ => True.intro
  promote := fun site _ _ formal =>
    match site with
    | .zeno => nomatch formal
    | .hott => nomatch formal

def vacantFormalUse : ZFCOneUse True vacantFormalCases where
  baseAccepted := True.intro
  qMissing := vacantFormal_QMissing
  policy := vacantFormalPolicy
  gapAdmitsZenoP := fun _ => True.intro

theorem vacantFormal_same_actual_Q : SameActualQ vacantFormalCases :=
  ⟨TaskEquiv.refl vacantFormalTask⟩

theorem vacantFormal_not_B : ¬ B vacantFormalCases := by
  intro h
  rcases h with ⟨_, formal, _⟩
  exact nomatch formal

theorem zfcOneUse_and_same_actual_Q_do_not_logically_force_B :
    ∃ (cases : Site → CompletionCase) (_ : ZFCOneUse True cases),
      SameActualQ cases ∧ ¬ B cases :=
  ⟨vacantFormalCases, vacantFormalUse,
    vacantFormal_same_actual_Q, vacantFormal_not_B⟩

theorem zenoToy_no_admitted_strong_P :
    ¬ ∃ policy : MathematicalIllusionP zenoToyCases,
      AdmittedZenoP policy := by
  intro h
  rcases h with ⟨policy, admitted⟩
  have wrong : zenoToyTask.originDone .limit := by
    exact policy.promote .zeno admitted .limit .atLimit
  exact nomatch wrong

/-- A contrasting endpoint model: formal and original completion agree, and
    the observation distinguishes the endpoint.  It is a positive control for
    the claim that this development does not infer a defect merely from the
    presence of an endpoint or a completion predicate. -/
inductive EndpointControlState where
  | before
  | atEndpoint
deriving DecidableEq, Repr

def endpointControlTask : TaskSignature where
  State := EndpointControlState
  input := .before
  step := fun state =>
    match state with
    | .before => .atEndpoint
    | .atEndpoint => .atEndpoint
  observe := fun state =>
    match state with
    | .before => 0
    | .atEndpoint => 1
  formalDone := fun state =>
    match state with
    | .atEndpoint => True
    | .before => False
  originDone := fun state =>
    match state with
    | .atEndpoint => True
    | .before => False

theorem endpointControl_observes_origin_completion :
    CompletionObservable endpointControlTask := by
  refine ⟨fun observation => observation = 1, ?_⟩
  intro state
  cases state with
  | before =>
      change (0 = 1) ↔ False
      constructor
      · intro h
        nomatch h
      · intro h
        exact False.elim h
  | atEndpoint =>
      change (1 = 1) ↔ True
      constructor
      · intro _
        exact True.intro
      · intro _
        rfl

theorem endpointControl_completion_bridge :
    (state : endpointControlTask.State) →
      endpointControlTask.formalDone state → endpointControlTask.originDone state := by
  intro state
  cases state with
  | before =>
      change False → False
      exact fun h => h
  | atEndpoint =>
      change True → True
      exact fun h => h

#print axioms zfc_plus_A_iff_zfc_plus_P
#print axioms revised_is_not_original
#print axioms unobserved_is_not_refuted
#print axioms q_gap_does_not_logically_force_P
#print axioms observation_collision_implies_QMissing
#print axioms same_actual_Q_has_task_equivalence
#print axioms task_equiv_transports_QMissing
#print axioms same_actual_Q_transports_QMissing
#print axioms zfc1_promotes_A
#print axioms same_actual_Q_transports_P_to_HoTT
#print axioms source_scoped_P_with_B_is_inconsistent
#print axioms zfc1_same_actual_Q_P_with_B_is_inconsistent
#print axioms zfc1_yields_A_and_conflicts_with_B
#print axioms zfcOneUse_is_ZFCMinusOne
#print axioms zfc_plus_A_iff_ZFCMinusOne
#print axioms zenoToyTask
#print axioms zenoToyRun
#print axioms endpointControlTask
#print axioms zenoToyRun_is_stage
#print axioms zenoToy_no_finite_stage_is_origin_done
#print axioms zenoToy_has_formal_completion
#print axioms zenoToy_QMissing
#print axioms zenoToy_weak_label_is_revised
#print axioms metadataOnlyCases_evidence_agrees
#print axioms bool_unit_have_no_task_equiv
#print axioms sourceEvidenceAgrees_does_not_prove_sameActualQ
#print axioms vacantFormal_QMissing
#print axioms vacantFormal_same_actual_Q
#print axioms vacantFormal_not_B
#print axioms zfcOneUse_and_same_actual_Q_do_not_logically_force_B
#print axioms zenoToy_no_unconditional_completion_bridge
#print axioms zenoToy_no_admitted_strong_P
#print axioms endpointControl_observes_origin_completion
#print axioms endpointControl_completion_bridge

end ZFCActualQPolicyV2
