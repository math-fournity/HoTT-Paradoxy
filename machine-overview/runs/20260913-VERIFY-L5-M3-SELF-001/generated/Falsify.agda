{-# OPTIONS --safe --cubical --guardedness #-}

module Falsify where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (false; not)

-- Negative control: false is not a fixed point of Boolean negation.
bad-fixed-point : false ≡ not false
bad-fixed-point = refl
