import GodelQ.ZFC.ShRE

/-!
# CG-007 · W4a：命题对照（CG001-C-111）
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory

namespace GodelQ.QualShRE

open GodelQ.ZFCArith GodelQ.ZFCZ0

/-- **CG001-C-111**：(1) 𝗭𝗙𝗖 的定理集可枚举；(2) 任一可计算、且与 `arithTrln.translate` 在 𝗭𝗙𝗖 中
可证性相同的翻译，给出 `Sh.RE`；(3) 若 `arithTrln.translate` 可计算，则 𝗭𝗙𝗖 证明不了它的算术影子
（的 Craig 公理化）一致性句的翻译。 -/
theorem qual_C111 :
    REPred (fun φ : Sentence ℒₛₑₜ ↦ 𝗭𝗙𝗖 ⊢ φ) ∧
    (∀ τ : ArithmeticSentence → Sentence ℒₛₑₜ, Computable τ →
      (∀ σ, 𝗭𝗙𝗖 ⊢ τ σ ↔ 𝗭𝗙𝗖 ⊢ arithTrln.translate σ) → Sh.RE) ∧
    (∀ h : Computable (fun σ : ArithmeticSentence ↦ arithTrln.translate σ),
      letI := Sh_RE_of_translate_computable h
      𝗭𝗙𝗖 ⊬ arithTrln.translate (Sh.craig.consistent.val)) :=
  ⟨zfc_provable_re, Sh_RE_of_computable, zfc_z0_of_translate_computable⟩

end GodelQ.QualShRE

#print axioms GodelQ.QualShRE.qual_C111
