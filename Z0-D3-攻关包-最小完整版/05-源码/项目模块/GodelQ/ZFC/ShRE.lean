import GodelQ.ZFC.Z0PA

/-!
# CG-007 · W4a：𝗭𝗙𝗖 的定理集可枚举；`Sh.RE` 归结为翻译的可计算性

* `zfc_provable_re`：`{φ ∣ 𝗭𝗙𝗖 ⊢ φ}` 可枚举（推广 C-97：那里只对“永不停机”句一族）。
  由 `𝗭𝗙𝗖.Δ₁`（C-95），`b ↦ Provable 𝗭𝗙𝗖 b` 是 Σ1 谓词；Foundation 的 `provable_iff_provable` 与
  `Sentence.quote_eq_encode_nat` 把它接到 Mathlib 的编码上。
* `Sh_RE_of_computable`：只要有一个可计算的翻译 τ，使 𝗭𝗙𝗖 对每个算术句证明 τ σ 当且仅当证明 σᵗ，
  𝗭𝗙𝗖 的算术影子 `Sh` 就可枚举。特例 `Sh_RE_of_translate_computable`：翻译 `arithTrln.translate`
  本身可计算。
* `zfc_z0_of_translate_computable`：于是 Z0 只剩一条纯语法引理——翻译 `arithTrln.translate`
  （从算术句到集合论句）可计算。这条引理关于一个具体的、按公式结构递归定义的函数，与 𝗭𝗙𝗖 的
  可证性无关；本文件没有证明它（见 `CLAIM.md` §4 的阻塞分析）。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping SetTheory
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.ZFCZ0

open GodelQ.ZFCArith

/-- **𝗭𝗙𝗖 的定理集可枚举。** -/
theorem zfc_provable_re : REPred (fun φ : Sentence ℒₛₑₜ ↦ 𝗭𝗙𝗖 ⊢ φ) := by
  have h : 𝚺ᴬ₁-Predicate fun b : ℕ ↦ Bootstrapping.Provable 𝗭𝗙𝗖 b := by definability
  apply REPred.of_eq ((rePred_iff_sigma1.mpr h).comp Computable.encode)
  intro φ
  rw [← provable_iff_provable, Sentence.quote_eq_encode_nat]

/-- 有一个可计算的翻译 τ，与 `arithTrln.translate` 在 𝗭𝗙𝗖 中可证性相同，则 `Sh` 可枚举。 -/
theorem Sh_RE_of_computable (τ : ArithmeticSentence → Sentence ℒₛₑₜ) (hτ : Computable τ)
    (heq : ∀ σ, 𝗭𝗙𝗖 ⊢ τ σ ↔ 𝗭𝗙𝗖 ⊢ arithTrln.translate σ) : Sh.RE :=
  ⟨(zfc_provable_re.comp hτ).of_eq fun σ ↦ (heq σ).trans mem_Sh.symm⟩

/-- 特例：翻译 `arithTrln.translate` 本身可计算，则 `Sh` 可枚举。 -/
theorem Sh_RE_of_translate_computable
    (h : Computable (fun σ : ArithmeticSentence ↦ arithTrln.translate σ)) : Sh.RE :=
  Sh_RE_of_computable _ h fun _ ↦ Iff.rfl

/-- **Z0 只剩一条纯语法引理**：若翻译 `arithTrln.translate` 可计算，则 𝗭𝗙𝗖 证明不了它的算术影子
（的 Craig 公理化）一致性句的翻译。 -/
theorem zfc_z0_of_translate_computable
    (h : Computable (fun σ : ArithmeticSentence ↦ arithTrln.translate σ)) :
    letI := Sh_RE_of_translate_computable h
    𝗭𝗙𝗖 ⊬ arithTrln.translate (Sh.craig.consistent.val) :=
  letI := Sh_RE_of_translate_computable h
  zfc_z0_of_RE

end GodelQ.ZFCZ0

#print axioms GodelQ.ZFCZ0.zfc_provable_re
#print axioms GodelQ.ZFCZ0.Sh_RE_of_computable
#print axioms GodelQ.ZFCZ0.Sh_RE_of_translate_computable
#print axioms GodelQ.ZFCZ0.zfc_z0_of_translate_computable
