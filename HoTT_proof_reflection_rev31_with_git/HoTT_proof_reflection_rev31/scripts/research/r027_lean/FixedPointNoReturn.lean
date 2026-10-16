/- R027: ordinary Lean shared-fragment proof draft. NOT native HoTT.
   No new axioms, no sorry. Kernel status is in NATIVE_RUN.json, not in this header.
   This generic theorem does NOT prove ReachTrap for the R024 compiler. -/
import Lean
namespace R027
universe u

def run {S : Type u} (step : S → S) (q : S) : Nat → S
  | 0 => q
  | n + 1 => step (run step q n)

theorem run_add {S : Type u} (step : S → S) (q : S) (m n : Nat) :
    run step q (m + n) = run step (run step q m) n := by
  induction n with
  | zero => rfl
  | succ n ih => simp only [Nat.add_succ, run, ih]

def Trap {S : Type u} (step : S → S) (Returned : S → Prop) (q : S) : Prop :=
  (¬ Returned q) ∧ step q = q

theorem run_fixed {S : Type u} (step : S → S) (q : S)
    (hfix : step q = q) (n : Nat) : run step q n = q := by
  induction n with
  | zero => rfl
  | succ n ih => simp only [run, ih, hfix]

theorem fixed_point_no_return {S : Type u} (step : S → S) (Returned : S → Prop)
    (q : S) (htrap : Trap step Returned q) (n : Nat) :
    ¬ Returned (run step q n) := by
  rw [run_fixed step q htrap.2 n]
  exact htrap.1

theorem return_persists {S : Type u} (step : S → S) (Returned : S → Prop)
    (hp : ∀ q, Returned q → Returned (step q))
    (q : S) (hq : Returned q) (n : Nat) : Returned (run step q n) := by
  induction n with
  | zero => exact hq
  | succ n ih => exact hp (run step q n) ih

theorem initial_no_return {S : Type u} (step : S → S) (Returned : S → Prop)
    (hp : ∀ q, Returned q → Returned (step q))
    (q0 qt : S) (htrap : Trap step Returned qt)
    (m : Nat) (hreach : run step q0 m = qt) (n : Nat) :
    ¬ Returned (run step q0 n) := by
  intro hn
  cases Nat.le_total n m with
  | inl hnm =>
    obtain ⟨k, hk⟩ := Nat.exists_eq_add_of_le hnm
    have later : Returned (run step (run step q0 n) k) :=
      return_persists step Returned hp (run step q0 n) hn k
    have atM : Returned (run step q0 m) := by
      rw [hk, run_add]
      exact later
    exact htrap.1 (hreach ▸ atM)
  | inr hmn =>
    obtain ⟨k, hk⟩ := Nat.exists_eq_add_of_le hmn
    have atN : run step q0 n = qt := by
      rw [hk, run_add, hreach]
      exact run_fixed step qt htrap.2 k
    exact htrap.1 (atN ▸ hn)

#print axioms fixed_point_no_return
#print axioms initial_no_return
end R027
