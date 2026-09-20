import PuncturedCircle

/-! Actual ambient subsets of the same real Euclidean plane. -/
noncomputable section
open Set Metric Topology
namespace AstraRealGeometry

def lineEmbed (t : ℝ) : Plane := EuclideanSpace.single (0 : Fin 2) t
def lineOpen : Set Plane := lineEmbed '' Set.Ioo (0 : ℝ) 1
def circleOpen : Set Plane := Subtype.val '' ({pole}ᶜ : Set Circle)

theorem lineEmbed_isometry : Isometry lineEmbed := by
  intro x y
  simp [lineEmbed]

theorem closure_lineOpen : closure lineOpen = lineEmbed '' Set.Icc (0 : ℝ) 1 := by
  rw [lineOpen, lineEmbed_isometry.isClosedEmbedding.closure_image_eq,
    closure_Ioo (by norm_num : (0 : ℝ) ≠ 1)]

theorem pole_ne_neg_pole : pole ≠ -pole := by
  intro h
  have hh := congrArg (fun x : Circle => (x : Plane) (0 : Fin 2)) h
  norm_num [pole] at hh

theorem circle_pole_not_open : ¬ IsOpen ({pole} : Set Circle) := by
  intro h
  let e := stereographic' (E := Plane) 1 (-pole)
  have hp : ({pole} : Set Circle) ⊆ e.source := by
    simpa [e] using pole_ne_neg_pole
  have hi := e.isOpen_image_of_subset_source h hp
  have hi' : IsOpen ({e pole} : Set (EuclideanSpace ℝ (Fin 1))) := by
    simpa using hi
  exact not_isOpen_singleton (e pole) hi'

theorem closure_circleOpen : closure circleOpen = Metric.sphere (0 : Plane) 1 := by
  have hd : Dense ({pole}ᶜ : Set Circle) :=
    dense_compl_singleton_iff_not_open.mpr circle_pole_not_open
  have he : IsClosedEmbedding (Subtype.val : Circle → Plane) :=
    isClosed_sphere.isClosedEmbedding_subtypeVal
  rw [circleOpen, he.closure_image_eq, hd.closure_eq]
  simp

theorem circleOpen_eq_diff : circleOpen = Metric.sphere (0 : Plane) 1 \ {(pole : Plane)} := by
  ext x
  constructor
  · rintro ⟨y, hy, rfl⟩
    refine ⟨y.property, ?_⟩
    intro h
    apply hy
    exact Subtype.ext (Set.mem_singleton_iff.mp h)
  · rintro ⟨hx, hp⟩
    refine ⟨⟨x, hx⟩, ?_, rfl⟩
    intro h
    apply hp
    exact congrArg Subtype.val (Set.mem_singleton_iff.mp h)

theorem circle_missing_boundary : closure circleOpen \ circleOpen = {(pole : Plane)} := by
  rw [closure_circleOpen, circleOpen_eq_diff]
  ext x
  simp only [Set.mem_sdiff, Set.mem_singleton_iff]
  constructor
  · rintro ⟨hx, h⟩
    by_contra hn
    exact h ⟨hx, hn⟩
  · intro h
    subst x
    exact ⟨pole.property, fun h => h.2 rfl⟩

#print axioms closure_circleOpen
#print axioms circle_missing_boundary
#print axioms closure_lineOpen

end AstraRealGeometry
