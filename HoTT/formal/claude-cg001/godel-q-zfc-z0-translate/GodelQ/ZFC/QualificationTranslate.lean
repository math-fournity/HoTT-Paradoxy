import GodelQ.ZFC.TranslateRE

/-!
# CG-007 · W4b：命题对照（CG001-C-119、C-120）

每条命题的类型逐字写在这里，证明只引用前面文件中的定理。
-/

namespace GodelQ.TranslateQual

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate

/-- **CG001-C-119（翻译在 𝗜𝚺₁ 内部是 Σ1 函数；翻译可计算）**：
(1) 在 𝗜𝚺₁ 的每个模型 V 中：内部变量等式 `iVE` 与内部翻译 `iT` 是 𝚺₁ 可定义的函数；
    对每个闭项 t，`iVE n ⌜t⌝ = ⌜varEqual t⌝`；对每个算术公式 φ，`iT n ⌜φ⌝ = ⌜translate φ⌝`；
(2) 在 ℕ 中：`iT 0 (encode σ) = encode σᵗ`；
(3) 翻译 `arithTrln.translate` 可计算（C-111 留下的阻塞引理）。 -/
theorem qual_C119 :
    (∀ (V : Type) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁],
      (𝚺ᴬ₁-Function₂ (iVE : V → V → V) via iVEDef) ∧
      (𝚺ᴬ₁-Function₂ (iT : V → V → V) via iTDef) ∧
      (∀ (n : ℕ) (t : ClosedSemiterm ℒₒᵣ n),
        iVE (n : V) ⌜t⌝ = ⌜(arithTrln.varEqual t : Semisentence ℒₛₑₜ (n + 1))⌝) ∧
      (∀ (n : ℕ) (φ : Semisentence ℒₒᵣ n),
        iT (n : V) ⌜φ⌝ = ⌜(arithTrln.translate φ : Semisentence ℒₛₑₜ n)⌝)) ∧
    (∀ σ : ArithmeticSentence,
      iT (0 : ℕ) (Encodable.encode σ) = Encodable.encode (arithTrln.translate σ)) ∧
    Computable (fun σ : ArithmeticSentence ↦ arithTrln.translate σ) :=
  ⟨fun _ _ _ ↦ ⟨iVE_defined, iT_defined, fun _ t ↦ iVE_quote t, fun _ φ ↦ iT_quote φ⟩,
   fun σ ↦ (iT_encode σ).trans (Sentence.quote_eq_encode_nat _),
   translate_computable⟩

/-- **CG001-C-120（Z0 的影子形式不再带前提）**：
(1) `{σ ∣ 𝗭𝗙𝗖 ⊢ σᵗ}` 可枚举；
(2) 𝗭𝗙𝗖 的算术影子 `Sh` 可枚举，并且扩张 𝗜𝚺₁（C-110）：C-103 的两条前提都是定理；
(3) 𝗭𝗙𝗖 证明不了它的算术影子（的 Craig 公理化）一致性句的翻译；
(4) 影子证明不了自己的一致性句。 -/
theorem qual_C120 :
    REPred (fun σ : ArithmeticSentence ↦ 𝗭𝗙𝗖 ⊢ arithTrln.translate σ) ∧
    Sh.RE ∧ 𝗜𝚺₁ ⪯ Sh ∧
    𝗭𝗙𝗖 ⊬ arithTrln.translate (Sh.craig.consistent.val) ∧
    Sh ⊬ Sh.craig.consistent.val :=
  ⟨translate_provable_re, Sh_RE, ISigma1_le_Sh, zfc_z0, sh_z0⟩

end GodelQ.TranslateQual

#print axioms GodelQ.TranslateQual.qual_C119
#print axioms GodelQ.TranslateQual.qual_C120
