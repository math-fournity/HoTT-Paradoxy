{-# OPTIONS --cubical --guarded --guardedness #-}

-- Conditional guarded-collapse target.
--
-- The exact Agda LaterPrims source supplies
--   fix : (▹ A → A) → A
-- relative to its explicitly declared Tick/dfix/pfix postulates.  If a
-- consumer additionally supplies an unrestricted same-clock eliminator
--   forceNow : ▹ A → A,
-- then `fix forceNow` inhabits every A, including bottom.  This does not claim
-- that Agda, GCTT, CCTT or a real application supplies forceNow.

module GuardedForceCollapse where

import LaterPrims as G

data ⊥ : Set where

collapse : (G.▹ ⊥ → ⊥) → ⊥
collapse forceNow = G.fix forceNow

