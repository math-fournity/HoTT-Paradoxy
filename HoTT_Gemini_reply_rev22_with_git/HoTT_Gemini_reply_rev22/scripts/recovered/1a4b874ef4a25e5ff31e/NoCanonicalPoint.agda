{-# OPTIONS --without-K --exact-split --no-import-sorts --auto-inline --no-require-unique-meta-solutions -WnoWithoutKFlagPrimEraseEquality --no-postfix-projections #-}

module hott-z.NoCanonicalPoint where

open import foundation.negation
open import foundation.universe-levels
open import univalent-combinatorics.2-element-types

-- This is the exact mathematical content imported from agda-unimath: there
-- is no uniform point of every unlabeled 2-element type.
no-canonical-point :
  {l : Level} → ¬ ((X : 2-Element-Type l) → type-2-Element-Type X)
no-canonical-point = no-section-type-2-Element-Type

-- A "first endpoint" package contains only a chosen point.  It is deliberately
-- not called a temporal order: no irreflexivity, transitivity, or totality
-- axiom is present.  Any temporal reading therefore needs a separate bridge.
record PointedOrientation {l : Level} (X : 2-Element-Type l) : UU l where
  field
    first-endpoint : type-2-Element-Type X

open PointedOrientation public

no-canonical-pointed-orientation :
  {l : Level} → ¬ ((X : 2-Element-Type l) → PointedOrientation X)
no-canonical-pointed-orientation choose =
  no-section-type-2-Element-Type (λ X → first-endpoint (choose X))
