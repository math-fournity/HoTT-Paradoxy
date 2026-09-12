/-!
Second-system specification for the finite automorphism obstruction.
This file is intentionally self-contained Lean 4 source.  It was not locally
compiled in the current runtime because no Lean executable was available.
-/

inductive Event where
  | left
  | right
  deriving DecidableEq

open Event

def swap : Event → Event
  | left  => right
  | right => left

theorem swap_no_fixed_point (x : Event) : swap x ≠ x := by
  cases x <;> simp [swap]

/-- A choice natural under every automorphism would in particular be fixed by swap. -/
theorem no_swap_invariant_choice : ¬ ∃ x : Event, swap x = x := by
  intro h
  rcases h with ⟨x, hx⟩
  exact swap_no_fixed_point x hx

inductive World where
  | forward
  | backward
  deriving DecidableEq

inductive Direction where
  | ab
  | ba
  deriving DecidableEq

/-- The reduct/core is the same unit value in both worlds. -/
def core : World → Unit := fun _ => ()

def direction : World → Direction
  | World.forward  => Direction.ab
  | World.backward => Direction.ba

theorem no_direction_decoder :
    ¬ ∃ decode : Unit → Direction, ∀ w, decode (core w) = direction w := by
  intro h
  rcases h with ⟨decode, exactness⟩
  have hf := exactness World.forward
  have hb := exactness World.backward
  have : Direction.ab = Direction.ba := hf.symm.trans hb
  cases this
