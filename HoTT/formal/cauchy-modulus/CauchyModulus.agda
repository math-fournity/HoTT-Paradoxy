{-# OPTIONS --safe --cubical --guardedness #-}

-- N9: minimal native Cubical Cauchy-modulus boundary.  A quotient that keeps
-- the eventual value (the limit) forgets the given modulus carried by the
-- representation; no function out of the quotient recovers that modulus.
-- Refining the identity criterion to include the modulus gives a positive
-- control where the modulus is recoverable.
module CauchyModulus where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Data.Nat
open import Cubical.Data.Sigma
open import Cubical.Data.Empty
open import Cubical.Data.Unit
open import Cubical.Data.Bool
open import Cubical.HITs.SetQuotients renaming (rec to SQ-rec)

¬_ : ∀ {ℓ} → Type ℓ → Type ℓ
¬ A = A → ⊥

IsZero : ℕ → Type
IsZero zero = Unit
IsZero (suc _) = ⊥

zero≠suc : ∀ n → ¬ (zero ≡ suc n)
zero≠suc n p = subst IsZero p tt

le : ℕ → ℕ → Type
le zero n = Unit
le (suc m) zero = ⊥
le (suc m) (suc n) = le m n

------------------------------------------------------------------------
-- Cauchy representations: a sequence plus a given modulus of constancy.

Seq : Type
Seq = ℕ → Bool

EventuallyConst : Seq → Type
EventuallyConst s = Σ[ N ∈ ℕ ] (∀ n → le N n → s n ≡ s N)

Cauchy : Type
Cauchy = Σ[ s ∈ Seq ] EventuallyConst s

seq : Cauchy → Seq
seq c = fst c

mod : Cauchy → ℕ
mod c = fst (snd c)

lim : Cauchy → Bool
lim c = seq c (mod c)

constTrue : Seq
constTrue _ = true

const-h0 : ∀ n → le 0 n → constTrue n ≡ constTrue 0
const-h0 n _ = refl

const-h1 : ∀ n → le 1 n → constTrue n ≡ constTrue 1
const-h1 n _ = refl

c0 : Cauchy
c0 = constTrue , 0 , const-h0

c1 : Cauchy
c1 = constTrue , 1 , const-h1

------------------------------------------------------------------------
-- Quotient by equality of the limit; the limit descends, the modulus does not.

_≈_ : Cauchy → Cauchy → Type
c ≈ d = lim c ≡ lim d

Q : Type
Q = Cauchy / _≈_

C-129-limit : Q → Bool
C-129-limit = SQ-rec isSetBool lim (λ c d p → p)

C-130-related : c0 ≈ c1
C-130-related = refl

C-130-moduli-differ : ¬ (mod c0 ≡ mod c1)
C-130-moduli-differ = zero≠suc 0

NoModulusRecovery : Type
NoModulusRecovery = Σ[ f ∈ (Q → ℕ) ] (∀ c → f [ c ] ≡ mod c)

C-131-no-modulus-recovery : ¬ NoModulusRecovery
C-131-no-modulus-recovery (f , hf) =
  zero≠suc 0 (sym (hf c0) ∙ cong f (eq/ c0 c1 C-130-related) ∙ hf c1)

------------------------------------------------------------------------
-- Refined identity criterion: include the modulus in the relation.

_≈'_ : Cauchy → Cauchy → Type
c ≈' d = (mod c ≡ mod d) × (lim c ≡ lim d)

Q' : Type
Q' = Cauchy / _≈'_

C-132-modulus-refined : Q' → ℕ
C-132-modulus-refined = SQ-rec isSetℕ mod (λ c d p → fst p)

C-133-refined-not-related : ¬ (c0 ≈' c1)
C-133-refined-not-related p = zero≠suc 0 (fst p)
