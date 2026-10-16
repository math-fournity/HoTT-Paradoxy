{-# OPTIONS --cubical --guarded #-}
module PathIndexedObservationClaim where

open import Agda.Builtin.Cubical.Path
open import Agda.Builtin.Reflection
open import Clocked.Primitives
open import ReflectionReductionClassification

path-indexed-observation
  : ∀ {k} → ▸ k \ α
  → directForceObs k ≡ directOrdinaryObs α
path-indexed-observation {k} α i =
  normalisedIsZero (force-delay family k α i)

