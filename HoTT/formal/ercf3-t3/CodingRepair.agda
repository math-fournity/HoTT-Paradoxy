module CodingRepair where

open import Agda.Builtin.Nat
open import Agda.Builtin.Equality
open import Agda.Builtin.Bool using (Bool; false; true)
open import ObjectSyntax
open import DiagonalCore
open import DiagonalLemma
open import DecodingFence

-- T3 sixteenth pulse (bounded): the *coding-repair specification*.
--
-- `DecodingFence` (C-160/C-161) showed the concrete `codeT`/`codeF` are not
-- injective, so the decodability obligation recorded in `ObjectSyntax` cannot
-- be met by them.  Before writing any arithmetic coding this module fixes what
-- "repaired" must mean, and derives the exact obligation that remains:
--
--   1. a coder that has a round-trip decoder is injective (generic lemma);
--   2. a *structured* (tree) coding is decodable and therefore injective
--      -- the positive control, and the shape any repaired coding should have;
--   3. the current Nat coding admits **no** decoder (no-go), which is the
--      precise form of the repair requirement.

------------------------------------------------------------------------
-- Local equality helpers (builtins only).

sym' : {A : Set} {x y : A} → x ≡ y → y ≡ x
sym' refl = refl

trans' : {A : Set} {x y z : A} → x ≡ y → y ≡ z → x ≡ z
trans' refl q = q

record Σ' (A : Set) (B : A → Set) : Set where
  constructor _,_
  field fst' : A
        snd' : B fst'

------------------------------------------------------------------------
-- C-164: generic lemma -- a coder with a round-trip decoder is injective.
-- This is the *specification* of what a repaired coding has to provide, and
-- it holds for any target type (not only Nat).

roundtrip-implies-injective :
  {A : Set} (c : Tm → A) (dec : A → Tm)
  → ((t : Tm) → dec (c t) ≡ t)
  → (t u : Tm) → c t ≡ c u → t ≡ u
roundtrip-implies-injective c dec rt t u p =
  trans' (sym' (rt t)) (trans' (cong-here dec p) (rt u))

------------------------------------------------------------------------
-- C-163: structured (tree) coding -- decodable, hence injective.
-- The coding keeps the constructors as constructors, so no arithmetic is
-- needed; this is the positive control showing a repaired coding exists for
-- the *structure* of the language.

data CodeT : Set where
  cvar cnum : Nat → CodeT
  cadd : CodeT → CodeT → CodeT

encT : Tm → CodeT
encT (var n) = cvar n
encT (num n) = cnum n
encT (t +t u) = cadd (encT t) (encT u)

decT : CodeT → Tm
decT (cvar n) = var n
decT (cnum n) = num n
decT (cadd a b) = decT a +t decT b

encT-roundtrip : (t : Tm) → decT (encT t) ≡ t
encT-roundtrip (var n) = refl
encT-roundtrip (num n) = refl
encT-roundtrip (t +t u) =
  cong₂ _+t_ (encT-roundtrip t) (encT-roundtrip u)

encT-injective : (t u : Tm) → encT t ≡ encT u → t ≡ u
encT-injective = roundtrip-implies-injective encT decT encT-roundtrip

------------------------------------------------------------------------
-- C-165: the current coding admits no decoder -- the repair requirement.

no-decoder-for-codeT :
  Σ' (Nat → Tm) (λ dec → (t : Tm) → dec (codeT t) ≡ t) → Empty
no-decoder-for-codeT (dec , rt) =
  no-injective-codeT (roundtrip-implies-injective codeT dec rt)

-- Repair obligation (recorded, not yet discharged): provide
-- `codeT' : Tm → Nat` together with `dec' : Nat → Tm` and a round-trip proof;
-- by C-164 such a pair is automatically injective.  The structural half is
-- done (C-163); the arithmetic half (a Nat-valued coder with a decoder,
-- e.g. disjoint tag ranges `3n`/`3n+1`/`3*⟨pair⟩+2` or a list encoding)
-- is the next bounded pulse.
repairObligation : Set
repairObligation = Nat
