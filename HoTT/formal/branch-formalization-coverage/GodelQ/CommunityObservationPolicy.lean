/-!
`MP-ZFC-COMMUNITY-OBSERVATION-POLICY-001` is a deliberately small
meta-policy calculus for the user's Q/P/A/B proposal.

It is not a formalization of ZFC syntax, ZFC semantics, real analysis, HoTT,
the mathematical community, or a physical process.  `baseZFC` is an arbitrary
base theory parameter.  The A <-> P and P -> B rules are explicit hypotheses
of this calculus: they must be source-mapped before anybody may call them facts
about actual mathematical practice.
-/

namespace ZfcCommunityObservationPolicy

/-- The four named positions in the user's proposed chain. -/
inductive Claim where
  | desiredResolutionA
  | mathematicalIllusionP
  | undesirableOutcomeB
  | observationCapacityQ
deriving DecidableEq, Repr

/-- A base theory is represented only by the claims it makes available. -/
abbrev Theory := Claim → Prop

/-- Add one admitted claim to a theory.  This is a policy-extension operator,
not ZFC's object-language axiom-adjoining construction. -/
def extend (T : Theory) (c : Claim) : Theory := fun goal => T goal ∨ goal = c

/-- `ZFC-1` is a label for the operational policy extension that admits P. -/
def zfc1 (baseZFC : Theory) : Theory := extend baseZFC .mathematicalIllusionP

/-- The alternative operational extension that admits A. -/
def zfcPlusA (baseZFC : Theory) : Theory := extend baseZFC .desiredResolutionA

/-- The explicit, hypothetical community inference policy. -/
inductive Derives (T : Theory) : Claim → Prop where
  | base {c : Claim} : T c → Derives T c
  | aToP : Derives T .desiredResolutionA → Derives T .mathematicalIllusionP
  | pToA : Derives T .mathematicalIllusionP → Derives T .desiredResolutionA
  | pToB : Derives T .mathematicalIllusionP → Derives T .undesirableOutcomeB

/-- Two policy theories have the same consequences in this small calculus. -/
def SameOperationalConsequences (left right : Theory) : Prop :=
  ∀ c, Derives left c ↔ Derives right c

/-- Translating a derivation from `baseZFC + A` to `baseZFC + P` uses the
explicit A-to-P/P-to-A policy rules, rather than identifying A and P as the
same sentence. -/
theorem translatePlusAToZfc1 (baseZFC : Theory) {c : Claim} :
    Derives (zfcPlusA baseZFC) c → Derives (zfc1 baseZFC) c := by
  intro derivation
  induction derivation with
  | base h =>
      rcases h with hBase | hA
      · exact .base (Or.inl hBase)
      · cases hA
        exact .pToA (.base (Or.inr rfl))
  | aToP _ ih => exact .aToP ih
  | pToA _ ih => exact .pToA ih
  | pToB _ ih => exact .pToB ih

/-- The reverse translation from `baseZFC + P` to `baseZFC + A`. -/
theorem translateZfc1ToPlusA (baseZFC : Theory) {c : Claim} :
    Derives (zfc1 baseZFC) c → Derives (zfcPlusA baseZFC) c := by
  intro derivation
  induction derivation with
  | base h =>
      rcases h with hBase | hP
      · exact .base (Or.inl hBase)
      · cases hP
        exact .aToP (.base (Or.inr rfl))
  | aToP _ ih => exact .aToP ih
  | pToA _ ih => exact .pToA ih
  | pToB _ ih => exact .pToB ih

/-- The precise formal reading of the user's `ZFC + A = ZFC + P`: equality of
operational consequences under the stated policy rules, not literal equality
of ZFC axiom sets. -/
theorem zfcPlusA_sameOperationalConsequences_as_zfc1 (baseZFC : Theory) :
    SameOperationalConsequences (zfcPlusA baseZFC) (zfc1 baseZFC) := by
  intro c
  constructor
  · exact translatePlusAToZfc1 baseZFC
  · exact translateZfc1ToPlusA baseZFC

/-- Once P is admitted, the explicit policy derives both A and B. -/
theorem zfc1_derives_A_and_B (baseZFC : Theory) :
    Derives (zfc1 baseZFC) .desiredResolutionA ∧
      Derives (zfc1 baseZFC) .undesirableOutcomeB := by
  have p : Derives (zfc1 baseZFC) .mathematicalIllusionP :=
    .base (Or.inr rfl)
  exact ⟨.pToA p, .pToB p⟩

/-- A provenance object is needed before one may say that a particular B was
obtained *because of* P.  Mere coexistence of derivable P and B is weaker. -/
structure PBacktrace (T : Theory) where
  p : Derives T .mathematicalIllusionP
  b : Derives T .undesirableOutcomeB
  bFromP : b = .pToB p

/-- The explicit P-to-B branch carries a recoverable P antecedent. -/
theorem PBacktrace.exposes_P {T : Theory} (trace : PBacktrace T) :
    Derives T .mathematicalIllusionP := trace.p

/-- `zfc1` has a concrete P-to-B provenance in this calculus because P is the
added policy claim and B is obtained with the explicit P-to-B rule. -/
theorem zfc1PBacktrace (baseZFC : Theory) : PBacktrace (zfc1 baseZFC) where
  p := .base (Or.inr rfl)
  b := .pToB (.base (Or.inr rfl))
  bFromP := rfl

theorem zfc1_B_has_P_backtrace (baseZFC : Theory) :
    Derives (zfc1 baseZFC) .mathematicalIllusionP :=
  (zfc1PBacktrace baseZFC).exposes_P

/-- The Q layer distinguishes an absence of observation capacity, permission,
and actual adoption.  None of these are inferred from bare ZFC by definition. -/
structure CommunityAdoption (baseZFC : Theory) where
  hasObservationQ : Prop
  lacksObservationQ : ¬ hasObservationQ
  permitted : Claim → Prop
  absencePermitsP : ¬ hasObservationQ → permitted .mathematicalIllusionP
  adoptsP : permitted .mathematicalIllusionP →
    Derives (zfc1 baseZFC) .mathematicalIllusionP

/-- The user's Q-absence route, written with every non-logical step exposed as
a field of `CommunityAdoption`. -/
theorem Q_absence_activates_operational_P
    (baseZFC : Theory) (community : CommunityAdoption baseZFC) :
    Derives (zfc1 baseZFC) .mathematicalIllusionP :=
  community.adoptsP (community.absencePermitsP community.lacksObservationQ)

/-- The complete Q-absence route to the proposed A/B fork.  Every
    non-logical step remains a field of `CommunityAdoption`; this is not a
    theorem that actual ZFC lacks Q. -/
theorem Q_absence_activates_A_and_B
    (baseZFC : Theory) (community : CommunityAdoption baseZFC) :
    Derives (zfc1 baseZFC) .desiredResolutionA ∧
      Derives (zfc1 baseZFC) .undesirableOutcomeB := by
  have p := Q_absence_activates_operational_P baseZFC community
  exact ⟨.pToA p, .pToB p⟩

/-- Reality/computability obligations for calling P a mathematical illusion.
They are assumptions to be populated by a future source-and-process audit. -/
structure RealityAudit where
  computationalBridgeForP : Prop
  realityBridgeForP : Prop
  noComputationalBridge : ¬ computationalBridgeForP
  noRealityBridge : ¬ realityBridgeForP

def IsMathematicalIllusion (audit : RealityAudit) : Prop :=
  ¬ audit.computationalBridgeForP ∧ ¬ audit.realityBridgeForP

/-- A community can operationally admit P while a separately fixed audit marks
both of its computational and reality bridges absent. -/
theorem admitted_P_can_be_marked_illusory
    (baseZFC : Theory) (community : CommunityAdoption baseZFC)
    (audit : RealityAudit) :
    Derives (zfc1 baseZFC) .mathematicalIllusionP ∧ IsMathematicalIllusion audit := by
  exact ⟨Q_absence_activates_operational_P baseZFC community,
    ⟨audit.noComputationalBridge, audit.noRealityBridge⟩⟩

/-- Community preference is a distinct layer from logical derivability. -/
structure CommunityValues where
  wanted : Claim → Prop
  unwanted : Claim → Prop
  wantsA : wanted .desiredResolutionA
  rejectsB : unwanted .undesirableOutcomeB

def NormativeTension (T : Theory) (values : CommunityValues) : Prop :=
  Derives T .desiredResolutionA ∧
    Derives T .undesirableOutcomeB ∧
    values.wanted .desiredResolutionA ∧
    values.unwanted .undesirableOutcomeB

/-- This is the exact formal form of “the community gets A that it wants and
also B that it does not want.”  It is a policy/normative tension, not yet an
object-language contradiction. -/
theorem zfc1_produces_normative_tension
    (baseZFC : Theory) (values : CommunityValues) :
    NormativeTension (zfc1 baseZFC) values := by
  rcases zfc1_derives_A_and_B baseZFC with ⟨a, b⟩
  exact ⟨a, b, values.wantsA, values.rejectsB⟩

/-- A Q-absence route plus the community's stated values yields the proposed
    desired-A / unwanted-B tension.  “Unwanted” remains normative. -/
theorem Q_absence_produces_normative_tension
    (baseZFC : Theory) (community : CommunityAdoption baseZFC)
    (values : CommunityValues) :
    NormativeTension (zfc1 baseZFC) values := by
  rcases Q_absence_activates_A_and_B baseZFC community with ⟨a, b⟩
  exact ⟨a, b, values.wantsA, values.rejectsB⟩

/-- A formal truth constraint is stronger than a community value.  It is the
    additional hypothesis needed to turn a B consequence into `False`. -/
structure TruthConstraint (T : Theory) where
  excludesB : ¬ Derives T .undesirableOutcomeB

/-- Under a separately supplied truth constraint, the Q-absence policy route
    is inconsistent.  The constraint is not established for actual ZFC here. -/
theorem Q_absence_violates_truth_constraint
    (baseZFC : Theory) (community : CommunityAdoption baseZFC)
    (truth : TruthConstraint (zfc1 baseZFC)) : False := by
  exact truth.excludesB (Q_absence_activates_A_and_B baseZFC community).2

/-- An actual object-level contradiction needs an extra source-mapped
incompatibility premise.  A community merely disliking B cannot fill it. -/
theorem object_level_false_requires_formal_incompatibility
    (baseZFC : Theory)
    (incompatible : ¬ (Derives (zfc1 baseZFC) .desiredResolutionA ∧
      Derives (zfc1 baseZFC) .undesirableOutcomeB)) : False := by
  exact incompatible (zfc1_derives_A_and_B baseZFC)

/-- The same object-level route with Q-absence and adoption hypotheses kept
    visible, rather than hidden behind the definition of `zfc1`. -/
theorem Q_absence_incompatible_A_and_B_yields_false
    (baseZFC : Theory) (community : CommunityAdoption baseZFC)
    (incompatible : ¬ (Derives (zfc1 baseZFC) .desiredResolutionA ∧
      Derives (zfc1 baseZFC) .undesirableOutcomeB)) : False := by
  exact incompatible (Q_absence_activates_A_and_B baseZFC community)

/-- A concrete policy fixture: it assumes the abstract observation capacity is
    absent, permits P, and records the policy's explicit adoption of P.  It is
    a control model, not a claim about actual mathematical practice. -/
def missingQPolicyFixture (baseZFC : Theory) : CommunityAdoption baseZFC where
  hasObservationQ := False
  lacksObservationQ := fun h => h
  permitted := fun c => c = .mathematicalIllusionP
  absencePermitsP := fun _ => rfl
  adoptsP := fun _ => .base (Or.inr rfl)

/-- A community may value A and reject B in the normative sense without that
    value judgment itself supplying a formal incompatibility premise. -/
def tensionValuesFixture : CommunityValues where
  wanted := fun _ => True
  unwanted := fun _ => True
  wantsA := True.intro
  rejectsB := True.intro

theorem normative_tension_fixture_is_inhabited (baseZFC : Theory) :
    NormativeTension (zfc1 baseZFC) tensionValuesFixture :=
  Q_absence_produces_normative_tension baseZFC
    (missingQPolicyFixture baseZFC) tensionValuesFixture

/-- The control fixture refutes the attempted move from an inhabited normative
    tension to a claim that the tension is formally impossible. -/
theorem normative_tension_fixture_not_formally_incompatible (baseZFC : Theory) :
    ¬ (¬ NormativeTension (zfc1 baseZFC) tensionValuesFixture) := by
  intro incompatible
  exact incompatible (normative_tension_fixture_is_inhabited baseZFC)

/-- A policy-level B derivation has only two possible immediate origins in this
    calculus: B was already admitted by the base theory, or the explicit
    `P → B` rule was used.  This is the formal core of the user's requested
    reductio-style backtrace.  It does not identify an actual historical or
    mathematical derivation until the base and the rules have source evidence. -/
theorem undesirable_derivation_has_base_or_policy
    (T : Theory) (derivation : Derives T .undesirableOutcomeB) :
    T .undesirableOutcomeB ∨ Derives T .mathematicalIllusionP := by
  cases derivation with
  | base h => exact Or.inl h
  | pToB p => exact Or.inr p

/-- If B was not already a base-theory claim, any derivation of B in this
    calculus can be traced back to P.  The non-base premise is essential: a
    bare occurrence of B alone does not license causal or historical blame on
    P. -/
theorem nonbase_undesirable_derivation_backtracks_to_policy
    (T : Theory)
    (baseDoesNotContainB : ¬ T .undesirableOutcomeB)
    (derivation : Derives T .undesirableOutcomeB) :
    Derives T .mathematicalIllusionP := by
  rcases undesirable_derivation_has_base_or_policy T derivation with baseB | policy
  · exact False.elim (baseDoesNotContainB baseB)
  · exact policy

/-- The same backtrace inside `ZFC-1`: if B is not already supplied by the
    underlying base theory, a B derivation in the policy extension reaches the
    explicitly admitted P.  This is an operational derivation fact, not a
    theorem that actual ZFC has this derivation or this policy extension. -/
theorem zfc1_nonbase_B_backtracks_to_admitted_P
    (baseZFC : Theory)
    (baseDoesNotContainB : ¬ baseZFC .undesirableOutcomeB)
    (derivation : Derives (zfc1 baseZFC) .undesirableOutcomeB) :
    Derives (zfc1 baseZFC) .mathematicalIllusionP := by
  apply nonbase_undesirable_derivation_backtracks_to_policy (zfc1 baseZFC)
  · intro baseB
    rcases baseB with baseB | addedClaim
    · exact baseDoesNotContainB baseB
    · cases addedClaim
  · exact derivation

/-- Positive control for the limitation above: when B is a base claim, it has
    a derivation that does not by itself expose an antecedent P. -/
theorem base_B_is_an_alternative_derivation_origin
    (T : Theory) (baseB : T .undesirableOutcomeB) :
    Derives T .undesirableOutcomeB :=
  .base baseB

/-- Negative control: the A/P cycle cannot generate a claim without a base
    premise. -/
def emptyTheory : Theory := fun _ => False

theorem emptyTheory_derives_no_claim (c : Claim) :
    ¬ Derives emptyTheory c := by
  intro derivation
  induction derivation with
  | base h => exact h
  | aToP _ ih => exact ih
  | pToA _ ih => exact ih
  | pToB _ ih => exact ih

/-- In this model, P enters `zfc1` by an explicit extension, not from an
    assumption-free base theory. -/
theorem zfc1_is_strict_over_empty :
    Derives (zfc1 emptyTheory) .mathematicalIllusionP ∧
      ¬ Derives emptyTheory .mathematicalIllusionP := by
  constructor
  · exact .base (Or.inr rfl)
  · exact emptyTheory_derives_no_claim .mathematicalIllusionP

#print axioms translatePlusAToZfc1
#print axioms translateZfc1ToPlusA
#print axioms zfcPlusA_sameOperationalConsequences_as_zfc1
#print axioms zfc1_derives_A_and_B
#print axioms PBacktrace.exposes_P
#print axioms zfc1_B_has_P_backtrace
#print axioms Q_absence_activates_operational_P
#print axioms admitted_P_can_be_marked_illusory
#print axioms zfc1_produces_normative_tension
#print axioms Q_absence_activates_A_and_B
#print axioms Q_absence_produces_normative_tension
#print axioms Q_absence_violates_truth_constraint
#print axioms object_level_false_requires_formal_incompatibility
#print axioms Q_absence_incompatible_A_and_B_yields_false
#print axioms normative_tension_fixture_is_inhabited
#print axioms normative_tension_fixture_not_formally_incompatible
#print axioms undesirable_derivation_has_base_or_policy
#print axioms nonbase_undesirable_derivation_backtracks_to_policy
#print axioms zfc1_nonbase_B_backtracks_to_admitted_P
#print axioms base_B_is_an_alternative_derivation_origin
#print axioms emptyTheory_derives_no_claim
#print axioms zfc1_is_strict_over_empty

end ZfcCommunityObservationPolicy
