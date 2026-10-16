/-
  The directed model of the pedometer ablation, checked again in Lean 4
  (Claude, session 91a6cdaa, 2026-09-25).

  proof id : MP-CG001-PEDOMETER-ABLATION-LEAN-001
  claim    : CG001-C-52, an independent second-kernel check of CG001-C-51
             (full statement in CLAIM.md)

  Lean's equality has uniqueness of identity proofs, so nothing in this file
  is a statement about HoTT paths.  The free category on the graph
  west -go-> east -back-> west is a set-level object, and every statement here
  is about that model only.  The HoTT side of the ablation (C-49, C-50) is
  checked in Cubical Agda (package pedometer-ablation), and C-49 again in Rzk
  (package pedometer-ablation-rzk).

  C-52 (a) walks form a category (unit and associativity laws);
       (b) the pedometer (fibre Nat at each town, +1 along each step) is a
           functor, with unique lifts;
       (c) every walk adds its length, so no walk lowers the pedometer and
           every nonempty walk strictly raises it; the round trip adds 2;
       (d) the stop-at-+2 search halts at fuel 1 with answer 1;
       (e) go has no inverse walk; the round trip is not the identity walk.
  The axioms each theorem depends on are printed at the end of the file.
-/

namespace CG001.PedometerDirected

inductive Town where
  | west
  | east

inductive Step : Town → Town → Type where
  | go   : Step .west .east
  | back : Step .east .west

inductive Walk : Town → Town → Type where
  | stay {x : Town} : Walk x x
  | next {x y z : Town} : Step x y → Walk y z → Walk x z

namespace Walk

def append : {x y z : Town} → Walk x y → Walk y z → Walk x z
  | _, _, _, stay, v => v
  | _, _, _, next s w, v => next s (append w v)

def length : {x y : Town} → Walk x y → Nat
  | _, _, stay => 0
  | _, _, next _ w => length w + 1

-- (a) the category laws (append stay w = w holds by definition)
theorem append_stay : ∀ {x y : Town} (w : Walk x y), append w stay = w
  | _, _, stay => rfl
  | _, _, next s w => congrArg (next s) (append_stay w)

theorem append_assoc : ∀ {x y z t : Town} (u : Walk x y) (v : Walk y z) (w : Walk z t),
    append (append u v) w = append u (append v w)
  | _, _, _, _, stay, _, _ => rfl
  | _, _, _, _, next s u, v, w => congrArg (next s) (append_assoc u v w)

end Walk

open Walk

-- (b) the pedometer
def carry : {x y : Town} → Walk x y → Nat → Nat
  | _, _, stay, n => n
  | _, _, next _ w, n => carry w (n + 1)

theorem carry_stay {x : Town} (n : Nat) : carry (stay : Walk x x) n = n := rfl

theorem carry_append : ∀ {x y z : Town} (w : Walk x y) (v : Walk y z) (n : Nat),
    carry (append w v) n = carry v (carry w n)
  | _, _, _, stay, _, _ => rfl
  | _, _, _, next _ w, v, n => carry_append w v (n + 1)

theorem unique_lift {x y : Town} (w : Walk x y) (n : Nat) :
    ∃ m, carry w n = m ∧ ∀ m', carry w n = m' → m' = m :=
  ⟨carry w n, rfl, fun _ h => h.symm⟩

-- (c) the pedometer adds the length of the walk
theorem carry_length : ∀ {x y : Town} (w : Walk x y) (n : Nat), carry w n = w.length + n
  | _, _, stay, n => (Nat.zero_add n).symm
  | _, _, next _ w, n =>
      (carry_length w (n + 1)).trans
        ((Nat.add_assoc w.length n 1).symm.trans (Nat.add_right_comm w.length 1 n).symm)

theorem never_lowers {x y : Town} (w : Walk x y) (n : Nat) : n ≤ carry w n :=
  (carry_length w n).symm ▸ Nat.le_add_left n w.length

theorem every_step_raises {x y z : Town} (s : Step x y) (w : Walk y z) (n : Nat) :
    n < carry (next s w) n :=
  (carry_length w (n + 1)).symm ▸
    Nat.lt_of_lt_of_le (Nat.lt_succ_self n) (Nat.le_add_left (n + 1) w.length)

def roundTrip : Walk .west .west := next .go (next .back stay)

theorem roundTrip_adds_two (n : Nat) : carry roundTrip n = n + 2 := rfl

-- (d) the stop-at-+2 process halts
def rounds : Nat → Walk .west .west
  | 0 => stay
  | k + 1 => append (rounds k) roundTrip

def after (k : Nat) : Nat := carry (rounds k) 0

def scan (P : Nat → Bool) : Nat → Nat → Option Nat
  | k, 0 => if P k then some k else none
  | k, fuel + 1 => if P k then some k else scan P (k + 1) fuel

def run (fuel : Nat) : Option Nat := scan (fun k => after k == 2) 0 fuel

theorem after_zero : after 0 = 0 := rfl
theorem after_one : after 1 = 2 := rfl
theorem halts : run 1 = some 1 := rfl

-- (e) no inverses
theorem go_has_no_inverse : ¬ ∃ w : Walk .east .west, next .go w = stay :=
  fun ⟨_, h⟩ => Nat.noConfusion (congrArg Walk.length h)

theorem roundTrip_ne_stay : roundTrip ≠ stay :=
  fun h => Nat.noConfusion (congrArg Walk.length h)

end CG001.PedometerDirected

#print axioms CG001.PedometerDirected.Walk.append_stay
#print axioms CG001.PedometerDirected.Walk.append_assoc
#print axioms CG001.PedometerDirected.carry_append
#print axioms CG001.PedometerDirected.unique_lift
#print axioms CG001.PedometerDirected.carry_length
#print axioms CG001.PedometerDirected.never_lowers
#print axioms CG001.PedometerDirected.every_step_raises
#print axioms CG001.PedometerDirected.roundTrip_adds_two
#print axioms CG001.PedometerDirected.halts
#print axioms CG001.PedometerDirected.go_has_no_inverse
#print axioms CG001.PedometerDirected.roundTrip_ne_stay
