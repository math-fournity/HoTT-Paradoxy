{-# OPTIONS --safe --cubical --guardedness #-}
{-
  The existence question of a domain element that never halts: the universe
  (Claude, session 7f138325, 2026-09-26; claims CG001-C-75, CG001-C-76).

  proof id : MP-CG001-UNIVERSE-QUESTIONING-001
  claims   : CG001-C-75, CG001-C-76 (full statements in CLAIM.md)

  The user's principle (2026-09-26): a theory may refuse other questions, but
  it can never refuse the existence question of the elements of its own
  domain; if that question, asked in reality, starts a computation that never
  halts, the Russell pattern has been found.

  The universe Type ℓ-zero is an element of HoTT's domain (it is a type in the
  next universe), and univalence is a statement about its identity types, so
  HoTT cannot keep it out of the domain.  One way to ask its existence
  question is to ask, level by level, in what way its members are the same.
  That questioning halts exactly when the universe is settled at some finite
  level (isOfHLevel m).

  (a) localGlobal : Ω^(2+n)(U, X) ≃ Π (x : X) Ω^(1+n)(X, x).  Univalence lifts
      the sameness inside each member one level up, into the sameness of the
      universe.
  (b) For K = EM ℤ (1+n) (Eilenberg-MacLane space), at every point x the
      (1+n)-fold loops of K are ℤ (ΩⁿK), so there is a section that is not
      the trivial one (secNontrivial); at n = 0 the kernel reads it back as 1
      by refl (sectionReadsOne).
  (c) universeHasNoLevel : for every m, Type ℓ-zero is not of h-level m.
      The questioning never halts.                                   (C-75)
  (d) gatheringNeverSettled : for every k, the gathering of the types of
      h-level (1+k) is not itself of h-level (1+k); with the library's upper
      bound (gatheringOneUp) it sits exactly one level above its members.
      contractiblesSettled : at level 0 the gathering is contractible, the
      only settled gathering.                                        (C-76)

  Negative control: WrongSectionReadsZero.agda claims the section reads back
  as 0 at the base point; the kernel computes 1 and rejects it.
-}
module UniverseHasNoLevel where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Univalence
open import Cubical.Foundations.HLevels
open import Cubical.Foundations.Pointed
open import Cubical.Foundations.Transport
open import Cubical.Data.Nat using (ℕ ; zero ; suc ; _+_ ; snotz)
open import Cubical.Data.Int using (ℤ ; pos)
open import Cubical.Data.Int.Properties using (injPos)
open import Cubical.Data.Unit using (Unit ; tt ; isContrUnit ; isPropUnit ; isContr→≃Unit)
open import Cubical.Data.Empty using (⊥ ; isProp⊥)
open import Cubical.Data.Bool using (Bool ; true ; true≢false)
open import Cubical.Data.Bool.Properties using (notEquiv ; isSetBool)
open import Cubical.Data.Sigma
open import Cubical.Relation.Nullary using (¬_)
open import Cubical.Homotopy.Loopspace using (Ω ; Ω^_ ; Ω^≃∙)
open import Cubical.Algebra.AbGroup.Base
open import Cubical.Algebra.AbGroup.Instances.Int using (ℤAbGroup)
open import Cubical.Homotopy.EilenbergMacLane.Base using (EM ; EM∙ ; 0ₖ ; hLevelEM)
open import Cubical.Homotopy.EilenbergMacLane.Properties
  using (Iso-EM-ΩEM+1-gen ; ΩEM+1→EM-gen-refl ; EM≃ΩEM+1∙)

private
  variable
    ℓ ℓ' : Level

Ω^suc : (n : ℕ) (A : Pointed ℓ) → (Ω^ (suc n)) A ≡ (Ω^ n) (Ω A)
Ω^suc zero A = refl
Ω^suc (suc n) A = cong Ω (Ω^suc n A)

hLevelΩ^ : (n : ℕ) {A : Type ℓ} (a : A) → isOfHLevel (suc n) A → isContr (typ ((Ω^ n) (A , a)))
hLevelΩ^ zero a h = a , h a
hLevelΩ^ (suc n) {A} a h =
  subst (λ P → isContr (typ P)) (sym (Ω^suc n (A , a)))
        (hLevelΩ^ n refl (isOfHLevelPath' (suc n) h a a))

Πpt : (A : Type ℓ) (B : A → Pointed ℓ') → Pointed (ℓ-max ℓ ℓ')
Πpt A B = ((x : A) → typ (B x)) , (λ x → pt (B x))

ΩΠpt : (A : Type ℓ) (B : A → Pointed ℓ') → Ω (Πpt A B) ≡ Πpt A (λ x → Ω (B x))
ΩΠpt A B = ua∙ (isoToEquiv πIso) refl
  where
  πIso : Iso (typ (Ω (Πpt A B))) (typ (Πpt A (λ x → Ω (B x))))
  Iso.fun πIso p x i = p i x
  Iso.inv πIso h i x = h x i
  Iso.rightInv πIso h = refl
  Iso.leftInv πIso p = refl

Ω^Πpt : (n : ℕ) (A : Type ℓ) (B : A → Pointed ℓ') → (Ω^ n) (Πpt A B) ≡ Πpt A (λ x → (Ω^ n) (B x))
Ω^Πpt zero A B = refl
Ω^Πpt (suc n) A B =
  Ω^suc n (Πpt A B)
  ∙ cong (Ω^ n) (ΩΠpt A B)
  ∙ Ω^Πpt n A (λ x → Ω (B x))
  ∙ cong (Πpt A) (funExt λ x → sym (Ω^suc n (B x)))

U∙ : (X : Type ℓ) → Pointed (ℓ-suc ℓ)
U∙ {ℓ} X = Type ℓ , X

ΩU≃∙ : (X : Type ℓ) → Ω (U∙ X) ≃∙ ((X ≃ X) , idEquiv X)
ΩU≃∙ X = univalence , pathToEquivRefl

ΩEquiv≡ΩFun : (X : Type ℓ) → Ω ((X ≃ X) , idEquiv X) ≡ Ω ((X → X) , (λ x → x))
ΩEquiv≡ΩFun X = ua∙ ((λ p → cong fst p) , isEmbeddingFstΣProp (λ f → isPropIsEquiv f)) refl

localGlobal : (n : ℕ) (X : Type ℓ)
  → typ ((Ω^ (suc (suc n))) (U∙ X)) ≃ ((x : X) → typ ((Ω^ (suc n)) (X , x)))
localGlobal n X =
  compEquiv (pathToEquiv (cong typ (Ω^suc (suc n) (U∙ X))))
  (compEquiv (fst (Ω^≃∙ (suc n) (ΩU≃∙ X)))
  (pathToEquiv (cong typ
     (Ω^suc n ((X ≃ X) , idEquiv X)
     ∙ cong (Ω^ n) (ΩEquiv≡ΩFun X ∙ ΩΠpt X (λ x → X , x))
     ∙ Ω^Πpt n X (λ x → Ω (X , x))
     ∙ cong (Πpt X) (funExt λ x → sym (Ω^suc n (X , x)))))))

ΩⁿEMⁿ : (m : ℕ) → (Ω^ m) (EM∙ ℤAbGroup m) ≡ EM∙ ℤAbGroup 0
ΩⁿEMⁿ zero = refl
ΩⁿEMⁿ (suc m) =
  Ω^suc m (EM∙ ℤAbGroup (suc m))
  ∙ cong (Ω^ m) (sym (EM≃ΩEM+1∙ {G = ℤAbGroup} m))
  ∙ ΩⁿEMⁿ m

K : ℕ → Type ℓ-zero
K n = EM ℤAbGroup (suc n)

ΩK : (n : ℕ) (x : K n) → Ω (K n , x) ≡ EM∙ ℤAbGroup n
ΩK n x = ua∙ (isoToEquiv (invIso (Iso-EM-ΩEM+1-gen {G = ℤAbGroup} n x)))
             (ΩEM+1→EM-gen-refl {G = ℤAbGroup} n x)

ΩⁿK : (n : ℕ) (x : K n) → (Ω^ (suc n)) (K n , x) ≡ EM∙ ℤAbGroup 0
ΩⁿK n x = Ω^suc n (K n , x) ∙ cong (Ω^ n) (ΩK n x) ∙ ΩⁿEMⁿ n

sec : (n : ℕ) (x : K n) → typ ((Ω^ (suc n)) (K n , x))
sec n x = transport (cong typ (sym (ΩⁿK n x))) (pos 1)

trivSec : (n : ℕ) (x : K n) → typ ((Ω^ (suc n)) (K n , x))
trivSec n x = pt ((Ω^ (suc n)) (K n , x))

secNontrivial : (n : ℕ) → ¬ (sec n ≡ trivSec n)
secNontrivial n p = snotz (injPos one≡zero)
  where
  x₀ : K n
  x₀ = 0ₖ {G = ℤAbGroup} (suc n)
  P : (Ω^ (suc n)) (K n , x₀) ≡ EM∙ ℤAbGroup 0
  P = ΩⁿK n x₀
  one≡zero : pos 1 ≡ pos 0
  one≡zero =
    sym (transportTransport⁻ (cong typ P) (pos 1))
    ∙ cong (transport (cong typ P)) (funExt⁻ p x₀)
    ∙ fromPathP (cong pt P)

noContrΩU : (n : ℕ) → ¬ isContr (typ ((Ω^ (suc (suc n))) (U∙ (K n))))
noContrΩU n c =
  secNontrivial n
    (isContr→isProp (isOfHLevelRespectEquiv 0 (localGlobal n (K n)) c) (sec n) (trivSec n))

universeNot3+n : (n : ℕ) → ¬ isOfHLevel (3 + n) (Type ℓ-zero)
universeNot3+n n h = noContrΩU n (hLevelΩ^ (suc (suc n)) (K n) h)

universeHasNoLevel : (m : ℕ) → ¬ isOfHLevel m (Type ℓ-zero)
universeHasNoLevel m h = universeNot3+n m (isOfHLevelPlus 3 h)

ΩGathering≃∙ : (k : ℕ) (X : Type ℓ) (hX : isOfHLevel k X)
  → Ω (TypeOfHLevel ℓ k , (X , hX)) ≃∙ Ω (U∙ X)
ΩGathering≃∙ k X hX =
  ((λ p → cong fst p) , isEmbeddingFstΣProp (λ A → isPropIsOfHLevel k)) , refl

gatheringNotLevel : (n : ℕ) → ¬ isOfHLevel (3 + n) (TypeOfHLevel ℓ-zero (3 + n))
gatheringNotLevel n h = noContrΩU n (isOfHLevelRespectEquiv 0 e (hLevelΩ^ (suc (suc n)) (K n , hK) h))
  where
  hK : isOfHLevel (3 + n) (K n)
  hK = hLevelEM ℤAbGroup (suc n)
  G∙ : Pointed (ℓ-suc ℓ-zero)
  G∙ = TypeOfHLevel ℓ-zero (3 + n) , (K n , hK)
  e : typ ((Ω^ (suc (suc n))) G∙) ≃ typ ((Ω^ (suc (suc n))) (U∙ (K n)))
  e = compEquiv (pathToEquiv (cong typ (Ω^suc (suc n) G∙)))
      (compEquiv (fst (Ω^≃∙ (suc n) (ΩGathering≃∙ (3 + n) (K n) hK)))
      (pathToEquiv (cong typ (sym (Ω^suc (suc n) (U∙ (K n)))))))

contractiblesSettled : isContr (TypeOfHLevel ℓ-zero 0)
contractiblesSettled =
  (Unit , isContrUnit) ,
  λ { (A , cA) → Σ≡Prop (λ _ → isPropIsOfHLevel 0) (ua (invEquiv (isContr→≃Unit cA))) }

propsGatherNotProp : ¬ isProp (TypeOfHLevel ℓ-zero 1)
propsGatherNotProp h = transport⁻ (cong fst (h (⊥ , isProp⊥) (Unit , isPropUnit))) tt

notPath : Bool ≡ Bool
notPath = ua notEquiv

notPath≢refl : ¬ (notPath ≡ refl)
notPath≢refl e = true≢false (sym (cong (λ q → transport q true) e))

setsGatherNotSet : ¬ isSet (TypeOfHLevel ℓ-zero 2)
setsGatherNotSet h =
  notPath≢refl (cong (cong fst) (h BoolSet BoolSet (Σ≡Prop (λ _ → isPropIsSet) notPath) refl))
  where
  BoolSet : TypeOfHLevel ℓ-zero 2
  BoolSet = Bool , isSetBool

gatheringNeverSettled : (k : ℕ) → ¬ isOfHLevel (suc k) (TypeOfHLevel ℓ-zero (suc k))
gatheringNeverSettled zero = propsGatherNotProp
gatheringNeverSettled (suc zero) = setsGatherNotSet
gatheringNeverSettled (suc (suc n)) = gatheringNotLevel n

gatheringOneUp : (k : ℕ) → isOfHLevel (suc k) (TypeOfHLevel ℓ-zero k)
gatheringOneUp = isOfHLevelTypeOfHLevel

sectionReadsOne :
  transport (cong typ (ΩⁿK 0 (0ₖ {G = ℤAbGroup} 1))) (sec 0 (0ₖ {G = ℤAbGroup} 1)) ≡ pos 1
sectionReadsOne = refl
