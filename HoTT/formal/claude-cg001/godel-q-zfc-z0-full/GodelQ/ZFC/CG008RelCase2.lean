import GodelQ.ZFC.CG008SubstFormula

/-!
# CG-008 · `rel` 情形：`cRel` 的 `IsUFormula`
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008RelCase2

open GodelQ.ZFCArith GodelQ.Translate

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 先看两个 quote 是否 defeq
example : (⌜(Language.Eq.eq : (ℒₒᵣ).Rel 2)⌝ : V) = (⌜(Language.ORing.Rel.eq : (ℒₒᵣ).Rel 2)⌝ : V) := rfl

/-- **`cRel` 保持 `IsUFormula`**：`R` 是算术关系码时，`cRel R` 是集合语言公式的码。

`(ℒₒᵣ).Rel 2` 只有 eq/lt 两种（`isRel_iff_LOR`），
`cRel_quote` 把 `cRel ⌜r⌝` 算成 `⌜arithTrln.rel r⌝`，
后者是标准公式的码——由 `quote_isUFormula` 判定。 -/
theorem cRel_isUFormula (R : V) (hR : (ℒₒᵣ).IsRel 2 R) :
    Bootstrapping.IsUFormula ℒₛₑₜ (Translate.cRel R) := by
  rcases (Bootstrapping.Arithmetic.isRel_iff_LOR (V := V)).mp hR with ⟨-, rfl⟩ | ⟨-, rfl⟩
  · rw [cRel_quote Language.Eq.eq]
    exact FFL.FirstOrder.Sentence.quote_isUFormula _
  · rw [cRel_quote Language.LT.lt]
    exact FFL.FirstOrder.Sentence.quote_isUFormula _

/-- **`eqAtom t` 是公式**（`t` 是项时）：`^rel 2 cEqN ?[^#0, t]` 的两个参数都是项。 -/
theorem eqAtom_isUFormula (t : V) (ht : Bootstrapping.IsUTerm ℒₛₑₜ t) :
    Bootstrapping.IsUFormula ℒₛₑₜ (Translate.eqAtom t) := by
  rw [Translate.eqAtom]
  refine Bootstrapping.IsUFormula.rel.mpr ⟨?_, ?_⟩
  · exact Bootstrapping.codeIn_rel_quote (V := V) (L := ℒₛₑₜ) Language.Eq.eq
  · exact Bootstrapping.IsUTermVec.mkSeq₂_iff.mpr
      ⟨Bootstrapping.IsUTerm.bvar (L := ℒₛₑₜ) (z := 0), ht⟩

/-! ## 卡点：`iVE` 没有 rank-1 实例

`iVE_isUFormula` 需要 `IsUFormula ℒₛₑₜ (iVE n t)`，其 Σ₁ 闸门是
`𝚺ᴬ₁-Predicate (fun t ↦ IsUFormula ℒₛₑₜ (iVE n t))`。

**实测**（本轮）：
- `definability` 在该形状上 `whnf` 超时——它展不开 `iVEDef`（已标 `irreducible`）；
- 显式复合需要 `iVE` 的 **rank-1** `Function₂` 实例，而包内只有 rank-0
  （`iVE_defined : 𝚺ᴬ₁-Function₂ iVE`）；
- 补 rank-1 实例的两次尝试（`DefinableFunction.of_sigmaOne`、
  `DefinedFunction.to_definable`）都在 `Tarski.Structure ?m V` 上卡住元变量——
  与 Foundation 的 `.definable'` 约定（`Term/Functions.lean:72`）形式相同但解析失败，
  原因未查明。

**所以 `iVE_isUFormula` 未证。** 本文件保留已证的两条零件。 -/


end GodelQ.CG008RelCase2

#print axioms GodelQ.CG008RelCase2.cRel_isUFormula
#print axioms GodelQ.CG008RelCase2.eqAtom_isUFormula
