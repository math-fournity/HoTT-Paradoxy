{-# OPTIONS --safe --cubical --guardedness #-}

-- Proof term synthesized from AST 450b7226e8ba0da8b670eecc1bd9b4053d080f6ab4fdce5416620ac5cb2c3b24.

module Proof where

open import Cubical.Foundations.Prelude
open import L3M4Support
open import Cubical.Data.Prod.Base using (_,_)
import Target

proof : Target.ExactEventBoundary
proof = (phase-start , (phase-finish , phase-apart))
