{-# OPTIONS --cubical --safe --guardedness #-}

module FormulaBitCode where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ ; zero ; suc ; _+_)
open import Cubical.Data.Bool.Base using (Bool ; false ; true)
open import Agda.Builtin.Equality renaming (_≡_ to _≡b_; refl to reflb)
open import MiniProofChecker using (Fml ; atom ; bot ; _⇒_)
open import ProofSerialization using (List ; [] ; _∷_)

infixr 5 _++_

_++_ : {A : Type} → List A → List A → List A
[] ++ ys = ys
(x ∷ xs) ++ ys = x ∷ (xs ++ ys)

LEN : {A : Type} → List A → ℕ
LEN [] = zero
LEN (x ∷ xs) = suc (LEN xs)

+-zero : (n : ℕ) → n + zero ≡b n
+-zero zero = reflb
+-zero (suc n) rewrite +-zero n = reflb

+-suc : (n m : ℕ) → n + suc m ≡b suc (n + m)
+-suc zero m = reflb
+-suc (suc n) m rewrite +-suc n m = reflb

+-assoc : (a b c : ℕ) → (a + b) + c ≡b a + (b + c)
+-assoc zero b c = reflb
+-assoc (suc a) b c rewrite +-assoc a b c = reflb

append-assoc : {A : Type} (xs ys zs : List A)
             → (xs ++ ys) ++ zs ≡b xs ++ (ys ++ zs)
append-assoc [] ys zs = reflb
append-assoc (x ∷ xs) ys zs rewrite append-assoc xs ys zs = reflb

append-zero : {A : Type} (xs : List A) → xs ++ [] ≡b xs
append-zero [] = reflb
append-zero (x ∷ xs) rewrite append-zero xs = reflb

congb : {A B : Type} (f : A → B) {x y : A} → x ≡b y → f x ≡b f y
congb f reflb = reflb

transb : {A : Type} {x y z : A} → x ≡b y → y ≡b z → x ≡b z
transb reflb q = q

symb : {A : Type} {x y : A} → x ≡b y → y ≡b x
symb reflb = reflb

unary : ℕ → List Bool
unary zero = false ∷ []
unary (suc n) = true ∷ unary n

bitsF : Fml → List Bool
bitsF (atom n) = false ∷ unary n
bitsF bot = true ∷ false ∷ []
bitsF (φ ⇒ ψ) = true ∷ true ∷ (bitsF φ ++ bitsF ψ)

STEPS : Fml → ℕ
STEPS (atom n) = suc (suc n)
STEPS bot = suc (suc zero)
STEPS (φ ⇒ ψ) = suc (suc (STEPS φ + STEPS ψ))

LEN-++ : {A : Type} (xs ys : List A) → LEN (xs ++ ys) ≡b LEN xs + LEN ys
LEN-++ [] ys = reflb
LEN-++ (x ∷ xs) ys rewrite LEN-++ xs ys = reflb

LEN-unary : (n : ℕ) → LEN (unary n) ≡b suc n
LEN-unary zero = reflb
LEN-unary (suc n) rewrite LEN-unary n = reflb

bits-length : (φ : Fml) → LEN (bitsF φ) ≡b STEPS φ
bits-length (atom n) rewrite LEN-unary n = reflb
bits-length bot = reflb
bits-length (φ ⇒ ψ)
  rewrite LEN-++ (bitsF φ) (bitsF ψ)
        | bits-length φ | bits-length ψ = reflb

data Slot : Type where
  wantRight : Slot
  haveLeft : Fml → Slot

data Stack : Type where
  ε : Stack
  pushF : Slot → Stack → Stack

data Mode : Type where
  wantFml : Stack → Mode
  tag2 : Stack → Mode
  index : ℕ → Stack → Mode

data Verdict : Type where
  finish : Fml → Verdict
  next : Mode → Verdict

record Result : Type where
  constructor res
  field
    rFml : Fml
    rBits : List Bool
    rOk : Bool

open Result

close : Fml → Stack → Verdict
close φ ε = finish φ
close φ (pushF wantRight stk) = next (wantFml (pushF (haveLeft φ) stk))
close φ (pushF (haveLeft left) stk) = close (left ⇒ φ) stk

mutual
  run : Mode → ℕ → List Bool → Result
  run (wantFml stk) (suc fuel) (false ∷ rest) = run (index zero stk) fuel rest
  run (wantFml stk) (suc fuel) (true ∷ rest) = run (tag2 stk) fuel rest
  run (tag2 stk) (suc fuel) (false ∷ rest) = resume (close bot stk) rest fuel
  run (tag2 stk) (suc fuel) (true ∷ rest) = run (wantFml (pushF wantRight stk)) fuel rest
  run (index n stk) (suc fuel) (false ∷ rest) = resume (close (atom n) stk) rest fuel
  run (index n stk) (suc fuel) (true ∷ rest) = run (index (suc n) stk) fuel rest
  run mode zero bits = res bot bits false
  run mode (suc fuel) [] = res bot [] false

  resume : Verdict → List Bool → ℕ → Result
  resume (finish φ) rest fuel = res φ rest true
  resume (next mode) rest fuel = run mode fuel rest

index-run :
  (m k : ℕ) (stk : Stack) (rest : List Bool) (fuel : ℕ)
  → run (index k stk) (suc (m + fuel)) (unary m ++ rest)
  ≡b resume (close (atom (k + m)) stk) rest fuel
index-run zero k stk rest fuel rewrite +-zero k = reflb
index-run (suc m) k stk rest fuel rewrite +-suc k m =
  index-run m (suc k) stk rest fuel

parse-run :
  (φ : Fml) (stk : Stack) (rest : List Bool) (fuel : ℕ)
  → run (wantFml stk) (STEPS φ + fuel) (bitsF φ ++ rest)
  ≡b resume (close φ stk) rest fuel
parse-run (atom n) stk rest fuel = index-run n zero stk rest fuel
parse-run bot stk rest fuel = reflb
parse-run (φ ⇒ ψ) stk rest fuel
  rewrite append-assoc (bitsF φ) (bitsF ψ) rest
        | +-assoc (STEPS φ) (STEPS ψ) fuel =
  transb
    (parse-run φ (pushF wantRight stk) (bitsF ψ ++ rest) (STEPS ψ + fuel))
    (parse-run ψ (pushF (haveLeft φ) stk) rest fuel)

parsePrefix : List Bool → Result
parsePrefix bits = run (wantFml ε) (LEN bits) bits

parsePrefix-roundtrip : (φ : Fml) (rest : List Bool)
                      → parsePrefix (bitsF φ ++ rest) ≡b res φ rest true
parsePrefix-roundtrip φ rest
  rewrite LEN-++ (bitsF φ) rest | bits-length φ =
  parse-run φ ε rest (LEN rest)

decodeF : List Bool → Fml
decodeF bits = rFml (parsePrefix bits)

parsePrefix-exact : (φ : Fml) → parsePrefix (bitsF φ) ≡b res φ [] true
parsePrefix-exact φ =
  transb (symb (congb parsePrefix (append-zero (bitsF φ))))
         (parsePrefix-roundtrip φ [])

decodeF-roundtrip : (φ : Fml) → decodeF (bitsF φ) ≡b φ
decodeF-roundtrip φ = congb rFml (parsePrefix-exact φ)

decodeF-ok : (φ : Fml) → rOk (parsePrefix (bitsF φ)) ≡b true
decodeF-ok φ = congb rOk (parsePrefix-exact φ)
