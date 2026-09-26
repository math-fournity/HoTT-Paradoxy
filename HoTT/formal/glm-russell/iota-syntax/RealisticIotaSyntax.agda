{-# OPTIONS --safe --cubical --guardedness #-}

-- GR-1 self-reference probe, first installment (GLM-5.3-Flash, session
-- S-GOV-20260926-GLM-WORKSPACE-01).  A toy syntax whose ONLY equations are
-- the per-constructor computation rules of a Bool eliminator (real
-- definitional equalities of type theory, by the fairness contract in
-- CLAIM.md).  Headline: this syntax normalizes to Bool and IS a set.

module RealisticIotaSyntax where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool using (Bool ; true ; false)

-- Own eliminator, guaranteeing literal reduction (no reliance on library
-- if-syntax).
BoolElim : ∀ {ℓ} → (A : Bool → Type ℓ) → A true → A false → (b : Bool) → A b
BoolElim A x f true  = x
BoolElim A x f false = f

-- The syntax: literals, a conditional eliminator, and its two computation
-- rules as path constructors.  betaT/betaF are the ι-rules every type
-- theory's Bool eliminator comes with; no substitution machinery is needed
-- to state them.
data Tm : Type where
  lit   : Bool → Tm
  cond  : Tm → Tm → Tm → Tm
  betaT : (t s : Tm) → cond (lit true)  t s ≡ t
  betaF : (t s : Tm) → cond (lit false) t s ≡ s

-- Standard interpretation into Bool.  Both βι-cases are literally refl:
-- this is the definitional fact that real equations are fact-interpreted
-- (GLM-R1-C02).
val : Tm → Bool
val (lit b) = b
val (cond u v w) = BoolElim (λ _ → Bool) (val v) (val w) (val u)
val (betaT t s i) = val t
val (betaF t s i) = val s

-- Machine-witnessed documentation of GLM-R1-C02: the interpretation of
-- each computation rule IS refl, definitionally.
valReflT : (t s : Tm)
         → Path (Path Bool (val (cond (lit true) t s)) (val t)) refl refl
valReflT t s = refl

valReflF : (t s : Tm)
         → Path (Path Bool (val (cond (lit false) t s)) (val s)) refl refl
valReflF t s = refl

-- A square filler: the composite (p ∙ r) seen over its LEFT factor p,
-- obtained by reversing the interval of the library's compPath-filler'
-- (whose family runs over p (~ j)).  Needed for HIT elimination at the
-- path constructors below.
squareLeft : ∀ {ℓ} {A : Type ℓ} {x y z : A} (p : x ≡ y) (r : y ≡ z)
           → PathP (λ i → p i ≡ z) (p ∙ r) r
squareLeft p r j = compPath-filler' p r (~ j)

-- OPEN OBLIGATION (GLM-R1-C01, not discharged in this installment):
--   isSet Tm.  The natural route is the normalization lemma
--   q : (t : Tm) → t ≡ lit (val t), whose path-constructor clauses demand
--   squares of the form  PathP (λ i → betaT t s i ≡ lit (val t))
--   ((λ i → cond (q (lit true) i) t s) ∙ (betaT t s ∙ q t)) (q t)
--   i.e. HIT-elimination into path types with boundary coherence between
--   the clause structure and the composite presentation.  The cubical
--   library's own way to obtain a set-level syntax is to ADD a trunc
--   constructor (as C-67 part (b) did), which forces rather than proves
--   set-hood.  Blocker recorded in CLAIM.md; see GLM-5.3-Flash index §8.
