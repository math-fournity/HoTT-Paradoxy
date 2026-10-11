/-!
`MP-ZFC-META-OBSERVATION-CONSISTENCY-001` formalizes a conditional version of
the user's proposed Zeno/HoTT comparison.

It does not formalize ZFC, IEP, a community consensus, or the existing HoTT
candidate.  Rather, it distinguishes three claims which ordinary prose can
otherwise conflate:

* an original task is resolved;
* a revised completion contract is resolved;
* a bridge is still required.

The theorems say exactly when opposite judgments create an inconsistency in a
purportedly uniform O3--O5 completion-observation policy.
-/

namespace ZfcMetaObservationConsistency

/-- The two comparison sites.  They are labels in a formal meta-model, not a
    claim that either historical/theoretical site has already been instantiated. -/
inductive ComparisonSite where
  | zeno
  | hott
deriving DecidableEq

/-- Q must include every fact on which a completion judgment is permitted to
    turn.  Sharing only one slogan such as "has a limit" is too weak. -/
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

/-- Keep original-task resolution separate from a source's explicit revision of
    its completion contract. -/
inductive CompletionJudgment where
  | originalResolved
  | revisedResolved
  | bridgeRequired
deriving DecidableEq

structure Assessment where
  profile : ComparisonSite → QProfile
  judgment : ComparisonSite → CompletionJudgment

/-- The O3--O5 responsibility proposed by the user: if a case needs a bridge
    and is asserted to resolve the *original* task, both payment and task
    preservation must be available. -/
def O3O5Adequate (assessment : Assessment) : Prop :=
  ∀ site,
    (assessment.profile site).requiresBridge = true →
    assessment.judgment site = .originalResolved →
    (assessment.profile site).o3DistinguishesCompletion = true ∧
      (assessment.profile site).o4SameTaskBridgeVerified = true ∧
      (assessment.profile site).o5MetaAuditPerformed = true ∧
      (assessment.profile site).bridgePaid = true ∧
      (assessment.profile site).originalTaskPreserved = true

/-- A foundation-level policy is Q-uniform when exactly identical Q profiles
    receive exactly identical completion judgments. -/
def QUniform (assessment : Assessment) : Prop :=
  ∀ left right,
    assessment.profile left = assessment.profile right →
    assessment.judgment left = assessment.judgment right

/-- Calling a case an original-task resolution without a required paid,
    task-preserving bridge violates the proposed O3--O5 responsibility. -/
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

/-- If the full Q profile is the same at Zeno and HoTT sites, opposite
    judgments cannot be part of a Q-uniform policy.  This is a policy
    inconsistency theorem, not an object-language contradiction of ZFC. -/
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

/-- A source that explicitly reports a revised completion contract is not, by
    that label alone, claiming original-task resolution. -/
theorem revised_resolution_is_not_original_resolution :
    CompletionJudgment.revisedResolved ≠ .originalResolved := by
  decide

/-- Sharing only the coarse feature `requiresBridge = true` does *not* force
    equal judgments: one case may actually supply payment and task preservation.
    This prevents the meta-model from manufacturing a contradiction merely from
    a shared keyword. -/
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

/-- The exact fixture for the user's conditional hypothesis: full Q profiles
    agree, yet one site is called originally resolved and the other is flagged
    as needing a bridge. -/
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

/-- The candidate terminal wording's exact abstract shape: O1/O2 can be
    present while O3--O5 are absent.  This is a fixture theorem only; mapping
    it to ZFC requires independent source evidence. -/
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

end ZfcMetaObservationConsistency
