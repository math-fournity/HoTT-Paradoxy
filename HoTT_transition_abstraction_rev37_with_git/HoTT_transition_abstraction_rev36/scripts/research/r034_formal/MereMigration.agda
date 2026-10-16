{-# OPTIONS --safe --without-K #-}
module MereMigration where

-- Parameterized HoTT-style identity argument. NOT compiled in this round.
-- The parameters are explicit assumptions, not postulates or claimed
-- implementations of univalence / propositional truncation.
open import Agda.Primitive using (Level; _⊔_; lsuc; lzero)

infix 4 _≡_
infixr 5 _∙_

data _≡_ {l : Level} {A : Set l} (x : A) : A → Set l where
  refl : x ≡ x

record Σ {a b : Level} (A : Set a) (B : A → Set b) : Set (a ⊔ b) where
  constructor _,_
  field
    fst : A
    snd : B fst
open Σ public

data ⊥ : Set where

data Bool : Set where
  false true : Bool

not : Bool → Bool
not false = true
not true = false

not-fixed : (b : Bool) → not b ≡ b → ⊥
not-fixed false ()
not-fixed true ()

sym : {l : Level} {A : Set l} {x y : A} → x ≡ y → y ≡ x
sym refl = refl

_∙_ : {l : Level} {A : Set l} {x y z : A} → x ≡ y → y ≡ z → x ≡ z
refl ∙ q = q

ap : {a b : Level} {A : Set a} {B : Set b}
     (f : A → B) {x y : A} → x ≡ y → f x ≡ f y
ap f refl = refl

transport : {a b : Level} {A : Set a} (B : A → Set b)
            {x y : A} → x ≡ y → B x → B y
transport B refl b = b

apd : {a b : Level} {A : Set a} {B : A → Set b}
      (f : (x : A) → B x) {x y : A} (p : x ≡ y) →
      transport B p (f x) ≡ f y
apd f refl = refl

pair-path : {a b : Level} {A : Set a} {B : A → Set b}
            {x y : A} {u : B x} {v : B y} →
            (p : x ≡ y) → transport B p u ≡ v →
            (x , u) ≡ (y , v)
pair-path refl refl = refl

pair-path-fst : {a b : Level} {A : Set a} {B : A → Set b}
                {x y : A} {u : B x} {v : B y}
                (p : x ≡ y) (q : transport B p u ≡ v) →
                ap fst (pair-path p q) ≡ p
pair-path-fst refl refl = refl

transport-ap : {a b c : Level} {A : Set a} {D : Set b}
               (f : A → D) (B : D → Set c)
               {x y : A} (p : x ≡ y) (u : B (f x)) →
               transport (λ z → B (f z)) p u ≡ transport B (ap f p) u
transport-ap f B refl u = refl

module NoMereMigration
  (Tr : Set₁ → Set₁)
  (inc : {A : Set₁} → A → Tr A)
  (squash : {A : Set₁} → (u v : Tr A) → u ≡ v)
  (flipPath : Bool ≡ Bool)
  (flipβ : (b : Bool) → transport (λ X → X) flipPath b ≡ not b)
  where

  H : Set → Set₁
  H Y = Tr (Bool ≡ Y)

  Component : Set₁
  Component = Σ Set H

  Family : Component → Set
  Family z = fst z

  h₀ : H Bool
  h₀ = inc refl

  z₀ : Component
  z₀ = Bool , h₀

  second-path : transport H flipPath h₀ ≡ h₀
  second-path = squash (transport H flipPath h₀) h₀

  loop : z₀ ≡ z₀
  loop = pair-path flipPath second-path

  loop-fst : ap fst loop ≡ flipPath
  loop-fst = pair-path-fst flipPath second-path

  loop-action : (b : Bool) → transport Family loop b ≡ not b
  loop-action b =
    transport-ap fst (λ X → X) loop b ∙
    (ap (λ p → transport (λ X → X) p b) loop-fst ∙ flipβ b)

  no-section : ((z : Component) → Family z) → ⊥
  no-section s =
    not-fixed (s z₀) (sym (loop-action (s z₀)) ∙ apd s loop)

  no-selector : ((Y : Set) → H Y → Y) → ⊥
  no-selector choose = no-section (λ z → choose (fst z) (snd z))

  no-migrator : ((X Y : Set) → Tr (X ≡ Y) → X → Y) → ⊥
  no-migrator migrate = no-selector (λ Y h → migrate Bool Y h false)

  -- A fixed pair is a genuinely different type: this positive control exists.
  fixed-pair-id : Tr (Bool ≡ Bool) → Bool → Bool
  fixed-pair-id h b = b

  -- Keeping a real path preserves a constructive migration operation.
  path-migrator : (X Y : Set) → X ≡ Y → X → Y
  path-migrator X Y p b = transport (λ Z → Z) p b
