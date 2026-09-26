/-
  Negative control for CG001-C-65 (expected KERNEL_REJECTED).
  proof id : MP-CG001-WILD-SST-LEAN-NEG-001

  Route A with its last rewrite applied to the pair in the wrong order
  (weaken j, weaken i instead of weaken i, weaken j).  The step no longer
  fits between the previous endpoint and the target, so the kernel must
  reject it.  This shows the route bookkeeping is checked, not merely parsed.
-/
import WildSSTUIP

open CG001.WildSSTUIP

theorem wrongRouteA (S : WildSST) (m : Nat) (i j k : Fin' (m + 2)) (p : LeF i j)
    (q : LeF j k) (x : S.X (m + 3)) :
    S.d m i (S.d (m + 1) (fsuc j) (S.d (m + 2) (fsuc (fsuc k)) x))
      = S.d m k (S.d (m + 1) (weaken j) (S.d (m + 2) (weaken (weaken i)) x)) :=
  (congrArg (S.d m i) (S.sid (m + 1) (fsuc j) (fsuc k) q x)).trans
    ((S.sid m i k (LeF_trans i j k p q) (S.d (m + 2) (weaken (fsuc j)) x)).trans
      (congrArg (S.d m k) (S.sid (m + 1) (weaken j) (weaken i) (weaken_le i j p) x)))
