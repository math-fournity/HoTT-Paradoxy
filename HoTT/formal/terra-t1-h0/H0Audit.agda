{-# OPTIONS --safe --cubical --guardedness #-}
{-
  H₀: an observable append-only audit-state positive control

  Proof ID : MP-TERRA-T1-H0-001
  Claims   : C-344 -- C-346

  This is a deliberately small Cubical Agda model of the model-level H₀
  countermodel in Terra audit 017.  One primitive step changes the content
  component and appends the event selected by that same action.  The model
  distinguishes content restoration from equality of the whole audit state.

  It does NOT encode FHIR resources, authorization enforcement, deployment
  storage, NIST controls, HPT's contractible contexts, merge, replay, or a
  theorem about all HoTT representations.
-}
module H0Audit where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma
open import Cubical.Data.Bool using (Bool ; true ; false ; not)
open import Cubical.Data.List using (List ; [] ; _∷_ ; _++_)
open import Cubical.Data.List.Properties using (¬cons≡nil)
open import Cubical.Relation.Nullary using (¬_)

------------------------------------------------------------------------
-- Content-level reversible action and audit events

data Action : Type where
  forward backward : Action

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
  evForward evBackward : AuditEvent

recordEvent : Action → AuditEvent
recordEvent forward  = evForward
recordEvent backward = evBackward

AuditLog : Type
AuditLog = List AuditEvent

State : Type
State = Bool × AuditLog

current : State → Bool
current = fst

audit : State → AuditLog
audit = snd

-- One primitive action performs both the content update and event append.
step : Action → State → State
step a (c , log) = apply a c , log ++ (recordEvent a ∷ [])

------------------------------------------------------------------------
-- C-344: content restoration is generic in the starting content and log.

contentUndo : (c : Bool) (log : AuditLog)
  → current (step (undo forward) (step forward (c , log))) ≡ c
contentUndo c log = undo-law forward c

------------------------------------------------------------------------
-- C-345: the same two primitive steps append their two audit events.

++-assoc : (xs ys zs : AuditLog) → (xs ++ ys) ++ zs ≡ xs ++ (ys ++ zs)
++-assoc []       ys zs = refl
++-assoc (x ∷ xs) ys zs = cong (x ∷_) (++-assoc xs ys zs)

auditAppend : (c : Bool) (log : AuditLog)
  → audit (step (undo forward) (step forward (c , log)))
      ≡ log ++ (evForward ∷ evBackward ∷ [])
auditAppend c log = ++-assoc log (evForward ∷ []) (evBackward ∷ [])

------------------------------------------------------------------------
-- C-346: a concrete complete state does not return, even though content does.

initial : State
initial = true , []

afterUndo : State
afterUndo = step backward (step forward initial)

initialContentRestored : current afterUndo ≡ current initial
initialContentRestored = refl

initialAuditRecordsBoth : audit afterUndo ≡ evForward ∷ evBackward ∷ []
initialAuditRecordsBoth = refl

fullStateNotReturn : ¬ (afterUndo ≡ initial)
fullStateNotReturn p = ¬cons≡nil (cong snd p)
