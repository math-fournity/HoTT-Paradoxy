{-# OPTIONS --safe #-}

-- L5 given-proof target for MS-TASK-L5-GIVEN-PROOF-CHECK-001 / WV-0001.
-- The derivation is supplied before checking; no search or truth decision is claimed.

module Target where

import ObjectSyntax as OS
import L5ConsumerSupport as L5

GivenProofAccepted : Set
GivenProofAccepted = OS.⊢ L5.kFormula
