import GodelQ.ZFC.TranslateRE

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate

namespace D3Probe

-- What exactly is `Provable 𝗭𝗙𝗖 (⌜zfcTr σ⌝ : V)` vs `Provable 𝗭𝗙𝗖 (⌜translate σ⌝ : V)`?
-- zfcTr σ = trProv.val/[⌜σ⌝]  — an ARITHMETIC sentence (a formula about numbers).
-- translate σ — a SET-THEORETIC sentence.
-- So "𝗭𝗙𝗖 proves the arithmetic sentence zfcTr σ" means: 𝗭𝗙𝗖 ⊢ ⌜(zfcTr σ)⌝ where the quote is
-- of an ARITHMETIC formula embedded... but 𝗭𝗙𝗖's Provable takes a V (number code).
-- Let's just check the two are different objects.
example (σ : ArithmeticSentence) : Provable 𝗭𝗙𝗼 (⌜(zfcTr σ : ArithmeticSentence)⌝ : ℕ) ≠
    Provable 𝗭𝗙𝗼 (⌜arithTrln.translate σ⌝ : ℕ) := by
  sorry

end D3Probe
