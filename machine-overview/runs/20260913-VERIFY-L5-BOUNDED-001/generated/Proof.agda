{-# OPTIONS --safe #-}

-- Proof term synthesized from AST 5b10f679ea9a299ec255b64581f034f757000b6b21eb895240161486ffcb103b.

module Proof where

import L5ConsumerSupport as L5
import Target

proof : Target.BoundedProofSearchFound
proof = Target.bounded (L5.searchAtOne) (L5.searchSoundAtOne (L5.searchAtOne))
