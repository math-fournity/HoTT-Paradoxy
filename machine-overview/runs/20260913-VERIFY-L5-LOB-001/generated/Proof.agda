{-# OPTIONS --safe #-}

-- Proof term synthesized from AST f3e60d5a935069305cdf2a8f75d9c9dafa76abe46349337b4fb80521b8d2330c.

module Proof where

open import L5ConsumerSupport using (⊥)
import L5ConsumerSupport as L5
import Target

proof : Target.NoLobSelfCertification
proof {Box = Box} reflect lob certify = reflect ⊥ (lob ⊥ (certify ⊥))
