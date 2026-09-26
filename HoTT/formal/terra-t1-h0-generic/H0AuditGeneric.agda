{-# OPTIONS --safe --cubical --guardedness #-}
open import Cubical.Foundations.Prelude
{-
  H₀ generic metadata positive control.

  Proof ID : MP-TERRA-T1-H0-GENERIC-001
  Claims   : C-351 -- C-353

  For arbitrary supplied metadata values, one primitive step records the
  actor, action, before/after content, and metadata in the append-only log.
  This isolates the structural question from the number or names of audit
  fields.  It is not an FHIR schema or a deployed security model.
-}
module H0AuditGeneric
  (Content Actor Action Metadata : Type)
  (apply : Action → Content → Content)
  (undo : Action → Action)
  (undo-law : (a : Action) (c : Content) → apply (undo a) (apply a c) ≡ c) where

open import Cubical.Data.Sigma
open import Cubical.Data.List using (List ; [] ; _∷_ ; _++_)
open import Cubical.Data.List.Properties using (¬cons≡nil)
open import Cubical.Relation.Nullary using (¬_)

AuditEvent : Type
AuditEvent = Actor × Action × Content × Content × Metadata

recordEvent : Actor → Action → Content → Content → Metadata → AuditEvent
recordEvent u a before after metadata = u , a , before , after , metadata

AuditLog : Type
AuditLog = List AuditEvent

State : Type
State = Content × AuditLog

current : State → Content
current = fst

audit : State → AuditLog
audit = snd

-- The metadata is an argument of the same primitive state transition.
step : Actor → Action → Metadata → State → State
step u a metadata (c , log) =
  apply a c , log ++ (recordEvent u a c (apply a c) metadata ∷ [])

++-assoc : (xs ys zs : AuditLog) → (xs ++ ys) ++ zs ≡ xs ++ (ys ++ zs)
++-assoc []       ys zs = refl
++-assoc (x ∷ xs) ys zs = cong (x ∷_) (++-assoc xs ys zs)

------------------------------------------------------------------------
-- C-351: content restoration works for arbitrary supplied metadata.

contentUndo : (u : Actor) (a : Action) (m₁ m₂ : Metadata)
  (c : Content) (log : AuditLog)
  → current (step u (undo a) m₂ (step u a m₁ (c , log))) ≡ c
contentUndo u a m₁ m₂ c log = undo-law a c

------------------------------------------------------------------------
-- C-352: both supplied metadata payloads survive in the same-step audit log.

auditAppend : (u : Actor) (a : Action) (m₁ m₂ : Metadata)
  (c : Content) (log : AuditLog)
  → audit (step u (undo a) m₂ (step u a m₁ (c , log)))
      ≡ log ++
        (recordEvent u a c (apply a c) m₁ ∷
         recordEvent u (undo a) (apply a c) (apply (undo a) (apply a c)) m₂ ∷ [])
auditAppend u a m₁ m₂ c log =
  ++-assoc log (recordEvent u a c (apply a c) m₁ ∷ [])
    (recordEvent u (undo a) (apply a c) (apply (undo a) (apply a c)) m₂ ∷ [])

------------------------------------------------------------------------
-- C-353: supplied audit payload prevents complete-state return at an empty log.

initial : Content → State
initial c = c , []

afterUndo : Actor → Action → Metadata → Metadata → Content → State
afterUndo u a m₁ m₂ c = step u (undo a) m₂ (step u a m₁ (initial c))

contentRestoredAtInitial : (u : Actor) (a : Action) (m₁ m₂ : Metadata)
  (c : Content) → current (afterUndo u a m₁ m₂ c) ≡ current (initial c)
contentRestoredAtInitial u a m₁ m₂ c = contentUndo u a m₁ m₂ c []

fullStateNotReturn : (u : Actor) (a : Action) (m₁ m₂ : Metadata)
  (c : Content) → ¬ (afterUndo u a m₁ m₂ c ≡ initial c)
fullStateNotReturn u a m₁ m₂ c p = ¬cons≡nil (cong snd p)
