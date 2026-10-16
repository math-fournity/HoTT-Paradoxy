module no-uniform-witness-extractor where

open import foundation.global-choice
open import foundation.negation
open import foundation.universe-levels

-- Global choice is precisely the uniform extraction principle from the
-- Hilbert/propositional truncation used by agda-unimath.
no-uniform-witness-extractor :
  {l : Level} → ¬ (Global-Choice l)
no-uniform-witness-extractor = no-global-choice
