/-
  The cast judgement of CG001-C-72, asked of the Lean kernel directly
  (Cloud-Opus audit, 2026-09-27).
  proof id : MP-COPUS-LEAN-C72-KERNEL-001

  The original negative control WrongCastFlips.lean is rejected in the
  elaborator: rfl fails because cast p true is not definitionally false.
  Behind it is one judgement of definitional equality: along any
  p : Bool = Bool, cast p true computes to true.  The kernel makes that
  judgement on its own, and here it is asked with no elaborator in between.
  addCastDecl states

      ∀ p : Bool = Bool, cast p true = r

  and offers fun p => Eq.refl r as the proof.  To accept it, the kernel must
  compute cast p true and compare the result with r.

  Positive half: r = true is accepted (kernelCastIsId), and it states exactly
  castIsId at b = true (kernelCastIsId_states_castIsId).
  Negative half: KernelCastFlips.lean.
-/
import Lean
import UniverseIsSet

open Lean Meta

namespace CopusLeanControls

/-- State `∀ p : Bool = Bool, cast p true = r`, offer `fun p => Eq.refl r`,
and hand both straight to the kernel as the theorem `name`. -/
def addCastDecl (name : Name) (r : Bool) : MetaM Unit := do
  let bool := mkConst ``Bool
  withLocalDeclD `p (← mkEq bool bool) fun p => do
    let castTrue := mkApp4 (mkConst ``cast [Level.one]) bool bool p (toExpr true)
    let statement ← mkForallFVars #[p] (← mkEq castTrue (toExpr r))
    let proof ← mkLambdaFVars #[p] (← mkEqRefl (toExpr r))
    addDecl (.thmDecl { name, levelParams := [], type := statement, value := proof })

run_meta addCastDecl `CopusLeanControls.kernelCastIsId true

/-- What the kernel accepted is `castIsId` at `b = true`. -/
theorem kernelCastIsId_states_castIsId :
    @kernelCastIsId = fun p => CG001.UniverseSetLean.castIsId p true := rfl

#print axioms kernelCastIsId
#print axioms kernelCastIsId_states_castIsId

end CopusLeanControls
