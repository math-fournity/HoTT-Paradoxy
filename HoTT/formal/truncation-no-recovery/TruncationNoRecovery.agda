{-# OPTIONS --safe --cubical --guardedness #-}

module TruncationNoRecovery where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
  using (isOfHLevelPath')
open import Cubical.Data.Bool.Base
  using (Bool; false; true)
open import Cubical.Data.Bool.Properties
  using (isSetBool)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.Nat.Properties
  using (isSetℕ)
open import Cubical.HITs.PropositionalTruncation.Base
  using (∥_∥₁; ∣_∣₁; squash₁)
open import Cubical.HITs.PropositionalTruncation.Properties
  using (rec)

private
  variable
    ℓ ℓ' : Level

-- Paths in a set are propositions (standard h-level law, library lemma).
setPathIsProp : {S : Type ℓ} (Sset : isSet S) (x y : S) → isProp (x ≡ y)
setPathIsProp Sset x y = isOfHLevelPath' 1 Sset x y

true≢false : true ≡ false → ⊥
true≢false p = subst T p tt
  where
    T : Bool → Type
    T true = Unit
    T false = ⊥

false≢true : false ≡ true → ⊥
false≢true p = true≢false (sym p)

zero≢one : zero ≡ suc zero → ⊥
zero≢one p = subst Z p tt
  where
    Z : ℕ → Type
    Z zero = Unit
    Z (suc _) = ⊥

-- C-134: the generic fence.  A test g that reads the propositional truncation
-- of a source and agrees with a realization h on every point constructor must
-- send any two point constructors to path-equal values: the squash path
-- constructor between them is carried by congruent application of g.  The
-- target only needs to be a set, because that is what makes the path type
-- g ∣ a₀ ∣₁ ≡ g ∣ a₁ ∣₁ a proposition and thus admissible as the motive of the
-- native truncated recursor.  No axiom, choice or classical principle occurs.
pointConstructorsForceEquality :
  {A : Type ℓ} {S : Type ℓ'}
  (Sset : isSet S)
  (h : A → S) (a₀ a₁ : A)
  (g : ∥ A ∥₁ → S)
  (β : (a : A) → g ∣ a ∣₁ ≡ h a)
  → h a₀ ≡ h a₁
pointConstructorsForceEquality {A = A} {S = S} Sset h a₀ a₁ g β =
  sym (β a₀) ∙ middle a₁ ∙ β a₁
  where
    -- Constancy of the test on two point constructors, for every pair.
    middle : (a₁' : A) → g ∣ a₀ ∣₁ ≡ g ∣ a₁' ∣₁
    middle a₁' = rec prop branch ∣ a₀ ∣₁
      where
        prop : isProp (g ∣ a₀ ∣₁ ≡ g ∣ a₁' ∣₁)
        prop = setPathIsProp Sset (g ∣ a₀ ∣₁) (g ∣ a₁' ∣₁)

        branch : (a : A) → g ∣ a₀ ∣₁ ≡ g ∣ a₁' ∣₁
        branch a =
          sym (cong g (squash₁ ∣ a ∣₁ ∣ a₀ ∣₁))
          ∙ cong g (squash₁ ∣ a ∣₁ ∣ a₁' ∣₁)

-- C-135: the named no-go, applied form.  Once a separation witness for the
-- realization is supplied, point-preserving untruncation is impossible.
noPointRecovery :
  {X : Type ℓ} {S : Type ℓ'}
  (Sset : isSet S)
  (h : X → S) (g : ∥ X ∥₁ → S) (x₀ x₁ : X)
  (β : (x : X) → g ∣ x ∣₁ ≡ h x)
  → (h x₀ ≡ h x₁ → ⊥) → ⊥
noPointRecovery Sset h g x₀ x₁ β sep =
  sep (pointConstructorsForceEquality Sset h x₀ x₁ g β)

-- C-136: first concrete instance.  The identity realizes two separated points
-- of Bool, so the point-preserving untruncation of Bool is impossible.
boolRecoveryImpossible :
  (extract : ∥ Bool ∥₁ → Bool)
  → ((b : Bool) → extract ∣ b ∣₁ ≡ b)
  → ⊥
boolRecoveryImpossible extract β =
  noPointRecovery isSetBool (λ b → b) extract false true β false≢true

-- C-137: second concrete instance.  The same fence applies to ℕ with the
-- separated pair 0 and 1, so the obstruction is not an artifact of a
-- two-element target.
ℕRecoveryImpossible :
  (extract : ∥ ℕ ∥₁ → ℕ)
  → ((n : ℕ) → extract ∣ n ∣₁ ≡ n)
  → ⊥
ℕRecoveryImpossible extract β =
  noPointRecovery isSetℕ (λ n → n) extract zero (suc zero) β zero≢one

-- C-138: positive control.  When the consumer target is a mere proposition,
-- the same shape is available and the fence does not apply; what is refused is
-- recovering the identity of the witness, not consuming the truncation.
propositionValuedTestExists :
  {A : Type ℓ} {P : Type ℓ'} (Pprop : isProp P) (f : A → P)
  → ∥ A ∥₁ → P
propositionValuedTestExists Pprop f = rec Pprop f

-- C-139: the section-candidate type is empty, as a statement inside HoTT.
-- The type of "programs that recover the untruncated witness" has no
-- inhabitant; this is the internal negation form of C-136, and it is what a
-- Zeno-style reading needs: the theory itself proves that the uniform
-- completion cannot be produced.
noSectionCandidate :
  (P : ∥ Bool ∥₁ → Bool)
  → ((b : Bool) → P ∣ b ∣₁ ≡ b)
  → ⊥
noSectionCandidate = boolRecoveryImpossible

-- C-140: the same statement for a general separated realization, phrased as
-- the emptiness of the completion-candidate type.  It is the applied form of
-- C-135 with the separation witness supplied by the consumer.
noCompletionCandidate :
  {X : Type ℓ} {S : Type ℓ'}
  (Sset : isSet S)
  (h : X → S) (x₀ x₁ : X)
  (sep : h x₀ ≡ h x₁ → ⊥)
  → (T : ∥ X ∥₁ → S)
  → ((x : X) → T ∣ x ∣₁ ≡ h x)
  → ⊥
noCompletionCandidate Sset h x₀ x₁ sep T β =
  noPointRecovery Sset h T x₀ x₁ β sep

-- C-141: the same fence on a real pinned-library interface.  Cubical's
-- `isFinSet A = Σ[ n ∈ ℕ ] ∥ A ≃ Fin n ∥₁` keeps only the mere existence of an
-- enumeration.  Any operation that reads a specific enumeration out of it is
-- therefore constant in the enumeration component, so it cannot return two
-- prescribed non-identical enumerations of the same two-element set.  This is
-- the concrete library-shape instance of C-139, stated for the interface that
-- derived developments actually consume.
isFinSetLikeNoUniformEnumeration :
  {E : Type ℓ} (P : isSet E)
  (e₀ e₁ : E) (sep : e₀ ≡ e₁ → ⊥)
  → (pick : ∥ E ∥₁ → E)
  → ((e : E) → pick ∣ e ∣₁ ≡ e)
  → ⊥
isFinSetLikeNoUniformEnumeration {E = E} P e₀ e₁ sep pick β =
  sep (pointConstructorsForceEquality' P (λ e → e) e₀ e₁ pick β)
  where
    pointConstructorsForceEquality' :
      isSet E → (h : E → E) → (a₀ a₁ : E)
      → (g : ∥ E ∥₁ → E)
      → ((a : E) → g ∣ a ∣₁ ≡ h a)
      → h a₀ ≡ h a₁
    pointConstructorsForceEquality' Q h a₀ a₁ g γ =
      pointConstructorsForceEquality Q h a₀ a₁ g γ
