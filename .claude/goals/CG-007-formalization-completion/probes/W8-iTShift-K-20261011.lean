import GodelQ.ZFC.TranslateShiftCompat

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate
open GodelQ.TranslateShiftCompat

set_option maxHeartbeats 800000

namespace GodelQ.ProbeK

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- ── 项向量的 shift ────────────────────────────────────────────────────────

lemma isSemitermVec_two_bvars {n : V} :
    IsSemitermVec ℒₛₑₜ 2 (2 + n) ((^#0 : V) ∷ (^#1 : V) ∷ (0 : V)) := by
  rw [show (2 : V) = 1 + 1 by norm_num, IsSemitermVec.cons_iff]
  refine ⟨IsSemiterm.bvar.mpr (by
      simpa [show (2 : V) = 1 + 1 by norm_num, add_assoc] using zero_lt_two_add n), ?_⟩
  rw [show (1 : V) = 0 + 1 by norm_num, IsSemitermVec.cons_iff]
  exact ⟨IsSemiterm.bvar.mpr (by
      simpa [show (2 : V) = 1 + 1 by norm_num, add_assoc] using one_lt_two_add n), by simp⟩

lemma isUTermVec_two_bvars :
    IsUTermVec ℒₛₑₜ 2 ((^#0 : V) ∷ (^#1 : V) ∷ (0 : V)) := by
  have h1 : IsUTermVec ℒₛₑₜ 1 ((^#1 : V) ∷ (0 : V)) := by
    simpa using IsUTermVec.adjoin IsUTermVec.empty (IsUTerm.bvar (z := 1))
  simpa using IsUTermVec.adjoin h1 (IsUTerm.bvar (z := 0))

lemma termShiftVec_two_bvars :
    termShiftVec ℒₛₑₜ 2 ((^#0 : V) ∷ (^#1 : V) ∷ (0 : V))
      = (^#0 : V) ∷ (^#1 : V) ∷ (0 : V) := by
  apply nth_ext' 2
  · rw [len_termShiftVec isUTermVec_two_bvars]
  · simp [show (2 : V) = 1 + 1 by norm_num]
  · intro i hi
    rw [nth_termShiftVec isUTermVec_two_bvars hi]
    have hle : i ≤ 1 := lt_two_iff_le_one.mp (by
      simpa [show (2 : V) = 1 + 1 by norm_num] using hi)
    rcases le_one_iff_eq_zero_or_one.mp hle with rfl | rfl <;> simp [termShift_bvar]

-- ── 原子层：iTR 与 shift 交换 ─────────────────────────────────────────────

/-- **`iTR` 与 `shift` 交换**。

`iTR n k R v = qqAlls (imp (A₀ ⋏ (A₁ ⋏ ⊤)) (subst ?[#0, #1] (cRel R))) 2`，
其中 `A_i = conjunct 2 n i (iVE n v.[i])`。`shift` 逐层交换：`qqAlls`（`shift_qqAlls`）、
`imp`/`⋏`（`shift_or`/`shift_and`/`shift_neg`）、`conjunct`（`shift_conjunct`）、
`subst`（`shift_substs`，向量 `?[#0, #1]` 是 bvar 故不动）、`cRel`（引号化句子）。

`iVE n v.[i]` 的 `shift` 用 `iVE_shift`——故假设是 `IsSemitermVec`（给层数），
与 `rel` 支从 `IsSemiformula.rel` 拿到的形状一致。 -/
lemma shift_iTR {n k R v : V} (hR : (ℒₒᵣ).IsRel k R)
    (hv : IsSemitermVec ℒₒᵣ k n v) :
    shift ℒₛₑₜ (iTR n k R v) = iTR n k R (termShiftVec ℒₒᵣ k v) := by
  have hk2 : k = 2 := by
    rcases Arithmetic.isRel_iff_LOR.mp hR with h | h
    · exact h.1
    · exact h.1
  subst hk2
  -- 先把右边也化成「iVE 作用在 shift 后的项上」的形状
  have e0 : iVE n (termShift ℒₒᵣ v.[0]) = shift ℒₛₑₜ (iVE n v.[0]) :=
    iVE_shift n v.[0] (hv.nth (by norm_num))
  have e1 : iVE n (termShift ℒₒᵣ v.[1]) = shift ℒₛₑₜ (iVE n v.[1]) :=
    iVE_shift n v.[1] (hv.nth (by norm_num))
  rw [iTR, iTR]
  rw [nth_termShiftVec hv.isUTerm (show (0 : V) < 2 by norm_num),
      nth_termShiftVec hv.isUTerm (show (1 : V) < 2 by norm_num),
      e0, e1]
  have hA0 : IsSemiformula ℒₛₑₜ (2 + n) (conjunct 2 n 0 (iVE n v.[0])) :=
    isSemiformula_conjunct (b := 2) (n := n) (i := 0)
      (isSemiformula_iVE (n := n) v.[0] (hv.nth (by norm_num))) (zero_lt_two_add n)
  have hA1 : IsSemiformula ℒₛₑₜ (2 + n) (conjunct 2 n 1 (iVE n v.[1])) :=
    isSemiformula_conjunct (b := 2) (n := n) (i := 1)
      (isSemiformula_iVE (n := n) v.[1] (hv.nth (by norm_num))) (one_lt_two_add n)
  have hA01 : IsSemiformula ℒₛₑₜ (2 + n) (conjunct 2 n 1 (iVE n v.[1]) ^⋏ ^⊤) :=
    IsSemiformula.and.mpr ⟨hA1, IsSemiformula.verum⟩
  have hA : IsSemiformula ℒₛₑₜ (2 + n)
      (conjunct 2 n 0 (iVE n v.[0]) ^⋏ (conjunct 2 n 1 (iVE n v.[1]) ^⋏ ^⊤)) :=
    IsSemiformula.and.mpr ⟨hA0, hA01⟩
  have hcr : IsSemiformula ℒₛₑₜ 2 (cRel R) := isSemiformula_cRel R
  have hv2 : IsSemitermVec ℒₛₑₜ 2 (2 + n) ((^#0 : V) ∷ (^#1 : V) ∷ (0 : V)) :=
    isSemitermVec_two_bvars
  have hsub : IsSemiformula ℒₛₑₜ (2 + n) (subst ℒₛₑₜ ?[^#0, ^#1] (cRel R)) :=
    IsSemiformula.subst (L := ℒₛₑₜ) hcr (by
      rwa [show (?[^#0, ^#1] : V) = (^#0 : V) ∷ (^#1 : V) ∷ (0 : V) from rfl])
  have hbody : IsUFormula ℒₛₑₜ
      (neg ℒₛₑₜ (conjunct 2 n 0 (iVE n v.[0]) ^⋏ (conjunct 2 n 1 (iVE n v.[1]) ^⋏ ^⊤))
        ^⋎ subst ℒₛₑₜ ?[^#0, ^#1] (cRel R)) :=
    IsUFormula.or.mpr ⟨hA.isUFormula.neg, hsub.isUFormula⟩
  have hsa : shift ℒₛₑₜ (conjunct 2 n 0 (iVE n v.[0]) ^⋏ (conjunct 2 n 1 (iVE n v.[1]) ^⋏ ^⊤))
      = conjunct 2 n 0 (shift ℒₛₑₜ (iVE n v.[0]))
        ^⋏ (conjunct 2 n 1 (shift ℒₛₑₜ (iVE n v.[1])) ^⋏ ^⊤) := by
    rw [Bootstrapping.shift_and hA0.isUFormula hA01.isUFormula,
      Bootstrapping.shift_and hA1.isUFormula IsUFormula.verum,
      shift_conjunct (b := 2) (n := n) (i := 0)
        (isSemiformula_iVE (n := n) v.[0] (hv.nth (by norm_num))) (zero_lt_two_add n),
      shift_conjunct (b := 2) (n := n) (i := 1)
        (isSemiformula_iVE (n := n) v.[1] (hv.nth (by norm_num))) (one_lt_two_add n),
      shift_verum]
  have hsb : shift ℒₛₑₜ (subst ℒₛₑₜ ?[^#0, ^#1] (cRel R))
      = subst ℒₛₑₜ ?[^#0, ^#1] (cRel R) := by
    rw [show (?[^#0, ^#1] : V) = (^#0 : V) ∷ (^#1 : V) ∷ (0 : V) from rfl]
    rw [Bootstrapping.shift_substs hcr hv2, termShiftVec_two_bvars, shift_cRel]
  show shift ℒₛₑₜ (qqAlls (neg ℒₛₑₜ (conjunct 2 n 0 (iVE n v.[0]) ^⋏ (conjunct 2 n 1 (iVE n v.[1]) ^⋏ ^⊤))
        ^⋎ subst ℒₛₑₜ ?[^#0, ^#1] (cRel R)) 2)
    = qqAlls (neg ℒₛₑₜ (conjunct 2 n 0 (shift ℒₛₑₜ (iVE n v.[0]))
        ^⋏ (conjunct 2 n 1 (shift ℒₛₑₜ (iVE n v.[1])) ^⋏ ^⊤))
      ^⋎ subst ℒₛₑₜ ?[^#0, ^#1] (cRel R)) 2
  rw [shift_qqAlls hbody,
      Bootstrapping.shift_or hA.isUFormula.neg hsub.isUFormula,
      Bootstrapping.shift_neg (n := 2 + n) hA, hsa, hsb]

end GodelQ.ProbeK
