/-
  Kernel-level negative control for CG001-C-72 (Cloud-Opus audit, 2026-09-27).
  proof id : MP-COPUS-LEAN-C72-KERNEL-NEG-001

  The same builder as in KernelCast.lean (addCastDecl), which there produced a
  theorem the kernel accepted, now with r = false: the statement is
  "∀ p : Bool = Bool, cast p true = false" and the offered proof is
  fun p => Eq.refl false.  The kernel must compute cast p true; it gets true,
  not false.
  Expected: the kernel itself rejects kernelCastFlips, with a "(kernel)"
  declaration type mismatch.
-/
import KernelCast

namespace CopusLeanControls

run_meta addCastDecl `CopusLeanControls.kernelCastFlips false

end CopusLeanControls
