{-# OPTIONS --safe --cubical --guardedness #-}

-- Proof term synthesized from AST 562c3e9090c7d4823f9198304a0365f318904908e42a0c589a16270b3ba8d414.

module Proof where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty.Base using (⊥)
import TransitionLift as TL
import Target

proof : Target.NoTruncatedLimitRecovery
proof recover = TL.C-114-LimA-empty (recover (TL.C-115-limTrunc))
