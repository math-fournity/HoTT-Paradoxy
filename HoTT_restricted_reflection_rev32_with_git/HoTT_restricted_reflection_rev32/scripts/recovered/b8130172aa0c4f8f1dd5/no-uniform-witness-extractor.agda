module hott-z.no-uniform-witness-extractor where

open import foundation.global-choice
open import foundation.negation
open import foundation.universe-levels

no-uniform-witness-extractor : {l : Level} → ¬ (Global-Choice l)
no-uniform-witness-extractor = no-global-choice
