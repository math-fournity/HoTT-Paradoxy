import GodelQ.ZFC.ProbeK

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate
open GodelQ.TranslateShiftCompat GodelQ.ProbeK

set_option maxHeartbeats 800000

namespace GodelQ.ProbeL

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- `domZero = subst ?[^#0] cDomN` 在 `shift` 下不变。 -/
@[simp] lemma shift_domZero : shift ℒₛₑₜ (domZero (V := V)) = domZero (V := V) := by
  rw [domZero]
  rw [Bootstrapping.shift_substs (L := ℒₛₑₜ) (n := 1) (m := 1) isSemiformula_cDomN
      (isSemitermVec_single_bvar (n := 1) (by simp)),
    show (termShiftVec ℒₛₑₜ 1 (?[^#0] : V)) = ?[^#0] from by
      rw [show (1 : V) = 0 + 1 by norm_num,
        termShiftVec_cons (IsUTerm.bvar (z := 0)) IsUTermVec.empty,
        termShift_bvar, termShiftVec_nil],
    shift_cDomN]

/-- `domZero` 是层数 1 的公式。 -/
lemma isSemiformula_domZero' : IsSemiformula (V := V) ℒₛₑₜ 1 (domZero (V := V)) := by
  simpa using isSemiformula_domZero (V := V) (n := 0)

/-- `imp domZero X` 在 `shift` 下：`domZero` 不动，`X` 跟着动。 -/
lemma shift_imp_domZero {x : V} (hx : IsUFormula ℒₛₑₜ x) :
    shift ℒₛₑₜ (imp ℒₛₑₜ (domZero (V := V)) x)
      = imp ℒₛₑₜ (domZero (V := V)) (shift ℒₛₑₜ x) := by
  have hd : IsUFormula (V := V) ℒₛₑₜ (domZero (V := V)) :=
    (isSemiformula_domZero' (V := V)).isUFormula
  show shift ℒₛₑₜ (neg ℒₛₑₜ (domZero (V := V)) ^⋎ x)
    = neg ℒₛₑₜ (domZero (V := V)) ^⋎ shift ℒₛₑₜ x
  rw [Bootstrapping.shift_or (IsUFormula.neg hd) hx,
      Bootstrapping.shift_neg (n := 1) (isSemiformula_domZero' (V := V)),
      shift_domZero]

lemma shift_conj_domZero {x : V} (hx : IsUFormula ℒₛₑₜ x) :
    shift ℒₛₑₜ ((domZero (V := V)) ^⋏ x)
      = (domZero (V := V)) ^⋏ shift ℒₛₑₜ x := by
  have hd : IsUFormula (V := V) ℒₛₑₜ (domZero (V := V)) :=
    (isSemiformula_domZero' (V := V)).isUFormula
  rw [Bootstrapping.shift_and hd hx, shift_domZero]


/-- `domZero` 的 `IsUFormula`（简写名，供 `iT_shift` 各支用）。 -/
lemma isUFormula_domZero2 : IsUFormula (V := V) ℒₛₑₜ (domZero (V := V)) :=
  (isSemiformula_domZero' (V := V)).isUFormula

end GodelQ.ProbeL
