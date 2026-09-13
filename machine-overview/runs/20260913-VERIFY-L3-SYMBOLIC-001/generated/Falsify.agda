{-# OPTIONS --safe --cubical --guardedness #-}

module Falsify where

open import Cubical.Foundations.Prelude
open import L3MotionSupport

-- Negative control: Path abstraction cannot be applied to an ordinary two-stage index.
bad-stage-path : {A : Type₀} (f : Stage → A) → f start ≡ f finish
bad-stage-path f i = f i
