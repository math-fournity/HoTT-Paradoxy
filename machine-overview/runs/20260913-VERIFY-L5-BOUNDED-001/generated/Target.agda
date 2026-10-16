{-# OPTIONS --safe #-}

-- L5 bounded-search target for MS-TASK-L5-BOUNDED-PROOF-SEARCH-001 / WV-0001.
-- One unit of fuel and the found derivation are both part of the target.

module Target where

open import Agda.Builtin.Bool using (true)
open import Agda.Builtin.Equality using (_≡_)
open import Agda.Builtin.Nat using (zero; suc)
import ObjectSyntax as OS
import L5ConsumerSupport as L5

record BoundedProofSearchFound : Set where
  constructor bounded
  field
    search-result : L5.searchK (suc zero) ≡ true
    found-proof : OS.⊢ L5.kFormula
