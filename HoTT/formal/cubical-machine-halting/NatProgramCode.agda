{-# OPTIONS --cubical --safe --guardedness #-}

module NatProgramCode where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ ; zero ; suc ; _+_)
open import Cubical.Data.Nat.Properties using (+-comm)
import Cubical.Data.Nat.Order as NOrder
open import Cubical.Data.Bool.Base using (Bool ; false ; true)
open import Agda.Builtin.List using (List ; [] ; _∷_)

open import MachineHalting using (Instr ; inc0 ; inc1 ; dec0 ; dec1 ; halt ; Config ; initial)
open import ProgramCode using
  ( ProgramCode ; pcNil ; pcCons
  ; runFor ; finalAt ; haltsWithin
  ; haltCode ; loopCode
  ; haltCode-within ; loopCode-not-final ; loopCode-never-within
  )

------------------------------------------------------------------------
-- List and arithmetic support.

_++_ : {A : Type} → List A → List A → List A
[] ++ ys = ys
(x ∷ xs) ++ ys = x ∷ (xs ++ ys)

infixr 5 _++_

LEN : {A : Type} → List A → ℕ
LEN [] = zero
LEN (_ ∷ xs) = suc (LEN xs)

+-zero : (n : ℕ) → n + zero ≡ n
+-zero zero = refl
+-zero (suc n) = cong suc (+-zero n)

+-suc : (a b : ℕ) → a + suc b ≡ suc (a + b)
+-suc zero b = refl
+-suc (suc a) b = cong suc (+-suc a b)

+-assoc : (a b c : ℕ) → (a + b) + c ≡ a + (b + c)
+-assoc zero b c = refl
+-assoc (suc a) b c = cong suc (+-assoc a b c)

++-assoc : {A : Type} (xs ys zs : List A) → (xs ++ ys) ++ zs ≡ xs ++ (ys ++ zs)
++-assoc [] ys zs = refl
++-assoc (x ∷ xs) ys zs = cong (λ rest → x ∷ rest) (++-assoc xs ys zs)

LEN-++ : {A : Type} (xs ys : List A) → LEN (xs ++ ys) ≡ LEN xs + LEN ys
LEN-++ [] ys = refl
LEN-++ (x ∷ xs) ys = cong suc (LEN-++ xs ys)

subst′ : {A : Type} (P : A → Type) {x y : A} → x ≡ y → P x → P y
subst′ P path px = subst P path px

record Σ′ (A : Type) (B : A → Type) : Type where
  constructor _,_
  field fst′ : A
        snd′ : B fst′

open Σ′

------------------------------------------------------------------------
-- A self-delimiting bit-list code in ℕ.

parity : ℕ → Bool
parity zero = false
parity (suc zero) = true
parity (suc (suc n)) = parity n

half : ℕ → ℕ
half zero = zero
half (suc zero) = zero
half (suc (suc n)) = suc (half n)

twice : ℕ → ℕ
twice zero = zero
twice (suc n) = suc (suc (twice n))

pack : Bool → ℕ → ℕ
pack false n = twice n
pack true n = suc (twice n)

codeBits : List Bool → ℕ
codeBits [] = suc zero
codeBits (b ∷ bs) = pack b (codeBits bs)

unbits : ℕ → ℕ → List Bool
unbits zero code = []
unbits (suc fuel) code = parity code ∷ unbits fuel (half code)

parity-twice : (n : ℕ) → parity (twice n) ≡ false
parity-twice zero = refl
parity-twice (suc n) = parity-twice n

parity-suc-twice : (n : ℕ) → parity (suc (twice n)) ≡ true
parity-suc-twice zero = refl
parity-suc-twice (suc n) = parity-suc-twice n

half-twice : (n : ℕ) → half (twice n) ≡ n
half-twice zero = refl
half-twice (suc n) = cong suc (half-twice n)

half-suc-twice : (n : ℕ) → half (suc (twice n)) ≡ n
half-suc-twice zero = refl
half-suc-twice (suc n) = cong suc (half-suc-twice n)

parity-pack : (b : Bool) (n : ℕ) → parity (pack b n) ≡ b
parity-pack false n = parity-twice n
parity-pack true n = parity-suc-twice n

half-pack : (b : Bool) (n : ℕ) → half (pack b n) ≡ n
half-pack false n = half-twice n
half-pack true n = half-suc-twice n

unbits-code : (bs : List Bool) → unbits (LEN bs) (codeBits bs) ≡ bs
unbits-code [] = refl
unbits-code (b ∷ bs) =
  cong
    (λ rest → parity (pack b code) ∷ unbits (LEN bs) rest)
    (half-pack b code)
  ∙ cong
      (λ head → head ∷ unbits (LEN bs) code)
      (parity-pack b code)
  ∙ cong (λ rest → b ∷ rest) (unbits-code bs)
  where
    code = codeBits bs

_≤′_ : ℕ → ℕ → Type
left ≤′ right = NOrder._≤_ left right

infix 4 _≤′_

≤′-suc : (n : ℕ) → n ≤′ suc n
≤′-suc n = NOrder.≤-sucℕ

≤′-trans : {i j k : ℕ} → i ≤′ j → j ≤′ k → i ≤′ k
≤′-trans = NOrder.≤-trans

twice-add : (n : ℕ) → n + n ≡ twice n
twice-add zero = refl
twice-add (suc n) =
  cong suc (+-suc n n)
  ∙ cong (λ value → suc (suc value)) (twice-add n)

n≤′twice : (n : ℕ) → n ≤′ twice n
n≤′twice n = subst (n ≤′_) (twice-add n) NOrder.≤SumLeft

suc≤′pack : (b : Bool) (n : ℕ) → suc zero ≤′ n → suc n ≤′ pack b n
suc≤′pack false n one≤n =
  subst (suc n ≤′_) (twice-add n)
    (NOrder.≤-+-≤ one≤n NOrder.≤-refl)
suc≤′pack true n one≤n =
  NOrder.≤-suc (suc≤′pack false n one≤n)

codeBits-dominates : (bs : List Bool) → suc (LEN bs) ≤′ codeBits bs
codeBits-dominates [] = NOrder.≤-refl
codeBits-dominates (b ∷ bs) =
  ≤′-trans (NOrder.suc-≤-suc (codeBits-dominates bs))
           (suc≤′pack b (codeBits bs)
             (≤′-trans (NOrder.suc-≤-suc NOrder.zero-≤)
                        (codeBits-dominates bs)))

≤′-split : {n m : ℕ} → n ≤′ m → Σ′ ℕ (λ slack → m ≡ n + slack)
≤′-split {n} bound =
  fst bound , sym (snd bound) ∙ +-comm (fst bound) n

halfs : ℕ → ℕ → ℕ
halfs zero code = code
halfs (suc fuel) code = halfs fuel (half code)

unbits-split :
  (prefix suffix code : ℕ) →
  unbits (prefix + suffix) code ≡
  unbits prefix code ++ unbits suffix (halfs prefix code)
unbits-split zero suffix code = refl
unbits-split (suc prefix) suffix code =
  cong (λ rest → parity code ∷ rest)
       (unbits-split prefix suffix (half code))

------------------------------------------------------------------------
-- Self-delimiting syntax for instructions and finite program tables.

unary : ℕ → List Bool
unary zero = false ∷ []
unary (suc n) = true ∷ unary n

LEN-unary : (n : ℕ) → LEN (unary n) ≡ suc n
LEN-unary zero = refl
LEN-unary (suc n) = cong suc (LEN-unary n)

-- Three-bit instruction tags:
-- 000 halt, 001 inc0, 010 inc1, 011 dec0, 100 dec1.
-- The remaining tags 101, 110 and 111 are invalid and decode to halt.

bitsInstr : Instr → List Bool
bitsInstr halt = false ∷ false ∷ false ∷ []
bitsInstr (inc0 next) = false ∷ false ∷ true ∷ unary next
bitsInstr (inc1 next) = false ∷ true ∷ false ∷ unary next
bitsInstr (dec0 onZero onSuc) =
  false ∷ true ∷ true ∷ (unary onZero ++ unary onSuc)
bitsInstr (dec1 onZero onSuc) =
  true ∷ false ∷ false ∷ (unary onZero ++ unary onSuc)

-- Program table framing: false terminates the table; true introduces one
-- instruction followed by the rest of the table.

bitsProgram : ProgramCode → List Bool
bitsProgram pcNil = false ∷ []
bitsProgram (pcCons instruction rest) =
  true ∷ (bitsInstr instruction ++ bitsProgram rest)

------------------------------------------------------------------------
-- Total streaming decoder.  Fuel zero or premature end returns pcNil.

data ProgramStack : Type where
  ε : ProgramStack
  push : Instr → ProgramStack → ProgramStack

closeProgram : ProgramStack → ProgramCode → ProgramCode
closeProgram ε code = code
closeProgram (push instruction stack) code =
  closeProgram stack (pcCons instruction code)

data OneOp : Type where
  doInc0 doInc1 : OneOp

oneInstr : OneOp → ℕ → Instr
oneInstr doInc0 next = inc0 next
oneInstr doInc1 next = inc1 next

data TwoOp : Type where
  doDec0 doDec1 : TwoOp

twoInstr : TwoOp → ℕ → ℕ → Instr
twoInstr doDec0 onZero onSuc = dec0 onZero onSuc
twoInstr doDec1 onZero onSuc = dec1 onZero onSuc

data Mode : Type where
  wantProgram : ProgramStack → Mode
  tag1 : ProgramStack → Mode
  tag2 : Bool → ProgramStack → Mode
  tag3 : Bool → Bool → ProgramStack → Mode
  readOne : OneOp → ℕ → ProgramStack → Mode
  readFirst : TwoOp → ℕ → ProgramStack → Mode
  readSecond : TwoOp → ℕ → ℕ → ProgramStack → Mode

record Result : Type where
  constructor result
  field
    rCode : ProgramCode
    rBits : List Bool

open Result

run : ℕ → List Bool → Mode → Result
run zero bits mode = result pcNil bits
run (suc fuel) [] mode = result pcNil []
run (suc fuel) (false ∷ rest) (wantProgram stack) =
  result (closeProgram stack pcNil) rest
run (suc fuel) (true ∷ rest) (wantProgram stack) =
  run fuel rest (tag1 stack)
run (suc fuel) (bit ∷ rest) (tag1 stack) =
  run fuel rest (tag2 bit stack)
run (suc fuel) (bit ∷ rest) (tag2 first stack) =
  run fuel rest (tag3 first bit stack)
run (suc fuel) (false ∷ rest) (tag3 false false stack) =
  run fuel rest (wantProgram (push halt stack))
run (suc fuel) (true ∷ rest) (tag3 false false stack) =
  run fuel rest (readOne doInc0 zero stack)
run (suc fuel) (false ∷ rest) (tag3 false true stack) =
  run fuel rest (readOne doInc1 zero stack)
run (suc fuel) (true ∷ rest) (tag3 false true stack) =
  run fuel rest (readFirst doDec0 zero stack)
run (suc fuel) (false ∷ rest) (tag3 true false stack) =
  run fuel rest (readFirst doDec1 zero stack)
run (suc fuel) (true ∷ rest) (tag3 true false stack) =
  run fuel rest (wantProgram (push halt stack))
run (suc fuel) (false ∷ rest) (tag3 true true stack) =
  run fuel rest (wantProgram (push halt stack))
run (suc fuel) (true ∷ rest) (tag3 true true stack) =
  run fuel rest (wantProgram (push halt stack))
run (suc fuel) (true ∷ rest) (readOne operation n stack) =
  run fuel rest (readOne operation (suc n) stack)
run (suc fuel) (false ∷ rest) (readOne operation n stack) =
  run fuel rest (wantProgram (push (oneInstr operation n) stack))
run (suc fuel) (true ∷ rest) (readFirst operation n stack) =
  run fuel rest (readFirst operation (suc n) stack)
run (suc fuel) (false ∷ rest) (readFirst operation n stack) =
  run fuel rest (readSecond operation n zero stack)
run (suc fuel) (true ∷ rest) (readSecond operation first n stack) =
  run fuel rest (readSecond operation first (suc n) stack)
run (suc fuel) (false ∷ rest) (readSecond operation first n stack) =
  run fuel rest (wantProgram (push (twoInstr operation first n) stack))

-- The three invalid instruction tags have an explicit, total interpretation.

invalid101 : (fuel : ℕ) (rest : List Bool) (stack : ProgramStack) →
  run (suc fuel) (true ∷ rest) (tag3 true false stack) ≡
  run fuel rest (wantProgram (push halt stack))
invalid101 fuel rest stack = refl

invalid110 : (fuel : ℕ) (rest : List Bool) (stack : ProgramStack) →
  run (suc fuel) (false ∷ rest) (tag3 true true stack) ≡
  run fuel rest (wantProgram (push halt stack))
invalid110 fuel rest stack = refl

invalid111 : (fuel : ℕ) (rest : List Bool) (stack : ProgramStack) →
  run (suc fuel) (true ∷ rest) (tag3 true true stack) ≡
  run fuel rest (wantProgram (push halt stack))
invalid111 fuel rest stack = refl

------------------------------------------------------------------------
-- Parser correctness for unary parameters, instructions and whole programs.

unary-one :
  (m k : ℕ) (operation : OneOp) (stack : ProgramStack)
  (rest : List Bool) (fuel : ℕ) →
  run (suc (m + fuel)) (unary m ++ rest) (readOne operation k stack) ≡
  run fuel rest (wantProgram (push (oneInstr operation (k + m)) stack))
unary-one zero k operation stack rest fuel =
  cong
    (λ value →
      run fuel rest (wantProgram (push (oneInstr operation value) stack)))
    (sym (+-zero k))
unary-one (suc m) k operation stack rest fuel =
  unary-one m (suc k) operation stack rest fuel
  ∙ cong
      (λ value →
        run fuel rest (wantProgram (push (oneInstr operation value) stack)))
      (sym (+-suc k m))

unary-first :
  (m k : ℕ) (operation : TwoOp) (stack : ProgramStack)
  (rest : List Bool) (fuel : ℕ) →
  run (suc (m + fuel)) (unary m ++ rest) (readFirst operation k stack) ≡
  run fuel rest (readSecond operation (k + m) zero stack)
unary-first zero k operation stack rest fuel =
  cong
    (λ value → run fuel rest (readSecond operation value zero stack))
    (sym (+-zero k))
unary-first (suc m) k operation stack rest fuel =
  unary-first m (suc k) operation stack rest fuel
  ∙ cong
      (λ value → run fuel rest (readSecond operation value zero stack))
      (sym (+-suc k m))

unary-second :
  (m k first : ℕ) (operation : TwoOp) (stack : ProgramStack)
  (rest : List Bool) (fuel : ℕ) →
  run (suc (m + fuel)) (unary m ++ rest)
      (readSecond operation first k stack) ≡
  run fuel rest
      (wantProgram (push (twoInstr operation first (k + m)) stack))
unary-second zero k first operation stack rest fuel =
  cong
    (λ value →
      run fuel rest
        (wantProgram (push (twoInstr operation first value) stack)))
    (sym (+-zero k))
unary-second (suc m) k first operation stack rest fuel =
  unary-second m (suc k) first operation stack rest fuel
  ∙ cong
      (λ value →
        run fuel rest
          (wantProgram (push (twoInstr operation first value) stack)))
      (sym (+-suc k m))

parseTwo :
  (onZero onSuc : ℕ) (operation : TwoOp) (stack : ProgramStack)
  (rest : List Bool) (fuel : ℕ) →
  run (LEN (unary onZero ++ unary onSuc) + fuel)
      ((unary onZero ++ unary onSuc) ++ rest)
      (readFirst operation zero stack) ≡
  run fuel rest
      (wantProgram (push (twoInstr operation onZero onSuc) stack))
parseTwo onZero onSuc operation stack rest fuel =
  bitsStep
  ∙ fuelStep
  ∙ unary-first onZero zero operation stack
      (unary onSuc ++ rest) (suc (onSuc + fuel))
  ∙ unary-second onSuc zero onZero operation stack rest fuel
  where
    associatedBits : List Bool
    associatedBits = unary onZero ++ (unary onSuc ++ rest)

    bitsStep :
      run (LEN (unary onZero ++ unary onSuc) + fuel)
          ((unary onZero ++ unary onSuc) ++ rest)
          (readFirst operation zero stack) ≡
      run (LEN (unary onZero ++ unary onSuc) + fuel)
          associatedBits (readFirst operation zero stack)
    bitsStep = cong
      (λ bits →
        run (LEN (unary onZero ++ unary onSuc) + fuel) bits
            (readFirst operation zero stack))
      (++-assoc (unary onZero) (unary onSuc) rest)

    fuelEquation :
      LEN (unary onZero ++ unary onSuc) + fuel ≡
      suc (onZero + suc (onSuc + fuel))
    fuelEquation =
      cong (λ length → length + fuel)
        (LEN-++ (unary onZero) (unary onSuc))
      ∙ +-assoc (LEN (unary onZero)) (LEN (unary onSuc)) fuel
      ∙ cong (λ length → length + (LEN (unary onSuc) + fuel))
          (LEN-unary onZero)
      ∙ cong (λ length → suc onZero + (length + fuel))
          (LEN-unary onSuc)

    fuelStep :
      run (LEN (unary onZero ++ unary onSuc) + fuel)
          associatedBits (readFirst operation zero stack) ≡
      run (suc (onZero + suc (onSuc + fuel)))
          associatedBits (readFirst operation zero stack)
    fuelStep = cong
      (λ amount → run amount associatedBits (readFirst operation zero stack))
      fuelEquation

parseInstr :
  (instruction : Instr) (stack : ProgramStack)
  (rest : List Bool) (fuel : ℕ) →
  run (LEN (bitsInstr instruction) + fuel)
      (bitsInstr instruction ++ rest) (tag1 stack) ≡
  run fuel rest (wantProgram (push instruction stack))
parseInstr halt stack rest fuel = refl
parseInstr (inc0 next) stack rest fuel =
  cong
    (λ amount → run amount (unary next ++ rest)
      (readOne doInc0 zero stack))
    (cong (λ length → length + fuel) (LEN-unary next))
  ∙ unary-one next zero doInc0 stack rest fuel
parseInstr (inc1 next) stack rest fuel =
  cong
    (λ amount → run amount (unary next ++ rest)
      (readOne doInc1 zero stack))
    (cong (λ length → length + fuel) (LEN-unary next))
  ∙ unary-one next zero doInc1 stack rest fuel
parseInstr (dec0 onZero onSuc) stack rest fuel =
  parseTwo onZero onSuc doDec0 stack rest fuel
parseInstr (dec1 onZero onSuc) stack rest fuel =
  parseTwo onZero onSuc doDec1 stack rest fuel

parseProgram :
  (code : ProgramCode) (stack : ProgramStack)
  (rest : List Bool) (fuel : ℕ) →
  run (LEN (bitsProgram code) + fuel)
      (bitsProgram code ++ rest) (wantProgram stack) ≡
  result (closeProgram stack code) rest
parseProgram pcNil stack rest fuel = refl
parseProgram (pcCons instruction code) stack rest fuel =
  bitsStep
  ∙ fuelStep
  ∙ parseInstr instruction stack (bitsProgram code ++ rest)
      (LEN (bitsProgram code) + fuel)
  ∙ parseProgram code (push instruction stack) rest fuel
  where
    associatedBits : List Bool
    associatedBits = bitsInstr instruction ++ (bitsProgram code ++ rest)

    bitsStep :
      run (LEN (bitsInstr instruction ++ bitsProgram code) + fuel)
          ((bitsInstr instruction ++ bitsProgram code) ++ rest)
          (tag1 stack) ≡
      run (LEN (bitsInstr instruction ++ bitsProgram code) + fuel)
          associatedBits (tag1 stack)
    bitsStep = cong
      (λ bits →
        run (LEN (bitsInstr instruction ++ bitsProgram code) + fuel)
            bits (tag1 stack))
      (++-assoc (bitsInstr instruction) (bitsProgram code) rest)

    fuelEquation :
      LEN (bitsInstr instruction ++ bitsProgram code) + fuel ≡
      LEN (bitsInstr instruction) + (LEN (bitsProgram code) + fuel)
    fuelEquation =
      cong (λ length → length + fuel)
        (LEN-++ (bitsInstr instruction) (bitsProgram code))
      ∙ +-assoc (LEN (bitsInstr instruction)) (LEN (bitsProgram code)) fuel

    fuelStep :
      run (LEN (bitsInstr instruction ++ bitsProgram code) + fuel)
          associatedBits (tag1 stack) ≡
      run (LEN (bitsInstr instruction) + (LEN (bitsProgram code) + fuel))
          associatedBits (tag1 stack)
    fuelStep = cong (λ amount → run amount associatedBits (tag1 stack)) fuelEquation

------------------------------------------------------------------------
-- C-195/C-196: ℕ coding, total decoding, round trip and injectivity.

encodeNat : ProgramCode → ℕ
encodeNat code = codeBits (bitsProgram code)

decodeNat : ℕ → ProgramCode
decodeNat code = rCode (run code (unbits code code) (wantProgram ε))

decodeNat-zero : decodeNat zero ≡ pcNil
decodeNat-zero = refl

-- A concrete natural number whose bit stream contains one program-table
-- entry with the invalid instruction tag 101, followed by the table
-- terminator.  The declared invalid-tag policy turns that entry into halt.

invalid101Bits : List Bool
invalid101Bits = true ∷ true ∷ false ∷ true ∷ false ∷ []

invalid101Nat : ℕ
invalid101Nat = codeBits invalid101Bits

decodeNat-invalid101 : decodeNat invalid101Nat ≡ pcCons halt pcNil
decodeNat-invalid101 = refl

encodeNat-bound : (code : ProgramCode) → LEN (bitsProgram code) ≤′ encodeNat code
encodeNat-bound code =
  ≤′-trans (≤′-suc (LEN (bitsProgram code)))
           (codeBits-dominates (bitsProgram code))

decodeNat-encodeNat : (code : ProgramCode) → decodeNat (encodeNat code) ≡ code
decodeNat-encodeNat code = bitsStep ∙ fuelStep
  where
    bits : List Bool
    bits = bitsProgram code

    split : Σ′ ℕ (λ slack → encodeNat code ≡ LEN bits + slack)
    split = ≤′-split (encodeNat-bound code)

    slack : ℕ
    slack = fst′ split

    fuelEquation : encodeNat code ≡ LEN bits + slack
    fuelEquation = snd′ split

    junk : List Bool
    junk = unbits slack (halfs (LEN bits) (encodeNat code))

    bitEquation : unbits (encodeNat code) (encodeNat code) ≡ bits ++ junk
    bitEquation = first ∙ second
      where
        first :
          unbits (encodeNat code) (encodeNat code) ≡
          unbits (LEN bits) (encodeNat code) ++ junk
        first = subst′
          (λ fuel →
            unbits fuel (encodeNat code) ≡
            unbits (LEN bits) (encodeNat code) ++ junk)
          (sym fuelEquation)
          (unbits-split (LEN bits) slack (encodeNat code))

        second :
          unbits (LEN bits) (encodeNat code) ++ junk ≡ bits ++ junk
        second = cong (λ prefix → prefix ++ junk) (unbits-code bits)

    bitsStep :
      rCode (run (encodeNat code) (unbits (encodeNat code) (encodeNat code))
                 (wantProgram ε)) ≡
      rCode (run (encodeNat code) (bits ++ junk) (wantProgram ε))
    bitsStep = cong
      (λ input → rCode (run (encodeNat code) input (wantProgram ε)))
      bitEquation

    parsed : rCode (run (LEN bits + slack) (bits ++ junk) (wantProgram ε)) ≡ code
    parsed = cong rCode (parseProgram code ε junk slack)

    fuelStep :
      rCode (run (encodeNat code) (bits ++ junk) (wantProgram ε)) ≡ code
    fuelStep = subst′
      (λ fuel → rCode (run fuel (bits ++ junk) (wantProgram ε)) ≡ code)
      (sym fuelEquation) parsed

encodeNat-injective :
  (left right : ProgramCode) → encodeNat left ≡ encodeNat right → left ≡ right
encodeNat-injective left right equality =
  sym (decodeNat-encodeNat left)
  ∙ cong decodeNat equality
  ∙ decodeNat-encodeNat right

decodeNat-surjective :
  (code : ProgramCode) → Σ′ ℕ (λ number → decodeNat number ≡ code)
decodeNat-surjective code = encodeNat code , decodeNat-encodeNat code

-- An instruction is encoded as a one-entry program.  The decoder is total:
-- malformed or empty program codes yield halt, while image codes round-trip.

headInstr : ProgramCode → Instr
headInstr pcNil = halt
headInstr (pcCons instruction rest) = instruction

encodeInstrNat : Instr → ℕ
encodeInstrNat instruction = encodeNat (pcCons instruction pcNil)

decodeInstrNat : ℕ → Instr
decodeInstrNat code = headInstr (decodeNat code)

decodeInstrNat-encodeInstrNat :
  (instruction : Instr) →
  decodeInstrNat (encodeInstrNat instruction) ≡ instruction
decodeInstrNat-encodeInstrNat instruction =
  cong headInstr (decodeNat-encodeNat (pcCons instruction pcNil))

encodeInstrNat-injective :
  (left right : Instr) →
  encodeInstrNat left ≡ encodeInstrNat right → left ≡ right
encodeInstrNat-injective left right equality =
  sym (decodeInstrNat-encodeInstrNat left)
  ∙ cong decodeInstrNat equality
  ∙ decodeInstrNat-encodeInstrNat right

------------------------------------------------------------------------
-- C-197/C-198: the numeric evaluator agrees on the image and preserves
-- the existing positive and negative controls.

runNat : ℕ → ℕ → Config → Config
runNat fuel code state = runFor fuel (decodeNat code) state

runNat-on-image :
  (fuel : ℕ) (code : ProgramCode) (state : Config) →
  runNat fuel (encodeNat code) state ≡ runFor fuel code state
runNat-on-image fuel code state =
  cong (λ decoded → runFor fuel decoded state) (decodeNat-encodeNat code)

finalNat : ℕ → ℕ → Config → Bool
finalNat fuel code state = finalAt fuel (decodeNat code) state

finalNat-on-image :
  (fuel : ℕ) (code : ProgramCode) (state : Config) →
  finalNat fuel (encodeNat code) state ≡ finalAt fuel code state
finalNat-on-image fuel code state =
  cong (λ decoded → finalAt fuel decoded state) (decodeNat-encodeNat code)

haltsWithinNat : ℕ → ℕ → Config → Bool
haltsWithinNat fuel code state = haltsWithin fuel (decodeNat code) state

haltsWithinNat-on-image :
  (fuel : ℕ) (code : ProgramCode) (state : Config) →
  haltsWithinNat fuel (encodeNat code) state ≡ haltsWithin fuel code state
haltsWithinNat-on-image fuel code state =
  cong (λ decoded → haltsWithin fuel decoded state) (decodeNat-encodeNat code)

haltNat-within : (fuel : ℕ) →
  haltsWithinNat fuel (encodeNat haltCode) initial ≡ true
haltNat-within fuel =
  haltsWithinNat-on-image fuel haltCode initial ∙ haltCode-within fuel

loopNat-not-final : (fuel : ℕ) →
  finalNat fuel (encodeNat loopCode) initial ≡ false
loopNat-not-final fuel =
  finalNat-on-image fuel loopCode initial ∙ loopCode-not-final fuel

loopNat-never-within : (fuel : ℕ) →
  haltsWithinNat fuel (encodeNat loopCode) initial ≡ false
loopNat-never-within fuel =
  haltsWithinNat-on-image fuel loopCode initial ∙ loopCode-never-within fuel
