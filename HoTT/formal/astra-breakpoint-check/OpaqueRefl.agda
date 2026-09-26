{-# OPTIONS --cubical --guardedness #-}
module OpaqueRefl where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool
open import OpaquePath
bad : transport p true ≡ false
bad = refl
