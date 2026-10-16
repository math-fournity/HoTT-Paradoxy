{-# OPTIONS --safe --cubical --guardedness #-}
module ScanTest where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool
open import Cubical.HITs.PropositionalTruncation
open import Agda.Builtin.List
open import Agda.Builtin.Reflection using (Name)
open import HITScan

t1 : Bool → Bool
t1 b = not b

s1 : sizeOf t1 ≡ sizeOf t1
s1 = refl

h1 : Path (List Name) (hitsOf t1) []
h1 = refl

u : ∥ Bool ∥₁
u = ∣ true ∣₁

h2 : Path (List Name) (hitsOf u) []
h2 = refl
