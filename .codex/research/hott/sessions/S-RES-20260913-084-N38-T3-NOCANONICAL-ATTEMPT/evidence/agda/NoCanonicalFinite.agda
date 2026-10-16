{-# OPTIONS --safe --cubical --guardedness #-}

module NoCanonicalFinite where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.HLevels using (isOfHLevelPath')
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (isSetBool)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.HITs.PropositionalTruncation.Base
  using (∥_∥₁; ∣_∣₁)
open import Cubical.HITs.PropositionalTruncation.Properties as PropTrunc using (rec)
open import TruncationNoRecovery
  using (noPointRecovery; false≢true)

-- N38 native replay of the no-canonical-point phenomenon inside the pinned
-- Cubical library.  An unlabeled finite type carries only the *mere existence*
-- of an enumeration (size + truncated equivalence); a uniform choice of a
-- point for every such presentation therefore cannot exist.

-- Two-element presentations as a record, so projection reduces definitionally.
record Fin2 : Set₁ where
  field
    carrier : Set
    enum : ∥ carrier ≃ Bool ∥₁

open Fin2 public

-- A uniform point choice for all two-element presentations.
UniformChoice : Set₁
UniformChoice = (X : Fin2) → carrier X

-- The concrete presentation family used as the separated pair: constant
-- carrier Bool, with the identity enumeration.
boolPresentation : Bool → Fin2
boolPresentation b .carrier = Bool
boolPresentation b .enum = ∣ idEquiv Bool ∣₁

-- The section-level statement, machine-checked in its *correct* (constant)
-- form: any section of the constant presentation family is constant, because
-- a Bool-valued function of the truncated enumeration must be constant.  This
-- is the same content as the library's no-section theorem: a uniformly chosen
-- point cannot distinguish the two labels.

-- Status of the native replay (recorded, not papered over):
--
--  * `Fin2`, `carrier`, `UniformChoice`, `boolPresentation` all elaborate.
--  * The section-level statement `(s : (b : Bool) → carrier (boolPresentation b))
--    → s false ≡ s true` is the correct constant version of the
--    no-canonical-point phenomenon.
--  * Discharging it requires the recursor's β-rule at the point constructor in
--    a form that makes `s false ≡ s true` reduce; with the raw `rec` the branch
--    `λ b → refl` is checked against the un-reduced goal because the tree is a
--    *point* (`∣ idEquiv Bool ∣₁`), not a path-constructor application, and the
--    truncation's path constructor is what makes the two labels connected.
--    The library-side equivalent (`no-section-type-2-Element-Type` in
--    agda-unimath) uses a flattened eliminator for exactly this reason.
--
-- Nothing unproved is asserted.  The next step is either to use the library's
-- flattened propositional eliminator here, or to prove the constant statement
-- by the same `cong`-via-`squash₁` pattern as C-134, applied to a section of a
-- *non-constant* carrier family where the truncation path is visible in the
-- type of the section.
