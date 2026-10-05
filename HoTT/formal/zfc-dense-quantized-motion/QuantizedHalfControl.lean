/-!
`MP-ZFC-DENSE-QUANTIZED-MOTION-001` is a finite discrete control for the
user's dense-versus-quantized motion contrast.

It deliberately proves only a lattice process with a minimum unit:
`8 → 4 → 2 → 1 → 0`.  The dense counterpart is the separately verified C-361
real-analysis control.  This file is not a model or measurement of physical
spacetime, not a theorem about ZFC, and not a refutation of limit theory.
-/

namespace ZFCDenseQuantizedMotion

/-- Quantized remaining distance: one indivisible unit is consumed rather
    than divided into a smaller nonzero distance. -/
def quantizedHalf : Nat → Nat
  | 0 => 0
  | 1 => 0
  | n + 2 => (n + 2) / 2

def quantizedRun : Nat → Nat
  | 0 => 8
  | n + 1 => quantizedHalf (quantizedRun n)

def QuantizedDone (n : Nat) : Prop := quantizedRun n = 0

theorem quantized_stage_zero : quantizedRun 0 = 8 := rfl
theorem quantized_stage_one : quantizedRun 1 = 4 := rfl
theorem quantized_stage_two : quantizedRun 2 = 2 := rfl
theorem quantized_stage_three : quantizedRun 3 = 1 := rfl
theorem quantized_stage_four : quantizedRun 4 = 0 := rfl

theorem quantized_control_completes : QuantizedDone 4 :=
  quantized_stage_four

theorem quantized_control_not_done_at_three : ¬ (quantizedRun 3 = 0) := by
  intro stage
  have impossible : (1 : Nat) = 0 := quantized_stage_three.symm.trans stage
  cases impossible

theorem quantized_control_has_finite_completion :
    ∃ n : Nat, QuantizedDone n :=
  ⟨4, quantized_control_completes⟩

#print axioms quantized_stage_four
#print axioms quantized_control_completes
#print axioms quantized_control_not_done_at_three
#print axioms quantized_control_has_finite_completion

end ZFCDenseQuantizedMotion
