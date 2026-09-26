/-
  The one-line definition of semi-simplicial structure, in Lean 4 core
  (Claude, session 7f138325, 2026-09-26; goal CG-002, gate G2).

  proof id : MP-CG001-WILD-SST-LEAN-001
  claim    : CG001-C-65 (full statement in CLAIM.md)

  The same definition as HoTT/formal/claude-cg001/wild-sst/WildSST.agda
  (CG001-C-64): Fin n by recursion (Unit ⊕ Fin n), weaken by recursion, the
  order by recursion, the record WildSST (simplices, face maps, and the
  semi-simplicial identities d_i d_{j+1} = d_j d_i for i ≤ j), and the two
  routes from d_i d_{j+1} d_{k+2} to d_k d_j d_i.

  Lean's equality is proof-irrelevant: any two proofs of the same equation are
  equal by rfl.  So the hexagon condition Coh2, which fails for the circle
  instance in Cubical Agda, holds here for every instance at once (theorem
  coh2).  When sameness is a mere fact, the one-line definition is already
  the whole definition.
-/

namespace CG001.WildSSTUIP

/-! ## Fin, weaken and the order, by recursion on n -/

def Fin' : Nat → Type
  | 0 => Empty
  | n + 1 => Sum Unit (Fin' n)

def fzero {n : Nat} : Fin' (n + 1) := Sum.inl ()

def fsuc {n : Nat} (i : Fin' n) : Fin' (n + 1) := Sum.inr i

def weaken : {n : Nat} → Fin' n → Fin' (n + 1)
  | 0, i => nomatch i
  | _ + 1, Sum.inl _ => Sum.inl ()
  | _ + 1, Sum.inr i => Sum.inr (weaken i)

def LeF : {n : Nat} → Fin' n → Fin' n → Prop
  | 0, _, _ => True
  | _ + 1, Sum.inl _, _ => True
  | _ + 1, Sum.inr _, Sum.inl _ => False
  | _ + 1, Sum.inr a, Sum.inr b => LeF a b

theorem LeF_trans : {n : Nat} → (a b c : Fin' n) → LeF a b → LeF b c → LeF a c
  | 0, a, _, _, _, _ => nomatch a
  | _ + 1, Sum.inl _, _, _, _, _ => trivial
  | _ + 1, Sum.inr _, Sum.inl _, _, h, _ => False.elim h
  | _ + 1, Sum.inr _, Sum.inr _, Sum.inl _, _, h => False.elim h
  | _ + 1, Sum.inr a, Sum.inr b, Sum.inr c, h₁, h₂ => LeF_trans a b c h₁ h₂

theorem weaken_le : {n : Nat} → (a b : Fin' n) → LeF a b → LeF (weaken a) (weaken b)
  | 0, a, _, _ => nomatch a
  | _ + 1, Sum.inl _, _, _ => trivial
  | _ + 1, Sum.inr _, Sum.inl _, h => False.elim h
  | _ + 1, Sum.inr a, Sum.inr b, h => weaken_le a b h

theorem weaken_le_fsuc : {n : Nat} → (a b : Fin' n) → LeF a b → LeF (weaken a) (fsuc b)
  | 0, a, _, _ => nomatch a
  | _ + 1, Sum.inl _, _, _ => trivial
  | _ + 1, Sum.inr _, Sum.inl _, h => False.elim h
  | _ + 1, Sum.inr a, Sum.inr b, h => weaken_le_fsuc a b h

/-! ## The definition -/

structure WildSST where
  X : Nat → Type
  d : (n : Nat) → Fin' (n + 2) → X (n + 1) → X n
  sid : ∀ (n : Nat) (i j : Fin' (n + 2)), LeF i j → ∀ x : X (n + 2),
    d n i (d (n + 1) (fsuc j) x) = d n j (d (n + 1) (weaken i) x)

/-! ## The two routes and the hexagon -/

section Routes

variable (S : WildSST)

theorem routeA (m : Nat) (i j k : Fin' (m + 2)) (p : LeF i j) (q : LeF j k)
    (x : S.X (m + 3)) :
    S.d m i (S.d (m + 1) (fsuc j) (S.d (m + 2) (fsuc (fsuc k)) x))
      = S.d m k (S.d (m + 1) (weaken j) (S.d (m + 2) (weaken (weaken i)) x)) :=
  (congrArg (S.d m i) (S.sid (m + 1) (fsuc j) (fsuc k) q x)).trans
    ((S.sid m i k (LeF_trans i j k p q) (S.d (m + 2) (weaken (fsuc j)) x)).trans
      (congrArg (S.d m k) (S.sid (m + 1) (weaken i) (weaken j) (weaken_le i j p) x)))

theorem routeB (m : Nat) (i j k : Fin' (m + 2)) (p : LeF i j) (q : LeF j k)
    (x : S.X (m + 3)) :
    S.d m i (S.d (m + 1) (fsuc j) (S.d (m + 2) (fsuc (fsuc k)) x))
      = S.d m k (S.d (m + 1) (weaken j) (S.d (m + 2) (weaken (weaken i)) x)) :=
  (S.sid m i j p (S.d (m + 2) (fsuc (fsuc k)) x)).trans
    ((congrArg (S.d m j) (S.sid (m + 1) (weaken i) (fsuc k)
        (weaken_le_fsuc i k (LeF_trans i j k p q)) x)).trans
      (S.sid m j k q (S.d (m + 2) (weaken (weaken i)) x)))

end Routes

def Coh2 (S : WildSST) : Prop :=
  ∀ (m : Nat) (i j k : Fin' (m + 2)) (p : LeF i j) (q : LeF j k) (x : S.X (m + 3)),
    routeA S m i j k p q x = routeB S m i j k p q x

/-- When sameness is a mere fact, the hexagon holds for every instance. -/
theorem coh2 (S : WildSST) : Coh2 S :=
  fun _ _ _ _ _ _ _ => rfl

#print axioms LeF_trans
#print axioms weaken_le
#print axioms weaken_le_fsuc
#print axioms coh2

end CG001.WildSSTUIP
