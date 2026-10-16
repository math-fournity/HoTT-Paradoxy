{-# OPTIONS --safe --without-K --exact-split #-}
module EncodedPair where

-- Native intensional identity fragment, not Cubical Path or record eta.
-- The supplied extensionality operation and its identity law are explicit
-- hypotheses. This file does not establish univalence or their consistency.
-- Explicit local constructors make the mathematical dependency closure visible.
-- No record eta or library choice of identity is imported.
data Bool : Set where
  false true : Bool

data Nat : Set where
  zero : Nat
  suc : Nat → Nat

infix 4 _≡_
data _≡_ {A : Set} (x : A) : A → Set where
  refl : x ≡ x

cong : {A B : Set} (f : A → B) {x y : A} → x ≡ y → f x ≡ f y
cong f refl = refl

_∙_ : {A : Set} {x y z : A} → x ≡ y → y ≡ z → x ≡ z
refl ∙ q = q

subst : {A : Set} (P : A → Set) {x y : A} → x ≡ y → P x → P y
subst P refl a = a

Encoded = Bool → Nat

pair : Nat → Nat → Encoded
pair a b false = a
pair a b true = b

left right : Encoded → Nat
left p = p false
right p = p true

rebuild-point : (p : Encoded) (x : Bool) → pair (left p) (right p) x ≡ p x
rebuild-point p false = refl
rebuild-point p true = refl

-- Normal control: reading the first component needs no extensionality.
projection-β : (a b : Nat) → left (pair a b) ≡ a
projection-β a b = refl

data PrimitivePair : Set where
  pack : Nat → Nat → PrimitivePair

primitive-elim : (C : PrimitivePair → Set)
  → ((a b : Nat) → C (pack a b)) → (p : PrimitivePair) → C p
primitive-elim C d (pack a b) = d a b

primitive-β : (C : PrimitivePair → Set)
  (d : (a b : Nat) → C (pack a b)) (a b : Nat)
  → primitive-elim C d (pack a b) ≡ d a b
primitive-β C d a b = refl

module WithExt
  (ext : {B : Bool → Set} {f g : (x : Bool) → B x}
       → ((x : Bool) → f x ≡ g x) → f ≡ g)
  (ext-id : {B : Bool → Set} (f : (x : Bool) → B x)
          → ext (λ x → refl {x = f x}) ≡ refl {x = f}) where

  η : (p : Encoded) → pair (left p) (right p) ≡ p
  η p = ext (rebuild-point p)

  canonical-point : (a b : Nat)
    → rebuild-point (pair a b) ≡ (λ x → refl {x = pair a b x})
  canonical-point a b = ext pointwise
    where
    pointwise : (x : Bool) → rebuild-point (pair a b) x ≡ refl
    pointwise false = refl
    pointwise true = refl

  η-canonical : (a b : Nat) → η (pair a b) ≡ refl
  η-canonical a b = cong (λ h → ext h) (canonical-point a b) ∙ ext-id (pair a b)

  encoded-elim : (C : Encoded → Set)
    → ((a b : Nat) → C (pair a b)) → (p : Encoded) → C p
  encoded-elim C d p = subst C (η p) (d (left p) (right p))

  -- The dependent beta law is a term built using the extensionality laws.
  encoded-β : (C : Encoded → Set)
    (d : (a b : Nat) → C (pair a b)) (a b : Nat)
    → encoded-elim C d (pair a b) ≡ d a b
  encoded-β C d a b = cong (λ q → subst C q (d a b)) (η-canonical a b)

  delivered-zero : encoded-elim (λ _ → Nat) (λ a b → a) (pair zero (suc zero)) ≡ zero
  delivered-zero = encoded-β (λ _ → Nat) (λ a b → a) zero (suc zero)
