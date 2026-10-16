import GodelQ.ZFC.Z0Full
import GodelQ.ZFC.Z0PA
import Foundation.FirstOrder.Incompleteness.StandardProvability

/-!
# Z0-D3 攻坚骨架（2026-10-10，Codex 会话 01a120e6）

**这个文件我本机编译通过（exit 0）**：Lean 4.34.0 + Foundation `1fb01b72`
+ 本 repo 的 24 个 GodelQ 模块。

它把"我可以确定成立的部分"全部落成可编译引理，把唯一的缺口写成 `gap`。
你的工作：把 `gap` 证掉（或把卡点写清楚）。

**怎么用**：复制这个文件到
`HoTT/formal/claude-cg001/godel-q-zfc-z0-full/GodelQ/ZFC/Z0D3Skeleton.lean`，
按 `BUILD.md` 的次序编译，然后改。

注意：本文件会进入收据源，所以**不得有 `sorry`**。
现在 `gap` 用 `sorry` 占位只是为了让你看到形状；证完请删掉这一行。
-/



open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCZ0 GodelQ.Z0Full

namespace Z0D3Skeleton

/-! ## 第 1 部分：Craig 化 —— 本机实测可合成 -/

/-- `Sh.RE`（C-119）经 Foundation 的 Craig 化给出 Δ1 公理表示。 -/
noncomputable example : (Sh.craig : ArithmeticTheory).Δ₁ := inferInstance

/-- Craig 化保持 𝗣𝗔⁻。 -/
noncomputable example : 𝗣𝗔⁻ ⪯ Sh.craig := inferInstance

/-- Craig 化双向弱于原理论（故等价）。 -/
example : Sh.craig ⪯ Sh := inferInstance
example : Sh ⪯ Sh.craig := inferInstance

lemma shCraig_iff (σ : ArithmeticSentence) : Sh.craig ⊢ σ ↔ Sh ⊢ σ := by
  refine ⟨fun h ↦ ?_, fun h ↦ ?_⟩
  · exact Entailment.weakerThan_iff.mp (inferInstance : Sh.craig ⪯ Sh) h
  · exact Entailment.weakerThan_iff.mp (inferInstance : Sh ⪯ Sh.craig) h

/-- **本轮核心发现**：`Sh.craig` 的标准可证性谓词满足全部 HBL 条件，包括 D3。
这条 `inferInstance` 能成功，意味着 Foundation 的 `provable_D3` 可以直接用在 `Sh.craig` 上。 -/
noncomputable example : (Sh.craig.standardProvability).HBL3 := inferInstance

/-- Foundation 的形式化 Σ1 完全性对 `Sh.craig` 可用。 -/
lemma sigma1_complete_craig (σ : ArithmeticSentence) (hσ : ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 σ) :
    𝗜𝚺₁ ⊢ σ 🡒 provabilityPred Sh.craig σ :=
  FFL.FirstOrder.Arithmetic.provable_sigma_one_complete hσ

/-! ## 第 2 部分：语义层桥 —— 本机实测可证 -/

/-- `V ⊧ provabilityPred Sh.craig σ ↔ Provable Sh.craig ⌜σ⌝`。 -/
lemma models_provabilityPred_craig {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (σ : ArithmeticSentence) :
    V↓[ℒₒᵣ] ⊧ (↑(provabilityPred (Theory.craig Sh) σ) : Sentence ℒₒᵣ) ↔
      Provable Sh.craig (⌜σ⌝ : V) := by
  rw [models_iff]
  simp [provabilityPred,
    (inferInstance : 𝚺ᴬ₁-Predicate (Provable Sh.craig : V → Prop) via (provable Sh.craig)).iff]

/-- **`step1`（本机实测可证）**：`zfcTr` 的语义给出 `Sh.craig` 的推导编码。 -/
theorem step1 {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (σ : ArithmeticSentence)
    (h : V↓[ℒₒᵣ] ⊧ zfcTr σ) : Provable Sh.craig (⌜zfcTr σ⌝ : V) :=
  Bootstrapping.Arithmetic.sigma_one_complete (T := Sh.craig) (zfcTr_sigma1 σ) h

/-! ## 第 3 部分：唯一缺口 -/

/-- **GAP = 唯一缺口**。
`zfcTr` 与 `Sh.craig` 的标准可证性谓词在 𝗜𝚺₁ 中可证等价。
一旦成立，`zfcTr.HBL3` 由 `Provability.ext` 从 Foundation 的 `provable_D3` 组合得到，
完整形式 `𝗭𝗙𝗂 ⊬ arithTrln.translate (𝗭𝗙𝗢.consistent)` 立即随之成立。

卡点（我的判断）：`Provable 𝗭𝗙́ ⌜σᵗ⌝ (V) ↔ Provable Sh.craig ⌜σ⌝ (V)` 的右→左方向
需要 V 层的推导消去；`Provable.sound` 只在 ℕ 层。 -/
lemma gap (σ : ArithmeticSentence) :
    𝗜𝚺₁ ⊢ (↑(zfcTr σ) 🡘 (↑(provabilityPred (Theory.craig Sh) σ) : Sentence ℒₒᵣ)) := by
  sorry

end Z0D3Skeleton
