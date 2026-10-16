{-# OPTIONS --safe --cubical --guardedness #-}

-- Independent controls for the M3 breadth cases.  The L5 searched diagonal
-- composition is deliberately absent; this module only supplies Boolean
-- negation's fixed-point boundary and a positive finite-proof checker.

module M3BreadthSupport where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true; not)
open import Cubical.Data.Bool.Properties using (false≢true; true≢false)
open import Cubical.Data.Empty.Base using (⊥)

notNoFixed : (b : Bool) → b ≡ not b → ⊥
notNoFixed false p = false≢true p
notNoFixed true p = true≢false p

checkGiven : true ≡ true → true ≡ true
checkGiven p = p

givenProof : true ≡ true
givenProof = refl
