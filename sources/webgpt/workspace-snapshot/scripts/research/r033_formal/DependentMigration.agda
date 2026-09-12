{-# OPTIONS --safe --without-K #-}
module DependentMigration where

-- Shared intensional type-theory proofs; NOT compiled in this session.
-- No postulates for circles, univalence, truncation, or funext are assumed here.
open import Agda.Primitive using (Level; _⊔_)
open import Agda.Builtin.Equality using (_≡_; refl)
open import Agda.Builtin.Sigma using (Σ; _,_; fst; snd)

data Empty : Set where

sym : ∀ {a} {A : Set a} {x y : A} → x ≡ y → y ≡ x
sym refl = refl

trans : ∀ {a} {A : Set a} {x y z : A} → x ≡ y → y ≡ z → x ≡ z
trans refl q = q

ap : ∀ {a b} {A : Set a} {B : Set b} (f : A → B) {x y : A} → x ≡ y → f x ≡ f y
ap f refl = refl

tr : ∀ {a b} {A : Set a} (B : A → Set b) {x y : A} → x ≡ y → B x → B y
tr B refl u = u

pairPath : ∀ {a b} {A : Set a} {B : A → Set b}
  {x x′ : A} {y : B x} {y′ : B x′} →
  (p : x ≡ x′) → tr B p y ≡ y′ →
  ((x , y) ≡ (x′ , y′))
pairPath refl refl = refl

liftPath : ∀ {a b} {A : Set a} {B : A → Set b}
  {x x′ : A} (p : x ≡ x′) (y : B x) →
  (x , y) ≡ (x′ , tr B p y)
liftPath p y = pairPath p refl

moveThird : ∀ {a b c} {A : Set a} {B : A → Set b}
  (D : Σ A B → Set c) {x x′ : A} {y : B x} {y′ : B x′}
  (p : x ≡ x′) (q : tr B p y ≡ y′) → D (x , y) → D (x′ , y′)
moveThird D p q z = tr D (pairPath p q) z

FibreMap : ∀ {a b c d} {A : Set a} {A′ : Set b} →
  (A → A′) → (A → Set c) → (A′ → Set d) → Set (a ⊔ c ⊔ d)
FibreMap f B C = ∀ x → B x → C (f x)

totalFromFibre : ∀ {a b c d} {A : Set a} {A′ : Set b}
  {f : A → A′} {B : A → Set c} {C : A′ → Set d} →
  FibreMap f B C → Σ A B → Σ A′ C
totalFromFibre {f = f} φ (x , y) = f x , φ x y

fibreFromOver : ∀ {a b c d} {A : Set a} {A′ : Set b}
  {f : A → A′} {B : A → Set c} {C : A′ → Set d}
  (F : Σ A B → Σ A′ C) →
  (∀ z → fst (F z) ≡ f (fst z)) → FibreMap f B C
fibreFromOver {C = C} F h x y = tr C (h (x , y)) (snd (F (x , y)))

naturality : ∀ {a b c d} {A : Set a} {A′ : Set b}
  (f : A → A′) (B : A → Set c) (C : A′ → Set d)
  (φ : FibreMap f B C) {x x′ : A} (p : x ≡ x′) (y : B x) →
  tr C (ap f p) (φ x y) ≡ φ x′ (tr B p y)
naturality f B C φ refl y = refl

sectionNaturality : ∀ {a b} {A : Set a} (B : A → Set b)
  (s : ∀ x → B x) {x y : A} (p : x ≡ y) → tr B p (s x) ≡ s y
sectionNaturality B s refl = refl

noSectionAtNonfixedLoop : ∀ {a b} {A : Set a} (B : A → Set b)
  (x : A) (p : x ≡ x) →
  (∀ y → tr B p y ≡ y → Empty) → (∀ z → B z) → Empty
noSectionAtNonfixedLoop B x p nofix s = nofix (s x) (sectionNaturality B s p)

-- If two paths have been merged by an information-erasing map, no single
-- decoder can preserve their two different actions on the same input.
noFaithfulPathErasure : ∀ {a b i} {A : Set a} (B : A → Set b)
  {x y : A} (u : B x) (p q : x ≡ y) {I : Set i}
  (erase : (x ≡ y) → I) (merged : erase p ≡ erase q)
  (different : tr B p u ≡ tr B q u → Empty)
  (decode : I → B y) →
  decode (erase p) ≡ tr B p u → decode (erase q) ≡ tr B q u → Empty
noFaithfulPathErasure B u p q erase merged different decode βp βq =
  different (trans (sym βp) (trans (ap decode merged) βq))

-- A sufficient local condition, not required for all data families:
-- proposition-valued fibres make all parallel transports pointwise equal.
isProp : ∀ {a} → Set a → Set a
isProp X = ∀ x y → x ≡ y

propFibresEraseParallel : ∀ {a b} {A : Set a} (B : A → Set b) →
  (∀ x → isProp (B x)) → ∀ {x y} (p q : x ≡ y) (u : B x) →
  tr B p u ≡ tr B q u
propFibresEraseParallel B props {y = y} p q u = props y (tr B p u) (tr B q u)
