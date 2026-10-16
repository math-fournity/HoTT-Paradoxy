{-# OPTIONS --cubical --guarded --guardedness #-}

-- Negative control: erasing the tick binder does not construct forceNow.

module BadGuardedForce where

import LaterPrims as G

forceNow : ∀ {A : Set} → G.▹ A → A
forceNow delayed = delayed

