/-
  Kernel-level endpoint negative control for CG001-C-65 (Cloud-Opus audit,
  2026-09-27).
  proof id : MP-COPUS-LEAN-C65-KERNEL-NEG-001

  The same builder as in KernelRoute.lean (addRoute), which there produced a
  route the kernel accepted.  Only the third step is replaced: stepThreeWrong
  is the right rewrite applied under the wrong outer face map (S.d m i instead
  of S.d m k).  It is accepted on its own (see its #print axioms line), so the
  only thing wrong is where it starts and ends.
  Expected: the kernel itself rejects kernelRouteWrong, with a "(kernel)"
  message at the joint between step two and step three.
-/
import KernelRoute

open CG001.WildSSTUIP

namespace CopusLeanControls

theorem stepThreeWrong (S : WildSST) (m : Nat) (i j k : Fin' (m + 2)) (p : LeF i j) (_q : LeF j k)
    (x : S.X (m + 3)) :
    S.d m i (S.d (m + 1) (weaken i) (S.d (m + 2) (fsuc (weaken j)) x))
      = S.d m i (S.d (m + 1) (weaken j) (S.d (m + 2) (weaken (weaken i)) x)) :=
  congrArg (S.d m i) (S.sid (m + 1) (weaken i) (weaken j) (weaken_le i j p) x)

#print axioms stepThreeWrong

run_meta addRoute `CopusLeanControls.kernelRouteWrong ``stepOne ``stepTwo ``stepThreeWrong

end CopusLeanControls
