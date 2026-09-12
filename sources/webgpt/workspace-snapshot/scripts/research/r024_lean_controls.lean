/- Comparison fixtures for ordinary Lean, NOT a HoTT model. NOT_RUN in R024.
   Run this positive-control file only in a version-pinned Lean environment.
   Negative fixture is a separate file; never hide failure using sorry. -/
import Lean

def ignoreDecision (P : Prop) (_d : Decidable P) : Nat := 0
noncomputable def ignoreClassical (P : Prop) : Nat :=
  ignoreDecision P (Classical.propDecidable P)

example (P : Prop) : ignoreClassical P = 0 := by rfl
example : 2 + 2 = 4 := by decide

#print axioms ignoreClassical
-- This source is not asserted compiled. It illustrates dead classical input;
-- syntactic classical dependence does not prove semantic noncomputability.
