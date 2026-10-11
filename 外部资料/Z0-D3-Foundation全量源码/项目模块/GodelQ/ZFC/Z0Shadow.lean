import GodelQ.ZFC.Effective
import Foundation.FirstOrder.Incompleteness.Second

/-!
# CG-006 · S6：Z0 的最小可续形式状态

Z0 是“𝗭𝗙𝗖 证明不了自己的矛盾搜索永不停机”，即哥德尔第二不完备定理落在 𝗭𝗙𝗖 上。
Foundation 的第二定理针对算术理论；𝗭𝗙𝗖 是集合论。本文件把两者接起来，并把还没有证明的
两步写成精确的 Lean 前提。

* `Sh := {σ ∣ 𝗭𝗙𝗖 ⊢ σᵗ}` 是 𝗭𝗙𝗖 的算术影子（`σᵗ := arithTrln.translate σ`）。
* 已证：`Sh ⊢ σ ↔ 𝗭𝗙𝗖 ⊢ σᵗ`；`Sh` 一致（来自 Foundation 的 `zfc_consistent`）；
  `𝗥₀ ⪯ Sh`（来自 S3 的 `arithInterp : 𝗭𝗙𝗖 ⊳ 𝗥₀`）。
* 条件定理：若 `Sh.RE` 且 `𝗜𝚺₁ ⪯ Sh`，则 `𝗭𝗙𝗖 ⊬ (Sh.craig.consistent)ᵗ`。

两条前提就是 S6 的卡点：
1. `Sh.RE`：`σ ↦ 𝗭𝗙𝗖 ⊢ σᵗ` 可枚举。需要翻译 `arithTrln.translate` 的可计算性（或其内部 Σ1 定义），
   再与 `𝗭𝗙𝗖.Δ₁`（CG001-C-95）给出的可证性 Σ1 性相接。
2. `𝗜𝚺₁ ⪯ Sh`：𝗭𝗙𝗖 解释 𝗜𝚺₁。按 `arithInterp` 的做法，要证明每个 𝗭𝗙𝗖 模型的 ω 满足
   𝗣𝗔⁻ 与 Σ1 归纳（归纳实例经分离公理在模型中取子集，再用 ω 是最小归纳集）。

`Sh.craig.consistent` 说的是“𝗭𝗙𝗖 的算术影子（以 Craig 技巧取得的 Δ1 公理化）不矛盾”。
在 Lean 元层，`Sh` 矛盾当且仅当 𝗭𝗙𝗖 矛盾（`Sh_provable_iff`）；把这一等价搬进 𝗜𝚺₁ 内部，
是 Z0 读作“𝗭𝗙𝗖 证明不了 Con(𝗭𝗙𝗖)”时的第三步，本文件没有做。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory
open scoped FFL.FirstOrder.Arithmetic

namespace GodelQ.ZFCZ0

open GodelQ.ZFCArith

/-- 𝗭𝗙𝗖 的算术影子：被 𝗭𝗙𝗖 证明了翻译的算术句子。 -/
def Sh : ArithmeticTheory := {σ | 𝗭𝗙𝗖 ⊢ arithTrln.translate σ}

lemma mem_Sh {σ : ArithmeticSentence} : σ ∈ Sh ↔ 𝗭𝗙𝗖 ⊢ arithTrln.translate σ := Iff.rfl

/-- 𝗭𝗙𝗖 直接解释它的算术影子。 -/
noncomputable abbrev shInterp : 𝗭𝗙𝗖 ⊳ Sh where
  trln := arithTrln
  interpret_theory _ hφ := hφ

/-- 影子恰好是 𝗭𝗙𝗖 经翻译所证的东西。 -/
lemma Sh_provable_iff (σ : ArithmeticSentence) : Sh ⊢ σ ↔ 𝗭𝗙𝗖 ⊢ arithTrln.translate σ :=
  ⟨fun h ↦ shInterp.of_provability h, fun h ↦ Entailment.by_axm (mem_Sh.mpr h)⟩

/-- 影子一致（来自 Foundation 的 `zfc_consistent`，Lean 元层的 `Universe` 模型）。 -/
instance Sh_consistent : Entailment.Consistent Sh :=
  Entailment.consistent_iff_unprovable_bot.mpr fun h ↦ by
    have h₁ : 𝗭𝗙𝗖 ⊢ arithTrln.translate (⊥ : ArithmeticSentence) := (Sh_provable_iff _).mp h
    simp at h₁

/-- 影子扩张 𝗥₀（来自 `arithInterp : 𝗭𝗙𝗖 ⊳ 𝗥₀`）。 -/
instance R0_le_Sh : 𝗥₀ ⪯ Sh :=
  Entailment.weakerThan_iff.mpr fun h ↦ (Sh_provable_iff _).mpr (arithInterp.of_provability h)

/-- **Z0 的条件形式**：若 𝗭𝗙𝗖 的算术影子可枚举、且扩张 𝗜𝚺₁，则 𝗭𝗙𝗖 证明不了
“这个影子（的 Craig 公理化）不矛盾”的翻译。 -/
theorem zfc_z0_conditional [Sh.RE] [𝗜𝚺₁ ⪯ Sh] :
    𝗭𝗙𝗖 ⊬ arithTrln.translate (Sh.craig.consistent.val) := fun h ↦
  craig_consistent_unprovable_of_RE Sh ((Sh_provable_iff _).mpr h)

/-- 同一结论的影子形式：影子自己证明不了它的一致性句。 -/
theorem sh_z0_conditional [Sh.RE] [𝗜𝚺₁ ⪯ Sh] : Sh ⊬ Sh.craig.consistent.val :=
  craig_consistent_unprovable_of_RE Sh

end GodelQ.ZFCZ0

#print axioms GodelQ.ZFCZ0.Sh_provable_iff
#print axioms GodelQ.ZFCZ0.Sh_consistent
#print axioms GodelQ.ZFCZ0.R0_le_Sh
#print axioms GodelQ.ZFCZ0.zfc_z0_conditional
#print axioms GodelQ.ZFCZ0.sh_z0_conditional
