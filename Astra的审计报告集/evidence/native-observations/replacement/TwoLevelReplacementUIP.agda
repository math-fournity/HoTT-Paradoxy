{-# OPTIONS --safe --cubical --guardedness #-}

module TwoLevelReplacementUIP where

-- MP-CUBICAL-2LTT-FIBRANT-REPLACEMENT-UIP-001 / C-227--C-232
--
-- A boundary-preserving algebraic encoding of the core of Theorem 2.20 in
-- Annenkov--Capriotti--Kraus--Sattler, "Two-Level Type Theory and Applications".
-- Outer types are ordinary Agda types and outer equality is the inductive
-- equality E._≡_.  Inner types are *codes* interpreted by El.  In particular,
-- the inner path eliminator below can eliminate only to an Inner code; it
-- cannot silently eliminate a native Cubical path into an arbitrary outer
-- Agda type.  This separation is why R is visible in the proof.

open import Cubical.Foundations.Prelude
import Agda.Builtin.Equality as E
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Bool.Base using (Bool; false)
open import Cubical.Data.Bool.Properties using (notEq; false≢true)
open import Cubical.HITs.S1.Base using (S¹; base; loop)


-- FORM-R, INTRO-R and ELIM-R live in the same record as the minimum inner and
-- outer structure used by the proof.  No COMP-R field is present: the proof
-- below therefore establishes that the computation rule is not required for
-- the UIP consequence.  ELIM-R is dependent; recR below is derived from it.
record TwoLevelReplacement : Type₂ where
  field
    Inner : Type₁
    El : Inner → Type

    Idᵢ : (A : Inner) → El A → El A → Inner
    reflᵢ : {A : Inner} (x : El A) → El (Idᵢ A x x)
    Jᵢ : {A : Inner} {x : El A}
      (P : (y : El A) → El (Idᵢ A x y) → Inner)
      → El (P x (reflᵢ x))
      → {y : El A} (p : El (Idᵢ A x y))
      → El (P y p)

    Πᵢ : (A : Inner) → (El A → Inner) → Inner
    lamᵢ : {A : Inner} {B : El A → Inner}
      → ((x : El A) → El (B x)) → El (Πᵢ A B)
    appᵢ : {A : Inner} {B : El A → Inner}
      → El (Πᵢ A B) → (x : El A) → El (B x)

    -- Outer UIP.  E._≡_ retains its ordinary J rule; UIP is supplied as the
    -- outer-level principle, never inferred from native Cubical paths.
    strictUIP : {X : Type} {x y : X}
      → (p q : x E.≡ y) → p E.≡ q

    -- The context-uniform replacement type former and its dependent
    -- eliminator.  R may be applied to the outer witness type that itself
    -- depends on an inner path p; this is the exact uniformity used below.
    R : Type → Inner
    r : {X : Type} → X → El (R X)
    elimR : {X : Type}
      → (P : El (R X) → Inner)
      → ((x : X) → El (P (r x)))
      → (z : El (R X))
      → El (P z)

open TwoLevelReplacement


strictCong : ∀ {X Y : Type} (f : X → Y) {x y : X}
  → x E.≡ y → f x E.≡ f y
strictCong f E.refl = E.refl


module ReplacementConsequences (F : TwoLevelReplacement) where
  private
    Code = Inner F
    Eᵢ = El F

  -- The internalisation of paper map (2.7): strict equality implies inner
  -- equality.  The refl computation is definitional because E._≡_ has J.
  encode : {A : Code} {x y : Eᵢ A}
    → x E.≡ y → Eᵢ (Idᵢ F A x y)
  encode E.refl = reflᵢ F _

  symᵢ : {A : Code} {x y : Eᵢ A}
    → Eᵢ (Idᵢ F A x y) → Eᵢ (Idᵢ F A y x)
  symᵢ {A} {x} =
    Jᵢ F (λ y _ → Idᵢ F A y x) (reflᵢ F x)

  -- The outer type inside R in paper formula (2.13).
  StrictWitness : (A : Code) (u v : Eᵢ A)
    → Eᵢ (Idᵢ F A u v) → Type
  StrictWitness A u v p =
    (h : u E.≡ v)
    → Eᵢ (Idᵢ F (Idᵢ F A u v) (encode h) p)

  -- C-227 / paper formula (2.14): outer UIP makes every strict loop encode to
  -- the inner reflexivity path.  strictCong transports the UIP proof through
  -- encode; the second encode turns that strict equality into an inner path.
  strict-loop-canonical : {A : Code} {u : Eᵢ A}
    → (h : u E.≡ u)
    → Eᵢ (Idᵢ F (Idᵢ F A u u) (encode h) (reflᵢ F u))
  strict-loop-canonical {A} {u} h =
    encode
      (strictCong (λ q → encode {A = A} q)
        (strictUIP F h E.refl))

  -- C-228 / paper formula (2.13).  The motive is inner only because the
  -- context-uniform R turns the p-dependent outer StrictWitness into a code.
  lifted-witness : {A : Code} {u v : Eᵢ A}
    → (p : Eᵢ (Idᵢ F A u v))
    → Eᵢ (R F (StrictWitness A u v p))
  lifted-witness {A} {u} =
    Jᵢ F
      (λ v p → R F (StrictWitness A u v p))
      (r F strict-loop-canonical)

  -- The nondependent universal property is the constant-family instance of
  -- ELIM-R.  It is kept as a derived definition so the proof dependency on the
  -- paper's eliminator is syntactically visible.
  recR : {X : Type} {Y : Code}
    → (X → Eᵢ Y) → Eᵢ (R F X) → Eᵢ Y
  recR {Y = Y} f = elimR F (λ _ → Y) f

  -- C-229 (based form): evaluate a StrictWitness at strict reflexivity, then
  -- reverse the resulting inner path.  This contracts every inner loop.
  based-uip : {A : Code} {u : Eᵢ A}
    → (p : Eᵢ (Idᵢ F A u u))
    → Eᵢ (Idᵢ F (Idᵢ F A u u) p (reflᵢ F u))
  based-uip {A} {u} p =
    recR
      (λ witness → symᵢ (witness E.refl))
      (lifted-witness p)

  -- C-229 (full form): inner Π and one further inner J turn based contraction
  -- into uniqueness of all inner identity proofs.
  inner-uip : {A : Code} {x y : Eᵢ A}
    → (p q : Eᵢ (Idᵢ F A x y))
    → Eᵢ (Idᵢ F (Idᵢ F A x y) p q)
  inner-uip {A} {x} p =
    appᵢ F
      (Jᵢ F
        (λ y p → Πᵢ F (Idᵢ F A x y)
          (λ q → Idᵢ F (Idᵢ F A x y) p q))
        (lamᵢ F (λ q → symᵢ (based-uip q)))
        p)

  record NontrivialInnerLoop : Type₁ where
    field
      A : Code
      x : Eᵢ A
      p : Eᵢ (Idᵢ F A x x)
      p≠refl :
        Eᵢ (Idᵢ F (Idᵢ F A x x) p (reflᵢ F x)) → ⊥

  -- C-230: any nontrivial inner loop contradicts the replacement fragment.
  replacement-excludes-nontrivial-loop : NontrivialInnerLoop → ⊥
  replacement-excludes-nontrivial-loop witness =
    NontrivialInnerLoop.p≠refl witness
      (based-uip (NontrivialInnerLoop.p witness))


-- C-231, native Cubical control: S¹ has a loop distinct from reflexivity.
-- This is deliberately outside ReplacementConsequences.  It confirms that
-- the intended HoTT inner world has higher structure; it is not a claimed
-- semantic instantiation of the abstract two-level record above.
möbius : S¹ → Type
möbius base = Bool
möbius (loop i) = notEq i

odd? : base ≡ base → Bool
odd? equality = subst möbius equality false

refl≢loop : refl ≡ loop → ⊥
refl≢loop equality = false≢true (cong odd? equality)

loop≢refl : loop ≡ refl → ⊥
loop≢refl equality = refl≢loop (sym equality)


-- C-232, positive ablation: FORM/INTRO/dependent ELIM by themselves are
-- inhabited in native Cubical Type.  The collapse needs the two-level strict
-- UIP bridge together with R's uniform availability inside inner path
-- induction; an R-shaped interface in a single universe is not the result.
NativeR : Type → Type
NativeR X = X

native-r : {X : Type} → X → NativeR X
native-r x = x

native-elimR : {X : Type}
  → (P : NativeR X → Type)
  → ((x : X) → P (native-r x))
  → (z : NativeR X)
  → P z
native-elimR P d z = d z
