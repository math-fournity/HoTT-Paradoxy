import GodelQ.ZFC.NumeralCode
import Foundation.FirstOrder.Arithmetic.Bootstrapping.DerivabilityCondition.D1

/-!
# CG-006 · S2d：𝗭𝗙𝗖 证明的“永不停机”句构成可枚举集合

对任意固定的 ℒₛₑₜ 公式 `Φ(z)`（之后取为“z 编码的过程停机”的翻译），令
`haltsS Φ n := ∃z (Num_n(z) ∧ Φ(z))`，`neverS Φ n := ¬ haltsS Φ n`。
由 `𝗭𝗙𝗖.Δ₁`（S2b）与 `numCode`（S2c），`n ↦ Provable 𝗭𝗙𝗖 ⌜neverS Φ n⌝` 是 Σ1 谓词；
经 Foundation 的 `provable_iff_provable` 与 `rePred_iff_sigma1`，得到 `REPred`。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping SetTheory
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.ZFCNum

open GodelQ.ZFCDelta1

/-- `∃z (Num_n(z) ∧ Φ(z))`。 -/
def haltsS (Φ : SetTheorySemisentence 1) (n : ℕ) : Sentence ℒₛₑₜ := ∃¹ (numeralF n ⋏ Φ)

/-- `¬ ∃z (Num_n(z) ∧ Φ(z))`。 -/
def neverS (Φ : SetTheorySemisentence 1) (n : ℕ) : Sentence ℒₛₑₜ := ∼ haltsS Φ n

/-- 句子的否定的编码是内部 `neg`。 -/
lemma sentence_quote_neg (σ : Sentence ℒₛₑₜ) : (⌜∼σ⌝ : ℕ) = Bootstrapping.neg ℒₛₑₜ (⌜σ⌝ : ℕ) := by
  rw [Sentence.quote_def, Sentence.quote_def]
  have h : (Rewriting.emb (∼σ) : SetTheorySemiproposition 0) = ∼ (Rewriting.emb σ) := by simp
  rw [h]
  change (⌜∼ (Rewriting.emb σ : SetTheorySemiproposition 0)⌝ : Bootstrapping.Semiformula ℕ ℒₛₑₜ 0).val
    = Bootstrapping.neg ℒₛₑₜ
      (⌜(Rewriting.emb σ : SetTheorySemiproposition 0)⌝ : Bootstrapping.Semiformula ℕ ℒₛₑₜ 0).val
  rw [LCWQIsoGödelQuote.neg, Bootstrapping.Semiformula.val_neg]

lemma quote_haltsS (Φ : SetTheorySemisentence 1) (n : ℕ) :
    (⌜haltsS Φ n⌝ : ℕ) = ^∃ ((⌜numeralF n⌝ : ℕ) ^⋏ (⌜Φ⌝ : ℕ)) := by
  simp [haltsS]

lemma quote_neverS (Φ : SetTheorySemisentence 1) (n : ℕ) :
    (⌜neverS Φ n⌝ : ℕ) = Bootstrapping.neg ℒₛₑₜ (^∃ (numCode (n : ℕ) ^⋏ ↑(⌜Φ⌝ : ℕ))) := by
  rw [numCode_quote, ← quote_haltsS]
  exact sentence_quote_neg (haltsS Φ n)

/-- **S2d**：`{n ∣ 𝗭𝗙𝗖 ⊢ neverS Φ n}` 可枚举。 -/
theorem never_re (Φ : SetTheorySemisentence 1) :
    REPred (fun n : ℕ ↦ 𝗭𝗙𝗖 ⊢ neverS Φ n) := by
  have : 𝚺ᴬ₁-Predicate fun b : ℕ ↦ Bootstrapping.Provable 𝗭𝗙𝗖
      (Bootstrapping.neg ℒₛₑₜ (^∃ (numCode b ^⋏ ↑(⌜Φ⌝ : ℕ)))) := by
    definability
  apply REPred.of_eq (rePred_iff_sigma1.mpr this)
  intro n
  rw [← provable_iff_provable, quote_neverS]

#print axioms never_re

end GodelQ.ZFCNum
