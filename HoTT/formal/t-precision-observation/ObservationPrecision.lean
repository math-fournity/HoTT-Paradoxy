/-!
MP-T-PRECISION-TOBS-001 formalizes the smallest theorem used by T-OBS.

It has no ZFC syntax, no HoTT-specific rule, no quotient construction, and no
claim about a physical process. It proves only a function/Prop statement:
when a chosen observation map identifies two inputs on which a chosen
predicate has opposite truth values, no decoder using only that observation
can decide the predicate on every input.

The concrete Bool-to-Unit control supplies an executable finite witness. The
identity map is a positive control: it retains enough data to decide the same
predicate.
-/

namespace TPrecisionObservation

/-- A chosen observation determines a predicate exactly when the predicate
    factors through that observation as a Prop-valued decoder. -/
def Determines
    {World View : Type}
    (project : World → View)
    (observe : World → Prop) : Prop :=
  ∃ decode : View → Prop, ∀ world, observe world ↔ decode (project world)

/-- A collision in the observation map with opposite truth values blocks every
    global decoder through that map. -/
theorem no_determines_of_collision
    {World View : Type}
    (project : World → View)
    (observe : World → Prop)
    {x y : World}
    (collision : project x = project y)
    (x_observed : observe x)
    (y_not_observed : ¬ observe y) :
    ¬ Determines project observe := by
  intro determines
  rcases determines with ⟨decode, decoder⟩
  have decoded_x : decode (project x) := (decoder x).mp x_observed
  have decoded_y : decode (project y) := by
    rw [← collision]
    exact decoded_x
  exact y_not_observed ((decoder y).mpr decoded_y)

/-- If the observation retains the entire world, every predicate factors
    through it. This is the generic rich-interface positive control. -/
theorem identity_determines
    {World : Type}
    (observe : World → Prop) :
    Determines (fun world : World => world) observe := by
  refine ⟨observe, ?_⟩
  intro world
  rfl

/-- Finite control world for the T-OBS card. -/
inductive TinyWorld where
  | retained
  | erased
deriving DecidableEq, Repr

/-- A coarse interface that retains no distinction between the two worlds. -/
inductive CoarseView where
  | collapsed
deriving DecidableEq, Repr

def coarseObservation : TinyWorld → CoarseView
  | _ => .collapsed

/-- The fixed task predicate differs precisely on the two worlds. -/
def taskDone : TinyWorld → Prop
  | .retained => True
  | .erased => False

theorem retained_done : taskDone .retained := by
  trivial

theorem erased_not_done : ¬ taskDone .erased := by
  intro h
  exact h

theorem coarse_collision :
    coarseObservation .retained = coarseObservation .erased := by
  rfl

/-- Concrete T-OBS control: the coarse one-value observation cannot decide the
    task predicate. -/
theorem coarse_observation_does_not_determine_task_done :
    ¬ Determines coarseObservation taskDone :=
  no_determines_of_collision coarseObservation taskDone coarse_collision retained_done erased_not_done

/-- Retaining the world itself is enough to decide the same task predicate. -/
def richObservation : TinyWorld → TinyWorld := fun world => world

theorem rich_observation_determines_task_done :
    Determines richObservation taskDone := by
  exact identity_determines taskDone

/-- The complete finite control has both the negative coarse result and the
    positive rich result. -/
theorem finite_control_has_relative_precision_boundary :
    (¬ Determines coarseObservation taskDone) ∧
      Determines richObservation taskDone := by
  exact ⟨coarse_observation_does_not_determine_task_done,
    rich_observation_determines_task_done⟩

#print axioms no_determines_of_collision
#print axioms identity_determines
#print axioms coarse_observation_does_not_determine_task_done
#print axioms rich_observation_determines_task_done
#print axioms finite_control_has_relative_precision_boundary

end TPrecisionObservation
