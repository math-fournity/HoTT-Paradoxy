import CompletionPromotionTension

open ZfcMetaSubtheoryAudit
open ZfcCompletionPromotionTension

/-- Deliberately false: in the coarse fixture the policy promotes a formally
    complete unresolved state, although that state is not origin complete.
    Lean must reject the attempted soundness proof. -/
theorem wrong_promoted_policy_is_sound_on_coarse_fixture :
    PolicySound promotedPolicy coarseSubtheory.task := by
  intro state _
  cases state with
  | origin => trivial
  | unresolved => assumption
