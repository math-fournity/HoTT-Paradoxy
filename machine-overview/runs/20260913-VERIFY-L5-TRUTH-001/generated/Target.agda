{-# OPTIONS --safe #-}

-- L5 finite-truth target for MS-TASK-L5-FINITE-TRUTH-DECISION-001 / WV-0001.
-- The decision domain is the closed finite BFml fragment only.

module Target where

open import Agda.Builtin.Bool using (true)
open import Agda.Builtin.Equality using (_≡_)
import L5ConsumerSupport as L5

RestrictedTruthDecided : Set
RestrictedTruthDecided = L5.evalB L5.truthFormula ≡ true
