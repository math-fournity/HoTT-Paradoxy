-- CG-009: func 支的组装 —— 逐分量桥接 + `iVE_open` 的最后一支。
--
-- ## 逐分量桥接（本文件的核心）
--
-- LHS 的参数向量是 `W' := W (mm+1) k (termSubstVec ℒₒᵣ k (QvecVOr mm) v)`
-- （`termSubst_func` + `iVE_func`），RHS 的参数向量是 `W (mm+1) k v` 经
-- `subst (QvecV (mm+1))` 逐项作用。逐项相等由归纳假设给出：
--     (W').[i] = iVE (mm+1) (termSubst (QvecVOr mm) v.[i])   (nth_resultVec + nth_termSubstVec)
--              = subst (QvecV (mm+1)) (iVE (mm+1) v.[i])     (ih i)
--              = subst (QvecV (mm+1)) ((W ... v).[i])        (nth_resultVec)
import GodelQ.ZFC.IVEOpenFunc16

open FFL FFL.FirstOrder FFL FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.IVEOpenFunc17
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc2 GodelQ.IVEOpenFunc3 GodelQ.IVEOpenFunc4
open GodelQ.IVEOpenFunc5 GodelQ.IVEOpenFunc6 GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFunc9
open GodelQ.IVEOpenFunc10 GodelQ.IVEOpenFunc15 GodelQ.IVEOpenFunc16

/-- 简写：`iVE` 的参数向量。 -/
noncomputable abbrev W (n k v : V) : V := iVE.construction.resultVec ℒₒᵣ ![n] k v

lemma len_W {n k v : V} (hv : IsUTermVec ℒₒᵣ k v) : len (W n k v) = k :=
  iVE.construction.resultVec_lh ℒₒᵣ ![n] hv

/-- **逐分量桥接**：`W'` 的第 `i` 项 = `subst (QvecV (mm+1))` 作用于 `W` 的第 `i` 项。 -/
lemma nth_W_termSubstVec {mm k v i : V} (hv : IsSemitermVec ℒₒᵣ k (mm + 1) v)
    (ih : ∀ i < k, iVE (mm + 1) (termSubst ℒₒᵣ (QvecVOr (V := V) mm) v.[i])
      = subst ℒₛₑₜ (QvecV (V := V) (mm + 1)) (iVE (mm + 1) v.[i]))
    (hi : i < k) :
    (W (mm + 1) k (termSubstVec ℒₒᵣ k (QvecVOr (V := V) mm) v)).[i]
      = subst ℒₛₑₜ (QvecV (V := V) (mm + 1)) ((W (mm + 1) k v).[i]) := by
  have hvT : IsUTermVec ℒₒᵣ k (termSubstVec ℒₒᵣ k (QvecVOr (V := V) mm) v) :=
    (IsSemitermVec.termSubstVec (L := ℒₒᵣ) (w := QvecVOr (V := V) mm)
      (isSemitermVec_QvecVOr mm) hv).isUTerm
  rw [iVE.construction.nth_resultVec ℒₒᵣ ![(mm + 1 : V)] hvT hi,
    nth_termSubstVec hv.isUTerm hi,
    iVE.construction.nth_resultVec ℒₒᵣ ![(mm + 1 : V)] hv.isUTerm hi]
  exact ih i hi

end GodelQ.IVEOpenFunc17

#print axioms GodelQ.IVEOpenFunc17.nth_W_termSubstVec

namespace GodelQ.IVEOpenFunc17
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc2 GodelQ.IVEOpenFunc3 GodelQ.IVEOpenFunc4
open GodelQ.IVEOpenFunc5 GodelQ.IVEOpenFunc6 GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFunc9
open GodelQ.IVEOpenFunc10 GodelQ.IVEOpenFunc15 GodelQ.IVEOpenFunc16

/-- **`iVE_open` 的 func 支**。 -/
lemma iVE_open_func {mm k f v : V} (hkf : (ℒₒᵣ).IsFunc k f) (hv : IsSemitermVec ℒₒᵣ k (mm + 1) v)
    (ih : ∀ i < k, iVE (mm + 1) (termSubst ℒₒᵣ (QvecVOr (V := V) mm) v.[i])
      = subst ℒₛₑₜ (QvecV (V := V) (mm + 1)) (iVE (mm + 1) v.[i])) :
    iVE (mm + 1) (termSubst ℒₒᵣ (QvecVOr (V := V) mm) (^func k f v)) =
      subst ℒₛₑₜ (QvecV (V := V) (mm + 1)) (iVE (mm + 1) (^func k f v)) := by
  rw [termSubst_func hkf hv.isUTerm]
  rw [iVE_func hkf ((IsSemitermVec.termSubstVec (L := ℒₒᵣ) (w := QvecVOr (V := V) mm)
    (isSemitermVec_QvecVOr mm) hv).isUTerm)]
  rw [iVE_func hkf hv.isUTerm]
  by_cases hk : k = 0
  · subst hk
    simp only [ite_true]
    exact (subst_QvecV_ve0 (mm := mm) (f := f)).symm
  · have hk2 : k = 2 := k_eq_two_of_func hkf hk
    subst hk2
    simp only [show (2 : V) ≠ 0 by norm_num, if_false]
    -- 目标：subst (QvecV (mm+1)) (ve2 (mm+1) 2 f (W ... v)) = ve2 (mm+1) 2 f (W ... (termSubstVec ... v))
    -- 用 subst_QvecV_ve2，需要 w' 满足 w'.[i] = subst (QvecV (mm+1)) w.[i]（逐分量）
    refine (subst_QvecV_ve2 (mm := mm) (f := f)
      (w := W (mm + 1) 2 v)
      (w' := W (mm + 1) 2 (termSubstVec ℒₒᵣ 2 (QvecVOr (V := V) mm) v))
      (by norm_num) ?_ ?_ ?_ ?_).symm
    · -- w.[0] 是层 mm+2 的公式
      show IsSemiformula ℒₛₑₜ (mm + 2) (W (mm + 1) 2 v).[0]
      rw [iVE.construction.nth_resultVec ℒₒᵣ ![(mm + 1 : V)] hv.isUTerm (by norm_num : (0:V) < 2)]
      have h := isSemiformula_iVE (n := mm + 1) v.[0] (hv.nth (by norm_num : (0:V) < 2))
      have e : (mm + 1 : V) + 1 = mm + 2 := by ring
      rwa [e] at h
    · show IsSemiformula ℒₛₑₜ (mm + 2) (W (mm + 1) 2 v).[1]
      rw [iVE.construction.nth_resultVec ℒₒᵣ ![(mm + 1 : V)] hv.isUTerm (by norm_num : (1:V) < 2)]
      have h := isSemiformula_iVE (n := mm + 1) v.[1] (hv.nth (by norm_num : (1:V) < 2))
      have e : (mm + 1 : V) + 1 = mm + 2 := by ring
      rwa [e] at h
    · -- w'.[0] = subst (QvecV (mm+1)) w.[0]
      exact (nth_W_termSubstVec (mm := mm) (k := 2) (i := 0) hv ih (by norm_num)).symm
    · exact (nth_W_termSubstVec (mm := mm) (k := 2) (i := 1) hv ih (by norm_num)).symm

end GodelQ.IVEOpenFunc17

#print axioms GodelQ.IVEOpenFunc17.iVE_open_func
