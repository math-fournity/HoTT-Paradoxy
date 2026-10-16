{-# OPTIONS --safe --cubical --guardedness #-}

module Controls where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty.Base using (⊥)
import L3M4Support as L3

check-path-repair : L3.left ≡ L3.right
check-path-repair = L3.segment-path

check-apart-repair : L3.phase L3.start ≡ L3.phase L3.finish → ⊥
check-apart-repair = L3.phase-apart
