import GodelQ.ZFC.InternalTranslate

/-!
# CG-007 · W4b：翻译可计算；`Sh.RE` 与 Z0 的影子形式不再带条件

* `iT_encode`：在标准模型 ℕ 里，内部翻译把算术句 σ 的编码送到 `σᵗ` 的编码（由 `iT_quote`）。
* `translate_computable`：翻译 `arithTrln.translate` 可计算。这就是 C-111 留下的阻塞引理；
  证法：内部翻译 `iT` 是 𝚺₁ 可定义的函数，Foundation 的 `computable_iff_sigma1` 把它变成
  Mathlib 意义下的可计算函数，再经编码搬到句子上。
* `translate_provable_re`：`{σ ∣ 𝗭𝗙𝗖 ⊢ σᵗ}` 可枚举（直接由内部翻译与 𝗭𝗙𝗖 的 Σ1 可证性得到，
  不经过 `translate_computable`）。
* `Sh_RE`：𝗭𝗙𝗖 的算术影子可枚举（经 C-111 的归结 `Sh_RE_of_translate_computable`）。
* `zfc_z0`、`sh_z0`：Z0 的影子形式不再带任何前提。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping SetTheory
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.ZFCZ0

open GodelQ.ZFCArith GodelQ.Translate

/-- 在标准模型 ℕ 里，内部翻译把 `encode σ` 送到 `⌜σᵗ⌝`。 -/
lemma iT_encode (σ : ArithmeticSentence) :
    iT (0 : ℕ) (Encodable.encode σ) = (⌜arithTrln.translate σ⌝ : ℕ) := by
  have h := iT_quote (V := ℕ) σ
  rw [Sentence.quote_eq_encode_nat σ] at h
  simpa using h

/-- 内部翻译（层数 0）在 ℕ 上可计算。 -/
lemma iT_zero_computable : Computable (fun b : ℕ ↦ iT (0 : ℕ) b) :=
  computable_iff_sigma1.mpr (by definability)

/-- **翻译可计算**：C-111 的阻塞引理。 -/
theorem translate_computable : Computable (fun σ : ArithmeticSentence ↦ arithTrln.translate σ) := by
  apply Computable.encode_iff.mp
  exact (iT_zero_computable.comp Computable.encode).of_eq fun σ ↦
    (iT_encode σ).trans (Sentence.quote_eq_encode_nat _)

/-- **翻译后的可证性可枚举**：`{σ ∣ 𝗭𝗙𝗖 ⊢ σᵗ}` 可枚举。 -/
theorem translate_provable_re :
    REPred (fun σ : ArithmeticSentence ↦ 𝗭𝗙𝗖 ⊢ arithTrln.translate σ) := by
  have h : 𝚺ᴬ₁-Predicate fun b : ℕ ↦ Bootstrapping.Provable 𝗭𝗙𝗖 (iT 0 b) := by definability
  apply REPred.of_eq ((rePred_iff_sigma1.mpr h).comp Computable.encode)
  intro σ
  rw [← provable_iff_provable, iT_encode]

/-- **𝗭𝗙𝗖 的算术影子可枚举**：C-111 的前提付清。 -/
instance Sh_RE : Sh.RE := Sh_RE_of_translate_computable translate_computable

/-- **Z0 的影子形式，不带前提**：𝗭𝗙𝗖 证明不了它的算术影子（的 Craig 公理化）一致性句的翻译。 -/
theorem zfc_z0 : 𝗭𝗙𝗖 ⊬ arithTrln.translate (Sh.craig.consistent.val) := zfc_z0_of_RE

/-- 同一结论的影子形式：影子证明不了自己的一致性句。 -/
theorem sh_z0 : Sh ⊬ Sh.craig.consistent.val := sh_z0_of_RE

end GodelQ.ZFCZ0

#print axioms GodelQ.Translate.iVE_quote
#print axioms GodelQ.Translate.iT_quote
#print axioms GodelQ.ZFCZ0.iT_encode
#print axioms GodelQ.ZFCZ0.translate_computable
#print axioms GodelQ.ZFCZ0.translate_provable_re
#print axioms GodelQ.ZFCZ0.Sh_RE
#print axioms GodelQ.ZFCZ0.zfc_z0
#print axioms GodelQ.ZFCZ0.sh_z0
