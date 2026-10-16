{-# OPTIONS --safe --cubical --guardedness #-}

module Verify where

open import Target
open import Proof

check : PathCarrierCoherence
check = proof
