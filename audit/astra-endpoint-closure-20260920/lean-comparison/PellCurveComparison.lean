import DeformationCircle

/-! Same arithmetic recurrence as the original Agda M1, checked alongside the actual curve theorem.
This does not claim a general Agda-to-Lean translation. -/
open Set Topology
namespace AstraRealGeometry

def pellPair : ℕ → ℤ × ℤ
  | 0 => (1,1)
  | n+1 => let s := pellPair n; (s.1+2*s.2,s.1+s.2)

def pellDiscriminant (n : ℕ) : ℤ := (pellPair n).1^2 - 2*(pellPair n).2^2

theorem pellDiscriminant_step (n : ℕ) : pellDiscriminant (n+1) = -pellDiscriminant n := by
  simp only [pellDiscriminant,pellPair]
  ring

theorem pellDiscriminant_sign (n : ℕ) : pellDiscriminant n = 1 ∨ pellDiscriminant n = -1 := by
  induction n with
  | zero => right; norm_num [pellDiscriminant,pellPair]
  | succ n ih =>
    rw [pellDiscriminant_step]
    rcases ih with h | h
    · right; rw [h]
    · left; rw [h]; norm_num

theorem pellDiscriminant_never_zero (n : ℕ) : pellDiscriminant n ≠ 0 := by
  rcases pellDiscriminant_sign n with h | h <;> rw [h] <;> norm_num

theorem pell_and_continuous_curve :
    (∀ n : ℕ, pellDiscriminant n ≠ 0) ∧
    (∃ F : MotionTime → Interval → Plane,
      Continuous (fun z : MotionTime × Interval => F z.1 z.2) ∧
      (∀ t, IsEmbedding (F t)) ∧
      range (F timeStart) = lineOpen ∧ range (F timeEnd) = circleOpen) :=
  ⟨pellDiscriminant_never_zero, exists_curve_deformation⟩

#print axioms pellDiscriminant_never_zero
#print axioms pell_and_continuous_curve
end AstraRealGeometry
