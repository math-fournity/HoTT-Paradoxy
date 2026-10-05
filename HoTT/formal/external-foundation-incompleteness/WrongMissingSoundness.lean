/- Expected-rejection control: the source theorem requires Sigma-one soundness. -/
import Foundation.FirstOrder.Incompleteness.First

open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace FFL.FirstOrder.Arithmetic

theorem wrong_incomplete_without_sigma1_soundness
    (T : ArithmeticTheory) [T.Δ₁] [𝗥₀ ⪯ T] :
    Entailment.Incomplete T :=
  incomplete T

end FFL.FirstOrder.Arithmetic
