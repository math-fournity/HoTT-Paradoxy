{-# OPTIONS --safe --cubical --guardedness --two-level #-}
module FiniteCoverSearch where

-- C02: instantiate least-witness elimination with actual rational chain
-- certificates and return the original indices, plus real-cover evidence.
-- The bridge from an arbitrary original cover to a successful stage is
-- a separate obligation, not assumed to follow just from this module.
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Foundations.Function using (_∘_)
open import Cubical.Data.Nat using (ℕ; zero; suc; _+_)
open import Cubical.Data.List using (List; []; _∷_; _++_; map; length)
open import Cubical.Data.Sum using (inl; inr)
open import Cubical.Data.Sigma
open import Cubical.Data.Empty as Empty
open import Cubical.Data.Unit
open import Cubical.Relation.Nullary
open import Cubical.HITs.PropositionalTruncation using (∥_∥₁; ∣_∣₁; isPropPropTrunc)
import Cubical.HITs.PropositionalTruncation as PT
import Cubical.Data.Nat.Order.Recursive as N
open import IntervalCover

data Result (F : ℕ → Interval) : Type where
  failure : Result F
  found : (xs : List ℕ) → Cert F xs → Result F

Has : {F : ℕ → Interval} → Result F → Type
Has failure = ⊥
Has (found xs cert) = Unit

propHas : {F : ℕ → Interval} (r : Result F) → isProp (Has r)
propHas failure = isProp⊥
propHas (found _ _) = isPropUnit

decHas : {F : ℕ → Interval} (r : Result F) → Dec (Has r)
decHas failure = no (λ p → p)
decHas (found _ _) = yes tt

extract : {F : ℕ → Interval} (r : Result F) → Has r → Σ[ xs ∈ List ℕ ] Cert F xs
extract failure ()
extract (found xs cert) _ = xs , cert

inspect : (F : ℕ → Interval) → List (List ℕ) → Result F
inspect F [] = failure
inspect F (xs ∷ rest) with checkCert F xs
... | yes cert = found xs cert
... | no _ = inspect F rest

concat : {ℓ : Level} {A : Type ℓ} → List (List A) → List A
concat [] = []
concat (xs ∷ xss) = xs ++ concat xss

upto : ℕ → List ℕ
upto zero = 0 ∷ []
upto (suc n) = upto n ++ (suc n ∷ [])

words : ℕ → List ℕ → List (List ℕ)
words zero alphabet = [] ∷ []
words (suc k) alphabet = [] ∷ concat (map (λ i → map (i ∷_) (words k alphabet)) alphabet)

stage : (F : ℕ → Interval) → ℕ → Result F
stage F n = inspect F (words n (upto n))

SuccessfulStage : (ℕ → Interval) → ℕ → Type
SuccessfulStage F n = Has (stage F n)

leastStage : (F : ℕ → Interval) → ∥ Σ ℕ (SuccessfulStage F) ∥₁ →
  Σ ℕ (N.Minimal.Least (SuccessfulStage F))
leastStage F = PT.rec (N.Minimal.isPropΣLeast (λ n → propHas (stage F n)))
  (N.Minimal.→Least (λ n → decHas (stage F n)))

deliverCert : (F : ℕ → Interval) → ∥ Σ ℕ (SuccessfulStage F) ∥₁ →
  Σ[ xs ∈ List ℕ ] Cert F xs
deliverCert F h = extract (stage F (fst result)) (fst (snd result))
  where
  result = leastStage F h

deliver : (F : ℕ → Interval) → ∥ Σ ℕ (SuccessfulStage F) ∥₁ →
  Σ[ xs ∈ List ℕ ] Cover F xs
deliver F h = fst result , chainSound F (fst result) (snd result)
  where
  result = deliverCert F h

overlapStage : SuccessfulStage overlapping 2
overlapStage = tt

overlapInput : ∥ Σ ℕ (SuccessfulStage overlapping) ∥₁
overlapInput = ∣ (2 , overlapStage) ∣₁

selectedIndices : fst (deliver overlapping overlapInput) ≡ pairIndices
selectedIndices = refl

selectedCoverage : Cover overlapping (fst (deliver overlapping overlapInput))
selectedCoverage = snd (deliver overlapping overlapInput)

touchingStage2 : stage touching 2 ≡ failure
touchingStage2 = refl

-- A constructive coverage proof for the finite-list generator. Every finite
-- list occurs at a finite stage; successful inspection is not a sampling claim.
data Mem {ℓ : Level} {A : Type ℓ} (x : A) : List A → Type ℓ where
  memHere : {xs : List A} → Mem x (x ∷ xs)
  memThere : {y : A} {xs : List A} → Mem x xs → Mem x (y ∷ xs)

appendLeft : {ℓ : Level} {A : Type ℓ} {x : A} {xs ys : List A} →
  Mem x xs → Mem x (xs ++ ys)
appendLeft memHere = memHere
appendLeft (memThere p) = memThere (appendLeft p)

appendRight : {ℓ : Level} {A : Type ℓ} {x : A} (xs : List A) {ys : List A} →
  Mem x ys → Mem x (xs ++ ys)
appendRight [] p = p
appendRight (x ∷ xs) p = memThere (appendRight xs p)

mapMember : {ℓ ℓ' : Level} {A : Type ℓ} {B : Type ℓ'} (f : A → B)
  {x : A} {xs : List A} → Mem x xs → Mem (f x) (map f xs)
mapMember f memHere = memHere
mapMember f (memThere p) = memThere (mapMember f p)

concatMapMember : {ℓ ℓ' : Level} {A : Type ℓ} {B : Type ℓ'} (f : A → List B)
  {x : A} {xs : List A} {y : B} → Mem x xs → Mem y (f x) →
  Mem y (concat (map f xs))
concatMapMember f memHere q = appendLeft q
concatMapMember f {xs = z ∷ zs} (memThere p) q =
  appendRight (f z) (concatMapMember f p q)

rangeMember : (k n : ℕ) → k N.≤ n → Mem k (upto n)
rangeMember zero zero p = memHere
rangeMember (suc k) zero ()
rangeMember k (suc n) p with N.≤-split {m = k} {n = suc n} p
... | inl small = appendLeft (rangeMember k n small)
... | inr same = subst (λ j → Mem j (upto (suc n))) (sym same)
  (appendRight (upto n) memHere)

AllIn : List ℕ → List ℕ → Type
AllIn alphabet [] = Unit
AllIn alphabet (x ∷ xs) = Mem x alphabet × AllIn alphabet xs

wordMember : (xs : List ℕ) (fuel : ℕ) (alphabet : List ℕ) →
  length xs N.≤ fuel → AllIn alphabet xs → Mem xs (words fuel alphabet)
wordMember [] zero alphabet p q = memHere
wordMember [] (suc fuel) alphabet p q = memHere
wordMember (x ∷ xs) zero alphabet () q
wordMember (x ∷ xs) (suc fuel) alphabet p (hx , hs) = memThere
  (concatMapMember (λ i → map (i ∷_) (words fuel alphabet)) hx
    (mapMember (x ∷_) (wordMember xs fuel alphabet p hs)))

Bounded : ℕ → List ℕ → Type
Bounded n [] = Unit
Bounded n (x ∷ xs) = (x N.≤ n) × Bounded n xs

raiseBound : {n m : ℕ} → n N.≤ m → (xs : List ℕ) → Bounded n xs → Bounded m xs
raiseBound p [] q = tt
raiseBound {n} {m} p (x ∷ xs) (q , qs) =
  N.≤-trans {k = x} {m = n} {n = m} q p , raiseBound {n} {m} p xs qs

stepBound : (n : ℕ) → n N.≤ suc n
stepBound zero = tt
stepBound (suc n) = stepBound n

boundData : (xs : List ℕ) → Σ[ n ∈ ℕ ] ((length xs N.≤ n) × Bounded n xs)
boundData [] = 0 , tt , tt
boundData (x ∷ xs) with boundData xs
... | n , ln , bs = suc (x + n) , N.≤-trans {k = length xs} {m = n} {n = x + n} ln n≤sum ,
  N.≤-trans {k = x} {m = x + n} {n = suc (x + n)} (N.k≤k+n {n = n} x) (stepBound (x + n)) ,
  raiseBound {n} {suc (x + n)}
    (N.≤-trans {k = n} {m = x + n} {n = suc (x + n)} n≤sum (stepBound (x + n))) xs bs
  where
  n≤sum : n N.≤ x + n
  n≤sum = N.n≤k+n {k = x} n

boundedIn : (n : ℕ) (xs : List ℕ) → Bounded n xs → AllIn (upto n) xs
boundedIn n [] p = tt
boundedIn n (x ∷ xs) (p , ps) = rangeMember x n p , boundedIn n xs ps

generatorComplete : (xs : List ℕ) → Σ[ n ∈ ℕ ] Mem xs (words n (upto n))
generatorComplete xs with boundData xs
... | n , ln , bs = n , wordMember xs n (upto n) ln (boundedIn n xs bs)

inspectComplete : (F : ℕ → Interval) (candidates : List (List ℕ)) (xs : List ℕ) →
  Mem xs candidates → Cert F xs → Has (inspect F candidates)
inspectComplete F [] xs () cert
inspectComplete F (xs ∷ rest) .xs memHere cert with checkCert F xs
... | yes _ = tt
... | no noCert = Empty.rec (noCert cert)
inspectComplete F (ys ∷ rest) xs (memThere mem) cert with checkCert F ys
... | yes _ = tt
... | no _ = inspectComplete F rest xs mem cert

certificateStage : (F : ℕ → Interval) (xs : List ℕ) → Cert F xs → Σ ℕ (SuccessfulStage F)
certificateStage F xs cert with generatorComplete xs
... | n , mem = n , inspectComplete F (words n (upto n)) xs mem cert

fromMereChain : (F : ℕ → Interval) → ∥ Σ[ xs ∈ List ℕ ] Cert F xs ∥₁ →
  Σ[ xs ∈ List ℕ ] Cover F xs
fromMereChain F = deliver F ∘ PT.map (λ { (xs , cert) → certificateStage F xs cert })

fromMereChainIndices : fst (fromMereChain overlapping ∣ (pairIndices , overlapCert) ∣₁) ≡ pairIndices
fromMereChainIndices = refl
