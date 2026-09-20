{-# OPTIONS --safe --cubical --guardedness #-}
module SC04 where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.GroupoidLaws
open import Cubical.Foundations.HLevels
open import Cubical.Foundations.Path
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Function
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Transport
open import Cubical.Foundations.Univalence

open import Cubical.Data.Nat
  hiding (_+_ ; _·_ ; +-assoc ; +-comm)
open import Cubical.Data.Int hiding (_·_)

import Cubical.HITs.S1.Base as Upstream
open Upstream using (S¹; base; loop)

-- ΩS¹ ≡ ℤ
helix : S¹ → Type₀
helix base     = ℤ
helix (loop i) = sucPathℤ i

ΩS¹ : Type₀
ΩS¹ = base ≡ base

encode : ∀ x → base ≡ x → helix x
encode x p = subst helix p (pos zero)

winding : ΩS¹ → ℤ
winding = encode base

intLoop : ℤ → ΩS¹
intLoop (pos zero)       = refl
intLoop (pos (suc n))    = intLoop (pos n) ∙ loop
intLoop (negsuc zero)    = sym loop
intLoop (negsuc (suc n)) = intLoop (negsuc n) ∙ sym loop

decodeSquare : (n : ℤ) → PathP (λ i → base ≡ loop i) (intLoop (predℤ n)) (intLoop n)
decodeSquare (pos zero) i j    = loop (i ∨ ~ j)
decodeSquare (pos (suc n)) i j = hfill (λ k → λ { (j = i0) → base
                                                ; (j = i1) → loop k } )
                                       (inS (intLoop (pos n) j)) i
decodeSquare (negsuc n) i j = hfill (λ k → λ { (j = i0) → base
                                             ; (j = i1) → loop (~ k) })
                                    (inS (intLoop (negsuc n) j)) (~ i)

decode : (x : S¹) → helix x → base ≡ x
decode base         = intLoop
decode (loop i) y j =
  let n : ℤ
      n = unglue (i ∨ ~ i) y
  in hcomp (λ k → λ { (i = i0) → intLoop (predSuc y k) j
                    ; (i = i1) → intLoop y j
                    ; (j = i0) → base
                    ; (j = i1) → loop i })
           (decodeSquare n i j)

decodeEncode : (x : S¹) (p : base ≡ x) → decode x (encode x p) ≡ p
decodeEncode x p = refl

isSetΩS¹ : isSet ΩS¹
isSetΩS¹ p q r s j i =
  hcomp (λ k → λ { (i = i0) → decodeEncode base p k
                 ; (i = i1) → decodeEncode base q k
                 ; (j = i0) → decodeEncode base (r i) k
                 ; (j = i1) → decodeEncode base (s i) k })
        (decode base (isSetℤ (winding p) (winding q) (cong winding r) (cong winding s) j i))

-- This proof does not rely on rewriting hcomp with empty systems in
-- ℤ as ghcomp has been implemented!
windingℤLoop : (n : ℤ) → winding (intLoop n) ≡ n
windingℤLoop (pos zero)       = refl
windingℤLoop (pos (suc n))    = cong sucℤ (windingℤLoop (pos n))
windingℤLoop (negsuc zero)    = refl
windingℤLoop (negsuc (suc n)) = cong predℤ (windingℤLoop (negsuc n))

ΩS¹Isoℤ : Iso ΩS¹ ℤ
Iso.fun ΩS¹Isoℤ      = winding
Iso.inv ΩS¹Isoℤ      = intLoop
Iso.rightInv ΩS¹Isoℤ = windingℤLoop
Iso.leftInv ΩS¹Isoℤ  = decodeEncode base

ΩS¹≡ℤ : ΩS¹ ≡ ℤ
ΩS¹≡ℤ = isoToPath ΩS¹Isoℤ

-- intLoop and winding are group homomorphisms
private
  intLoop-sucℤ : (z : ℤ) → intLoop (sucℤ z) ≡ intLoop z ∙ loop
  intLoop-sucℤ (pos n)          = refl
  intLoop-sucℤ (negsuc zero)    = sym (lCancel loop)
  intLoop-sucℤ (negsuc (suc n)) =
      rUnit (intLoop (negsuc n))
    ∙ (λ i → intLoop (negsuc n) ∙ lCancel loop (~ i))
    ∙ assoc (intLoop (negsuc n)) (sym loop) loop

  intLoop-predℤ : (z : ℤ) → intLoop (predℤ z) ≡ intLoop z ∙ sym loop
  intLoop-predℤ (pos zero)    = lUnit (sym loop)
  intLoop-predℤ (pos (suc n)) =
      rUnit (intLoop (pos n))
    ∙ (λ i → intLoop (pos n) ∙ (rCancel loop (~ i)))
    ∙ assoc (intLoop (pos n)) loop (sym loop)
  intLoop-predℤ (negsuc n)    = refl

intLoop-hom : (a b : ℤ) → (intLoop a) ∙ (intLoop b) ≡ intLoop (a + b)
intLoop-hom a (pos zero)       = sym (rUnit (intLoop a))
intLoop-hom a (pos (suc n))    =
    assoc (intLoop a) (intLoop (pos n)) loop
  ∙ (λ i → (intLoop-hom a (pos n) i) ∙ loop)
  ∙ sym (intLoop-sucℤ (a + pos n))
intLoop-hom a (negsuc zero)    = sym (intLoop-predℤ a)
intLoop-hom a (negsuc (suc n)) =
    assoc (intLoop a) (intLoop (negsuc n)) (sym loop)
  ∙ (λ i → (intLoop-hom a (negsuc n) i) ∙ (sym loop))
  ∙ sym (intLoop-predℤ (a + negsuc n))

winding-hom : (a b : ΩS¹) → winding (a ∙ b) ≡ (winding a) + (winding b)
winding-hom a b i =
  hcomp (λ t → λ { (i = i0) → winding (decodeEncode base a t ∙ decodeEncode base b t)
                 ; (i = i1) → windingℤLoop (winding a + winding b) t })
        (winding (intLoop-hom (winding a) (winding b) i))


-- The copied consumer uses the actual upstream circle, not a new local HIT.
-- These bridges identify its data with the corresponding upstream functions.
helixAgreement : helix ≡ Upstream.helix
helixAgreement t base = ℤ
helixAgreement t (loop i) = sucPathℤ i

encodeAgreement : (x : S¹) (p : base ≡ x) →
  PathP (λ t → helixAgreement t x) (encode x p) (Upstream.encode x p)
encodeAgreement x p t = subst (helixAgreement t) p (pos zero)

windingAgreement : (p : ΩS¹) → winding p ≡ Upstream.winding p
windingAgreement p = encodeAgreement base p

intLoopAgreement : (n : ℤ) → intLoop n ≡ Upstream.intLoop n
intLoopAgreement (pos zero) = refl
intLoopAgreement (pos (suc n)) = cong (_∙ loop) (intLoopAgreement (pos n))
intLoopAgreement (negsuc zero) = refl
intLoopAgreement (negsuc (suc n)) = cong (_∙ sym loop) (intLoopAgreement (negsuc n))

roundTripLoop : (p : Upstream.ΩS¹) → intLoop (winding p) ≡ p
roundTripLoop = decodeEncode base

roundTripInteger : (n : ℤ) → winding (intLoop n) ≡ n
roundTripInteger = windingℤLoop

composedObservation : (p q : Upstream.ΩS¹) →
  winding (p ∙ q) ≡ winding p + winding q
composedObservation = winding-hom
