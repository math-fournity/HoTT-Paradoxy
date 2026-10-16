/-! Expected rejection control: the fixed lattice process is not done at stage 3. -/

namespace WrongZFCDenseQuantizedMotion

def quantizedHalf : Nat → Nat
  | 0 => 0
  | 1 => 0
  | n + 2 => (n + 2) / 2

def quantizedRun : Nat → Nat
  | 0 => 8
  | n + 1 => quantizedHalf (quantizedRun n)

theorem wrong_quantized_done_at_three : quantizedRun 3 = 0 := by
  rfl

end WrongZFCDenseQuantizedMotion
