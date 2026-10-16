{-# OPTIONS --safe --cubical --guardedness #-}

-- Proof term synthesized from AST bdc25fd93a061e96ddffd725fbcf4682fd88411450bba178d9625c0f70eb7ad5.

module Proof where

open import Cubical.Foundations.Prelude
open import L3M4Support
import Target

proof : Target.FiniteToExact
proof finite = finiteToExactCandidate (finite)
