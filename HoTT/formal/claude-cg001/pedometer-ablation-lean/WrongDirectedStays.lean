/-
  Negative control for CG001-C-52 (expected KERNEL_REJECTED).
  proof id : MP-CG001-PEDOMETER-ABLATION-LEAN-NEG-001

  In the directed model a round trip is two arrows, not an arrow and its
  inverse.  Claiming by rfl that the pedometer is unchanged after one round
  trip must be rejected: the kernel computes 2, not 0.
-/
import PedometerDirected

open CG001.PedometerDirected

theorem roundTrip_leaves_the_pedometer : carry roundTrip 0 = 0 := rfl
