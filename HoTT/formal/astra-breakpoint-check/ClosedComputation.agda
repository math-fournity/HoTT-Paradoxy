{-# OPTIONS --safe --cubical --guardedness #-}
module ClosedComputation where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Univalence
open import Cubical.Data.Bool
open import Cubical.Data.Sigma

nativeClosed : transport (ua notEquiv) true ≡ false
nativeClosed = refl

opaqueContractHasWitness : Σ[ p ∈ (Bool ≡ Bool) ] (transport p true ≡ false)
opaqueContractHasWitness = ua notEquiv , uaβ notEquiv true

module Symbolic (p : Bool ≡ Bool) (β : transport p true ≡ false) where
  pathCertificate : transport p true ≡ false
  pathCertificate = β
