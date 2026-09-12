/-!
Independent Lean 4 finite models for two claims in the audit.

These theorems concern a two-element automorphism and a deliberately lossy
reduct.  They do not establish a general theorem about all HoTT models.
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

/-- A choice invariant under every automorphism would be fixed by `swap`. -/
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
