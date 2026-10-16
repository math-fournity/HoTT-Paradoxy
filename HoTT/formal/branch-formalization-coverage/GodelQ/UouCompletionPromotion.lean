/-!
`MP-UOU-COMPLETION-PROMOTION-SOURCE-001` checks a finite transcription of a
frozen paragraph from Uttarakhand Open University's *Real Analysis* course
text.  It does not formalize ZFC, real analysis, Achilles' physical motion, or
the truth of the source's explanation.

The point of the card is deliberately narrow: the quoted paragraph explicitly
states a formal result F, a source-level catch-up/resolution Done D, and a
promotion from F to D, while the frozen paragraph supplies no separately
verified task-preserving bridge.  Absence below is absence *from this source
card*, never a claim that no bridge exists elsewhere.
-/

namespace UouCompletionPromotion

inductive SourceStatus where
  | stated
  | notSupplied
deriving DecidableEq

structure CompletionPromotionSourceCard where
  formalCompletion : SourceStatus
  namedOriginDone : SourceStatus
  promotionClaim : SourceStatus
  verifiedTaskBridge : SourceStatus
  doneDistinction : SourceStatus
  strongerDoneEquivalence : SourceStatus
deriving DecidableEq

/-- The source-card shape needed to classify a P candidate. -/
def MapsUnverifiedCompletionPromotionCandidate
    (card : CompletionPromotionSourceCard) : Prop :=
  card.formalCompletion = .stated ∧
    card.namedOriginDone = .stated ∧
    card.promotionClaim = .stated ∧
    card.verifiedTaskBridge = .notSupplied

/-- A source card does not establish a stronger completion contract merely by
    giving the named F-to-D promotion.  This is a card-status predicate, not a
    theorem about the source's mathematics. -/
def LeavesStrongerDoneUnestablished
    (card : CompletionPromotionSourceCard) : Prop :=
  card.doneDistinction = .notSupplied ∧
    card.strongerDoneEquivalence = .notSupplied

/-- Transcription of UOU *Real Analysis*, MT(N)-201 §5.1, physical PDF page
    75, as frozen in H104. -/
def uouFrozenCard : CompletionPromotionSourceCard where
  formalCompletion := .stated
  namedOriginDone := .stated
  promotionClaim := .stated
  verifiedTaskBridge := .notSupplied
  doneDistinction := .notSupplied
  strongerDoneEquivalence := .notSupplied

theorem uou_frozen_card_maps_P_candidate :
    MapsUnverifiedCompletionPromotionCandidate uouFrozenCard := by
  exact ⟨rfl, rfl, rfl, rfl⟩

theorem uou_frozen_card_leaves_stronger_done_unestablished :
    LeavesStrongerDoneUnestablished uouFrozenCard := by
  exact ⟨rfl, rfl⟩

theorem uou_candidate_does_not_establish_stronger_done_equivalence :
    MapsUnverifiedCompletionPromotionCandidate uouFrozenCard ∧
      LeavesStrongerDoneUnestablished uouFrozenCard := by
  exact ⟨uou_frozen_card_maps_P_candidate,
    uou_frozen_card_leaves_stronger_done_unestablished⟩

#print axioms uou_frozen_card_maps_P_candidate
#print axioms uou_frozen_card_leaves_stronger_done_unestablished
#print axioms uou_candidate_does_not_establish_stronger_done_equivalence

end UouCompletionPromotion
