module SemB02DefinitionalNegative where

open import SemB02Kernel
open import foundation-core.booleans
open import foundation-core.identity-types

-- Expected to be rejected: the branch obtained from mere finiteness is
-- propositionally correct but does not reduce judgmentally in this postulated
-- truncation implementation.
finiteTag-eq-false-by-refl : finiteTag ＝ false
finiteTag-eq-false-by-refl = refl
