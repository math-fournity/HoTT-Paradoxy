module hott-z.no-canonical-temporal-order where

open import foundation.negation
open import foundation.universe-levels
open import univalent-combinatorics.2-element-types

record TemporalOrder {l : Level} (X : 2-Element-Type l) : UU l where
  field
    least-event : type-2-Element-Type X
open TemporalOrder public

-- Any temporal-order structure that includes a chosen least event would give
-- a forbidden global section of the canonical two-element family.
no-canonical-temporal-order :
  {l : Level} → ¬ ((X : 2-Element-Type l) → TemporalOrder X)
no-canonical-temporal-order choose =
  no-section-type-2-Element-Type (λ X → least-event (choose X))
