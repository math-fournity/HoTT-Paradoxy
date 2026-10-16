{-# OPTIONS --safe --cubical-compatible --no-guardedness #-}

-- Negative control: an Agda TC computation is not an object-level value.

module BadRunTC where

import Agda.Builtin.Reflection as R

runTC : ∀ {a} {A : Set a} → R.TC A → A
runTC computation = computation

