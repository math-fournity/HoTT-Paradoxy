module ReflectionSketch where

open import Agda.Builtin.Nat
open import Agda.Builtin.Equality
open import ObjectSyntax
open import DiagonalCore
open import DiagonalLemma
open import ProvRepresentability

-- T3 pulse (bounded, fourth stage): the *reflection interface* between the
-- code-level substitution function (DiagonalLemma) and the object-level
-- provability predicate (ProvRepresentability).  We do not claim to derive the
-- reflection principle from arithmetic; we pin down its exact shape, so that
-- the remaining gap is a single named obligation instead of an implicit one.

-- The reflection obligation: the object language recognises that substituting
-- the numeral k for the variable i in φ yields the formula whose code is
-- computed by the code-level substitution function.
Reflect : Set
Reflect = (φ : Fml) (k i : Nat)
        → ⊢p (P (inj (num (_⟨_/_⟩c φ k i) =f num (_⟨_/_⟩c φ k i))))

-- The reflection obligation, pinned as a type.  Whether it follows from
-- `repr` alone is NOT claimed here: the formula whose representation `repr`
-- provides is keyed by `codeFml`, while the substitution instance's code is
-- computed by `_⟨_/_⟩c`; deriving that the two agree (an arithmetic identity on
-- codes) is part of the remaining T3 work.  Pinning the shape turns the gap
-- from an implicit assumption into a single named obligation.
reflectIsNamedObligation : Set
reflectIsNamedObligation = Reflect

-- What remains open (and is NOT claimed here): that the object theory proves
-- the fixed-point equation φ ↔ ¬P(⌜φ⌝) for the diagonal candidate.  That
-- derivation needs the reflection principle plus the consistency side
-- conditions, which are exactly the gated ERCF-3 body.
