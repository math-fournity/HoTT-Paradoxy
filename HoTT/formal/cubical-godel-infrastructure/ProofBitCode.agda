{-# OPTIONS --cubical --safe --guardedness #-}

module ProofBitCode where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ ; zero ; suc)
open import Cubical.Data.Bool.Base using (Bool ; false ; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty as Empty
open import Agda.Builtin.Equality renaming (_≡_ to _≡b_; refl to reflb)
open import MiniProofChecker
import ProofSerialization as PS
import FormulaBitCode as FB

bindM : {A B : Type} → PS.Maybe A → (A → PS.Maybe B) → PS.Maybe B
bindM PS.nothing f = PS.nothing
bindM (PS.just x) f = f x

record ParsedFormula : Type where
  constructor parsedFormula
  field
    formula : Fml
    formulaRest : PS.List Bool

open ParsedFormula

acceptFormula : FB.Result → PS.Maybe ParsedFormula
acceptFormula (FB.res φ rest true) = PS.just (parsedFormula φ rest)
acceptFormula (FB.res φ rest false) = PS.nothing

parseFormula : PS.List Bool → PS.Maybe ParsedFormula
parseFormula bits = acceptFormula (FB.parsePrefix bits)

parseFormula-roundtrip : (φ : Fml) (rest : PS.List Bool)
                       → parseFormula (FB.bitsF φ FB.++ rest)
                       ≡b PS.just (parsedFormula φ rest)
parseFormula-roundtrip φ rest =
  FB.congb acceptFormula (FB.parsePrefix-roundtrip φ rest)

record ParsedToken : Type where
  constructor parsedToken
  field
    token : PS.Token
    tokenRest : PS.List Bool

open ParsedToken

emitToken : PS.Token → PS.List Bool → PS.List Bool
emitToken (PS.tokK φ ψ) rest =
  false PS.∷ false PS.∷ (FB.bitsF φ FB.++ (FB.bitsF ψ FB.++ rest))
emitToken (PS.tokS φ ψ χ) rest =
  false PS.∷ true PS.∷
    (FB.bitsF φ FB.++ (FB.bitsF ψ FB.++ (FB.bitsF χ FB.++ rest)))
emitToken (PS.tokMp φ ψ) rest =
  true PS.∷ false PS.∷ (FB.bitsF φ FB.++ (FB.bitsF ψ FB.++ rest))

parseToken : PS.List Bool → PS.Maybe ParsedToken
parseToken PS.[] = PS.nothing
parseToken (false PS.∷ PS.[]) = PS.nothing
parseToken (true PS.∷ PS.[]) = PS.nothing
parseToken (false PS.∷ false PS.∷ rest) =
  bindM (parseFormula rest) λ first →
  bindM (parseFormula (formulaRest first)) λ second →
  PS.just (parsedToken (PS.tokK (formula first) (formula second))
                       (formulaRest second))
parseToken (false PS.∷ true PS.∷ rest) =
  bindM (parseFormula rest) λ first →
  bindM (parseFormula (formulaRest first)) λ second →
  bindM (parseFormula (formulaRest second)) λ third →
  PS.just (parsedToken (PS.tokS (formula first) (formula second) (formula third))
                       (formulaRest third))
parseToken (true PS.∷ false PS.∷ rest) =
  bindM (parseFormula rest) λ first →
  bindM (parseFormula (formulaRest first)) λ second →
  PS.just (parsedToken (PS.tokMp (formula first) (formula second))
                       (formulaRest second))
parseToken (true PS.∷ true PS.∷ rest) = PS.nothing

parseToken-emit : (tok : PS.Token) (rest : PS.List Bool)
                → parseToken (emitToken tok rest)
                ≡b PS.just (parsedToken tok rest)
parseToken-emit (PS.tokK φ ψ) rest =
  FB.transb
    (FB.congb
      (λ result →
        bindM result λ first →
        bindM (parseFormula (formulaRest first)) λ second →
        PS.just (parsedToken (PS.tokK (formula first) (formula second))
                             (formulaRest second)))
      (parseFormula-roundtrip φ (FB.bitsF ψ FB.++ rest)))
    (FB.congb
      (λ result →
        bindM result λ second →
        PS.just (parsedToken (PS.tokK φ (formula second))
                             (formulaRest second)))
      (parseFormula-roundtrip ψ rest))
parseToken-emit (PS.tokS φ ψ χ) rest =
  FB.transb
    (FB.congb
      (λ result →
        bindM result λ first →
        bindM (parseFormula (formulaRest first)) λ second →
        bindM (parseFormula (formulaRest second)) λ third →
        PS.just (parsedToken (PS.tokS (formula first) (formula second) (formula third))
                             (formulaRest third)))
      (parseFormula-roundtrip φ
        (FB.bitsF ψ FB.++ (FB.bitsF χ FB.++ rest))))
    (FB.transb
      (FB.congb
        (λ result →
          bindM result λ second →
          bindM (parseFormula (formulaRest second)) λ third →
          PS.just (parsedToken (PS.tokS φ (formula second) (formula third))
                               (formulaRest third)))
        (parseFormula-roundtrip ψ (FB.bitsF χ FB.++ rest)))
      (FB.congb
        (λ result →
          bindM result λ third →
          PS.just (parsedToken (PS.tokS φ ψ (formula third))
                               (formulaRest third)))
        (parseFormula-roundtrip χ rest)))
parseToken-emit (PS.tokMp φ ψ) rest =
  FB.transb
    (FB.congb
      (λ result →
        bindM result λ first →
        bindM (parseFormula (formulaRest first)) λ second →
        PS.just (parsedToken (PS.tokMp (formula first) (formula second))
                             (formulaRest second)))
      (parseFormula-roundtrip φ (FB.bitsF ψ FB.++ rest)))
    (FB.congb
      (λ result →
        bindM result λ second →
        PS.just (parsedToken (PS.tokMp φ (formula second))
                             (formulaRest second)))
      (parseFormula-roundtrip ψ rest))

countTokens : PS.List PS.Token → ℕ
countTokens PS.[] = zero
countTokens (tok PS.∷ toks) = suc (countTokens toks)

emitTokens : PS.List PS.Token → PS.List Bool → PS.List Bool
emitTokens PS.[] rest = rest
emitTokens (tok PS.∷ toks) rest = emitToken tok (emitTokens toks rest)

record ParsedTokens : Type where
  constructor parsedTokens
  field
    tokens : PS.List PS.Token
    tokensRest : PS.List Bool

open ParsedTokens

parseNTokens : ℕ → PS.List Bool → PS.Maybe ParsedTokens
parseNTokens zero bits = PS.just (parsedTokens PS.[] bits)
parseNTokens (suc n) bits =
  bindM (parseToken bits) λ first →
  bindM (parseNTokens n (tokenRest first)) λ tail →
  PS.just (parsedTokens (token first PS.∷ tokens tail) (tokensRest tail))

parseTokens-emit : (toks : PS.List PS.Token) (rest : PS.List Bool)
                 → parseNTokens (countTokens toks) (emitTokens toks rest)
                 ≡b PS.just (parsedTokens toks rest)
parseTokens-emit PS.[] rest = reflb
parseTokens-emit (tok PS.∷ toks) rest =
  FB.transb
    (FB.congb
      (λ result →
        bindM result λ first →
        bindM (parseNTokens (countTokens toks) (tokenRest first)) λ tail →
        PS.just (parsedTokens (token first PS.∷ tokens tail) (tokensRest tail)))
      (parseToken-emit tok (emitTokens toks rest)))
    (FB.congb
      (λ result →
        bindM result λ tail →
        PS.just (parsedTokens (tok PS.∷ tokens tail) (tokensRest tail)))
      (parseTokens-emit toks rest))

record ParsedCount : Type where
  constructor parsedCount
  field
    count : ℕ
    countRest : PS.List Bool

open ParsedCount

parseCount : PS.List Bool → PS.Maybe ParsedCount
parseCount PS.[] = PS.nothing
parseCount (false PS.∷ rest) = PS.just (parsedCount zero rest)
parseCount (true PS.∷ rest) =
  bindM (parseCount rest) λ result →
  PS.just (parsedCount (suc (count result)) (countRest result))

parseCount-roundtrip : (n : ℕ) (rest : PS.List Bool)
                     → parseCount (FB.unary n FB.++ rest)
                     ≡b PS.just (parsedCount n rest)
parseCount-roundtrip zero rest = reflb
parseCount-roundtrip (suc n) rest =
  FB.congb
    (λ result →
      bindM result λ parsed →
      PS.just (parsedCount (suc (count parsed)) (countRest parsed)))
    (parseCount-roundtrip n rest)

record DecodedTokenList : Type where
  constructor decodedTokenList
  field
    decodedTokens : PS.List PS.Token
    decodedRest : PS.List Bool

open DecodedTokenList

decodeTokenList : PS.List Bool → PS.Maybe DecodedTokenList
decodeTokenList bits =
  bindM (parseCount bits) λ header →
  bindM (parseNTokens (count header) (countRest header)) λ body →
  PS.just (decodedTokenList (tokens body) (tokensRest body))

tokenListBits : PS.List PS.Token → PS.List Bool
tokenListBits toks = FB.unary (countTokens toks) FB.++ emitTokens toks PS.[]

decodeTokenList-roundtrip : (toks : PS.List PS.Token)
                          → decodeTokenList (tokenListBits toks)
                          ≡b PS.just (decodedTokenList toks PS.[])
decodeTokenList-roundtrip toks =
  FB.transb
    (FB.congb
      (λ result →
        bindM result λ header →
        bindM (parseNTokens (count header) (countRest header)) λ body →
        PS.just (decodedTokenList (tokens body) (tokensRest body)))
      (parseCount-roundtrip (countTokens toks) (emitTokens toks PS.[])))
    (FB.congb
      (λ result →
        bindM result λ body →
        PS.just (decodedTokenList (tokens body) (tokensRest body)))
      (parseTokens-emit toks PS.[]))

builtin→Path : {A : Type} {x y : A} → x ≡b y → x ≡ y
builtin→Path reflb = refl

decodeProofBody : PS.Maybe DecodedTokenList → PS.Maybe RawProof
decodeProofBody PS.nothing = PS.nothing
decodeProofBody (PS.just body) = PS.decode (decodedTokens body)

proofBits : RawProof → PS.List Bool
proofBits p = tokenListBits (PS.serialize p)

decodeProofBits : PS.List Bool → PS.Maybe RawProof
decodeProofBits bits = decodeProofBody (decodeTokenList bits)

decodeProofBits-roundtrip : (p : RawProof)
                          → decodeProofBits (proofBits p) ≡ PS.just p
decodeProofBits-roundtrip p =
  cong decodeProofBody
    (builtin→Path (decodeTokenList-roundtrip (PS.serialize p)))
  ∙ PS.decode-serialize p

checkProofBitsBody : PS.Maybe RawProof → Fml → Bool
checkProofBitsBody PS.nothing φ = false
checkProofBitsBody (PS.just p) φ = checkAgainst p φ

checkProofBits : PS.List Bool → Fml → Bool
checkProofBits bits φ = checkProofBitsBody (decodeProofBits bits) φ

checkProofBits-roundtrip : (p : RawProof) (φ : Fml)
                         → checkProofBits (proofBits p) φ ≡ checkAgainst p φ
checkProofBits-roundtrip p φ =
  cong (λ result → checkProofBitsBody result φ) (decodeProofBits-roundtrip p)

BitChecked : Fml → Type
BitChecked φ = Σ[ bits ∈ PS.List Bool ] checkProofBits bits φ ≡ true

bitChecked-sound : {φ : Fml} → BitChecked φ → ⊢ φ
bitChecked-sound {φ} (bits , ok) with decodeProofBits bits
... | PS.nothing = Empty.rec (false≢true ok)
... | PS.just p = checkAgainst-sound p φ ok

derives→bitChecked : {φ : Fml} → ⊢ φ → BitChecked φ
derives→bitChecked {φ} d =
  proofBits (erase d) ,
  (checkProofBits-roundtrip (erase d) φ ∙ checkAgainst-erase d)

positiveBits : PS.List Bool
positiveBits = proofBits kRaw

positiveBits-accepted :
  checkProofBits positiveBits (zeroAtom ⇒ (oneAtom ⇒ zeroAtom)) ≡ true
positiveBits-accepted =
  checkProofBits-roundtrip kRaw (zeroAtom ⇒ (oneAtom ⇒ zeroAtom))
  ∙ kRaw-checks

negativeBits : PS.List Bool
negativeBits = proofBits badMp

negativeBits-rejected : checkProofBits negativeBits oneAtom ≡ false
negativeBits-rejected = refl
