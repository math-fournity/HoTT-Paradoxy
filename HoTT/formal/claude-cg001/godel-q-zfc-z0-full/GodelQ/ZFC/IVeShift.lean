import GodelQ.ZFC.ShiftConjunct
import GodelQ.ZFC.TranslateShiftCompat

/-!
# CG-007 · W8 第二层（十五）：`iVE`/`iTR` 与 `shift` 的相容律

`iT_shift` 的 rel/nrel 支归结为项层的

```
iVE n (termShift t) = shift ℒₛₑₜ (iVE n t)          -- iVE_shift
```

与原子层的

```
iTR n k R (termShiftVec k v) = shift ℒₛₑₜ (iTR n k R v)   -- iTR_shift
```

本文件把这两条补齐。bvar/fvar 两支已在 `TranslateShiftCompat.lean`
（`iVE_shift_bvar`/`iVE_shift_fvar`）；func 支用 `IsSemiterm.sigma1_induction`
（`isSemiformula_iVE` 的先例），分 `ve0`（k = 0）与 `ve2`（k = 2）两种，
后者用 `ShiftConjunct.shift_ve2` 加 `resultVec` 的点相容。

## 为什么 func 支要对 `resultVec` 做点相容

`iVE` 的 func 支是 `ve2 n k f (resultVec ℒₒᵣ ![n] k v)`，`shift` 之后每个分量
要换名；`shift_ve2` 给出 `shift (ve2 n k f w) = ve2 n k f ?[shift w.[0], shift w.[1]]`，
故还差 `resultVec ![n] 2 (termShiftVec 2 v) = ?[shift (resultVec ![n] 2 v).[0], …]`。
两条边都用 `nth_resultVec` 逐分量化成 `iVE n v.[i]`，交给归纳假设。
-/

set_option maxHeartbeats 4000000

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

namespace GodelQ.IVeShift

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- `(resultVec ![n] 2 v).[i]` 就是 `iVE n v.[i]`（`iVE` 的定义即 `result`）。 -/
lemma resultVec2_nth {n v i : V} (hv : IsUTermVec ℒₒᵣ 2 v) (hi : i < 2) :
    (iVE.construction.resultVec ℒₒᵣ ![n] 2 v).[i] = iVE n v.[i] := by
  rw [iVE.construction.nth_resultVec ℒₒᵣ ![n] hv hi]
  rfl

/-- **项层主定理**：`iVE n (termShift t) = shift ℒₛₑₜ (iVE n t)`。

三支：bvar/fvar 已证；func 支分 `ve0`（k = 0，走 `shift_ve0`）与
`ve2`（k = 2，走 `shift_ve2` + 向量点相容 + 归纳假设）。 -/
lemma iVE_shift {n : V} : ∀ t, IsSemiterm ℒₒᵣ n t →
    iVE n (termShift ℒₒᵣ t) = shift ℒₛₑₜ (iVE n t) := by
  apply IsSemiterm.sigma1_induction (L := ℒₒᵣ) (n := n)
    (P := fun t ↦ iVE n (termShift ℒₒᵣ t) = shift ℒₛₑₜ (iVE n t))
  · definability
  · intro z hz
    exact GodelQ.TranslateShiftCompat.iVE_shift_bvar n z
  · intro x
    exact GodelQ.TranslateShiftCompat.iVE_shift_fvar n x
  · intro k f v hkf hv ih
    by_cases hk : k = 0
    · subst hk
      rw [termShift_func hkf hv.isUTerm, iVE_func hkf hv.termShiftVec.isUTerm,
        iVE_func hkf hv.isUTerm]
      simp only [reduceIte]
      exact (GodelQ.ShiftTools.shift_ve0 f).symm
    · have hk2 := k_eq_two_of_func hkf hk
      subst hk2
      have h20 : ¬(2 : V) = 0 := by norm_num
      have hR0 : IsSemiformula ℒₛₑₜ (n + 1)
          (iVE.construction.resultVec ℒₒᵣ ![n] 2 v).[0] := by
        rw [resultVec2_nth hv.isUTerm (by norm_num)]
        exact isSemiformula_iVE v.[0] (hv.nth (i := 0) (by norm_num))
      have hR1 : IsSemiformula ℒₛₑₜ (n + 1)
          (iVE.construction.resultVec ℒₒᵣ ![n] 2 v).[1] := by
        rw [resultVec2_nth hv.isUTerm (by norm_num)]
        exact isSemiformula_iVE v.[1] (hv.nth (i := 1) (by norm_num))
      rw [termShift_func hkf hv.isUTerm, iVE_func hkf hv.termShiftVec.isUTerm,
        iVE_func hkf hv.isUTerm]
      simp only [if_neg h20]
      rw [GodelQ.ShiftConjunct.shift_ve2 h20 hR0 hR1]
      congr 1
      refine nth_ext' (2 : V) ?_ ?_ ?_
      · rw [iVE.construction.resultVec_lh ℒₒᵣ ![n] hv.isUTerm.termShiftVec]
      · simp [len_adjoin]
        norm_num
      · intro i hi
        have hi01 : i = 0 ∨ i = 1 :=
          le_one_iff_eq_zero_or_one.mp (lt_two_iff_le_one.mp hi)
        rcases hi01 with rfl | rfl
        · simp only [nth_adjoin_zero]
          rw [resultVec2_nth hv.isUTerm.termShiftVec (by norm_num),
            nth_termShiftVec hv.isUTerm (by norm_num), ih 0 (by norm_num),
            resultVec2_nth hv.isUTerm (by norm_num)]
        · rw [nth_adjoin_one]
          rw [resultVec2_nth hv.isUTerm.termShiftVec (by norm_num),
            nth_termShiftVec hv.isUTerm (by norm_num), ih 1 (by norm_num),
            resultVec2_nth hv.isUTerm (by norm_num)]
          simp

/-- `ℒₒᵣ` 的关系只有 2 元（等号、小于）。 -/
lemma rel_arity_eq_two {k R : V} (hR : (ℒₒᵣ).IsRel k R) : k = 2 := by
  rcases Arithmetic.isRel_iff_LOR.mp hR with h | h
  · exact h.1
  · exact h.1

/-- **原子层主定理**：`iTR n k R (termShiftVec k v) = shift ℒₛₑₜ (iTR n k R v)`。

`iTR` 只读 `v.[0]`、`v.[1]`（`k = 2`，由 `rel_arity_eq_two`）。两边 `iTR` 都展开后：
分量用 `nth_termShiftVec` + `iVE_shift` 换名；外层走 `shift_qqAlls` + `shift_imp`
+ `shift_and_pair` + `shift_conjunct`；结论项走 `shift_subst_cRel_closed`。 -/
lemma iTR_shift {n k R v : V} (hR : (ℒₒᵣ).IsRel k R) (hv : IsSemitermVec ℒₒᵣ k n v) :
    iTR n k R (termShiftVec ℒₒᵣ k v) = shift ℒₛₑₜ (iTR n k R v) := by
  have hk2 : k = 2 := rel_arity_eq_two hR
  subst hk2
  have h0 : IsSemiformula ℒₛₑₜ (n + 1) (iVE n v.[0]) :=
    isSemiformula_iVE v.[0] (hv.nth (i := 0) (by norm_num))
  have h1 : IsSemiformula ℒₛₑₜ (n + 1) (iVE n v.[1]) :=
    isSemiformula_iVE v.[1] (hv.nth (i := 1) (by norm_num))
  have hc0 : IsUFormula ℒₛₑₜ (conjunct 2 n 0 (iVE n v.[0])) :=
    (isSemiformula_conjunct h0 (zero_lt_two_add n)).isUFormula
  have hc1 : IsUFormula ℒₛₑₜ (conjunct 2 n 1 (iVE n v.[1])) :=
    (isSemiformula_conjunct h1 (one_lt_two_add n)).isUFormula
  have hA : IsUFormula ℒₛₑₜ
      (conjunct 2 n 0 (iVE n v.[0]) ^⋏ (conjunct 2 n 1 (iVE n v.[1]) ^⋏ ^⊤)) :=
    IsUFormula.and.mpr ⟨hc0, IsUFormula.and.mpr ⟨hc1, IsUFormula.verum⟩⟩
  have hB : IsUFormula ℒₛₑₜ (subst ℒₛₑₜ (?[^#0, ^#1] : V) (cRel R)) :=
    (IsSemiformula.subst (isSemiformula_cRel R)
      GodelQ.ShiftConjunct.isSemitermVec_v01).isUFormula
  rw [iTR]
  conv_rhs => rw [iTR]
  rw [nth_termShiftVec hv.isUTerm (show (0 : V) < 2 by norm_num),
    nth_termShiftVec hv.isUTerm (show (1 : V) < 2 by norm_num),
    iVE_shift (n := n) v.[0] (hv.nth (i := 0) (by norm_num)),
    iVE_shift (n := n) v.[1] (hv.nth (i := 1) (by norm_num)),
    GodelQ.ShiftConjunct.shift_qqAlls (IsUFormula.imp.mpr ⟨hA, hB⟩),
    GodelQ.ShiftTools.shift_imp hA hB,
    GodelQ.ShiftConjunct.shift_and_pair hc0 hc1,
    GodelQ.ShiftConjunct.shift_conjunct h0 (zero_lt_two_add n),
    GodelQ.ShiftConjunct.shift_conjunct h1 (one_lt_two_add n),
    GodelQ.ShiftConjunct.shift_subst_cRel_closed R]

end GodelQ.IVeShift

#print axioms GodelQ.IVeShift.resultVec2_nth
#print axioms GodelQ.IVeShift.iVE_shift
#print axioms GodelQ.IVeShift.rel_arity_eq_two
#print axioms GodelQ.IVeShift.iTR_shift
