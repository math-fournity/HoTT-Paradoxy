import GodelQ.ZFC.CG008BvMain
import GodelQ.ZFC.CG008SubstNine

/-!
# CG-008 · `cRel` 的公式性与层数

`cRel R = if R = 0 then cRelN 0 else cRelN 1`——**只分两支**，
与 `R` 具体是哪个关系码无关。两支都是闭句的编码（`⌜op(=)⌝`、`⌜op(<)⌝`），
所以层数由 `quote_isSemiformula` 给。

**注意**：不需要 `IsRel 2 R`。`cRel` 对**任意** `R : V` 都有定义，
两分支各自给出一个层 2 的公式。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008ITR
open GodelQ.ZFCArith GodelQ.Translate
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- `cRelN 0` 的编码值是 `⌜op(=)⌝`。 -/
lemma cRelN_zero_eq : (Translate.cRelN 0 : V) =
    ((⌜(arithTrln.rel Language.ORing.Rel.eq : Semisentence ℒₛₑₜ 2)⌝ : ℕ) : V) := rfl

/-- `cRelN 1` 的编码值是 `⌜op(<)⌝`。 -/
lemma cRelN_one_eq : (Translate.cRelN 1 : V) =
    ((⌜(arithTrln.rel Language.ORing.Rel.lt : Semisentence ℒₛₑₜ 2)⌝ : ℕ) : V) := rfl

/-- `cRel R` 在层 2 是公式。 -/
lemma cRel_isSemiformula (R : V) :
    Bootstrapping.IsSemiformula ℒₛₑₜ 2 (Translate.cRel R) := by
  by_cases hR : R = 0
  · rw [Translate.cRel, if_pos hR, cRelN_zero_eq,
      FFL.FirstOrder.Sentence.coe_quote_eq_quote (V := V) (L := ℒₛₑₜ) (n := 2)]
    simpa [Nat.cast_ofNat] using
      FFL.FirstOrder.Sentence.quote_isSemiformula (V := V) (L := ℒₛₑₜ) (n := 2)
        (arithTrln.rel Language.ORing.Rel.eq)
  · rw [Translate.cRel, if_neg hR, cRelN_one_eq,
      FFL.FirstOrder.Sentence.coe_quote_eq_quote (V := V) (L := ℒₛₑₜ) (n := 2)]
    simpa [Nat.cast_ofNat] using
      FFL.FirstOrder.Sentence.quote_isSemiformula (V := V) (L := ℒₛₑₜ) (n := 2)
        (arithTrln.rel Language.ORing.Rel.lt)

/-! ## `iTR` 的层数 -/

/-- `iTR n k R v` 在层 `n + 2` 是公式（`v` 的分量在层 `n`）。

`iTR n k R v = qqAlls (imp A B) 2`，其中
- `A = conjunct 2 n 0 (iVE n v.[0]) ⋏ (conjunct 2 n 1 (iVE n v.[1]) ⋏ ⊤)`，在层 `2 + n`；
- `B = subst (^#0 ∷ ?[^#1]) (cRel R)`，`cRel R` 在层 2、向量长度 2、分量在层 3，
  所以 `B` 在层 3；由 `3 ≤ 2 + n` 单调升到 `2 + n`。

于是 `imp A B` 在层 `2 + n`，`qqAlls · 2` 给出层 `n`。
**但注意结论取 `n + 2`**（比 `n` 宽），因为 `qqAlls` 的层数下界在 `V` 上不便计算；
`n + 2` 够用且由单调性免费。 -/
theorem iTR_isSemiformula (n k R v : V) (hv : Bootstrapping.IsSemitermVec ℒₒᵣ 2 n v) :
    Bootstrapping.IsSemiformula ℒₛₑₜ (n + 2) (Translate.iTR n k R v) := by
  -- 分量：`v.[0]`、`v.[1]` 在层 `n`
  have h0 : Bootstrapping.IsSemiterm ℒₒᵣ n v.[0] := hv.nth (by norm_num)
  have h1 : Bootstrapping.IsSemiterm ℒₒᵣ n v.[1] := hv.nth (by norm_num)
  -- 两个 `conjunct 2 n i (iVE n v.[i])` 在层 `2 + n`
  have hc0 : Bootstrapping.IsSemiformula ℒₛₑₜ (2 + n)
      (Translate.conjunct 2 n 0 (Translate.iVE n v.[0])) :=
    GodelQ.CG008BvMain.isSemiformula_conjunct 2 n 0 (Translate.iVE n v.[0]) (by
      exact lt_of_lt_of_le (by norm_num : (0 : V) < 2)
        (le_add_of_nonneg_right (Arithmetic.zero_le n)))
      (GodelQ.CG008BvMain.isSemiformula_iVE h0)
  have hc1 : Bootstrapping.IsSemiformula ℒₛₑₜ (2 + n)
      (Translate.conjunct 2 n 1 (Translate.iVE n v.[1])) :=
    GodelQ.CG008BvMain.isSemiformula_conjunct 2 n 1 (Translate.iVE n v.[1]) (by
      exact lt_of_lt_of_le (by norm_num : (1 : V) < 2)
        (le_add_of_nonneg_right (Arithmetic.zero_le n)))
      (GodelQ.CG008BvMain.isSemiformula_iVE h1)
  -- `B = subst (^#0 ∷ ?[^#1]) (cRel R)` 在层 3
  have hB : Bootstrapping.IsSemiformula ℒₛₑₜ 3
      (Bootstrapping.subst ℒₛₑₜ (^#0 ∷ (?[^#1] : V)) (Translate.cRel R)) := by
    refine Bootstrapping.IsSemiformula.subst (cRel_isSemiformula R) ?_
    refine Bootstrapping.IsSemitermVec.iff.mpr ⟨?_, ?_⟩
    · rw [Arithmetic.len_adjoin, Arithmetic.len_adjoin, Arithmetic.len_nil]
      rfl
    · intro j hj
      have h3 : (3 : V) ≤ 3 := le_rfl
      rcases Arithmetic.zero_or_succ j with rfl | ⟨j', rfl⟩
      · rw [Arithmetic.nth_adjoin_zero]
        exact Bootstrapping.IsSemiterm.bvar.mpr (by norm_num)
      · rw [Arithmetic.nth_adjoin_succ]
        have hj0 : j' = 0 := by
          -- `j' + 1 < 2 = 1 + 1` ⇒ `j' + 1 ≤ 1` ⇒ `j' ≤ 0` ⇒ `j' = 0`
          have h : j' + 1 < 2 := by simpa using hj
          rw [show (2 : V) = 1 + 1 by norm_num, lt_succ_iff_le] at h
          -- `h : j' + 1 ≤ 1`
          have hle : j' ≤ 0 := by
            have h' : j' + 1 ≤ (0 : V) + 1 := by
              rwa [show ((0 : V) + 1) = 1 by simp]
            exact add_le_add_iff_right 1 |>.mp h'
          exact le_antisymm hle (Arithmetic.zero_le j')
        subst hj0
        rw [Arithmetic.nth_adjoin_zero]
        exact Bootstrapping.IsSemiterm.bvar.mpr (by norm_num)
  rw [Translate.iTR]
  apply Bootstrapping.IsSemiformula.qqAlls
  rw [Bootstrapping.IsSemiformula.imp]
  -- 目标层是 `(n + 2) + 2`；用一个统一的升层助手。
  have hmono : ∀ {a b : V}, a ≤ b → ∀ {p : V},
      Bootstrapping.IsSemiformula ℒₛₑₜ a p → Bootstrapping.IsSemiformula ℒₛₑₜ b p :=
    fun hab _ hp ↦ GodelQ.CG008BvMain.isSemiformula_mono hp hab
  -- `2 + n ≤ (n + 2) + 2`：左边交换后即 `n + 2`，右边是 `(n + 2) + 2`
  have hL : (2 : V) + n ≤ (n + 2) + 2 := by
    rw [add_comm 2 n]
    exact le_add_of_nonneg_right (Arithmetic.zero_le (2 : V))
  -- `3 ≤ (n + 2) + 2`：`n + 2 ≥ 2`，故 `(n + 2) + 2 ≥ 4 ≥ 3`
  have hn2 : (2 : V) ≤ n + 2 := by
    have h : (0 : V) + 2 ≤ n + 2 := add_le_add_left (Arithmetic.zero_le n) 2
    rwa [show ((0 : V) + 2) = 2 by simp] at h
  have hL3 : (3 : V) ≤ (n + 2) + 2 := by
    have h : (2 : V) + 2 ≤ (n + 2) + 2 := add_le_add_left hn2 2
    have h43 : (3 : V) ≤ 2 + 2 := by norm_num
    exact le_trans h43 h
  refine ⟨?_, hmono hL3 hB⟩
  rw [Bootstrapping.IsSemiformula.and]
  exact ⟨hmono hL hc0, by
    rw [Bootstrapping.IsSemiformula.and]
    exact ⟨hmono hL hc1, Bootstrapping.IsSemiformula.verum⟩⟩

end GodelQ.CG008ITR

#print axioms GodelQ.CG008ITR.cRel_isSemiformula
#print axioms GodelQ.CG008ITR.iTR_isSemiformula
