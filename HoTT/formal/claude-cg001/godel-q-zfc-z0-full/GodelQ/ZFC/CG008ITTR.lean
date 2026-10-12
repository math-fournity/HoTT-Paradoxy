import GodelQ.ZFC.CG008SubstNine
import GodelQ.ZFC.InternalTranslate

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open GodelQ.Translate GodelQ.ZFCArith
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
namespace GodelQ.CG008ITTR
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

section
variable {L : Language} [L.Encodable] [L.LORDefinable]

set_option maxHeartbeats 800000 in
/-- **零件 A**：`cRel R` 是公式码。

**桥**：`Sentence.coe_quote_eq_quote`（`Formula/Coding.lean:263`）：
`(⌜phi⌝ : ℕ) : V) = ⌜phi⌝`。
本包自己的 `cRel_quote`（`InternalTranslate.lean:541`）用的就是它。
本题里 `cRelN 0 = ⌜(arithTrln.rel eq : Semisentence ℒₛₑₜ 2)⌝`（按定义），
`cRelN 1` 同理，所以只需把 `⌜.⌝` 换成 `↑⌜.⌝`。 -/
theorem cRel_isUFormula (R : V) : Bootstrapping.IsUFormula ℒₛₑₜ (cRel R) := by
  by_cases hR : R = 0
  · have h : (cRel R) = (((⌜(arithTrln.rel Language.ORing.Rel.eq : Semisentence ℒₛₑₜ 2)⌝ : ℕ) : V)) := by
      simp [cRel, cRelN, hR]
    rw [h]
    rw [Sentence.coe_quote_eq_quote]
    exact Sentence.quote_isUFormula (V := V) (L := ℒₛₑₜ) (arithTrln.rel Language.ORing.Rel.eq)
  · have h : (cRel R) = (((⌜(arithTrln.rel Language.ORing.Rel.lt : Semisentence ℒₛₑₜ 2)⌝ : ℕ) : V)) := by
      simp [cRel, cRelN, hR]
    rw [h]
    rw [Sentence.coe_quote_eq_quote]
    exact Sentence.quote_isUFormula (V := V) (L := ℒₛₑₜ) (arithTrln.rel Language.ORing.Rel.lt)

end
end GodelQ.CG008ITTR