import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **（真命题 1）`termBShift` 在 bvar 上与语言无关。**

证法：两侧各用 `termBShift_bvar`，都归到 `^#(z+1)`（**不含 `L`**）。 -/
lemma termBShift_lang_indep_bvar (z : V) :
    termBShift ℒₒᵣ (^#z : V) = termBShift ℒₛₑₜ (^#z : V) := by
  rw [termBShift_bvar, termBShift_bvar]

/-- **（真命题 2）`termBShift` 在 fvar 上与语言无关。**

证法：两侧各用 `termBShift_fvar`，都归到 `^&x`（**不含 `L`**）。 -/
lemma termBShift_lang_indep_fvar (x : V) :
    termBShift ℒₒᵣ (^&x : V) = termBShift ℒₛₑₜ (^&x : V) := by
  rw [termBShift_fvar, termBShift_fvar]

/-- **（真命题 3）`termSubst` 在 bvar 上与语言无关。**

两侧各用 `termSubst_bvar`，都归到 `w.[z]`。 -/
lemma termSubst_lang_indep_bvar (w z : V) :
    termSubst ℒₒᵣ w (^#z : V) = termSubst ℒₛₑₜ w (^#z : V) := by
  rw [termSubst_bvar, termSubst_bvar]

/-- **（真命题 4）`termSubst` 在 fvar 上与语言无关。** -/
lemma termSubst_lang_indep_fvar (w x : V) :
    termSubst ℒₒᵣ w (^&x : V) = termSubst ℒₛₑₜ w (^&x : V) := by
  rw [termSubst_fvar, termSubst_fvar]

end GodelQ.ProbeFL

#print axioms GodelQ.ProbeFL.termBShift_lang_indep_bvar
#print axioms GodelQ.ProbeFL.termBShift_lang_indep_fvar
#print axioms GodelQ.ProbeFL.termSubst_lang_indep_bvar
#print axioms GodelQ.ProbeFL.termSubst_lang_indep_fvar
