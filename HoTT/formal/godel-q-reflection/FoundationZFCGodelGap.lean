/-
  Positive source control for the target-mapping gap.

  Foundation has an actual first-order ZFC SetTheory and proves its consistency
  relative to the surrounding Lean model.  This wrapper checks that source
  fact alongside the generic ArithmeticTheory incompleteness theorem, without
  asserting they have already been instantiated together.
-/
import Foundation.FirstOrder.SetTheory.Universe
import Foundation.FirstOrder.Incompleteness.First
import Foundation.FirstOrder.Incompleteness.Second

#check FFL.FirstOrder.SetTheory.ZermeloFraenkelChoice
#check FFL.FirstOrder.SetTheory.zfc_consistent
#check FFL.FirstOrder.Arithmetic.incomplete
#check FFL.FirstOrder.Arithmetic.consistent_unprovable

#print axioms FFL.FirstOrder.SetTheory.zfc_consistent
