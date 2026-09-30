/-
  The fact-world instance of the questioning program (Claude, cloud session
  01FJANnV, 2026-09-30).

  proof id : MP-CG001-QUESTIONING-DELAY-LEAN-001
  claim    : CG001-C-80 (full statement in HoTT/formal/claude-cg001/questioning-delay/CLAIM.md)

  QuestioningDelay.agda (CG001-C-77) writes the questioning process Q as a
  program in the delay monad.  Its fuel-bounded run obeys three equations
  (runYes, runNoZero, runNoSuc there, all by refl):

      the judge says yes at level k           : the run returns k, whatever the fuel;
      the judge says no at level k, fuel 0     : the run returns nothing;
      the judge says no at level k, fuel n+1   : the run is the run from level k+1 with fuel n.

  Lean 4 has no coinductive types in its kernel, so here the same process is
  written directly as its fuel-bounded run, defined by exactly these three
  equations, and the judge has the same shape: at every level k, a decision
  whether C is settled at level k+1.

  h-levels use the clauses of the cubical library's isOfHLevel.  Lean's
  equality is a proposition with proof irrelevance (uniqueness of identity
  proofs), so the identity types of any type are propositions and the
  recursion continues in IsOfHLevelProp; level 0 uses the existential, the
  proposition-valued form of isContr.

  Result: every type is a set, the universe Type included (C-72), so for
  every judge the questioning of Type stops at step 1 and returns 1, at
  every fuel.  A judge for Type exists (it answers no at level 0, because
  Unit and Empty are different types, and yes at every level from 1 on).
-/
namespace CG001.QuestioningLean

universe u

/-- h-levels of a proposition. -/
def IsOfHLevelProp : Nat → Prop → Prop
  | 0, A => ∃ a : A, ∀ b : A, a = b
  | 1, A => ∀ a b : A, a = b
  | n + 2, A => ∀ a b : A, IsOfHLevelProp (n + 1) (a = b)

/-- h-levels of a type, with the clauses of the cubical library's isOfHLevel. -/
def IsOfHLevel : Nat → Sort u → Prop
  | 0, A => ∃ a : A, ∀ b : A, a = b
  | 1, A => ∀ a b : A, a = b
  | n + 2, A => ∀ a b : A, IsOfHLevelProp (n + 1) (a = b)

/-- A judge answers, at every level k, whether C is settled at level k+1. -/
def Judge (C : Sort u) : Type := (k : Nat) → Decidable (IsOfHLevel (k + 1) C)

/-- The fuel-bounded run of the questioning process, started at level k. -/
def runFrom (C : Sort u) (judge : Judge C) : Nat → Nat → Option Nat
  | k, 0 =>
    match judge k with
    | isTrue _ => some k
    | isFalse _ => none
  | k, fuel + 1 =>
    match judge k with
    | isTrue _ => some k
    | isFalse _ => runFrom C judge (k + 1) fuel

/-- The questioning process starts at level 1 (is C a set?). -/
def question (C : Sort u) (judge : Judge C) (fuel : Nat) : Option Nat :=
  runFrom C judge 1 fuel

/-- The three equations, stated with the judge's answer. -/
theorem runYes (C : Sort u) (judge : Judge C) (k fuel : Nat) (h : IsOfHLevel (k + 1) C)
    (e : judge k = isTrue h) : runFrom C judge k fuel = some k := by
  cases fuel <;> rw [runFrom, e]

theorem runNoZero (C : Sort u) (judge : Judge C) (k : Nat) (nh : ¬ IsOfHLevel (k + 1) C)
    (e : judge k = isFalse nh) : runFrom C judge k 0 = none := by
  rw [runFrom, e]

theorem runNoSucc (C : Sort u) (judge : Judge C) (k n : Nat) (nh : ¬ IsOfHLevel (k + 1) C)
    (e : judge k = isFalse nh) : runFrom C judge k (n + 1) = runFrom C judge (k + 1) n := by
  rw [runFrom, e]

/-- If C is settled at level k+1, the run from level k returns k, whatever the judge and the fuel. -/
theorem settledAt (C : Sort u) (judge : Judge C) (k fuel : Nat) (h : IsOfHLevel (k + 1) C) :
    runFrom C judge k fuel = some k := by
  cases e : judge k with
  | isTrue h' => exact runYes C judge k fuel h' e
  | isFalse nh => exact absurd h nh

/-- Every proposition is of every h-level from 1 on (proof irrelevance). -/
theorem propLevels : (n : Nat) → (P : Prop) → IsOfHLevelProp (n + 1) P
  | 0, _ => fun _ _ => rfl
  | n + 1, _ => fun a b => propLevels n (a = b)

/-- Every type is of every h-level from 2 on; in particular every type is a set. -/
theorem higherLevels (C : Sort u) (k : Nat) : IsOfHLevel (k + 2) C :=
  fun a b => propLevels k (a = b)

theorem universeIsSet : IsOfHLevel 2 Type := higherLevels Type 0

/-- The universe is not a proposition: Unit and Empty are different types. -/
theorem universeNotProp : ¬ IsOfHLevel 1 Type :=
  fun h => Empty.elim (cast (h Unit Empty) ())

/-- A judge for the universe exists. -/
def judgeType : Judge Type
  | 0 => isFalse universeNotProp
  | k + 1 => isTrue (higherLevels Type k)

/-- In the fact world the questioning of the universe stops at step 1 and
    returns 1, for every judge and every fuel. -/
theorem universeStopsAtOne (judge : Judge Type) (fuel : Nat) :
    question Type judge fuel = some 1 :=
  settledAt Type judge 1 fuel universeIsSet

/-- The same for every type. -/
theorem everyTypeStopsAtOne (C : Sort u) (judge : Judge C) (fuel : Nat) :
    question C judge fuel = some 1 :=
  settledAt C judge 1 fuel (higherLevels C 0)

/-- With the judge judgeType the kernel computes the answer at fuel 0. -/
theorem kernelComputesOne : question Type judgeType 0 = some 1 := rfl

end CG001.QuestioningLean

#print axioms CG001.QuestioningLean.runYes
#print axioms CG001.QuestioningLean.runNoZero
#print axioms CG001.QuestioningLean.runNoSucc
#print axioms CG001.QuestioningLean.settledAt
#print axioms CG001.QuestioningLean.universeIsSet
#print axioms CG001.QuestioningLean.universeNotProp
#print axioms CG001.QuestioningLean.universeStopsAtOne
#print axioms CG001.QuestioningLean.everyTypeStopsAtOne
#print axioms CG001.QuestioningLean.kernelComputesOne
