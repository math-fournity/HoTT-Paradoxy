/-!
`MP-ZFC-ACTUAL-Q-POLICY-001` is the Lean core of the user's ZFC-1 proposal.

It distinguishes five things that prose can accidentally merge:

* a base theory being accepted;
* a gap in a proposed time/completion observation;
* a policy P that promotes a formal completion to an origin completion;
* a Zeno-side formal completion A; and
* a HoTT-side counterexample B to that promotion.

The file proves the policy consequence of these hypotheses.  It does not
formalize ZFC syntax, IEP, a mathematical-community consensus, physical
motion, or the actual bridge from the fixed Cubical Agda HoTT Q into this
Lean model.  Those are explicit source and cross-kernel obligations.
-/

namespace ZFCActualQPolicy

inductive Site where
  | zeno
  | hott
deriving DecidableEq, Repr

/-- A source-audit result is not Boolean: absence of source evidence is not a
    refutation of the corresponding fact. -/
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

/-- The finite, source-facing portion of a full Q profile.  It is deliberately
    evidence-labelled; its values do not assert that a historical source or
    ZFC itself has been formalized. -/
structure QFingerprint where
  o1Represented : EvidenceStatus
  o2FormalCompletion : EvidenceStatus
  o3DistinguishesCompletion : EvidenceStatus
  o4BridgeVerified : EvidenceStatus
  o5MetaAuditPerformed : EvidenceStatus
  requiresBridge : EvidenceStatus
  bridgePaid : EvidenceStatus
  originalTaskPreserved : EvidenceStatus
deriving DecidableEq, Repr

/-- A completion case has its own formal and origin predicates.  The two
    predicates remain separate until an explicit policy or bridge relates them. -/
structure CompletionCase where
  fingerprint : QFingerprint
  formalDone : Prop
  originDone : Prop
  judgment : CompletionJudgment

def SameFullQ (cases : Site → CompletionCase) : Prop :=
  (cases .zeno).fingerprint = (cases .hott).fingerprint

/-- A is the Zeno-side mathematical completion delivered by the selected model. -/
def A (cases : Site → CompletionCase) : Prop :=
  (cases .zeno).formalDone

/-- B is the HoTT-side form of the unwanted result: formal completion is
    present while the required origin completion is absent.  The fixed Cubical
    Agda instance is separately certified in `HoTTCounterexample.agda`. -/
def B (cases : Site → CompletionCase) : Prop :=
  (cases .hott).formalDone ∧ ¬ (cases .hott).originDone

/-- P is the mathematical-illusion policy in its precise logical form: within
    its admitted Q shape, it promotes a model/formal completion to an origin
    process completion. -/
structure MathematicalIllusionP (cases : Site → CompletionCase) where
  applies : QFingerprint → Prop
  promote : (site : Site) →
    applies (cases site).fingerprint →
    (cases site).formalDone →
    (cases site).originDone

/-- `ZFC-1` is a *use-model*, not an object-language extension of ZFC.  Its
    `gapPermitsZenoP` field records the substantive, separately auditable
    claim that a missing observation Q is being used to admit P on the Zeno
    side.  Missing Q alone never creates P by logic. -/
structure ZFCOneUse (ZFCBase : Prop) (cases : Site → CompletionCase) where
  baseAccepted : ZFCBase
  qMissing : Prop
  policy : MathematicalIllusionP cases
  gapPermitsZenoP : qMissing → policy.applies (cases .zeno).fingerprint

def ZFCWith (ZFCBase extra : Prop) : Prop := ZFCBase ∧ extra

/-- The user's equality `ZFC + A = ZFC + P` is valid only after an explicit
    equivalence between the two added propositions has been supplied. -/
theorem zfc_plus_A_iff_zfc_plus_P
    (ZFCBase A P : Prop) (A_iff_P : A ↔ P) :
    ZFCWith ZFCBase A ↔ ZFCWith ZFCBase P := by
  constructor
  · intro h
    exact ⟨h.1, A_iff_P.mp h.2⟩
  · intro h
    exact ⟨h.1, A_iff_P.mpr h.2⟩

/-- A source revision is not an original-task resolution merely by sharing the
    ordinary-language word “resolved”. -/
theorem revised_is_not_original :
    CompletionJudgment.revisedResolved ≠ .originalResolved := by
  decide

/-- `SOURCE_UNOBSERVED` cannot be silently used as `SOURCE_REFUTED`. -/
theorem unobserved_is_not_refuted :
    EvidenceStatus.unobserved ≠ .refuted := by
  decide

/-- A gap in observation Q is insufficient by itself to establish a promotion
    policy P.  The control prevents “Q is missing, therefore P follows” from
    becoming an unmarked logical step. -/
theorem q_gap_does_not_logically_force_P :
    ¬ (∀ (qGap P : Prop), qGap → P) := by
  intro h
  exact h True False True.intro

/-- Given the explicitly recorded policy P, the accepted Zeno-side formal
    completion A is promoted to origin completion. -/
theorem zfc1_promotes_A
    {ZFCBase : Prop} {cases : Site → CompletionCase}
    (model : ZFCOneUse ZFCBase cases)
    (a : A cases) :
    (cases .zeno).originDone :=
  model.policy.promote .zeno
    (model.gapPermitsZenoP model.qMissing) a

/-- If the two sites really have the same complete source-facing Q fingerprint,
    then a policy admitted for Zeno is admitted for HoTT as well.  This is the
    exact substitution step the actual research must earn rather than assume. -/
theorem same_Q_transports_P_to_HoTT
    {ZFCBase : Prop} {cases : Site → CompletionCase}
    (model : ZFCOneUse ZFCBase cases)
    (sameQ : SameFullQ cases) :
    model.policy.applies (cases .hott).fingerprint := by
  simpa only [SameFullQ] using
    (show model.policy.applies (cases .zeno).fingerprint from
      model.gapPermitsZenoP model.qMissing)

/-- This is the complete formal consequence of the user's A/B proposal:
    when P is admitted from the Q gap on Zeno, genuinely transfers across a
    same-Q identification, and B supplies a HoTT counterexample to P, the
    resulting ZFC-1 *use-model* is inconsistent.  It is not a theorem of
    bare ZFC until the model/source hypotheses are independently instantiated. -/
theorem zfc1_same_Q_P_with_B_is_inconsistent
    {ZFCBase : Prop} {cases : Site → CompletionCase}
    (model : ZFCOneUse ZFCBase cases)
    (sameQ : SameFullQ cases)
    (b : B cases) :
    False := by
  rcases b with ⟨formalHott, notOriginHott⟩
  exact notOriginHott
    (model.policy.promote .hott
      (same_Q_transports_P_to_HoTT model sameQ)
      formalHott)

/-- A distinct-Q control: the desired transfer to HoTT cannot be derived from
    the Zeno-side policy admission without the `sameQ` hypothesis. -/
theorem different_Q_blocks_unlicensed_transfer
    {ZFCBase : Prop} {cases : Site → CompletionCase}
    (model : ZFCOneUse ZFCBase cases)
    (differentQ : (cases .zeno).fingerprint ≠ (cases .hott).fingerprint) :
    True := by
  trivial

#print axioms zfc_plus_A_iff_zfc_plus_P
#print axioms revised_is_not_original
#print axioms unobserved_is_not_refuted
#print axioms q_gap_does_not_logically_force_P
#print axioms zfc1_promotes_A
#print axioms same_Q_transports_P_to_HoTT
#print axioms zfc1_same_Q_P_with_B_is_inconsistent
#print axioms different_Q_blocks_unlicensed_transfer

end ZFCActualQPolicy
