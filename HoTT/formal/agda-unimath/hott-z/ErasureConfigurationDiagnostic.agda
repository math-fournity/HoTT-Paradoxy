{-# OPTIONS --without-K --exact-split #-}
module hott-z.ErasureConfigurationDiagnostic where

-- Diagnostic of an EXTRA Agda primitive together with library univalence.
-- This is not a derivation in the ordinary HoTT rules alone.
open import foundation.universe-levels
open import foundation.dependent-pair-types
open import foundation-core.identity-types
open import foundation.action-on-identifications-functions
open import foundation-core.equivalences
open import foundation-core.booleans
open import foundation-core.empty-types
open import foundation.univalence
open import reflection.erasing-equality

eraseRetract : {l : Level} {A : UU l} {x y : A}
  (p : x ＝ y) → primEraseEquality p ＝ p
eraseRetract refl = refl

-- The primitive reduces ANY loop to refl before conversion checking.
loopRefl : {l : Level} {A : UU l} {x : A} (p : x ＝ x) → p ＝ refl
loopRefl p = inv (eraseRetract p)

swap : bool → bool
swap true = false
swap false = true

swapTwice : (b : bool) → swap (swap b) ＝ b
swapTwice true = refl
swapTwice false = refl

swapEquiv : bool ≃ bool
swapEquiv = swap , is-equiv-is-invertible swap swapTwice swapTwice

swapPath : bool ＝ bool
swapPath = eq-equiv swapEquiv

-- Library univalence sends the swap path to the swapping equivalence.
swapAction : map-equiv (equiv-eq swapPath) true ＝ false
swapAction = ap (λ e → map-equiv e true) (is-section-eq-equiv swapEquiv)

collapsedAction : map-equiv (equiv-eq swapPath) true ＝ true
collapsedAction = ap (λ p → map-equiv (equiv-eq p) true) (loopRefl swapPath)

configurationEmpty : empty
configurationEmpty = neq-true-false-bool (inv collapsedAction ∙ swapAction)
