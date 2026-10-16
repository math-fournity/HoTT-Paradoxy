{-# OPTIONS --safe --cubical --guardedness #-}
module UpstreamLoopHoldout where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty
import Cubical.Data.Nat as N
import Cubical.Data.Int as Z
open import Cubical.HITs.S1.Base

-- A source holdout using the library's integer winding consumer.
-- This is not a blind experiment or an independent reviewer.
oneLoop : base ≡ base
oneLoop = intLoop (Z.pos 1)

oneWinding : winding oneLoop ≡ Z.pos 1
oneWinding = windingℤLoop (Z.pos 1)

zeroWinding : winding refl ≡ Z.pos 0
zeroWinding = refl

nontrivialLoop : oneLoop ≡ refl → ⊥
nontrivialLoop p = N.snotz
  (Z.injPos (sym oneWinding ∙ cong winding p ∙ zeroWinding))

notAllProofsEqual : ((p q : base ≡ base) → p ≡ q) → ⊥
notAllProofsEqual collapse = nontrivialLoop (collapse oneLoop refl)
