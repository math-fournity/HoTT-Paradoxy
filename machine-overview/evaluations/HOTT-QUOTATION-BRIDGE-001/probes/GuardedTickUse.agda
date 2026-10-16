{-# OPTIONS --cubical --guarded --guardedness #-}

-- Positive control: a delayed value can be consumed only under a tick.

module GuardedTickUse where

import LaterPrims as G

useAfterTick : ∀ {A : Set} → G.▹ A → G.▹ A
useAfterTick delayed tick = delayed tick

introduceLater : ∀ {A : Set} → A → G.▹ A
introduceLater = G.next

