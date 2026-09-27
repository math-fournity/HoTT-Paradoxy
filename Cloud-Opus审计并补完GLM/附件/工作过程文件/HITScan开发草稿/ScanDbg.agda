{-# OPTIONS --safe --cubical --guardedness #-}
module ScanDbg where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool
open import Cubical.HITs.PropositionalTruncation
open import Agda.Builtin.List
open import Agda.Builtin.Unit
open import Agda.Builtin.Reflection
open import HITScan

u : ∥ Bool ∥₁
u = ∣ true ∣₁

r : ⊤
r = reportClosure u

macro
  showDef : Name → Term → TC ⊤
  showDef n hole = bindTC (getDefinition n) λ d → bindTC (withNormalisation true (getType (quote squash₁))) λ t → bindTC (quoteTC d) λ qd → bindTC (quoteTC t) λ qt → typeError (strErr "DEF: " ∷ termErr qd ∷ strErr "  SQUASH TYPE: " ∷ termErr qt ∷ [])

x : ⊤
x = showDef ∥_∥₁
