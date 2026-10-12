import GodelQ.ZFC.CG008BvBound
import GodelQ.ZFC.CG008BvT

/-!
# CG-008 · `bv (iVE n t) ≤ n + 1`——主定理与它要的引理

## 策略：**证层数，不证 `bv` 算术**

`ve2` 的外层是 `qqAlls · 2`，它把层数**减 2**。所以
「`ve2` 在层 `n + 1` 是公式」比「`bv ≤ n + 1`」更好证——
前者的内层只需层 `(n+1) + 2`，与 `conjunct` 给出的 `3 + n` 只差交换律。

`IsSemiformula` 对层数**单调**（层数只增不减），所以这些差都是免费的。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008BvMain
open GodelQ.ZFCArith GodelQ.Translate
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## 一、基础 -/

/-- `len (shiftVec b n) = n`。**由 `IsUTermVec.lh` 直接给出**。 -/
lemma len_shiftVec (b n : V) : Arithmetic.len (Translate.shiftVec b n) = n :=
  (GodelQ.CG008ShiftProof.isUTermVec_shiftVec (V := V) b n).lh.symm

/-- `IsSemiformula` 对层数单调。 -/
lemma isSemiformula_mono {n m p : V} (h : Bootstrapping.IsSemiformula ℒₛₑₜ n p) (hnm : n ≤ m) :
    Bootstrapping.IsSemiformula ℒₛₑₜ m p :=
  ⟨h.isUFormula, le_trans h.bv_le hnm⟩

/-- `j' + 1 < k + 1 ⇒ j' < k`（`V` 上无 `lt_of_succ_lt_succ`，用两条现成的搭）。 -/
lemma lt_of_succ_lt_succ' {j k : V} (h : j + 1 < k + 1) : j < k :=
  succ_le_iff_lt.mp (lt_succ_iff_le.mp h)

/-! ## 二、`^#i ∷ shiftVec b n` 是项向量（层 `b + n`） -/

lemma isSemitermVec_conjunctVec' (b n i : V) (hi : i < b + n) :
    Bootstrapping.IsSemitermVec ℒₛₑₜ (n + 1) (b + n) (^#i ∷ Translate.shiftVec b n) := by
  refine Bootstrapping.IsSemitermVec.iff.mpr ⟨?_, ?_⟩
  · rw [Arithmetic.len_adjoin, len_shiftVec]
  · intro j hj
    rcases Arithmetic.zero_or_succ j with rfl | ⟨j', rfl⟩
    · rw [Arithmetic.nth_adjoin_zero]
      simpa using hi
    · rw [Arithmetic.nth_adjoin_succ]
      have hj' : j' < n := by
        have h : j' + 1 < n + 1 := by simpa using hj
        exact lt_of_succ_lt_succ' h
      rw [GodelQ.CG008BvT.nth_shiftVec b n j' hj']
      have hb : b + j' < b + n := by
        have h := add_lt_add_left hj' b
        rwa [add_comm j' b, add_comm n b] at h
      exact Bootstrapping.IsSemiterm.bvar.mpr hb

/-! ## 三、`conjunct b n i y` 的层数 -/

/-- `conjunct b n i y` 在层 `b + n` 是公式（`i < b + n` 时）。 -/
theorem isSemiformula_conjunct (b n i y : V) (hi : i < b + n)
    (hy : Bootstrapping.IsSemiformula ℒₛₑₜ (n + 1) y) :
    Bootstrapping.IsSemiformula ℒₛₑₜ (b + n) (Translate.conjunct b n i y) := by
  have h₁ : Bootstrapping.IsSemiformula ℒₛₑₜ (i + 1)
      (Bootstrapping.subst ℒₛₑₜ (?[^#i] : V) (Translate.cDomN : V)) :=
    Bootstrapping.IsSemiformula.subst
      (GodelQ.CG008Ve2.cDomN_isSemiformula (V := V))
      (GodelQ.CG008Conj.isSemitermVec_single (V := V) i)
  have h₂ : Bootstrapping.IsSemiformula ℒₛₑₜ (b + n)
      (Bootstrapping.subst ℒₛₑₜ (^#i ∷ Translate.shiftVec b n) y) :=
    Bootstrapping.IsSemiformula.subst hy (isSemitermVec_conjunctVec' b n i hi)
  rw [Translate.conjunct, Bootstrapping.IsSemiformula.and]
  refine ⟨?_, h₂⟩
  have hle : i + 1 ≤ b + n := by
    have h : i + 1 < (b + n) + 1 := by
      have h0 : i + 1 < (b + n) + 1 := add_lt_add_left hi 1
      exact h0
    rwa [lt_succ_iff_le] at h
  exact isSemiformula_mono h₁ hle

/-! ## 三·五、`^#1 ∷ 0` 的长度 -/

/-! ## 四、`ve2` 的层数 -/

/-- `^#2 ∷ ?[^#0, ^#1]` 的三个分量都是 `^#` 变量，都在层 `3 + n` 是项。

**用 `adjoin` 逐步搭**，不做 `.[i]` 的展开——那会在 `IsSemiterm` 的参数位置
留下一个 `Fixpoint` 项，`rw` 匹配不上。 -/
lemma isSemitermVec_ve2vec' (n : V) :
    Bootstrapping.IsSemitermVec ℒₛₑₜ 3 (3 + n) (^#2 ∷ (?[^#0, ^#1] : V)) := by
  have h3 : (3 : V) ≤ 3 + n := le_add_of_nonneg_right (Arithmetic.zero_le n)
  have h0 : Bootstrapping.IsSemiterm ℒₛₑₜ (3 + n) (^#0 : V) :=
    Bootstrapping.IsSemiterm.bvar.mpr (lt_of_lt_of_le (by norm_num : (0 : V) < 3) h3)
  have h1 : Bootstrapping.IsSemiterm ℒₛₑₜ (3 + n) (^#1 : V) :=
    Bootstrapping.IsSemiterm.bvar.mpr (lt_of_lt_of_le (by norm_num : (1 : V) < 3) h3)
  have h2 : Bootstrapping.IsSemiterm ℒₛₑₜ (3 + n) (^#2 : V) :=
    Bootstrapping.IsSemiterm.bvar.mpr (lt_of_lt_of_le (by norm_num : (2 : V) < 3) h3)
  have hnil : Bootstrapping.IsSemitermVec ℒₛₑₜ 0 (3 + n) (0 : V) :=
    Bootstrapping.IsSemitermVec.empty (3 + n)
  have hv1 : Bootstrapping.IsSemitermVec ℒₛₑₜ (0 + 1) (3 + n) (^#1 ∷ (0 : V)) :=
    Bootstrapping.IsSemitermVec.adjoin hnil h1
  have hv2 : Bootstrapping.IsSemitermVec ℒₛₑₜ ((0 + 1) + 1) (3 + n) (^#0 ∷ ^#1 ∷ (0 : V)) :=
    Bootstrapping.IsSemitermVec.adjoin hv1 h0
  have hv3 : Bootstrapping.IsSemitermVec ℒₛₑₜ (((0 + 1) + 1) + 1) (3 + n)
      (^#2 ∷ ^#0 ∷ ^#1 ∷ (0 : V)) :=
    Bootstrapping.IsSemitermVec.adjoin hv2 h2
  rw [show ((0 : V) + 1 + 1 + 1) = 3 by norm_num] at hv3
  exact hv3

/-- **`ve2 n k f w` 在层 `n + 1` 是公式**（`k ≠ 0`，`w` 的分量在层 `n + 1`）。

`ve2 = qqAlls inner 2`，故内层要在层 `(n+1) + 2 = 3 + n`；
而 `conjunct 3 n i w.[i]` 恰好给 `3 + n`——**层数正好对上**，无需算术界。 -/
theorem isSemiformula_ve2 (n k f w : V) (hk : k ≠ 0)
    (hw : ∀ j : V, j < 2 → Bootstrapping.IsSemiformula ℒₛₑₜ (n + 1) w.[j]) :
    Bootstrapping.IsSemiformula ℒₛₑₜ (n + 1) (Translate.ve2 n k f w) := by
  rw [Translate.ve2]
  apply Bootstrapping.IsSemiformula.qqAlls
  rw [show (n + 1) + 2 = 3 + n by
    rw [add_assoc, show (1 : V) + 2 = 3 by norm_num, add_comm n 3]]
  rw [Bootstrapping.IsSemiformula.imp]
  refine ⟨?_, ?_⟩
  · rw [Bootstrapping.IsSemiformula.and]
    refine ⟨?_, ?_⟩
    · exact isSemiformula_conjunct 3 n 0 w.[0] (by
        exact lt_of_lt_of_le (by norm_num : (0 : V) < 3)
          (le_add_of_nonneg_right (Arithmetic.zero_le n))) (hw 0 (by norm_num))
    · rw [Bootstrapping.IsSemiformula.and]
      exact ⟨isSemiformula_conjunct 3 n 1 w.[1] (by
          exact lt_of_lt_of_le (by norm_num : (1 : V) < 3)
            (le_add_of_nonneg_right (Arithmetic.zero_le n))) (hw 1 (by norm_num)),
        Bootstrapping.IsSemiformula.verum⟩
  · -- `subst (^#2 ∷ ?[^#0, ^#1]) (cFunc k f)`
    exact Bootstrapping.IsSemiformula.subst (GodelQ.CG008Ve2.cFunc_isSemiformula_three hk)
      (isSemitermVec_ve2vec' n)


/-! ## 五、`ve0` 的层数 -/

/-- `ve0 k f` 在层 `n + 1` 是公式（任何 `n`；`k = 0`）。 -/
lemma isSemiformula_ve0 (n k f : V) (hk : k = 0) :
    Bootstrapping.IsSemiformula ℒₛₑₜ (n + 1) (Translate.ve0 k f) := by
  rw [Translate.ve0]
  rw [Bootstrapping.IsSemiformula.imp]
  refine ⟨Bootstrapping.IsSemiformula.verum, ?_⟩
  have h1 : Bootstrapping.IsSemiformula ℒₛₑₜ (0 + 1)
      (Bootstrapping.subst ℒₛₑₜ (?[^#0] : V) (Translate.cFunc k f)) :=
    Bootstrapping.IsSemiformula.subst (GodelQ.CG008VeLevel.cFunc_isSemiformula_one hk)
      (GodelQ.CG008Conj.isSemitermVec_single (V := V) 0)
  exact isSemiformula_mono h1 (by
    rw [show ((0 : V) + 1) = 1 by simp]
    exact le_add_of_nonneg_left (Arithmetic.zero_le n))

/-! ## 六、主定理：`iVE n t` 的层数 -/

/-- **`iVE n t` 在层 `n + 1` 是公式**（`t` 是层 `n` 的算术项）。

三个分支：
- `bvar z`（`z < n`）：`eqAtom (^#(z+1))`，其层是 `z + 2 ≤ n + 1`；
- `fvar x`：`eqAtom (^&x)`，其层是 `1 ≤ n + 1`；
- `func k f v`：`k = 0` 走 `ve0`（层 1），否则走 `ve2`（层 `n + 1`），
  后者的分量由归纳假设给。 -/
theorem isSemiformula_iVE {n t : V} (ht : Bootstrapping.IsSemiterm ℒₒᵣ n t) :
    Bootstrapping.IsSemiformula ℒₛₑₜ (n + 1) (Translate.iVE n t) := by
  apply Bootstrapping.IsSemiterm.induction 𝚺
    (P := fun t ↦ Bootstrapping.IsSemiformula ℒₛₑₜ (n + 1) (Translate.iVE n t)) ?_ ?_ ?_ ?_ t ht
  · -- Σ₁ 闸门
    definability
  · -- `bvar z`，`z < n`
    intro z hz
    rw [Translate.iVE, Bootstrapping.Language.TermRec.Construction.result_bvar]
    refine Bootstrapping.isSemiformula_iff.mpr ⟨?_, ?_⟩
    · exact (GodelQ.CG008RelCase2.eqAtom_isUFormula _
        (Bootstrapping.IsUTerm.bvar (L := ℒₛₑₜ) (z := z + 1)))
    · have h := GodelQ.CG008BvBound.bv_eqAtom_le (V := V) (^#(z + 1))
        (Bootstrapping.IsUTerm.bvar (L := ℒₛₑₜ) (z := z + 1))
      have hbv : Bootstrapping.termBV ℒₛₑₜ (^#(z + 1) : V) = z + 1 + 1 := by
        rw [Bootstrapping.termBV_bvar]
      rw [hbv] at h
      have h2 : Max.max (z + 1 + 1) 1 ≤ n + 1 := by
        rw [max_le_iff]
        refine ⟨?_, ?_⟩
        · have hh : z + 1 ≤ n := succ_le_iff_lt.mpr hz
          have h3 : z + 1 + 1 ≤ n + 1 := add_le_add_left hh 1
          exact h3
        · have h4 : (0 : V) + 1 ≤ n + 1 := add_le_add_left (Arithmetic.zero_le n) 1
          rwa [show ((0 : V) + 1) = 1 by simp] at h4
      exact le_trans h h2
  · -- `fvar x`
    intro x
    rw [Translate.iVE, Bootstrapping.Language.TermRec.Construction.result_fvar]
    refine Bootstrapping.isSemiformula_iff.mpr ⟨?_, ?_⟩
    · exact GodelQ.CG008RelCase2.eqAtom_isUFormula _
        (Bootstrapping.IsUTerm.fvar (L := ℒₛₑₜ) x)
    · have h := GodelQ.CG008BvBound.bv_eqAtom_le (V := V) (^&x)
        (Bootstrapping.IsUTerm.fvar (L := ℒₛₑₜ) x)
      have hbv : Bootstrapping.termBV ℒₛₑₜ (^&x : V) = 0 := by
        rw [Bootstrapping.termBV_fvar]
      rw [hbv] at h
      have h2 : Max.max (0 : V) 1 ≤ n + 1 := by
        rw [max_le_iff]
        refine ⟨Arithmetic.zero_le _, ?_⟩
        have h4 : (0 : V) + 1 ≤ n + 1 := add_le_add_left (Arithmetic.zero_le n) 1
        rwa [show ((0 : V) + 1) = 1 by simp] at h4
      exact le_trans h h2
  · -- `func k f v`
    intro k f v hkf hv ih
    show Bootstrapping.IsSemiformula ℒₛₑₜ (n + 1)
      (Bootstrapping.Language.TermRec.Construction.result ℒₒᵣ Translate.iVE.construction ![n]
        (^func k f v))
    rw [Bootstrapping.Language.TermRec.Construction.result_func' (c := Translate.iVE.construction)
      (param := ![n]) hkf hv.isUTerm]
    simp only [Translate.iVE.construction]
    split_ifs with hk
    · exact isSemiformula_ve0 n k f hk
    · have hk2 : k = 2 := by
        rcases (Bootstrapping.Arithmetic.isFunc_iff_LOR (V := V)).mp hkf with
          ⟨h, -⟩ | ⟨h, -⟩ | ⟨h, -⟩ | ⟨h, -⟩
        · exact absurd h hk
        · exact absurd h hk
        · exact h
        · exact h
      refine isSemiformula_ve2 n k f _ hk ?_
      intro j hj
      show Bootstrapping.IsSemiformula ℒₛₑₜ (n + 1)
        ((Bootstrapping.Language.TermRec.Construction.resultVec ℒₒᵣ Translate.iVE.construction
          ![n] k v).[j])
      rw [Bootstrapping.Language.TermRec.Construction.nth_resultVec
        (L := ℒₒᵣ) (c := Translate.iVE.construction) (param := ![n])
        (w := v) hv.isUTerm (i := j) (by rw [hk2]; exact hj)]
      exact ih j (by rw [hk2]; exact hj)

/-- **推论**：`bv (iVE n t) ≤ n + 1`。 -/
theorem bv_iVE_le {n t : V} (ht : Bootstrapping.IsSemiterm ℒₒᵣ n t) :
    Bootstrapping.bv ℒₛₑₜ (Translate.iVE n t) ≤ n + 1 :=
  (isSemiformula_iVE ht).bv_le

end GodelQ.CG008BvMain

#print axioms GodelQ.CG008BvMain.isSemiformula_iVE
#print axioms GodelQ.CG008BvMain.bv_iVE_le
#print axioms GodelQ.CG008BvMain.isSemiformula_ve2
#print axioms GodelQ.CG008BvMain.isSemiformula_conjunct
