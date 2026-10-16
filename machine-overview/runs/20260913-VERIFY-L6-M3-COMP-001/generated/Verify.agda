{-# OPTIONS --safe --cubical --guardedness #-}

module Verify where

open import Target
open import Proof

check : NoJointPathAndApart
check = proof
