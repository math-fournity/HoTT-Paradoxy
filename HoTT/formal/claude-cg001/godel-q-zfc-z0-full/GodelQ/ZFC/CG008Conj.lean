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

-- **`conjunct` 的第一块未证**：`subst ?[#i] cDomN` 要 `IsSemiformula ℒₛₑₜ (i+1) cDomN`，
-- 即需要 `1 ≤ i + 1`。但 `V` 的 `LT` 是**裸的**（`ORingStructure` 只 extends `LT α`，
-- 见 `Basic/Misc.lean:16`），没有 `OrderedRing`/`Preorder` 实例——
-- 所以 `1 ≤ i + 1` **不能**由 `add_le_add_right`/`omega` 直接得到。
-- 需要用 `V ⊧ 𝗜𝚺₁` 的语义（`V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁`）把 `≤` 与系统内的 `<` 连起来。
-- **这是下一步的具体工作**，不是概念障碍。

end GodelQ.CG008Conj

#print axioms GodelQ.CG008Conj.isSemitermVec_single
#print axioms GodelQ.CG008Conj.cDomN_isSemiformula_le
