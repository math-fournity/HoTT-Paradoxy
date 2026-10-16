/-
  G2 generic Gödel baseline for GODEL-Q-REFLECTION-SOP.

  This wrapper does not instantiate the Foundation arithmetic theorems with
  set.mm, bare ZFC, a Zeno process, or fixed HoTT H0.  It pins the exact
  theorem interfaces that a later target-specific GodelizationCard would
  have to match: arithmetic strength, definability/recursively enumerable
  theory hypotheses, soundness or consistency, quotation/substitution and
  standard provability.
-/
import Foundation.FirstOrder.Incompleteness.First
import Foundation.FirstOrder.Incompleteness.Second

#check FFL.FirstOrder.Arithmetic.incomplete
#check FFL.FirstOrder.Arithmetic.consistent_unprovable

#print axioms FFL.FirstOrder.Arithmetic.incomplete
#print axioms FFL.FirstOrder.Arithmetic.consistent_unprovable
