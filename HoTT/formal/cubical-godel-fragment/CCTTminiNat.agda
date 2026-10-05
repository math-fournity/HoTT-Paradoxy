{-# OPTIONS --safe --cubical #-}

-- GZ-009: a total natural-number coding for the finite CCTTmini₀
-- certificate language.  This is deliberately self-contained: it does not
-- import the older ERCF coding chain, because its object syntax is different.

module CCTTminiNat where

open import Agda.Builtin.Nat using (Nat; zero; suc; _+_)
open import Agda.Builtin.Equality using (_≡_; refl)
open import Agda.Builtin.Bool using (Bool; true; false)
open import Agda.Builtin.List using (List; []; _∷_)
open import Agda.Builtin.Maybe using (Maybe; nothing; just)
open import CCTTmini

------------------------------------------------------------------------
-- Equality and list utilities.

sym' : {A : Set} {x y : A} → x ≡ y → y ≡ x
sym' refl = refl

trans' : {A : Set} {x y z : A} → x ≡ y → y ≡ z → x ≡ z
trans' refl q = q

cong' : {A B : Set} (f : A → B) {x y : A} → x ≡ y → f x ≡ f y
cong' f refl = refl

_++_ : {A : Set} → List A → List A → List A
[] ++ ys = ys
(x ∷ xs) ++ ys = x ∷ (xs ++ ys)

infixr 5 _++_

+-zero : (n : Nat) → n + zero ≡ n
+-zero zero = refl
+-zero (suc n) = cong' suc (+-zero n)

+-suc : (a b : Nat) → a + suc b ≡ suc (a + b)
+-suc zero b = refl
+-suc (suc a) b = cong' suc (+-suc a b)

+-assoc : (a b c : Nat) → (a + b) + c ≡ a + (b + c)
+-assoc zero b c = refl
+-assoc (suc a) b c = cong' suc (+-assoc a b c)

++-assoc : {A : Set} (xs ys zs : List A) → (xs ++ ys) ++ zs ≡ xs ++ (ys ++ zs)
++-assoc [] ys zs = refl
++-assoc (x ∷ xs) ys zs = cong' (λ ws → x ∷ ws) (++-assoc xs ys zs)

------------------------------------------------------------------------
-- Bit packing into natural numbers and its bounded inverse.

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

pack : Bool → Nat → Nat
pack false c = twice c
pack true c = suc (twice c)

LEN : List Bool → Nat
LEN [] = zero
LEN (b ∷ bs) = suc (LEN bs)

codeBits : List Bool → Nat
codeBits [] = suc zero
codeBits (b ∷ bs) = pack b (codeBits bs)

unbits : Nat → Nat → List Bool
unbits zero c = []
unbits (suc k) c = parity c ∷ unbits k (half c)

parity-twice : (n : Nat) → parity (twice n) ≡ false
parity-twice zero = refl
parity-twice (suc n) = parity-twice n

parity-suc-twice : (n : Nat) → parity (suc (twice n)) ≡ true
parity-suc-twice zero = refl
parity-suc-twice (suc n) = parity-suc-twice n

half-twice : (n : Nat) → half (twice n) ≡ n
half-twice zero = refl
half-twice (suc n) = cong' suc (half-twice n)

half-suc-twice : (n : Nat) → half (suc (twice n)) ≡ n
half-suc-twice zero = refl
half-suc-twice (suc n) = cong' suc (half-suc-twice n)

parity-pack : (b : Bool) (c : Nat) → parity (pack b c) ≡ b
parity-pack false c = parity-twice c
parity-pack true c = parity-suc-twice c

half-pack : (b : Bool) (c : Nat) → half (pack b c) ≡ c
half-pack false c = half-twice c
half-pack true c = half-suc-twice c

unbits-code : (bs : List Bool) → unbits (LEN bs) (codeBits bs) ≡ bs
unbits-code [] = refl
unbits-code (b ∷ bs) =
  trans' (cong' (λ x → parity (pack b c) ∷ unbits (LEN bs) x) (half-pack b c))
    (trans' (cong' (λ x → x ∷ unbits (LEN bs) c) (parity-pack b c))
            (cong' (λ xs → b ∷ xs) (unbits-code bs)))
  where
    c = codeBits bs

data _≤_ : Nat → Nat → Set where
  z≤n : {n : Nat} → zero ≤ n
  s≤s : {m n : Nat} → m ≤ n → suc m ≤ suc n

≤-suc : (n : Nat) → n ≤ suc n
≤-suc zero = z≤n
≤-suc (suc n) = s≤s (≤-suc n)

≤-trans : {i j k : Nat} → i ≤ j → j ≤ k → i ≤ k
≤-trans z≤n q = z≤n
≤-trans (s≤s p) (s≤s q) = s≤s (≤-trans p q)

n≤twice : (n : Nat) → n ≤ twice n
n≤twice zero = z≤n
n≤twice (suc n) = s≤s (≤-trans (n≤twice n) (≤-suc (twice n)))

suc≤pack : (b : Bool) (c : Nat) → suc zero ≤ c → suc c ≤ pack b c
suc≤pack false (suc c) _ = s≤s (s≤s (n≤twice c))
suc≤pack true (suc c) _ = s≤s (s≤s (≤-trans (n≤twice c) (≤-suc (twice c))))

codeBits-dominates : (bs : List Bool) → suc (LEN bs) ≤ codeBits bs
codeBits-dominates [] = s≤s z≤n
codeBits-dominates (b ∷ bs) =
  ≤-trans (s≤s (codeBits-dominates bs))
          (suc≤pack b (codeBits bs) (≤-trans (s≤s z≤n) (codeBits-dominates bs)))

data Split (n m : Nat) : Set where
  split : (k : Nat) → m ≡ n + k → Split n m

≤-split : {n m : Nat} → n ≤ m → Split n m
≤-split z≤n = split _ refl
≤-split (s≤s p) with ≤-split p
... | split k eq = split k (cong' suc eq)

halfs : Nat → Nat → Nat
halfs zero c = c
halfs (suc k) c = halfs k (half c)

unbits-split :
  (i j c : Nat) → unbits (i + j) c ≡ unbits i c ++ unbits j (halfs i c)
unbits-split zero j c = refl
unbits-split (suc i) j c =
  cong' (λ xs → parity c ∷ xs) (unbits-split i j (half c))

------------------------------------------------------------------------
-- A prefix grammar for RawCert.

unary : Nat → List Bool
unary zero = false ∷ []
unary (suc n) = true ∷ unary n

bits : RawCert → List Bool
bits (varC n) = false ∷ false ∷ unary n
bits zeroC = false ∷ true ∷ []
bits (sucC c) = true ∷ false ∷ bits c
bits (reflC c) = true ∷ true ∷ bits c

STEPS : RawCert → Nat
STEPS (varC n) = suc (suc (suc n))
STEPS zeroC = suc (suc zero)
STEPS (sucC c) = suc (suc (STEPS c))
STEPS (reflC c) = suc (suc (STEPS c))

data Slot : Set where
  wantSuc  : Slot
  wantRefl : Slot

data Stack : Set where
  ε : Stack
  _▷_ : Slot → Stack → Stack

infixr 5 _▷_

close : RawCert → Stack → RawCert
close c ε = c
close c (wantSuc ▷ stk) = close (sucC c) stk
close c (wantRefl ▷ stk) = close (reflC c) stk

data Mode : Set where
  startSub : Stack → Mode
  tag2     : Bool → Stack → Mode
  readVar  : Nat → Stack → Mode

record Result : Set where
  constructor res
  field
    rCert : RawCert
    rBits : List Bool

open Result

-- `run` is total because its first argument is a structural fuel counter.
run : Nat → List Bool → Mode → Result
run zero bs m = res zeroC bs
run (suc f) [] m = res zeroC []
run (suc f) (true ∷ rest) (startSub stk) = run f rest (tag2 true stk)
run (suc f) (false ∷ rest) (startSub stk) = run f rest (tag2 false stk)
run (suc f) (true ∷ rest) (tag2 false stk) = res (close zeroC stk) rest
run (suc f) (false ∷ rest) (tag2 false stk) = run f rest (readVar zero stk)
run (suc f) (true ∷ rest) (tag2 true stk) = run f rest (startSub (wantRefl ▷ stk))
run (suc f) (false ∷ rest) (tag2 true stk) = run f rest (startSub (wantSuc ▷ stk))
run (suc f) (true ∷ rest) (readVar n stk) = run f rest (readVar (suc n) stk)
run (suc f) (false ∷ rest) (readVar n stk) = res (close (varC n) stk) rest

unary-run :
  (m k : Nat) (stk : Stack) (rest : List Bool) (f : Nat)
  → run (suc (m + f)) (unary m ++ rest) (readVar k stk)
  ≡ res (close (varC (k + m)) stk) rest
unary-run zero k stk rest f rewrite +-zero k = refl
unary-run (suc m) k stk rest f rewrite +-suc k m = unary-run m (suc k) stk rest f

parse-run :
  (c : RawCert) (stk : Stack) (rest : List Bool) (f : Nat)
  → run (STEPS c + f) (bits c ++ rest) (startSub stk)
  ≡ res (close c stk) rest
parse-run (varC n) stk rest f = unary-run n zero stk rest f
parse-run zeroC stk rest f = refl
parse-run (sucC c) stk rest f = parse-run c (wantSuc ▷ stk) rest f
parse-run (reflC c) stk rest f = parse-run c (wantRefl ▷ stk) rest f

LEN-unary : (n : Nat) → LEN (unary n) ≡ suc n
LEN-unary zero = refl
LEN-unary (suc n) = cong' suc (LEN-unary n)

bits-length : (c : RawCert) → LEN (bits c) ≡ STEPS c
bits-length (varC n) = cong' (λ x → suc (suc x)) (LEN-unary n)
bits-length zeroC = refl
bits-length (sucC c) = cong' (λ x → suc (suc x)) (bits-length c)
bits-length (reflC c) = cong' (λ x → suc (suc x)) (bits-length c)

code : RawCert → Nat
code c = codeBits (bits c)

decode : Nat → RawCert
decode n = rCert (run n (unbits n n) (startSub ε))

code-bound : (c : RawCert) → STEPS c ≤ code c
code-bound c rewrite sym' (bits-length c) =
  ≤-trans (≤-suc (LEN (bits c))) (codeBits-dominates (bits c))

decode-code : (c : RawCert) → decode (code c) ≡ c
decode-code c = trans' run-step cert-step
  where
    n : Nat
    n = code c

    split-fuel : Split (STEPS c) n
    split-fuel = ≤-split (code-bound c)

    k : Nat
    k with split-fuel
    ... | split q eq = q

    fuel-eq : n ≡ STEPS c + k
    fuel-eq with split-fuel
    ... | split q eq = eq

    junk : List Bool
    junk = unbits k (halfs (STEPS c) n)

    bytes : unbits n n ≡ bits c ++ junk
    bytes = trans' step1 step2
      where
        step1 : unbits n n ≡ unbits (STEPS c) n ++ junk
        step1 = trans' (cong' (λ fuel → unbits fuel n) fuel-eq)
                       (unbits-split (STEPS c) k n)

        step2 : unbits (STEPS c) n ++ junk ≡ bits c ++ junk
        step2 = cong' (λ xs → xs ++ junk)
                      (trans' (cong' (λ fuel → unbits fuel n) (sym' (bits-length c)))
                              (unbits-code (bits c)))

    run-step :
      rCert (run n (unbits n n) (startSub ε))
      ≡ rCert (run n (bits c ++ junk) (startSub ε))
    run-step = cong' (λ bs → rCert (run n bs (startSub ε))) bytes

    cert-step : rCert (run n (bits c ++ junk) (startSub ε)) ≡ c
    cert-step = trans' (cong' (λ fuel → rCert (run fuel (bits c ++ junk) (startSub ε))) fuel-eq)
                       (cong' rCert (parse-run c ε junk k))

code-injective : (c d : RawCert) → code c ≡ code d → c ≡ d
code-injective c d p =
  trans' (sym' (decode-code c))
    (trans' (cong' decode p) (decode-code d))

positive-code-roundtrip : decode (code positiveC) ≡ positiveC
positive-code-roundtrip = decode-code positiveC
