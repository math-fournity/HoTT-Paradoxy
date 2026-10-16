{-# OPTIONS --safe --cubical --guardedness #-}

-- Proof term synthesized from AST f7e15a7fa1967ae7810f646bba6a39b6d49192b2c4f6866da2c6bff77a21ab4c.

module Proof where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
import SIPRepresentation as SIP
import Target

proof : Target.NoOutsideObservationRecovery
proof f hs ht = SIP.C-125-obs-differs (sym (hs) ∙ cong f (SIP.C-124-identification) ∙ ht)
