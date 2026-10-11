/-!
`MP-SEP-COMPLETION-PROMOTION-SOURCE-001` machine-checks the classification of
a frozen SEP source card, not SEP's mathematics or a fact about actual ZFC.

The card records five source-level claims: convergence is stated, a promotion
to every-step completion is stated, every-step Done is named, final-action Done
is excluded, and a verified task-preserving bridge is not supplied on the
frozen card.  The theorem only checks that these frozen labels meet the project's
definition of an actual P *candidate source map*.
-/

namespace SepCompletionPromotion

inductive SourceStatus where
  | stated
  | notSupplied
deriving DecidableEq

structure CompletionPromotionSourceCard where
  formalCompletion : SourceStatus
  promotionClaim : SourceStatus
  namedOriginDone : SourceStatus
  verifiedBridge : SourceStatus
  finalActionExcluded : SourceStatus
deriving DecidableEq

/-- A source maps the P candidate when it states F, a promotion to named D,
and no verified bridge is supplied in the frozen source card. -/
def MapsUnverifiedCompletionPromotion (card : CompletionPromotionSourceCard) : Prop :=
  card.formalCompletion = .stated ∧
    card.promotionClaim = .stated ∧
    card.namedOriginDone = .stated ∧
    card.verifiedBridge = .notSupplied

/-- The classification of the SEP lines 46--53 frozen in H103. This is a
transcribed source card, not a proof of the English source's truth. -/
def sepFrozenCard : CompletionPromotionSourceCard where
  formalCompletion := .stated
  promotionClaim := .stated
  namedOriginDone := .stated
  verifiedBridge := .notSupplied
  finalActionExcluded := .stated

theorem sep_frozen_card_maps_P_candidate :
    MapsUnverifiedCompletionPromotion sepFrozenCard := by
  exact ⟨rfl, rfl, rfl, rfl⟩

theorem sep_frozen_card_excludes_final_action :
    sepFrozenCard.finalActionExcluded = .stated := by
  decide

theorem p_candidate_does_not_imply_final_action_completion :
    MapsUnverifiedCompletionPromotion sepFrozenCard ∧
      sepFrozenCard.finalActionExcluded = .stated := by
  exact ⟨sep_frozen_card_maps_P_candidate, sep_frozen_card_excludes_final_action⟩

#print axioms sep_frozen_card_maps_P_candidate
#print axioms sep_frozen_card_excludes_final_action
#print axioms p_candidate_does_not_imply_final_action_completion

end SepCompletionPromotion
