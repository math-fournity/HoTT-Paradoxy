{-# OPTIONS --safe --cubical #-}

module VerificationEvent where

open import Agda.Primitive.Cubical using (I; i0; i1; primTransp)
open import Agda.Builtin.Cubical.Path using (_≡_)

-- Native Cubical Path and a higher inductive propositional truncation.
-- No user postulates, termination overrides, or unsolved metas.

data Empty : Set where

record Unit : Set where
  constructor tt

record _×_ (A B : Set) : Set where
  constructor _,_
  field
    fst : A
    snd : B
open _×_
infixr 4 _×_
infixr 4 _,_

Not : Set → Set
Not A = A → Empty

isProp : Set → Set
isProp A = (x y : A) → x ≡ y

emptyIsProp : isProp Empty
emptyIsProp ()

unitIsProp : isProp Unit
unitIsProp tt tt i = tt

negIsProp : {A : Set} → isProp (Not A)
negIsProp f g i a = emptyIsProp (f a) (g a) i

productIsProp : {A B : Set} → isProp A → isProp B → isProp (A × B)
productIsProp aProp bProp (a , b) (a' , b') i =
  aProp a a' i , bProp b b' i

data Trunc (A : Set) : Set where
  inc : A → Trunc A
  squash : (x y : Trunc A) → x ≡ y

truncRec : {A B : Set} → isProp B → (A → B) → Trunc A → B
truncRec prop f (inc a) = f a
truncRec prop f (squash x y i) =
  prop (truncRec prop f x) (truncRec prop f y) i

pathRefl : {A : Set} {a : A} → a ≡ a
pathRefl {a = a} i = a

cong : {A : Set} {B : Set₁} (f : A → B) {x y : A} →
       x ≡ y → f x ≡ f y
cong f p i = f (p i)

transportType : {A B : Set} → A ≡ B → A → B
transportType p a = primTransp (λ i → p i) i0 a

-- Three explicit snapshots and two events. These are logical stages,
-- not a model of physical time or of all proof search.
data Stage : Set where
  initial afterP afterHistory : Stage

data Step : Stage → Stage → Set where
  issueP : Step initial afterP
  recordHistory : Step afterP afterHistory

twoEventTrace : Step initial afterP × Step afterP afterHistory
twoEventTrace = issueP , recordHistory

-- A finite, closed vocabulary. P is a fixed true atom. The two other
-- claims differ in whether their reference stage is frozen or current.
data Claim : Set where
  atom historical current : Claim

data Registered : Stage → Claim → Set where
  pAtFirst : Registered afterP atom
  pAtLast : Registered afterHistory atom
  historyAtLast : Registered afterHistory historical

-- Knowledge means merely having a registration at the specified stage,
-- not merely the existence of a proof somewhere or at any time.
K : Stage → Claim → Set
K s c = Trunc (Registered s c)

P : Set
P = Unit

noInitialRegistration : {c : Claim} → Registered initial c → Empty
noInitialRegistration ()

noInitialKnowledge : (c : Claim) → Not (K initial c)
noInitialKnowledge c = truncRec emptyIsProp noInitialRegistration

Current : Stage → Set
Current s = P × Not (K s atom)

Historical : Set
Historical = P × Not (K initial atom)

historicalWitness : Historical
historicalWitness = tt , noInitialKnowledge atom

initialCurrentWitness : Current initial
initialCurrentWitness = historicalWitness

Meaning : Stage → Claim → Set
Meaning s atom = P
Meaning s historical = Historical
Meaning s current = Current s

meaningIsProp : (s : Stage) (c : Claim) → isProp (Meaning s c)
meaningIsProp s atom = unitIsProp
meaningIsProp s historical = productIsProp unitIsProp negIsProp
meaningIsProp s current = productIsProp unitIsProp negIsProp

-- Registration soundness is proved for every registration of this model.
-- It is NOT assumed as a global self-soundness axiom for HoTT.
registeredSound : {s : Stage} {c : Claim} →
                  Registered s c → Meaning s c
registeredSound pAtFirst = tt
registeredSound pAtLast = tt
registeredSound historyAtLast = historicalWitness

knowledgeSound : (s : Stage) (c : Claim) → K s c → Meaning s c
knowledgeSound s c = truncRec (meaningIsProp s c) registeredSound

historicalKnownLater : K afterHistory historical
historicalKnownLater = inc historyAtLast

historicalVerifiedLater : Historical
historicalVerifiedLater = knowledgeSound afterHistory historical historicalKnownLater

currentFalseAfterP : Not (Current afterP)
currentFalseAfterP q = snd q (inc pAtFirst)

currentFalseAfterHistory : Not (Current afterHistory)
currentFalseAfterHistory q = snd q (inc pAtLast)

-- Exact failure of confusing the historical proposition with the new
-- current proposition. This is a function-space non-inhabitation result.
noHistoricalToCurrent : Not (Historical → Current afterP)
noHistoricalToCurrent f = currentFalseAfterP (f historicalWitness)

noStageIndependentTruthPath : Not (Current initial ≡ Current afterP)
noStageIndependentTruthPath p =
  currentFalseAfterP (transportType p initialCurrentWitness)

-- A typed observer can later certify the frozen past claim, but it cannot
-- certify the corresponding false current claim at either later stage.
currentNotKnown : (s : Stage) → Not (K s current)
currentNotKnown initial = noInitialKnowledge current
currentNotKnown afterP k = currentFalseAfterP (knowledgeSound afterP current k)
currentNotKnown afterHistory k =
  currentFalseAfterHistory (knowledgeSound afterHistory current k)

data Bool : Set where
  false true : Bool

data Decision (A : Set) : Set where
  yes : A → Decision A
  no : Not A → Decision A

decideCurrent : (s : Stage) → Decision (Current s)
decideCurrent initial = yes initialCurrentWitness
decideCurrent afterP = no currentFalseAfterP
decideCurrent afterHistory = no currentFalseAfterHistory

decisionBit : {A : Set} → Decision A → Bool
decisionBit (yes a) = true
decisionBit (no n) = false

initialDecision : decisionBit (decideCurrent initial) ≡ true
initialDecision = pathRefl

laterDecision : decisionBit (decideCurrent afterP) ≡ false
laterDecision = pathRefl

-- Genuine HIT test: completely squash the stage type. No predicate on
-- that quotient can have pointwise two-way maps to Current at every stage.
-- The result rejects this chosen erasure, not HoTT itself.
noTruthFaithfulStageErasure :
  (F : Trunc Stage → Set) →
  ((s : Stage) → Current s → F (inc s)) →
  ((s : Stage) → F (inc s) → Current s) → Empty
noTruthFaithfulStageErasure F encode decode =
  currentFalseAfterP
    (decode afterP
      (transportType (cong F (squash (inc initial) (inc afterP)))
        (encode initial initialCurrentWitness)))

-- The un-erased, stage-indexed family is a positive control.
stageAwareFamily : Stage → Set
stageAwareFamily = Current

stageAwareIdentity : (s : Stage) → Current s → stageAwareFamily s
stageAwareIdentity s q = q

-- Conditional logical kernel of the Moore/Fitch comparison. Factivity
-- and conjunction closure are explicit parameters; no knowability
-- principle, classical logic, Gödel coding, or universal evaluator is used.
noKnownMoore :
  (A : Set) (Know : Set → Set) →
  ((X : Set) → Know X → X) →
  ((X Y : Set) → Know (X × Y) → Know X × Know Y) →
  Know (A × Not (Know A)) → Empty
noKnownMoore A Know fact split k =
  fact (Not (Know A)) (snd (split A (Not (Know A)) k))
    (fst (split A (Not (Know A)) k))
