/-
  Route A of CG001-C-65, assembled by hand and handed straight to the Lean
  kernel (Cloud-Opus audit, 2026-09-27).
  proof id : MP-COPUS-LEAN-C65-KERNEL-001

  The three steps of route A are proved one by one (stepOne, stepTwo,
  stepThree), each with the full argument list of routeA.  addRoute then
  builds the chain

      Eq.trans stepOne (Eq.trans stepTwo stepThree)

  as a raw term with mkAppN, writing every endpoint out (the start and end of
  step one, the end of step two, the end of step three), and gives it to the
  kernel with Lean.addDecl under the statement of routeA.  mkAppN checks
  nothing, and addDecl does not go through the elaborator: only the kernel
  decides whether each step starts where the previous one ends and whether the
  chain ends at the target.  (Step two ends at weaken (fsuc j), step three
  starts at fsuc (weaken j): the kernel has to unfold weaken to join them.)

  Positive half: with the right third step the kernel accepts the route
  (kernelRouteA), and kernelRouteA states exactly routeA
  (kernelRouteA_states_routeA).  Negative half: KernelRouteEndpoint.lean.
-/
import Lean
import WildSSTUIP

open Lean Meta
open CG001.WildSSTUIP

namespace CopusLeanControls

theorem stepOne (S : WildSST) (m : Nat) (i j k : Fin' (m + 2)) (_p : LeF i j) (q : LeF j k)
    (x : S.X (m + 3)) :
    S.d m i (S.d (m + 1) (fsuc j) (S.d (m + 2) (fsuc (fsuc k)) x))
      = S.d m i (S.d (m + 1) (fsuc k) (S.d (m + 2) (weaken (fsuc j)) x)) :=
  congrArg (S.d m i) (S.sid (m + 1) (fsuc j) (fsuc k) q x)

theorem stepTwo (S : WildSST) (m : Nat) (i j k : Fin' (m + 2)) (p : LeF i j) (q : LeF j k)
    (x : S.X (m + 3)) :
    S.d m i (S.d (m + 1) (fsuc k) (S.d (m + 2) (weaken (fsuc j)) x))
      = S.d m k (S.d (m + 1) (weaken i) (S.d (m + 2) (weaken (fsuc j)) x)) :=
  S.sid m i k (LeF_trans i j k p q) (S.d (m + 2) (weaken (fsuc j)) x)

theorem stepThree (S : WildSST) (m : Nat) (i j k : Fin' (m + 2)) (p : LeF i j) (_q : LeF j k)
    (x : S.X (m + 3)) :
    S.d m k (S.d (m + 1) (weaken i) (S.d (m + 2) (fsuc (weaken j)) x))
      = S.d m k (S.d (m + 1) (weaken j) (S.d (m + 2) (weaken (weaken i)) x)) :=
  congrArg (S.d m k) (S.sid (m + 1) (weaken i) (weaken j) (weaken_le i j p) x)

/-- Build `Eq.trans s₁ (Eq.trans s₂ s₃)` under the statement of `routeA`, every
endpoint written out, and hand it to the kernel as the theorem `name`.
`mkAppN` only assembles the term; the kernel is the only checker. -/
def addRoute (name s₁ s₂ s₃ : Name) : MetaM Unit := do
  let statement := (← getConstInfo ``routeA).type
  let proof ← forallTelescope statement fun xs _ => do
    let h₁ := mkAppN (mkConst s₁) xs
    let h₂ := mkAppN (mkConst s₂) xs
    let h₃ := mkAppN (mkConst s₃) xs
    let some (α, a, b) := (← inferType h₁).eq? | throwError "step one is not an equation"
    let some (_, _, c) := (← inferType h₂).eq? | throwError "step two is not an equation"
    let some (_, _, d) := (← inferType h₃).eq? | throwError "step three is not an equation"
    let trans := mkConst ``Eq.trans [← getLevel α]
    mkLambdaFVars xs (mkAppN trans #[α, a, b, d, h₁, mkAppN trans #[α, b, c, d, h₂, h₃]])
  addDecl (.thmDecl { name, levelParams := [], type := statement, value := proof })

run_meta addRoute `CopusLeanControls.kernelRouteA ``stepOne ``stepTwo ``stepThree

/-- The route the kernel accepted states exactly `routeA`. -/
theorem kernelRouteA_states_routeA : @kernelRouteA = @routeA := rfl

#print axioms kernelRouteA
#print axioms kernelRouteA_states_routeA

end CopusLeanControls
