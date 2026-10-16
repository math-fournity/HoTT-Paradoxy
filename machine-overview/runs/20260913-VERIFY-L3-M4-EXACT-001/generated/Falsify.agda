{-# OPTIONS --safe --cubical --guardedness #-}

module Falsify where

open import Cubical.Data.Nat.Base using (zero)
open import L3M4Support

-- Negative control: a finite approximation is not an ExactArrival constructor.
bad-exact-arrival : ExactArrival
bad-exact-arrival = approximate zero
