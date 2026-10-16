{-# OPTIONS --safe #-}

-- Proof term synthesized from AST 034a4efdc3880504f6399285ad2c3fbd1097888ca01e72ed3f3ff95f90c19755.

module Proof where

import L5ConsumerSupport as L5
import Target

proof : Target.GivenProofAccepted
proof = L5.checkGivenProof (L5.givenK)
