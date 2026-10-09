import GodelQ.ZFC.Z0PA

/-!
# CG-007 · W3：命题对照（CG001-C-109、C-110）
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory

namespace GodelQ.QualZ0PA

open GodelQ.ZFCArith GodelQ.ZFCZ0

/-- **CG001-C-109**：每个 𝗭𝗙𝗖 模型的 ω（翻译 `arithTrln` 给出的解释）满足 𝗣𝗔；𝗭𝗙𝗖 直接解释 𝗣𝗔；
𝗭𝗙𝗖 证明 𝗣𝗔 每个定理的翻译。 -/
theorem qual_C109 :
    (∀ (M : Type) [SetStructure M] [Nonempty M] [M↓[ℒₛₑₜ] ⊧* 𝗭𝗙𝗖], (N M)↓[ℒₒᵣ] ⊧* 𝗣𝗔) ∧
    Nonempty (𝗭𝗙𝗖 ⊳ 𝗣𝗔) ∧
    (∀ σ : ArithmeticSentence, 𝗣𝗔 ⊢ σ → 𝗭𝗙𝗖 ⊢ arithTrln.translate σ) :=
  ⟨fun _ _ _ _ => models_PA, ⟨paInterp⟩, fun _ h => zfc_proves_PA_theorems h⟩

/-- **CG001-C-110**：𝗭𝗙𝗖 的算术影子扩张 𝗣𝗔 与 𝗜𝚺₁（C-103 的第二条前提成为定理）；Z0 只剩一条前提：
若 `Sh.RE`，则 𝗭𝗙𝗖 证明不了影子（的 Craig 公理化）一致性句的翻译，影子也证明不了自己的一致性句。 -/
theorem qual_C110 :
    (𝗣𝗔 ⪯ Sh) ∧ (𝗜𝚺₁ ⪯ Sh) ∧
    (∀ [Sh.RE], 𝗭𝗙𝗖 ⊬ arithTrln.translate (Sh.craig.consistent.val) ∧
      Sh ⊬ Sh.craig.consistent.val) :=
  ⟨inferInstance, inferInstance, ⟨zfc_z0_of_RE, sh_z0_of_RE⟩⟩

end GodelQ.QualZ0PA

#print axioms GodelQ.QualZ0PA.qual_C109
#print axioms GodelQ.QualZ0PA.qual_C110
