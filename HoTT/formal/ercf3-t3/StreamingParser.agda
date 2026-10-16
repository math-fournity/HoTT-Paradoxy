module StreamingParser where

open import Agda.Builtin.Nat
open import Agda.Builtin.Equality
open import Agda.Builtin.Bool using (Bool; true; false)
open import Agda.Builtin.List using (List; []; _∷_)
open import ObjectSyntax
open import DiagonalCore
open import DecodingFence
open import CodingRepair
open import BitCoding

-- T3 nineteenth pulse (bounded): the *symbol layer* and a parser that can be
-- driven by the code alone.
--
-- `BitCoding` (C-169-C-172) closed the bit substrate: digits, bundling and the
-- bound that the code dominates its own length.  This module closes the piece
-- the two earlier pulses recorded as the next obligation:
--
--   C-173  the self-delimiting index layer: `unary n` is `n` ones followed by a
--          zero, and reading it returns exactly `n` and the rest;
--   C-174  the symbol layer (`bits`/`BLEN`: two tag bits for `var`/`num` plus
--          their index, one tag bit for application) and a *streaming* parser
--          (`run`) whose round trip is exact: the fuel needed is `BLEN t + k`
--          and the unconsumed fuel is exactly `k`.
--   C-175  length bookkeeping (`LEN (bits t) ≡ BLEN t`), the bound-as-sum
--          splitting (`n ≤ m` gives `m ≡ n + k`) and the extra-fuel splitting of
--          `unbits` (reading with more fuel than the length appends exactly the
--          bits the halving sequence supplies);
--   C-176  the repaired coder `codeT'` (`t ↦ codeBits (bits t)`) with a *total*
--          decoder `dec` (default branches included, as C-168 requires) and the
--          round trip `dec (codeT' t) ≡ t`; by C-164 `codeT'` is injective.
--
-- The parser solves the sequential-consumption problem with an explicit frame
-- stack instead of nested recursive calls, so it terminates structurally on the
-- fuel: after reading the left child of an application the loop must know that
-- the right child is still pending, and it must do so *inside* the same
-- decreasing recursion.
--
-- What this pulse does *not* do: it discharges the coding-repair obligation of
-- C-163/C-165 (a decodable, hence injective, Nat-valued coding of the terms),
-- but it says nothing about the proof predicate `P`, reflection or the diagonal
-- fixed point; ERCF-3 itself stays `GATED` on the consumer door.

------------------------------------------------------------------------
-- Local list append (builtins only).

_++_ : {A : Set} → List A → List A → List A
[] ++ ys = ys
(x ∷ xs) ++ ys = x ∷ (xs ++ ys)

infixr 5 _++_

------------------------------------------------------------------------
-- C-173: the self-delimiting index layer.

unary : Nat → List Bool
unary zero = false ∷ []
unary (suc n) = true ∷ unary n

leafTerm : Bool → Nat → Tm
leafTerm false n = var n
leafTerm true n = num n

------------------------------------------------------------------------
-- The symbol layer: two tag bits for the leaves, one for application.

bits : Tm → List Bool
bits (var n) = false ∷ false ∷ unary n
bits (num n) = false ∷ true ∷ unary n
bits (t +t u) = true ∷ (bits t ++ bits u)

BLEN : Tm → Nat
BLEN (var n) = suc (suc (suc n))
BLEN (num n) = suc (suc (suc n))
BLEN (t +t u) = suc (BLEN t + BLEN u)

------------------------------------------------------------------------
-- Pending application frames and the control state of the streaming parser.

data Slot : Set where
  wantLeft : Slot
  haveLeft : Tm → Slot

data Stack : Set where
  ε : Stack
  _▷_ : Slot → Stack → Stack

infixr 5 _▷_

data Verdict : Set where
  finish : Tm → Verdict
  next : Stack → Verdict

-- Completing `t` in the context `stk`: either the whole term is finished, or
-- the enclosing application still needs its right child (parsed from the same
-- remaining bits).
close : Tm → Stack → Verdict
close t ε = finish t
close t (wantLeft ▷ stk) = next (haveLeft t ▷ stk)
close t (haveLeft l ▷ stk) = close (l +t t) stk

data Mode : Set where
  startSub : Stack → Mode
  wantTag2 : Stack → Mode
  readIndex : Bool → Nat → Stack → Mode

record Result : Set where
  constructor res
  field rTerm : Tm
        rBits : List Bool

open Result
open Σ'

subst' : {A : Set} (P : A → Set) {x y : A} → x ≡ y → P x → P y
subst' P refl p = p

-- One iteration consumes exactly one bit and one unit of fuel, so `run`
-- terminates structurally on the fuel.  `zero` and `[]` are the default
-- branches that C-168 requires of any total decoder.
--
-- `resume` says what the loop does once a completed subterm has been placed in
-- its context; the leaf clause *is* that continuation, which keeps the
-- definitional behaviour and the round-trip statement aligned.
mutual
  run : Nat → List Bool → Mode → Result
  run zero bs m = res (num 0) bs
  run (suc f) [] m = res (num 0) []
  run (suc f) (true ∷ rest) (startSub stk) = run f rest (startSub (wantLeft ▷ stk))
  run (suc f) (false ∷ rest) (startSub stk) = run f rest (wantTag2 stk)
  run (suc f) (true ∷ rest) (wantTag2 stk) = run f rest (readIndex true 0 stk)
  run (suc f) (false ∷ rest) (wantTag2 stk) = run f rest (readIndex false 0 stk)
  run (suc f) (true ∷ rest) (readIndex b n stk) = run f rest (readIndex b (suc n) stk)
  run (suc f) (false ∷ rest) (readIndex b n stk) = resume (close (leafTerm b n) stk) rest f

  resume : Verdict → List Bool → Nat → Result
  resume (finish t) rest f = res t rest
  resume (next stk) rest f = run f rest (startSub stk)

------------------------------------------------------------------------
-- Arithmetic and list bookkeeping (builtins only).

+-zero : (n : Nat) → n + zero ≡ n
+-zero zero = refl
+-zero (suc n) = cong-here suc (+-zero n)

+-suc : (a b : Nat) → a + suc b ≡ suc (a + b)
+-suc zero b = refl
+-suc (suc a) b = cong-here suc (+-suc a b)

+-assoc : (a b c : Nat) → (a + b) + c ≡ a + (b + c)
+-assoc zero b c = refl
+-assoc (suc a) b c = cong-here suc (+-assoc a b c)

++-assoc : {A : Set} (xs ys zs : List A) → (xs ++ ys) ++ zs ≡ xs ++ (ys ++ zs)
++-assoc [] ys zs = refl
++-assoc (x ∷ xs) ys zs = cong-here (λ zs' → x ∷ zs') (++-assoc xs ys zs)

LEN-++ : (xs ys : List Bool) → LEN (xs ++ ys) ≡ LEN xs + LEN ys
LEN-++ [] ys = refl
LEN-++ (x ∷ xs) ys = cong-here suc (LEN-++ xs ys)

------------------------------------------------------------------------
-- C-173: reading a self-delimiting index from a bit stream.

unary-run :
  (m k : Nat) (b : Bool) (stk : Stack) (rest : List Bool) (f : Nat)
  → run (suc (m + f)) (unary m ++ rest) (readIndex b k stk)
  ≡ resume (close (leafTerm b (k + m)) stk) rest f
unary-run zero k b stk rest f rewrite +-zero k = refl
unary-run (suc m) k b stk rest f rewrite +-suc k m =
  unary-run m (suc k) b stk rest f

------------------------------------------------------------------------
-- C-174: the streaming round trip of the symbol layer.

mutual
  parse-run :
    (t : Tm) (stk : Stack) (rest : List Bool) (f : Nat)
    → run (BLEN t + f) (bits t ++ rest) (startSub stk)
    ≡ resume (close t stk) rest f
  parse-run (var n) stk rest f = unary-run n 0 false stk rest f
  parse-run (num n) stk rest f = unary-run n 0 true stk rest f
  parse-run (t +t u) stk rest f = parse-run-app t u stk rest f

  parse-run-app :
    (t u : Tm) (stk : Stack) (rest : List Bool) (f : Nat)
    → run (suc ((BLEN t + BLEN u) + f)) (true ∷ ((bits t ++ bits u) ++ rest)) (startSub stk)
    ≡ resume (close (t +t u) stk) rest f
  parse-run-app t u stk rest f
    rewrite +-assoc (BLEN t) (BLEN u) f
    | ++-assoc (bits t) (bits u) rest
    = trans' (parse-run t (wantLeft ▷ stk) (bits u ++ rest) (BLEN u + f))
             (parse-run u (haveLeft t ▷ stk) rest f)

------------------------------------------------------------------------
-- C-175: length bookkeeping and the fuel splittings the Nat-level decoder
-- needs.

LEN-unary : (n : Nat) → LEN (unary n) ≡ suc n
LEN-unary zero = refl
LEN-unary (suc n) = cong-here suc (LEN-unary n)

bits-length : (t : Tm) → LEN (bits t) ≡ BLEN t
bits-length (var n) = cong-here (λ x → suc (suc x)) (LEN-unary n)
bits-length (num n) = cong-here (λ x → suc (suc x)) (LEN-unary n)
bits-length (t +t u)
  rewrite LEN-++ (bits t) (bits u)
  | bits-length t
  | bits-length u = refl

-- `≤` as a sum: every bound is a slack decomposition.
≤-split : {n m : Nat} → n ≤ m → Σ' Nat (λ k → m ≡ n + k)
≤-split z≤n = _ , refl
≤-split (s≤s p) with ≤-split p
... | k , eq = k , cong-here suc eq

-- Reading with more fuel than the length: the extra bits are exactly the ones
-- the halving sequence supplies.
halfs : Nat → Nat → Nat
halfs zero c = c
halfs (suc k) c = halfs k (half c)

unbits-split :
  (i j c : Nat) → unbits (i + j) c ≡ unbits i c ++ unbits j (halfs i c)
unbits-split zero j c = refl
unbits-split (suc i) j c =
  cong-here (λ xs → parity c ∷ xs) (unbits-split i j (half c))

------------------------------------------------------------------------
-- C-176: the repaired coder and its total decoder, with the round trip.

codeT' : Tm → Nat
codeT' t = codeBits (bits t)

dec : Nat → Tm
dec c = rTerm (run c (unbits c c) (startSub ε))

-- The bound that lets the code be its own fuel: C-172 (the code dominates the
-- length) transported along the length agreement of the symbol layer.
codeT'-bound : (t : Tm) → BLEN t ≤ codeBits (bits t)
codeT'-bound t rewrite sym' (bits-length t) =
  ≤-trans (≤-suc (LEN (bits t))) (codeBits-dominates (bits t))

codeT'-roundtrip : (t : Tm) → dec (codeT' t) ≡ t
codeT'-roundtrip t = trans' run-step term-step
  where
    bound : BLEN t ≤ codeBits (bits t)
    bound rewrite sym' (bits-length t) =
      ≤-trans (≤-suc (LEN (bits t))) (codeBits-dominates (bits t))

    split : Σ' Nat (λ k → codeBits (bits t) ≡ BLEN t + k)
    split = ≤-split bound

    k : Nat
    k = fst' split

    eq : codeBits (bits t) ≡ BLEN t + k
    eq = snd' split

    junk : List Bool
    junk = unbits k (halfs (BLEN t) (codeBits (bits t)))

    bytes : unbits (codeBits (bits t)) (codeBits (bits t)) ≡ bits t ++ junk
    bytes = trans' step1 step2
      where
        step1 :
          unbits (codeBits (bits t)) (codeBits (bits t))
          ≡ unbits (BLEN t) (codeBits (bits t)) ++ junk
        step1 = subst'
          (λ fuel → unbits fuel (codeBits (bits t))
                   ≡ unbits (BLEN t) (codeBits (bits t)) ++ junk)
          (sym' eq)
          (unbits-split (BLEN t) k (codeBits (bits t)))

        step2 : unbits (BLEN t) (codeBits (bits t)) ++ junk ≡ bits t ++ junk
        step2 = subst'
          (λ fuel → unbits fuel (codeBits (bits t)) ++ junk ≡ bits t ++ junk)
          (bits-length t)
          (cong-here (λ xs → xs ++ junk) (unbits-code (bits t)))

    run-step :
      rTerm (run (codeBits (bits t)) (unbits (codeBits (bits t)) (codeBits (bits t))) (startSub ε))
      ≡ rTerm (run (codeBits (bits t)) (bits t ++ junk) (startSub ε))
    run-step = cong-here (λ bs → rTerm (run (codeBits (bits t)) bs (startSub ε))) bytes

    term-step : rTerm (run (codeBits (bits t)) (bits t ++ junk) (startSub ε)) ≡ t
    term-step = subst'
      (λ fuel → rTerm (run fuel (bits t ++ junk) (startSub ε)) ≡ t)
      (sym' eq)
      (cong-here rTerm (parse-run t ε junk k))

-- The repair obligation recorded in `CodingRepair` (C-163/C-164/C-165) is
-- discharged at the *coding* layer: `codeT'` is a Nat-valued coder with a total
-- decoder, hence injective, and it is built from the same syntax the diagonal
-- core uses.
codeT'-injective : (t u : Tm) → codeT' t ≡ codeT' u → t ≡ u
codeT'-injective = roundtrip-implies-injective codeT' dec codeT'-roundtrip
