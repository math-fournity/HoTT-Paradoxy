/-
R018 audit of ORDINARY Lean equality, not a HoTT formalization.
No mathlib dependency, new axioms or sorry in the proof declarations below.
STATUS: source supplied for verification; not compiled in this environment.
-/
import Lean

universe u

-- Ordinary Lean equality lives in proof-irrelevant Prop.
theorem audit_self_cast (A : Type u) (p : A = A) (a : A) : cast p a = a := by
  have hp : p = (rfl : A = A) := Subsingleton.elim _ _
  cases hp
  rfl

-- A loop in Lean Eq cannot implement Boolean negation.
theorem audit_bool_cast_not_false (p : Bool = Bool) :
    ¬ (cast p true = false) := by
  intro h
  have ht : cast p true = true := audit_self_cast Bool p true
  have contradiction : true = false := ht.symm.trans h
  cases contradiction

-- A subsingleton can be empty; uniqueness alone does not construct a witness.
theorem audit_empty_subsingleton :
    (∀ (x y : {n : Nat // False}), x = y) := by
  intro x y
  exact False.elim x.property

theorem audit_empty_no_witness : ¬ Nonempty {n : Nat // False} := by
  intro h
  cases h with
  | intro x => exact x.property

-- The proposed false beta law contradicts Lean's existing Eq.
theorem audit_incompatible_beta (p : Bool = Bool)
    (claimed_beta : cast p true = false) : False :=
  audit_bool_cast_not_false p claimed_beta

#print axioms audit_self_cast
#print axioms audit_bool_cast_not_false
#print axioms audit_empty_subsingleton
#print axioms audit_empty_no_witness
#print axioms audit_incompatible_beta
