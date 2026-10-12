import GodelQ.ZFC.CG008SubstFormula

/-!
# CG-008 · `ve0`/`ve2` 装配：`cFunc` 的公式性

`ve0 k f = imp ⊤ (subst ?[#0] (cFunc k f))`。要证它是公式，需要
`cFunc k f` 是公式的码、且替换保持公式性。

本文件给出三块（均公理洁净）：

| 引理 | 内容 |
|---|---|
| `cFuncN_isUFormula` | `cFuncN i j` 的码（自然数）是公式的码 |
| `cFunc_isUFormula` | `cFunc k f` 是公式的码（四分支穷举） |
| `subst_singleton_isUFormula` | `subst ?[#0] q` 保持公式性（层 1） |

**未证**：`ve0_isUFormula` 的最后一跳——`cFunc k f` 的层数依分支而变
（zero/one 是 1，add/mul 是 3），`subst_singleton_isUFormula` 只吃层 1 的公式。
需要一条按分支给层数的 `IsSemiformula` 版本（本轮两次尝试均未过）。 -/



open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008VeParts
open GodelQ.ZFCArith GodelQ.Translate
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- `cFuncN i j` 的码总是标准公式的码。 -/
lemma cFuncN_isUFormula (i j : ℕ) :
    Bootstrapping.IsUFormula ℒₛₑₜ ((Translate.cFuncN i j : ℕ) : V) := by
  by_cases hi : i = 0 <;> by_cases hj : j = 0 <;>
    simp only [Translate.cFuncN, hi, hj, ↓reduceIte]
  all_goals
    first
      | rw [FFL.FirstOrder.Sentence.coe_quote_eq_quote (V := V) (L := ℒₛₑₜ) (n := 1)
          (arithTrln.func Language.ORing.Func.zero)]
        exact FFL.FirstOrder.Sentence.quote_isUFormula (V := V) (L := ℒₛₑₜ) _
      | rw [FFL.FirstOrder.Sentence.coe_quote_eq_quote (V := V) (L := ℒₛₑₜ) (n := 1)
          (arithTrln.func Language.ORing.Func.one)]
        exact FFL.FirstOrder.Sentence.quote_isUFormula (V := V) (L := ℒₛₑₜ) _
      | rw [FFL.FirstOrder.Sentence.coe_quote_eq_quote (V := V) (L := ℒₛₑₜ) (n := 3)
          (arithTrln.func Language.ORing.Func.add)]
        exact FFL.FirstOrder.Sentence.quote_isUFormula (V := V) (L := ℒₛₑₜ) _
      | rw [FFL.FirstOrder.Sentence.coe_quote_eq_quote (V := V) (L := ℒₛₑₜ) (n := 3)
          (arithTrln.func Language.ORing.Func.mul)]
        exact FFL.FirstOrder.Sentence.quote_isUFormula (V := V) (L := ℒₛₑₜ) _

/-- `cFunc k f` 是公式的码（四分支都是 `cFuncN i j`）。 -/
lemma cFunc_isUFormula (k f : V) : Bootstrapping.IsUFormula ℒₛₑₜ (Translate.cFunc k f) := by
  rw [Translate.cFunc]
  by_cases hk : k = 0 <;> by_cases hf : f = 0 <;> simp only [hk, hf, ↓reduceIte]
  · exact cFuncN_isUFormula 0 0
  · exact cFuncN_isUFormula 0 1
  · exact cFuncN_isUFormula 2 0
  · exact cFuncN_isUFormula 2 1

-- `subst L w q`：`w : IsSemitermVec L n m w`，即 `len w = n` 且各分量在层 `n` 是项，
-- 结果在层 `m`。取 `w = ?[^#0]`（`len = 1`）、`n = 1`、`m = 1`：
-- 分量 `^#0` 需 `0 < 1`（成立）。所以公式的层数也必须是 1。
lemma subst_singleton_isUFormula {q : V}
    (hq : Bootstrapping.IsSemiformula ℒₛₑₜ 1 q) :
    Bootstrapping.IsUFormula ℒₛₑₜ (Bootstrapping.subst ℒₛₑₜ (?[^#0] : V) q) := by
  have hw : Bootstrapping.IsSemitermVec ℒₛₑₜ 1 1 (?[^#0] : V) := by
    refine Bootstrapping.IsSemitermVec.iff.mpr ⟨?_, ?_⟩
    · simp
    · intro i hi
      have hi0 : i = 0 := by
        have hh := hi
        simp at hh
        exact hh
      subst hi0
      simpa using (Bootstrapping.IsSemiterm.bvar (L := ℒₛₑₜ) (n := 1) (z := 0)).mpr (by simp)
  exact GodelQ.CG008SubstFormula.subst_isUFormula (n := 1) (m := 1) hw hq

-- 任意下标 `^#z` 的版本未证：`len ?[^#z]` 是 1，而 `IsSemitermVec L n m w` 要求 `len w = n`，
-- 所以层数固定为 1，`z` 必须满足 `z < 1`。**`conjunct` 的 `?[#i]` 用任意下标，与此不符**——
-- 这说明 `conjunct` 的层数论证需要另找形式（`?[#i]` 的层数实为 `i + 1`）。

end GodelQ.CG008VeParts

#print axioms GodelQ.CG008VeParts.cFuncN_isUFormula
#print axioms GodelQ.CG008VeParts.cFunc_isUFormula
#print axioms GodelQ.CG008VeParts.subst_singleton_isUFormula