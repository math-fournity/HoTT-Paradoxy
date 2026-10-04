/-!
Negative control for C-362.  A greatest natural action index must not be
silently introduced in order to turn the revised completion contract into the
strict one.
-/

theorem wrongStrictLastActionCompletion : ∃ last : Nat, ∀ action : Nat, action ≤ last := by
  refine ⟨0, ?_⟩
  intro action
  exact Nat.zero_le action
