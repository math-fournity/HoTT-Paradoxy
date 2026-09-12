/- Ordinary Lean shared fragment, NOT native HoTT. Not compiled in this run.
   No new axioms or sorry. This proves a consequence of a PARAMETERIZED hypothesis,
   not ReachTrap of the concrete R024 compiler. -/
namespace R028
universe u

def run {S : Type u} (step : S → S) (q : S) : Nat → S
  | 0 => q
  | n + 1 => step (run step q n)

def Trap {S : Type u} (step : S → S) (R : S → Prop) (q : S) : Prop :=
  step q = q ∧ ¬ R q

def ReachTrap {S : Type u} (step : S → S) (R : S → Prop) (q : S) : Prop :=
  ∃ m qt, run step q m = qt ∧ Trap step R qt

theorem returned_persists {S : Type u} (step : S → S) (R : S → Prop)
    (pres : ∀ q, R q → R (step q)) (q : S) (hq : R q) (n : Nat) :
    R (run step q n) := by
  induction n with
  | zero => exact hq
  | succ n ih => exact pres (run step q n) ih

theorem reaches_trap_excludes_initial_return {S : Type u} (step : S → S)
    (R : S → Prop) (pres : ∀ q, R q → R (step q)) (q : S)
    (hreach : ReachTrap step R q) : ¬ R q := by
  intro hr
  obtain ⟨m, qt, heq, ht⟩ := hreach
  have hm : R (run step q m) := returned_persists step R pres q hr m
  rw [heq] at hm
  exact ht.2 hm

theorem universal_reach_forces_empty_return {S : Type u} (step : S → S)
    (R : S → Prop) (pres : ∀ q, R q → R (step q))
    (all : ∀ q, ReachTrap step R q) : ∀ q, ¬ R q := by
  intro q
  exact reaches_trap_excludes_initial_return step R pres q (all q)

theorem universal_reach_conflicts_with_return_witness {S : Type u}
    (step : S → S) (R : S → Prop) (pres : ∀ q, R q → R (step q))
    (all : ∀ q, ReachTrap step R q) (witness : ∃ q, R q) : False := by
  obtain ⟨q, hq⟩ := witness
  exact universal_reach_forces_empty_return step R pres all q hq

-- The universal assumptions themselves can have a model: no returned states.
example : ∀ q : Nat, ReachTrap (fun _ => 0) (fun _ => False) q := by
  intro q
  exact ⟨1, 0, rfl, rfl, fun h => h⟩

#print axioms universal_reach_forces_empty_return
#print axioms universal_reach_conflicts_with_return_witness
end R028
