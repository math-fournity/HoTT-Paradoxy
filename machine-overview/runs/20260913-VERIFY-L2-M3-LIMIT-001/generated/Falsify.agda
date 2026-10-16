{-# OPTIONS --safe --cubical --guardedness #-}

module Falsify where

import TransitionLift as TL

-- Negative control: a truncated limit is not an exact compatible limit.
bad-exact-limit : TL.LimA
bad-exact-limit = TL.C-115-limTrunc
