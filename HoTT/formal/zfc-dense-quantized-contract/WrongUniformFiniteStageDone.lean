/-! Expected-rejection control: a dense positive dyadic remainder is not zero at stage four. -/

namespace WrongZFCDenseQuantizedContract

inductive NormalizedRemainder where
  | zero : NormalizedRemainder
  | dyadic : Nat → NormalizedRemainder

def denseRemaining (n : Nat) : NormalizedRemainder := .dyadic n
def DenseFiniteStageDone (n : Nat) : Prop := denseRemaining n = .zero

theorem wrong_dense_done_at_four : DenseFiniteStageDone 4 := by
  rfl

end WrongZFCDenseQuantizedContract
