import GodelQ.ZFC.CG008ShiftVec

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Vhelp
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗣𝗔⁻]

theorem le_of_succ_le_succ (a b : V) (h : a + 1 ≤ b + 1) : a ≤ b := by
  rcases le_or_gt a b with (h1 | h1)
  · exact h1
  · have hb : b + 1 ≤ a := succ_le_iff_lt.mpr h1
    have h3 : a + 1 ≤ a := le_trans h (le_trans hb (le_refl a))
    have h4 : a < a := succ_le_iff_lt.mp h3
    exact absurd h4 (_root_.lt_irrefl a)

end GodelQ.CG008Vhelp