/-
  The fact-world counterpart of CG001-C-63 and CG001-C-71 (Claude, session
  7f138325, 2026-09-26; goal CG-003, gate G4).

  proof id : MP-CG001-UNIVERSE-SET-LEAN-001
  claim    : CG001-C-72 (full statement in CLAIM.md)

  Lean 4 has uniqueness of identity proofs: equality is a proposition with
  definitional proof irrelevance.  So the universe is a set, and every
  self-identification of Bool acts on Bool as the identity.  In Cubical Agda
  the universe is not a set (C-63), and not even the universe of sets is a
  set (C-71): there, ua notEquiv is a self-identification of Bool that sends
  true to false.
-/
namespace CG001.UniverseSetLean

/-- Any two proofs that two types are equal are equal. -/
theorem universeIsSet {A B : Type} (p q : A = B) : p = q := rfl

/-- Casting along any proof of `Bool = Bool` leaves every boolean unchanged. -/
theorem castIsId (p : Bool = Bool) (b : Bool) : cast p b = b := rfl

/-- In particular no self-identification of Bool sends true to false. -/
theorem noFlip (p : Bool = Bool) : cast p true ≠ false := by
  rw [castIsId p true]
  exact Bool.noConfusion

end CG001.UniverseSetLean

#print axioms CG001.UniverseSetLean.universeIsSet
#print axioms CG001.UniverseSetLean.castIsId
#print axioms CG001.UniverseSetLean.noFlip
