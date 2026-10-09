{-# OPTIONS --safe --cubical --guardedness #-}
-- Negative control for CG001-C-112: "the runner arrives ⟹ never settled" needs the
-- proviso that a settled stage stays settled.  The alternating question arrives
-- (monotoneNeeded) but is settled at stage 0; passing it off as monotone must be rejected.
module WrongRunnerWithoutMonotone where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma
open import SameQ

wrongNeverAlt : Never alt
wrongNeverAlt = neverOfArrives alt (λ k p → p) (fst (snd monotoneNeeded))
