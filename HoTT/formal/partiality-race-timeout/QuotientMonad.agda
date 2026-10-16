{-# OPTIONS --safe --cubical --guardedness #-}

-- Native Cubical Agda continuation of MP-RACE-TIMEOUT-001 / MP-CONTEXTUAL-EQUIV-001:
-- the quotient-valued continuation bind for the R041 delay fragment.
--
--   C-84  the ≈-quotient has a canonical section sec : Q A → Delay A
--         (canonical representative = minimal-time representative), with
--         sec [p] ≡ canon p and [ sec x ] ≋ x
--   C-85  quotient-valued continuation bind bindQQ : Q A → (A → Q B) → Q B
--         exists and is representative-compatible with bind
--   C-86  unit laws: bindQQ [ret 0 a] f ≋ f a and
--         bindQQ q ([_] ∘ (λ a → ret 0 a)) ≋ q
--
-- This is the positive answer to R041 §2.1 *for this fragment*: no choice
-- principle is needed because each class has a definable canonical
-- representative. Associativity and a wider context language remain open.

module QuotientMonad where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels using (isSet×; isOfHLevelRetractFromIso; isPropΠ)
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Sigma.Base
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Unit.Properties using (isSetUnit)
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)
open import Cubical.Data.Sum.Properties using (isSet⊎)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.Nat.Properties using (isSetℕ)
open import Cubical.Data.Empty.Base using () renaming (rec to ⊥-rec)
open import Cubical.HITs.SetQuotients.Base using (_/_; [_]; eq/; squash/)
open import Cubical.HITs.SetQuotients.Properties using (rec; elimProp)
open import PartialityRaceTimeout

private
  variable
    ℓ : Level
    A : Type ℓ

------------------------------------------------------------------
-- 1. Delay is a set, and the ≈-quotient has a canonical section
------------------------------------------------------------------

DelayIso : {ℓ : Level} {A : Type ℓ} → Iso (Delay A) (Unit ⊎ (ℕ × A))
Iso.fun DelayIso ω = inl tt
Iso.fun DelayIso (ret n a) = inr (n , a)
Iso.inv DelayIso (inl _) = ω
Iso.inv DelayIso (inr (n , a)) = ret n a
Iso.rightInv DelayIso (inl _) = refl
Iso.rightInv DelayIso (inr (n , a)) = refl
Iso.leftInv DelayIso ω = refl
Iso.leftInv DelayIso (ret n a) = refl

isSetDelay : {ℓ : Level} {A : Type ℓ} → isSet A → isSet (Delay A)
isSetDelay {A = A} setA =
  isOfHLevelRetractFromIso 2 DelayIso (isSet⊎ isSetUnit (isSet× isSetℕ setA))

-- The canonical representative: return immediately with the same value.
canon : {ℓ : Level} {A : Type ℓ} → Delay A → Delay A
canon ω = ω
canon (ret n a) = ret zero a

canon-≈ : (d : Delay A) → canon d ≈ d
canon-≈ ω b = ⇔-refl (Conv ω b)
canon-≈ (ret n a) b = ⇔-refl (a ≡ b)

canon-respects : (p q : Delay A) → p ≈ q → canon p ≡ canon q
canon-respects ω ω h = refl
canon-respects ω (ret m a) h = ⊥-rec (lower (⇔-bwd (h a) refl))
canon-respects (ret n a) ω h = ⊥-rec (lower (⇔-fwd (h a) refl))
canon-respects (ret n a) (ret m b) h =
  cong (λ c → ret zero c) (sym (⇔-fwd (h a) refl))

-- C-84: the canonical section of the result quotient.
sec : {ℓ : Level} {A : Type ℓ} → isSet A → Q A → Delay A
sec setA = rec (isSetDelay setA) canon canon-respects

sec-β : (setA : isSet A) (p : Delay A) → sec setA [ p ] ≡ canon p
sec-β setA p = refl

sec-section : (setA : isSet A) (x : Q A) → [ sec setA x ] ≋ x
sec-section setA =
  elimProp (λ x → squash/ [ sec setA x ] x)
    (λ p → eq/ (canon p) p (canon-≈ p))

------------------------------------------------------------------
-- 2. C-85: quotient-valued continuation bind
------------------------------------------------------------------

bindQQ : {ℓ ℓ' : Level} {A : Type ℓ} {B : Type ℓ'}
  → isSet A → isSet B → Q A → (A → Q B) → Q B
bindQQ setA setB q f = bindQ (λ a → sec setB (f a)) q

bindQQ-β : {ℓ ℓ' : Level} {A : Type ℓ} {B : Type ℓ'}
  (setA : isSet A) (setB : isSet B) (p : Delay A) (f : A → Delay B)
  → bindQQ setA setB [ p ] (λ a → [ f a ]) ≋ [ p bind f ]
bindQQ-β setA setB p f =
    bindQ-β (λ a → sec setB [ f a ]) p
  ∙ eq/ (p bind (λ a → sec setB [ f a ])) (p bind f)
      (bind-cong p p (λ a → sec setB [ f a ]) f (≈-refl p)
        (λ a → canon-≈ (f a)))

------------------------------------------------------------------
-- 3. C-86: unit laws at the quotient level
------------------------------------------------------------------

later-≈ : (d : Delay A) → later d ≈ d
later-≈ d b = later-conv d b

bindQQ-left-unit : {ℓ ℓ' : Level} {A : Type ℓ} {B : Type ℓ'}
  (setA : isSet A) (setB : isSet B) (a : A) (f : A → Q B)
  → bindQQ setA setB [ ret zero a ] f ≋ f a
bindQQ-left-unit setA setB a f =
    bindQ-β (λ x → sec setB (f x)) (ret zero a)
  ∙ eq/ (later (sec setB (f a))) (sec setB (f a)) (later-≈ (sec setB (f a)))
  ∙ sec-section setB (f a)

bind-unit-≈ : (p : Delay A) → (p bind (λ a → ret zero a)) ≈ p
bind-unit-≈ ω b = ⇔-refl (Conv ω b)
bind-unit-≈ (ret n a) b =
  ⇔-comp (bind-conv-ret n a (λ x → ret zero x) b) (⇔-refl (a ≡ b))

bindQQ-right-unit : {ℓ : Level} {A : Type ℓ}
  (setA : isSet A) (q : Q A)
  → bindQQ setA setA q (λ a → [ ret zero a ]) ≋ q
bindQQ-right-unit setA =
  elimProp (λ q → squash/ _ _)
    (λ p → eq/ (p bind (λ a → ret zero a)) p (bind-unit-≈ p))

------------------------------------------------------------------
-- 4. C-87/C-88: associativity
------------------------------------------------------------------

bind-later-eq : {ℓ ℓ' : Level} {B : Type ℓ} {C : Type ℓ'}
  (d : Delay B) (g : B → Delay C) → ((later d) bind g) ≡ (later (d bind g))
bind-later-eq ω g = refl
bind-later-eq (ret m b) g = refl

later-≈-cong : (d d' : Delay A) → d ≈ d' → later d ≈ later d'
later-≈-cong d d' h b =
  ⇔-comp (later-conv d b) (⇔-comp (h b) (⇔-sym (later-conv d' b)))

bind-iterLater-≈ : {ℓ ℓ' : Level} {B : Type ℓ} {C : Type ℓ'}
  (n : ℕ) (d : Delay B) (g : B → Delay C)
  → ((iterLater n d) bind g) ≈ (iterLater n (d bind g))
bind-iterLater-≈ zero d g = ≈-refl (d bind g)
bind-iterLater-≈ (suc n) d g =
  subst (λ x → x ≈ iterLater (suc n) (d bind g))
    (sym (bind-later-eq (iterLater n d) g))
    (later-≈-cong ((iterLater n d) bind g) (iterLater n (d bind g))
      (bind-iterLater-≈ n d g))

bind-assoc-≈ : {ℓ ℓ' ℓ'' : Level} {A : Type ℓ} {B : Type ℓ'} {C : Type ℓ''}
  (p : Delay A) (f : A → Delay B) (g : B → Delay C)
  → ((p bind f) bind g) ≈ (p bind (λ a → f a bind g))
bind-assoc-≈ ω f g = ≈-refl ω
bind-assoc-≈ (ret n a) f g =
  subst (λ x → x ≈ later (iterLater n (f a bind g)))
    (sym (bind-later-eq (iterLater n (f a)) g))
    (later-≈-cong ((iterLater n (f a)) bind g) (iterLater n (f a bind g))
      (bind-iterLater-≈ n (f a) g))

assocQ-β : {ℓ ℓ' ℓ'' : Level} {A : Type ℓ} {B : Type ℓ'} {C : Type ℓ''}
  (setA : isSet A) (setB : isSet B) (setC : isSet C)
  (p : Delay A) (f : A → Q B) (g : B → Q C)
  → bindQQ setB setC (bindQQ setA setB [ p ] f) g
  ≋ bindQQ setA setC [ p ] (λ a → bindQQ setB setC (f a) g)
assocQ-β {ℓ = ℓ} {ℓ' = ℓ'} {ℓ'' = ℓ''} {A = A} {B = B} {C = C} setA setB setC p f g =
  eq/ R0 R2
    (≈-trans R0 R1 R2
      (bind-assoc-≈ p F G)
      (bind-cong p p (λ a → F a bind G) G' (≈-refl p) pt))
  where
  F : A → Delay B
  F a = sec setB (f a)

  G : B → Delay C
  G b = sec setC (g b)

  G' : A → Delay C
  G' a = sec setC (bindQQ setB setC (f a) g)

  R0 : Delay C
  R0 = (p bind F) bind G

  R1 : Delay C
  R1 = p bind (λ a → F a bind G)

  R2 : Delay C
  R2 = p bind G'

  on-section : (a : A) → bindQQ setB setC (f a) g ≋ [ F a bind G ]
  on-section a =
    subst (λ z → bindQQ setB setC z g ≋ [ F a bind G ])
      (sec-section setB (f a)) refl

  sec-rewrite : (a : A) → G' a ≡ canon (F a bind G)
  sec-rewrite a = cong (sec setC) (on-section a)

  pt : (a : A) → (F a bind G) ≈ G' a
  pt a =
    subst (λ d → (F a bind G) ≈ d) (sym (sec-rewrite a))
      (≈-sym (canon (F a bind G)) (F a bind G) (canon-≈ (F a bind G)))

assocQ : {ℓ ℓ' ℓ'' : Level} {A : Type ℓ} {B : Type ℓ'} {C : Type ℓ''}
  (setA : isSet A) (setB : isSet B) (setC : isSet C)
  (q : Q A) (f : A → Q B) (g : B → Q C)
  → bindQQ setB setC (bindQQ setA setB q f) g
  ≋ bindQQ setA setC q (λ a → bindQQ setB setC (f a) g)
assocQ setA setB setC =
  elimProp (λ q → isPropΠ (λ f → isPropΠ (λ g → squash/ _ _)))
    (λ p f g → assocQ-β setA setB setC p f g)
