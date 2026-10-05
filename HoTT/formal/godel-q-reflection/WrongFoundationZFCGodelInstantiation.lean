/-
  Negative control: a SetTheory cannot directly be supplied where Foundation's
  generic incompleteness theorem requires an ArithmeticTheory.  A future
  target-specific G2 route must construct and verify an actual interpretation,
  not rely on co-location in the same source tree.
-/
import Foundation.FirstOrder.SetTheory.Universe
import Foundation.FirstOrder.Incompleteness.First

#check FFL.FirstOrder.Arithmetic.incomplete FFL.FirstOrder.SetTheory.ZermeloFraenkelChoice
