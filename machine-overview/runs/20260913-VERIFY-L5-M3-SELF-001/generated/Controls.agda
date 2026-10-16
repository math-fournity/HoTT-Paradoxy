{-# OPTIONS --safe --cubical --guardedness #-}

module Controls where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true; not)
open import Cubical.Data.Empty.Base using (⊥)
open import M3BreadthSupport

check-given : true ≡ true → true ≡ true
check-given = checkGiven

check-no-fixed : (b : Bool) → b ≡ not b → ⊥
check-no-fixed = notNoFixed
