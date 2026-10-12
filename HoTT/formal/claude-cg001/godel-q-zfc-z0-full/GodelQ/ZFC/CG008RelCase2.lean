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

/-! ## `iVE_isUFormula`：闸门已开

`iVE` 的 rank-1 实例已在 `InternalTranslate.lean` 补齐（`iVE_definable'`），
所以 `P t := IsUFormula ℒₛₑₜ (iVE n t)` 的 Σ₁ 闸门现在可过。 -/

-- 早先记录的 `ve0` 卡点（`cFunc` 的四分支 if）**已解决**：
-- 见 `CG008VeLevel.ve0_isUFormula` 与 `CG008VeParts.cFunc_isUFormula`。
-- 关键修法：**先 split_ifs 再**用 `coe_quote_eq_quote` 桥 `↑⌜·⌝`（早先顺序反了）。

end GodelQ.CG008RelCase2

#print axioms GodelQ.CG008RelCase2.cRel_isUFormula
#print axioms GodelQ.CG008RelCase2.eqAtom_isUFormula
