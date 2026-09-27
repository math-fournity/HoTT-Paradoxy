{-# OPTIONS --safe --cubical --guardedness #-}

-- Negative control for the groupoid-universe package: assert that the
-- a-involution fixes (true,true).  Expected: kernel REJECTION
-- (a (tt,tt) = (false,true) != (true,true), computable).

module WrongGroupoidWitness where

open import Cubical.Foundations.Prelude
open import NoHitGroupoidUniverse using (a)

wrong : a (true , true) ≡ (true , true)
wrong = refl
