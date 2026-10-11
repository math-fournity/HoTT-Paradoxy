{-# OPTIONS --cubical --safe --guardedness #-}

module NatProofCode where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ ; zero ; suc ; _+_)
open import Cubical.Data.Bool.Base using (Bool ; false ; true)
open import Agda.Builtin.Equality renaming (_≡_ to _≡b_; refl to reflb)
open import MiniProofChecker
import ProofSerialization as PS
import FormulaBitCode as FB
import ProofBitCode as PB
open PB.ParsedCount using (count ; countRest)
open PB.ParsedTokens using (tokens ; tokensRest)

------------------------------------------------------------------------
-- Prefix stability of the finite proof-bit decoder.

emitToken-append : (tok : PS.Token) (xs ys : PS.List Bool)
                 → PB.emitToken tok (xs FB.++ ys)
                 ≡b PB.emitToken tok xs FB.++ ys
emitToken-append (PS.tokK φ ψ) xs ys =
  FB.congb (λ zs → false PS.∷ false PS.∷ zs)
    (FB.transb
      (FB.congb (λ zs → FB.bitsF φ FB.++ zs)
        (FB.symb (FB.append-assoc (FB.bitsF ψ) xs ys)))
      (FB.symb
        (FB.append-assoc (FB.bitsF φ) (FB.bitsF ψ FB.++ xs) ys)))
emitToken-append (PS.tokS φ ψ χ) xs ys =
  FB.congb (λ zs → false PS.∷ true PS.∷ zs)
    (FB.transb
      (FB.congb (λ zs → FB.bitsF φ FB.++ (FB.bitsF ψ FB.++ zs))
        (FB.symb (FB.append-assoc (FB.bitsF χ) xs ys)))
      (FB.transb
        (FB.congb (λ zs → FB.bitsF φ FB.++ zs)
          (FB.symb
            (FB.append-assoc (FB.bitsF ψ) (FB.bitsF χ FB.++ xs) ys)))
        (FB.symb
          (FB.append-assoc (FB.bitsF φ)
            (FB.bitsF ψ FB.++ (FB.bitsF χ FB.++ xs)) ys))))
emitToken-append (PS.tokMp φ ψ) xs ys =
  FB.congb (λ zs → true PS.∷ false PS.∷ zs)
    (FB.transb
      (FB.congb (λ zs → FB.bitsF φ FB.++ zs)
        (FB.symb (FB.append-assoc (FB.bitsF ψ) xs ys)))
      (FB.symb
        (FB.append-assoc (FB.bitsF φ) (FB.bitsF ψ FB.++ xs) ys)))

emitTokens-append : (toks : PS.List PS.Token) (rest : PS.List Bool)
                  → PB.emitTokens toks PS.[] FB.++ rest
                  ≡b PB.emitTokens toks rest
emitTokens-append PS.[] rest = reflb
emitTokens-append (tok PS.∷ toks) rest =
  FB.transb
    (FB.symb (emitToken-append tok (PB.emitTokens toks PS.[]) rest))
    (FB.congb (PB.emitToken tok) (emitTokens-append toks rest))

tokenListBits-append : (toks : PS.List PS.Token) (rest : PS.List Bool)
                     → PB.tokenListBits toks FB.++ rest
                     ≡b FB.unary (PB.countTokens toks)
                         FB.++ PB.emitTokens toks rest
tokenListBits-append toks rest
  rewrite FB.append-assoc (FB.unary (PB.countTokens toks))
            (PB.emitTokens toks PS.[]) rest
        | emitTokens-append toks rest = reflb

decodeTokenList-prefix : (toks : PS.List PS.Token) (rest : PS.List Bool)
                       → PB.decodeTokenList (PB.tokenListBits toks FB.++ rest)
                       ≡b PS.just (PB.decodedTokenList toks rest)
decodeTokenList-prefix toks rest rewrite tokenListBits-append toks rest =
  FB.transb
    (FB.congb
      (λ result →
        PB.bindM result λ header →
        PB.bindM (PB.parseNTokens (count header) (countRest header)) λ body →
        PS.just (PB.decodedTokenList (tokens body) (tokensRest body)))
      (PB.parseCount-roundtrip (PB.countTokens toks) (PB.emitTokens toks rest)))
    (FB.congb
      (λ result →
        PB.bindM result λ body →
        PS.just (PB.decodedTokenList (tokens body) (tokensRest body)))
      (PB.parseTokens-emit toks rest))

decodeProofBits-prefix : (p : RawProof) (rest : PS.List Bool)
                       → PB.decodeProofBits (PB.proofBits p FB.++ rest)
                       ≡ PS.just p
decodeProofBits-prefix p rest =
  cong PB.decodeProofBody
    (PB.builtin→Path (decodeTokenList-prefix (PS.serialize p) rest))
  ∙ PS.decode-serialize p

checkProofBits-prefix : (p : RawProof) (rest : PS.List Bool) (φ : Fml)
                      → PB.checkProofBits (PB.proofBits p FB.++ rest) φ
                      ≡ checkAgainst p φ
checkProofBits-prefix p rest φ =
  cong (λ result → PB.checkProofBitsBody result φ)
       (decodeProofBits-prefix p rest)

------------------------------------------------------------------------
-- Packing finite Bool strings into natural numbers.

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

pack : Bool → ℕ → ℕ
pack false c = twice c
pack true c = suc (twice c)

codeBits : PS.List Bool → ℕ
codeBits PS.[] = suc zero
codeBits (b PS.∷ bs) = pack b (codeBits bs)

unbits : ℕ → ℕ → PS.List Bool
unbits zero c = PS.[]
unbits (suc k) c = parity c PS.∷ unbits k (half c)

parity-code : (b : Bool) (c : ℕ) → parity (pack b c) ≡ b
parity-code false c = parity-twice c
parity-code true c = parity-suc-twice c

half-code : (b : Bool) (c : ℕ) → half (pack b c) ≡ c
half-code false c = half-twice c
half-code true c = half-suc-twice c

unbits-code : (bs : PS.List Bool) → unbits (FB.LEN bs) (codeBits bs) ≡ bs
unbits-code PS.[] = refl
unbits-code (b PS.∷ bs) =
  cong (λ x → parity (pack b c) PS.∷ unbits (FB.LEN bs) x) (half-code b c)
  ∙ cong (λ y → y PS.∷ unbits (FB.LEN bs) c) (parity-code b c)
  ∙ cong (λ xs → b PS.∷ xs) (unbits-code bs)
  where
  c : ℕ
  c = codeBits bs

data _≤_ : ℕ → ℕ → Type where
  z≤n : {n : ℕ} → zero ≤ n
  s≤s : {m n : ℕ} → m ≤ n → suc m ≤ suc n

≤-refl : (n : ℕ) → n ≤ n
≤-refl zero = z≤n
≤-refl (suc n) = s≤s (≤-refl n)

≤-suc : (n : ℕ) → n ≤ suc n
≤-suc zero = z≤n
≤-suc (suc n) = s≤s (≤-suc n)

≤-trans : {i j k : ℕ} → i ≤ j → j ≤ k → i ≤ k
≤-trans z≤n q = z≤n
≤-trans (s≤s p) (s≤s q) = s≤s (≤-trans p q)

n≤twice : (n : ℕ) → n ≤ twice n
n≤twice zero = z≤n
n≤twice (suc n) = s≤s (≤-trans (n≤twice n) (≤-suc (twice n)))

suc≤pack : (b : Bool) (c : ℕ) → suc zero ≤ c → suc c ≤ pack b c
suc≤pack false (suc c) p = s≤s (s≤s (n≤twice c))
suc≤pack true (suc c) p =
  s≤s (s≤s (≤-trans (n≤twice c) (≤-suc (twice c))))

codeBits-dominates : (bs : PS.List Bool) → suc (FB.LEN bs) ≤ codeBits bs
codeBits-dominates PS.[] = s≤s z≤n
codeBits-dominates (b PS.∷ bs) =
  ≤-trans (s≤s (codeBits-dominates bs))
          (suc≤pack b (codeBits bs)
            (≤-trans (s≤s z≤n) (codeBits-dominates bs)))

≤-split : {n m : ℕ} → n ≤ m → Σ[ k ∈ ℕ ] m ≡ n + k
≤-split z≤n = _ , refl
≤-split (s≤s p) with ≤-split p
... | k , eq = k , cong suc eq

halfs : ℕ → ℕ → ℕ
halfs zero c = c
halfs (suc k) c = halfs k (half c)

unbits-split : (i j c : ℕ)
             → unbits (i + j) c
             ≡ FB._++_ (unbits i c) (unbits j (halfs i c))
unbits-split zero j c = refl
unbits-split (suc i) j c =
  cong (λ xs → parity c PS.∷ xs) (unbits-split i j (half c))

------------------------------------------------------------------------
-- Natural-number proof code, total decoder and checker.

codeProof : RawProof → ℕ
codeProof p = codeBits (PB.proofBits p)

decodeProofNat : ℕ → PS.Maybe RawProof
decodeProofNat c = PB.decodeProofBits (unbits c c)

codeProof-roundtrip : (p : RawProof) → decodeProofNat (codeProof p) ≡ PS.just p
codeProof-roundtrip p =
  cong PB.decodeProofBits bits-with-junk
  ∙ decodeProofBits-prefix p junk
  where
  bits : PS.List Bool
  bits = PB.proofBits p

  c : ℕ
  c = codeBits bits

  length-bound : FB.LEN bits ≤ c
  length-bound = ≤-trans (≤-suc (FB.LEN bits)) (codeBits-dominates bits)

  split : Σ[ k ∈ ℕ ] c ≡ FB.LEN bits + k
  split = ≤-split length-bound

  k : ℕ
  k = fst split

  fuel-eq : c ≡ FB.LEN bits + k
  fuel-eq = snd split

  junk : PS.List Bool
  junk = unbits k (halfs (FB.LEN bits) c)

  bits-with-junk : unbits c c ≡ FB._++_ bits junk
  bits-with-junk =
    subst
      (λ fuel → unbits fuel c ≡ FB._++_ (unbits (FB.LEN bits) c) junk)
      (sym fuel-eq)
      (unbits-split (FB.LEN bits) k c)
    ∙ cong (λ xs → FB._++_ xs junk) (unbits-code bits)

fromMaybeProof : PS.Maybe RawProof → RawProof
fromMaybeProof PS.nothing = kRaw
fromMaybeProof (PS.just p) = p

codeProof-injective : (p q : RawProof) → codeProof p ≡ codeProof q → p ≡ q
codeProof-injective p q code-eq =
  sym (cong fromMaybeProof (codeProof-roundtrip p))
  ∙ cong (λ c → fromMaybeProof (decodeProofNat c)) code-eq
  ∙ cong fromMaybeProof (codeProof-roundtrip q)

checkProofNat : ℕ → Fml → Bool
checkProofNat c φ = PB.checkProofBits (unbits c c) φ

checkProofNat-code : (p : RawProof) (φ : Fml)
                   → checkProofNat (codeProof p) φ ≡ checkAgainst p φ
checkProofNat-code p φ =
  cong (λ bits → PB.checkProofBits bits φ) bits-with-junk
  ∙ checkProofBits-prefix p junk φ
  where
  bits : PS.List Bool
  bits = PB.proofBits p

  c : ℕ
  c = codeBits bits

  length-bound : FB.LEN bits ≤ c
  length-bound = ≤-trans (≤-suc (FB.LEN bits)) (codeBits-dominates bits)

  split : Σ[ k ∈ ℕ ] c ≡ FB.LEN bits + k
  split = ≤-split length-bound

  k : ℕ
  k = fst split

  fuel-eq : c ≡ FB.LEN bits + k
  fuel-eq = snd split

  junk : PS.List Bool
  junk = unbits k (halfs (FB.LEN bits) c)

  bits-with-junk : unbits c c ≡ FB._++_ bits junk
  bits-with-junk =
    subst
      (λ fuel → unbits fuel c ≡ FB._++_ (unbits (FB.LEN bits) c) junk)
      (sym fuel-eq)
      (unbits-split (FB.LEN bits) k c)
    ∙ cong (λ xs → FB._++_ xs junk) (unbits-code bits)

NatChecked : Fml → Type
NatChecked φ = Σ[ c ∈ ℕ ] checkProofNat c φ ≡ true

natChecked-sound : {φ : Fml} → NatChecked φ → ⊢ φ
natChecked-sound {φ} (c , ok) =
  PB.bitChecked-sound (unbits c c , ok)

derives→natChecked : {φ : Fml} → ⊢ φ → NatChecked φ
derives→natChecked {φ} d =
  codeProof (erase d) ,
  (checkProofNat-code (erase d) φ ∙ checkAgainst-erase d)

tinyK : RawProof
tinyK = rawK bot bot

tinyK-checks : checkAgainst tinyK (bot ⇒ (bot ⇒ bot)) ≡ true
tinyK-checks = refl

positiveNatCode : ℕ
positiveNatCode = codeProof tinyK

positiveNatCode-accepted :
  checkProofNat positiveNatCode (bot ⇒ (bot ⇒ bot)) ≡ true
positiveNatCode-accepted =
  checkProofNat-code tinyK (bot ⇒ (bot ⇒ bot)) ∙ tinyK-checks

negativeNatCode : ℕ
negativeNatCode = zero

negativeNatCode-rejected : checkProofNat negativeNatCode bot ≡ false
negativeNatCode-rejected = refl
