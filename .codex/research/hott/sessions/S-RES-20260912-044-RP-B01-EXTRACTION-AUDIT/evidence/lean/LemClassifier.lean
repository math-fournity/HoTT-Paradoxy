-- N2 audit: a classical LEM classifier is a well-typed object-layer function.
-- Question: does the default Lean evaluation/compilation interface silently
-- deliver an effective implementation, or does it refuse?
axiom lem : (P : Prop) → P ∨ ¬P

open Classical

-- Control 3: the LEM-based mathematical classifier chi.
noncomputable def chi (P : Prop) : Bool :=
  if P then true else false

-- Control 2: classical branches with equal constants.
noncomputable def equalConst (P : Prop) : Bool :=
  if P then true else true

-- Control 1: bounded-step halt detection (total, no LEM).
def haltWithin (_n : Nat) : Bool := true

#eval haltWithin 5
#eval chi True

-- Control 4: the explicit unsafe escape hatch. This is a contract change,
-- not a default delivery of an implementation.
#eval! chi True
