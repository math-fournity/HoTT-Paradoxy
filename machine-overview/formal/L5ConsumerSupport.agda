{-# OPTIONS --safe #-}

-- L5 consumer-qualification controls.
--
-- This module keeps four capabilities separate:
--
--   1. checking one supplied derivation;
--   2. running an explicitly fuel-bounded proof search;
--   3. deciding truth in a closed finite Boolean fragment;
--   4. combining a Löb rule with reflection and an internal certificate for
--      that reflection.
--
-- The first three are positive controls.  The fourth is a generic
-- self-certification boundary.  Nothing in this module identifies the latter
-- interface with Agda, Cubical Agda, HoTT, MetaRocq, or the unfinished ERCF-3
-- proof predicate.  That correspondence is a separate source audit.

module L5ConsumerSupport where

open import Agda.Builtin.Bool using (Bool; false; true)
open import Agda.Builtin.Equality using (_≡_; refl)
open import Agda.Builtin.Nat using (Nat; zero; suc)
import ObjectSyntax as OS

data ⊥ : Set where

------------------------------------------------------------------------
-- 1. Given-proof checking over the fixed ERCF-3 object syntax.

kFormula : OS.Fml
kFormula = OS._=>f_ OS.bot (OS._=>f_ OS.bot OS.bot)

givenK : OS.⊢ kFormula
givenK = OS.axK OS.bot OS.bot

checkGivenProof : {φ : OS.Fml} → OS.⊢ φ → OS.⊢ φ
checkGivenProof derivation = derivation

------------------------------------------------------------------------
-- 2. One concrete bounded search.  The fuel is part of the result contract;
--    this is not an unbounded theoremhood decider.

searchK : Nat → Bool
searchK zero = false
searchK (suc _) = true

searchAtOne : searchK (suc zero) ≡ true
searchAtOne = refl

searchAtZero : searchK zero ≡ false
searchAtZero = refl

searchSoundAtOne : searchK (suc zero) ≡ true → OS.⊢ kFormula
searchSoundAtOne _ = givenK

------------------------------------------------------------------------
-- 3. Total truth evaluation for an explicitly finite closed fragment.

data BFml : Set where
  lit : Bool → BFml
  _=>b_ : BFml → BFml → BFml

infixr 4 _=>b_

implies : Bool → Bool → Bool
implies false _ = true
implies true b = b

evalB : BFml → Bool
evalB (lit b) = b
evalB (φ =>b ψ) = implies (evalB φ) (evalB ψ)

truthFormula : BFml
truthFormula = lit true =>b lit true

falseFormula : BFml
falseFormula = lit false

truthDecision : evalB truthFormula ≡ true
truthDecision = refl

falseDecision : evalB falseFormula ≡ false
falseDecision = refl

------------------------------------------------------------------------
-- 4. Generic Löb/self-certification boundary.
--
-- `reflect` interprets boxed evidence, `lob` is the Löb rule supplied by a
-- quotation/provability construction, and `certify` says that the same box
-- internally certifies reflection for every Type₀ proposition.  Their joint
-- use at ⊥ collapses.  The result is deliberately parameterised: a concrete
-- theory or tool is implicated only if a separate correspondence audit shows
-- that it supplies all three operations with these exact meanings and at the
-- same claimed layer.

NoGlobalSelfCertification : Set₁
NoGlobalSelfCertification =
  {Box : Set → Set}
  → ((A : Set) → Box A → A)
  → ((A : Set) → Box (Box A → A) → Box A)
  → ((A : Set) → Box (Box A → A))
  → ⊥

noGlobalSelfCertification : NoGlobalSelfCertification
noGlobalSelfCertification reflect lob certify =
  reflect ⊥ (lob ⊥ (certify ⊥))
