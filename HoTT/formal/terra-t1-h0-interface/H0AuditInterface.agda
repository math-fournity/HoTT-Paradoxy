{-# OPTIONS --safe --cubical --guardedness #-}
{-
  H₀ interface positive control: the same primitive update carries actor,
  event, update permission, and authorized audit-query data.

  Proof ID : MP-TERRA-T1-H0-INTERFACE-001
  Claims   : C-347 -- C-350

  This fixed finite model is deliberately an interface model, not a deployed
  authorization system.  A successful update needs CanUpdate; an audit query
  needs CanReadAudit; and step itself constructs the event it appends.

  It does NOT prove FHIR conformance, NIST enforcement, retention/WORM,
  cryptographic integrity, HPT merge/replay, or any general HoTT theorem.
-}
module H0AuditInterface where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma
open import Cubical.Data.Bool using (Bool ; true ; false ; not)
open import Cubical.Data.List using (List ; [] ; _∷_ ; _++_)
open import Cubical.Data.List.Properties using (¬cons≡nil)
open import Cubical.Relation.Nullary using (¬_)

------------------------------------------------------------------------
-- A fixed, finite actor/action/audit interface

data Actor : Type where
  updater auditor outsider : Actor

data Action : Type where
  forward backward : Action

data Permit : Type where
  grant : Permit

data Denied : Type where

CanUpdate : Actor → Action → Bool → Type
CanUpdate updater _ _ = Permit
CanUpdate auditor _ _ = Denied
CanUpdate outsider _ _ = Denied

undo : Action → Action
undo forward  = backward
undo backward = forward

apply : Action → Bool → Bool
apply forward  = not
apply backward = not

undo-law : (a : Action) (c : Bool) → apply (undo a) (apply a c) ≡ c
undo-law forward  true  = refl
undo-law forward  false = refl
undo-law backward true  = refl
undo-law backward false = refl

data AuditEvent : Type where
  event : Actor → Action → Bool → Bool → AuditEvent

eventActor : AuditEvent → Actor
eventActor (event u _ _ _) = u

eventAction : AuditEvent → Action
eventAction (event _ a _ _) = a

eventBefore : AuditEvent → Bool
eventBefore (event _ _ c _) = c

eventAfter : AuditEvent → Bool
eventAfter (event _ _ _ c') = c'

AuditLog : Type
AuditLog = List AuditEvent

State : Type
State = Bool × AuditLog

current : State → Bool
current = fst

audit : State → AuditLog
audit = snd

CanReadAudit : Actor → State → Type
CanReadAudit updater _ = Denied
CanReadAudit auditor _ = Permit
CanReadAudit outsider _ = Denied

-- The audit event is generated inside this same primitive state transition.
step : (u : Actor) (a : Action) (s : State)
     → CanUpdate u a (current s) → State
step u a (c , log) _ = apply a c , log ++ (event u a c (apply a c) ∷ [])

readAudit : (u : Actor) (s : State) → CanReadAudit u s → AuditLog
readAudit u s _ = audit s

------------------------------------------------------------------------
-- C-347: update permission and event metadata are internal to one step.

initial : State
initial = true , []

forwardPermit : CanUpdate updater forward (current initial)
forwardPermit = grant

afterForward : State
afterForward = step updater forward initial forwardPermit

forwardEventIsInternal : audit afterForward ≡ event updater forward true false ∷ []
forwardEventIsInternal = refl

forwardEventCarriesActor : eventActor (event updater forward true false) ≡ updater
forwardEventCarriesActor = refl

forwardEventCarriesAction : eventAction (event updater forward true false) ≡ forward
forwardEventCarriesAction = refl

------------------------------------------------------------------------
-- C-348: an authorized reader observes the two events of the same two steps.

backwardPermit : CanUpdate updater backward (current afterForward)
backwardPermit = grant

afterUndo : State
afterUndo = step updater backward afterForward backwardPermit

auditReaderPermit : CanReadAudit auditor afterUndo
auditReaderPermit = grant

authorizedQuery : readAudit auditor afterUndo auditReaderPermit
  ≡ event updater forward true false ∷ event updater backward false true ∷ []
authorizedQuery = refl

------------------------------------------------------------------------
-- C-349: the fixed interface rejects outsider update/read capabilities.

outsiderCannotUpdate : ¬ (CanUpdate outsider forward (current initial))
outsiderCannotUpdate ()

outsiderCannotRead : ¬ (CanReadAudit outsider afterUndo)
outsiderCannotRead ()

------------------------------------------------------------------------
-- C-350: content returns while the complete audit state does not.

contentRestored : current afterUndo ≡ current initial
contentRestored = refl

fullStateNotReturn : ¬ (afterUndo ≡ initial)
fullStateNotReturn p = ¬cons≡nil (cong snd p)
