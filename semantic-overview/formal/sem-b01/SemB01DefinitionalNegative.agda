module SemB01DefinitionalNegative where

open import SemB01Kernel
open import foundation-core.booleans
open import foundation-core.identity-types

-- Expected to be rejected: agda-unimath postulates truncations and their
-- universal property, so the unit computation law is propositional rather
-- than judgmental for this implementation.
truncatedResult-eq-true-by-refl : truncatedResult ＝ true
truncatedResult-eq-true-by-refl = refl
