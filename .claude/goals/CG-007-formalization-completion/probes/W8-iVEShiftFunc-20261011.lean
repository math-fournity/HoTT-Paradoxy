import GodelQ.ZFC.ProbeH

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate
open GodelQ.ProbeE GodelQ.ProbeH

set_option maxHeartbeats 800000

namespace GodelQ.ProbeI

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`iVE_shift` 的 `func` 支**：`iVE` 与 `termShift` 交换。

`termShift` 只改 `ℒₒᵣ` 侧的项（fvar 加一），`iVE` 把它送到 `ℒₛₑₜ` 的
`eqAtom`；`shift ℒₛₑₜ` 在 `ℒₛₑₜ` 侧对 fvar 也加一，故两条路一致。 -/
lemma iVE_shift_func {n k f v : V} (hkf : (ℒₒᵣ).IsFunc k f)
    (hv : IsSemitermVec ℒₒᵣ k n v)
    (ih : ∀ i < k, iVE n (termShift ℒₒᵣ v.[i]) = shift ℒₛₑₜ (iVE n v.[i])) :
    iVE n (termShift ℒₒᵣ (^func k f v)) = shift ℒₛₑₜ (iVE n (^func k f v)) := by
  rw [termShift_func hkf hv.isUTerm]
  rw [iVE_func hkf hv.termShiftVec.isUTerm, iVE_func hkf hv.isUTerm]
  by_cases hk : k = 0
  · subst hk
    simp only [ite_true]
    exact (shift_ve0 f).symm
  · have hk2 : k = 2 := k_eq_two_of_func hkf hk
    subst hk2
    simp only [show (2 : V) ≠ 0 by norm_num, if_false]
    refine (shift_ve2 (n := n) (k := 2) (f := f)
      (w := iVE.construction.resultVec ℒₒᵣ ![n] 2 v)
      (w' := iVE.construction.resultVec ℒₒᵣ ![n] 2 (termShiftVec ℒₒᵣ 2 v))
      (by norm_num) ?_ ?_ ?_ ?_).symm
    · -- hw0
      rw [iVE.construction.nth_resultVec ℒₒᵣ ![n] hv.isUTerm (show (0 : V) < 2 by norm_num)]
      exact isSemiformula_iVE (n := n) v.[0] (hv.nth (i := 0) (by norm_num))
    · -- hw1
      rw [iVE.construction.nth_resultVec ℒₒᵣ ![n] hv.isUTerm (show (1 : V) < 2 by norm_num)]
      exact isSemiformula_iVE (n := n) v.[1] (hv.nth (i := 1) (by norm_num))
    · -- hw'0
      rw [iVE.construction.nth_resultVec ℒₒᵣ ![n] hv.termShiftVec.isUTerm
            (show (0 : V) < 2 by norm_num),
          iVE.construction.nth_resultVec ℒₒᵣ ![n] hv.isUTerm (show (0 : V) < 2 by norm_num),
          nth_termShiftVec hv.isUTerm (show (0 : V) < 2 by norm_num)]
      exact ih 0 (by norm_num)
    · -- hw'1
      rw [iVE.construction.nth_resultVec ℒₒᵣ ![n] hv.termShiftVec.isUTerm
            (show (1 : V) < 2 by norm_num),
          iVE.construction.nth_resultVec ℒₒᵣ ![n] hv.isUTerm (show (1 : V) < 2 by norm_num),
          nth_termShiftVec hv.isUTerm (show (1 : V) < 2 by norm_num)]
      exact ih 1 (by norm_num)

end GodelQ.ProbeI
