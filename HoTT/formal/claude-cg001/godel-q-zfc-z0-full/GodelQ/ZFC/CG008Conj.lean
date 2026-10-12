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

-- **`conjunct` 的第二块未证**。层数：替换向量 `#i ∷ shiftVec b n` 的长度是 `1 + n`
-- （一个 `^#i` 加 `n` 个移位变量），所以 `subst_isUFormula` 要
-- `IsSemiformula ℒₛₑₜ (1 + n) y`，且向量要满足 `IsSemitermVec ℒₛₑₜ (1+n) (1+n) …`——
-- 后者需要**每个分量的 `termBV` ≤ `1 + n`**，而分量是 `^#i`、`^#b`、…、`^#(b+n-1)`，
-- 即需要 `i ≤ 1 + n`、`b + n - 1 ≤ 1 + n` 这类**算术界**。
-- 与第一块同理，`V` 的 `LT` 是裸的，这些界要经 `V ⊨ 𝗜𝚺₁` 的语义得到。
-- **下一步**：按调用点（`iTR` 的 `conjunct 2 n 0/1`）把 `b`、`i` 的具体值代入，
-- 届时的界是 `i ∈ {0,1}`、`b = 2`，比一般情形弱得多。

end GodelQ.CG008Conj

#print axioms GodelQ.CG008Conj.isSemitermVec_single
#print axioms GodelQ.CG008Conj.cDomN_isSemiformula_le
#print axioms GodelQ.CG008Conj.conjunct_fst_isUFormula
