/-!
`MP-ZFC-COMPLETION-POLICY-UNIFORMITY-001` formalizes the conditional
meta-policy form of the user's Zeno/HoTT comparison:

    same complete Q profile + opposite completion judgments
      => not a Q-uniform observation policy.

The file deliberately does not assert that actual Zeno, the user's circle, and
the fixed Cubical Agda HoTT program share such a profile.  It does not encode
ZFC, IEP, a mathematical-community consensus, or physical time.  Its role is
to make explicit the exact source-and-task premises that would be required
before the phrase "the same Q receives different judgments" can be used.
-/

namespace ZFCCompletionPolicyUniformity

inductive ComparisonSite where
  | zeno
  | hott
deriving DecidableEq

/-- A complete Q profile includes not only representation and formal
    completion, but the distinction, bridge and audit fields whose absence is
    at issue.  Booleans are a conditional finite fixture; they do not encode
    unknown source evidence as false. -/
structure QProfile where
  o1Represented : Bool
  o2FormalCompletion : Bool
  o3DistinguishesCompletion : Bool
  o4SameTaskBridgeVerified : Bool
  o5MetaAuditPerformed : Bool
  requiresBridge : Bool
  bridgePaid : Bool
  originalTaskPreserved : Bool
deriving DecidableEq

inductive CompletionJudgment where
  | originalResolved
  | revisedResolved
  | bridgeRequired
deriving DecidableEq

structure Assessment where
  profile : ComparisonSite → QProfile
  judgment : ComparisonSite → CompletionJudgment

/-- The proposed O3--O5 adequacy responsibility.  It is a policy hypothesis,
    not an axiom or theorem of ZFC. -/
def O3O5Adequate (assessment : Assessment) : Prop :=
  ∀ site,
    (assessment.profile site).requiresBridge = true →
    assessment.judgment site = .originalResolved →
    (assessment.profile site).o3DistinguishesCompletion = true ∧
      (assessment.profile site).o4SameTaskBridgeVerified = true ∧
      (assessment.profile site).o5MetaAuditPerformed = true ∧
      (assessment.profile site).bridgePaid = true ∧
      (assessment.profile site).originalTaskPreserved = true

/-- Uniformity means equal *full* profiles receive equal completion judgments.
    Sharing only the word "completion" or one field is deliberately weaker. -/
def QUniform (assessment : Assessment) : Prop :=
  ∀ left right,
    assessment.profile left = assessment.profile right →
    assessment.judgment left = assessment.judgment right

/-- An original-resolution judgment with an unpaid required bridge violates
    the proposed O3--O5 responsibility. -/
theorem unbridged_original_resolution_breaks_O3O5
    (assessment : Assessment) (site : ComparisonSite)
    (needsBridge : (assessment.profile site).requiresBridge = true)
    (claimsOriginalResolution : assessment.judgment site = .originalResolved)
    (bridgeMissing : (assessment.profile site).bridgePaid = false) :
    ¬ O3O5Adequate assessment := by
  intro adequate
  have payment := (adequate site needsBridge claimsOriginalResolution).2.2.2.1
  rw [bridgeMissing] at payment
  cases payment

/-- The exact conditional policy result: equal complete profiles cannot carry
    opposite original-resolution and bridge-required judgments under a
    Q-uniform policy.  It is a policy contradiction, not `ZFC ⊢ False`. -/
theorem same_Q_opposite_judgments_break_uniformity
    (assessment : Assessment)
    (sameQ : assessment.profile .zeno = assessment.profile .hott)
    (zenoOriginal : assessment.judgment .zeno = .originalResolved)
    (hottBridgeRequired : assessment.judgment .hott = .bridgeRequired) :
    ¬ QUniform assessment := by
  intro uniform
  have equalJudgment := uniform .zeno .hott sameQ
  have impossible : CompletionJudgment.originalResolved = .bridgeRequired :=
    zenoOriginal.symm.trans (equalJudgment.trans hottBridgeRequired)
  cases impossible

/-- An explicitly revised completion contract is not an original-task
    resolution merely by sharing the ordinary-language word "resolved". -/
theorem revised_resolution_is_not_original_resolution :
    CompletionJudgment.revisedResolved ≠ .originalResolved := by
  decide

/-- A control against a false positive: two cases may both require a bridge
    and yet be judged differently when one has paid it and preserved the task. -/
def coarseSharedQButDifferentPaymentFixture : Assessment where
  profile
    | .zeno => {
        o1Represented := true, o2FormalCompletion := true,
        o3DistinguishesCompletion := true, o4SameTaskBridgeVerified := true,
        o5MetaAuditPerformed := true, requiresBridge := true,
        bridgePaid := true, originalTaskPreserved := true }
    | .hott => {
        o1Represented := true, o2FormalCompletion := true,
        o3DistinguishesCompletion := false, o4SameTaskBridgeVerified := false,
        o5MetaAuditPerformed := false, requiresBridge := true,
        bridgePaid := false, originalTaskPreserved := false }
  judgment
    | .zeno => .originalResolved
    | .hott => .bridgeRequired

theorem coarse_shared_Q_can_have_different_judgments :
    QUniform coarseSharedQButDifferentPaymentFixture := by
  intro left right sameProfile
  cases left <;> cases right
  · rfl
  · have paymentConflict := congrArg QProfile.bridgePaid sameProfile
    cases paymentConflict
  · have paymentConflict := congrArg QProfile.bridgePaid sameProfile
    cases paymentConflict
  · rfl

/-- The exact conditional fixture suggested by the user: O1/O2 are present,
    O3--O5 and bridge payment are absent, but Zeno is called originally
    resolved while HoTT is flagged as requiring a bridge. -/
def sameQAsymmetryFixture : Assessment where
  profile _ := {
    o1Represented := true, o2FormalCompletion := true,
    o3DistinguishesCompletion := false, o4SameTaskBridgeVerified := false,
    o5MetaAuditPerformed := false, requiresBridge := true,
    bridgePaid := false, originalTaskPreserved := false }
  judgment
    | .zeno => .originalResolved
    | .hott => .bridgeRequired

theorem sameQ_fixture_breaks_O3O5 :
    ¬ O3O5Adequate sameQAsymmetryFixture := by
  apply unbridged_original_resolution_breaks_O3O5 sameQAsymmetryFixture .zeno <;> rfl

theorem sameQ_fixture_breaks_uniformity :
    ¬ QUniform sameQAsymmetryFixture := by
  apply same_Q_opposite_judgments_break_uniformity sameQAsymmetryFixture <;> rfl

theorem sameQ_fixture_has_O1O2_without_O3O5 :
    (sameQAsymmetryFixture.profile .zeno).o1Represented = true ∧
    (sameQAsymmetryFixture.profile .zeno).o2FormalCompletion = true ∧
    (sameQAsymmetryFixture.profile .zeno).o3DistinguishesCompletion = false ∧
    (sameQAsymmetryFixture.profile .zeno).o4SameTaskBridgeVerified = false ∧
    (sameQAsymmetryFixture.profile .zeno).o5MetaAuditPerformed = false := by
  decide

#print axioms unbridged_original_resolution_breaks_O3O5
#print axioms same_Q_opposite_judgments_break_uniformity
#print axioms revised_resolution_is_not_original_resolution
#print axioms coarse_shared_Q_can_have_different_judgments
#print axioms sameQ_fixture_breaks_O3O5
#print axioms sameQ_fixture_breaks_uniformity
#print axioms sameQ_fixture_has_O1O2_without_O3O5

end ZFCCompletionPolicyUniformity
