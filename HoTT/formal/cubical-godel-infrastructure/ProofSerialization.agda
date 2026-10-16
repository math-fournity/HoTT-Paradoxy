{-# OPTIONS --cubical --safe --guardedness #-}

module ProofSerialization where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool ; false ; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty as Empty
open import MiniProofChecker

infixr 5 _∷_

data List (A : Type) : Type where
  [] : List A
  _∷_ : A → List A → List A

data Maybe (A : Type) : Type where
  nothing : Maybe A
  just : A → Maybe A

data Token : Type where
  tokK : Fml → Fml → Token
  tokS : Fml → Fml → Fml → Token
  tokMp : Fml → Fml → Token

emit : RawProof → List Token → List Token
emit (rawK φ ψ) rest = tokK φ ψ ∷ rest
emit (rawS φ ψ χ) rest = tokS φ ψ χ ∷ rest
emit (rawMp φ ψ p q) rest = emit p (emit q (tokMp φ ψ ∷ rest))

serialize : RawProof → List Token
serialize p = emit p []

Stack : Type
Stack = List RawProof

stepToken : Token → Stack → Maybe Stack
stepToken (tokK φ ψ) stack = just (rawK φ ψ ∷ stack)
stepToken (tokS φ ψ χ) stack = just (rawS φ ψ χ ∷ stack)
stepToken (tokMp φ ψ) (q ∷ p ∷ stack) = just (rawMp φ ψ p q ∷ stack)
stepToken (tokMp φ ψ) _ = nothing

run : List Token → Stack → Maybe Stack
run [] stack = just stack
run (tok ∷ toks) stack with stepToken tok stack
... | nothing = nothing
... | just stack' = run toks stack'

run-emit : (p : RawProof) (rest : List Token) (stack : Stack)
         → run (emit p rest) stack ≡ run rest (p ∷ stack)
run-emit (rawK φ ψ) rest stack = refl
run-emit (rawS φ ψ χ) rest stack = refl
run-emit (rawMp φ ψ p q) rest stack =
  run-emit p (emit q (tokMp φ ψ ∷ rest)) stack
  ∙ run-emit q (tokMp φ ψ ∷ rest) (p ∷ stack)

finish : Maybe Stack → Maybe RawProof
finish (just (p ∷ [])) = just p
finish _ = nothing

decode : List Token → Maybe RawProof
decode toks = finish (run toks [])

decode-serialize : (p : RawProof) → decode (serialize p) ≡ just p
decode-serialize p = cong finish (run-emit p [] [])

checkDecoded : Maybe RawProof → Fml → Bool
checkDecoded nothing φ = false
checkDecoded (just p) φ = checkAgainst p φ

checkSerialized : List Token → Fml → Bool
checkSerialized code φ = checkDecoded (decode code) φ

checkSerialized-serialize : (p : RawProof) (φ : Fml)
                          → checkSerialized (serialize p) φ ≡ checkAgainst p φ
checkSerialized-serialize p φ =
  cong (λ result → checkDecoded result φ) (decode-serialize p)

checkSerialized-sound : (code : List Token) (φ : Fml)
                      → checkSerialized code φ ≡ true → ⊢ φ
checkSerialized-sound code φ ok with decode code
... | nothing = Empty.rec (false≢true ok)
... | just p = checkAgainst-sound p φ ok

SerializedChecked : Fml → Type
SerializedChecked φ = Σ[ code ∈ List Token ] checkSerialized code φ ≡ true

derives→serialized : {φ : Fml} → ⊢ φ → SerializedChecked φ
derives→serialized {φ} d =
  serialize (erase d) ,
  (checkSerialized-serialize (erase d) φ ∙ checkAgainst-erase d)

serialized→derives : {φ : Fml} → SerializedChecked φ → ⊢ φ
serialized→derives {φ} (code , ok) = checkSerialized-sound code φ ok

positiveCode : List Token
positiveCode = serialize kRaw

positiveCode-accepted :
  checkSerialized positiveCode (zeroAtom ⇒ (oneAtom ⇒ zeroAtom)) ≡ true
positiveCode-accepted =
  checkSerialized-serialize kRaw (zeroAtom ⇒ (oneAtom ⇒ zeroAtom))
  ∙ kRaw-checks

negativeCode : List Token
negativeCode = serialize badMp

negativeCode-rejected : checkSerialized negativeCode oneAtom ≡ false
negativeCode-rejected = refl
