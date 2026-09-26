/-
  Terra's T1 (H0 generic) and T2 (one-shot code) positive-control models,
  transcribed constructor for constructor into Lean 4 core
  (Claude, session 7f138325, 2026-09-26).

  proof id : MP-CG001-TERRA-MODELS-UIP-LEAN-001
  claim    : CG001-C-61 (full statement in CLAIM.md)

  Why: this is an ablation.  In Lean's kernel every proof of an equation is
  equal to every other one (theorem `uip` below holds by rfl), so uniqueness
  of identity proofs holds definitionally.  Univalence refutes that principle
  for a universe that contains Bool (HoTT Book, Example 3.1.9; the Cubical
  side is CG001-C-63 (a)).  If Terra's models go through here unchanged,
  their success does not depend on anything specific to homotopy type theory:
  not on paths used as transitions, univalence, higher inductive types, or
  transport.  They then show what ordinary data and state-passing can do in
  any dependent type theory, and nothing either way about HoTT's own
  identity-as-structure principle.

  Transcribed sources (read only; SHA-256 recorded in CLAIM.md):
    HoTT/formal/terra-t2-one-shot/OneShotCapability.agda   (Terra C-354 to C-356)
    HoTT/formal/terra-t1-h0-generic/H0AuditGeneric.agda     (Terra C-351 to C-353)
  Names follow the Agda originals, with Lean spelling (undo_law for undo-law).
-/

namespace CG001.TerraModelsUIP

/-! ## (a) Uniqueness of identity proofs holds in this kernel -/

theorem uip {α : Sort u} {a b : α} (p q : a = b) : p = q := rfl

#print axioms uip

/-! ## (b) T2: the one-shot authorization code (Terra C-354 to C-356) -/

def duplicate {A : Type} (x : A) : A × A := (x, x)

inductive Code where
  | authorizationCode

inductive Token where
  | accessToken

def duplicatedCode : Code × Code := duplicate Code.authorizationCode

theorem duplicateIsTwoCopies :
    duplicatedCode = (Code.authorizationCode, Code.authorizationCode) := rfl

def pureRedeem : Code → Token
  | .authorizationCode => .accessToken

def pureTwice (c : Code) : Token × Token := (pureRedeem c, pureRedeem c)

theorem pureCopiesBothGrant :
    pureTwice Code.authorizationCode = (Token.accessToken, Token.accessToken) := rfl

inductive Reply where
  | granted : Token → Reply
  | denied

inductive Status where
  | unused
  | consumed

inductive RedemptionEvent where
  | grantAttempt
  | denialAttempt

abbrev Server : Type := Status × List RedemptionEvent

def redeem : Code → Server → Reply × Server
  | .authorizationCode, (.unused, log) =>
      (.granted .accessToken, (.consumed, log ++ [.grantAttempt]))
  | .authorizationCode, (.consumed, log) =>
      (.denied, (.consumed, log ++ [.denialAttempt]))

def initialServer : Server := (.unused, [])

def firstAttempt : Reply × Server := redeem duplicatedCode.1 initialServer

def secondAttempt : Reply × Server := redeem duplicatedCode.2 firstAttempt.2

theorem firstCopyGrants : firstAttempt.1 = Reply.granted Token.accessToken := rfl

theorem secondCopyIsDenied : secondAttempt.1 = Reply.denied := rfl

theorem serverHasConsumedCode : secondAttempt.2.1 = Status.consumed := rfl

theorem bothAttemptsRecorded :
    secondAttempt.2.2 = [RedemptionEvent.grantAttempt, RedemptionEvent.denialAttempt] := rfl

#print axioms duplicateIsTwoCopies
#print axioms pureCopiesBothGrant
#print axioms firstCopyGrants
#print axioms secondCopyIsDenied
#print axioms serverHasConsumedCode
#print axioms bothAttemptsRecorded

/-! ## (c) T1: the H0 generic audit model (Terra C-351 to C-353)

  Terra's Agda module is parameterised by Content, Actor, Action, Metadata,
  apply, undo and undo-law; here they are explicit arguments.
-/

section H0

variable {Content Actor Action Metadata : Type}

def recordEvent (u : Actor) (a : Action) (before after : Content) (m : Metadata) :
    Actor × Action × Content × Content × Metadata :=
  (u, a, before, after, m)

def step (apply : Action → Content → Content) (u : Actor) (a : Action) (m : Metadata) :
    Content × List (Actor × Action × Content × Content × Metadata) →
    Content × List (Actor × Action × Content × Content × Metadata)
  | (c, log) => (apply a c, log ++ [recordEvent u a c (apply a c) m])

theorem appendAssoc {α : Type} :
    (xs ys zs : List α) → (xs ++ ys) ++ zs = xs ++ (ys ++ zs)
  | [], _, _ => rfl
  | x :: xs, ys, zs => congrArg (x :: ·) (appendAssoc xs ys zs)

-- Terra C-351: the content projection is restored, for any supplied metadata.
theorem contentUndo (apply : Action → Content → Content) (undo : Action → Action)
    (undo_law : ∀ a c, apply (undo a) (apply a c) = c)
    (u : Actor) (a : Action) (m₁ m₂ : Metadata) (c : Content)
    (log : List (Actor × Action × Content × Content × Metadata)) :
    (step apply u (undo a) m₂ (step apply u a m₁ (c, log))).1 = c :=
  undo_law a c

-- Terra C-352: both supplied metadata payloads survive in the same-step log.
theorem auditAppend (apply : Action → Content → Content) (undo : Action → Action)
    (u : Actor) (a : Action) (m₁ m₂ : Metadata) (c : Content)
    (log : List (Actor × Action × Content × Content × Metadata)) :
    (step apply u (undo a) m₂ (step apply u a m₁ (c, log))).2
      = log ++ [recordEvent u a c (apply a c) m₁,
                recordEvent u (undo a) (apply a c) (apply (undo a) (apply a c)) m₂] :=
  appendAssoc log [recordEvent u a c (apply a c) m₁]
    [recordEvent u (undo a) (apply a c) (apply (undo a) (apply a c)) m₂]

def initialState (c : Content) :
    Content × List (Actor × Action × Content × Content × Metadata) :=
  (c, [])

-- Terra C-353: at an empty log the complete state does not return.
theorem fullStateNotReturn (apply : Action → Content → Content) (undo : Action → Action)
    (u : Actor) (a : Action) (m₁ m₂ : Metadata) (c : Content) :
    step apply u (undo a) m₂ (step apply u a m₁ (initialState (Actor := Actor)
      (Action := Action) (Metadata := Metadata) c))
      ≠ initialState c := by
  intro p
  have h : (step apply u (undo a) m₂ (step apply u a m₁ (initialState (Actor := Actor)
      (Action := Action) (Metadata := Metadata) c))).2 = [] :=
    congrArg (fun s => s.2) p
  exact List.cons_ne_nil _ _ h

end H0

#print axioms appendAssoc
#print axioms contentUndo
#print axioms auditAppend
#print axioms fullStateNotReturn

end CG001.TerraModelsUIP
