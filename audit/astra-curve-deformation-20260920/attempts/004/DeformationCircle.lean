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

def squash (c r : ℝ) : ℝ := r / (1 + c * |r|)

theorem squash_den_pos {c : ℝ} (hc : 0 ≤ c) (r : ℝ) : 0 < 1 + c * |r| := by
  positivity

theorem squash_strictMono {c : ℝ} (hc : 0 ≤ c) : StrictMono (squash c) := by
  apply strictMono_of_odd_strictMonoOn_nonneg
  · intro r
    simp [squash]
  · intro x hx y hy hxy
    have hx' : 0 ≤ x := hx
    have hy' : 0 ≤ y := hy
    dsimp [squash]
    rw [abs_of_nonneg hx', abs_of_nonneg hy']
    apply (div_lt_div_iff₀ (by positivity) (by positivity)).2
    nlinarith

theorem squash_parameter (u : Interval) : squash 1 (unboundedParameter u) = 2*(u : ℝ)-1 := by
  have h := congrArg Subtype.val ((orderIsoIooNegOneOne ℝ).apply_symm_apply (centeredOrder u))
  simpa [squash, unboundedParameter, centeredOrder, orderIsoIooNegOneOne] using h

def stretch (t : ℝ) (u : Interval) : ℝ :=
  ((1+t^2)/2) * squash ((1-t)^2) (unboundedParameter u) + (1-t)/2

theorem stretch_continuous : Continuous (fun z : ℝ × Interval => stretch z.1 z.2) := by
  unfold stretch
  have hc : Continuous unboundedParameter := unboundedParameter.continuous
  have hd : ∀ z : ℝ × Interval, 1 + (1-z.1)^2 * |unboundedParameter z.2| ≠ 0 :=
    fun z => ne_of_gt (squash_den_pos (sq_nonneg _) _)
  unfold squash
  fun_prop

theorem stretch_strictMono (t : ℝ) : StrictMono (stretch t) := by
  intro u v huv
  have h := squash_strictMono (sq_nonneg (1-t)) (unboundedParameter.strictMono huv)
  dsimp [stretch]
  exact add_lt_add_right (mul_lt_mul_of_pos_left h (by positivity)) _

theorem stretch_isEmbedding (t : ℝ) : IsEmbedding (stretch t) := by
  let : PreconnectedSpace Interval := Subtype.preconnectedSpace isPreconnected_Ioo
  apply (stretch_strictMono t).isEmbedding_of_ordConnected
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

theorem deformation_isEmbedding {t : ℝ} (_ht : t ∈ Icc (0 : ℝ) 1) : IsEmbedding (deformation t) :=
  (turn t).isEmbedding.comp ((bend_isEmbedding t).comp (stretch_isEmbedding t))

theorem deformation_start (u : Interval) : deformation 0 u = lineEmbed u := by
  have hs : stretch 0 u = (u : ℝ) := by simp [stretch, squash_parameter]; ring
  ext i
  fin_cases i <;> simp [deformation, turn, bend, hs, lineEmbed, vec2]

def circleParameter (r : ℝ) : Plane := vec2 ((r^2-1)/(1+r^2)) (-2*r/(1+r^2))

theorem deformation_end (u : Interval) : deformation 1 u = circleParameter (unboundedParameter u) := by
  have hs : stretch 1 u = unboundedParameter u := by simp [stretch, squash]
  ext i
  fin_cases i <;> simp [deformation, turn, bend, hs, circleParameter, vec2]
  all_goals field_simp; ring

theorem sphere_coordinate_iff (v : Plane) :
    v ∈ Metric.sphere (0 : Plane) 1 ↔ (v 0)^2 + (v 1)^2 = 1 := by
  have hn : ‖v‖^2 = (v 0)^2 + (v 1)^2 := by
    simpa only [Fin.sum_univ_two] using EuclideanSpace.real_norm_sq_eq v
  rw [mem_sphere_zero_iff_norm]
  constructor <;> intro h <;> nlinarith [norm_nonneg v]

theorem circleParameter_mem (r : ℝ) : circleParameter r ∈ circleOpen := by
  rw [circleOpen_eq_diff]
  constructor
  · rw [sphere_coordinate_iff]
    simp only [circleParameter, vec2_zero, vec2_one]
    field_simp
    ring
  · intro h
    have h0 := congrArg (fun v : Plane => v 0) (Set.mem_singleton_iff.mp h)
    simp [circleParameter, pole, vec2] at h0
    have hd : 1+r^2 ≠ 0 := by positivity
    have he := (div_eq_iff hd).mp h0
    nlinarith

theorem circleParameter_onto : range circleParameter = circleOpen := by
  ext v
  constructor
  · rintro ⟨r,rfl⟩
    exact circleParameter_mem r
  · intro hv
    rw [circleOpen_eq_diff] at hv
    have hs := (sphere_coordinate_iff v).mp hv.1
    have hx : v 0 ≠ 1 := by
      intro h
      have hy : v 1 = 0 := by nlinarith [sq_nonneg (v 1)]
      apply hv.2
      apply Set.mem_singleton_iff.mpr
      ext i
      fin_cases i <;> simp [pole, h, hy]
    let r : ℝ := -v 1 / (1-v 0)
    have hd : 1-v 0 ≠ 0 := sub_ne_zero.mpr (Ne.symm hx)
    have hr : 1+r^2 = 2/(1-v 0) := by
      dsimp [r]
      field_simp
      nlinarith
    refine ⟨r, ?_⟩
    ext i
    fin_cases i
    · change (r^2-1)/(1+r^2) = v 0
      rw [hr]
      have hn : r^2-1 = 2/(1-v 0)-2 := by linarith [hr]
      rw [hn]
      field_simp
      ring
    · change -2*r/(1+r^2) = v 1
      rw [hr]
      dsimp [r]
      field_simp

theorem deformation_initial_image : range (deformation 0) = lineOpen := by
  ext v
  constructor
  · rintro ⟨u,rfl⟩
    exact ⟨u, u.property, (deformation_start u).symm⟩
  · rintro ⟨u,hu,rfl⟩
    exact ⟨⟨u,hu⟩, deformation_start ⟨u,hu⟩⟩

theorem deformation_final_image : range (deformation 1) = circleOpen := by
  have he : deformation 1 = circleParameter ∘ unboundedParameter := funext deformation_end
  rw [he, range_comp, unboundedParameter.surjective.range_eq, image_univ, circleParameter_onto]

abbrev MotionTime := ↥(Icc (0 : ℝ) 1)
def timeStart : MotionTime := ⟨0, by constructor <;> norm_num⟩
def timeEnd : MotionTime := ⟨1, by constructor <;> norm_num⟩

theorem exists_curve_deformation :
    ∃ F : MotionTime → Interval → Plane,
      Continuous (fun z : MotionTime × Interval => F z.1 z.2) ∧
      (∀ t, IsEmbedding (F t)) ∧
      range (F timeStart) = lineOpen ∧ range (F timeEnd) = circleOpen := by
  refine ⟨fun t u => deformation t u, ?_, ?_, deformation_initial_image, deformation_final_image⟩
  · exact deformation_continuous.comp
      ((continuous_subtype_val.comp continuous_fst).prodMk continuous_snd)
  · intro t
    exact deformation_isEmbedding t.property

#print axioms deformation_isEmbedding
#print axioms deformation_continuous
#print axioms deformation_start
#print axioms exists_curve_deformation

end AstraRealGeometry
