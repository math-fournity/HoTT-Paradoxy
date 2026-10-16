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
    simpa [e] using pole_ne_neg_pole.symm
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
  ext x
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

theorem line_missing_boundary :
    closure lineOpen \ lineOpen = {lineEmbed 0, lineEmbed 1} := by
  rw [closure_lineOpen, lineOpen,
    ← Set.image_sdiff lineEmbed_isometry.injective,
    Set.Icc_sdiff_Ioo_same (by norm_num : (0 : ℝ) ≤ 1)]
  simp

theorem line_endpoints_distinct : lineEmbed 0 ≠ lineEmbed 1 := by
  intro h
  have hh := lineEmbed_isometry.injective h
  norm_num at hh

theorem no_ambient_homeomorph :
    ¬ ∃ h : Plane ≃ₜ Plane, h '' circleOpen = lineOpen := by
  rintro ⟨h, hmap⟩
  have hboundary : h '' (closure circleOpen \ circleOpen) =
      closure lineOpen \ lineOpen := by
    rw [Set.image_sdiff h.injective, h.image_closure, hmap]
  rw [circle_missing_boundary, line_missing_boundary, Set.image_singleton] at hboundary
  have h0 : lineEmbed 0 = h pole := by
    have : lineEmbed 0 ∈ ({h (pole : Plane)} : Set Plane) := by
      rw [hboundary]
      simp
    exact Set.mem_singleton_iff.mp this
  have h1 : lineEmbed 1 = h pole := by
    have : lineEmbed 1 ∈ ({h (pole : Plane)} : Set Plane) := by
      rw [hboundary]
      simp
    exact Set.mem_singleton_iff.mp this
  exact line_endpoints_distinct (h0.trans h1.symm)

def puncturedToAmbient : Punctured pole ≃ₜ circleOpen := by
  have hs : {x : Circle | x ≠ pole} = ({pole}ᶜ : Set Circle) := by
    ext x
    simp
  have he : IsClosedEmbedding (Subtype.val : Circle → Plane) :=
    isClosed_sphere.isClosedEmbedding_subtypeVal
  exact (Homeomorph.setCongr hs).trans
    (he.isEmbedding.homeomorphImage ({pole}ᶜ : Set Circle))

def intervalToAmbient : Interval ≃ₜ lineOpen :=
  lineEmbed_isometry.isEmbedding.homeomorphImage (Set.Ioo (0 : ℝ) 1)

def embeddedIntrinsicHomeomorph : ↥circleOpen ≃ₜ ↥lineOpen :=
  puncturedToAmbient.symm.trans (actualMToN.trans intervalToAmbient)

theorem no_ambient_homeomorph_reverse :
    ¬ ∃ h : Plane ≃ₜ Plane, h '' lineOpen = circleOpen := by
  rintro ⟨h, hmap⟩
  apply no_ambient_homeomorph
  refine ⟨h.symm, ?_⟩
  rw [← hmap]
  exact h.symm_image_image lineOpen

/- A declared operation model, not an assertion about every physical construction. -/
def runAmbient : List (Plane ≃ₜ Plane) → Set Plane → Set Plane
  | [], s => s
  | h :: hs, s => runAmbient hs (h '' s)

theorem ambient_run_is_image (hs : List (Plane ≃ₜ Plane)) (s : Set Plane) :
    ∃ h : Plane ≃ₜ Plane, runAmbient hs s = h '' s := by
  induction hs generalizing s with
  | nil =>
    refine ⟨Homeomorph.refl _, ?_⟩
    simp [runAmbient]
  | cons h hs ih =>
    obtain ⟨k, hk⟩ := ih (h '' s)
    refine ⟨h.trans k, ?_⟩
    rw [runAmbient, hk]
    simp [Set.image_image, Function.comp_def]

theorem no_finite_ambient_reconstruction (hs : List (Plane ≃ₜ Plane)) :
    runAmbient hs lineOpen ≠ circleOpen := by
  intro heq
  obtain ⟨h, hh⟩ := ambient_run_is_image hs lineOpen
  exact no_ambient_homeomorph_reverse ⟨h, hh.symm.trans heq⟩

theorem one_step_positive_control (h : Plane ≃ₜ Plane) :
    runAmbient [h] lineOpen = h '' lineOpen := rfl

#print axioms no_finite_ambient_reconstruction
#print axioms embeddedIntrinsicHomeomorph
#print axioms no_ambient_homeomorph_reverse
#print axioms no_ambient_homeomorph
#print axioms line_missing_boundary
#print axioms closure_circleOpen
#print axioms circle_missing_boundary
#print axioms closure_lineOpen

end AstraRealGeometry
