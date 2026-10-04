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

/-- An actual object-level contradiction needs an extra source-mapped
incompatibility premise.  A community merely disliking B cannot fill it. -/
theorem object_level_false_requires_formal_incompatibility
    (baseZFC : Theory)
    (incompatible : ¬ (Derives (zfc1 baseZFC) .desiredResolutionA ∧
      Derives (zfc1 baseZFC) .undesirableOutcomeB)) : False := by
  exact incompatible (zfc1_derives_A_and_B baseZFC)

#print axioms translatePlusAToZfc1
#print axioms translateZfc1ToPlusA
#print axioms zfcPlusA_sameOperationalConsequences_as_zfc1
#print axioms zfc1_derives_A_and_B
#print axioms PBacktrace.exposes_P
#print axioms zfc1_B_has_P_backtrace
#print axioms Q_absence_activates_operational_P
#print axioms admitted_P_can_be_marked_illusory
#print axioms zfc1_produces_normative_tension
#print axioms object_level_false_requires_formal_incompatibility

end ZfcCommunityObservationPolicy
