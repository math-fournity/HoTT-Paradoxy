{-# OPTIONS --safe --cubical --guardedness #-}

-- Proof term synthesized from AST 7e96a14d76183e976ee8081dab44ce1a67c03e29ea8fdde52499f06339f1921d.

module Proof where

open import Cubical.Foundations.Prelude
import Target

proof : Target.PathCarrierCoherence
proof f = (λ i → f i)
