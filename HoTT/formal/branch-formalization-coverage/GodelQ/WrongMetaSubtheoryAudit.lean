import MetaSubtheoryAudit

open ZfcMetaSubtheoryAudit

/-- Deliberately false: the coarse meta interface accepts an unresolved state
    as formally complete, so it cannot promote every accepted result to origin
    completion. This file must be rejected by Lean. -/
theorem wrong_coarse_meta_promotes_formal_to_origin :
    MetaPromotesAcceptedAsOrigin coarseMeta coarseSubtheory := by
  intro state _
  cases state with
  | origin => trivial
  | unresolved => trivial
