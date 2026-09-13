module BitCoding where

open import Agda.Builtin.Nat
open import Agda.Builtin.Equality
open import Agda.Builtin.Bool using (Bool; true; false)
open import Agda.Builtin.List using (List; []; _∷_)
open import ObjectSyntax
open import DiagonalCore
open import DecodingFence
open import CodingRepair

-- T3 eighteenth pulse (bounded): the *bit-level substrate* of the arithmetic half.
--
-- The application node needs a pairing/branching code.  Rather than postulating
-- a pairing function with arithmetic lemmas, this pulse builds the substrate a
-- branch code can be decoded with: least-significant-bit extraction
-- (`parity`), the halving map (`half`), and the packing map (`pack`) into a
-- bit list.  Claims:
--
--   C-169  digit arithmetic: `parity (twice n) = false`, `parity (suc (twice n)) = true`,
--          `half (twice n) = n`, `half (suc (twice n)) = n`;
--   C-170  bundle coding: `codeBits` packs a bit list (`[] ↦ 1`, `b∷bs ↦ pack b …`) and
--          `unbits` extracts it back; the two are inverse on the two sides;
--   C-171  round-trip *when the length is known*:
--          `unbits (LEN bs) (codeBits bs) ≡ bs`.
--   C-172  the code dominates its own length: `suc (LEN bs) ≤ codeBits bs`,
--          so the fuel for the future parser can be taken from the code itself.
--
-- The remaining piece (next bounded pulse) is the *decoder side*: the symbol
-- layer (self-delimiting var/num index bits and the constructor tags) and the
-- parser with its default branch (C-168) -- after which C-164 yields
-- injectivity of the full Nat-valued coding.

------------------------------------------------------------------------
-- C-169: digit arithmetic.

parity : Nat → Bool
parity zero = false
parity (suc zero) = true
parity (suc (suc n)) = parity n

half : Nat → Nat
half zero = zero
half (suc zero) = zero
half (suc (suc n)) = suc (half n)

twice : Nat → Nat
twice zero = zero
twice (suc n) = suc (suc (twice n))

parity-twice : (n : Nat) → parity (twice n) ≡ false
parity-twice zero = refl
parity-twice (suc n) = parity-twice n

parity-suc-twice : (n : Nat) → parity (suc (twice n)) ≡ true
parity-suc-twice zero = refl
parity-suc-twice (suc n) = parity-suc-twice n

half-twice : (n : Nat) → half (twice n) ≡ n
half-twice zero = refl
half-twice (suc n) = cong-here suc (half-twice n)

half-suc-twice : (n : Nat) → half (suc (twice n)) ≡ n
half-suc-twice zero = refl
half-suc-twice (suc n) = cong-here suc (half-suc-twice n)

------------------------------------------------------------------------
-- C-170: packing a bit list into Nat and extracting it again.

bitToNat : Bool → Nat
bitToNat false = zero
bitToNat true = suc zero

pack : Bool → Nat → Nat
pack false c = twice c
pack true c = suc (twice c)

LEN : List Bool → Nat
LEN [] = zero
LEN (b ∷ bs) = suc (LEN bs)

-- The sentinel is the leading 1: `[] ↦ 1`, and each further bit is shifted in.
codeBits : List Bool → Nat
codeBits [] = suc zero
codeBits (b ∷ bs) = pack b (codeBits bs)

-- Length-driven extraction (this is why the round-trip below needs `LEN`).
unbits : Nat → Nat → List Bool
unbits zero c = []
unbits (suc k) c = parity c ∷ unbits k (half c)

parity-code : (b : Bool) (c : Nat) → parity (pack b c) ≡ b
parity-code false c = parity-twice c
parity-code true c = parity-suc-twice c

half-code : (b : Bool) (c : Nat) → half (pack b c) ≡ c
half-code false c = half-twice c
half-code true c = half-suc-twice c

------------------------------------------------------------------------
-- C-171: round-trip of `codeBits`/`unbits` when the length is supplied.

unbits-code : (bs : List Bool) → unbits (LEN bs) (codeBits bs) ≡ bs
unbits-code [] = refl
unbits-code (b ∷ bs) =
  trans' (cong-here (λ x → parity (pack b c) ∷ unbits (LEN bs) x) (half-code b c))
    (trans' (cong-here (λ y → y ∷ unbits (LEN bs) c) (parity-code b c))
            (cong-here (λ xs → b ∷ xs) (unbits-code bs)))
  where
    c = codeBits bs

------------------------------------------------------------------------
-- C-172: the code dominates its own length, so the parser can be driven by the
-- code itself (no external length parameter).  The bound is the only arithmetic
-- statement the decoder side needs from the bit substrate.

data _≤_ : Nat → Nat → Set where
  z≤n : {n : Nat} → zero ≤ n
  s≤s : {m n : Nat} → m ≤ n → suc m ≤ suc n

≤-refl : (n : Nat) → n ≤ n
≤-refl zero = z≤n
≤-refl (suc n) = s≤s (≤-refl n)

≤-suc : (n : Nat) → n ≤ suc n
≤-suc zero = z≤n
≤-suc (suc n) = s≤s (≤-suc n)

≤-trans : {i j k : Nat} → i ≤ j → j ≤ k → i ≤ k
≤-trans z≤n q = z≤n
≤-trans (s≤s p) (s≤s q) = s≤s (≤-trans p q)

n≤twice : (n : Nat) → n ≤ twice n
n≤twice zero = z≤n
n≤twice (suc n) = s≤s (≤-trans (n≤twice n) (≤-suc (twice n)))

-- One halving step is dominated by one packed digit, provided a digit is there
-- to read (`suc zero ≤ c` is exactly "the remaining bundle is non-empty").
suc≤pack : (b : Bool) (c : Nat) → suc zero ≤ c → suc c ≤ pack b c
suc≤pack false (suc c) _ = s≤s (s≤s (n≤twice c))
suc≤pack true (suc c) _ = s≤s (s≤s (≤-trans (n≤twice c) (≤-suc (twice c))))

codeBits-dominates : (bs : List Bool) → suc (LEN bs) ≤ codeBits bs
codeBits-dominates [] = s≤s z≤n
codeBits-dominates (b ∷ bs) =
  ≤-trans (s≤s (codeBits-dominates bs))
          (suc≤pack b (codeBits bs) (≤-trans (s≤s z≤n) (codeBits-dominates bs)))

-- Recorded remaining obligation for the next bounded pulse (stated only; the
-- bit substrate itself is closed above):
--
--   the symbol layer (`var n`/`num n` index bits, self-delimiting so that the
--   parser needs no length parameter) plus the parser with its default branch
--   (C-168), and the round-trip on the image -- which by C-164 yields
--   injectivity of the full Nat-valued coder `t ↦ codeBits (bits t)`.
