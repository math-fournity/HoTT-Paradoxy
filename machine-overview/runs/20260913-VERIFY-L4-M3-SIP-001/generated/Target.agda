{-# OPTIONS --safe --cubical --guardedness #-}

-- M3/L4 SIP observation target for MS-TASK-L4-SIP-OBSERVATION-001 / WV-0001.
-- The observer asks for data outside the identified structure's signature.

module Target where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Empty.Base using (⊥)
import SIPRepresentation as SIP

NoOutsideObservationRecovery : Type₁
NoOutsideObservationRecovery =
  (f : SIP.Str → Bool) → f SIP.s ≡ true → f SIP.t ≡ false → ⊥
