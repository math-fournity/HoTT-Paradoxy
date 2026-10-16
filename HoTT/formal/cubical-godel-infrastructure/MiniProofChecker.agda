{-# OPTIONS --cubical --safe --guardedness #-}

module MiniProofChecker where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ ; zero ; suc)
open import Cubical.Data.Bool.Base using (Bool ; false ; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty as Empty using (isProp⊥)
open import Cubical.HITs.PropositionalTruncation as PT

infixr 4 _⇒_

data Fml : Type where
  atom : ℕ → Fml
  bot : Fml
  _⇒_ : Fml → Fml → Fml

_and_ : Bool → Bool → Bool
true and b = b
false and b = false

and-left : (a b : Bool) → a and b ≡ true → a ≡ true
and-left true b p = refl
and-left false b p = Empty.rec (false≢true p)

and-right : (a b : Bool) → a and b ≡ true → b ≡ true
and-right true b p = p
and-right false b p = Empty.rec (false≢true p)

eqNat : ℕ → ℕ → Bool
eqNat zero zero = true
eqNat zero (suc n) = false
eqNat (suc m) zero = false
eqNat (suc m) (suc n) = eqNat m n

eqNat-refl : (n : ℕ) → eqNat n n ≡ true
eqNat-refl zero = refl
eqNat-refl (suc n) = eqNat-refl n

eqNat-sound : (m n : ℕ) → eqNat m n ≡ true → m ≡ n
eqNat-sound zero zero p = refl
eqNat-sound zero (suc n) p = Empty.rec (false≢true p)
eqNat-sound (suc m) zero p = Empty.rec (false≢true p)
eqNat-sound (suc m) (suc n) p = cong suc (eqNat-sound m n p)

eqF : Fml → Fml → Bool
eqF (atom m) (atom n) = eqNat m n
eqF bot bot = true
eqF (φ ⇒ ψ) (φ' ⇒ ψ') = eqF φ φ' and eqF ψ ψ'
eqF _ _ = false

eqF-refl : (φ : Fml) → eqF φ φ ≡ true
eqF-refl (atom n) = eqNat-refl n
eqF-refl bot = refl
eqF-refl (φ ⇒ ψ) = cong₂ _and_ (eqF-refl φ) (eqF-refl ψ)

eqF-sound : (φ ψ : Fml) → eqF φ ψ ≡ true → φ ≡ ψ
eqF-sound (atom m) (atom n) p = cong atom (eqNat-sound m n p)
eqF-sound (atom m) bot p = Empty.rec (false≢true p)
eqF-sound (atom m) (φ ⇒ ψ) p = Empty.rec (false≢true p)
eqF-sound bot (atom n) p = Empty.rec (false≢true p)
eqF-sound bot bot p = refl
eqF-sound bot (φ ⇒ ψ) p = Empty.rec (false≢true p)
eqF-sound (φ ⇒ ψ) (atom n) p = Empty.rec (false≢true p)
eqF-sound (φ ⇒ ψ) bot p = Empty.rec (false≢true p)
eqF-sound (φ ⇒ ψ) (φ' ⇒ ψ') p =
  cong₂ _⇒_
    (eqF-sound φ φ' (and-left (eqF φ φ') (eqF ψ ψ') p))
    (eqF-sound ψ ψ' (and-right (eqF φ φ') (eqF ψ ψ') p))

infix 3 ⊢_

data ⊢_ : Fml → Type where
  axK : (φ ψ : Fml) → ⊢ (φ ⇒ (ψ ⇒ φ))
  axS : (φ ψ χ : Fml) → ⊢ ((φ ⇒ (ψ ⇒ χ)) ⇒ ((φ ⇒ ψ) ⇒ (φ ⇒ χ)))
  mp : {φ ψ : Fml} → ⊢ (φ ⇒ ψ) → ⊢ φ → ⊢ ψ

data RawProof : Type where
  rawK : Fml → Fml → RawProof
  rawS : Fml → Fml → Fml → RawProof
  rawMp : Fml → Fml → RawProof → RawProof → RawProof

conclusion : RawProof → Fml
conclusion (rawK φ ψ) = φ ⇒ (ψ ⇒ φ)
conclusion (rawS φ ψ χ) = (φ ⇒ (ψ ⇒ χ)) ⇒ ((φ ⇒ ψ) ⇒ (φ ⇒ χ))
conclusion (rawMp φ ψ p q) = ψ

check : RawProof → Bool
check (rawK φ ψ) = true
check (rawS φ ψ χ) = true
check (rawMp φ ψ p q) =
  check p and
    (check q and
      (eqF (conclusion p) (φ ⇒ ψ) and
       eqF (conclusion q) φ))

transport⊢ : {φ ψ : Fml} → φ ≡ ψ → ⊢ φ → ⊢ ψ
transport⊢ p d = subst (λ χ → ⊢ χ) p d

check-sound : (p : RawProof) → check p ≡ true → ⊢ conclusion p
check-sound (rawK φ ψ) ok = axK φ ψ
check-sound (rawS φ ψ χ) ok = axS φ ψ χ
check-sound (rawMp φ ψ p q) ok =
  mp (transport⊢ p-conclusion (check-sound p p-checks))
     (transport⊢ q-conclusion (check-sound q q-checks))
  where
  p-checks : check p ≡ true
  p-checks = and-left (check p)
    (check q and
      (eqF (conclusion p) (φ ⇒ ψ) and eqF (conclusion q) φ)) ok

  tail-checks :
    check q and
      (eqF (conclusion p) (φ ⇒ ψ) and eqF (conclusion q) φ) ≡ true
  tail-checks = and-right (check p)
    (check q and
      (eqF (conclusion p) (φ ⇒ ψ) and eqF (conclusion q) φ)) ok

  q-checks : check q ≡ true
  q-checks = and-left (check q)
    (eqF (conclusion p) (φ ⇒ ψ) and eqF (conclusion q) φ) tail-checks

  equality-checks :
    eqF (conclusion p) (φ ⇒ ψ) and eqF (conclusion q) φ ≡ true
  equality-checks = and-right (check q)
    (eqF (conclusion p) (φ ⇒ ψ) and eqF (conclusion q) φ) tail-checks

  p-conclusion : conclusion p ≡ (φ ⇒ ψ)
  p-conclusion = eqF-sound (conclusion p) (φ ⇒ ψ)
    (and-left (eqF (conclusion p) (φ ⇒ ψ))
              (eqF (conclusion q) φ) equality-checks)

  q-conclusion : conclusion q ≡ φ
  q-conclusion = eqF-sound (conclusion q) φ
    (and-right (eqF (conclusion p) (φ ⇒ ψ))
               (eqF (conclusion q) φ) equality-checks)

erase : {φ : Fml} → ⊢ φ → RawProof
erase (axK φ ψ) = rawK φ ψ
erase (axS φ ψ χ) = rawS φ ψ χ
erase (mp {φ} {ψ} d e) = rawMp φ ψ (erase d) (erase e)

conclusion-erase : {φ : Fml} (d : ⊢ φ) → conclusion (erase d) ≡ φ
conclusion-erase (axK φ ψ) = refl
conclusion-erase (axS φ ψ χ) = refl
conclusion-erase (mp d e) = refl

check-erase : {φ : Fml} (d : ⊢ φ) → check (erase d) ≡ true
check-erase (axK φ ψ) = refl
check-erase (axS φ ψ χ) = refl
check-erase (mp {φ} {ψ} d e) =
  cong₂ _and_ (check-erase d)
    (cong₂ _and_ (check-erase e)
      (cong₂ _and_ p-equality q-equality))
  where
  p-equality : eqF (conclusion (erase d)) (φ ⇒ ψ) ≡ true
  p-equality = cong (λ χ → eqF χ (φ ⇒ ψ)) (conclusion-erase d)
             ∙ eqF-refl (φ ⇒ ψ)

  q-equality : eqF (conclusion (erase e)) φ ≡ true
  q-equality = cong (λ χ → eqF χ φ) (conclusion-erase e)
             ∙ eqF-refl φ

checkAgainst : RawProof → Fml → Bool
checkAgainst p φ = check p and eqF (conclusion p) φ

checkAgainst-sound : (p : RawProof) (φ : Fml)
                   → checkAgainst p φ ≡ true → ⊢ φ
checkAgainst-sound p φ ok =
  transport⊢ (eqF-sound (conclusion p) φ equality-checks)
             (check-sound p proof-checks)
  where
  proof-checks : check p ≡ true
  proof-checks = and-left (check p) (eqF (conclusion p) φ) ok

  equality-checks : eqF (conclusion p) φ ≡ true
  equality-checks = and-right (check p) (eqF (conclusion p) φ) ok

checkAgainst-erase : {φ : Fml} (d : ⊢ φ) → checkAgainst (erase d) φ ≡ true
checkAgainst-erase {φ} d = cong₂ _and_ (check-erase d) equality-checks
  where
  equality-checks : eqF (conclusion (erase d)) φ ≡ true
  equality-checks = cong (λ χ → eqF χ φ) (conclusion-erase d)
                  ∙ eqF-refl φ

Checked : Fml → Type
Checked φ = Σ[ p ∈ RawProof ] checkAgainst p φ ≡ true

derives→checked : {φ : Fml} → ⊢ φ → Checked φ
derives→checked d = erase d , checkAgainst-erase d

checked→derives : {φ : Fml} → Checked φ → ⊢ φ
checked→derives {φ} (p , ok) = checkAgainst-sound p φ ok

Provable : Fml → Type
Provable φ = ∥ Checked φ ∥₁

derives→provable : {φ : Fml} → ⊢ φ → Provable φ
derives→provable d = ∣ derives→checked d ∣₁

provable→mereDerives : {φ : Fml} → Provable φ → ∥ ⊢ φ ∥₁
provable→mereDerives = PT.rec squash₁ (λ checked → ∣ checked→derives checked ∣₁)

zeroAtom oneAtom : Fml
zeroAtom = atom zero
oneAtom = atom (suc zero)

kRaw : RawProof
kRaw = rawK zeroAtom oneAtom

kRaw-checks : checkAgainst kRaw (zeroAtom ⇒ (oneAtom ⇒ zeroAtom)) ≡ true
kRaw-checks = refl

badMp : RawProof
badMp = rawMp zeroAtom oneAtom kRaw kRaw

badMp-rejected : check badMp ≡ false
badMp-rejected = refl
