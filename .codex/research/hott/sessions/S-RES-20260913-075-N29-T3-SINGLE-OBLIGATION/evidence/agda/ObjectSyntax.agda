{-# OPTIONS --safe #-}

-- ERCF-3 prerequisite task T2 (encoding-route experiment, route (a)).
--
-- Question: can the syntactic layer required by P2/P3 -- object-language
-- syntax, capture-free substitution, and one proof-predicate interface -- be
-- built in the SAME layer without adding a level (QIIT or 2LTT)?
--
-- This file uses only Agda builtins: no cubical features, no library imports.
-- If it type-checks, route (a) suffices for the syntactic layer a fortiori.
-- Goedel coding with decodability/injectivity, representability of the proof
-- predicate by a formula, and the diagonal lemma are T3 obligations and are
-- deliberately NOT formalised here.
module ObjectSyntax where

open import Agda.Builtin.Nat
open import Agda.Builtin.Equality
open import Agda.Builtin.Bool

------------------------------------------------------------------------
-- Local equality helpers (kept self-contained).

cong₂ : ∀ {A B C : Set} (f : A → B → C) {x₁ x₂ : A} {y₁ y₂ : B}
      → x₁ ≡ x₂ → y₁ ≡ y₂ → f x₁ y₁ ≡ f x₂ y₂
cong₂ f refl refl = refl

------------------------------------------------------------------------
-- 1. Object-language terms and formulas (named variables).

data Tm : Set where
  var : Nat → Tm
  num : Nat → Tm
  _+t_ : Tm → Tm → Tm

data Fml : Set where
  _=f_ : Tm → Tm → Fml
  bot : Fml
  _=>f_ : Fml → Fml → Fml
  all : Nat → Fml → Fml

infix 6 _+t_
infix 5 _=f_
infixr 4 _=>f_

------------------------------------------------------------------------
-- 2. Decidable equality on Nat.

_=n_ : Nat → Nat → Bool
zero =n zero = true
zero =n suc _ = false
suc _ =n zero = false
suc m =n suc n = m =n n

=n-refl : ∀ n → n =n n ≡ true
=n-refl zero = refl
=n-refl (suc n) = =n-refl n

if_then_else_ : ∀ {A : Set} → Bool → A → A → A
if_then_else_ true  x y = x
if_then_else_ false x y = y

infix 1 if_then_else_

------------------------------------------------------------------------
-- 3. Substitution of a CLOSED numeral for a variable.  Because the
--    substituted term is closed, capture can never occur; bound occurrences
--    are shadowed by the equality test.

substT : Nat → Nat → Tm → Tm
substT k n (var m) = if n =n m then num k else var m
substT k n (num m) = num m
substT k n (t +t u) = substT k n t +t substT k n u

substF : Nat → Nat → Fml → Fml
substF k n (t =f u) = substT k n t =f substT k n u
substF k n bot = bot
substF k n (φ =>f ψ) = substF k n φ =>f substF k n ψ
substF k n (all m φ) = if n =n m then all m φ else all m (substF k n φ)

------------------------------------------------------------------------
-- 4. Structural lemmas (machine-checked).

substT-num : ∀ k n m → substT k n (num m) ≡ num m
substT-num k n m = refl

substT-var-self : ∀ k n → substT k n (var n) ≡ num k
substT-var-self k n rewrite =n-refl n = refl

substF-bot : ∀ k n → substF k n bot ≡ bot
substF-bot k n = refl

substF-all-same : ∀ k n φ → substF k n (all n φ) ≡ all n φ
substF-all-same k n φ rewrite =n-refl n = refl

-- Substitution at an absent variable is the identity (the case that
-- representability uses for "fresh" variables).
substT-var-absent : ∀ k n m → n =n m ≡ false → substT k n (var m) ≡ var m
substT-var-absent k n m eq rewrite eq = refl

substF-all-absent : ∀ k n m φ → n =n m ≡ false
                  → substF k n (all m φ) ≡ all m (substF k n φ)
substF-all-absent k n m φ eq rewrite eq = refl

substT-num-comm : ∀ k j n m → substT k n (num m) ≡ substT j n (num m)
substT-num-comm k j n m = refl

------------------------------------------------------------------------
-- 5. A minimal proof-predicate interface over the object syntax: a
--    Hilbert-style system with two axiom schemas and modus ponens.

infix 3 ⊢_

data ⊢_ : Fml → Set where
  axK : (φ ψ : Fml) → ⊢ (φ =>f (ψ =>f φ))
  axS : (φ ψ χ : Fml)
      → ⊢ ((φ =>f (ψ =>f χ)) =>f ((φ =>f ψ) =>f (φ =>f χ)))
  mp  : {φ ψ : Fml} → ⊢ (φ =>f ψ) → ⊢ φ → ⊢ ψ

Prov : Fml → Set
Prov φ = ⊢ φ

-- The interface exposes exactly what T3 needs to represent: a decidable
-- proof relation presented as derivability of object formulas.
prov-interface : (φ ψ : Fml) → Prov (φ =>f ψ) → Prov φ → Prov ψ
prov-interface φ ψ p q = mp p q
