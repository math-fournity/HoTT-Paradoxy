{-# OPTIONS --safe --cubical --guardedness #-}

-- Negative control for the GR-1 package: asserting that the artificial
-- equation art is definitionally refl.  Expected: kernel REJECTION
-- (art is a distinct path constructor, not refl).

module WrongArtIsRefl where

open import Cubical.Foundations.Prelude
open import ArtificialEquationControl

wrong : art ≡ refl
wrong = refl
