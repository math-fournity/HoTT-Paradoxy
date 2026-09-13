module SemB01Kernel where

open import foundation.propositional-truncations
open import foundation.unit-type
open import foundation.universal-property-propositional-truncation-into-sets
open import foundation.weakly-constant-maps
open import foundation-core.booleans
open import foundation-core.identity-types

toTrue : unit → bool
toTrue _ = true

toTrue-is-weakly-constant : is-weakly-constant-map toTrue
toTrue-is-weakly-constant _ _ = refl

truncatedUnit : type-trunc-Prop unit
truncatedUnit = unit-trunc-Prop star

truncatedResult : bool
truncatedResult =
  map-universal-property-set-quotient-trunc-Prop
    bool-Set
    toTrue
    toTrue-is-weakly-constant
    truncatedUnit

truncatedResult-eq-true : truncatedResult ＝ true
truncatedResult-eq-true =
  htpy-universal-property-set-quotient-trunc-Prop
    bool-Set
    toTrue
    toTrue-is-weakly-constant
    star
