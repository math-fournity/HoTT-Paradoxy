/-!
`MP-ZFC-DENSE-QUANTIZED-CONTRACT-001` is a symbolic finite-stage control.

It gives a common normalized state space for two already separate controls:
the C-361 dense geometric remainder and C-370's finite quantized process.
`dyadic n` represents the nonzero remainder `2⁻ⁿ`; `zero` is exact arrival.
This file does not establish the real-analysis facts of C-361, reuse C-370's
source implementation, model physical spacetime, or state anything about ZFC.
-/

namespace ZFCDenseQuantizedContract

inductive NormalizedRemainder where
  | zero : NormalizedRemainder
  | dyadic : Nat → NormalizedRemainder
deriving DecidableEq, Repr

/-- Symbolic normalized dense remainder: `dyadic n` represents `2⁻ⁿ`. -/
def denseRemaining (n : Nat) : NormalizedRemainder := .dyadic n

/-- A finite-minimum-unit counterpart.  It follows the same first four
    normalized half stages and then consumes the indivisible final unit. -/
def quantizedRemaining : Nat → NormalizedRemainder
  | 0 => .dyadic 0
  | 1 => .dyadic 1
  | 2 => .dyadic 2
  | 3 => .dyadic 3
  | _ => .zero

def DenseFiniteStageDone (n : Nat) : Prop := denseRemaining n = .zero
def QuantizedFiniteStageDone (n : Nat) : Prop := quantizedRemaining n = .zero

theorem shared_normalized_start :
    denseRemaining 0 = quantizedRemaining 0 := rfl

theorem shared_stage_one :
    denseRemaining 1 = quantizedRemaining 1 := rfl

theorem shared_stage_two :
    denseRemaining 2 = quantizedRemaining 2 := rfl

theorem shared_stage_three :
    denseRemaining 3 = quantizedRemaining 3 := rfl

theorem dense_not_done (n : Nat) : ¬ DenseFiniteStageDone n := by
  intro h
  cases h

theorem dense_has_no_finite_stage_completion :
    ¬ ∃ n : Nat, DenseFiniteStageDone n := by
  intro h
  cases h with
  | intro n hn => exact dense_not_done n hn

theorem quantized_done_at_four : QuantizedFiniteStageDone 4 := rfl

theorem quantized_not_done_at_three : ¬ QuantizedFiniteStageDone 3 := by
  intro h
  cases h

theorem finite_stage_done_not_pointwise_equivalent :
    ¬ (∀ n : Nat, DenseFiniteStageDone n ↔ QuantizedFiniteStageDone n) := by
  intro h
  have denseDoneAtFour : DenseFiniteStageDone 4 := (h 4).mpr quantized_done_at_four
  exact dense_not_done 4 denseDoneAtFour

#print axioms shared_normalized_start
#print axioms dense_has_no_finite_stage_completion
#print axioms quantized_done_at_four
#print axioms quantized_not_done_at_three
#print axioms finite_stage_done_not_pointwise_equivalent

end ZFCDenseQuantizedContract
