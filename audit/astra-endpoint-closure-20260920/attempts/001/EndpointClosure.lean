import DeformationCircle

/-! Extend the same curve motion to its closed parameter interval and inspect its endpoints. -/
noncomputable section
open Set Metric Topology
namespace AstraRealGeometry

abbrev ClosedParameter := ↥(Icc (0 : ℝ) 1)
def centered (u : ℝ) : ℝ := 2*u-1
def closingD (t u : ℝ) : ℝ := 1 - |centered u| + (1-t)^2 * |centered u|
def closingN (t u : ℝ) : ℝ := ((1+t^2)/2) * centered u + ((1-t)/2)*closingD t u
def closingDen (t u : ℝ) : ℝ := (closingD t u)^2 + (t*closingN t u)^2
def closedBase (t u : ℝ) : Plane :=
  vec2 (closingN t u * closingD t u / closingDen t u)
    (t*(closingN t u)^2 / closingDen t u)
def extendedDeformation (t u : ℝ) : Plane := turn t (closedBase t u)

theorem centered_abs_le (u : ClosedParameter) : |centered u| ≤ 1 := by
  rw [abs_le]
  dsimp [centered]
  constructor <;> linarith [u.property.1,u.property.2]

theorem closingD_pos_ne_one (t : ℝ) (u : ClosedParameter) (ht : t ≠ 1) : 0 < closingD t u := by
  have ha := centered_abs_le u
  have hc : 0 < (1-t)^2 := sq_pos_of_ne_zero (sub_ne_zero.mpr (Ne.symm ht))
  by_cases h : |centered u| < 1
  · have hp := mul_nonneg hc.le (abs_nonneg (centered u))
    dsimp [closingD]
    linarith
  · have he : |centered u| = 1 := by linarith
    simpa [closingD,he] using hc

theorem closingDen_pos (t : MotionTime) (u : ClosedParameter) : 0 < closingDen t u := by
  by_cases ht : (t : ℝ) = 1
  · simp only [closingDen, closingN, closingD, ht]
    norm_num
    nlinarith [sq_abs (centered u), sq_nonneg (centered u)]
  · have hd := closingD_pos_ne_one t u ht
    unfold closingDen
    nlinarith [sq_pos_of_pos hd, sq_nonneg ((t : ℝ)*closingN t u)]

theorem extendedDeformation_continuous :
    Continuous (fun z : MotionTime × ClosedParameter => extendedDeformation z.1 z.2) := by
  have hd : ∀ z : MotionTime × ClosedParameter, closingDen z.1 z.2 ≠ 0 :=
    fun z => ne_of_gt (closingDen_pos z.1 z.2)
  have hb : Continuous (fun z : MotionTime × ClosedParameter => closedBase z.1 z.2) := by
    unfold closedBase
    apply continuous_vec2_pair
    all_goals apply Continuous.div
    all_goals first | exact hd | (unfold closingN closingD closingDen centered; fun_prop)
  unfold extendedDeformation turn
  apply continuous_vec2_pair <;> fun_prop

theorem unboundedParameter_formula (u : Interval) :
    unboundedParameter u = centered u / (1-|centered u|) := by
  have hf : ∀ x : ↥(Ioo (-1 : ℝ) 1), (orderIsoIooNegOneOne ℝ).symm x = (x : ℝ)/(1-|(x : ℝ)|) := by
    intro x
    unfold orderIsoIooNegOneOne
    rfl
  simpa only [unboundedParameter, OrderIso.trans_apply, centeredOrder_val, centered] using hf (centeredOrder u)

theorem closingD_pos_interior (t : ℝ) (u : Interval) : 0 < closingD t u := by
  have ha : |centered u| < 1 := by
    rw [abs_lt]
    dsimp [centered]
    constructor <;> linarith [u.property.1,u.property.2]
  have hp := mul_nonneg (sq_nonneg (1-t)) (abs_nonneg (centered u))
  dsimp [closingD]
  linarith

theorem stretch_as_fraction (t : ℝ) (u : Interval) :
    stretch t u = closingN t u / closingD t u := by
  have he : 0 < 1-|centered u| := by
    apply sub_pos.mpr
    rw [abs_lt]
    dsimp [centered]
    constructor <;> linarith [u.property.1,u.property.2]
  have hd := closingD_pos_interior t u
  unfold stretch squash
  rw [unboundedParameter_formula, abs_div, abs_of_pos he]
  dsimp [closingN,closingD] at hd ⊢
  field_simp
  ring

theorem closedBase_eq_bend {t u : ℝ} (hd : closingD t u ≠ 0) :
    closedBase t u = bend t (closingN t u / closingD t u) := by
  ext i
  fin_cases i <;> simp [closedBase,bend,vec2,closingDen]
  all_goals field_simp [hd] <;> ring

theorem extended_agrees_interior (t : ℝ) (u : Interval) :
    extendedDeformation t u = deformation t u := by
  unfold extendedDeformation deformation
  rw [closedBase_eq_bend (ne_of_gt (closingD_pos_interior t u)), stretch_as_fraction]

theorem extended_initial (u : ClosedParameter) : extendedDeformation 0 u = lineEmbed u := by
  ext i
  fin_cases i <;> simp [extendedDeformation,closedBase,closingDen,closingN,closingD,centered,turn,vec2,lineEmbed]
  all_goals ring

theorem extended_final_left : extendedDeformation 1 0 = (pole : Plane) := by
  ext i
  fin_cases i <;> norm_num [extendedDeformation,closedBase,closingDen,closingN,closingD,centered,turn,vec2,pole]

theorem extended_final_right : extendedDeformation 1 1 = (pole : Plane) := by
  ext i
  fin_cases i <;> norm_num [extendedDeformation,closedBase,closingDen,closingN,closingD,centered,turn,vec2,pole]

theorem endpoint_images_distinct_before {t : ℝ} (ht : t < 1) :
    extendedDeformation t 0 ≠ extendedDeformation t 1 := by
  intro h
  have hc : (1-t)^2 ≠ 0 := pow_ne_zero 2 (ne_of_gt (sub_pos.mpr ht))
  have hd0 : closingD t 0 ≠ 0 := by simpa [closingD,centered] using hc
  have hd1 : closingD t 1 ≠ 0 := by simpa [closingD,centered] using hc
  have he := (turn t).injective h
  rw [closedBase_eq_bend hd0,closedBase_eq_bend hd1] at he
  have hr := (bend_isEmbedding t).injective he
  norm_num [closingN,closingD,centered] at hr
  field_simp [hc] at hr
  nlinarith [sq_nonneg t]

def endpointGap (t : MotionTime) : ℝ := dist (extendedDeformation t 0) (extendedDeformation t 1)

theorem endpointGap_continuous : Continuous endpointGap := by
  have h0 := extendedDeformation_continuous.comp
    (continuous_id.prodMk (continuous_const : Continuous (fun _ : MotionTime => (timeStart : ClosedParameter))))
  have h1 := extendedDeformation_continuous.comp
    (continuous_id.prodMk (continuous_const : Continuous (fun _ : MotionTime => (timeEnd : ClosedParameter))))
  exact h0.dist h1

theorem endpointGap_pos_before (t : MotionTime) (ht : (t : ℝ) < 1) : 0 < endpointGap t :=
  dist_pos.mpr (endpoint_images_distinct_before ht)

theorem endpointGap_zero_at_end : endpointGap timeEnd = 0 := by
  change dist (extendedDeformation 1 0) (extendedDeformation 1 1) = 0
  rw [extended_final_left,extended_final_right,dist_self]

theorem extended_final_not_injective :
    ¬ Function.Injective (fun u : ClosedParameter => extendedDeformation 1 u) := by
  intro h
  have he : extendedDeformation 1 (timeStart : ClosedParameter) = extendedDeformation 1 timeEnd := by
    exact extended_final_left.trans extended_final_right.symm
  have hx := congrArg Subtype.val (h he)
  norm_num [timeStart,timeEnd] at hx

#print axioms extendedDeformation_continuous
#print axioms extended_agrees_interior
#print axioms endpointGap_continuous
#print axioms endpointGap_pos_before
#print axioms endpointGap_zero_at_end
#print axioms extended_final_not_injective

end AstraRealGeometry
