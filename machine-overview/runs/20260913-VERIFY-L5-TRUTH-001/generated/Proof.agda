{-# OPTIONS --safe #-}

-- Proof term synthesized from AST 5c75d8265ee1c2f1c0b3ca4c0d64591e01636343fa77183ec6f38eb40d19ad04.

module Proof where

import L5ConsumerSupport as L5
import Target

proof : Target.RestrictedTruthDecided
proof = L5.truthDecision
