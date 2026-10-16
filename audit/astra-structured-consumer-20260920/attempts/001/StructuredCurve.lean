import EndpointClosure

/-! Actual curve presentations retain a continuous completion and its endpoint incidence.
The bare relation compares only the intrinsic open image. -/
noncomputable section
open Set Metric Topology
namespace AstraRealGeometry

def includeInterior (u : Interval) : ClosedParameter := ⟨u,⟨u.property.1.le,u.property.2.le⟩⟩
def endParameter : Bool → ClosedParameter
  | false => timeStart
  | true => timeEnd

structure CurvePresentation where
  interior : Interval → Plane
  completion : ClosedParameter → Plane
  embedded : IsEmbedding interior
  continuous_completion : Continuous completion
  agrees : ∀ u, completion (includeInterior u) = interior u

def CurvePresentation.boundary (R : CurvePresentation) (b : Bool) : Plane :=
  R.completion (endParameter b)

def presentationAt (t : MotionTime) : CurvePresentation where
  interior := deformation t
  completion := extendedDeformation t
  embedded := deformation_isEmbedding t.property
  continuous_completion := by
    have hc : Continuous (fun u : ClosedParameter => (t,u)) := continuous_const.prodMk continuous_id
    simpa only [Function.comp_def] using extendedDeformation_continuous.comp hc
  agrees u := extended_agrees_interior t u

def nPresentation : CurvePresentation := presentationAt timeStart
def mPresentation : CurvePresentation := presentationAt timeEnd

abbrev BareCarrier (R : CurvePresentation) := ↥(range R.interior)
def BareEquivalent (R S : CurvePresentation) : Prop := Nonempty (BareCarrier R ≃ₜ BareCarrier S)
def BoundaryCoincident (R : CurvePresentation) : Prop := R.boundary false = R.boundary true

theorem n_image : range nPresentation.interior = lineOpen := deformation_initial_image
theorem m_image : range mPresentation.interior = circleOpen := deformation_final_image

def concreteBareHomeomorph : BareCarrier nPresentation ≃ₜ BareCarrier mPresentation :=
  (Homeomorph.setCongr n_image).trans
    (embeddedIntrinsicHomeomorph.symm.trans (Homeomorph.setCongr m_image.symm))

theorem n_boundary_separate : ¬ BoundaryCoincident nPresentation := by
  change extendedDeformation 0 0 ≠ extendedDeformation 0 1
  exact endpoint_images_distinct_before (by norm_num)

theorem m_boundary_at_pole (b : Bool) : mPresentation.boundary b = (pole : Plane) := by
  cases b
  · exact extended_final_left
  · exact extended_final_right

theorem m_boundary_coincident : BoundaryCoincident mPresentation :=
  (m_boundary_at_pole false).trans (m_boundary_at_pole true).symm

structure PresentationEquivalence (R S : CurvePresentation) where
  ambient : Plane ≃ₜ Plane
  parameters : ClosedParameter ≃ₜ ClosedParameter
  labels : Bool ≃ Bool
  endpoints : ∀ b, parameters (endParameter b) = endParameter (labels b)
  completion_commutes : ∀ u, ambient (R.completion u) = S.completion (parameters u)

theorem no_concrete_structure_equivalence :
    ¬ Nonempty (PresentationEquivalence nPresentation mPresentation) := by
  rintro ⟨e⟩
  have hb : ∀ b, e.ambient (nPresentation.boundary b) = mPresentation.boundary (e.labels b) := by
    intro b
    exact (e.completion_commutes (endParameter b)).trans (congrArg mPresentation.completion (e.endpoints b))
  apply n_boundary_separate
  apply e.ambient.injective
  exact (hb false).trans ((m_boundary_at_pole _).trans ((m_boundary_at_pole _).symm.trans (hb true).symm))

theorem no_bare_coincidence_transport :
    ¬ (∀ R S : CurvePresentation, BareEquivalent R S → (BoundaryCoincident R ↔ BoundaryCoincident S)) := by
  intro h
  exact n_boundary_separate ((h _ _ ⟨concreteBareHomeomorph⟩).mpr m_boundary_coincident)

def ambientTransport (h : Plane ≃ₜ Plane) (R : CurvePresentation) : CurvePresentation where
  interior := h ∘ R.interior
  completion := h ∘ R.completion
  embedded := h.isEmbedding.comp R.embedded
  continuous_completion := h.continuous.comp R.continuous_completion
  agrees u := congrArg h (R.agrees u)

def ambientTransportEquivalence (h : Plane ≃ₜ Plane) (R : CurvePresentation) :
    PresentationEquivalence R (ambientTransport h R) where
  ambient := h
  parameters := Homeomorph.refl _
  labels := Equiv.refl _
  endpoints _ := rfl
  completion_commutes _ := rfl

theorem ambientTransport_preserves_coincidence (h : Plane ≃ₜ Plane) (R : CurvePresentation) :
    BoundaryCoincident (ambientTransport h R) ↔ BoundaryCoincident R := h.injective.eq_iff

abbrev IntegralPoint := ℤ × ℤ
def integralEmbedding (p : IntegralPoint) : Plane := vec2 (p.1 : ℝ) (p.2 : ℝ)
def nIntegralBoundary : Bool → IntegralPoint
  | false => (0,0)
  | true => (1,0)
def mIntegralBoundary (_ : Bool) : IntegralPoint := (1,0)

theorem integralEmbedding_injective : Function.Injective integralEmbedding := by
  intro p q h
  have h0 := congrArg (fun v : Plane => v 0) h
  have h1 := congrArg (fun v : Plane => v 1) h
  simp only [integralEmbedding,vec2_zero,vec2_one] at h0 h1
  apply Prod.ext <;> exact_mod_cast ‹_›

theorem n_integral_observation_exact (b : Bool) :
    integralEmbedding (nIntegralBoundary b) = nPresentation.boundary b := by
  cases b
  · have h := extended_initial timeStart
    simpa [integralEmbedding,nIntegralBoundary,nPresentation,presentationAt,CurvePresentation.boundary,
      endParameter,timeStart,vec2,lineEmbed] using h.symm
  · have h := extended_initial timeEnd
    simpa [integralEmbedding,nIntegralBoundary,nPresentation,presentationAt,CurvePresentation.boundary,
      endParameter,timeStart,timeEnd,vec2,lineEmbed] using h.symm

theorem m_integral_observation_exact (b : Bool) :
    integralEmbedding (mIntegralBoundary b) = mPresentation.boundary b := by
  rw [m_boundary_at_pole]
  simp [integralEmbedding,mIntegralBoundary,vec2,pole]

#print axioms no_concrete_structure_equivalence
#print axioms no_bare_coincidence_transport
#print axioms ambientTransportEquivalence
#print axioms integralEmbedding_injective
#print axioms n_integral_observation_exact
#print axioms m_integral_observation_exact
end AstraRealGeometry
