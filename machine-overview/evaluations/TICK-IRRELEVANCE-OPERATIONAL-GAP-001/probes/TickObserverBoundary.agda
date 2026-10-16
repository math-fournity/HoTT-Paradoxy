{-# OPTIONS --safe --cubical #-}
module TickObserverBoundary where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Empty.Base using (⊥)

data ExtTick : Type₀ where
  forcing ordinary : ExtTick
  tirr : forcing ≡ ordinary

noOperationalObserver
  : (observe : ExtTick → Bool)
  → observe forcing ≡ true
  → observe ordinary ≡ false
  → ⊥
noOperationalObserver observe forcing-now ordinary-later =
  true≢false (sym forcing-now ∙ cong observe tirr ∙ ordinary-later)

constantObserver : ExtTick → Bool
constantObserver _ = true

constantObserver-forcing : constantObserver forcing ≡ true
constantObserver-forcing = refl

constantObserver-ordinary : constantObserver ordinary ≡ true
constantObserver-ordinary = refl

data OperationalTick : Type₀ where
  forcing ordinary : OperationalTick

isForcing : OperationalTick → Bool
isForcing forcing = true
isForcing ordinary = false

forcing-computes : isForcing forcing ≡ true
forcing-computes = refl

ordinary-stays-delayed : isForcing ordinary ≡ false
ordinary-stays-delayed = refl
