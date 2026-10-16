{-# OPTIONS --safe --cubical --guardedness #-}

module Falsify where

open import Cubical.Foundations.Prelude
import L3M4Support as L3

-- Negative control: a Segment path cannot be reused as a Stage endpoint path.
bad-stage-path : L3.start ≡ L3.finish
bad-stage-path = L3.segment-path
