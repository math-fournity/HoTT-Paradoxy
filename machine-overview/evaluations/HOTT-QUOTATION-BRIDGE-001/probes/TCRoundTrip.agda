{-# OPTIONS --safe --cubical-compatible --no-guardedness #-}

-- Agda's quotation and unquotation compose inside the host TC monad.
-- This target deliberately returns TC A rather than A.

module TCRoundTrip where

import Agda.Builtin.Reflection as R

roundTripTC : ∀ {a} {A : Set a} → A → R.TC A
roundTripTC x = R.bindTC (R.quoteTC x) R.unquoteTC

-- `returnTC` can give the same type shape as a cojoin, but its meaning is
-- monadic return of an already available checker computation.  It is not a
-- quotation of a typed proof and supplies no reflection `TC A → A`.
cojoinTCByReturn : ∀ {a} {A : Set a} → R.TC A → R.TC (R.TC A)
cojoinTCByReturn = R.returnTC

