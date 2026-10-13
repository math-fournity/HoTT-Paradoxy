-- CG-009: hRoot_quoted steps 1-5 empirical assembly test.
import GodelQ.ZFC.HRoot

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate

namespace GodelQ.HRootAttempt2

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- step 2: iT 0 quote = quote translate (iT_quote at layer 0). -/
lemma iT_zero_quote (φ : Sentence ℒₒᵣ) :
    iT (0 : V) (⌜φ⌝ : V) = (⌜arithTrln.translate φ⌝ : V) :=
  iT_quote (V := V) φ

/-- steps 2 + 4: padding commutes under iT/translate. -/
lemma iT_zero_quote_padding (σ : Sentence ℒₒᵣ) (s : ℕ) :
    iT (0 : V) (⌜σ.padding s⌝ : V)
      = (⌜(arithTrln.translate σ).padding s⌝ : V) := by
  rw [iT_zero_quote, GodelQ.HRoot.translate_padding]

end GodelQ.HRootAttempt2

#print axioms GodelQ.HRootAttempt2.iT_zero_quote
#print axioms GodelQ.HRootAttempt2.iT_zero_quote_padding
