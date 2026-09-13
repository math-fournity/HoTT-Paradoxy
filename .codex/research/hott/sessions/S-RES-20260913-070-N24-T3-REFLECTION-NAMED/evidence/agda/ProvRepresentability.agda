module ProvRepresentability where

open import Agda.Builtin.Nat
open import Agda.Builtin.Equality
open import ObjectSyntax
open import DiagonalCore

-- T3 pulse (bounded, second stage): the provability-side representability
-- fragment.  The object language is extended with a single unary predicate
-- constant P; the T3 obligation is that every object derivation can be
-- reflected into the object-level predicate on the quotation of its formula.
-- Only the fragment needed for the refutation interface is modelled; the full
-- diagonal lemma (arithmetised substitution inside P) remains open.

data FmlP : Set where
  inj : Fml → FmlP
  P : FmlP → FmlP
  botP : FmlP
  _=>p_ : FmlP → FmlP → FmlP
  allP : Nat → FmlP → FmlP

infixr 4 _=>p_

-- A quotation function for the extended language (tagged numerals).
codeFml : FmlP → Nat
codeFml (inj φ) = (suc (code φ))
codeFml (P φ) = 2 + (1 + codeFml φ)
codeFml botP = 3
codeFml (φ =>p ψ) = 4 + (1 + (codeFml φ + codeFml ψ))
codeFml (allP n φ) = 5 + (1 + (n + codeFml φ))

-- Object-level derivability in the extended language: the Hilbert core plus
-- the representability axiom schema for P on quotations.
infix 3 ⊢p_

data ⊢p_ : FmlP → Set where
  liftK : (φ ψ : FmlP) → ⊢p (φ =>p (ψ =>p φ))
  liftS : (φ ψ χ : FmlP) → ⊢p ((φ =>p (ψ =>p χ)) =>p ((φ =>p ψ) =>p (φ =>p χ)))
  liftMp : {φ ψ : FmlP} → ⊢p (φ =>p ψ) → ⊢p φ → ⊢p ψ
  -- The quotation of φ's code, re-injected as a formula of the extended
  -- language: `inj (num (codeFml φ))`.
  repr : (φ : FmlP) → ⊢p (P (inj (num (codeFml φ) =f num (codeFml φ))))

-- C-pulse-1: the representability schema is available for every formula of
-- the extended language, in particular for the diagonal instance.
reprAll : (φ : FmlP) → ⊢p (P (inj (num (codeFml φ) =f num (codeFml φ))))
reprAll φ = repr φ

-- C-pulse-2: modus ponens is preserved by the lifting, so the object
-- derivability relation of the extended language contains the original
-- Hilbert core.
provMp : {φ ψ : FmlP} → ⊢p (φ =>p ψ) → ⊢p φ → ⊢p ψ
provMp = liftMp
