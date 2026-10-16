import MetaSubtheoryAudit

/-!
`MP-ZFC-COMPLETION-PROMOTION-TENSION-001` refines the user's Q/P/A/B
proposal at the point where a formal result is promoted to a claim about an
origin process.

It is not a formalization of ZFC, real analysis, HoTT, a mathematical
community, physical motion, or an assertion that an actual source makes this
promotion.  Its central distinction is deliberately sharp:

* `PAdopted` is a policy rule that permits a *derivation* of origin completion
  from formal completion.
* a `CompletionBridge` is the semantic fact that makes that rule sound.

The first can be adopted without the second.  A countertrace then refutes the
soundness of the policy; it does not prove an object-language inconsistency of
ZFC.  The two-state fixtures reuse the exact Meta/Sub Theory task from the
companion package.
-/

open ZfcMetaSubtheoryAudit

namespace ZfcCompletionPromotionTension

universe u

/-- Two distinct judgments concerning one fixed process state. -/
inductive CompletionJudgment where
  | formalComplete
  | originComplete
deriving DecidableEq, Repr

/-- `admitsPromotion = true` is an inference-policy choice.  It is not itself
    evidence that the associated semantic bridge is true. -/
structure PromotionPolicy where
  admitsPromotion : Bool
deriving DecidableEq, Repr

/-- The exact policy-level reading of P used in this small calculus. -/
def PAdopted (policy : PromotionPolicy) : Prop :=
  policy.admitsPromotion = true

/-- A policy can record a formal completion and, if P is adopted, promote that
    judgment to origin completion.  The latter is a syntactic derivation, not
    a semantic validity theorem. -/
inductive Derives {State : Type u} (policy : PromotionPolicy)
    (task : ProcessTask State) : State → CompletionJudgment → Prop where
  | formal {state : State} : task.formalDone state →
      Derives policy task state .formalComplete
  | promote {state : State} : PAdopted policy →
      Derives policy task state .formalComplete →
      Derives policy task state .originComplete

/-- The semantic bridge which a sound promotion rule must actually pay. -/
def CompletionBridge {State : Type u} (task : ProcessTask State) : Prop :=
  ∀ state, task.formalDone state → task.originDone state

/-- Policy soundness is evaluated against the origin-process predicate, not
    merely against what the policy itself can derive. -/
def PolicySound {State : Type u} (policy : PromotionPolicy)
    (task : ProcessTask State) : Prop :=
  ∀ state, Derives policy task state .originComplete → task.originDone state

/-- A is the formal-completion judgment at one named process state. -/
def FormalResolutionA {State : Type u} (policy : PromotionPolicy)
    (task : ProcessTask State) (state : State) : Prop :=
  Derives policy task state .formalComplete

/-- B is the semantic countertrace: the original process has not completed at
    that same named state. -/
def OriginCountertraceB {State : Type u} (task : ProcessTask State)
    (state : State) : Prop :=
  ¬ task.originDone state

/-- Every derived origin-completion judgment records the adopted P rule and
    the formal-completion premise that was promoted.  This is a derivation
    provenance fact, not a claim about an actual historical derivation. -/
theorem origin_derivation_exposes_p_and_A
    {State : Type u} (policy : PromotionPolicy) (task : ProcessTask State)
    (state : State)
    (derivation : Derives policy task state .originComplete) :
    PAdopted policy ∧ FormalResolutionA policy task state := by
  cases derivation with
  | promote p formal => exact ⟨p, formal⟩

/-- A promotion policy is semantically sound only if its P rule pays a
    statewise completion bridge.  This gives a formal meaning to the phrase
    “a completion claim needs a bridge”; it does not source-map that bridge to
    ZFC or to any actual theory. -/
theorem sound_adopted_P_pays_completion_bridge
    {State : Type u} (policy : PromotionPolicy) (task : ProcessTask State)
    (p : PAdopted policy) (sound : PolicySound policy task) :
    CompletionBridge task := by
  intro state formal
  exact sound state (.promote p (.formal formal))

/-- A concrete policy whose rule admits the promotion. -/
def promotedPolicy : PromotionPolicy where
  admitsPromotion := true

/-- A control policy that does not make the promotion.  It uses the same
    process and the same observation boundary as `promotedPolicy`. -/
def guardedPolicy : PromotionPolicy where
  admitsPromotion := false

/-- The companion Meta/Sub fixture has a coarse observation that cannot audit
    origin completion.  This is a relative Q-missing fact for that fixture,
    not a theorem about actual ZFC. -/
theorem coarse_fixture_lacks_Q_observation_capacity :
    ¬ MetaCanAuditOriginDone coarseMeta coarseSubtheory :=
  coarse_meta_lacks_origin_audit

theorem promoted_policy_adopts_P : PAdopted promotedPolicy := by
  rfl

theorem guarded_policy_does_not_adopt_P : ¬ PAdopted guardedPolicy := by
  intro h
  cases h

/-- In the coarse fixture the unresolved state is formally complete.  This is
    the local A-side input; it does not yet assert origin completion. -/
theorem coarse_unresolved_has_formal_resolution_A :
    FormalResolutionA promotedPolicy coarseSubtheory.task .unresolved := by
  exact .formal True.intro

/-- In that same state, origin completion is false.  This is the B-side
    countertrace, not a judgment of any actual mathematical community. -/
theorem coarse_unresolved_has_origin_countertrace_B :
    OriginCountertraceB coarseSubtheory.task .unresolved := by
  intro h
  exact h

/-- Once P is adopted, the policy derives origin completion for the same state
    from its formal-completion judgment. -/
theorem promoted_policy_derives_origin_completion_at_countertrace :
    Derives promotedPolicy coarseSubtheory.task .unresolved .originComplete := by
  exact .promote promoted_policy_adopts_P
    coarse_unresolved_has_formal_resolution_A

/-- The P/A/B fixture makes the policy semantically unsound.  This is the
    precise proof-level counterpart of the proposed “mathematical illusion”:
    a derivable completion judgment is not licensed by the process semantics.
    It is deliberately *not* an object-language contradiction of ZFC. -/
theorem P_A_B_fixture_breaks_policy_soundness :
    ¬ PolicySound promotedPolicy coarseSubtheory.task := by
  intro sound
  exact coarse_unresolved_has_origin_countertrace_B
    (sound .unresolved promoted_policy_derives_origin_completion_at_countertrace)

/-- Q-missing alone does not logically force adoption of P.  The same coarse
    observation fixture can use `guardedPolicy`, which refuses the promotion.
    Thus any real `Q-missing → P` claim needs a separate source-defined
    permission/adoption premise, exactly as in CommunityObservationPolicy. -/
theorem Q_missing_alone_does_not_entail_P_adoption :
    (¬ MetaCanAuditOriginDone coarseMeta coarseSubtheory) ∧
      ¬ PAdopted guardedPolicy := by
  exact ⟨coarse_fixture_lacks_Q_observation_capacity,
    guarded_policy_does_not_adopt_P⟩

/-- Positive control: exactly the same adopted P rule is sound when the task
    itself has paid the bridge, namely when formal completion holds precisely
    at the origin-complete state. -/
theorem promoted_policy_is_sound_when_bridge_is_paid :
    PolicySound promotedPolicy paidSubtheory.task := by
  intro state derivation
  cases derivation with
  | promote _ formal =>
      cases formal with
      | formal h =>
          cases state with
          | origin => trivial
          | unresolved => exact False.elim h

/-- The positive control yields the actual bridge required by the generic
    theorem above. -/
theorem paid_fixture_has_completion_bridge :
    CompletionBridge paidSubtheory.task :=
  sound_adopted_P_pays_completion_bridge promotedPolicy paidSubtheory.task
    promoted_policy_adopts_P promoted_policy_is_sound_when_bridge_is_paid

/-- The coarse countertrace proves that no semantic completion bridge exists
    for that fixture. -/
theorem coarse_fixture_has_no_completion_bridge :
    ¬ CompletionBridge coarseSubtheory.task := by
  intro bridge
  exact coarse_unresolved_has_origin_countertrace_B (bridge .unresolved True.intro)

/-- The complete bounded relation among Q, P, A and B in the controlled
    fixture.  It deliberately leaves the real-source mapping as an external
    obligation. -/
theorem controlled_Q_P_A_B_tension :
    (¬ MetaCanAuditOriginDone coarseMeta coarseSubtheory) ∧
      PAdopted promotedPolicy ∧
      FormalResolutionA promotedPolicy coarseSubtheory.task .unresolved ∧
      OriginCountertraceB coarseSubtheory.task .unresolved ∧
      ¬ PolicySound promotedPolicy coarseSubtheory.task := by
  exact ⟨coarse_fixture_lacks_Q_observation_capacity,
    promoted_policy_adopts_P,
    coarse_unresolved_has_formal_resolution_A,
    coarse_unresolved_has_origin_countertrace_B,
    P_A_B_fixture_breaks_policy_soundness⟩

#print axioms origin_derivation_exposes_p_and_A
#print axioms sound_adopted_P_pays_completion_bridge
#print axioms coarse_fixture_lacks_Q_observation_capacity
#print axioms promoted_policy_adopts_P
#print axioms guarded_policy_does_not_adopt_P
#print axioms coarse_unresolved_has_formal_resolution_A
#print axioms coarse_unresolved_has_origin_countertrace_B
#print axioms promoted_policy_derives_origin_completion_at_countertrace
#print axioms P_A_B_fixture_breaks_policy_soundness
#print axioms Q_missing_alone_does_not_entail_P_adoption
#print axioms promoted_policy_is_sound_when_bridge_is_paid
#print axioms paid_fixture_has_completion_bridge
#print axioms coarse_fixture_has_no_completion_bridge
#print axioms controlled_Q_P_A_B_tension

end ZfcCompletionPromotionTension
