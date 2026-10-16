{-# OPTIONS --cubical --safe --guardedness #-}

module FairEnumeration where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ ; zero ; suc ; _+_)
open import Cubical.Data.Bool.Base using (Bool ; false ; true)
open import Cubical.Data.Sigma.Base using (_×_)
import Cubical.Data.Nat.Order as NOrder
open import Agda.Builtin.List using (List ; [] ; _∷_)

open import MachineHalting using (Config ; cfg ; pc ; r0 ; r1 ; initial)
open import ProgramCode using
  ( ProgramCode ; haltsWithin ; haltCode ; loopCode
  ; haltCode-within ; loopCode-never-within
  )
import NatProgramCode as NPC

open NPC using (_++_ ; unary ; LEN ; codeBits ; unbits ; halfs)

------------------------------------------------------------------------
-- A total reader for one self-delimiting unary natural.

record UnaryResult : Type where
  constructor unaryResult
  field
    unaryValue : ℕ
    unaryRest : List Bool

open UnaryResult

incrementUnary : UnaryResult → UnaryResult
incrementUnary (unaryResult value rest) = unaryResult (suc value) rest

readUnary : List Bool → UnaryResult
readUnary [] = unaryResult zero []
readUnary (false ∷ rest) = unaryResult zero rest
readUnary (true ∷ rest) = incrementUnary (readUnary rest)

readUnary-unary :
  (value : ℕ) (rest : List Bool) →
  readUnary (unary value ++ rest) ≡ unaryResult value rest
readUnary-unary zero rest = refl
readUnary-unary (suc value) rest =
  cong incrementUnary (readUnary-unary value rest)

------------------------------------------------------------------------
-- A fixed-arity, self-delimiting natural-number triple code.

record Triple : Type where
  constructor triple
  field
    first : ℕ
    second : ℕ
    third : ℕ

open Triple

afterThird : ℕ → ℕ → UnaryResult → Triple
afterThird left middle (unaryResult right rest) = triple left middle right

afterSecond : ℕ → UnaryResult → Triple
afterSecond left (unaryResult middle rest) =
  afterThird left middle (readUnary rest)

afterFirst : UnaryResult → Triple
afterFirst (unaryResult left rest) =
  afterSecond left (readUnary rest)

parseTriple : List Bool → Triple
parseTriple bits = afterFirst (readUnary bits)

tripleBits : ℕ → ℕ → ℕ → List Bool
tripleBits left middle right =
  unary left ++ (unary middle ++ unary right)

encodeTriple : ℕ → ℕ → ℕ → ℕ
encodeTriple left middle right = codeBits (tripleBits left middle right)

decodeTriple : ℕ → Triple
decodeTriple code = parseTriple (unbits code code)

tripleBits-associated :
  (left middle right : ℕ) (junk : List Bool) →
  tripleBits left middle right ++ junk ≡
  unary left ++ (unary middle ++ (unary right ++ junk))
tripleBits-associated left middle right junk =
  NPC.++-assoc (unary left) (unary middle ++ unary right) junk
  ∙ cong (λ suffix → unary left ++ suffix)
      (NPC.++-assoc (unary middle) (unary right) junk)

parseTriple-junk :
  (left middle right : ℕ) (junk : List Bool) →
  parseTriple (tripleBits left middle right ++ junk) ≡
  triple left middle right
parseTriple-junk left middle right junk =
  cong parseTriple (tripleBits-associated left middle right junk)
  ∙ cong afterFirst
      (readUnary-unary left (unary middle ++ (unary right ++ junk)))
  ∙ cong (afterSecond left)
      (readUnary-unary middle (unary right ++ junk))
  ∙ cong (afterThird left middle)
      (readUnary-unary right junk)

tripleBound :
  (left middle right : ℕ) →
  NOrder._≤_ (LEN (tripleBits left middle right))
             (encodeTriple left middle right)
tripleBound left middle right =
  NOrder.≤-trans NOrder.≤-sucℕ
    (NPC.codeBits-dominates (tripleBits left middle right))

decodeTriple-encodeTriple :
  (left middle right : ℕ) →
  decodeTriple (encodeTriple left middle right) ≡
  triple left middle right
decodeTriple-encodeTriple left middle right =
  cong parseTriple bitEquation
  ∙ parseTriple-junk left middle right junk
  where
    bits : List Bool
    bits = tripleBits left middle right

    split : NPC.Σ′ ℕ
      (λ slack → encodeTriple left middle right ≡ LEN bits + slack)
    split = NPC.≤′-split (tripleBound left middle right)

    slack : ℕ
    slack = NPC.Σ′.fst′ split

    fuelEquation : encodeTriple left middle right ≡ LEN bits + slack
    fuelEquation = NPC.Σ′.snd′ split

    junk : List Bool
    junk = unbits slack (halfs (LEN bits) (encodeTriple left middle right))

    bitEquation :
      unbits (encodeTriple left middle right)
             (encodeTriple left middle right) ≡
      bits ++ junk
    bitEquation = firstStep ∙ secondStep
      where
        firstStep :
          unbits (encodeTriple left middle right)
                 (encodeTriple left middle right) ≡
          unbits (LEN bits) (encodeTriple left middle right) ++ junk
        firstStep = subst
          (λ fuel →
            unbits fuel (encodeTriple left middle right) ≡
            unbits (LEN bits) (encodeTriple left middle right) ++ junk)
          (sym fuelEquation)
          (NPC.unbits-split
            (LEN bits) slack (encodeTriple left middle right))

        secondStep :
          unbits (LEN bits) (encodeTriple left middle right) ++ junk ≡
          bits ++ junk
        secondStep =
          cong (λ prefix → prefix ++ junk) (NPC.unbits-code bits)

encodeTriple-injective :
  (a b c x y z : ℕ) →
  encodeTriple a b c ≡ encodeTriple x y z →
  triple a b c ≡ triple x y z
encodeTriple-injective a b c x y z equality =
  sym (decodeTriple-encodeTriple a b c)
  ∙ cong decodeTriple equality
  ∙ decodeTriple-encodeTriple x y z

decodeTriple-surjective :
  (numbers : Triple) → Σ[ index ∈ ℕ ] decodeTriple index ≡ numbers
decodeTriple-surjective (triple left middle right) =
  encodeTriple left middle right ,
  decodeTriple-encodeTriple left middle right

------------------------------------------------------------------------
-- Config is a fixed triple of natural numbers.

configToTriple : Config → Triple
configToTriple state = triple (pc state) (r0 state) (r1 state)

tripleToConfig : Triple → Config
tripleToConfig (triple label left right) = cfg label left right

config-roundtrip : (state : Config) → tripleToConfig (configToTriple state) ≡ state
config-roundtrip (cfg label left right) = refl

encodeConfig : Config → ℕ
encodeConfig state =
  encodeTriple (pc state) (r0 state) (r1 state)

decodeConfig : ℕ → Config
decodeConfig code = tripleToConfig (decodeTriple code)

decodeConfig-encodeConfig :
  (state : Config) → decodeConfig (encodeConfig state) ≡ state
decodeConfig-encodeConfig state =
  cong tripleToConfig
    (decodeTriple-encodeTriple (pc state) (r0 state) (r1 state))
  ∙ config-roundtrip state

encodeConfig-injective :
  (left right : Config) →
  encodeConfig left ≡ encodeConfig right → left ≡ right
encodeConfig-injective left right equality =
  sym (decodeConfig-encodeConfig left)
  ∙ cong decodeConfig equality
  ∙ decodeConfig-encodeConfig right

decodeConfig-surjective :
  (state : Config) → Σ[ code ∈ ℕ ] decodeConfig code ≡ state
decodeConfig-surjective state =
  encodeConfig state , decodeConfig-encodeConfig state

------------------------------------------------------------------------
-- Fair enumeration of program-code, input and fuel cases.

record SearchCase : Type where
  constructor searchCase
  field
    caseProgram : ProgramCode
    caseInput : Config
    caseFuel : ℕ

open SearchCase

numbersToCase : Triple → SearchCase
numbersToCase (triple programNumber inputNumber fuel) =
  searchCase (NPC.decodeNat programNumber)
             (decodeConfig inputNumber)
             fuel

caseAt : ℕ → SearchCase
caseAt index = numbersToCase (decodeTriple index)

caseIndex : ProgramCode → Config → ℕ → ℕ
caseIndex program input fuel =
  encodeTriple (NPC.encodeNat program) (encodeConfig input) fuel

caseAt-caseIndex :
  (program : ProgramCode) (input : Config) (fuel : ℕ) →
  caseAt (caseIndex program input fuel) ≡
  searchCase program input fuel
caseAt-caseIndex program input fuel =
  cong numbersToCase
    (decodeTriple-encodeTriple
      (NPC.encodeNat program) (encodeConfig input) fuel)
  ∙ cong₂ (λ decodedProgram decodedInput →
      searchCase decodedProgram decodedInput fuel)
      (NPC.decodeNat-encodeNat program)
      (decodeConfig-encodeConfig input)

-- `AppearsBy stage target` means a schedule index no greater than `stage`
-- already denotes `target`.  Every case has the explicit finite stage given
-- by `caseIndex`; this is the no-starvation statement required by R2-FAIR.

AppearsBy : ℕ → SearchCase → Type
AppearsBy stage target =
  Σ[ index ∈ ℕ ]
    (NOrder._≤_ index stage) × (caseAt index ≡ target)

eventuallyVisited :
  (program : ProgramCode) (input : Config) (fuel : ℕ) →
  AppearsBy (caseIndex program input fuel) (searchCase program input fuel)
eventuallyVisited program input fuel =
  caseIndex program input fuel ,
  NOrder.≤-refl ,
  caseAt-caseIndex program input fuel

noStarvation :
  (program : ProgramCode) (input : Config) (fuel : ℕ) →
  Σ[ stage ∈ ℕ ] AppearsBy stage (searchCase program input fuel)
noStarvation program input fuel =
  caseIndex program input fuel ,
  eventuallyVisited program input fuel

------------------------------------------------------------------------
-- The scheduled bounded observation is the original R2 observation.

observeCase : SearchCase → Bool
observeCase (searchCase program input fuel) =
  haltsWithin fuel program input

observeAt : ℕ → Bool
observeAt index = observeCase (caseAt index)

observeAt-caseIndex :
  (program : ProgramCode) (input : Config) (fuel : ℕ) →
  observeAt (caseIndex program input fuel) ≡
  haltsWithin fuel program input
observeAt-caseIndex program input fuel =
  cong observeCase (caseAt-caseIndex program input fuel)

haltCase-visited-true : (fuel : ℕ) →
  observeAt (caseIndex haltCode initial fuel) ≡ true
haltCase-visited-true fuel =
  observeAt-caseIndex haltCode initial fuel
  ∙ haltCode-within fuel

loopCase-visited-false : (fuel : ℕ) →
  observeAt (caseIndex loopCode initial fuel) ≡ false
loopCase-visited-false fuel =
  observeAt-caseIndex loopCode initial fuel
  ∙ loopCode-never-within fuel
