import GodelQ.ZFC.CG008Ve2

/-!
# CG-008 · `conjunct` 的公式性：正确的层数

`conjunct b n i y = (subst ?[#i] cDomN) ⋏ (subst (#i ∷ shiftVec b n) y)`。

**层数事实**（本轮查清）：`subst L w q` 要 `IsSemitermVec L n m w`，即 `len w = n`。
`?[^#i]` 是单分量向量，`len` 是 **1**——与 `i` 无关。分量 `^#i` 要在层 `m` 是项，
即 `i < m`。所以取 `n = 1`、`m := i + 1`。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Conj
open GodelQ.ZFCArith GodelQ.Translate GodelQ.CG008VeParts
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- `?[^#i]` 在层 `i + 1` 是项向量。 -/
lemma isSemitermVec_single (i : V) :
    Bootstrapping.IsSemitermVec ℒₛₑₜ 1 (i + 1) (?[^#i] : V) := by
  refine Bootstrapping.IsSemitermVec.iff.mpr ⟨?_, ?_⟩
  · simp
  · intro j hj
    have hj0 : j = 0 := by
      have hh := hj
      simp at hh
      exact hh
    subst hj0
    simpa using
      (Bootstrapping.IsSemiterm.bvar (L := ℒₛₑₜ) (n := i + 1) (z := i)).mpr (by simp)

/-- `cDomN` 在任意层 `≥ 1` 都是 `IsSemiformula`（层数只增不减）。 -/
lemma cDomN_isSemiformula_le {n : V} (hn : 1 ≤ n) :
    Bootstrapping.IsSemiformula ℒₛₑₜ n ((Translate.cDomN : ℕ) : V) := by
  rcases GodelQ.CG008Ve2.cDomN_isSemiformula (V := V) with ⟨hu, hbv⟩
  exact ⟨hu, le_trans hbv hn⟩

/-- **`conjunct` 的第一块**：`subst ?[#i] cDomN` 是公式。

**层数**：`subst_isUFormula` 的形状是
`IsSemiformula L n p → IsSemitermVec L n m w → IsSemiformula L m (subst L w p)`。
`?[^#i]` 给的是 `IsSemitermVec L 1 (i+1)`，所以 **`n = 1`**（不是 `i+1`！），
而 `cDomN` 恰好在层 1 是 `IsSemiformula`（`cDomN_isSemiformula`）——
**不需要 `1 ≤ i + 1`**。先前把 `n` 与 `m` 弄反了。 -/
lemma conjunct_fst_isUFormula (i : V) :
    Bootstrapping.IsUFormula ℒₛₑₜ (Bootstrapping.subst ℒₛₑₜ (?[^#i] : V) (Translate.cDomN : V)) :=
  GodelQ.CG008SubstFormula.subst_isUFormula (n := 1) (m := i + 1)
    (isSemitermVec_single i) (GodelQ.CG008Ve2.cDomN_isSemiformula (V := V))

end GodelQ.CG008Conj

#print axioms GodelQ.CG008Conj.isSemitermVec_single
#print axioms GodelQ.CG008Conj.cDomN_isSemiformula_le
#print axioms GodelQ.CG008Conj.conjunct_fst_isUFormula
