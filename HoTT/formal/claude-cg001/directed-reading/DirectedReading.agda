{-# OPTIONS --safe --cubical --guardedness #-}
{-
  What an up-then-down reading needs from its target (Claude, session
  91a6cdaa, 2026-09-25), in reply to Terra's audit 003, question O-010.

  proof id : MP-CG001-DIRECTED-READING-001
  claims   : CG001-C-34 .. CG001-C-38 (full statements in CLAIM.md)

  A reading along a directed journey 0 -> 1 -> 2 that goes a, b, a sends the
  two arrows of the journey to arrows a -> b and b -> a of the reading target.

  C-34  if every arrow of the target collapses (a -> b gives a = b), or the
        target is antisymmetric (a -> b and b -> a give a = b), there is no
        such reading with a /= b.
  C-35  if in the target a mutually inverse pair of arrows forces equal
        objects (as it does when isomorphism is identity, the Rezk
        condition), every such reading uses a pair that is not mutually
        inverse.
  C-36  a target where inverse pairs do not collapse: two distinct objects
        joined by one invertible pair (codiscrete); it carries such a reading
        with an invertible cycle.
  C-37  a target where they do: the walking retraction (objects A, B;
        f : A -> B, g : B -> A, g after f = id_B, f then g = an idempotent
        e /= id_A), a category; it carries such a reading with a
        non-invertible cycle.
  C-38  abstract freeze: for any type J with points j0, j1, a reading into a
        type R whose constant map R -> (J -> R) is an equivalence takes equal
        values at the two ends of every journey J -> X.

  This is a model at the level of objects, arrows and composition, plus one
  abstract lemma; it is not simplicial type theory.  Bridge labels (reading,
  journey, thermometer) prove no physical fact.
-}
module DirectedReading where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Sigma
open import Cubical.Data.Bool using (Bool; true; false; true≢false; false≢true)
open import Cubical.Data.Unit using (Unit; tt)
open import Cubical.Data.Empty using (⊥) renaming (rec to ⊥-rec)
open import Cubical.Relation.Nullary using (¬_)

------------------------------------------------------------------------
-- Reading targets: objects, arrows, identities, composition (first ⋆ then)

record Target : Type₁ where
  field
    Ob  : Type
    Hom : Ob → Ob → Type
    idA : (a : Ob) → Hom a a
    _⋆_ : {a b c : Ob} → Hom a b → Hom b c → Hom a c

module Readings (T : Target) where
  open Target T

  -- a reading along 0 -> 1 -> 2 that goes a, b, a with a /= b
  UpThenDown : Type
  UpThenDown = Σ[ a ∈ Ob ] Σ[ b ∈ Ob ] (¬ (a ≡ b)) × Hom a b × Hom b a

  InversePair : {a b : Ob} → Hom a b → Hom b a → Type
  InversePair {a} {b} f g = ((f ⋆ g) ≡ idA a) × ((g ⋆ f) ≡ idA b)

  ArrowsCollapse : Type
  ArrowsCollapse = (a b : Ob) → Hom a b → a ≡ b

  Antisymmetric : Type
  Antisymmetric = (a b : Ob) → Hom a b → Hom b a → a ≡ b

  InversePairsCollapse : Type
  InversePairsCollapse = (a b : Ob) (f : Hom a b) (g : Hom b a) → InversePair f g → a ≡ b

  -- CG001-C-34
  collapseFreezes : ArrowsCollapse → ¬ UpThenDown
  collapseFreezes c (a , b , a≢b , f , g) = a≢b (c a b f)

  antisymmetryFreezes : Antisymmetric → ¬ UpThenDown
  antisymmetryFreezes s (a , b , a≢b , f , g) = a≢b (s a b f g)

  -- CG001-C-35
  cycleNotInvertible : InversePairsCollapse → (a b : Ob) → ¬ (a ≡ b)
    → (f : Hom a b) (g : Hom b a) → ¬ InversePair f g
  cycleNotInvertible c a b a≢b f g inv = a≢b (c a b f g inv)

------------------------------------------------------------------------
-- CG001-C-36  A codiscrete target: an invertible cycle between distinct objects

codiscrete : Target
codiscrete = record
  { Ob = Bool
  ; Hom = λ _ _ → Unit
  ; idA = λ _ → tt
  ; _⋆_ = λ _ _ → tt
  }

module Codiscrete = Readings codiscrete

codiscreteUpThenDown : Codiscrete.UpThenDown
codiscreteUpThenDown = true , false , true≢false , tt , tt

codiscreteCycleInvertible : Codiscrete.InversePair {true} {false} tt tt
codiscreteCycleInvertible = refl , refl

codiscreteDoesNotCollapse : ¬ Codiscrete.InversePairsCollapse
codiscreteDoesNotCollapse c = true≢false (c true false tt tt (refl , refl))

------------------------------------------------------------------------
-- CG001-C-37  The walking retraction: inverse pairs collapse, yet a, b, a is read

-- endomorphisms of A: the identity and the idempotent e = f then g
data EndA : Type where
  idAA idem : EndA

isIdentity : EndA → Bool
isIdentity idAA = true
isIdentity idem = false

idem≢idAA : ¬ (idem ≡ idAA)
idem≢idAA p = false≢true (cong isIdentity p)

-- objects: true is A, false is B
WHom : Bool → Bool → Type
WHom true true = EndA    -- id_A and e
WHom true false = Unit   -- f : A -> B
WHom false true = Unit   -- g : B -> A
WHom false false = Unit  -- id_B

wid : (a : Bool) → WHom a a
wid true = idAA
wid false = tt

-- composition in diagrammatic order: wcomp x y is "x, then y"
wcomp : {a b c : Bool} → WHom a b → WHom b c → WHom a c
wcomp {true} {true} {true} idAA y = y
wcomp {true} {true} {true} idem idAA = idem
wcomp {true} {true} {true} idem idem = idem
wcomp {true} {true} {false} x y = tt     -- id_A then f = f;  e then f = f
wcomp {true} {false} {true} x y = idem   -- f then g = e
wcomp {true} {false} {false} x y = tt    -- f then id_B = f
wcomp {false} {true} {true} x y = tt     -- g then id_A = g;  g then e = g
wcomp {false} {true} {false} x y = tt    -- g then f = id_B
wcomp {false} {false} {true} x y = tt    -- id_B then g = g
wcomp {false} {false} {false} x y = tt   -- id_B then id_B = id_B

-- it is a category: unit laws and associativity
wIdL : {a b : Bool} (x : WHom a b) → wcomp (wid a) x ≡ x
wIdL {true} {true} idAA = refl
wIdL {true} {true} idem = refl
wIdL {true} {false} tt = refl
wIdL {false} {true} tt = refl
wIdL {false} {false} tt = refl

wIdR : {a b : Bool} (x : WHom a b) → wcomp x (wid b) ≡ x
wIdR {true} {true} idAA = refl
wIdR {true} {true} idem = refl
wIdR {true} {false} tt = refl
wIdR {false} {true} tt = refl
wIdR {false} {false} tt = refl

wAssoc : {a b c d : Bool} (x : WHom a b) (y : WHom b c) (z : WHom c d)
  → wcomp (wcomp x y) z ≡ wcomp x (wcomp y z)
wAssoc {true} {true} {true} {true} idAA y z = refl
wAssoc {true} {true} {true} {true} idem idAA z = refl
wAssoc {true} {true} {true} {true} idem idem idAA = refl
wAssoc {true} {true} {true} {true} idem idem idem = refl
wAssoc {true} {true} {true} {false} x y z = refl
wAssoc {true} {true} {false} {true} idAA y z = refl
wAssoc {true} {true} {false} {true} idem y z = refl
wAssoc {true} {true} {false} {false} x y z = refl
wAssoc {true} {false} {true} {true} x y idAA = refl
wAssoc {true} {false} {true} {true} x y idem = refl
wAssoc {true} {false} {true} {false} x y z = refl
wAssoc {true} {false} {false} {true} x y z = refl
wAssoc {true} {false} {false} {false} x y z = refl
wAssoc {false} {true} {true} {true} x y z = refl
wAssoc {false} {true} {true} {false} x y z = refl
wAssoc {false} {true} {false} {true} x y z = refl
wAssoc {false} {true} {false} {false} x y z = refl
wAssoc {false} {false} {true} {true} x y z = refl
wAssoc {false} {false} {true} {false} x y z = refl
wAssoc {false} {false} {false} {true} x y z = refl
wAssoc {false} {false} {false} {false} x y z = refl

walkingRetraction : Target
walkingRetraction = record { Ob = Bool ; Hom = WHom ; idA = wid ; _⋆_ = wcomp }

module Retraction = Readings walkingRetraction

retractionCollapsesInversePairs : Retraction.InversePairsCollapse
retractionCollapsesInversePairs true true f g _ = refl
retractionCollapsesInversePairs false false f g _ = refl
retractionCollapsesInversePairs true false f g (fg , gf) = ⊥-rec (idem≢idAA fg)
retractionCollapsesInversePairs false true f g (fg , gf) = ⊥-rec (idem≢idAA gf)

retractionUpThenDown : Retraction.UpThenDown
retractionUpThenDown = true , false , true≢false , tt , tt

retractionCycleNotInvertible : ¬ Retraction.InversePair {true} {false} tt tt
retractionCycleNotInvertible =
  Retraction.cycleNotInvertible retractionCollapsesInversePairs true false true≢false tt tt

------------------------------------------------------------------------
-- CG001-C-38  Abstract freeze: readings into a J-null type do not change along J

module Freeze {ℓ ℓ' ℓ''} (J : Type ℓ) (j0 j1 : J) {X : Type ℓ'} {R : Type ℓ''} where

  constMap : R → (J → R)
  constMap r _ = r

  frozenAlongJourney : isEquiv constMap → (T : X → R) (γ : J → X) → T (γ j0) ≡ T (γ j1)
  frozenAlongJourney e T γ =
    sym (funExt⁻ back j0) ∙ funExt⁻ back j1
    where
    back : constMap (invEq (constMap , e) (λ j → T (γ j))) ≡ (λ j → T (γ j))
    back = secEq (constMap , e) (λ j → T (γ j))
