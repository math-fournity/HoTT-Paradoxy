/-
  Endpoint negative control for CG001-C-65 (Cloud-Opus audit, 2026-09-27).
  proof id : MP-COPUS-LEAN-C65-ENDPOINT-NEG-001

  Why this file exists.  The original control WrongRoute.lean says that its
  last step "no longer fits between the previous endpoint and the target, so
  the kernel must reject it", and that this "shows the route bookkeeping is
  checked".  Its replay shows something else: the error is reported at the
  argument of that step (weaken_le i j p proves LeF (weaken i) (weaken j),
  the step asks for LeF (weaken j) (weaken i)), so the run cannot show
  whether endpoints are compared; and the error comes from the elaborator,
  not from the kernel.

  Here the third step is proved on its own first (stepThreeWrongFace, accepted:
  see its #print axioms line).  It is the right rewrite applied under the
  wrong outer face map, S.d m i instead of S.d m k.  So it starts where the
  second step does not end, and it ends away from the target.
  Expected: this file is rejected at wrongRouteEndpoint, with a type mismatch
  whose two sides differ in that outer face map (and otherwise only by the
  unfolding weaken (fsuc j) = fsuc (weaken j)).  The same broken chain handed
  straight to the kernel is KernelRouteEndpoint.lean.
-/
import WildSSTUIP

open CG001.WildSSTUIP

namespace CopusLeanControls

/-- The third step alone: a well-typed equation. -/
theorem stepThreeWrongFace (S : WildSST) (m : Nat) (i j : Fin' (m + 2)) (p : LeF i j)
    (x : S.X (m + 3)) :
    S.d m i (S.d (m + 1) (weaken i) (S.d (m + 2) (fsuc (weaken j)) x))
      = S.d m i (S.d (m + 1) (weaken j) (S.d (m + 2) (weaken (weaken i)) x)) :=
  congrArg (S.d m i) (S.sid (m + 1) (weaken i) (weaken j) (weaken_le i j p) x)

#print axioms stepThreeWrongFace

/-- Route A with that third step: steps one and two exactly as in routeA. -/
theorem wrongRouteEndpoint (S : WildSST) (m : Nat) (i j k : Fin' (m + 2)) (p : LeF i j)
    (q : LeF j k) (x : S.X (m + 3)) :
    S.d m i (S.d (m + 1) (fsuc j) (S.d (m + 2) (fsuc (fsuc k)) x))
      = S.d m k (S.d (m + 1) (weaken j) (S.d (m + 2) (weaken (weaken i)) x)) :=
  (congrArg (S.d m i) (S.sid (m + 1) (fsuc j) (fsuc k) q x)).trans
    ((S.sid m i k (LeF_trans i j k p q) (S.d (m + 2) (weaken (fsuc j)) x)).trans
      (stepThreeWrongFace S m i j p x))

end CopusLeanControls
