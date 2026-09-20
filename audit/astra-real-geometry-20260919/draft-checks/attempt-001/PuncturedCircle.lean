import Mathlib.Geometry.Manifold.Instances.Sphere
import Mathlib.Order.Interval.Set.IsoIoo
import Mathlib.Topology.Order.MonotoneContinuity
import Mathlib.Topology.Algebra.Field

/-!
Real point-set geometry for BP-GEO-REAL-01.
This is an auxiliary Lean/mathlib model, not a native HoTT theorem or a physical trace.
The statements distinguish intrinsic homeomorphisms from later ambient/endpoint constraints.
-/

noncomputable section
open Set Metric
namespace AstraRealGeometry

abbrev Plane := EuclideanSpace ℝ (Fin 2)
abbrev Circle := ↥(Metric.sphere (0 : Plane) 1)
abbrev Punctured (p : Circle) := {x : Circle // x ≠ p}
abbrev Interval := ↥(Set.Ioo (0 : ℝ) 1)

instance : Fact (Module.finrank ℝ Plane = 1 + 1) := ⟨by simp [Plane]⟩

def pole : Circle :=
  ⟨EuclideanSpace.single (0 : Fin 2) (1 : ℝ), by simp [Metric.mem_sphere, dist_eq_norm]⟩

def puncturedToEuclidean (p : Circle) : Punctured p ≃ₜ EuclideanSpace ℝ (Fin 1) := by
  let e := stereographic' (E := Plane) 1 p
  have hs : e.source = {x : Circle | x ≠ p} := by simp [e]
  have ht : e.target = Set.univ := by simp [e]
  exact (Homeomorph.setCongr hs.symm).trans
    (e.toHomeomorphSourceTarget.trans
      ((Homeomorph.setCongr ht).trans (Homeomorph.Set.univ _)))

def euclideanLineToReal : EuclideanSpace ℝ (Fin 1) ≃ₜ ℝ :=
  (EuclideanSpace.equiv (Fin 1) ℝ).toHomeomorph.trans
    (Homeomorph.piUnique (fun _ : Fin 1 => ℝ))

def rescaleInterval : ↥(Set.Ioo (-1 : ℝ) 1) ≃ₜ Interval := by
  refine (affineHomeomorph (1 / 2 : ℝ) (1 / 2) (by norm_num)).subtype ?_
  intro x
  change (-1 < x ∧ x < 1) ↔ (0 < 1 / 2 * x + 1 / 2 ∧ 1 / 2 * x + 1 / 2 < 1)
  constructor
  · rintro ⟨hx, hy⟩
    constructor <;> linarith
  · rintro ⟨hx, hy⟩
    constructor <;> linarith

def realToInterval : ℝ ≃ₜ Interval :=
  (orderIsoIooNegOneOne ℝ).toHomeomorph.trans rescaleInterval

def puncturedCircleHomeomorph (p : Circle) : Punctured p ≃ₜ Interval :=
  (puncturedToEuclidean p).trans (euclideanLineToReal.trans realToInterval)

def actualMToN : Punctured pole ≃ₜ Interval := puncturedCircleHomeomorph pole

theorem every_interval_point_has_circle_preimage (y : Interval) :
    ∃ x : Punctured pole, actualMToN x = y :=
  actualMToN.surjective y

theorem exact_inverse_roundtrip (x : Punctured pole) :
    actualMToN.symm (actualMToN x) = x :=
  actualMToN.symm_apply_apply x

theorem forward_continuous : Continuous actualMToN := actualMToN.continuous_toFun
theorem inverse_continuous : Continuous actualMToN.symm := actualMToN.continuous_invFun

#print axioms actualMToN
#print axioms exact_inverse_roundtrip
#print axioms forward_continuous
#print axioms inverse_continuous

end AstraRealGeometry
