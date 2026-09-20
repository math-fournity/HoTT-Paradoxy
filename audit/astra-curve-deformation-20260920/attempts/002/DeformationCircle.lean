import AmbientCircle

/-! A continuous family of curve embeddings, with explicit initial and final images.
This operation model does not require an extension to homeomorphisms of the plane. -/
noncomputable section
open Set Metric Topology
namespace AstraRealGeometry

def vec2 (x y : ℝ) : Plane :=
  x • EuclideanSpace.single (0 : Fin 2) 1 + y • EuclideanSpace.single (1 : Fin 2) 1

@[simp] theorem vec2_zero (x y : ℝ) : vec2 x y 0 = x := by simp [vec2]
@[simp] theorem vec2_one (x y : ℝ) : vec2 x y 1 = y := by simp [vec2]

theorem continuous_vec2 : Continuous (fun z : ℝ × ℝ => vec2 z.1 z.2) := by
  unfold vec2
  fun_prop

theorem continuous_vec2_pair {X : Type*} [TopologicalSpace X] {f g : X → ℝ}
    (hf : Continuous f) (hg : Continuous g) : Continuous (fun x => vec2 (f x) (g x)) :=
  continuous_vec2.comp (hf.prodMk hg)

def centeredOrder : Interval ≃o ↥(Ioo (-1 : ℝ) 1) where
  toFun u := ⟨2 * (u : ℝ) - 1, by constructor <;> linarith [u.property.1, u.property.2]⟩
  invFun v := ⟨((v : ℝ) + 1) / 2, by constructor <;> linarith [v.property.1, v.property.2]⟩
  left_inv u := by apply Subtype.ext; dsimp; ring
  right_inv v := by apply Subtype.ext; dsimp; ring
  map_rel_iff' := by intro u v; change 2 * (u : ℝ) - 1 ≤ 2 * (v : ℝ) - 1 ↔ (u : ℝ) ≤ v; constructor <;> intro h <;> linarith

def unboundedParameter : Interval ≃o ℝ :=
  centeredOrder.trans (orderIsoIooNegOneOne ℝ).symm

def stretch (t : ℝ) (u : Interval) : ℝ :=
  (1-t) * (u : ℝ) + t * unboundedParameter u

theorem stretch_continuous : Continuous (fun z : ℝ × Interval => stretch z.1 z.2) := by
  unfold stretch
  have hc : Continuous unboundedParameter := unboundedParameter.continuous
  fun_prop

theorem stretch_strictMono {t : ℝ} (ht : t ∈ Icc (0 : ℝ) 1) : StrictMono (stretch t) := by
  intro u v huv
  by_cases hz : t = 0
  · simpa [stretch, hz] using huv
  · have hp : 0 < t := lt_of_le_of_ne ht.1 (Ne.symm hz)
    have hρ := unboundedParameter.strictMono huv
    have hu : (u : ℝ) < v := huv
    have h1 := mul_nonneg (sub_nonneg.mpr ht.2) (sub_nonneg.mpr hu.le)
    have h2 := mul_pos hp (sub_pos.mpr hρ)
    dsimp [stretch]
    nlinarith

theorem stretch_isEmbedding {t : ℝ} (ht : t ∈ Icc (0 : ℝ) 1) : IsEmbedding (stretch t) := by
  letI : PreconnectedSpace Interval := isPreconnected_Ioo.preconnectedSpace
  apply (stretch_strictMono ht).isEmbedding_of_ordConnected
  exact (isPreconnected_range (stretch_continuous.comp (continuous_const.prodMk continuous_id))).ordConnected

def bend (t r : ℝ) : Plane :=
  vec2 (r / (1 + (t*r)^2)) (t*r^2 / (1 + (t*r)^2))

theorem bend_den_pos (t r : ℝ) : 0 < 1 + (t*r)^2 := by positivity

theorem bend_continuous : Continuous (fun z : ℝ × ℝ => bend z.1 z.2) := by
  unfold bend
  apply continuous_vec2_pair
  · exact continuous_snd.div (by fun_prop) (fun z => ne_of_gt (bend_den_pos z.1 z.2))
  · exact (by fun_prop : Continuous (fun z : ℝ × ℝ => z.1*z.2^2)).div
      (by fun_prop) (fun z => ne_of_gt (bend_den_pos z.1 z.2))

theorem bend_inverse_den (t r : ℝ) : 1 - t * bend t r 1 = 1 / (1 + (t*r)^2) := by
  simp only [bend, vec2_one]
  field_simp
  ring

def bendChart (t : ℝ) (r : ℝ) : {z : Plane // 1 - t * z 1 ≠ 0} :=
  ⟨bend t r, by rw [bend_inverse_den]; exact one_div_ne_zero (ne_of_gt (bend_den_pos t r))⟩

theorem bend_isEmbedding (t : ℝ) : IsEmbedding (bend t) := by
  let inv : {z : Plane // 1 - t * z 1 ≠ 0} → ℝ := fun z => z.val 0 / (1 - t * z.val 1)
  have hc : Continuous (bendChart t) :=
    (bend_continuous.comp (continuous_const.prodMk continuous_id)).subtype_mk _
  have hi : Continuous inv := by
    apply Continuous.div (by fun_prop) (by fun_prop)
    intro z
    exact z.property
  have hl : Function.LeftInverse inv (bendChart t) := by
    intro r
    change bend t r 0 / (1 - t * bend t r 1) = r
    rw [bend_inverse_den]
    simp only [bend, vec2_zero]
    field_simp
  exact IsEmbedding.subtypeVal.comp (hl.isEmbedding hi hc)

def turnDet (t : ℝ) : ℝ := (1-t)^2 + (2*t)^2

theorem turnDet_pos (t : ℝ) : 0 < turnDet t := by
  unfold turnDet
  nlinarith [sq_nonneg (1-t), sq_nonneg (2*t), sq_nonneg (t - 1/5)]

def turn (t : ℝ) : Plane ≃ₜ Plane where
  toFun v := vec2 ((1-t)*v 0 + 2*t*v 1 - t) (-2*t*v 0 + (1-t)*v 1)
  invFun w := vec2 (((1-t)*(w 0+t) - 2*t*w 1) / turnDet t)
    ((2*t*(w 0+t) + (1-t)*w 1) / turnDet t)
  left_inv v := by
    ext i
    fin_cases i <;> simp [vec2]
    all_goals field_simp [ne_of_gt (turnDet_pos t)]
    all_goals dsimp [turnDet]; ring
  right_inv w := by
    ext i
    fin_cases i <;> simp [vec2]
    all_goals field_simp [ne_of_gt (turnDet_pos t)]
    all_goals dsimp [turnDet]; ring
  continuous_toFun := by
    apply continuous_vec2_pair <;> fun_prop
  continuous_invFun := by
    apply continuous_vec2_pair <;> fun_prop

def deformation (t : ℝ) (u : Interval) : Plane := turn t (bend t (stretch t u))

theorem deformation_continuous : Continuous (fun z : ℝ × Interval => deformation z.1 z.2) := by
  have hb : Continuous (fun z : ℝ × Interval => bend z.1 (stretch z.1 z.2)) :=
    bend_continuous.comp (continuous_fst.prodMk stretch_continuous)
  unfold deformation turn
  apply continuous_vec2_pair <;> fun_prop

theorem deformation_isEmbedding {t : ℝ} (ht : t ∈ Icc (0 : ℝ) 1) : IsEmbedding (deformation t) :=
  (turn t).isEmbedding.comp ((bend_isEmbedding t).comp (stretch_isEmbedding ht))

theorem deformation_start (u : Interval) : deformation 0 u = lineEmbed u := by
  ext i
  fin_cases i <;> simp [deformation, turn, bend, stretch, lineEmbed, vec2]

#print axioms deformation_isEmbedding
#print axioms deformation_continuous
#print axioms deformation_start

end AstraRealGeometry
