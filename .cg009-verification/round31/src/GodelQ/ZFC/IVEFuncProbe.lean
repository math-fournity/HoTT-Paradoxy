-- CG-009: the func case of iVE_shift — reduction shape.
import GodelQ.ZFC.TranslateShiftCompat

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

namespace GodelQ.IVEFuncProbe
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- Key reduction: it suffices that resultVec commutes pointwise with termShiftVec at the term level.
-- Check: does `shift` distribute over `conjunct`?  (conjunct n k i x = x ^⋏ x ^⋏ ... )
#check @conjunct
#check @shift_and
-- ve2 = qqAlls (imp (conjunct 3 n 0 w.[0] ⋏ (conjunct 3 n 1 w.[1] ⋏ ⊤)) (subst (^#2 ∷ [#0,#1]) (cFunc k f))) 2
-- Under shift: need shift (conjunct 3 n i x) and shift (subst ... (cFunc k f)) [closed!].
-- The subst part is closed (cFunc is numeral) — shift_quote route handles it.
-- conjunct part: conjunct n k i x = x ^⋏ (x ^⋏ (... )) — need shift_conjunct.

-- probe: does conjunct admit a shift rule via shift_and + induction on the arity index?
example (n k i x : V) : True := by trivial
