{-# OPTIONS --safe --cubical --guardedness #-}
module LocalCoherence where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool
open import Cubical.Core.Glue
open import Cubical.HITs.S1.Base
import Cubical.HITs.S1.Properties as Circle

compatibleFaces : (i j : I) → Partial (i ∨ j) Bool
compatibleFaces i j = λ { (i = i1) → true ; (j = i1) → true }

fullFaceConsumer : Partial i1 Bool → Bool
fullFaceConsumer u = u 1=1

cornerValue : fullFaceConsumer (compatibleFaces i1 i1) ≡ true
cornerValue = refl

G : Type
G = Glue Bool {φ = i1} (λ _ → Bool , notEquiv)

glued : G
glued = glue {A = Bool} {φ = i1} {T = λ _ → Bool} {e = λ _ → notEquiv}
  (λ _ → true) false

glueConsumer : unglue {A = Bool} i1 {T = λ _ → Bool} {e = λ _ → notEquiv} glued ≡ false
glueConsumer = refl

circleConsumer : S¹ → Bool
circleConsumer = Circle.rec true refl

circleLoopCoherence : cong circleConsumer loop ≡ refl
circleLoopCoherence = refl

data Joined : Type where
  left right : Joined
  join : left ≡ right

joinedConsumer : Joined → Bool
joinedConsumer left = true
joinedConsumer right = true
joinedConsumer (join i) = true
