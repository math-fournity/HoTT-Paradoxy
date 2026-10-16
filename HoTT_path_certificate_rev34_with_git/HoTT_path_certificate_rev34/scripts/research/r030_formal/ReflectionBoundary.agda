{-# OPTIONS --safe --without-K #-}
module ReflectionBoundary where

open import Agda.Primitive using (Level)

data Empty : Set where

data Bool : Set where
  false true : Bool

not : Bool → Bool
not false = true
not true = false

infix 4 _≡_
data _≡_ {ℓ : Level} {A : Set ℓ} (x : A) : A → Set ℓ where
  refl : x ≡ x

sym : {ℓ : Level} {A : Set ℓ} {x y : A} → x ≡ y → y ≡ x
sym refl = refl

trans : {ℓ : Level} {A : Set ℓ} {x y z : A} → x ≡ y → y ≡ z → x ≡ z
trans refl q = q

no-negation-fixed-point : (b : Bool) → b ≡ not b → Empty
no-negation-fixed-point false ()
no-negation-fixed-point true ()

-- Only ONE self-input equation is required, not all-functions surjectivity.
no-self-certificate : {ℓ : Level} {C : Set ℓ}
  (E : C → C → Bool) (c : C) → E c c ≡ not (E c c) → Empty
no-self-certificate E c = no-negation-fixed-point (E c c)

-- The new-stage diagonal d has no extensionally faithful old-stage code.
no-old-representative : {ℓ : Level} {C : Set ℓ}
  (E : C → C → Bool) (d : C → Bool)
  (diag : (x : C) → d x ≡ not (E x x))
  (c : C) → ((x : C) → E c x ≡ d x) → Empty
no-old-representative E d diag c correct =
  no-self-certificate E c (trans (correct c) (diag c))

-- Any purported compilation back to the old language supplies a forbidden code.
no-faithful-back-translation : {ℓ ℓ′ : Level} {C : Set ℓ} {D : Set ℓ′}
  (E : C → C → Bool) (F : D → C → Bool) (dcode : D)
  (diag : (x : C) → F dcode x ≡ not (E x x))
  (back : D → C) → ((z : D) (x : C) → E (back z) x ≡ F z x) → Empty
no-faithful-back-translation E F dcode diag back correct =
  no-old-representative E (F dcode) diag (back dcode) (correct dcode)

data Answer : Set where
  unknown : Answer
  known : Bool → Answer

flip : Answer → Answer
flip unknown = unknown
flip (known b) = known (not b)

-- UNKNOWN is a result status, not a proof of program divergence.
forced-unknown : (r : Answer) → r ≡ flip r → r ≡ unknown
forced-unknown unknown h = refl
forced-unknown (known false) ()
forced-unknown (known true) ()
