{-# OPTIONS --cubical --guardedness #-}
module OpaquePath where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool
-- Explicit axiom control; this exact pair has a safe native witness elsewhere.
postulate
  p : Bool ≡ Bool
  β : transport p true ≡ false
certificate : transport p true ≡ false
certificate = β
