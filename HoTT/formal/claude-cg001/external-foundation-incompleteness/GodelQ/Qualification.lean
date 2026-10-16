/-
  GZ-002 / MP-FOUNDATION-INCOMPLETENESS-R3-001 qualification probe.

  It checks only the frozen Foundation Lean first-order arithmetic theorem.
  It does not instantiate an exact HoTT calculus, ZFC, an acceptance policy,
  or an OriginDone bridge.
-/
import Foundation.FirstOrder.Incompleteness.First

open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace FFL.FirstOrder.Arithmetic

#check incomplete
#check incomplete_of_RE
#check exists_true_but_unprovable_sentence_of_sigma1sound
#check exists_true_but_unprovable_sentence_of_RE_of_sigma1sound

#print axioms incomplete
#print axioms incomplete_of_RE
#print axioms exists_true_but_unprovable_sentence_of_sigma1sound
#print axioms exists_true_but_unprovable_sentence_of_RE_of_sigma1sound

end FFL.FirstOrder.Arithmetic
