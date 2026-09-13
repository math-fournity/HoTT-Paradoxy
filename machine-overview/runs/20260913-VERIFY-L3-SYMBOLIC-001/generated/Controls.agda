{-# OPTIONS --safe --cubical --guardedness #-}

module Controls where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Empty.Base using (⊥)
open import L3MotionSupport

check-stage-change : (phase start ≡ phase finish) → ⊥
check-stage-change = phase-changes

check-segment-motion : left ≡ right
check-segment-motion = segment-motion
