{-# OPTIONS --cubical --safe --guardedness #-}

module SyntheticIncompleteness where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ)
open import Cubical.Data.Bool.Base using (Bool ; false ; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty as Empty
open import Cubical.Data.Sum.Base using (_⊎_ ; inl ; inr)

infix 30 ¬_

¬_ : Type → Type
¬ A = A → Empty.⊥

infixr 25 _×_

_×_ : Type → Type → Type
A × B = Σ[ _ ∈ A ] B

------------------------------------------------------------------------
-- Deterministic step-indexed partial Boolean computations.

data OptionBool : Type where
  none : OptionBool
  some : Bool → OptionBool

optionValue : OptionBool → Bool
optionValue none = false
optionValue (some b) = b

isSome : OptionBool → Bool
isSome none = false
isSome (some b) = true

none≢some : {b : Bool} → ¬ (none ≡ some b)
none≢some eq = false≢true (cong isSome eq)

some-injective : {b₁ b₂ : Bool} → some b₁ ≡ some b₂ → b₁ ≡ b₂
some-injective = cong optionValue

flip : Bool → Bool
flip false = true
flip true = false

mapFlip : OptionBool → OptionBool
mapFlip none = none
mapFlip (some b) = some (flip b)

mapFlip-success : {o : OptionBool} {b : Bool}
                → mapFlip o ≡ some b
                → Σ[ a ∈ Bool ] (o ≡ some a) × (flip a ≡ b)
mapFlip-success {none} eq = Empty.rec (none≢some eq)
mapFlip-success {some a} eq = a , refl , some-injective eq

record PartBool : Type₁ where
  constructor partBool
  field
    core : ℕ → OptionBool
    deterministic : (b₁ b₂ : Bool) (k₁ k₂ : ℕ)
                  → core k₁ ≡ some b₁ → core k₂ ≡ some b₂ → b₁ ≡ b₂

open PartBool public

infix 35 _⇓_

_⇓_ : PartBool → Bool → Type
p ⇓ b = Σ[ k ∈ ℕ ] core p k ≡ some b

runs-deterministic : (p : PartBool) (b₁ b₂ : Bool)
                   → p ⇓ b₁ → p ⇓ b₂ → b₁ ≡ b₂
runs-deterministic p b₁ b₂ (k₁ , run₁) (k₂ , run₂) =
  deterministic p b₁ b₂ k₁ k₂ run₁ run₂

flipPart : PartBool → PartBool
flipPart p = partBool
  (λ k → mapFlip (core p k))
  λ b₁ b₂ k₁ k₂ eq₁ eq₂ →
    let a₁ = fst (mapFlip-success eq₁)
        core₁ = fst (snd (mapFlip-success eq₁))
        flip₁ = snd (snd (mapFlip-success eq₁))
        a₂ = fst (mapFlip-success eq₂)
        core₂ = fst (snd (mapFlip-success eq₂))
        flip₂ = snd (snd (mapFlip-success eq₂))
        same = deterministic p a₁ a₂ k₁ k₂ core₁ core₂
    in sym flip₁ ∙ cong flip same ∙ flip₂

flip-runs-false : {p : PartBool} → p ⇓ true → flipPart p ⇓ false
flip-runs-false (k , run) = k , cong mapFlip run

flip-runs-true : {p : PartBool} → p ⇓ false → flipPart p ⇓ true
flip-runs-true (k , run) = k , cong mapFlip run

Diverges : PartBool → Type
Diverges p = (b : Bool) → ¬ (p ⇓ b)

------------------------------------------------------------------------
-- A synthetic universal enumeration of partial Boolean functions.

infix 20 _↔_

_↔_ : Type → Type → Type
A ↔ B = (A → B) × (B → A)

Universal : (ℕ → ℕ → PartBool) → Type₁
Universal θ =
  (f : ℕ → PartBool) →
  Σ[ c ∈ ℕ ] ((x : ℕ) (b : Bool) → (f x ⇓ b) ↔ (θ c x ⇓ b))

SelfReturns : (ℕ → ℕ → PartBool) → Bool → ℕ → Type
SelfReturns θ b x = θ x x ⇓ b

SeparatesSelfReturns :
  (θ : ℕ → ℕ → PartBool) → (ℕ → PartBool) → Type
SeparatesSelfReturns θ f =
  (b : Bool) (x : ℕ) → SelfReturns θ b x → f x ⇓ b

separator-diverges :
  (θ : ℕ → ℕ → PartBool)
  → Universal θ
  → (f : ℕ → PartBool)
  → SeparatesSelfReturns θ f
  → Σ[ c ∈ ℕ ] Diverges (f c)
separator-diverges θ universal f separates
  with universal (λ x → flipPart (f x))
... | c , sim = c , λ
  { false runFalse →
      let thetaTrue : θ c c ⇓ true
          thetaTrue = fst (sim c true) (flip-runs-true {p = f c} runFalse)

          runTrue : f c ⇓ true
          runTrue = separates true c thetaTrue
      in false≢true (runs-deterministic (f c) false true runFalse runTrue)
  ; true runTrue →
      let thetaFalse : θ c c ⇓ false
          thetaFalse = fst (sim c false) (flip-runs-false {p = f c} runTrue)

          runFalse : f c ⇓ false
          runFalse = separates false c thetaFalse
      in false≢true (runs-deterministic (f c) false true runFalse runTrue)
  }

no-total-separator :
  (θ : ℕ → ℕ → PartBool)
  → Universal θ
  → (f : ℕ → PartBool)
  → SeparatesSelfReturns θ f
  → ¬ ((x : ℕ) → Σ[ b ∈ Bool ] f x ⇓ b)
no-total-separator θ universal f separates total
  with separator-diverges θ universal f separates
... | c , diverges = diverges (fst (total c)) (snd (total c))

------------------------------------------------------------------------
-- Effective formal systems and the abstract incompleteness theorem.

record FormalSystem (S : Type) (neg : S → S) : Type₁ where
  constructor formalSystem
  field
    Derives : S → Type
    classifier : S → PartBool
    proof-runs-true : (s : S) → Derives s → classifier s ⇓ true
    true-runs-proof : (s : S) → classifier s ⇓ true → Derives s
    refutation-runs-false : (s : S) → Derives (neg s) → classifier s ⇓ false
    false-runs-refutation : (s : S) → classifier s ⇓ false → Derives (neg s)

open FormalSystem public

classifier-consistent :
  {S : Type} {neg : S → S} (fs : FormalSystem S neg) (s : S)
  → Derives fs s → Derives fs (neg s) → Empty.⊥
classifier-consistent fs s proof refutation =
  false≢true
    (runs-deterministic (classifier fs s) false true
      (refutation-runs-false fs s refutation)
      (proof-runs-true fs s proof))

Independent :
  {S : Type} {neg : S → S} → FormalSystem S neg → S → Type
Independent {neg = neg} fs s = (¬ Derives fs s) × (¬ Derives fs (neg s))

Complete :
  {S : Type} {neg : S → S} → FormalSystem S neg → Type
Complete {S = S} {neg = neg} fs =
  (s : S) → Derives fs s ⊎ Derives fs (neg s)

StronglySeparates :
  {S : Type} {neg : S → S}
  → FormalSystem S neg
  → (ℕ → Type) → (ℕ → Type) → (ℕ → S) → Type
StronglySeparates {neg = neg} fs P Q r =
  ((x : ℕ) → P x → Derives fs (r x))
  × ((x : ℕ) → Q x → Derives fs (neg (r x)))

synthetic-incompleteness :
  (θ : ℕ → ℕ → PartBool)
  → Universal θ
  → {S : Type} {neg : S → S}
  → (fs : FormalSystem S neg)
  → (r : ℕ → S)
  → StronglySeparates fs (SelfReturns θ true) (SelfReturns θ false) r
  → Σ[ c ∈ ℕ ] Independent fs (r c)
synthetic-incompleteness θ universal fs r separates
  with separator-diverges θ universal (λ x → classifier fs (r x)) classifier-separates
  where
  classifier-separates :
    SeparatesSelfReturns θ (λ x → classifier fs (r x))
  classifier-separates false x returnsFalse =
    refutation-runs-false fs (r x) (snd separates x returnsFalse)
  classifier-separates true x returnsTrue =
    proof-runs-true fs (r x) (fst separates x returnsTrue)
... | c , diverges =
  c ,
  ( (λ proof → diverges true (proof-runs-true fs (r c) proof))
  , (λ refutation →
      diverges false (refutation-runs-false fs (r c) refutation))
  )

independent-refutes-complete :
  {S : Type} {neg : S → S}
  → (fs : FormalSystem S neg)
  → (s : S)
  → Independent fs s
  → ¬ Complete fs
independent-refutes-complete fs s independent complete with complete s
... | inl proof = fst independent proof
... | inr refutation = snd independent refutation

synthetic-not-complete :
  (θ : ℕ → ℕ → PartBool)
  → Universal θ
  → {S : Type} {neg : S → S}
  → (fs : FormalSystem S neg)
  → (r : ℕ → S)
  → StronglySeparates fs (SelfReturns θ true) (SelfReturns θ false) r
  → ¬ Complete fs
synthetic-not-complete θ universal fs r separates complete
  with synthetic-incompleteness θ universal fs r separates
... | c , independent = independent-refutes-complete fs (r c) independent complete

Extends :
  {S : Type} {neg : S → S}
  → FormalSystem S neg → FormalSystem S neg → Type
Extends {S = S} base extension =
  (s : S) → Derives base s → Derives extension s

strong-separation-extends :
  {S : Type} {neg : S → S}
  → (base extension : FormalSystem S neg)
  → Extends base extension
  → (P Q : ℕ → Type)
  → (r : ℕ → S)
  → StronglySeparates base P Q r
  → StronglySeparates extension P Q r
strong-separation-extends base extension extends P Q r separates =
  ( (λ x px → extends (r x) (fst separates x px))
  , (λ x qx → extends _ (snd separates x qx))
  )

synthetic-essential-incompleteness :
  (θ : ℕ → ℕ → PartBool)
  → Universal θ
  → {S : Type} {neg : S → S}
  → (base extension : FormalSystem S neg)
  → Extends base extension
  → (r : ℕ → S)
  → StronglySeparates base (SelfReturns θ true) (SelfReturns θ false) r
  → Σ[ c ∈ ℕ ] Independent extension (r c)
synthetic-essential-incompleteness θ universal base extension extends r separates =
  synthetic-incompleteness θ universal extension r
    (strong-separation-extends base extension extends
      (SelfReturns θ true) (SelfReturns θ false) r separates)
