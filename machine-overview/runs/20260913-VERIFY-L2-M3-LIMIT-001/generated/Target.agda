{-# OPTIONS --safe --cubical --guardedness #-}

-- M3/L2 local-to-global target for MS-TASK-L2-TRUNCATED-LIMIT-001 / WV-0001.
-- Stagewise mere existence is kept distinct from one compatible exact limit.

module Target where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty.Base using (⊥)
import TransitionLift as TL

NoTruncatedLimitRecovery : Type
NoTruncatedLimitRecovery = (TL.LimTruncA → TL.LimA) → ⊥
