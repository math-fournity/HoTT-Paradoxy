/-!
Expected-negative control for MP-T-PRECISION-TDIAG-001.

The context has a self-code and the diagonal completion contract, but accepts
the code while its originDone predicate is False.  This file falsely asserts
the missing bridge.  Lean must reject the attempt rather than deriving a
contradiction from self-reference alone.
-/

namespace WrongAcceptanceDiagonal

inductive OneCode where
  | only

structure DiagonalContext (Code : Type) where
  step : Code → Code
  selfCode : Code
  accept : Code → Prop
  originDone : Code → Prop
  fixed : step selfCode = selfCode
  diagonalContract : originDone (step selfCode) ↔ ¬ accept selfCode

def Bridge {Code : Type} (context : DiagonalContext Code) : Prop :=
  context.accept context.selfCode → context.originDone (context.step context.selfCode)

def bridgeMissingControl : DiagonalContext OneCode where
  step := fun _ => .only
  selfCode := .only
  accept := fun _ => True
  originDone := fun _ => False
  fixed := rfl
  diagonalContract := by
    constructor
    · intro impossible
      exact False.elim impossible
    · intro not_true
      exact not_true True.intro

theorem wrong_bridge : Bridge bridgeMissingControl := by
  intro accepted
  exact accepted

end WrongAcceptanceDiagonal
