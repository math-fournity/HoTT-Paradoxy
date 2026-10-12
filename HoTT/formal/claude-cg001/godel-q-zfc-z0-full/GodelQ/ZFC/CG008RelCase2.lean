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

/-! ## 卡点：`ve0` 的 `cFunc` 码

`ve0 k f = imp ⊤ (subst ?[#0] (cFunc k f))`，`cFunc` 是**自然数码**（`cFuncN`）。
要证 `IsUFormula` 需要：
1. `cFunc k f` 是标准公式的码（`cFuncN` 的四分支各是 `⌜arithTrln.func …⌝`）；
2. 该码经 `↑· : V` 后仍是公式（`coe_quote_eq_quote`）。

**实测**：第 1 步的 `cFuncN` 是 `if` 套 `if`，`rw` 只展开外层；
内层在部分分支（如 `h✝ : ¬f = 0` 时的 `cFuncN 0 1`）**保持未展开**，
再 `rw [Translate.cFuncN]` 触发 `whnf` 超时。

**单分支的 `coe_quote_eq_quote` 路线已单独验证成功**
（`rw [coe_quote_eq_quote …]` 后 `exact quote_isUFormula _`，见本文件顶部 `cRel_isUFormula` 的同类用法），
但**四分支统一处理**未成功。**所以 `ve0_isUFormula` 未证。** -/

end GodelQ.CG008RelCase2

#print axioms GodelQ.CG008RelCase2.cRel_isUFormula
#print axioms GodelQ.CG008RelCase2.eqAtom_isUFormula
