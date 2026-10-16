module hott-z.no-canonical-earlier-event where

open import foundation.negation
open import foundation.universe-levels
open import univalent-combinatorics.2-element-types

EarlierEvent : {l : Level} → 2-Element-Type l → UU l
EarlierEvent X = type-2-Element-Type X

-- This is an interpretive wrapper around the upstream theorem.
no-canonical-earlier-event :
  {l : Level} → ¬ ((X : 2-Element-Type l) → EarlierEvent X)
no-canonical-earlier-event = no-section-type-2-Element-Type
