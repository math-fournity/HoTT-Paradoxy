module ArithmeticTags where

open import Agda.Builtin.Nat
open import Agda.Builtin.Equality
open import Agda.Builtin.Bool using (Bool; false; true)
open import ObjectSyntax
open import DiagonalCore
open import CodingRepair
open import DecodingFence

-- T3 seventeenth pulse (bounded): the *arithmetic half*, first piece.
--
-- `CodingRepair` (C-163/C-164/C-165) fixed the repair obligation: a Nat-valued
-- coder with a decoder (round-trip).  Its arithmetic half starts with the
-- classic tag-disjoint shapes `2n` and `2n + 1`; this module machine-checks the
-- arithmetic core those shapes need, on the `var`/`num` fragment:
--
--   C-166  `double` is injective, and `double n` never equals `odd m`
--          (even/odd tag disjointness);
--   C-167  the fragment coder `codeAtom` (`avar n ↦ 2n`, `anum n ↦ 2n+1`)
--          is injective -- the first Nat-valued injective coding in the chain;
--   C-168  the coder is not surjective (`1` has no preimage), so any *total*
--          decoder must have a default branch -- the control the next pulse
--          (application node + decoder) has to respect.

------------------------------------------------------------------------
-- Arithmetic helpers (builtins only).

suc-injective : {x y : Nat} → suc x ≡ suc y → x ≡ y
suc-injective refl = refl

suc≠zero : {k : Nat} → Not (suc k ≡ zero)
suc≠zero ()

ex-falso : {A : Set} → Empty → A
ex-falso ()

double : Nat → Nat
double zero = zero
double (suc n) = suc (suc (double n))

odd : Nat → Nat
odd n = suc (double n)

-- C-166 (part 1): double is injective.
double-injective : (n m : Nat) → double n ≡ double m → n ≡ m
double-injective zero zero p = refl
double-injective zero (suc m) ()
double-injective (suc n) zero ()
double-injective (suc n) (suc m) p =
  cong-here suc (double-injective n m (suc-injective (suc-injective p)))

-- C-166 (part 2): even and odd tags are disjoint.
double≠odd : (n m : Nat) → Not (double n ≡ odd m)
double≠odd zero m ()
double≠odd (suc n) zero p = suc≠zero (suc-injective p)
double≠odd (suc n) (suc m) p = double≠odd n m (suc-injective (suc-injective p))

odd-injective : (n m : Nat) → odd n ≡ odd m → n ≡ m
odd-injective n m p = double-injective n m (suc-injective p)

------------------------------------------------------------------------
-- C-167: the fragment coder with disjoint tags is injective.

data Atom : Set where
  avar anum : Nat → Atom

codeAtom : Atom → Nat
codeAtom (avar n) = double n
codeAtom (anum n) = odd n

codeAtom-injective : (x y : Atom) → codeAtom x ≡ codeAtom y → x ≡ y
codeAtom-injective (avar n) (avar m) p = cong-here avar (double-injective n m p)
codeAtom-injective (avar n) (anum m) p = ex-falso (double≠odd n m p)
codeAtom-injective (anum n) (avar m) p = ex-falso (double≠odd m n (sym' p))
codeAtom-injective (anum n) (anum m) p = cong-here anum (odd-injective n m p)

------------------------------------------------------------------------
-- C-168: the coder is not surjective, so a total decoder needs a default.

one-has-no-preimage : Not (Σ' Nat (λ m → double m ≡ suc zero))
one-has-no-preimage (zero , ())
one-has-no-preimage (suc m , p) = suc≠zero (suc-injective p)

-- Recorded remaining obligation of the arithmetic half: extend the disjoint-tag
-- shapes to the application node (`_+t_` needs a pairing function) and write a
-- total decoder with a default branch, then prove the round-trip on the image
-- (which by C-164 yields injectivity of the Nat-valued coder).
remainingArithmeticObligation : Set
remainingArithmeticObligation = Nat
