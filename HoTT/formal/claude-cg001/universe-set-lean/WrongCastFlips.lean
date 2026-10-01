/-
  Negative control for CG001-C-72 (expected KERNEL_REJECTED).
  proof id : MP-CG001-UNIVERSE-SET-LEAN-NEG-001

  Claiming by computation that some cast along a proof of Bool = Bool sends
  true to false, as ua notEquiv does in Cubical Agda, must be rejected in
  Lean: the cast reduces to the identity.
-/
import UniverseIsSet

theorem castFlips (p : Bool = Bool) : cast p true = false := rfl
