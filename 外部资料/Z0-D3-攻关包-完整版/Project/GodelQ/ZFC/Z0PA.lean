import GodelQ.ZFC.Z0Shadow
import GodelQ.ZFC.PAModel

/-!
# CG-007 · W3（三）：Z0 的第一条前提成为定理

C-103 把 Z0（𝗭𝗙𝗖 证明不了自己的矛盾搜索永不停机）化成两条前提：`Sh.RE` 与 `𝗜𝚺₁ ⪯ Sh`。
由 `paInterp : 𝗭𝗙𝗖 ⊳ 𝗣𝗔`，𝗭𝗙𝗖 的算术影子扩张 𝗣𝗔，于是扩张 𝗜𝚺₁（Foundation 的 `𝗜𝚺₁ ⪯ 𝗣𝗔`）。
Z0 只剩一条前提 `Sh.RE`。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory

namespace GodelQ.ZFCZ0

open GodelQ.ZFCArith

/-- 𝗭𝗙𝗖 证明 𝗣𝗔 的每个定理的翻译。 -/
theorem zfc_proves_PA_theorems {σ : ArithmeticSentence} (h : 𝗣𝗔 ⊢ σ) :
    𝗭𝗙𝗖 ⊢ arithTrln.translate σ :=
  paInterp.of_provability h

/-- 𝗭𝗙𝗖 的算术影子扩张 𝗣𝗔。 -/
instance PA_le_Sh : 𝗣𝗔 ⪯ Sh :=
  Entailment.weakerThan_iff.mpr fun h ↦ (Sh_provable_iff _).mpr (paInterp.of_provability h)

/-- 𝗭𝗙𝗖 的算术影子扩张 𝗜𝚺₁：C-103 的第二条前提，现在是定理。 -/
instance ISigma1_le_Sh : 𝗜𝚺₁ ⪯ Sh :=
  Entailment.WeakerThan.trans (inferInstance : 𝗜𝚺₁ ⪯ 𝗣𝗔) PA_le_Sh

/-- **Z0 只剩一条前提**：若 𝗭𝗙𝗖 的算术影子可枚举，则 𝗭𝗙𝗖 证明不了这个影子（的 Craig 公理化）
不矛盾这句话的翻译。 -/
theorem zfc_z0_of_RE [Sh.RE] : 𝗭𝗙𝗖 ⊬ arithTrln.translate (Sh.craig.consistent.val) :=
  zfc_z0_conditional

/-- 同一结论的影子形式。 -/
theorem sh_z0_of_RE [Sh.RE] : Sh ⊬ Sh.craig.consistent.val :=
  sh_z0_conditional

end GodelQ.ZFCZ0

#print axioms GodelQ.ZFCZ0.zfc_proves_PA_theorems
#print axioms GodelQ.ZFCZ0.PA_le_Sh
#print axioms GodelQ.ZFCZ0.ISigma1_le_Sh
#print axioms GodelQ.ZFCZ0.zfc_z0_of_RE
#print axioms GodelQ.ZFCZ0.sh_z0_of_RE
