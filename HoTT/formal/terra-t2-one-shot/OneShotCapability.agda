{-# OPTIONS --safe --cubical --guardedness #-}
{-
  T2: one-shot authorization-code capability, in two representations

  Proof ID : MP-TERRA-T2-ONESHOT-001
  Claims   : C-354 -- C-356

  The first part records a concrete consequence of an ordinary, unrestricted
  dependent-type context: an input x can inhabit both positions of a product.
  The second part is a positive control for the same externally observable
  authorization-code task: copies of the code can be supplied twice, while a
  stateful server grants the first redemption and denies the second.

  This deliberately does NOT prove that all HoTT representations of a
  one-shot resource are inadequate, that a state-passing representation is
  physically secure, or that standard HoTT has a contradiction.  It isolates
  the difference between a bare pure Code -> Token interface and a server
  transition that records consumption.
-}
module OneShotCapability where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma
open import Cubical.Data.List using (List ; [] ; _∷_ ; _++_)

------------------------------------------------------------------------
-- C-354: ordinary product formation admits a duplicated input.

duplicate : {A : Type} → A → A × A
duplicate x = x , x

data Code : Type where
  authorizationCode : Code

data Token : Type where
  accessToken : Token

duplicatedCode : Code × Code
duplicatedCode = duplicate authorizationCode

duplicateIsTwoCopies : duplicatedCode ≡ (authorizationCode , authorizationCode)
duplicateIsTwoCopies = refl

------------------------------------------------------------------------
-- C-355: a deliberately bare pure redemption interface grants twice.

pureRedeem : Code → Token
pureRedeem authorizationCode = accessToken

pureTwice : Code → Token × Token
pureTwice c = pureRedeem c , pureRedeem c

pureCopiesBothGrant : pureTwice authorizationCode ≡ (accessToken , accessToken)
pureCopiesBothGrant = refl

------------------------------------------------------------------------
-- C-356: the same copied input can instead be processed by a stateful
-- server interface which grants once, rejects once, and records both tries.

data Reply : Type where
  granted : Token → Reply
  denied  : Reply

data Status : Type where
  unused consumed : Status

data RedemptionEvent : Type where
  grantAttempt denialAttempt : RedemptionEvent

Server : Type
Server = Status × List RedemptionEvent

reply : Reply × Server → Reply
reply = fst

nextServer : Reply × Server → Server
nextServer = snd

-- This is the single protocol operation.  Its second result records the
-- consumption state; it is not a second, task-external logging operation.
redeem : Code → Server → Reply × Server
redeem authorizationCode (unused   , log) =
  granted accessToken , (consumed , log ++ (grantAttempt ∷ []))
redeem authorizationCode (consumed , log) =
  denied , (consumed , log ++ (denialAttempt ∷ []))

initial : Server
initial = unused , []

firstAttempt : Reply × Server
firstAttempt = redeem (fst duplicatedCode) initial

secondAttempt : Reply × Server
secondAttempt = redeem (snd duplicatedCode) (nextServer firstAttempt)

firstCopyGrants : reply firstAttempt ≡ granted accessToken
firstCopyGrants = refl

secondCopyIsDenied : reply secondAttempt ≡ denied
secondCopyIsDenied = refl

serverHasConsumedCode : fst (nextServer secondAttempt) ≡ consumed
serverHasConsumedCode = refl

bothAttemptsRecorded : snd (nextServer secondAttempt)
  ≡ grantAttempt ∷ denialAttempt ∷ []
bothAttemptsRecorded = refl
